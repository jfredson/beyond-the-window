#!/usr/bin/env python3
"""Beyond the Window: refuse a news post that cannot be trusted (tracker pattern, rule 4.16).

Copied on 2026-11-21 from Outrunning Ageing's scripts/check_news.py (its main branch), the model
the sibling sites copied, and adapted to this site's records. The kinds and the changes below are
PROPOSED (docs/proposals/2026-11-21-news-section.md).

Plain Python, standard library only. Run from anywhere, after scripts/export.py has written
site/src/data/window.json (the build's prebuild does both, in that order):

    python3 scripts/check_news.py                 check the folder the site builds from
    python3 scripts/check_news.py --posts DIR     check another folder (for tests)
    python3 scripts/check_news.py --records FILE  read another window.json (for tests)

The folder the site builds from is site/src/content/news, unless NEWS_POSTS names another (the
site's content.config.ts reads the same setting), so the check always reads what the build reads.

A post is one Markdown file, YYYY-MM-DD-slug.md, with a frontmatter block. The check refuses a
post that: has a file name not of that form, or a frontmatter date that differs from it; lacks a
title, date, kind or summary; carries a kind outside the six; names no entry, or one that does not
exist (the opener, kind "start-here", and a story from the field, kind "story", need not name
one); cites no source with an https address; states a figure (any digit) in a paragraph that
carries no link (a Markdown link or a written-out https address) to a source or an entry; or names
an entry that shows no dated change within fourteen days of the post's date, so a post cannot
announce what the record does not show. A story carries no before-and-after line, since no number
on the site moved. There is one opening post at most. The rules are the family's of 2026-10-18,
and the story kind is Outrunning Ageing's of 2026-11-09.

What counts as a dated change to an entry here (the sibling reads revisions, a rung reached and a
weekly reading, none of which this site has): the day it was added; the day its present state was
set; any dated line of its history; any day in its record of checks; and the date of any act in
the record that belongs to it. An act dated only to a month or a year counts from the first day of
that month or year.

One rule of this site's own: a post marked `constructed: true` (a made-up example, used to draw the
pages before any real post exists) is refused in site/src/content/news, the folder the site
publishes from. It is allowed anywhere else, such as scripts/fixtures/news. The check of the built
site (scripts/check_site.py, rule 14) refuses a built page that shows one, so a made-up post cannot
be published by building with NEWS_POSTS pointed at the fixtures either.

Pictures (tracker pattern, rule 4.23). A post may show real photographs of its event. The check
refuses a post whose picture: is not written as a <figure> with an <img> and a <figcaption>; is
loaded from another site and not from /news/ here; has no description (alt); has no entry under
`photos:` in the frontmatter giving its file, source page, credit, licence, licence link and the
day the licence was read; has a caption that does not link to that source page; or is listed under
`photos:` and not shown. It also refuses a listed picture whose file is not in the folder the site
serves at /news/. The check cannot tell whether a licence really allows the use: that is read on
the source page by whoever adds the picture, and the entry records that it was.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLISHED = ROOT / "site" / "src" / "content" / "news"
KINDS = {"start-here", "count-moved", "state-changed", "entry-added", "method-changed", "story"}
NO_RECORD_KINDS = {"start-here", "story"}  # the kinds that need not name an entry
WINDOW_DAYS = 14
NAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)\.md$")


def frontmatter(text: str) -> tuple[dict, str]:
    """A small reader for the frontmatter this site writes: scalars, lists of scalars, and lists of
    {label, url} tables written as `- label: ...` / `  url: ...`. Enough for the posts; nothing else."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    head, body = text[4:end], text[end + 4:]
    data: dict = {}
    key = None
    for raw in head.split("\n"):
        if not raw.strip():
            continue
        if raw.lstrip().startswith("- ") and key is not None:
            item = raw.lstrip()[2:].strip()
            if ":" in item and not item.startswith(("http:", "https:")):
                k, v = item.split(":", 1)
                data.setdefault(key, []).append({k.strip(): v.strip().strip('"')})
            else:
                data.setdefault(key, []).append(item.strip('"'))
            continue
        if raw.startswith("  ") and ":" in raw and key is not None and isinstance(data.get(key), list) and data[key] and isinstance(data[key][-1], dict):
            k, v = raw.strip().split(":", 1)
            data[key][-1][k.strip()] = v.strip().strip('"')
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", raw)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            data[key] = []
        elif val.startswith("[") and val.endswith("]"):
            data[key] = [x.strip().strip('"') for x in val[1:-1].split(",") if x.strip()]
        elif val in ("true", "false"):
            data[key] = val == "true"
        else:
            data[key] = val.strip('"')
    return data, body


