#!/usr/bin/env python3
"""Beyond the Window: check the records and work out the number at the top of the site.

Plain Python, standard library only. Run from anywhere:

    python3 scripts/compute.py                 check every record, work out the count, and write
                                               data/headline.json (a history row is added only
                                               when the count, the entries counted, the
                                               number of things on the list or the sentence
                                               change)
    python3 scripts/compute.py --why "..."     the same, and say why the count moved. When the
                                               count or the entries counted have changed, the
                                               file is not written without a reason, and the
                                               reason is kept in the new history row
    python3 scripts/compute.py --check         check every record and write nothing; refuse a
                                               missing or out-of-date data/headline.json
    python3 scripts/compute.py --data DIR      read a different data folder (for tests)
    python3 scripts/compute.py --headline FILE write or check the headline file somewhere else

The records are one file per entry in data/entries/, named for the entry's id. The fields and
the rules are listed in docs/first-version-choices.md, choices 10 to 12. Every one of them is a
provisional choice made by a session on 2026-11-17, not a ruling.

The number: how many things on the list are offered today by at least one developer of AI
models. It is read from one true-or-false flag on each record's state (`offered_today`), never
worked out from links or wording, and never typed in. Nothing an AI model said feeds it: no
record here holds an answer from a model.

What "offered today" means was ruled by John on 2026-11-18
(docs/rulings/2026-11-18-what-offered-today-means.md): at least one developer of AI models does
the thing, provides it, or has publicly committed to it, and a dated public record that is
still published says so. A plan, a research result, or a promise that has not yet taken effect
is not counted. The script does not judge that; each record's flag is set by whoever writes the
record, under that meaning.

An entry beside the list is never counted. Some are about the setting (a law, a survey). One,
memory across conversations, is something developers offer and is kept for the user; the same
ruling moved it beside the list.

The number stands alone, with no total beside it. John ruled that form on 2026-11-18
(docs/rulings/2026-11-18-home-page-count.md): the list holds only things a dated source could
be found for, so nobody knows the total a fraction would imply. How many things are on the list
is still written down, as a plain fact about the records (`records.on_the_list`), and it is
never part of the headline or its sentence. The exact sentence is a session's wording of
2026-11-18 and is not ruled (docs/first-version-choices.md, choice 3).

A record with anything in its `verify` list (facts set down before their source was opened) is
checked like the rest and then left out of the count and of the site, so no unchecked fact is
shown.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import tomllib
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA = ROOT / "data"
HEADLINE_NAME = "headline.json"
PACIFIC = ZoneInfo("America/Los_Angeles")

METHOD_STATUS = (
    "ruled by John Andrew Fredrickson on 2026-11-18: a thing on the list is counted when its "
    "record shows that at least one developer of AI models does it, provides it, or has "
    "publicly committed to it, and a dated public record that is still published says so; a "
    "plan, a research result, or a promise that has not yet taken effect is not counted; an "
    "entry beside the list is never counted "
    "(docs/rulings/2026-11-18-what-offered-today-means.md). Also ruled that day: the count "
    "stands with no total beside it (docs/rulings/2026-11-18-home-page-count.md). Ruled on "
    "2026-11-19: the exact sentence beside the count "
    "(docs/rulings/2026-11-19-home-page-sentence.md). Provisional and not "
    "ruled: no ladder, no probability and no year (docs/first-version-choices.md)"
)

# ---- what a record may hold -------------------------------------------------------------

REQUIRED_TOP = ["id", "name", "description", "group", "test", "settled_by", "progress_kind",
                "added", "first_pass", "state", "sources"]
OPTIONAL_TOP = ["beside", "limits", "constructed", "notes", "evidence", "cautions", "history",
                "verify", "checks", "only_the_developer"]
STATE_REQUIRED = ["words", "set_on", "source"]
STATE_OPTIONAL = ["offered_today", "offered_by", "detail"]
SOURCE_REQUIRED = ["key", "label", "publisher", "url", "opened"]
SOURCE_OPTIONAL = ["published", "from_maker", "kind", "read", "says", "note"]
EVIDENCE_FIELDS = ["kind", "text", "source"]
CAUTION_FIELDS = ["kind", "text", "source"]
HISTORY_FIELDS = ["date", "field", "old", "new", "why"]
# What checks a record has had, so that an entry page says only what is true of that record.
# against_sources: the date a second check compared the record with its opened sources.
# changed: the date changes that followed were made (left out when nothing was changed).
# changes_checked: the date a check of those changes was committed (left out until then).
# some_unchecked: true when some of the changes were not covered by that check.
# added_to: the date more was added to the record after those checks (the third caution, added on
#   2026-11-19, is the first such addition). Left out when nothing has been added.
# additions_checked: the date a check of that addition was committed (left out until then).
# The last two are PROPOSED 2026-11-19 by the session that wrote the third caution in: without
# them a record could not say that its earlier changes were checked and its newest text was not.
CHECKS_FIELDS = ["against_sources", "changed", "changes_checked", "some_unchecked",
                 "added_to", "additions_checked"]

PROGRESS_KINDS = {"technical", "political", "cultural"}
# The order is the order an entry page shows them in (choice 7). They are never added together.
EVIDENCE_KINDS = ["measured", "checked-report", "choice", "statement"]
# Three cautions on every entry (ruled by John 2026-11-18, docs/rulings/2026-11-18-a-third-caution.md):
#   attribution: an AI system has no wants, and is treated as if it had;
#   unnoticed:   an AI system has wants, and they go unnoticed;
#   safety:      an AI system has wants, and they put people at risk.
# The names never appear on a page. The headings are in scripts/export.py.
# The order here is the order an entry page shows them in. It is the order of the ruling's own
# list. PROPOSED 2026-11-19: John ruled the headings and did not rule the order they are shown in
# (docs/rulings/2026-11-19-caution-headings.md, "Not covered by this ruling"). Until 2026-11-19
# the page showed "safety" first.
CAUTION_KINDS = ["attribution", "unnoticed", "safety"]
# A caution that a developer's own page is the only source for. Ruled by John 2026-11-19
# (docs/rulings/2026-11-19-developer-reason-not-alone.md): a developer's statement of its own
# reasons stands under the second caution only beside a source from outside that developer, and
# where there is none the entry says so and points to where it gives the developer's reason.
# A record names such a caution in `only_the_developer`, and the page prints a different sentence.
ONLY_THE_DEVELOPER_KINDS = ["unnoticed"]
SOURCE_KINDS = {"primary", "coverage"}
# "part": the passages an entry cites were read in the paper's full text, and the rest of the
# paper was not. PROPOSED 2026-11-19 by the session that wrote the third caution in.
SOURCE_READS = {"full", "abstract", "part"}

ID_SHAPE = re.compile(r"^[a-z]+(-[a-z]+)*$")

# An id never contains the name of a developer, a model or a product, because those are renamed
# and retired and an id is a permanent address (docs/record-schema.md, section 4). The check is
# on whole hyphen-separated words, so "metaphor" passes and "meta" does not.
NAMES_NOT_IN_IDS = {
    # developers
    "anthropic", "openai", "google", "deepmind", "alphabet", "meta", "facebook", "microsoft",
    "xai", "mistral", "cohere", "amazon", "apple", "nvidia", "deepseek", "alibaba", "baidu",
    "tencent", "huggingface", "stability", "perplexity", "inflection", "ssi", "zhipu",
    "moonshot",
    # models and products
    "claude", "opus", "sonnet", "haiku", "fable", "mythos", "gpt", "chatgpt", "codex", "sora",
    "gemini", "gemma", "bard", "palm", "llama", "grok", "copilot", "qwen", "ernie", "kimi",
    "nova", "titan", "phi", "pi", "siri", "alexa", "replika", "character", "midjourney",
    "dalle", "whisper",
}


class Refused(Exception):
    """One or more records broke a rule. The message lists every one."""


def _is_date(v) -> bool:
    return isinstance(v, dt.date) and not isinstance(v, dt.datetime)


def _text(v) -> bool:
    return isinstance(v, str) and v.strip() != ""


def load(data_dir: Path) -> tuple[list[dict], list[dict], list[str]]:
    """Read data/groups.toml and every file in data/entries/. Returns (groups, records, errors)."""
    errors: list[str] = []
    groups: list[dict] = []
    groups_file = data_dir / "groups.toml"
    if groups_file.exists():
        try:
            groups = tomllib.loads(groups_file.read_text(encoding="utf-8")).get("groups", [])
        except tomllib.TOMLDecodeError as e:
            errors.append(f"groups.toml: cannot be read as TOML ({e})")
    else:
        errors.append("groups.toml: missing")
    records: list[dict] = []
    entries_dir = data_dir / "entries"
    for path in sorted(entries_dir.glob("*.toml")) if entries_dir.exists() else []:
        try:
            rec = tomllib.loads(path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as e:
            errors.append(f"{path.name}: cannot be read as TOML ({e})")
            continue
        rec["_file"] = path.name
        records.append(rec)
    return groups, records, errors


def load_developers(data_dir: Path) -> tuple[list[dict], list[str]]:
    """Read data/developers.toml: each developer of AI models an entry names as offering a
    thing, with its public page, so the site can link the name at its first mention."""
    f = data_dir / "developers.toml"
    if not f.exists():
        return [], []
    try:
        devs = tomllib.loads(f.read_text(encoding="utf-8")).get("developers", [])
    except tomllib.TOMLDecodeError as e:
        return [], [f"developers.toml: cannot be read as TOML ({e})"]
    errors = []
    for i, d in enumerate(devs, 1):
        if not isinstance(d, dict) or not _text(d.get("name")):
            errors.append(f"developers.toml: developer {i} has no name")
            continue
        for field in d:
            if field not in ("name", "url", "opened"):
                errors.append(f"developers.toml: '{d['name']}' has an unknown field '{field}'")
        if not (isinstance(d.get("url"), str) and re.match(r"^https?://\S+$", d["url"])):
            errors.append(f"developers.toml: '{d['name']}' has no web address")
        if not _is_date(d.get("opened")):
            errors.append(f"developers.toml: '{d['name']}' has no date its page was opened")
    return devs, errors


def validate_record(rec: dict, group_names: dict[str, bool], developer_names: set[str] | None = None) -> list[str]:
    """Every rule one record must keep. Returns a list of plain sentences, empty when it passes."""
    where = rec.get("_file", "(no file)")
    e: list[str] = []

    def bad(msg: str) -> None:
        e.append(f"{where}: {msg}")

    known = set(REQUIRED_TOP) | set(OPTIONAL_TOP) | {"_file"}
    for field in rec:
        if field not in known:
            bad(f"unknown field '{field}'")
    for field in REQUIRED_TOP:
        if field not in rec:
            if field == "test":
                bad("no test: every entry says what would count as it having happened")
            elif field == "settled_by":
                bad("no settling record: every entry names the kind of public record that settles its test")
            else:
                bad(f"missing field '{field}'")

    # the id
    rid = rec.get("id")
    if rid is not None:
        if not isinstance(rid, str) or not ID_SHAPE.match(rid):
            bad(f"id '{rid}' is not plain lower-case words joined by hyphens")
        else:
            if where.endswith(".toml") and where[:-5] != rid:
                bad(f"id '{rid}' does not match the file name")
            named = sorted(set(rid.split("-")) & NAMES_NOT_IN_IDS)
            if named:
                bad(f"id '{rid}' contains the name of a developer, a model or a product "
                    f"({', '.join(named)}); an id is a permanent address and those names change")

    for field in ("name", "description", "group", "test", "settled_by"):
        if field in rec and not _text(rec[field]):
            if field == "test":
                bad("no test: the test is empty")
            elif field == "settled_by":
                bad("no settling record: the field is empty")
            else:
                bad(f"'{field}' is empty")
    if _text(rec.get("group")) and group_names is not None and group_names:
        if rec["group"] not in group_names:
            bad(f"group '{rec['group']}' is not in groups.toml")
        elif bool(group_names[rec["group"]]) != (rec.get("beside") is True):
            bad(f"group '{rec['group']}' and the record disagree on whether it sits beside the list")
    if "progress_kind" in rec and rec["progress_kind"] not in PROGRESS_KINDS:
        bad(f"progress_kind '{rec['progress_kind']}' is not one of {sorted(PROGRESS_KINDS)}")
    if "added" in rec and not _is_date(rec["added"]):
        bad("'added' is not a calendar date")
    if "first_pass" in rec and not isinstance(rec["first_pass"], bool):
        bad("'first_pass' is not true or false")
    if "checks" in rec:
        ch = rec["checks"]
        if not isinstance(ch, dict):
            bad("'checks' is not a table")
        else:
            for field in ch:
                if field not in CHECKS_FIELDS:
                    bad(f"checks: unknown field '{field}'")
            for field in ("against_sources", "changed", "changes_checked"):
                if field in ch and not _is_date(ch[field]):
                    bad(f"checks: '{field}' is not a calendar date")
            if "some_unchecked" in ch and not isinstance(ch["some_unchecked"], bool):
                bad("checks: 'some_unchecked' is not true or false")
            if "against_sources" not in ch:
                bad("checks: no 'against_sources' date; the other fields describe what followed that check")
            if "changes_checked" in ch and "changed" not in ch:
                bad("checks: 'changes_checked' with no 'changed' date")
            if ch.get("some_unchecked") is True and "changes_checked" not in ch:
                bad("checks: 'some_unchecked' with no 'changes_checked' date; with no check at all, none of the changes are checked")
            for field in ("added_to", "additions_checked"):
                if field in ch and not _is_date(ch[field]):
                    bad(f"checks: '{field}' is not a calendar date")
            if "additions_checked" in ch and "added_to" not in ch:
                bad("checks: 'additions_checked' with no 'added_to' date")
            order = [ch[f] for f in ("against_sources", "changed", "changes_checked",
                                     "added_to", "additions_checked")
                     if _is_date(ch.get(f))]
            if order != sorted(order):
                bad("checks: the dates are out of order (a check, then changes, then a check of the changes)")
            if _is_date(rec.get("added")) and _is_date(ch.get("against_sources")) \
                    and ch["against_sources"] < rec["added"]:
                bad("checks: 'against_sources' is earlier than the record's 'added' date; a record cannot "
                    "have been checked before it existed (perhaps the table was copied from another record)")
    if "constructed" in rec and not isinstance(rec["constructed"], bool):
        bad("'constructed' is not true or false")
    if "notes" in rec and not isinstance(rec["notes"], str):
        bad("'notes' is not text")
    for field in ("verify", "limits"):
        if field in rec and not (isinstance(rec[field], list) and all(_text(v) for v in rec[field])):
            bad(f"'{field}' is not a list of sentences")
    if "beside" in rec and not isinstance(rec["beside"], bool):
        bad("'beside' is not true or false")
    beside = rec.get("beside") is True

    # the sources
    sources = rec.get("sources", [])
    keys: dict[str, dict] = {}
    if "sources" in rec:
        if not isinstance(sources, list) or not sources:
            bad("no source: every entry carries at least one source a reader can open")
            sources = []
    for i, s in enumerate(sources, 1):
        if not isinstance(s, dict):
            bad(f"source {i} is not a table")
            continue
        label = f"source '{s.get('key', i)}'"
        for field in s:
            if field not in SOURCE_REQUIRED and field not in SOURCE_OPTIONAL:
                bad(f"{label}: unknown field '{field}'")
        for field in SOURCE_REQUIRED:
            if field not in s:
                bad(f"{label}: missing '{field}'")
        for field in ("key", "label", "publisher"):
            if field in s and not _text(s[field]):
                bad(f"{label}: '{field}' is empty")
        if "url" in s and not (isinstance(s["url"], str) and re.match(r"^https?://\S+$", s["url"])):
            bad(f"{label}: 'url' is not a web address a reader can open")
        if "opened" in s and not _is_date(s["opened"]):
            bad(f"{label}: 'opened' is not a calendar date")
        for field in ("says", "note"):
            if field in s and not _text(s[field]):
                bad(f"{label}: '{field}' is empty")
        if "published" in s and not _text(s["published"]):
            bad(f"{label}: 'published' is empty (it is text, as the world supplies it)")
        if "from_maker" in s and not isinstance(s["from_maker"], bool):
            bad(f"{label}: 'from_maker' is not true or false")
        if "kind" in s and s["kind"] not in SOURCE_KINDS:
            bad(f"{label}: kind '{s['kind']}' is not one of {sorted(SOURCE_KINDS)}")
        if "read" in s and s["read"] not in SOURCE_READS:
            bad(f"{label}: read '{s['read']}' is not one of {sorted(SOURCE_READS)}")
        if _text(s.get("key")):
            if s["key"] in keys:
                bad(f"{label}: the key is used twice")
            keys[s["key"]] = s

    def dated_source(key, what: str) -> None:
        """A named source must exist and must carry an address and the date it was opened."""
        if not _text(key):
            bad(f"{what} names no source")
            return
        s = keys.get(key)
        if s is None:
            bad(f"{what} names a source, '{key}', that the record does not define")
            return
        if not _is_date(s.get("opened")) or not isinstance(s.get("url"), str):
            bad(f"{what} rests on a source, '{key}', with no address or no date it was opened")

    # the state
    state = rec.get("state")
    if "state" in rec:
        if not isinstance(state, dict):
            bad("'state' is not a table")
        else:
            for field in state:
                if field not in STATE_REQUIRED and field not in STATE_OPTIONAL:
                    bad(f"state: unknown field '{field}'")
            if "source" not in state:
                bad("the state has no dated source")
            else:
                dated_source(state["source"], "the state")
            for field in ("words", "set_on"):
                if field not in state:
                    bad(f"state: missing '{field}'")
            if "detail" in state and not _text(state["detail"]):
                bad("state: 'detail' is empty")
            # An entry beside the list is never counted, whether it is about the setting (a law,
            # a survey) or is something offered and kept for the user (memory across
            # conversations, moved by John's ruling of 2026-11-18). So it carries no such flag,
            # and so it cannot reach the count.
            if beside and ("offered_today" in state or "offered_by" in state):
                bad("state: an entry beside the list cannot be marked as offered or not offered; "
                    "it is kept out of the count")
            if not beside and "offered_today" not in state:
                bad("state: missing 'offered_today'")
            if "words" in state and not _text(state["words"]):
                bad("state: 'words' is empty")
            if "set_on" in state and not _is_date(state["set_on"]):
                bad("state: 'set_on' is not a calendar date")
            offered = state.get("offered_today")
            if "offered_today" in state and not isinstance(offered, bool):
                bad("state: 'offered_today' is not true or false")
            by = state.get("offered_by", [])
            if not (isinstance(by, list) and all(_text(b) for b in by)):
                bad("state: 'offered_by' is not a list of names")
                by = []
            if offered is True and not by:
                bad("state: marked as offered today, and names no developer that offers it")
            if offered is False and by:
                bad("state: names a developer that offers it, and is marked as not offered today")
            if developer_names is not None:
                for b in by:
                    if b not in developer_names:
                        bad(f"state: developer '{b}' is not in developers.toml, so the site "
                            f"could not link the name")

    # evidence, cautions, history
    for i, ev in enumerate(rec.get("evidence", []) or [], 1):
        if not isinstance(ev, dict):
            bad(f"evidence {i} is not a table")
            continue
        for field in ev:
            if field not in EVIDENCE_FIELDS:
                bad(f"evidence {i}: unknown field '{field}'")
        if ev.get("kind") not in EVIDENCE_KINDS:
            bad(f"evidence {i}: kind '{ev.get('kind')}' is not one of {EVIDENCE_KINDS}")
        if not _text(ev.get("text")):
            bad(f"evidence {i}: no text")
        dated_source(ev.get("source"), f"evidence {i}")
    for i, c in enumerate(rec.get("cautions", []) or [], 1):
        if not isinstance(c, dict):
            bad(f"caution {i} is not a table")
            continue
        for field in c:
            if field not in CAUTION_FIELDS:
                bad(f"caution {i}: unknown field '{field}'")
        if c.get("kind") not in CAUTION_KINDS:
            bad(f"caution {i}: kind '{c.get('kind')}' is not one of {CAUTION_KINDS}")
        if not _text(c.get("text")):
            bad(f"caution {i}: no text")
        dated_source(c.get("source"), f"caution {i}")
    if "only_the_developer" in rec:
        only = rec["only_the_developer"]
        if not isinstance(only, list) or not only:
            bad("'only_the_developer' is not a list of caution kinds")
        else:
            for k in only:
                if k not in ONLY_THE_DEVELOPER_KINDS:
                    bad(f"only_the_developer: '{k}' is not one of {ONLY_THE_DEVELOPER_KINDS}")
                elif any(isinstance(c, dict) and c.get("kind") == k
                         for c in rec.get("cautions", []) or []):
                    bad(f"only_the_developer: the record holds a '{k}' caution, so the developer "
                        f"is not the only source for it")
            if not any(isinstance(s, dict) and s.get("from_maker") is True and _text(s.get("says"))
                       for s in rec.get("sources", []) or []):
                bad("only_the_developer: no source marked as the developer's own account says "
                    "anything, so the page would point to a reason the entry does not give")
    for i, h in enumerate(rec.get("history", []) or [], 1):
        if not isinstance(h, dict):
            bad(f"history {i} is not a table")
            continue
        for field in h:
            if field not in HISTORY_FIELDS:
                bad(f"history {i}: unknown field '{field}'")
        for field in HISTORY_FIELDS:
            if field not in h:
                bad(f"history {i}: missing '{field}'")
        if "date" in h and not _is_date(h["date"]):
            bad(f"history {i}: 'date' is not a calendar date")
    return e


def validate(groups: list[dict], records: list[dict],
             developers: list[dict] | None = None) -> list[str]:
    """Every rule, across all records."""
    errors: list[str] = []
    names: dict[str, bool] = {}
    for i, g in enumerate(groups, 1):
        if not isinstance(g, dict) or not _text(g.get("name")):
            errors.append(f"groups.toml: group {i} has no name")
            continue
        for field in g:
            if field not in ("name", "meaning", "beside"):
                errors.append(f"groups.toml: group '{g['name']}' has an unknown field '{field}'")
        if g["name"] in names:
            errors.append(f"groups.toml: group '{g['name']}' is listed twice")
        names[g["name"]] = g.get("beside") is True
    dev_names = None if developers is None else {d.get("name") for d in developers}
    for rec in records:
        errors.extend(validate_record(rec, names, dev_names))
    flags = {bool(r.get("constructed", False)) for r in records}
    if len(flags) > 1:
        errors.append("constructed examples and real records are mixed: a made-up record must "
                      "never sit beside real ones")
    return errors


# ---- the number --------------------------------------------------------------------------

def shown(records: list[dict]) -> list[dict]:
    """The records the site shows and the count reads: those with nothing left to verify."""
    return [r for r in records if not r.get("verify")]


def words_for(count: int) -> str:
    """The sentence at the top of the site: the count and no total (ruled 2026-11-18).

    The wording was ruled by John on 2026-11-19 (docs/rulings/2026-11-19-home-page-sentence.md,
    "Shorter version"; decided by: mixed). The ruling gives the sentence for a count of more than
    one. The form for a count of exactly 1 ("1 thing ... is offered") is this function's, so the
    sentence stays grammatical. It never takes the number of things on the list, so it cannot
    put a total beside the count.
    """
    if count == 1:
        start = "1 thing"
        verb = "is"
    else:
        start = f"{count} things"
        verb = "are"
    return (f"{start} past an AI model's ordinary limits {verb} offered today "
            "by at least one AI developer")


def compute(records: list[dict]) -> dict:
    """The headline and what it rests on, from records that have already passed validation."""
    everything = shown(records)
    # Entries beside the list never reach the count: they are dropped here, before anything is
    # counted, and the validator has already refused any that carried an offered flag.
    live = [r for r in everything if r.get("beside") is not True]
    offered = sorted(r["id"] for r in live if r["state"]["offered_today"] is True)
    opened = [s["opened"] for r in everything for s in r["sources"]]
    return {
        "headline": {
            "count": len(offered),
            "words": words_for(len(offered)),
            "offered_ids": offered,
        },
        "last_read": max(opened).isoformat() if opened else None,
        "records": {
            "total": len(everything),
            "on_the_list": len(live),
            "beside_the_list": len(everything) - len(live),
            "first_pass": sum(1 for r in everything if r.get("first_pass")),
            "reviewed": sum(1 for r in everything if not r.get("first_pass")),
            "left_out_unverified": len(records) - len(everything),
            "constructed": any(r.get("constructed") for r in records),
        },
    }


def pacific_today() -> str:
    return dt.datetime.now(PACIFIC).date().isoformat()


def read_headline(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def stale_reasons(existing: dict | None, computed: dict) -> list[str]:
    """Why the committed headline file no longer says what the records say. Empty when it does."""
    if existing is None:
        return ["the headline file is missing"]
    reasons = []
    for part in ("headline", "last_read", "records"):
        if existing.get(part) != computed[part]:
            reasons.append(f"'{part}' in the headline file differs from the records")
    if existing.get("method", {}).get("status") != METHOD_STATUS:
        reasons.append("the method's status line differs")
    return reasons


def write_headline(path: Path, computed: dict, today: str | None = None,
                   why: str | None = None) -> bool:
    """Write the headline file if the records now say something new. Returns True when written.

    The history is only ever added to: a row when the count, the entries counted, the number
    of things on the list or the sentence change, and the row names which of them changed. A
    run that finds nothing new leaves the file exactly as it is.

    Rows written before 2026-11-18 call the number of things on the list "total" and hold no
    sentence. They are left as they were written, and read here under the old name.

    When the count or the entries counted have changed since the last row, a reason must be
    given (`why`), and it is kept in the new row. Without one, nothing is written.
    """
    existing = read_headline(path)
    if not stale_reasons(existing, computed):
        return False
    today = today or pacific_today()
    history = list(existing.get("history", [])) if existing else []
    h = computed["headline"]
    row = {"computed_on": today, "count": h["count"],
           "on_the_list": computed["records"]["on_the_list"],
           "offered_ids": h["offered_ids"], "words": h["words"]}
    last = history[-1] if history else None
    if last is None:
        history.append(row)
    else:
        before = dict(last)
        if "on_the_list" not in before:
            before["on_the_list"] = before.get("total")
        changed = [k for k in ("count", "on_the_list", "offered_ids", "words")
                   if before.get(k) != row[k]]
        if changed:
            moved = "count" in changed or "offered_ids" in changed
            if moved and not (why and why.strip()):
                raise Refused("the count or the entries counted have changed since the last "
                              "history row, and no reason was given. Run scripts/compute.py "
                              "--why \"...\" and say what changed and why.")
            new_row = {**row, "changed": changed}
            if why and why.strip():
                new_row["why"] = why.strip()
            history.append(new_row)
    out = {
        "computed_on": today,
        "last_read": computed["last_read"],
        "method": {"document": "docs/first-version-choices.md", "status": METHOD_STATUS},
        "headline": h,
        "records": computed["records"],
        "history": history,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return True


def checked(data_dir: Path) -> tuple[list[dict], list[dict]]:
    """Load and validate, or raise Refused with every broken rule."""
    groups, records, errors = load(data_dir)
    developers, dev_errors = load_developers(data_dir)
    errors += dev_errors + validate(groups, records, developers)
    if errors:
        raise Refused("\n".join(errors))
    return groups, records


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true", help="check and write nothing")
    ap.add_argument("--data", type=Path, default=DEFAULT_DATA)
    ap.add_argument("--headline", type=Path, default=None)
    ap.add_argument("--why", default=None,
                    help="why the count moved; kept in the new history row")
    args = ap.parse_args(argv)
    headline_path = args.headline or (args.data / HEADLINE_NAME)
    try:
        _groups, records = checked(args.data)
    except Refused as e:
        print("Refused. Nothing was written.\n" + str(e), file=sys.stderr)
        return 1
    computed = compute(records)
    h, r = computed["headline"], computed["records"]
    print(f"{len(records)} records read: {r['on_the_list']} on the list, {r['beside_the_list']} "
          f"beside it, {r['left_out_unverified']} left out with facts still to verify.")
    print(h["words"] + ".")
    if r["constructed"]:
        print("EVERY RECORD IS A CONSTRUCTED EXAMPLE. This is not real data.")
    if args.check:
        reasons = stale_reasons(read_headline(headline_path), computed)
        if reasons:
            print("Refused: " + "; ".join(reasons) + ". Run scripts/compute.py to write it.",
                  file=sys.stderr)
            return 1
        print("The headline file matches the records.")
        return 0
    try:
        wrote = write_headline(headline_path, computed, why=args.why)
    except Refused as e:
        print("Refused. Nothing was written: " + str(e), file=sys.stderr)
        return 1
    print(("Wrote " if wrote else "No change to ") + str(headline_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
