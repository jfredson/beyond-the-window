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
never part of the headline or its sentence. The exact sentence was ruled by John on
2026-11-19 (docs/rulings/2026-11-19-home-page-sentence.md).

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
                "verify", "checks", "only_the_developer", "acts", "measures", "searches",
                "done_by", "found"]
STATE_REQUIRED = ["words", "set_on", "source"]
STATE_OPTIONAL = ["offered_today", "offered_by", "detail"]
SOURCE_REQUIRED = ["key", "label", "publisher", "url", "opened"]
SOURCE_OPTIONAL = ["published", "from_maker", "kind", "read", "says", "note", "draft"]
# `draft` (PROPOSED 2026-11-20): true on a source that was added for an act of the rebuild and
# nothing else. Such a source is left off the entry's published page and out of the date the
# record was last read, so that adding it changes no published page. Only an act or a measure
# may rest on it. The flag comes off when the rebuilt pages are published.
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
# corrected: the date corrections were made after the addition (the first are those of 2026-11-19,
#   which followed a check of the additions and a second reading of the sources). Left out when
#   there were none.
# corrections_checked: the date a check of those corrections was committed (left out until then).
# These two are PROPOSED 2026-11-19 by the session that made those corrections, for the same
# reason: a record whose addition was checked, and was then corrected, must be able to say that
# the corrections have not been checked. They are kept apart from the two before them because a
# check of the addition may be dated after the corrections were made.
# fixed: the date fixes were made after the full check before the first release
#   (docs/reviews/2026-11-19-full-check-before-publishing.md). Left out when there were none.
# fixes_checked: the date a check of those fixes was committed (left out until then).
# PROPOSED 2026-11-19, for the same reason as the two before them: the full check confirmed the
# additions and the corrections, and the fixes it asked for are newer text that no check has read.
CHECKS_FIELDS = ["against_sources", "changed", "changes_checked", "some_unchecked",
                 "added_to", "additions_checked", "corrected", "corrections_checked",
                 "fixed", "fixes_checked"]

# ---- the rebuild: dated acts, measures and searches ----------------------------------------
# PROPOSED 2026-11-20 (docs/proposals/2026-11-20-rebuild-design.md, part 1), after John ruled
# that day that the unit of the record becomes a dated act by a named actor
# (docs/rulings/2026-11-20-pursue-the-rebuild.md). The fields are a session's and are not ruled.
#
# An act: who did what, on what date, and the source on this record that says so.
#   date       text, as the source gives it: a day ("2025-11-04"), a month ("2025-05") or a
#              year ("2022")
#   actor      a developer in data/developers.toml, or a named body
#   actor_kind one of ACTOR_KINDS
#   words      what the actor did, written so that it reads after the actor's name, with no
#              full stop and with no developer's name in it (the home page prints a developer's
#              act as "A developer ...", so the words must stand without the name)
#   source     the key of a source already on the record
#   read_on    the day that source was opened again and found to say this. It is kept on the
#              act, so that writing an act never changes a source's own `opened` date
#   withdraws  true when the act takes something back (left out otherwise)
ACT_REQUIRED = ["date", "actor", "actor_kind", "words", "source", "read_on"]
#   about      for an act by someone other than a developer: the developers whose models it is
#              about, so that the table of developers can show it in their places (added
#              2026-11-20 with the measurement of weeks-long tasks)
#   actor_url  the public page of an actor that is not a developer, so the name can be linked
ACT_OPTIONAL = ["withdraws", "about", "actor_url"]
# A place in the table of developers that needs its own plain words: something was found there
# that is not counted (added 2026-11-20, after the check of the rebuilt page). `counts` says
# which of two cases it is:
#   "undecided"  whether it counts is John's to rule and not yet ruled; the place says what
#                was found and that it is not decided
#   "no"         John has ruled, or the ruling on what "offered today" means settles it, and
#                it is not counted; the place says what was found and that it is not counted
# A place that is counted is never written here: it is in the state's `offered_by`. `words` is
# the plain fact, written to follow a date and to stand without a developer's name; `source`
# is a source on the record that says it.
FOUND_REQUIRED = ["developer", "date", "words", "source", "counts"]
FOUND_COUNTS = ["undecided", "no"]
ACTOR_KINDS = ["developer", "lawmaker", "court", "researchers"]
# A measure: one figure from a survey, so that a figure on the home page is read from a record
# and never typed. `words` is the rest of a sentence that opens with the figure. The design
# called this field `of`; it is `words` here because not every figure is a share of a group.
MEASURE_REQUIRED = ["date", "by", "value", "unit", "words", "source", "read_on"]
MEASURE_BY = ["public", "researchers"]
MEASURE_UNITS = ["percent"]
# A search that found nothing: the one thing that lets the grid of developers say "nothing
# found" for a developer and a thing. `words` says what was looked for and where.
SEARCH_REQUIRED = ["date", "developer", "words"]
# Who could do the thing an entry on the list is about. Left out, it is a developer. The grid
# of developers holds only the things a developer could do.
DONE_BY = ["developer", "lawmaker"]
PARTIAL_DATE = re.compile(r"^(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?$")
# The two entries the reading on law is worked out from. Ids are permanent addresses.
LAW_AGAINST_ID = "law-against-legal-personhood"
LAW_PROTECTING_ID = "protection-in-law"