def paragraphs(body: str) -> list[str]:
    """The prose paragraphs of the body: not headings, not table rows, not blank."""
    out, cur = [], []
    for line in body.split("\n"):
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("|"):
            if cur:
                out.append(" ".join(cur)); cur = []
            continue
        cur.append(s)
    if cur:
        out.append(" ".join(cur))
    return out


def start_of(text: str) -> str:
    """A date given as a day, a month or a year, placed at its first day."""
    parts = text.split("-")
    y, m, d = (parts + ["01", "01"])[:3]
    return f"{y}-{m}-{d}"


def entry_dates(entry: dict, acts: list[dict]) -> list[str]:
    """Every date on which the record shows a change to this entry."""
    dates: list[str] = []
    if entry.get("added"):
        dates.append(entry["added"])
    if (entry.get("state") or {}).get("set_on"):
        dates.append(entry["state"]["set_on"])
    for h in entry.get("history") or []:
        if h.get("date"):
            dates.append(h["date"])
    for v in (entry.get("checks") or {}).values():
        if isinstance(v, str) and re.match(r"^\d{4}-\d{2}-\d{2}$", v):
            dates.append(v)
    for a in acts:
        if a.get("entry") == entry.get("id") and a.get("date"):
            dates.append(start_of(a["date"]))
    return dates


def changed_near(entry: dict, when: date, acts: list[dict]) -> bool:
    lo, hi = when - timedelta(days=WINDOW_DAYS), when + timedelta(days=WINDOW_DAYS)
    for d in entry_dates(entry, acts):
        try:
            if lo <= date.fromisoformat(d) <= hi:
                return True
        except ValueError:
            pass
    return False


def story_problems(name: str, fm: dict) -> list[str]:
    """What a post about a story that changes no record may not carry."""
    if fm.get("before") or fm.get("after"):
        return [f"{name}: a story changes no number on the site, so it carries no before or after line"]
    return []


PHOTO_FIELDS = ("source", "credit", "licence", "licence_url", "read_on")
FIGURE_RE = re.compile(r"<figure\b.*?</figure>", re.S | re.I)
IMG_RE = re.compile(r"<img\b[^>]*>", re.I)


def _attr(tag: str, name: str) -> str | None:
    m = re.search(rf'\b{name}\s*=\s*"([^"]*)"', tag, re.I)
    return m.group(1) if m else None


def check_photos(name: str, fm: dict, body: str, pictures_dir: Path | None) -> list[str]:
    """The pictures in one post (tracker pattern, rule 4.23), as on Outrunning Ageing."""
    problems: list[str] = []
    listed: dict[str, dict] = {}
    for ph in fm.get("photos") or []:
        if not isinstance(ph, dict) or not ph.get("file"):
            problems.append(f"{name}: an entry under photos names no file"); continue
        f = ph["file"]
        listed[f] = ph
        for field in PHOTO_FIELDS:
            if not str(ph.get(field) or "").strip():
                problems.append(f"{name}: the picture {f} has no {field} under photos")
        for field in ("source", "licence_url"):
            v = str(ph.get(field) or "")
            if v and not v.startswith("https://"):
                problems.append(f"{name}: the picture {f} gives a {field} that is not an https address")
        if ph.get("read_on"):
            try:
                date.fromisoformat(str(ph["read_on"]))
            except ValueError:
                problems.append(f"{name}: the picture {f} gives a read_on that is not a date (YYYY-MM-DD)")
        if pictures_dir is not None and not (pictures_dir / f).is_file():
            problems.append(f"{name}: the picture file {f} is not in {pictures_dir.name}/; a picture is kept on this site")
    if re.search(r"!\[[^\]]*\]\(", body):
        problems.append(f"{name}: a picture is written as ![...](...); write it as a <figure> with a <figcaption>")
    outside = FIGURE_RE.sub("", body)
    if IMG_RE.search(outside):
        problems.append(f"{name}: a picture stands outside a <figure>; every picture needs a caption")
    shown: set[str] = set()
    for fig in FIGURE_RE.findall(body):
        caption = re.search(r"<figcaption\b.*?</figcaption>", fig, re.S | re.I)
        for tag in IMG_RE.findall(fig):
            src = _attr(tag, "src") or ""
            f = src.rsplit("/", 1)[-1]
            shown.add(f)
            if not src.startswith("/news/"):
                problems.append(f"{name}: the picture {src or '(no address)'} is not served from /news/ on this site")
            if not (_attr(tag, "alt") or "").strip():
                problems.append(f"{name}: the picture {f} has no description (alt) for readers who cannot see it")
            if not caption:
                problems.append(f"{name}: the picture {f} has no caption")
            if f not in listed:
                problems.append(f"{name}: the picture {f} has no entry under photos (file, source, credit, licence, licence_url, read_on)")
            elif caption and listed[f].get("source") and str(listed[f]["source"]) not in caption.group(0):
                problems.append(f"{name}: the caption of {f} does not link to its source page")
    for f in listed:
        if f not in shown:
            problems.append(f"{name}: photos lists {f}, which the post does not show")
    return problems


