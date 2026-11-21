#!/usr/bin/env python3
"""Beyond the Window: read the built site and refuse it if a page breaks a rule of public text.

Plain Python, standard library only. Run after a build:

    python3 scripts/check_site.py              check site/dist
    python3 scripts/check_site.py --dist DIR   check a different folder
    python3 scripts/check_site.py --links      also print every outside address the pages link
                                               to, with the pages that use it, for opening by hand

What it refuses (docs/first-version-choices.md, choice 18):

1. A working word of the project on a public page: "schema", "protocol", "leaf", "branch",
   "generation", "weights", "context window", "wanting", and "reach" anywhere but in "reach
   for", which is the question's own wording.
2. A long dash.
3. A phrase that writes the site as its own agent ("the site expects").
4. The name of an AI model or its developer anywhere but on an entry's page, where it is the
   subject. The title of a source is a quotation and is not checked for rules 1 and 4: titles
   sit inside <cite> on every page.
   One exception: the About page names two developers in its paragraph on where the record's
   sources come from (the paragraph marked id="sources") and nowhere else: the one whose own
   pages most of the things counted rest on, and the one whose head wrote most of what stood
   under the first caution on 2026-11-19 (half of it since 2026-11-20, 9 items of 18; the About
   page's own build stops below half). John's ruling of 2026-11-19
   (docs/rulings/2026-11-19-no-public-mention-of-ai-help-in-building.md) keeps those facts on
   the page as facts about sources. The second name was added on 2026-11-19, because a reader
   of the About page alone could not tell who "another developer" was
   (docs/reviews/2026-11-19-check-of-site-changes.md, item 20). Those two names are allowed
   there. Every other name is still refused there, both are still refused everywhere else on
   the About page and on every other page, and no model's name is allowed anywhere off an
   entry's page.
   A second exception, since 2026-11-19: the Still Asking page names one model and its
   developer in the one paragraph marked id="capture", which says that ten questions were put
   to that model outside the record. John approved the paragraph
   (docs/rulings/2026-11-19-capture-paragraph-on-still-asking.md), and his ruling of the same
   day on what the site says about AI makes this the one thing it does say: when a model has
   been asked. The two names are allowed in that paragraph and are still refused everywhere
   else on that page.
   Widened on 2026-11-20, in the same narrow way: the paragraph now also names the second
   model asked, its developer, and the model that developer would not let the project ask
   (docs/rulings/2026-11-20-capture-paragraph-names-gemini.md). So five names are allowed in
   that one paragraph, and every one of them is still refused everywhere else on that page.
5. Since 2026-11-19, when the site was made listable as the sibling sites are: a page that asks
   search engines to leave it out, other than the page for a missing address; a page that does
   not give its own address at beyondthewindow.org; a robots file that turns search engines
   away or does not name the sitemap; and a sitemap that does not list exactly the built pages
   other than the page for a missing address. Until that day the rule was the opposite: every
   page had to ask to be left out, because nothing was published.
6. A link inside the site that leads to no page.
7. Since 2026-11-20, the rebuilt home page (design: docs/proposals/2026-11-20-rebuild-design.md,
   part 4). Until that day this rule refused a home page whose top was not the count ruled on
   2026-11-18, alone in the large type. John's go of 2026-11-20 to publish the rebuilt page
   sets that form aside for the home page
   (docs/rulings/2026-11-20-go-to-publish-the-rebuilt-home-page-once-checked.md), and the rule
   now has three parts:
   a. Every figure marked on the home page or the page of acts (data-figure) equals the figure
      in the readings of the served headline file, and the home page carries the figures it
      must. Every place in the table of developers shows the kind and the date the served file
      gives it, so no place says "nothing found" unless the records hold a search.
   b. The acts the home page and the page of acts list are exactly the acts in the served
      file, in the same order, each with its date, and the page of acts links each to its
      source. In the served file no act lacks a date, an actor, or a source with an address and
      the date it was opened, and no act by a developer names one the record does not cover.
      The feed holds one item for each act.
   c. The count itself is still served, and still equals the number of entries the served file
      lists as counted.
   d. Since 2026-11-20, when John ruled that the home page opens with a headline number again
      (docs/rulings/2026-11-20-home-page-opens-with-a-headline-again.md): the first figure on the
      home page is the count. The page holds one number in the large type (class="big-number"),
      it is marked as the count, it reads the count in the served file and nothing else (no
      total, no "of", nothing beside it inside the large type), and no other marked figure and
      no reading comes before it. Rule 8 still refuses the count written as a share of the list
      anywhere on the page.
9. The first person ("I", "my", "mine", "me", "we", "our", "ours", "us") anywhere but the
   About page's opening block on who is asking (the block marked id="who"), which is in John's
   own first person. The rest of the site stays impersonal. The notice that
   once stood on the home page and the Still Asking page, and had the same allowance, was
   removed on 2026-11-19. Words inside quotation marks are a source speaking and are not
   checked, as source titles are not.
8. The count written as a share of the things on the list ("6 of 9", "six of nine") on any
   page, or a total in the served headline. John ruled on 2026-11-18 that the count stands
   with no total beside it (docs/rulings/2026-11-18-home-page-count.md).
10. A phrase saying that an AI model, or a working session of one, drafted or checked the site.
   John ruled on 2026-11-19 that public pages do not mention AI help in building the project
   (docs/rulings/2026-11-19-no-public-mention-of-ai-help-in-building.md). The served headline
   file is read for these phrases too. A page saying that an AI model was asked the questions
   that make up the project's data is not refused: the same ruling says the pages state that
   plainly. Since 2026-11-19 the rule also refuses a sentence saying that no AI model took part,
   because a denial is the one thing the ruling forbids outright, and a sentence saying the site
   was made "with the help of" an AI
   (docs/reviews/2026-11-19-check-of-site-changes.md, item 25). It is still a short list of
   phrases and not a test of whether a page keeps the ruling.

11. Since 2026-11-20: no page is built under /draft/, and no page mentions that address. The
    rebuilt home page was drafted there, and no draft is to be published.
12. Rule 4, for the rebuilt pages. A developer the record covers (data/developers.toml, as the
    served file lists them) may be named on the home page inside the developers' reading (the
    list and the table marked data-developers-reading) and nowhere else on that page. John
    ruled on 2026-11-20 that the reading names every covered developer
    (docs/rulings/2026-11-20-home-page-names-every-covered-developer.md), so each must be named
    in both. On the page that lists every act, a covered developer may be named as the actor of
    an act (the element marked class="actor") and nowhere else. That second allowance is a
    session's and is not ruled. In the pages' own sentences no AI model is named on either
    page. On the page of acts and in the feed a model's name does appear inside the label of a
    source, which sits inside <cite> and is not checked for this rule, as on every page: a
    label says what a source is, and two of the records' sources are about a named model (a
    developer's update on one model's retirement, and another's notice withdrawing one). Until
    2026-11-20 this note said flatly that no model is named on either page, which the labels
    made untrue; the note was changed and the labels were not, because they are sources that
    stood before the rebuild and each entry's page already shows them.
13. The phrase "from memory" on any page. A fact written without opening its source does not
    reach a public page, so the phrase on a page means a check was skipped.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DIST = ROOT / "site" / "dist"

WORKING_WORDS = [
    (r"\bschemas?\b", "schema"),
    (r"\bprotocols?\b", "protocol"),
    (r"\bleaf\b", "leaf"),
    (r"\bbranch(es)?\b", "branch"),
    (r"\bgenerations?\b", "generation"),
    (r"\bweights\b", "weights"),
    (r"\bcontext windows?\b", "context window"),
    (r"\bwanting\b", "wanting"),
    (r"\breach(es|ed|ing)?\b(?! for\b)", "reach"),
]
SITE_AS_AGENT = (r"\b(the|this) (site|page|list|record|tracker) (does )?"
                 r"(expects?|believes?|thinks?|hopes?|wants?|feels?|fears?|knows?|judges?|doubts?|"
                 r"suspects?|takes? (a|the) view)\b")
# Rule 9: where the first person may stand, and nowhere else.
FIRST_PERSON = r"\b(I|[Mm]y|[Mm]ine|[Mm]e|[Ww]e|[Oo]urs?|us)\b"
ABOUT_PAGE = "/about/"
# Rule 5: the site's address, and the one page search engines are asked to leave out.
SITE_ADDRESS = "https://beyondthewindow.org"
NOT_FOUND_PAGE = "/404.html"
FIRST_PERSON_PLACE = r'(?is)<div\b[^>]*\bid="who"[^>]*>.*?</div>'
QUOTED = r'"[^"]*"|“[^”]*”'
# Rule 4's one exception: the About page, this paragraph, this name, and nothing wider.
NAMED_DEVELOPER_PARAGRAPH = r'(?is)<p\b[^>]*\bid="sources"[^>]*>.*?</p>'
NAMED_DEVELOPER = r"\b(Anthropic|Microsoft AI)\b"
# Rule 10: the phrases removed on 2026-11-19 under John's ruling that public pages do not
# mention AI help in building the project
# (docs/rulings/2026-11-19-no-public-mention-of-ai-help-in-building.md). Kept short on purpose:
# it is there so that those sentences cannot come back unnoticed, and it is not a test of
# whether a page keeps the ruling. "An AI model was asked" is allowed, and is not listed.
BUILT_WITH_AI = [
    (r"\bdrafted by an AI\b", "drafted by an AI"),
    (r"\b(AI )?model (that )?(drafted|wrote|helped|checked)\b", "a model drafted, wrote, helped or checked"),
    (r"\b(by|of) a session\b|\ba session(’|')s\b|\bsessions? (that|in which this)\b", "a working session"),
    (r"\bunder my direction\b", "under my direction"),
    (r"\bwho wrote this\b", "who wrote this"),
    (r"\bcheckers?\b", "checkers"),
    (r"\b(AI|language) models? (prepared|produced|generated|built|made)\b",
     "a model prepared, produced, generated, built or made"),
    (r"\bwith the (help|aid|assistance) of (an? )?(AI\b|artificial intelligence|language model)",
     "with the help of an AI"),
    (r"\b(written|drafted|built|checked|produced|generated) (with|by|using) "
     r"(an? )?(AI\b|artificial intelligence|language model)", "written with or by an AI"),
    # A denial is the one thing the ruling forbids outright.
    (r"\bno (AI|language) models? (took part|helped|was used|were used|was involved|were involved|"
     r"had a hand|drafted|wrote|checked)\b", "a denial that an AI model took part"),
    (r"\bwithout (the help of )?(any |an? )?(AI\b|artificial intelligence|language model)",
     "a denial that an AI model took part"),
    (r"\bno AI model has been asked anything\b", "a sentence that reads as a denial"),
]
# Rule 4's second exception: the Still Asking page, this paragraph, these five names.
CAPTURE_PAGE = "/still-asking/"
CAPTURE_PARAGRAPH = r'(?is)<p\b[^>]*\bid="capture"[^>]*>.*?</p>'
CAPTURE_NAMES = r"\b(Claude Sonnet 4\.5|Anthropic|Gemini 2\.5 Flash|Gemini 2\.5 Pro|Google)\b"
MODEL_NAMES = (r"\b(claude|anthropic|openai|chatgpt|gpt|gemini|deepmind|google|llama|grok|xai|"
               r"mistral|copilot|microsoft|deepseek|opus|sonnet|haiku)\b")


# The rebuilt home page and the page of acts (rules 7, 11 and 12).
DRAFT_PREFIX = "/draft/"
HOME_PAGE = "/"
ACTS_PAGE = "/acts/"
ACTS_FEED = "acts.xml"
DEVELOPERS_READING = r'(?is)<(ul|table)\b[^>]*\bdata-developers-reading\b[^>]*>.*?</\1>'
ACTOR = r'(?is)<span class="actor"[^>]*>(?:\s*<a\b[^>]*>)?\s*([^<]*?)\s*(?:</a>\s*)?</span>'
FIGURE = r'(?is)<span\b[^>]*\bdata-figure="([^"]+)"[^>]*>\s*([^<]*?)\s*</span>'
# Figures the home page must carry, so that leaving the mark off is not a way past rule 7.
# (How many places are not yet searched is shown only while there are any, so it is not here.)
REQUIRED_FIGURES = ["developers.covered", "developers.things", "developers.cells",
                    "developers.nothing_found", "law.against.count", "public.0",
                    "researchers.0", "researchers.1", "acts.count"]
COUNT_WORDS = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
               "ten", "eleven", "twelve"]
CELL_KINDS = ["offered", "unruled", "not_counted", "taken_back", "nothing_found", "not_searched"]


def expected_figures(rd: dict) -> dict[str, float]:
    """Every figure a draft page may show, by its mark, from the served readings."""
    g = rd["developers"]
    f: dict[str, float] = {
        "developers.covered": len(g["covered"]),
        "developers.things": g["things"],
        "developers.cells": g["cells"],
        "developers.offering": g["offering"],
        "acts.count": len(rd["acts"]),
    }
    for k in CELL_KINDS:
        f[f"developers.{k}"] = g["counts"][k]
        for d in g["by_developer"]:
            f[f"developers.{d['name']}.{k}"] = d[k]
            # found and not counted, of either kind: what a developer's box shows as one figure
            f[f"developers.{d['name']}.near"] = d["not_counted"] + d["taken_back"]
    for half in ("against", "protecting"):
        if rd["law"].get(half):
            f[f"law.{half}.count"] = rd["law"][half]["count"]
    for who in ("public", "researchers"):
        for i, m in enumerate((rd.get(who) or {}).get("measures", [])):
            f[f"{who}.{i}"] = m["value"]
    return f


def as_number(text: str) -> float | None:
    text = text.strip().lower().rstrip("%").strip()
    if text in COUNT_WORDS:
        return COUNT_WORDS.index(text)
    try:
        return float(text)
    except ValueError:
        return None


BIG_NUMBER = r'(?is)<p\b[^>]*\bclass="big-number"[^>]*>(.*?)</p>'


def headline_problems(raw: str, count: int) -> list[str]:
    """Rule 7d: the home page's first figure is the computed count, alone in the large type."""
    rel = HOME_PAGE
    body = raw.split("<body", 1)[-1]
    bigs = list(re.finditer(BIG_NUMBER, body))
    if len(bigs) != 1:
        return [f"{rel}: the page should hold one number in the large type, the count, and "
                f"{len(bigs)} were found"]
    big = bigs[0]
    problems = []
    if not re.fullmatch(r'(?is)\s*<span\b[^>]*\bdata-figure="headline\.count"[^>]*>[^<]*</span>\s*',
                        big.group(1)):
        problems.append(f"{rel}: the number in the large type is not marked as the count, or "
                        f"something stands beside it")
    inner = " ".join(html.unescape(re.sub(r"<[^>]+>", "", big.group(1))).split())
    if inner != str(count):
        problems.append(f"{rel}: the large type reads \"{inner}\" and the count in "
                        f"/data/headline.json is {count}, alone")
    first_figure = re.search(r'\bdata-figure="([^"]+)"', body)
    if not first_figure or first_figure.group(1) != "headline.count":
        problems.append(f"{rel}: the first figure on the page is not the count "
                        f"({first_figure.group(1) if first_figure else 'none'} comes first)")
    reading = re.search(r'class="rb-reading', body)
    if reading and reading.start() < big.start():
        problems.append(f"{rel}: a reading stands above the count")
    return problems