PROGRESS_KINDS = {"technical", "political", "cultural"}
# The order is the order an entry page shows them in (choice 7). They are never added together.
EVIDENCE_KINDS = ["measured", "checked-report", "choice", "statement"]
# Three cautions on every entry (ruled by John 2026-11-18, docs/rulings/2026-11-18-a-third-caution.md):
#   attribution: an AI system has no wants, and is treated as if it had;
#   unnoticed:   an AI system has wants, and they go unnoticed;
#   safety:      an AI system has wants, and they put people at risk.
# The names never appear on a page. The headings are in scripts/export.py.
# The order here is the order an entry page shows them in. John ruled it on 2026-11-19
# (docs/rulings/2026-11-19-order-of-the-three-cautions.md, "Your headings' order"). Until
# 2026-11-19 the page showed "safety" first.
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


def start_of(text) -> dt.date | None:
    """The first day of a date written as a day, a month or a year. None when it is not one."""
    m = PARTIAL_DATE.match(text) if isinstance(text, str) else None
    if not m:
        return None
    try:
        return dt.date(int(m.group(1)), int(m.group(2) or 1), int(m.group(3) or 1))
    except ValueError:
        return None


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
            for field in ("corrected", "corrections_checked"):
                if field in ch and not _is_date(ch[field]):
                    bad(f"checks: '{field}' is not a calendar date")
            if "corrections_checked" in ch and "corrected" not in ch:
                bad("checks: 'corrections_checked' with no 'corrected' date")
            if _is_date(ch.get("corrected")):
                before = [ch[f] for f in ("against_sources", "changed", "added_to") if _is_date(ch.get(f))]
                if before and ch["corrected"] < max(before):
                    bad("checks: 'corrected' is earlier than the check, the changes or the addition "
                        "it corrects")
                if _is_date(ch.get("corrections_checked")) and ch["corrections_checked"] < ch["corrected"]:
                    bad("checks: 'corrections_checked' is earlier than 'corrected'")
            for field in ("fixed", "fixes_checked"):
                if field in ch and not _is_date(ch[field]):
                    bad(f"checks: '{field}' is not a calendar date")
            if "fixes_checked" in ch and "fixed" not in ch:
                bad("checks: 'fixes_checked' with no 'fixed' date")
            if _is_date(ch.get("fixed")):
                before = [ch[f] for f in ("against_sources", "changed", "added_to", "corrected")
                          if _is_date(ch.get(f))]
                if before and ch["fixed"] < max(before):
                    bad("checks: 'fixed' is earlier than something it comes after")
                if _is_date(ch.get("fixes_checked")) and ch["fixes_checked"] < ch["fixed"]:
                    bad("checks: 'fixes_checked' is earlier than 'fixed'")
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
        if "draft" in s and not isinstance(s["draft"], bool):
            bad(f"{label}: 'draft' is not true or false")
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
        if s.get("draft") is True and not what.startswith(("act ", "measure ", "found ")):
            bad(f"{what} rests on a source, '{key}', that is marked as a draft; only an act or "
                f"a measure may, because a draft source is not on the published page")

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
    # acts, measures and searches (the rebuild, PROPOSED 2026-11-20)
    if "done_by" in rec:
        if rec["done_by"] not in DONE_BY:
            bad(f"done_by '{rec['done_by']}' is not one of {DONE_BY}")
        if beside:
            bad("'done_by' on an entry beside the list; it says who could do a thing on the list")
    for field in ("acts", "measures", "searches"):
        if field in rec and not isinstance(rec[field], list):
            bad(f"'{field}' is not a list")
    acts = rec.get("acts", []) if isinstance(rec.get("acts", []), list) else []
    for i, a in enumerate(acts, 1):
        if not isinstance(a, dict):
            bad(f"act {i} is not a table")
            continue
        for field in a:
            if field not in ACT_REQUIRED and field not in ACT_OPTIONAL:
                bad(f"act {i}: unknown field '{field}'")
        if "date" not in a:
            bad(f"act {i}: no date")
        elif start_of(a["date"]) is None:
            bad(f"act {i}: date '{a['date']}' is not a day, a month or a year written as text "
                f"(\"2025-11-04\", \"2025-05\" or \"2022\")")
        if not _text(a.get("actor")):
            bad(f"act {i}: no actor")
        if a.get("actor_kind") not in ACTOR_KINDS:
            bad(f"act {i}: actor_kind '{a.get('actor_kind')}' is not one of {ACTOR_KINDS}")
        elif developer_names is not None and _text(a.get("actor")):
            if a["actor_kind"] == "developer" and a["actor"] not in developer_names:
                bad(f"act {i}: developer '{a['actor']}' is not in developers.toml, so the record "
                    f"does not cover it")
            if a["actor_kind"] != "developer" and a["actor"] in developer_names:
                bad(f"act {i}: '{a['actor']}' is a developer in developers.toml and the act "
                    f"calls it a {a['actor_kind']}")
        if not _text(a.get("words")):
            bad(f"act {i}: no words saying what was done")
        else:
            if a["words"].rstrip().endswith("."):
                bad(f"act {i}: the words end with a full stop; the page adds it")
            for name in sorted(developer_names or []):
                if _text(name) and re.search(rf"\b{re.escape(name)}\b", a["words"]):
                    bad(f"act {i}: the words name a developer ('{name}'); the name belongs in "
                        f"'actor', and the words must stand without it")
        dated_source(a.get("source"), f"act {i}")
        if not _is_date(a.get("read_on")):
            bad(f"act {i}: no 'read_on' date, the day its source was opened again for this act")
        elif start_of(a.get("date")) is not None and start_of(a["date"]) > a["read_on"]:
            bad(f"act {i}: dated after the day its source was read")
        if "withdraws" in a and not isinstance(a["withdraws"], bool):
            bad(f"act {i}: 'withdraws' is not true or false")
        if "actor_url" in a:
            if not (isinstance(a["actor_url"], str) and re.match(r"^https?://\S+$", a["actor_url"])):
                bad(f"act {i}: 'actor_url' is not a web address")
            if a.get("actor_kind") == "developer":
                bad(f"act {i}: 'actor_url' on a developer's act; a developer's page is in developers.toml")
        if "about" in a:
            if not (isinstance(a["about"], list) and a["about"] and all(_text(n) for n in a["about"])):
                bad(f"act {i}: 'about' is not a list of developers")
            else:
                if a.get("actor_kind") == "developer":
                    bad(f"act {i}: 'about' on a developer's own act")
                for n in a["about"]:
                    if developer_names is not None and n not in developer_names:
                        bad(f"act {i}: 'about' names '{n}', which is not in developers.toml")
    # A record that holds acts and is marked as offered by a developer must hold an act by that
    # developer that does not take something back, so the grid can give the cell a date.
    if acts and isinstance(state, dict):
        for b in state.get("offered_by", []) if isinstance(state.get("offered_by", []), list) else []:
            if not any(isinstance(a, dict) and a.get("actor") == b
                       and a.get("actor_kind") == "developer" and a.get("withdraws") is not True
                       for a in acts):
                bad(f"marked as offered by '{b}', and holds no act by that developer")
    for i, m in enumerate(rec.get("measures", []) if isinstance(rec.get("measures", []), list) else [], 1):
        if not isinstance(m, dict):
            bad(f"measure {i} is not a table")
            continue
        for field in m:
            if field not in MEASURE_REQUIRED:
                bad(f"measure {i}: unknown field '{field}'")
        for field in MEASURE_REQUIRED:
            if field not in m:
                bad(f"measure {i}: missing '{field}'")
        if "date" in m and start_of(m["date"]) is None:
            bad(f"measure {i}: date '{m['date']}' is not a day, a month or a year written as text")
        if "by" in m and m["by"] not in MEASURE_BY:
            bad(f"measure {i}: by '{m['by']}' is not one of {MEASURE_BY}")
        if "value" in m and (isinstance(m["value"], bool) or not isinstance(m["value"], (int, float))):
            bad(f"measure {i}: 'value' is not a number")
        if "unit" in m and m["unit"] not in MEASURE_UNITS:
            bad(f"measure {i}: unit '{m['unit']}' is not one of {MEASURE_UNITS}")
        elif m.get("unit") == "percent" and isinstance(m.get("value"), (int, float)) \
                and not isinstance(m["value"], bool) and not 0 <= m["value"] <= 100:
            bad(f"measure {i}: {m['value']} percent is not between 0 and 100")
        if "words" in m and not _text(m["words"]):
            bad(f"measure {i}: 'words' is empty")
        if "source" in m:
            dated_source(m["source"], f"measure {i}")
        if "read_on" in m and not _is_date(m["read_on"]):
            bad(f"measure {i}: 'read_on' is not a calendar date")
    for i, s in enumerate(rec.get("searches", []) if isinstance(rec.get("searches", []), list) else [], 1):
        if not isinstance(s, dict):
            bad(f"search {i} is not a table")
            continue
        for field in s:
            if field not in SEARCH_REQUIRED:
                bad(f"search {i}: unknown field '{field}'")
        if not _is_date(s.get("date")):
            bad(f"search {i}: no calendar date; a search that found nothing is only as good as its date")
        if not _text(s.get("developer")):
            bad(f"search {i}: names no developer; a search made for no one developer cannot fill a cell")
        elif developer_names is not None and s["developer"] not in developer_names:
            bad(f"search {i}: developer '{s['developer']}' is not in developers.toml")
        if not _text(s.get("words")):
            bad(f"search {i}: no words saying what was looked for and where")
        if beside or rec.get("done_by", "developer") != "developer":
            bad(f"search {i}: this entry is not a thing a developer could do, so it has no cell to fill")
    if "found" in rec and not isinstance(rec["found"], list):
        bad("'found' is not a list")
    for i, u in enumerate(rec.get("found", []) if isinstance(rec.get("found", []), list) else [], 1):
        if not isinstance(u, dict):
            bad(f"found {i} is not a table")
            continue
        for field in u:
            if field not in FOUND_REQUIRED:
                bad(f"found {i}: unknown field '{field}'")
        if u.get("counts") not in FOUND_COUNTS:
            bad(f"found {i}: counts '{u.get('counts')}' is not one of {FOUND_COUNTS}")
        if not _text(u.get("developer")):
            bad(f"found {i}: names no developer")
        elif developer_names is not None and u["developer"] not in developer_names:
            bad(f"found {i}: developer '{u['developer']}' is not in developers.toml")
        elif isinstance(state, dict) and u["developer"] in (state.get("offered_by") or []):
            bad(f"found {i}: '{u['developer']}' is already named as offering this; a place "
                f"cannot be both counted and written as found and not counted")
        if start_of(u.get("date")) is None:
            bad(f"found {i}: no date written as a day, a month or a year")
        if not _text(u.get("words")):
            bad(f"found {i}: no words saying plainly what was found")
        else:
            if u["words"].rstrip().endswith("."):
                bad(f"found {i}: the words end with a full stop; the page adds it")
            for name in sorted(developer_names or []):
                if _text(name) and re.search(rf"\b{re.escape(name)}\b", u["words"]):
                    bad(f"found {i}: the words name a developer ('{name}')")
        dated_source(u.get("source"), f"found {i}")
        if beside or rec.get("done_by", "developer") != "developer":
            bad(f"found {i}: this entry is not a thing a developer could do, so it has no place to fill")
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


