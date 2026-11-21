#!/usr/bin/env python3
"""Tests for scripts/compute.py, scripts/export.py and the rebuilt home page's part of
scripts/check_site.py. Run: python3 scripts/test_compute.py

Every record in this file is a constructed example, made up to exercise a rule. None is real
data, and none describes anything any developer does.
"""
from __future__ import annotations

import copy
import datetime as dt
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compute as c  # noqa: E402
import export as x  # noqa: E402
import check_site as s  # noqa: E402

D = dt.date(2026, 11, 17)
GROUPS = [{"name": "A constructed group"}]


def good(rid: str = "a-made-up-thing", offered: bool = False) -> dict:
    """A constructed record that passes every rule."""
    rec = {
        "_file": f"{rid}.toml",
        "id": rid,
        "name": "A made-up thing",
        "description": "Constructed for a test.",
        "group": "A constructed group",
        "test": "A constructed test.",
        "settled_by": "A constructed kind of record.",
        "progress_kind": "technical",
        "added": D,
        "first_pass": True,
        "state": {"words": "An idea only", "offered_today": offered, "set_on": D, "source": "s"},
        "sources": [{"key": "s", "label": "Constructed", "publisher": "Nobody",
                     "url": "https://example.com/", "opened": D}],
    }
    if offered:
        rec["state"]["offered_by"] = ["A made-up developer"]
        rec["state"]["words"] = "Offered by one developer"
    return rec


def errs(rec: dict) -> str:
    return "\n".join(c.validate(GROUPS, [rec]))


class Validator(unittest.TestCase):
    def test_a_good_record_passes(self):
        self.assertEqual(errs(good()), "")
        self.assertEqual(errs(good(offered=True)), "")

    def test_refuses_an_unknown_field(self):
        rec = good(); rec["probability"] = 0.4
        self.assertIn("unknown field 'probability'", errs(rec))
        rec = good(); rec["state"]["rung"] = 2
        self.assertIn("state: unknown field 'rung'", errs(rec))
        rec = good(); rec["sources"][0]["trust"] = "high"
        self.assertIn("unknown field 'trust'", errs(rec))

    def test_refuses_a_record_with_no_test(self):
        rec = good(); del rec["test"]
        self.assertIn("no test", errs(rec))
        rec = good(); rec["test"] = "  "
        self.assertIn("no test", errs(rec))

    def test_refuses_a_record_with_no_settling_record(self):
        rec = good(); del rec["settled_by"]
        self.assertIn("no settling record", errs(rec))
        rec = good(); rec["settled_by"] = ""
        self.assertIn("no settling record", errs(rec))

    def test_refuses_a_state_with_no_dated_source(self):
        rec = good(); del rec["state"]["source"]
        self.assertIn("the state has no dated source", errs(rec))
        rec = good(); rec["state"]["source"] = "nowhere"
        self.assertIn("that the record does not define", errs(rec))
        rec = good(); del rec["sources"][0]["opened"]
        self.assertIn("no address or no date it was opened", errs(rec))
        rec = good(); rec["sources"][0]["opened"] = "2026-11-17"  # text, not a date
        self.assertIn("'opened' is not a calendar date", errs(rec))

    def test_refuses_an_id_with_a_developers_models_or_products_name(self):
        for rid in ("anthropic-keeps-the-files", "what-claude-is-told", "a-gpt-store",
                    "memory-in-gemini", "the-llama-files"):
            self.assertIn("contains the name of a developer, a model or a product",
                          errs(good(rid)), rid)
        # whole words only: these are fine
        for rid in ("a-metaphor", "an-opening", "philosophy-of-mind"):
            self.assertEqual(errs(good(rid)), "", rid)

    def test_refuses_an_id_that_is_not_plain_words_or_differs_from_its_file(self):
        self.assertIn("not plain lower-case words", errs(good("Model_Memory2")))
        rec = good(); rec["_file"] = "something-else.toml"
        self.assertIn("does not match the file name", errs(rec))

    def test_offered_today_must_name_who_offers_it(self):
        rec = good(offered=True); rec["state"]["offered_by"] = []
        self.assertIn("names no developer", errs(rec))
        rec = good(); rec["state"]["offered_by"] = ["A made-up developer"]
        self.assertIn("marked as not offered today", errs(rec))

    def test_evidence_and_cautions_need_a_known_kind_and_a_source(self):
        rec = good(); rec["evidence"] = [{"kind": "wanted", "text": "x", "source": "s"}]
        self.assertIn("evidence 1: kind 'wanted'", errs(rec))
        rec = good(); rec["cautions"] = [{"kind": "safety", "text": "x"}]
        self.assertIn("caution 1 names no source", errs(rec))
        rec = good(); rec["cautions"] = [{"kind": "missed", "text": "x", "source": "s"}]
        self.assertIn("caution 1: kind 'missed'", errs(rec))

    def test_there_are_three_cautions_in_the_order_of_the_ruling(self):
        self.assertEqual(c.CAUTION_KINDS, ["attribution", "unnoticed", "safety"])

    def test_only_the_developer_is_refused_beside_a_caution_of_that_kind(self):
        rec = good(); rec["sources"][0]["from_maker"] = True; rec["sources"][0]["says"] = "x"
        rec["only_the_developer"] = ["unnoticed"]
        self.assertEqual(errs(rec), "")
        rec["cautions"] = [{"kind": "unnoticed", "text": "x", "source": rec["sources"][0]["key"]}]
        self.assertIn("is not the only source for it", errs(rec))
        rec = good(); rec["only_the_developer"] = ["safety"]
        self.assertIn("only_the_developer: 'safety' is not one of", errs(rec))
        rec = good(); rec["only_the_developer"] = ["unnoticed"]
        self.assertIn("point to a reason the entry does not give", errs(rec))

    def test_an_addition_is_dated_after_the_checks_before_it(self):
        rec = good(); rec["checks"] = {"against_sources": D, "additions_checked": D}
        self.assertIn("'additions_checked' with no 'added_to' date", errs(rec))

    def test_a_correction_is_dated_after_what_it_corrects_and_before_its_own_check(self):
        later = dt.date(2026, 11, 19)
        rec = good(); rec["checks"] = {"against_sources": D, "corrected": later}
        self.assertEqual(errs(rec), "")
        # a check of the addition may be dated after the corrections were made
        rec["checks"] = {"against_sources": D, "added_to": later, "corrected": later,
                         "additions_checked": dt.date(2026, 11, 20),
                         "corrections_checked": dt.date(2026, 11, 20)}
        self.assertEqual(errs(rec), "")
        rec["checks"] = {"against_sources": D, "corrections_checked": later}
        self.assertIn("'corrections_checked' with no 'corrected' date", errs(rec))
        rec["checks"] = {"against_sources": D, "added_to": later, "corrected": D}
        self.assertIn("'corrected' is earlier than", errs(rec))
        rec["checks"] = {"against_sources": D, "corrected": later, "corrections_checked": D}
        self.assertIn("'corrections_checked' is earlier than 'corrected'", errs(rec))

    def test_a_fix_after_the_full_check_is_dated_and_has_its_own_check(self):
        later = dt.date(2026, 11, 19)
        rec = good(); rec["checks"] = {"against_sources": D, "corrected": later,
                                       "corrections_checked": later, "fixed": later}
        self.assertEqual(errs(rec), "")
        rec["checks"] = {"against_sources": D, "fixes_checked": later}
        self.assertIn("'fixes_checked' with no 'fixed' date", errs(rec))
        rec["checks"] = {"against_sources": D, "corrected": later, "fixed": D}
        self.assertIn("'fixed' is earlier than", errs(rec))
        rec["checks"] = {"against_sources": D, "fixed": later, "fixes_checked": D}
        self.assertIn("'fixes_checked' is earlier than 'fixed'", errs(rec))

    def test_constructed_and_real_records_are_never_mixed(self):
        a, b = good("one-thing"), good("another-thing")
        b["constructed"] = True
        self.assertIn("mixed", "\n".join(c.validate(GROUPS, [a, b])))

    def test_a_developer_named_must_have_a_page_to_link(self):
        rec = good(offered=True)
        devs = [{"name": "Somebody else", "url": "https://example.com/", "opened": D}]
        self.assertIn("is not in developers.toml", "\n".join(c.validate(GROUPS, [rec], devs)))
        devs[0]["name"] = "A made-up developer"
        self.assertEqual(c.validate(GROUPS, [rec], devs), [])

    def test_an_entry_beside_the_list_cannot_carry_an_offered_flag(self):
        groups = GROUPS + [{"name": "The setting", "beside": True}]
        rec = good(); rec["beside"] = True; rec["group"] = "The setting"
        self.assertIn("cannot be marked as offered", "\n".join(c.validate(groups, [rec])))
        del rec["state"]["offered_today"]
        self.assertEqual(c.validate(groups, [rec]), [])
        rec["group"] = "A constructed group"
        self.assertIn("disagree on whether it sits beside", "\n".join(c.validate(groups, [rec])))

    def test_checks_must_be_dated_and_in_order(self):
        rec = good()
        rec["checks"] = {"against_sources": D}
        self.assertEqual(errs(rec), "")
        rec["checks"] = {"against_sources": D, "changed": D, "changes_checked": D, "some_unchecked": True}
        self.assertEqual(errs(rec), "")
        rec["checks"] = {"changed": D}
        self.assertIn("no 'against_sources' date", errs(rec))
        rec["checks"] = {"against_sources": D, "changes_checked": D}
        self.assertIn("'changes_checked' with no 'changed' date", errs(rec))
        rec["checks"] = {"against_sources": D, "changed": D, "some_unchecked": True}
        self.assertIn("'some_unchecked' with no 'changes_checked' date", errs(rec))
        rec["checks"] = {"against_sources": dt.date(2026, 11, 18), "changed": D}
        self.assertIn("out of order", errs(rec))
        rec["checks"] = {"against_sources": D, "when": D}
        self.assertIn("unknown field 'when'", errs(rec))
        rec["checks"] = {"against_sources": D}
        rec["added"] = dt.date(2026, 12, 1)
        self.assertIn("earlier than the record's 'added' date", errs(rec))

    def test_group_must_be_listed(self):
        rec = good(); rec["group"] = "Somewhere else"
        self.assertIn("is not in groups.toml", errs(rec))