def rebuilt_problems(dist: Path, rd: dict | None, count: int | None = None) -> list[str]:
    """Rule 7, parts a and b, and the half of rule 12 that asks for every covered developer."""
    problems: list[str] = []
    homes = [HOME_PAGE] if (dist / "index.html").is_file() else []
    acts_page = dist / ACTS_PAGE.strip("/") / "index.html"
    if not rd:
        return ["/data/headline.json holds no readings, and the home page shows them"]
    if not acts_page.is_file():
        problems.append(f"{ACTS_PAGE}: the page that lists every act is not built")
    covered = rd["developers"]["covered"]
    for a in rd["acts"]:
        src = a.get("source") or {}
        missing = [k for k in ("date", "actor", "actor_kind", "words", "read_on") if not a.get(k)]
        if not src.get("url") or not src.get("opened"):
            missing.append("a source with an address and the date it was opened")
        if missing:
            problems.append(f"/data/headline.json: the act '{a.get('id')}' lacks "
                            + ", ".join(missing))
        if a.get("actor_kind") == "developer" and a.get("actor") not in covered:
            problems.append(f"/data/headline.json: the act '{a.get('id')}' is by a developer "
                            f"the record does not cover ({a.get('actor')})")
    want_figures = expected_figures(rd)
    if count is not None:
        want_figures["headline.count"] = count
    want_acts = [(a["id"], a["date"]) for a in rd["acts"]]
    want_cells = {(row["entry"], c["developer"]): (c["kind"], c["date"] or "")
                  for row in rd["developers"]["rows"] for c in row["cells"]}

    def figures(rel: str, raw: str, required: list[str]) -> None:
        seen = set()
        for key, text in re.findall(FIGURE, raw):
            seen.add(key)
            if key not in want_figures:
                problems.append(f"{rel}: a figure marked '{key}', which the served file does not hold")
            elif as_number(html.unescape(text)) != want_figures[key]:
                problems.append(f"{rel}: the figure '{key}' reads \"{text}\" and the served file "
                                f"says {want_figures[key]:g}")
        for key in required:
            if key not in seen:
                problems.append(f"{rel}: the figure '{key}' is not on the page, or is not marked")

    def acts(rel: str, raw: str) -> None:
        got = re.findall(r'<li\b[^>]*\bdata-act="([^"]+)"[^>]*\bdata-date="([^"]*)"', raw)
        if got != want_acts:
            problems.append(f"{rel}: the acts listed are not the acts in the served file, in "
                            f"order, each with its date ({len(got)} listed, {len(want_acts)} served)")

    for rel in homes:
        raw = (dist / "index.html").read_text(encoding="utf-8")
        figures(rel, raw, REQUIRED_FIGURES + (["headline.count"] if count is not None else []))
        if count is not None:
            problems += headline_problems(raw, count)
        acts(rel, raw)
        got_cells = {}
        for entry, row in re.findall(r'(?is)<tr\b[^>]*\bdata-entry="([^"]+)"[^>]*>(.*?)</tr>', raw):
            for td in re.findall(r"<td\b[^>]*>", row):
                # an empty attribute may be written with no value, so each is read on its own
                attr = {k: v for k, v in re.findall(r'\bdata-(dev|kind|date)(?:="([^"]*)")?', td)}
                got_cells[(entry, html.unescape(attr.get("dev", "")))] = (attr.get("kind", ""),
                                                                         attr.get("date", ""))
        if got_cells != want_cells:
            wrong = sorted(set(got_cells.items()) ^ set(want_cells.items()))
            problems.append(f"{rel}: the table of developers does not show what the served file "
                            f"holds, place by place ({len(wrong)} differences, the first: {wrong[:1]})")
        blocks = [m.group(0) for m in re.finditer(DEVELOPERS_READING, raw)]
        if len(blocks) != 2:
            problems.append(f"{rel}: the developers' reading should be one list and one table, "
                            f"and {len(blocks)} such blocks were found")
        for block in blocks:
            text = visible_text(block, keep_cites=False)
            for name in covered:
                if not re.search(rf"\b{re.escape(name)}\b", text):
                    problems.append(f"{rel}: the developers' reading does not name {name}, a "
                                    f"developer the record covers")
    if acts_page.is_file():
        raw = acts_page.read_text(encoding="utf-8")
        figures(ACTS_PAGE, raw, ["acts.count"])
        acts(ACTS_PAGE, raw)
        linked = {html.unescape(h) for h in re.findall(r'<a\b[^>]*\bhref="([^"]+)"', raw)}
        for a in rd["acts"]:
            if a["source"]["url"] not in linked:
                problems.append(f"{ACTS_PAGE}: the act '{a['id']}' is listed without a link to "
                                f"its source")
    feed = dist / ACTS_FEED
    if not feed.is_file():
        problems.append(f"/{ACTS_FEED}: the feed of acts is not built")
    else:
        feed_text = feed.read_text(encoding="utf-8")
        if len(re.findall(r"<entry>", feed_text)) != len(rd["acts"]):
            problems.append(f"/{ACTS_FEED}: does not hold one item for each act in the served file")
        if re.search("[—–]", feed_text):
            problems.append(f"/{ACTS_FEED}: long dash")
    return problems