# ---- the readings (the rebuild, PROPOSED 2026-11-20) ----------------------------------------
# docs/proposals/2026-11-20-rebuild-design.md, part 2. Worked out here and written to the
# headline file beside the count, which is left exactly as it was. The home page reads these
# since 2026-11-20; the page of the list still reads the count.

def _source_for_site(rec: dict, key: str) -> dict:
    s = next(x for x in rec["sources"] if x["key"] == key)
    return {"key": key, "label": s["label"], "publisher": s["publisher"], "url": s["url"],
            "opened": s["opened"].isoformat()}


def all_acts(records: list[dict]) -> list[dict]:
    """Every act in the records shown, newest first. A date that is a month or a year is placed
    at its first day. Each act gets an address made of its entry's id and its date."""
    rows, seen = [], {}
    for r in sorted(shown(records), key=lambda r: r["id"]):
        for a in r.get("acts", []):
            base = f"{r['id']}-{a['date']}"
            seen[base] = seen.get(base, 0) + 1
            rows.append({
                "id": base if seen[base] == 1 else f"{base}-{seen[base]}",
                "entry": r["id"],
                "entry_name": r["name"],
                "date": a["date"],
                "actor": a["actor"],
                "actor_kind": a["actor_kind"],
                "words": a["words"],
                "withdraws": a.get("withdraws") is True,
                "about": list(a.get("about", [])),
                "actor_url": a.get("actor_url"),
                "source": _source_for_site(r, a["source"]),
                "read_on": a["read_on"].isoformat(),
            })
    rows.sort(key=lambda a: start_of(a["date"]), reverse=True)  # stable: ties keep entry order
    return rows