def check(posts_dir: Path, window: dict, pictures_dir: Path | None = None) -> tuple[list[str], int]:
    problems: list[str] = []
    by_id = {e["id"]: e for e in window.get("entries") or []}
    acts = ((window.get("headline") or {}).get("readings") or {}).get("acts") or []
    published = posts_dir.resolve() == PUBLISHED.resolve()
    files = sorted(p for p in posts_dir.glob("*.md")) if posts_dir.exists() else []
    openers = 0
    for path in files:
        name = path.name
        m = NAME_RE.match(name)
        if not m:
            problems.append(f"{name}: the file name must be YYYY-MM-DD-slug.md")
            continue
        fm, body = frontmatter(path.read_text(encoding="utf-8"))
        if not fm:
            problems.append(f"{name}: no frontmatter"); continue
        for field in ("title", "date", "kind", "summary"):
            if not fm.get(field):
                problems.append(f"{name}: frontmatter has no {field}")
        if fm.get("date") and fm["date"] != m.group(1):
            problems.append(f"{name}: the frontmatter date {fm['date']} differs from the file name's {m.group(1)}")
        if fm.get("constructed") is True and published:
            problems.append(f"{name}: a constructed example stands in the folder the site publishes from; keep it in scripts/fixtures/news")
        kind = fm.get("kind")
        if kind not in KINDS:
            problems.append(f"{name}: kind {kind!r} is not one of the six")
        if kind == "start-here":
            openers += 1
        recs = fm.get("records") or []
        if kind not in NO_RECORD_KINDS and not recs:
            problems.append(f"{name}: names no entry (records: [...])")
        for rid in recs:
            if rid not in by_id:
                problems.append(f"{name}: names an entry that does not exist: {rid}")
        sources = fm.get("sources") or []
        if not any(isinstance(s, dict) and str(s.get("url", "")).startswith("https://") for s in sources):
            problems.append(f"{name}: cites no source with an https address")
        problems.extend(check_photos(name, fm, body, pictures_dir))
        try:
            when = date.fromisoformat(fm.get("date") or m.group(1))
        except ValueError:
            when = None
        if kind == "story":
            problems += story_problems(name, fm)
        if when and kind not in NO_RECORD_KINDS:
            for rid in recs:
                if rid in by_id and not changed_near(by_id[rid], when, acts):
                    problems.append(f"{name}: {rid} shows no dated change within {WINDOW_DAYS} days of {when}; a post cannot announce what the record does not show")
        for i, para in enumerate(paragraphs(body), 1):
            if re.search(r"\d", para) and "](" not in para and "https://" not in para:
                problems.append(f"{name}: paragraph {i} states a figure with no link to a source or an entry: {para[:70]!r}")
    if openers > 1:
        problems.append(f"{posts_dir}: {openers} posts of kind start-here; there is one per site")
    return problems, len(files)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    default_posts = os.environ.get("NEWS_POSTS")
    if default_posts:  # the site reads it relative to site/, as content.config.ts does
        default_posts = str((ROOT / "site" / default_posts).resolve())
    ap.add_argument("--posts", default=default_posts or str(PUBLISHED))
    ap.add_argument("--records", default=str(ROOT / "site" / "src" / "data" / "window.json"))
    ap.add_argument("--pictures", default=str(ROOT / "site" / "public" / "news"), help="the folder the site serves at /news/, where a post's pictures are kept")
    a = ap.parse_args(argv)
    rp = Path(a.records)
    if not rp.exists():
        print(f"{rp} is missing; run scripts/export.py first", file=sys.stderr)
        return 2
    window = json.loads(rp.read_text(encoding="utf-8"))
    problems, n = check(Path(a.posts), window, pictures_dir=Path(a.pictures) if a.pictures else None)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        print(f"{len(problems)} problem(s) in {n} post(s)", file=sys.stderr)
        return 1
    print(f"OK: {n} news post(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