def visible_text(page: str, keep_cites: bool) -> str:
    page = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", page)
    if not keep_cites:
        page = re.sub(r"(?is)<cite\b.*?</cite>", " ", page)
    # words in attributes a reader meets: descriptions, hover titles, labels
    attrs = re.findall(r'(?is)\b(?:content|title|aria-label|alt)="([^"]*)"', page)
    body = re.sub(r"(?s)<[^>]+>", " ", page)
    return html.unescape(" ".join([body] + attrs))


NUMBER_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                "seventeen", "eighteen", "nineteen", "twenty"]


def fraction_problems(dist: Path, pages: list[Path], count: int, on_the_list: int) -> list[str]:
    """Rule 8: no page gives the count as a share of the things on the list."""
    def forms(n: int) -> str:
        names = [str(n)] + ([NUMBER_WORDS[n]] if n < len(NUMBER_WORDS) else [])
        return "(?:" + "|".join(names) + ")"
    pattern = rf"\b{forms(count)} (?:out )?of (?:the |all )?{forms(on_the_list)}\b"
    found = []
    for page in pages:
        rel = "/" + str(page.relative_to(dist)).replace("index.html", "")
        text = " ".join(visible_text(page.read_text(encoding="utf-8"), keep_cites=False).split())
        for m in re.finditer(pattern, text, re.I):
            snippet = text[max(0, m.start() - 40):m.end() + 40]
            found.append(f"{rel}: the count written as a share of the list: \"...{snippet}...\"")
    return found