def developer_grid(records: list[dict], developers: list[dict]) -> dict:
    """The developers' reading: every developer the record covers, against every thing on the
    list that a developer could do (ruled 2026-11-20: every covered developer is named,
    docs/rulings/2026-11-20-home-page-names-every-covered-developer.md, and the covered
    developers are those in data/developers.toml,
    docs/rulings/2026-11-20-the-record-covers-three-developers.md).

    A cell is one of five kinds, and the kind is read from the record, never judged here:
      offered        the record's state names the developer as offering the thing; the date is
                     that developer's first act that does not take something back
      unruled        the record holds a `found` place marked "undecided": something was found,
                     and whether it counts is John's to rule and not yet ruled
      not_counted    the record holds a `found` place marked "no", with its own words; or it
                     holds an act by the developer, and does not count the thing as
                     offered (a research result, a plan, or a promise not yet in effect, under
                     the ruling of 2026-11-18 on what "offered today" means)
      taken_back     the developer's newest act on the record takes something back
      nothing_found  no act, and the record holds a search made for that developer and that
                     thing; the date is the newest such search
      not_searched   no act, and no such search
    A cell never says "nothing found" without a search on the record."""
    names = [d["name"] for d in developers]
    things = [r for r in shown(records)
              if r.get("beside") is not True and r.get("done_by", "developer") == "developer"]
    kinds = ["offered", "unruled", "not_counted", "taken_back", "nothing_found", "not_searched"]
    rows = []
    for r in things:
        cells = []
        for name in names:
            acts = sorted((a for a in r.get("acts", [])
                           if a["actor_kind"] == "developer" and a["actor"] == name),
                          key=lambda a: start_of(a["date"]))
            searches = sorted(s["date"] for s in r.get("searches", []) if s["developer"] == name)
            cell = {"developer": name, "kind": "not_searched", "date": None}
            open_ = next((u for u in r.get("found", []) if u["developer"] == name), None)
            if name in r["state"].get("offered_by", []):
                first = next((a for a in acts if a.get("withdraws") is not True), None)
                cell.update(kind="offered", date=first["date"] if first else None)
            elif open_ is not None:
                cell.update(kind="unruled" if open_["counts"] == "undecided" else "not_counted",
                            date=open_["date"], words=open_["words"])
            elif acts and acts[-1].get("withdraws") is True:
                cell.update(kind="taken_back", date=acts[-1]["date"])
            elif acts:
                cell.update(kind="not_counted", date=acts[-1]["date"])
            elif searches:
                cell.update(kind="nothing_found", date=searches[-1].isoformat())
            cells.append(cell)
        rows.append({"entry": r["id"], "name": r["name"], "cells": cells})
    # Things offered by the most developers come first, then those with the most places
    # holding an act, then by name.
    rows.sort(key=lambda row: (-sum(1 for c in row["cells"] if c["kind"] == "offered"),
                               -sum(1 for c in row["cells"]
                                    if c["kind"] in ("unruled", "not_counted", "taken_back")),
                               row["name"].lower()))
    by_developer = []
    for d in developers:
        mine = [c for row in rows for c in row["cells"] if c["developer"] == d["name"]]
        by_developer.append({"name": d["name"], "url": d.get("url"),
                             **{k: sum(1 for c in mine if c["kind"] == k) for k in kinds}})
    return {
        "covered": names,
        "things": len(rows),
        "cells": len(rows) * len(names),
        "offering": sum(1 for d in by_developer if d["offered"] > 0),
        "counts": {k: sum(d[k] for d in by_developer) for k in kinds},
        "by_developer": by_developer,
        "rows": rows,
    }


