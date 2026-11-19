#!/usr/bin/env python3
"""Beyond the Window: turn the checked records into the one file the website reads.

Plain Python, standard library only. Run from anywhere:

    python3 scripts/export.py              check the records, refuse an out-of-date headline
                                           file, then write site/src/data/window.json and copy
                                           data/headline.json to site/public/data/headline.json
    python3 scripts/export.py --data DIR   read a different data folder (for tests)
    python3 scripts/export.py --out DIR    write window.json somewhere else
    python3 scripts/export.py --public DIR write the public copy of the headline file elsewhere

This script is the only reader of the data for the site. Every page reads window.json, and the
number at the top of every page comes from the headline file that scripts/compute.py wrote, so
it is the same number everywhere. The export never works the number out again: if the headline
file is missing or no longer matches the records, it stops and says to run compute.py.

A record with facts still to verify is not exported, so the site cannot show an unchecked fact.
A record's working notes are not exported either.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compute as c  # noqa: E402

ROOT = c.ROOT
DEFAULT_OUT = ROOT / "site" / "src" / "data"
DEFAULT_PUBLIC = ROOT / "site" / "public" / "data"

EVIDENCE_HEADINGS = {
    "measured": "Measured without the AI model's own word",
    "checked-report": "Reports checked against an independent reading",
    "choice": "Choices made at a cost",
    "statement": "Plain statements",
}
# The three headings, word for word as John ruled them on 2026-11-19
# (docs/rulings/2026-11-19-caution-headings.md). The same wording on every entry.
CAUTION_HEADINGS = {
    "attribution": "If an AI system has no wants, and is treated as if it had",
    "unnoticed": "If an AI system has wants, and they go unnoticed",
    "safety": "If an AI system has wants, and they put people at risk",
}
# What an entry page prints under a caution that holds nothing. Both sentences are a session's
# draft of 2026-11-19 and are PROPOSED: the rulings of that day say what each must tell the
# reader and leave the exact words to a session and its checker
# (docs/rulings/2026-11-19-memory-entry-nothing-recorded.md,
# docs/rulings/2026-11-19-developer-reason-not-alone.md).
NOTHING_RECORDED = "Nothing recorded yet. No source was found for this caution on this entry."
ONLY_THE_DEVELOPER = ("Nothing recorded yet from anyone but the developer. The developer's own "
                      "reason is given beside its page under Sources, below.")


def _plain(v):
    """TOML values as JSON can hold them: calendar dates become year-month-day text."""
    if isinstance(v, (dt.date, dt.datetime)):
        return v.isoformat()
    if isinstance(v, dict):
        return {k: _plain(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_plain(x) for x in v]
    return v


def commit() -> str | None:
    try:
        out = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True, check=True)
        return out.stdout.strip() or None
    except (OSError, subprocess.CalledProcessError):
        return None


def entry_for_site(rec: dict, developers: dict[str, str]) -> dict:
    sources = {s["key"]: _plain(s) for s in rec["sources"]}
    state = _plain(rec["state"])
    beside = rec.get("beside") is True
    state["offered_today"] = None if beside else rec["state"]["offered_today"]
    state["offered_by"] = [{"name": n, "url": developers.get(n)}
                           for n in rec["state"].get("offered_by", [])]
    state.setdefault("detail", "")
    evidence = []
    for kind in c.EVIDENCE_KINDS:  # always all four, in the stated order, never added together
        evidence.append({
            "kind": kind,
            "heading": EVIDENCE_HEADINGS[kind],
            "items": [{"text": e["text"], "source": e["source"]}
                      for e in rec.get("evidence", []) if e["kind"] == kind],
        })
    only = rec.get("only_the_developer", [])
    cautions = [{"kind": k, "heading": CAUTION_HEADINGS[k],
                 "none": ONLY_THE_DEVELOPER if k in only else NOTHING_RECORDED,
                 "items": [{"text": x["text"], "source": x["source"]}
                           for x in rec.get("cautions", []) if x["kind"] == k]}
                for k in c.CAUTION_KINDS]
    return {
        "id": rec["id"],
        "path": f"/list/{rec['id']}/",
        "name": rec["name"],
        "description": rec["description"],
        "group": rec["group"],
        "beside": beside,
        "limits": list(rec.get("limits", [])),
        "test": rec["test"],
        "settled_by": rec["settled_by"],
        "progress_kind": rec["progress_kind"],
        "added": _plain(rec["added"]),
        "first_pass": rec["first_pass"],
        "constructed": bool(rec.get("constructed", False)),
        "checks": _plain(rec["checks"]) if "checks" in rec else None,
        "state": state,
        "evidence": evidence,
        "cautions": cautions,
        "history": _plain(rec.get("history", [])),
        "sources": [sources[s["key"]] for s in rec["sources"]],
    }


def build(groups: list[dict], records: list[dict], headline: dict,
          developers: list[dict] | None = None) -> dict:
    urls = {d["name"]: d["url"] for d in developers or []}
    live = sorted(c.shown(records), key=lambda r: r["name"].lower())
    entries = [entry_for_site(r, urls) for r in live]
    out_groups = []
    for g in groups:
        ids = [e["id"] for e in entries if e["group"] == g["name"]]
        if ids:
            out_groups.append({"name": g["name"], "meaning": g.get("meaning", ""),
                               "beside": g.get("beside") is True, "entries": ids})
    return {
        "exported_on": c.pacific_today(),
        "commit": commit(),
        "constructed": headline["records"]["constructed"],
        "headline": {k: headline[k] for k in ("computed_on", "last_read", "headline", "records")},
        "groups": out_groups,
        "entries": entries,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--data", type=Path, default=c.DEFAULT_DATA)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--public", type=Path, default=DEFAULT_PUBLIC)
    args = ap.parse_args(argv)
    try:
        groups, records = c.checked(args.data)
    except c.Refused as e:
        print("Refused. Nothing was written.\n" + str(e), file=sys.stderr)
        return 1
    headline_path = args.data / c.HEADLINE_NAME
    headline = c.read_headline(headline_path)
    reasons = c.stale_reasons(headline, c.compute(records))
    if reasons:
        print("Refused. Nothing was written: " + "; ".join(reasons)
              + ". Run scripts/compute.py first.", file=sys.stderr)
        return 1
    args.out.mkdir(parents=True, exist_ok=True)
    args.public.mkdir(parents=True, exist_ok=True)
    developers, _ = c.load_developers(args.data)
    data = build(groups, records, headline, developers)
    (args.out / "window.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    shutil.copyfile(headline_path, args.public / c.HEADLINE_NAME)
    print(f"Wrote {args.out / 'window.json'} ({len(data['entries'])} entries) and "
          f"{args.public / c.HEADLINE_NAME}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
