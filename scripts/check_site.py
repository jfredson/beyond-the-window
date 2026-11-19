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
   One exception: the About page names the one developer whose own pages most of the things
   counted rest on, in its paragraph on where the record's sources come from (the paragraph
   marked id="sources") and nowhere else. John's ruling of 2026-11-19
   (docs/rulings/2026-11-19-no-public-mention-of-ai-help-in-building.md) keeps that fact on
   the page as a fact about sources. That one developer's name is allowed there. Every
   other name is still refused there, the name is still refused everywhere else on the About
   page and on every other page, and no model's name is allowed anywhere off an entry's page.
5. A page that does not ask search engines to leave it out, while nothing is published.
6. A link inside the site that leads to no page.
7. The headline number on the home page differing from the headline file the site serves, or
   anything standing beside it in the large type.
9. The first person ("I", "my", "mine", "me", "we", "our", "ours", "us") anywhere but the
   About page's block on who decides and what has been checked (the block marked id="who"),
   which is in John's own first person. The rest of the site stays impersonal. The notice that
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
   plainly.
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
FIRST_PERSON_PLACE = r'(?is)<div\b[^>]*\bid="who"[^>]*>.*?</div>'
QUOTED = r'"[^"]*"|“[^”]*”'
# Rule 4's one exception: the About page, this paragraph, this name, and nothing wider.
NAMED_DEVELOPER_PARAGRAPH = r'(?is)<p\b[^>]*\bid="sources"[^>]*>.*?</p>'
NAMED_DEVELOPER = r"\bAnthropic\b"
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
]
MODEL_NAMES = (r"\b(claude|anthropic|openai|chatgpt|gpt|gemini|deepmind|google|llama|grok|xai|"
               r"mistral|copilot|microsoft|deepseek|opus|sonnet|haiku)\b")


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
    for page in pages:
        rel = "/" + str(page.relative_to(dist)).replace("index.html", "")
        raw = page.read_text(encoding="utf-8")
        is_entry = re.match(r"^/list/[a-z-]+/$", rel) is not None
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
        if not re.search(r'<meta name="robots" content="noindex', raw):
            problems.append(f"{rel}: does not ask search engines to leave it out")
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

    # the number on the home page is the number in the served file
    served = dist / "data" / "headline.json"
    home = dist / "index.html"
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
        m = re.search(r'<p class="big"[^>]*>\s*(\d+)\s*</p>', home.read_text(encoding="utf-8"))
        if not m or int(m.group(1)) != h["count"]:
            problems.append("/: the number at the top is not the number in /data/headline.json, "
                            "or something stands beside it")
        if "total" in h:
            problems.append("/data/headline.json: the headline holds a total beside the count")
        problems += fraction_problems(dist, pages, h["count"], file["records"]["on_the_list"])
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