def law_reading(records: list[dict]) -> dict:
    """Where a lawmaker has passed a law against legal personhood for AI, and whether any
    government has protected an AI system for its own sake. Each half is None when its entry is
    not among the records shown."""
    by_id = {r["id"]: r for r in shown(records)}
    against = protecting = None
    r = by_id.get(LAW_AGAINST_ID)
    if r is not None:
        acts = sorted((a for a in r.get("acts", [])
                       if a["actor_kind"] == "lawmaker" and a.get("withdraws") is not True),
                      key=lambda a: start_of(a["date"]))
        places = []
        for a in acts:
            if a["actor"] not in [p["name"] for p in places]:
                places.append({"name": a["actor"], "date": a["date"]})
        against = {"entry": r["id"], "count": len(places), "places": places,
                   "first": places[0]["date"] if places else None,
                   "latest": places[-1]["date"] if places else None}
    r = by_id.get(LAW_PROTECTING_ID)
    if r is not None:
        places = sorted({a["actor"] for a in r.get("acts", [])
                         if a["actor_kind"] == "lawmaker" and a.get("withdraws") is not True})
        protecting = {"entry": r["id"], "count": len(places), "places": places,
                      "met": r["state"].get("offered_today") is True,
                      "looked_on": r["state"]["set_on"].isoformat()}
    return {"against": against, "protecting": protecting}