class Count(unittest.TestCase):
    def test_counts_the_flag_and_nothing_else(self):
        recs = [good("one-thing", offered=True), good("another-thing"), good("a-third-thing")]
        h = c.compute(recs)["headline"]
        self.assertEqual((h["count"], h["offered_ids"]), (1, ["one-thing"]))
        self.assertEqual(h["words"], "1 thing past an AI model's ordinary limits is offered today "
                                     "by at least one AI developer")

    def test_the_sentence_is_the_one_ruled(self):
        # Ruled 2026-11-19 (docs/rulings/2026-11-19-home-page-sentence.md).
        self.assertEqual(c.words_for(5), "5 things past an AI model's ordinary limits are offered "
                                         "today by at least one AI developer")

    def test_the_headline_carries_no_total(self):
        # Ruled 2026-11-18 (docs/rulings/2026-11-18-home-page-count.md): a count, no fraction.
        recs = [good("one-thing", offered=True), good("another-thing", offered=True),
                good("a-third-thing"), good("a-fourth-thing"), good("a-fifth-thing")]
        out = c.compute(recs)
        h = out["headline"]
        self.assertEqual(sorted(h), ["count", "offered_ids", "words"])
        self.assertTrue(h["words"].startswith("2 things past "))
        self.assertNotIn("5", h["words"])
        self.assertNotRegex(h["words"], r"\d+ of \d+")
        # how many things are on the list stays, as a plain fact about the records
        self.assertEqual(out["records"]["on_the_list"], 5)

    def test_a_record_with_facts_to_verify_is_left_out(self):
        a, b = good("one-thing", offered=True), good("another-thing", offered=True)
        b["verify"] = ["A fact nobody has opened a source for."]
        out = c.compute([a, b])
        self.assertEqual((out["headline"]["count"], out["records"]["on_the_list"]), (1, 1))
        self.assertEqual(out["records"]["left_out_unverified"], 1)

    def test_an_entry_beside_the_list_is_never_counted(self):
        a = good("one-thing", offered=True)
        b = good("a-law-somewhere"); b["beside"] = True; del b["state"]["offered_today"]
        out = c.compute([a, b])
        self.assertEqual((out["headline"]["count"], out["records"]["on_the_list"]), (1, 1))
        self.assertEqual(out["records"]["beside_the_list"], 1)
        # even if a flag were smuggled past the validator, the count would not read it
        b["state"]["offered_today"] = True
        self.assertEqual(c.compute([a, b])["headline"]["offered_ids"], ["one-thing"])

    def test_a_thing_offered_and_kept_for_the_user_sits_beside_the_list_and_is_not_counted(self):
        # Ruled 2026-11-18 (docs/rulings/2026-11-18-what-offered-today-means.md): the record
        # for memory across conversations moves beside the list. A record moved there loses
        # its flag, the count falls by one, and the list is one shorter.
        a, b = good("one-thing", offered=True), good("a-memory-thing", offered=True)
        before = c.compute([a, b])
        self.assertEqual((before["headline"]["count"], before["records"]["on_the_list"]), (2, 2))
        b["beside"] = True
        self.assertIn("cannot be marked as offered or not offered", errs(b))  # the flag must go
        del b["state"]["offered_today"]; b["state"].pop("offered_by", None)
        after = c.compute([a, b])
        self.assertEqual(after["headline"]["offered_ids"], ["one-thing"])
        self.assertEqual((after["headline"]["count"], after["records"]["on_the_list"],
                          after["records"]["beside_the_list"]), (1, 1, 1))

    def test_what_was_said_cannot_move_the_count(self):
        # Evidence of any kind, including a plain statement, changes nothing in the number.
        a = good("one-thing")
        before = c.compute([a])["headline"]
        b = copy.deepcopy(a)
        b["evidence"] = [{"kind": "statement", "text": "Constructed.", "source": "s"},
                         {"kind": "choice", "text": "Constructed.", "source": "s"}]
        self.assertEqual(c.compute([b])["headline"], before)


