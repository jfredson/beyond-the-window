#!/usr/bin/env python3
"""Tests for scripts/compute.py and scripts/export.py. Run: python3 scripts/test_compute.py

Every record in this file is a constructed example, made up to exercise a rule. None is real
data, and none describes anything any developer does.
"""
from __future__ import annotations

import copy
import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compute as c  # noqa: E402
import export as x  # noqa: E402

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
        self.assertEqual(h["words"], "1 thing that lies past the limits an AI model ordinarily "
                                     "works within is offered today by at least one developer of AI models")

    def test_the_headline_carries_no_total(self):
        # Ruled 2026-11-18 (docs/rulings/2026-11-18-home-page-count.md): a count, no fraction.
        recs = [good("one-thing", offered=True), good("another-thing", offered=True),
                good("a-third-thing"), good("a-fourth-thing"), good("a-fifth-thing")]
        out = c.compute(recs)
        h = out["headline"]
        self.assertEqual(sorted(h), ["count", "offered_ids", "words"])
        self.assertTrue(h["words"].startswith("2 things that lie past "))
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
            self.assertTrue(c.write_headline(path, two, today="2026-11-19"))
            hist = json.loads(path.read_text())["history"]
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


if __name__ == "__main__":
    unittest.main(verbosity=1)