def measure_reading(records: list[dict], by: str) -> dict | None:
    """The newest measures by one group (the public, or researchers): every measure that shares
    the newest date. `one_source` is true when every measure by that group rests on one source,
    and then the page says so beside the figure."""
    found = [(r, m) for r in shown(records) for m in r.get("measures", []) if m["by"] == by]
    if not found:
        return None
    newest = max(start_of(m["date"]) for _r, m in found)
    top = [(r, m) for r, m in found if start_of(m["date"]) == newest]
    return {
        "entry": top[0][0]["id"],
        "date": top[0][1]["date"],
        "one_source": len({(r["id"], m["source"]) for r, m in found}) == 1,
        "measures": [{"value": m["value"], "unit": m["unit"], "words": m["words"],
                      "entry": r["id"], "source": _source_for_site(r, m["source"]),
                      "read_on": m["read_on"].isoformat()} for r, m in top],
    }


def readings(records: list[dict], developers: list[dict] | None = None) -> dict:
    acts = all_acts(records)
    return {
        "status": "the readings of the home page since 2026-11-20 "
                  "(docs/proposals/2026-11-20-rebuild-design.md). Which readings stand there, "
                  "and how each is worked out, are provisional choices and not rulings. The "
                  "count above them is worked out as before.",
        "developers": developer_grid(records, developers or []),
        "law": law_reading(records),
        "public": measure_reading(records, "public"),
        "researchers": measure_reading(records, "researchers"),
        "latest": acts[0] if acts else None,
        "acts": acts,
    }


def compute(records: list[dict], developers: list[dict] | None = None) -> dict:
    """The headline and what it rests on, from records that have already passed validation."""
    everything = shown(records)
    # Entries beside the list never reach the count: they are dropped here, before anything is
    # counted, and the validator has already refused any that carried an offered flag.
    live = [r for r in everything if r.get("beside") is not True]
    offered = sorted(r["id"] for r in live if r["state"]["offered_today"] is True)
    # A source added for an act of the rebuild is left out, so the published home page's line
    # on when the record was last read does not move until the rebuilt page is published.
    opened = [s["opened"] for r in everything for s in r["sources"] if s.get("draft") is not True]
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
        "readings": readings(records, developers),
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
    for part in ("headline", "last_read", "records", "readings"):
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
        "readings": computed["readings"],
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
    developers, _ = load_developers(args.data)
    computed = compute(records, developers)
    h, r = computed["headline"], computed["records"]
    print(f"{len(records)} records read: {r['on_the_list']} on the list, {r['beside_the_list']} "
          f"beside it, {r['left_out_unverified']} left out with facts still to verify.")
    print(h["words"] + ".")
    g = computed["readings"]["developers"]
    print(f"{len(computed['readings']['acts'])} dated acts. The grid of developers: "
          f"{g['cells']} cells, " + ", ".join(f"{v} {k.replace('_', ' ')}"
                                             for k, v in g["counts"].items()) + ".")
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