class HeadlineFile(unittest.TestCase):
    def test_history_is_added_to_and_never_edited(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "headline.json"
            one = c.compute([good("one-thing")])
            self.assertTrue(c.write_headline(path, one, today="2026-11-17"))
            first = path.read_text()
            self.assertFalse(c.write_headline(path, one, today="2026-11-18"))  # nothing new
            self.assertEqual(path.read_text(), first)
            two = c.compute([good("one-thing", offered=True)])
            self.assertEqual(c.stale_reasons(json.loads(first), two)[0],
                             "'headline' in the headline file differs from the records")
            # the count moved, so the file is not written until a reason is given
            with self.assertRaises(c.Refused):
                c.write_headline(path, two, today="2026-11-19")
            self.assertEqual(path.read_text(), first)
            self.assertTrue(c.write_headline(path, two, today="2026-11-19",
                                             why="A developer began to offer the thing."))
            hist = json.loads(path.read_text())["history"]
            self.assertEqual(hist[1]["why"], "A developer began to offer the thing.")
            self.assertEqual([(h["computed_on"], h["count"]) for h in hist],
                             [("2026-11-17", 0), ("2026-11-19", 1)])
            self.assertEqual(hist[0], json.loads(first)["history"][0])
            self.assertEqual(hist[1]["changed"], ["count", "offered_ids", "words"])
            self.assertNotIn("total", hist[1])

    def test_a_row_written_before_the_ruling_is_kept_and_the_new_sentence_gets_its_own_row(self):
        # The file as it stood on 2026-11-17: the old row calls the size of the list "total"
        # and holds no sentence. The first run after the ruling adds one row and edits none.
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "headline.json"
            now = c.compute([good("one-thing", offered=True), good("another-thing")])
            old_row = {"computed_on": "2026-11-17", "count": 1, "total": 2,
                       "offered_ids": ["one-thing"]}
            path.write_text(json.dumps({"computed_on": "2026-11-17", "history": [old_row]}))
            self.assertTrue(c.write_headline(path, now, today="2026-11-18"))
            hist = json.loads(path.read_text())["history"]
            self.assertEqual(hist[0], old_row)
            self.assertEqual(len(hist), 2)
            self.assertEqual(hist[1]["changed"], ["words"])
            self.assertEqual((hist[1]["count"], hist[1]["on_the_list"]), (1, 2))

    def test_check_refuses_a_missing_file(self):
        self.assertEqual(c.stale_reasons(None, c.compute([good()])), ["the headline file is missing"])


class Export(unittest.TestCase):
    def test_export_keeps_notes_and_unverified_records_off_the_site(self):
        a, b = good("one-thing", offered=True), good("another-thing")
        a["notes"] = "A working note."
        b["verify"] = ["Unchecked."]
        computed = c.compute([a, b])
        head = {"computed_on": "2026-11-17", "last_read": computed["last_read"],
                "headline": computed["headline"], "records": computed["records"]}
        out = x.build(GROUPS, [a, b], head)
        self.assertEqual([e["id"] for e in out["entries"]], ["one-thing"])
        self.assertNotIn("notes", out["entries"][0])
        self.assertEqual([k["kind"] for k in out["entries"][0]["evidence"]], c.EVIDENCE_KINDS)
        self.assertEqual(out["entries"][0]["sources"][0]["opened"], "2026-11-17")
        self.assertIs(out["entries"][0]["beside"], False)
        self.assertIsNone(out["entries"][0]["checks"])

    def _beside_with_note(self, rulings: Path) -> tuple[list[dict], dict]:
        """A constructed record beside the list, with a note and a constructed ruling that
        holds the note across a line break, inside a quoted passage."""
        (rulings / "2026-01-01-a-constructed-ruling.md").write_text(
            "# A constructed ruling\n\n> A constructed sentence on what the\n> placement rests on.\n",
            encoding="utf-8")
        groups = GROUPS + [{"name": "The setting", "beside": True}]
        noted = good("another-thing"); noted["beside"] = True; noted["group"] = "The setting"
        del noted["state"]["offered_today"]
        noted["placement_note"] = "A constructed sentence on what the placement rests on."
        noted["placement_note_ruling"] = "2026-01-01-a-constructed-ruling.md"
        return groups, noted

    def test_a_record_with_no_placement_note_builds_as_before_and_one_with_it_carries_it(self):
        kept = c.RULINGS_DIR
        with tempfile.TemporaryDirectory() as d:
            c.RULINGS_DIR = Path(d)
            try:
                groups, noted = self._beside_with_note(Path(d))
                plain_rec = good("one-thing", offered=True)
                self.assertEqual(errs(plain_rec), "")
                self.assertEqual(c.validate(groups, [noted]), [])
                computed = c.compute([plain_rec, noted])
                head = {"computed_on": "2026-11-17", "last_read": computed["last_read"],
                        "headline": computed["headline"], "records": computed["records"]}
                out = {e["id"]: e for e in x.build(groups, [plain_rec, noted], head)["entries"]}
                self.assertIsNone(out["one-thing"]["placement_note"])
                self.assertEqual(out["another-thing"]["placement_note"], noted["placement_note"])
                self.assertNotIn("placement_note_ruling", out["another-thing"])
                # The note changes nothing that is counted.
                bare = {k: v for k, v in noted.items() if not k.startswith("placement_note")}
                self.assertEqual(computed["headline"], c.compute([plain_rec, bare])["headline"])
            finally:
                c.RULINGS_DIR = kept

    def test_a_placement_note_is_refused_unless_a_ruling_holds_it_word_for_word(self):
        kept = c.RULINGS_DIR
        with tempfile.TemporaryDirectory() as d:
            c.RULINGS_DIR = Path(d)
            try:
                groups, noted = self._beside_with_note(Path(d))
                said = lambda rec: "\n".join(c.validate(groups, [rec]))
                self.assertEqual(said(noted), "")
                # No ruling named.
                rec = copy.deepcopy(noted); del rec["placement_note_ruling"]
                self.assertIn("'placement_note' with no 'placement_note_ruling'", said(rec))
                # A name that is not a plain file name in the rulings folder.
                rec = copy.deepcopy(noted); rec["placement_note_ruling"] = "../compute.py"
                self.assertIn("'placement_note' with no 'placement_note_ruling'", said(rec))
                # A ruling that does not exist.
                rec = copy.deepcopy(noted); rec["placement_note_ruling"] = "2026-01-02-no-such-ruling.md"
                self.assertIn("docs/rulings/ holds no such file", said(rec))
                # A sentence the ruling does not hold, by one word.
                rec = copy.deepcopy(noted)
                rec["placement_note"] = "A made-up sentence on what the placement rests on."
                self.assertIn("is not found word for word in the ruling it names", said(rec))
                # A ruling named with no note.
                rec = copy.deepcopy(noted); del rec["placement_note"]
                self.assertIn("'placement_note_ruling' with no 'placement_note'", said(rec))
                # On the list, and not a sentence: refused as before.
                on_the_list = good(); on_the_list["placement_note"] = noted["placement_note"]
                on_the_list["placement_note_ruling"] = noted["placement_note_ruling"]
                self.assertIn("'placement_note' on an entry that is not beside the list", errs(on_the_list))
                rec = copy.deepcopy(noted); rec["placement_note"] = ["not", "text"]
                self.assertIn("'placement_note' is not a sentence", said(rec))
            finally:
                c.RULINGS_DIR = kept

    def test_the_real_memory_entry_passes_with_its_real_ruling(self):
        groups, records, problems = c.load(c.ROOT / "data")
        self.assertEqual(problems, [])
        memory = next(r for r in records if r["id"] == "memory-across-conversations")
        self.assertTrue((c.RULINGS_DIR / memory["placement_note_ruling"]).is_file())
        self.assertEqual(c.validate_record(memory, {g["name"]: g.get("beside") is True for g in groups}), [])
        self.assertEqual([r["id"] for r in records if "placement_note" in r], ["memory-across-conversations"])
        # The same record with one word of the sentence changed is refused.
        changed = copy.deepcopy(memory)
        changed["placement_note"] = changed["placement_note"].replace("says nothing", "says little")
        self.assertIn("is not found word for word",
                      "\n".join(c.validate_record(changed, {g["name"]: g.get("beside") is True for g in groups})))




class SecondCautionSources(unittest.TestCase):
    """The About page's sentence on where the second caution's items come from. Ruled by John
    on 2026-11-21: the build stops only when the group it names is no longer the largest single
    source under the second caution. Every record here is constructed."""

    GROUP = "https://eleosai.org/a-constructed-post"

    def _records(self, from_group: int, others: dict[str, int]) -> list[dict]:
        rec = good()
        rec["sources"].append({"key": "g", "label": "Constructed", "publisher": "Nobody",
                               "url": self.GROUP, "opened": D})
        rec["cautions"] = [{"kind": "unnoticed", "text": "Constructed.", "source": "g"}
                           for _ in range(from_group)]
        for n, (url, count) in enumerate(others.items()):
            rec["sources"].append({"key": f"o{n}", "label": "Constructed", "publisher": "Nobody",
                                   "url": url, "opened": D})
            rec["cautions"] += [{"kind": "unnoticed", "text": "Constructed.", "source": f"o{n}"}
                                for _ in range(count)]
        rec["cautions"].append({"kind": "attribution", "text": "Constructed.", "source": "s"})
        self.assertEqual(errs(rec), "")
        return [rec]

    def test_passes_at_twelve_of_twenty_six(self):
        others = {f"https://example.com/{n}": 1 for n in range(12)}
        others["https://example.com/a"] = 2
        records = self._records(12, others)
        self.assertEqual(c.second_caution_sources(records)[:2], (12, 26))
        self.assertIsNone(c.second_caution_problem(records))

    def test_stops_when_another_single_source_equals_the_groups_count(self):
        problem = c.second_caution_problem(self._records(4, {"https://example.com/a": 4}))
        self.assertIn("no longer the largest single source", problem)
        self.assertIn("goes back to John", problem)

    def test_stops_when_another_single_source_passes_the_groups_count(self):
        self.assertIn("no longer the largest single source",
                      c.second_caution_problem(self._records(2, {"https://example.com/a": 3})))

    def test_the_real_records_pass(self):
        _groups, records, problems = c.load(c.ROOT / "data")
        self.assertEqual(problems, [])
        from_group, total, others = c.second_caution_sources(records)
        self.assertGreater(from_group, max(others.values()))
        self.assertIsNone(c.second_caution_problem(records))


class MovedTableDates(unittest.TestCase):
    """A moved "Since" or "By" date in the table of developers needs a history row on its entry
    dated the same day and naming the developer (added 2026-11-21, decided by: agent). These
    tests use the real records, changed in memory only."""

    def setUp(self):
        _groups, self.records, problems = c.load(c.ROOT / "data")
        self.assertEqual(problems, [])
        self.developers, _ = c.load_developers(c.ROOT / "data")
        self.now = c.compute(self.records, self.developers)

    def _cell(self, headline, entry, developer):
        row = next(r for r in headline["readings"]["developers"]["rows"] if r["entry"] == entry)
        return next(x for x in row["cells"] if x["developer"] == developer)

    def test_openais_corrected_cell_passes_with_its_history_row(self):
        before = copy.deepcopy(self.now)
        cell = self._cell(before, "ending-a-conversation", "OpenAI")
        self.assertEqual((cell["date"], cell.get("by")), ("2026-11-20", True))
        cell["date"] = "2026-10-30"; del cell["by"]  # as it stood before the correction
        self.assertEqual(c.table_date_problems(before, self.now, self.records, "2026-11-21"), [])
        # The same move on another day, with no row of that day, is refused.
        self.assertTrue(c.table_date_problems(before, self.now, self.records, "2026-11-22"))

    def test_an_announcement_mark_with_no_history_row_is_refused(self):
        recs = copy.deepcopy(self.records)
        rec = next(r for r in recs if r["id"] == "welfare-assessment-at-release")
        first = min((a for a in rec["acts"] if a["actor"] == "Anthropic"),
                    key=lambda a: c.start_of(a["date"]))
        first["announces"] = True
        later = c.compute(recs, self.developers)
        problems = c.table_date_problems(self.now, later, recs, "2026-11-21")
        self.assertEqual(len(problems), 1)
        self.assertIn("Anthropic's date on 'welfare-assessment-at-release'", problems[0])

    def test_a_new_seen_in_effect_act_with_no_history_row_is_refused(self):
        recs = copy.deepcopy(self.records)
        rec = next(r for r in recs if r["id"] == "kept-files-of-retired-models")
        for a in rec["acts"]:
            if a["actor"] == "Anthropic":
                a["seen_in_effect"] = True
        later = c.compute(recs, self.developers)
        self.assertEqual(self._cell(later, "kept-files-of-retired-models", "Anthropic").get("by"), True)
        problems = c.table_date_problems(self.now, later, recs, "2026-11-21")
        self.assertEqual(len(problems), 1)
        self.assertIn("moves from Since", problems[0])
        # With a row of that day naming the developer, it passes.
        rec["history"] = list(rec.get("history", [])) + [{
            "date": dt.date(2026, 11, 21), "field": "Anthropic's date in the table of developers",
            "old": "x", "new": "y", "why": "Constructed for a test."}]
        self.assertEqual(c.table_date_problems(self.now, later, recs, "2026-11-21"), [])

    def test_no_committed_file_means_nothing_to_compare(self):
        self.assertEqual(c.table_date_problems(None, self.now, self.records, "2026-11-21"), [])


class FirstCautionSources(unittest.TestCase):
    """The About page's sentence on where the first caution's items come from. Ruled by John on
    2026-11-20: the build stops only when the writer it names is no longer the largest single
    source under the first caution. Every record here is constructed."""

    WRITER = "https://mustafa-suleyman.ai/a-constructed-essay"

    def _records(self, from_writer: int, others: dict[str, int]) -> list[dict]:
        rec = good()
        rec["sources"].append({"key": "w", "label": "Constructed", "publisher": "Nobody",
                               "url": self.WRITER, "opened": D})
        rec["cautions"] = [{"kind": "attribution", "text": "Constructed.", "source": "w"}
                           for _ in range(from_writer)]
        for n, (url, count) in enumerate(others.items()):
            rec["sources"].append({"key": f"o{n}", "label": "Constructed", "publisher": "Nobody",
                                   "url": url, "opened": D})
            rec["cautions"] += [{"kind": "attribution", "text": "Constructed.", "source": f"o{n}"}
                                for _ in range(count)]
        # An item under another caution is never counted here.
        rec["cautions"].append({"kind": "unnoticed", "text": "Constructed.", "source": "s"})
        self.assertEqual(errs(rec), "")
        return [rec]

    def test_passes_at_nine_of_twenty_four_spread_over_other_sources(self):
        others = {f"https://example.com/{n}": 1 for n in range(11)}
        others.update({"https://example.com/a": 2, "https://example.com/b": 2})
        records = self._records(9, others)
        self.assertEqual(c.first_caution_sources(records)[:2], (9, 24))
        self.assertIsNone(c.first_caution_problem(records))

    def test_passes_below_half_while_the_writer_is_still_the_largest(self):
        self.assertIsNone(c.first_caution_problem(self._records(3, {"https://example.com/a": 2,
                                                                    "https://example.com/b": 2,
                                                                    "https://example.com/c": 2})))

    def test_stops_when_another_single_source_equals_the_writers_count(self):
        problem = c.first_caution_problem(self._records(9, {"https://example.com/a": 9,
                                                            "https://example.com/b": 1}))
        self.assertIn("no longer the largest single source", problem)
        self.assertIn("goes back to John", problem)
        self.assertIn("https://example.com/a", problem)

    def test_stops_when_another_single_source_passes_the_writers_count(self):
        self.assertIn("no longer the largest single source",
                      c.first_caution_problem(self._records(2, {"https://example.com/a": 3})))

    def test_the_real_records_pass_and_give_the_about_pages_figures(self):
        _groups, records, problems = c.load(c.ROOT / "data")
        self.assertEqual(problems, [])
        from_writer, total, others = c.first_caution_sources(records)
        # The About page's figures as the records give them: 9 of 25 since 2026-11-21, when
        # Sean Richey's essay was added (docs/rulings/2026-11-21-richeys-essay-is-added.md).
        self.assertEqual((from_writer, total), (9, 25))
        self.assertLess(max(others.values()), from_writer)
        self.assertIsNone(c.first_caution_problem(records))
        c.checked(c.ROOT / "data")  # the build's own way in, which would raise if it stopped


# ---- the rebuild: acts, measures, searches and the readings (PROPOSED 2026-11-20) -----------

DEVS = [{"name": "A made-up developer", "url": "https://example.com/a", "opened": D},
        {"name": "Another made-up developer", "url": "https://example.com/b", "opened": D}]


def act(date: str = "2026-03-02", actor: str = "A made-up developer", kind: str = "developer",
        **more) -> dict:
    """A constructed act that passes every rule."""
    return {"date": date, "actor": actor, "actor_kind": kind,
            "words": "does a made-up thing", "source": "s", "read_on": D, **more}


def measure(value=40, by: str = "public", date: str = "2025") -> dict:
    return {"date": date, "by": by, "value": value, "unit": "percent",
            "words": "of made-up people said a made-up thing", "source": "s", "read_on": D}


def errs_with(rec: dict) -> str:
    return "\n".join(c.validate(GROUPS, [rec], DEVS))


class Acts(unittest.TestCase):
    def test_a_record_with_acts_measures_and_a_search_passes(self):
        rec = good(offered=True)
        rec["acts"] = [act(), act("2022", "A made-up state", "lawmaker"), act("2025-05")]
        rec["measures"] = [measure()]
        rec["searches"] = [{"date": D, "developer": "Another made-up developer",
                            "words": "A constructed search."}]
        self.assertEqual(errs_with(rec), "")

    def test_an_act_needs_a_date_an_actor_and_a_kind(self):
        for field, said in (("date", "no date"), ("actor", "no actor"),
                            ("actor_kind", "is not one of"), ("words", "no words"),
                            ("read_on", "no 'read_on' date")):
            rec = good(); a = act(); del a[field]; rec["acts"] = [a]
            self.assertIn(said, errs_with(rec), field)
        rec = good(); rec["acts"] = [act(date="March 2026")]
        self.assertIn("is not a day, a month or a year", errs_with(rec))
        rec = good(); rec["acts"] = [act(date="2026-13")]
        self.assertIn("is not a day, a month or a year", errs_with(rec))
        rec = good(); rec["acts"] = [act(kind="company")]
        self.assertIn("is not one of", errs_with(rec))
        rec = good(); rec["acts"] = [act(certainty="high")]
        self.assertIn("unknown field 'certainty'", errs_with(rec))

    def test_an_act_rests_on_a_source_on_its_record_that_has_been_opened(self):
        rec = good(); rec["acts"] = [act(source="nowhere")]
        self.assertIn("names a source, 'nowhere', that the record does not define", errs_with(rec))
        rec = good(); del rec["sources"][0]["opened"]; rec["acts"] = [act()]
        self.assertIn("act 1 rests on a source, 's', with no address or no date", errs_with(rec))
        rec = good(); rec["acts"] = [act(date="2027-01-01")]
        self.assertIn("dated after the day its source was read", errs_with(rec))

    def test_a_source_added_for_an_act_stays_off_the_published_pages(self):
        rec = good()
        rec["sources"].append({"key": "new", "label": "Constructed", "publisher": "Nobody",
                               "url": "https://example.com/new", "opened": dt.date(2026, 11, 20),
                               "draft": True})
        rec["acts"] = [act(source="new")]
        self.assertEqual(errs_with(rec), "")
        # the date the record was last read does not move, and the entry page does not list it
        self.assertEqual(c.compute([rec], DEVS)["last_read"], "2026-11-17")
        entry = x.entry_for_site(rec, {})
        self.assertEqual([s["key"] for s in entry["sources"]], ["s"])
        self.assertEqual(c.all_acts([rec])[0]["source"]["url"], "https://example.com/new")
        # nothing a published page prints may rest on it
        rec["state"]["source"] = "new"
        self.assertIn("the state rests on a source, 'new', that is marked as a draft", errs_with(rec))

    def test_a_developer_who_acts_must_be_one_the_record_covers(self):
        rec = good(); rec["acts"] = [act(actor="A developer nobody listed")]
        self.assertIn("is not in developers.toml, so the record does not cover it", errs_with(rec))
        rec = good(); rec["acts"] = [act(kind="researchers")]
        self.assertIn("is a developer in developers.toml and the act calls it a researchers",
                      errs_with(rec))

    def test_the_words_of_an_act_stand_without_a_developers_name(self):
        rec = good(); a = act(); a["words"] = "does what Another made-up developer did"
        rec["acts"] = [a]
        self.assertIn("the words name a developer", errs_with(rec))
        rec = good(); a = act(); a["words"] = "does a made-up thing."
        rec["acts"] = [a]
        self.assertIn("end with a full stop", errs_with(rec))

    def test_a_thing_marked_as_offered_holds_an_act_by_that_developer(self):
        rec = good(offered=True); rec["acts"] = [act(actor="Another made-up developer")]
        self.assertIn("holds no act by that developer", errs_with(rec))
        rec = good(offered=True); rec["acts"] = [act(withdraws=True)]
        self.assertIn("holds no act by that developer", errs_with(rec))

    def test_a_measure_is_a_number_with_a_source(self):
        rec = good(); m = measure("seventeen"); rec["measures"] = [m]
        self.assertIn("'value' is not a number", errs_with(rec))
        rec = good(); rec["measures"] = [measure(140)]
        self.assertIn("is not between 0 and 100", errs_with(rec))
        rec = good(); rec["measures"] = [measure(by="everyone")]
        self.assertIn("by 'everyone' is not one of", errs_with(rec))
        rec = good(); m = measure(); m["source"] = "nowhere"; rec["measures"] = [m]
        self.assertIn("measure 1 names a source", errs_with(rec))

    def test_a_search_names_one_developer_and_a_date(self):
        rec = good(); rec["searches"] = [{"date": D, "words": "A constructed search."}]
        self.assertIn("names no developer", errs_with(rec))
        rec = good(); rec["searches"] = [{"developer": "A made-up developer", "words": "x"}]
        self.assertIn("no calendar date", errs_with(rec))
        rec = good(); rec["searches"] = [{"date": D, "developer": "Nobody listed", "words": "x"}]
        self.assertIn("is not in developers.toml", errs_with(rec))
        rec = good(); rec["done_by"] = "lawmaker"
        rec["searches"] = [{"date": D, "developer": "A made-up developer", "words": "x"}]
        self.assertIn("is not a thing a developer could do", errs_with(rec))


class Readings(unittest.TestCase):
    def records(self) -> list[dict]:
        offered = good("a-thing-offered", offered=True)
        offered["acts"] = [act("2026-03-02"), act("2025-05")]
        studied = good("a-thing-studied")
        studied["acts"] = [act("2025-10")]
        back = good("a-thing-taken-back")
        back["acts"] = [act("2024-01-01"), act("2026-01-29", withdraws=True)]
        searched = good("a-thing-searched-for")
        searched["searches"] = [{"date": dt.date(2026, 11, 1), "developer": "A made-up developer",
                                 "words": "A constructed search."},
                                {"date": D, "developer": "A made-up developer",
                                 "words": "A constructed search."}]
        law = good("a-thing-for-lawmakers"); law["done_by"] = "lawmaker"
        return [offered, studied, back, searched, law]

    def test_each_cell_of_the_grid_is_read_from_the_record(self):
        recs = self.records()
        self.assertEqual(c.validate(GROUPS, recs, DEVS), [])
        g = c.developer_grid(recs, DEVS)
        self.assertEqual(g["covered"], ["A made-up developer", "Another made-up developer"])
        cells = {row["entry"]: row["cells"] for row in g["rows"]}
        first = {entry: (cs[0]["kind"], cs[0]["date"]) for entry, cs in cells.items()}
        self.assertEqual(first["a-thing-offered"], ("offered", "2025-05"))
        self.assertEqual(first["a-thing-studied"], ("not_counted", "2025-10"))
        self.assertEqual(first["a-thing-taken-back"], ("taken_back", "2026-01-29"))
        self.assertEqual(first["a-thing-searched-for"], ("nothing_found", "2026-11-17"))
        # the second developer did nothing and was searched for nothing
        self.assertEqual({cs[1]["kind"] for cs in cells.values()}, {"not_searched"})
        self.assertEqual(g["offering"], 1)
        self.assertEqual(g["counts"], {"offered": 1, "unruled": 0, "not_counted": 1,
                                       "taken_back": 1, "nothing_found": 1, "not_searched": 4})

    def test_an_announcement_is_skipped_and_a_change_seen_in_effect_is_marked_by(self):
        # Added 2026-11-21 (docs/rulings/2026-11-21-openai-date-corrected.md). Constructed.
        recs = self.records()
        recs[0]["acts"] = [act("2025-05", announces=True), act("2026-03-02", seen_in_effect=True)]
        self.assertEqual(c.validate(GROUPS, recs, DEVS), [])
        cell = {row["entry"]: row["cells"] for row in c.developer_grid(recs, DEVS)["rows"]}["a-thing-offered"][0]
        self.assertEqual((cell["kind"], cell["date"], cell.get("by")), ("offered", "2026-03-02", True))
        # The announcement is still an act: the page of acts and the feed show it.
        self.assertIn("2025-05", [a["date"] for a in c.all_acts(recs)])

    def test_without_the_seen_in_effect_mark_the_cell_says_since(self):
        recs = self.records()
        recs[0]["acts"] = [act("2025-05", announces=True), act("2026-03-02")]
        cell = {row["entry"]: row["cells"] for row in c.developer_grid(recs, DEVS)["rows"]}["a-thing-offered"][0]
        self.assertEqual((cell["date"], "by" in cell), ("2026-03-02", False))
        # and with no marks at all the first act gives the date, as before
        self.assertNotIn("by", {row["entry"]: row["cells"] for row in
                                c.developer_grid(self.records(), DEVS)["rows"]}["a-thing-offered"][0])

    def test_the_two_marks_are_refused_where_they_make_no_sense(self):
        said = lambda acts: "\n".join(c.validate(GROUPS, [dict(self.records()[0], acts=acts)], DEVS))
        self.assertIn("both 'announces' and 'seen_in_effect'",
                      said([act("2025-05", announces=True, seen_in_effect=True), act("2026-03-02")]))
        self.assertIn("'announces' is set and is not true", said([act("2025-05", announces=False)]))
        self.assertIn("'seen_in_effect' on an act that takes something back",
                      said([act("2025-05"), act("2026-03-02", withdraws=True, seen_in_effect=True)]))
        self.assertIn("'announces' on an act that is not a developer's",
                      said([act("2025-05"), act("2026-03-02", actor="Some researchers", kind="researchers",
                                                announces=True, about=["A made-up developer"])]))
        # An entry offered by a developer whose only act is an announcement has no day it began.
        self.assertIn("not an announcement or a withdrawal", said([act("2025-05", announces=True)]))

    def test_a_place_found_and_not_counted_says_so_in_its_own_words(self):
        recs = self.records()
        recs[1]["found"] = [{"developer": "A made-up developer", "date": "2026-11-20",
                             "words": "a made-up thing is in effect", "source": "s",
                             "counts": "undecided"}]
        recs[3]["found"] = [{"developer": "Another made-up developer", "date": "2026-04",
                             "words": "an outside group reports a made-up result", "source": "s",
                             "counts": "no"}]
        self.assertEqual(c.validate(GROUPS, recs, DEVS), [])
        g = c.developer_grid(recs, DEVS)
        cells = {row["entry"]: row["cells"] for row in g["rows"]}
        self.assertEqual((cells["a-thing-studied"][0]["kind"], cells["a-thing-studied"][0]["words"]),
                         ("unruled", "a made-up thing is in effect"))
        # once it is ruled not to count, the place keeps its own words and says so
        self.assertEqual((cells["a-thing-searched-for"][1]["kind"], cells["a-thing-searched-for"][1]["words"]),
                         ("not_counted", "an outside group reports a made-up result"))
        self.assertEqual(g["counts"]["unruled"], 1)
        self.assertEqual(c.compute(recs, DEVS)["headline"]["count"], 1)
        # it cannot stand where the thing is already counted, and it needs a source
        recs[0]["found"] = [{"developer": "A made-up developer", "date": "2026",
                             "words": "x", "source": "nowhere", "counts": "perhaps"}]
        said = "\n".join(c.validate(GROUPS, recs, DEVS))
        self.assertIn("cannot be both counted and written as found and not counted", said)
        self.assertIn("found 1 names a source", said)
        self.assertIn("counts 'perhaps' is not one of", said)

    def test_an_act_by_researchers_can_say_whose_models_it_is_about(self):
        rec = good(); rec["acts"] = [act(actor="A made-up group", kind="researchers",
                                         about=["A made-up developer"],
                                         actor_url="https://example.com/group")]
        self.assertEqual(errs_with(rec), "")
        self.assertEqual(c.all_acts([rec])[0]["about"], ["A made-up developer"])
        rec["acts"][0]["about"] = ["Nobody listed"]
        self.assertIn("'about' names 'Nobody listed'", errs_with(rec))
        rec = good(); rec["acts"] = [act(about=["Another made-up developer"])]
        self.assertIn("'about' on a developer's own act", errs_with(rec))

    def test_a_thing_for_lawmakers_is_not_a_row_of_the_grid(self):
        g = c.developer_grid(self.records(), DEVS)
        self.assertNotIn("a-thing-for-lawmakers", [row["entry"] for row in g["rows"]])
        self.assertEqual((g["things"], g["cells"]), (4, 8))

    def test_nothing_found_is_never_said_without_a_search(self):
        recs = [good("one-thing"), good("another-thing")]
        g = c.developer_grid(recs, DEVS)
        self.assertEqual(g["counts"]["nothing_found"], 0)
        self.assertEqual(g["counts"]["not_searched"], 4)
        # a search for one developer fills that developer's cell and no other
        recs[0]["searches"] = [{"date": D, "developer": "Another made-up developer", "words": "x"}]
        kinds = [cell["kind"] for cell in c.developer_grid(recs, DEVS)["rows"][1]["cells"]] \
            + [cell["kind"] for cell in c.developer_grid(recs, DEVS)["rows"][0]["cells"]]
        self.assertEqual(sorted(kinds), ["not_searched"] * 3 + ["nothing_found"])

    def test_acts_are_listed_newest_first_and_the_latest_is_the_first(self):
        r = c.readings(self.records(), DEVS)
        dates = [a["date"] for a in r["acts"]]
        self.assertEqual(dates, ["2026-03-02", "2026-01-29", "2025-10", "2025-05", "2024-01-01"])
        self.assertEqual(r["latest"]["id"], "a-thing-offered-2026-03-02")
        self.assertEqual(len({a["id"] for a in r["acts"]}), len(r["acts"]))
        self.assertEqual(r["acts"][0]["source"]["url"], "https://example.com/")

    def test_the_law_reading_counts_places_and_not_acts(self):
        against = good(c.LAW_AGAINST_ID); against["state"].pop("offered_today")
        against["beside"] = True
        against["acts"] = [act("2022", "A made-up state", "lawmaker"),
                           act("2024", "A made-up state", "lawmaker"),
                           act("2023", "Another made-up state", "lawmaker"),
                           act("2025", "A third made-up state", "lawmaker", withdraws=True)]
        protecting = good(c.LAW_PROTECTING_ID); protecting["done_by"] = "lawmaker"
        law = c.law_reading([against, protecting])
        self.assertEqual(law["against"]["count"], 2)
        self.assertEqual((law["against"]["first"], law["against"]["latest"]), ("2022", "2023"))
        self.assertEqual((law["protecting"]["count"], law["protecting"]["met"]), (0, False))
        self.assertEqual(c.law_reading([good()]), {"against": None, "protecting": None})

    def test_a_measure_reading_is_the_newest_and_says_when_it_rests_on_one_source(self):
        a = good("one-thing"); a["measures"] = [measure(20, date="2023"), measure(17, date="2024")]
        b = good("another-thing"); b["measures"] = [measure(1, "researchers", "2024"),
                                                    measure(70, "researchers", "2024")]
        public = c.measure_reading([a, b], "public")
        self.assertEqual([m["value"] for m in public["measures"]], [17])
        self.assertIs(public["one_source"], True)
        self.assertEqual([m["value"] for m in c.measure_reading([a, b], "researchers")["measures"]],
                         [1, 70])
        b["measures"].append(measure(5, "public", "2022"))
        self.assertIs(c.measure_reading([a, b], "public")["one_source"], False)
        self.assertIsNone(c.measure_reading([good()], "public"))

    def test_the_readings_leave_the_count_as_it_was(self):
        recs = self.records()
        self.assertEqual(c.compute(recs, DEVS)["headline"], c.compute(recs)["headline"])
        self.assertEqual(c.compute(recs, DEVS)["headline"]["count"], 1)

    def test_a_record_with_facts_to_verify_gives_no_act_and_no_cell(self):
        recs = self.records(); recs[0]["verify"] = ["Unchecked."]
        r = c.readings(recs, DEVS)
        self.assertNotIn("a-thing-offered", [a["entry"] for a in r["acts"]])
        self.assertNotIn("a-thing-offered", [row["entry"] for row in r["developers"]["rows"]])

    def test_the_headline_file_is_stale_when_the_readings_change(self):
        recs = self.records()
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "headline.json"
            c.write_headline(path, c.compute(recs, DEVS), today="2026-11-20")
            self.assertEqual(c.stale_reasons(c.read_headline(path), c.compute(recs, DEVS)), [])
            recs[1]["acts"].append(act("2026-04-04"))
            self.assertIn("'readings' in the headline file differs from the records",
                          c.stale_reasons(c.read_headline(path), c.compute(recs, DEVS)))
            # an act that leaves the count alone adds no row to the history
            before = len(c.read_headline(path)["history"])
            c.write_headline(path, c.compute(recs, DEVS), today="2026-11-21")
            self.assertEqual(len(c.read_headline(path)["history"]), before)


# ---- the check of the built site: the rebuilt home page (rule 7 of scripts/check_site.py) ----

def built_site(folder: Path, rd: dict, change=lambda home: home) -> Path:
    """A constructed built site, as small as the check allows: a home page that shows the
    readings, a page of acts and a feed. `change` edits the home page before it is written."""
    g = rd["developers"]
    fig = lambda key, value: f'<span data-figure="{key}">{value}</span>'
    names = "".join(f"<li>{d['name']} {fig('developers.' + d['name'] + '.offered', d['offered'])}</li>"
                    for d in g["by_developer"])
    rows = "".join(
        f'<tr data-entry="{row["entry"]}"><th>{row["name"]}</th>' + "".join(
            f'<td data-dev="{c_["developer"]}" data-kind="{c_["kind"]}"'
            + (f' data-date="{c_["date"]}"' if c_["date"] else " data-date") + ">x</td>"
            for c_ in row["cells"]) + "</tr>" for row in g["rows"])
    acts = "".join(f'<li data-act="{a["id"]}" data-date="{a["date"]}">'
                   f'<a href="{a["source"]["url"]}">source</a></li>' for a in rd["acts"])
    measures = "".join(fig(f"{who}.{i}", m["value"]) for who in ("public", "researchers")
                       for i, m in enumerate((rd[who] or {}).get("measures", [])))
    home = (f'<ul data-developers-reading>{names}</ul>'
            f'{fig("developers.covered", len(g["covered"]))}{fig("developers.things", g["things"])}'
            f'{fig("developers.cells", g["cells"])}'
            f'{fig("developers.nothing_found", g["counts"]["nothing_found"])}'
            f'{fig("law.against.count", rd["law"]["against"]["count"])}{measures}'
            f'<table data-developers-reading><tr><th>Thing</th>'
            + "".join(f"<th>{n}</th>" for n in g["covered"]) + f'</tr>{rows}</table>'
            f'{fig("acts.count", len(rd["acts"]))}<ul>{acts}</ul>')
    (folder / "acts").mkdir(parents=True)
    (folder / "index.html").write_text(change(home), encoding="utf-8")
    (folder / "acts" / "index.html").write_text(
        f'{fig("acts.count", len(rd["acts"]))}<ul>{acts}</ul>', encoding="utf-8")
    (folder / "acts.xml").write_text("<feed>" + "<entry></entry>" * len(rd["acts"]) + "</feed>",
                                     encoding="utf-8")
    return folder


class SiteCheck(unittest.TestCase):
    def readings(self) -> dict:
        recs = Readings().records()
        against = good(c.LAW_AGAINST_ID); against["state"].pop("offered_today")
        against["beside"] = True
        against["acts"] = [act("2022", "A made-up state", "lawmaker")]
        survey = good("a-made-up-survey")
        survey["measures"] = [measure(17), measure(1, "researchers"), measure(70, "researchers")]
        return json.loads(json.dumps(c.readings(recs + [against, survey], DEVS)))

    def problems(self, change=lambda home: home, rd_change=lambda rd: None) -> str:
        rd = self.readings()
        with tempfile.TemporaryDirectory() as d:
            site = built_site(Path(d) / "dist", rd, change)
            rd_change(rd)
            return "\n".join(s.rebuilt_problems(site, rd))

    def test_a_home_page_that_shows_the_served_readings_passes(self):
        self.assertEqual(self.problems(), "")

    def test_a_figure_on_the_page_must_equal_the_served_figure(self):
        wrong = lambda home: home.replace('data-figure="law.against.count">1<',
                                          'data-figure="law.against.count">2<')
        self.assertIn("the figure 'law.against.count' reads \"2\"", self.problems(wrong))
        self.assertEqual(s.as_number("three"), 3)
        self.assertEqual(s.as_number(" 17% "), 17)
        self.assertIsNone(s.as_number("several"))

    def test_a_figure_the_page_must_carry_cannot_be_left_unmarked(self):
        gone = lambda home: home.replace('<span data-figure="acts.count">', "<span>")
        self.assertIn("the figure 'acts.count' is not on the page, or is not marked",
                      self.problems(gone))

    def test_a_place_cannot_say_nothing_found_unless_the_served_file_does(self):
        claimed = lambda home: home.replace('data-kind="not_searched" data-date',
                                            'data-kind="nothing_found" data-date="2026-11-20"', 1)
        self.assertIn("the table of developers does not show what the served file holds",
                      self.problems(claimed))

    def test_the_acts_listed_are_the_acts_served_in_order(self):
        dropped = lambda home: home.replace('<li data-act="a-thing-offered-2026-03-02"', '<li', 1)
        self.assertIn("the acts listed are not the acts in the served file", self.problems(dropped))

    def test_every_covered_developer_is_named_in_the_developers_reading(self):
        alone = lambda home: home.replace("<th>Another made-up developer</th>", "<th></th>")
        self.assertIn("does not name Another made-up developer", self.problems(alone))

    def test_a_served_act_needs_a_date_an_actor_and_an_opened_source(self):
        def strip(rd):
            rd["acts"][0]["source"]["opened"] = None
            rd["acts"][1]["actor"] = "A developer nobody listed"
        said = self.problems(rd_change=strip)
        self.assertIn("lacks a source with an address and the date it was opened", said)
        self.assertIn("is by a developer the record does not cover", said)


class HomeHeadline(unittest.TestCase):
    """Rule 7d of the site check: the first figure on the home page is the count, alone."""
    # Since 2026-11-21 the question opens the page in a row of its own, above the two columns
    # (docs/rulings/2026-11-21-the-question-opens-the-home-page.md).
    GOOD = ('<html><body><div class="hl-head"><p class="eyebrow">A record</p>'
            '<h1 class="question">A question?</h1></div>'
            '<div class="rb-first"><div class="hl-top">'
            '<p class="big-number"><span data-figure="headline.count">5</span></p>'
            '<p class="big-claim">things are counted.</p></div>'
            '<div class="rb-side"><p class="rb-reading"><span data-figure="researchers.0">1</span>%</p>'
            '</div></div></body></html>')

    def test_the_count_alone_and_first_passes(self):
        self.assertEqual(s.headline_problems(self.GOOD, 5), [])

    def test_refuses_a_number_that_is_not_the_count(self):
        self.assertTrue(s.headline_problems(self.GOOD, 6))

    def test_refuses_a_total_beside_the_count(self):
        page = self.GOOD.replace(">5</span></p>", ">5</span><small>of 8</small></p>")
        self.assertTrue(s.headline_problems(page, 5))

    def test_refuses_a_page_whose_top_is_not_the_count(self):
        page = self.GOOD.replace('<p class="big-number"><span data-figure="headline.count">5</span></p>', "")
        self.assertTrue(s.headline_problems(page, 5))

    def test_refuses_another_figure_or_a_reading_before_the_count(self):
        page = self.GOOD.replace('<p class="eyebrow">A record</p>',
                                 '<p class="rb-reading"><span data-figure="law.against.count">4</span></p>')
        self.assertTrue(s.headline_problems(page, 5))

    def test_refuses_an_unmarked_count(self):
        page = self.GOOD.replace(' data-figure="headline.count"', "")
        self.assertTrue(s.headline_problems(page, 5))

    def test_refuses_the_question_inside_the_columns(self):
        # The layout of the first draft of 2026-11-21: on a computer the readings column started
        # beside the question, so a reading stood above the count on the screen.
        page = self.GOOD.replace('<h1 class="question">A question?</h1></div>', '</div>').replace(
            '<div class="hl-top">', '<div class="hl-top"><h1 class="question">A question?</h1>')
        self.assertTrue(any("inside the two columns" in m for m in s.headline_problems(page, 5)))

    def test_refuses_the_count_above_the_question(self):
        page = self.GOOD.replace('<h1 class="question">A question?</h1>', '').replace(
            '</body>', '<h1 class="question">A question?</h1></body>')
        self.assertTrue(any("count stands above the question" in m for m in s.headline_problems(page, 5)))

    def test_refuses_a_page_without_the_question(self):
        page = self.GOOD.replace('<h1 class="question">A question?</h1>', '')
        self.assertTrue(s.headline_problems(page, 5))



class HomeFraction(unittest.TestCase):
    """Rule 7d as PROPOSED on 2026-11-21 (docs/proposals/2026-11-21-headline-fraction.md): the
    count, then "of" and the number of things on the List; the List on the page holds that many
    things; and the list of how both moved is read from the served file's history."""
    BIG = ('<p class="big-number"><span data-figure="headline.count">5</span> '
           '<small> of <span data-figure="records.on_the_list">8</span></small></p>')
    HISTORY = [
        {"computed_on": "2026-11-17", "count": 6, "total": 9, "offered_ids": []},
        {"computed_on": "2026-11-18", "count": 6, "on_the_list": 9, "offered_ids": [], "words": "x"},
        {"computed_on": "2026-11-18", "count": 5, "on_the_list": 8, "offered_ids": []},
        {"computed_on": "2026-11-19", "count": 5, "on_the_list": 8, "offered_ids": [], "words": "y"},
    ]
    ROWS = ('<ol class="hl-history" data-fraction-history>'
            '<li data-date="2026-11-17" data-count="6" data-total="9">November 17th, 2026 '
            '<span class="hl-frac">6 of 9</span> <span class="hl-what">The first count.</span></li>'
            '<li data-date="2026-11-18" data-count="5" data-total="8">November 18th, 2026 '
            '<span class="hl-frac">5 of 8</span> <span class="hl-what">A thing moved.</span></li></ol>')
    LIST = '<section class="below" id="list"><ul>' + "<li>a thing</li>" * 8 + "</ul></section>"

    def page(self) -> str:
        return HomeHeadline.GOOD.replace(
            '<p class="big-number"><span data-figure="headline.count">5</span></p>', self.BIG
        ).replace("</body>", self.ROWS + self.LIST + "</body>")

    def known(self, page: str, count=5, total=8, history=None) -> list[str]:
        return s.fraction_known_problems(page, count, total, self.HISTORY if history is None else history)

    def test_the_fraction_with_the_count_first_passes(self):
        self.assertEqual(s.headline_problems(self.page(), 5, 8), [])
        self.assertEqual(self.known(self.page()), [])

    def test_the_count_alone_is_refused_once_a_total_is_served(self):
        self.assertTrue(s.headline_problems(HomeHeadline.GOOD, 5, 8))

    def test_a_total_that_is_not_the_served_total_is_refused(self):
        self.assertTrue(s.headline_problems(self.page(), 5, 9))
        page = self.page().replace('on_the_list">8<', 'on_the_list">9<')
        self.assertTrue(s.headline_problems(page, 5, 8))

    def test_the_total_first_is_refused(self):
        page = self.page().replace(self.BIG, '<p class="big-number"><span data-figure="records.on_the_list">8</span>'
                                   '<small>of <span data-figure="headline.count">5</span></small></p>')
        self.assertTrue(s.headline_problems(page, 5, 8))

    def test_an_unmarked_total_is_refused(self):
        page = self.page().replace(' data-figure="records.on_the_list"', "")
        self.assertTrue(s.headline_problems(page, 5, 8))

    def test_the_total_must_be_the_number_of_things_the_list_shows(self):
        page = self.page().replace("<li>a thing</li>", "", 1)
        self.assertTrue(any("the List on the page shows 7 things" in m for m in self.known(page)))

    def test_the_history_must_be_the_points_in_the_served_file(self):
        typed = self.page().replace('data-count="6" data-total="9"', 'data-count="6" data-total="10"')
        self.assertTrue(self.known(typed))
        dropped = re.sub(r'<li data-date="2026-11-17".*?</li>', "", self.page())
        self.assertTrue(self.known(dropped))
        reworded = self.page().replace(">6 of 9<", ">six of ten<")
        self.assertTrue(self.known(reworded))
        self.assertTrue(self.known(self.page().replace("data-fraction-history", "")))

    def test_the_history_must_end_at_today(self):
        self.assertTrue(self.known(self.page(), count=4, total=8))

    def test_a_row_where_neither_number_moved_is_not_a_point(self):
        self.assertEqual(s.history_points(self.HISTORY),
                         [("2026-11-17", 6, 9), ("2026-11-18", 5, 8)])

    def test_the_share_is_still_refused_outside_the_two_places(self):
        with tempfile.TemporaryDirectory() as d:
            dist = Path(d)
            (dist / "index.html").write_text(self.page(), encoding="utf-8")
            self.assertEqual(s.fraction_problems(dist, [dist / "index.html"], 5, 8), [])
            (dist / "index.html").write_text(self.page().replace("</body>", "<p>5 of 8 things.</p></body>"),
                                             encoding="utf-8")
            self.assertTrue(s.fraction_problems(dist, [dist / "index.html"], 5, 8))
            # a share written into the reason beside a row is still refused (the check of
            # 2026-11-21, must fix 1)
            (dist / "index.html").write_text(self.page().replace("A thing moved.", "Now 5 of 8."),
                                             encoding="utf-8")
            self.assertTrue(s.fraction_problems(dist, [dist / "index.html"], 5, 8))
            (dist / "about").mkdir()
            (dist / "about" / "index.html").write_text(self.ROWS, encoding="utf-8")
            self.assertTrue(s.fraction_problems(dist, [dist / "about" / "index.html"], 5, 8))


if __name__ == "__main__":
    unittest.main(verbosity=1)