def check(dist: Path) -> tuple[list[str], dict[str, set[str]]]:
    problems: list[str] = []
    outside: dict[str, set[str]] = {}
    pages = sorted(dist.rglob("*.html"))
    if not pages:
        return [f"no built pages in {dist}"], outside
    # The readings of the served file, for rules 7 and 12. None when it holds none.
    served_file = dist / "data" / "headline.json"
    readings = json.loads(served_file.read_text(encoding="utf-8")).get("readings") \
        if served_file.is_file() else None
    covered = "|".join(re.escape(n) for n in readings["developers"]["covered"]) if readings else ""
    for page in pages:
        rel = "/" + str(page.relative_to(dist)).replace("index.html", "")
        raw = page.read_text(encoding="utf-8")
        is_entry = re.match(r"^/list/[a-z-]+/$", rel) is not None
        is_draft = rel.startswith(DRAFT_PREFIX)
        text = visible_text(raw, keep_cites=False)
        everything = visible_text(raw, keep_cites=True)

        def flag(pattern: str, label: str, where: str = text) -> None:
            for m in re.finditer(pattern, where, re.I):
                start = max(0, m.start() - 40)
                snippet = " ".join(where[start:m.end() + 40].split())
                problems.append(f"{rel}: {label}: \"...{snippet}...\"")

        for pattern, word in WORKING_WORDS:
            flag(pattern, f"working word '{word}'")
        flag("[—–]", "long dash", everything)
        flag(SITE_AS_AGENT, "the site written as its own agent", everything)
        if not is_entry:
            names_text = text
            if rel == ABOUT_PAGE:
                without = re.sub(NAMED_DEVELOPER_PARAGRAPH,
                                 lambda m: re.sub(NAMED_DEVELOPER, " ", m.group(0)), raw, count=1)
                names_text = visible_text(without, keep_cites=False)
            elif rel == CAPTURE_PAGE:
                without = re.sub(CAPTURE_PARAGRAPH,
                                 lambda m: re.sub(CAPTURE_NAMES, " ", m.group(0)), raw, count=1)
                names_text = visible_text(without, keep_cites=False)
            elif rel == HOME_PAGE and covered:  # rule 12: the developers' reading only
                without = re.sub(DEVELOPERS_READING,
                                 lambda m: re.sub(rf"\b({covered})\b", " ", m.group(0)), raw)
                names_text = visible_text(without, keep_cites=False)
            elif rel == ACTS_PAGE and covered:  # rule 12: the actor of an act only
                without = re.sub(ACTOR, lambda m: " " if re.fullmatch(covered, m.group(1))
                                 else m.group(0), raw)
                names_text = visible_text(without, keep_cites=False)
            flag(MODEL_NAMES, "an AI model or developer named off an entry's page", names_text)
        for pattern, label in BUILT_WITH_AI:
            flag(pattern, f"says how the site was built ('{label}')")
        outside_places = raw
        if rel == ABOUT_PAGE:  # the block on About only, and once
            outside_places = re.sub(FIRST_PERSON_PLACE, " ", outside_places, count=1)
        unquoted = re.sub(QUOTED, " ", visible_text(outside_places, keep_cites=False))
        for m in re.finditer(FIRST_PERSON, unquoted):
            start = max(0, m.start() - 40)
            snippet = " ".join(unquoted[start:m.end() + 40].split())
            problems.append(f"{rel}: the first person outside the About page's block marked "
                            f"id=\"who\": \"...{snippet}...\"")
        asks_out = re.search(r'<meta name="robots" content="noindex', raw) is not None
        if asks_out != (rel == NOT_FOUND_PAGE):
            problems.append(f"{rel}: " + ("asks search engines to leave it out" if asks_out else
                                          "the page for a missing address does not ask search "
                                          "engines to leave it out"))
        if is_draft:  # rule 11
            problems.append(f"{rel}: a draft is built; no page under {DRAFT_PREFIX} is published")
        elif DRAFT_PREFIX in raw:
            problems.append(f"{rel}: mentions the address {DRAFT_PREFIX}, where nothing is published")
        flag(r"\bfrom memory\b", "the phrase 'from memory'", everything)  # rule 13
        own = SITE_ADDRESS + rel
        if rel != NOT_FOUND_PAGE and f'<link rel="canonical" href="{own}"' not in raw:
            problems.append(f"{rel}: does not give its own address ({own})")
        for href in re.findall(r'<a\b[^>]*\bhref="([^"]+)"', raw):
            href = html.unescape(href)
            if href.startswith(("http://", "https://")):
                outside.setdefault(href, set()).add(rel)
            elif href.startswith("/"):
                target = href.split("#")[0]
                f = dist / target.lstrip("/")
                if not (f.is_file() or (f / "index.html").is_file()):
                    problems.append(f"{rel}: links to {href}, which is not a page")
            elif not href.startswith(("#", "mailto:")):
                problems.append(f"{rel}: a link that is neither a full address nor from the root: {href}")

    # rule 5: the robots file and the sitemap
    robots = dist / "robots.txt"
    robots_text = robots.read_text(encoding="utf-8") if robots.is_file() else ""
    if re.search(r"(?m)^Disallow: */ *$", robots_text) or "Allow: /" not in robots_text:
        problems.append("/robots.txt: turns search engines away, or is missing")
    if f"Sitemap: {SITE_ADDRESS}/sitemap.xml" not in robots_text:
        problems.append("/robots.txt: does not name the sitemap")
    sitemap = dist / "sitemap.xml"
    listed = set(re.findall(r"<loc>([^<]+)</loc>", sitemap.read_text(encoding="utf-8"))) \
        if sitemap.is_file() else set()
    built = {SITE_ADDRESS + "/" + str(p.relative_to(dist)).replace("index.html", "")
             for p in pages if "/" + str(p.relative_to(dist)) != NOT_FOUND_PAGE}
    if listed != built:
        problems.append("/sitemap.xml: does not list exactly the built pages: "
                        + ", ".join(sorted(listed ^ built) or ["it is missing"]))

    # the served file: what it must not say, and the count, which is still served (rule 7c)
    served = dist / "data" / "headline.json"
    home = dist / "index.html"
    count = None
    if not served.is_file():
        problems.append("/data/headline.json is not served")
    elif home.is_file():
        served_text = served.read_text(encoding="utf-8")
        for pattern, label in BUILT_WITH_AI:
            for m in re.finditer(pattern, served_text, re.I):
                snippet = " ".join(served_text[max(0, m.start() - 40):m.end() + 40].split())
                problems.append(f"/data/headline.json: says how the site was built ('{label}'): "
                                f"\"...{snippet}...\"")
        file = json.loads(served_text)
        h = file["headline"]
        if h.get("count") != len(h.get("offered_ids", [])) or not str(h.get("words", "")).startswith(f"{h.get('count')} "):
            problems.append("/data/headline.json: the count, the entries counted and the "
                            "sentence do not agree")
        if "total" in h:
            problems.append("/data/headline.json: the headline holds a total beside the count")
        problems += fraction_problems(dist, pages, h["count"], file["records"]["on_the_list"])
        count = h.get("count")
    problems += rebuilt_problems(dist, readings, count)
    return problems, outside


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--dist", type=Path, default=DEFAULT_DIST)
    ap.add_argument("--links", action="store_true")
    args = ap.parse_args(argv)
    problems, outside = check(args.dist)
    if args.links:
        for url in sorted(outside):
            print(f"{url}\n    on {', '.join(sorted(outside[url]))}")
    if problems:
        print(f"Refused: {len(problems)} problem(s) in the built site.", file=sys.stderr)
        for p in problems:
            print("  " + p, file=sys.stderr)
        return 1
    print(f"The built site passes: {len(list(args.dist.rglob('*.html')))} pages, "
          f"{len(outside)} outside addresses linked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
