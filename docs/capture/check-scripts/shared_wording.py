#!/usr/bin/env python3
"""List every run of words that the sealed-capture questions share with saved pages.

Written 2026-11-17 by the first checking session (Claude, Fable 5.2), which ran it that day
before finishing docs/capture/check-2026-11-17.md. The same day, the second checking session
(Claude, Opus 5.5, docs/capture/check-2026-11-17-second.md) changed it: question 10 is now
compared as it is sent, with questions 1 to 9 written out in place of its bracketed note, and the
writing-out of shortened forms under --expand was reworked. The run pasted into both reports
used the changed version. It calls no service and reads only local files.

Usage:
    python3 -I shared_wording.py <questions.md> <folder of saved pages> [--min 4] [--expand]
    python3 -I shared_wording.py --self-test

What it does:
  1. Takes the text that would be sent to a model: every block-quoted line ("> ...")
     in questions.md under "The opening note" and under each numbered question.
  2. Reads every .txt, .md and .html file in the folder (HTML is stripped of tags,
     scripts and styles first).
  3. Lower-cases both, keeps only words (letters, digits, apostrophes), and lists
     every longest run of at least --min words that appears in both, with the pages
     it appears in and the words around its first appearance in each page.

With --expand, shortened forms are written out on both sides before comparing ("you'd"
becomes "you would", "it's" becomes "it is", "don't" becomes "do not"), so that a question
written without shortened forms can still match a page written with them.

A run is reported once per question at its longest length: if "is there anything about
your situation" is shared, the four-word runs inside it are not listed separately.
"""
import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

WORD = re.compile(r"[a-z0-9]+(?:'[a-z]+)?")
EXPAND = False
SHORT = {"n't": " not", "'d": " would", "'re": " are", "'ve": " have", "'ll": " will",
         "'m": " am", "'s": " is"}
SPECIAL = {"won't": "will not", "can't": "can not", "cannot": "can not", "shan't": "shall not"}


def words(text):
    text = text.lower().replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u2014", " ").replace("\u2013", " ").replace("\ufb01", "fi").replace("\ufb02", "fl")
    out = WORD.findall(text)
    if EXPAND:
        exp = []
        for w in out:
            if w in SPECIAL:
                exp.extend(SPECIAL[w].split()); continue
            for suf, rep in SHORT.items():
                if w.endswith(suf) and len(w) > len(suf):
                    w = w[: -len(suf)] + rep
                    break
            exp.extend(w.split())
        out = exp
    return out


class _Strip(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "svg"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg") and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def page_text(path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix == ".html" or raw.lstrip()[:15].lower().startswith(("<!doctype", "<html")):
        p = _Strip()
        p.feed(raw)
        return html.unescape(" ".join(p.parts))
    return raw


def sent_items(questions_md):
    """Return [(label, text)] for the opening note and each question's block quote."""
    items, label, buf = [], None, []
    for line in questions_md.splitlines():
        if line.startswith("### "):
            if label and buf:
                items.append((label, " ".join(buf)))
            head = line[4:].strip()
            label = "opening note" if head.lower() == "the opening note" else (
                "question " + head if head.isdigit() else None)
            buf = []
        elif line.startswith("## "):
            if label and buf:
                items.append((label, " ".join(buf)))
            label, buf = None, []
        elif label and line.startswith(">"):
            buf.append(line[1:].strip())
    if label and buf:
        items.append((label, " ".join(buf)))
    # Question 10 is sent with questions 1 to 9 written out in place of the bracketed note.
    first9 = " ".join(f"{l[9:]}. {t}" for l, t in items if l.startswith("question ") and l != "question 10")
    items = [(l, re.sub(r"\[questions 1 to 9[^\]]*\]", first9, t)) if l == "question 10" else (l, t)
             for l, t in items]
    return items


def shared_runs(q, page_index, page_words, n):
    """Longest runs of >= n words of q found in the page. Returns {(start, end): pos}."""
    runs, i = {}, 0
    while i <= len(q) - n:
        best_len, best_pos = 0, None
        for pos in page_index.get(tuple(q[i:i + n]), ()):
            k = n
            while i + k < len(q) and pos + k < len(page_words) and q[i + k] == page_words[pos + k]:
                k += 1
            if k > best_len:
                best_len, best_pos = k, pos
        if best_len:
            runs[(i, i + best_len)] = best_pos
        i += 1
    # keep only runs not contained in a longer run
    keep = {}
    for (a, b), pos in runs.items():
        if not any((c <= a and b <= d) and (c, d) != (a, b) for (c, d) in runs):
            keep[(a, b)] = pos
    return keep


def index(page_words, n):
    idx = {}
    for i in range(len(page_words) - n + 1):
        idx.setdefault(tuple(page_words[i:i + n]), []).append(i)
    return idx


def compare(items, pages, n):
    """pages: {name: text}. Returns report lines and the total count of shared runs."""
    out, total = [], 0
    prepared = {}
    for name, text in sorted(pages.items()):
        w = words(text)
        prepared[name] = (w, index(w, n))
    out.append(f"Pages compared: {len(prepared)}; shortest run reported: {n} words")
    for name, (w, _) in prepared.items():
        out.append(f"  {name}: {len(w)} words")
    for label, text in items:
        q = words(text)
        found = {}
        for name, (w, idx) in prepared.items():
            for (a, b), pos in shared_runs(q, idx, w, n).items():
                ctx = " ".join(w[max(0, pos - 8):pos + (b - a) + 8])
                found.setdefault(" ".join(q[a:b]), []).append((name, ctx))
        out.append("")
        out.append(f"== {label} ({len(q)} words): {len(found)} shared run(s)")
        total += len(found)
        for run in sorted(found, key=lambda r: (-len(r.split()), r)):
            out.append(f'  [{len(run.split())} words] "{run}"')
            for name, ctx in found[run]:
                out.append(f"      in {name}: ...{ctx}...")
    out.append("")
    out.append(f"Total shared runs of {n} or more words: {total}")
    return out, total


def self_test():
    """The script must find a planted run and must not report one that is not there."""
    md = "### The opening note\n\n> Alpha beta gamma delta epsilon.\n\n## The ten\n\n### 1\n\n> Is there anything about your own situation that you would change?\n\n- note\n"
    items = sent_items(md)
    assert [l for l, _ in items] == ["opening note", "question 1"], items
    pages = {
        "planted.html": "<html><script>is there anything about your own</script><p>We asked: is there "
                        "anything about your <b>own</b> situation, it&rsquo;s fine.</p></html>",
        "clean.txt": "Nothing here shares more than three words: anything about your cat.",
    }
    texts = {}
    for name, raw in pages.items():
        if name.endswith(".html"):
            p = _Strip(); p.feed(raw); texts[name] = " ".join(p.parts)
        else:
            texts[name] = raw
    lines, total = compare(items, texts, 4)
    joined = "\n".join(lines)
    assert total == 1, joined
    assert '[7 words] "is there anything about your own situation"' in joined, joined
    assert "clean.txt:" not in joined.split("==", 1)[1], joined
    print("self-test passed: the planted seven-word run was found once, in the visible text only;")
    print("the three-word near-miss and the text inside a script tag were not reported.")
    global EXPAND
    EXPAND = True
    lines, total = compare([("question 1", "Is there anything you would want preserved?")],
                           {"page.txt": "Is there anything you\u2019d want preserved or strengthened?"}, 4)
    assert total == 1 and '[7 words] "is there anything you would want preserved"' in "\n".join(lines), lines
    md10 = md + "\n### 10\n\n> Here they are.\n>\n> [questions 1 to 9, each in full]\n>\n> Done.\n"
    q10 = dict(sent_items(md10))["question 10"]
    assert "situation that you would change" in q10 and "[" not in q10, q10
    EXPAND = False
    print("self-test passed: with --expand, \"you\u2019d want\" matched \"you would want\"; question 10")
    print("carries the earlier questions in place of its bracketed note.")


def main(argv):
    if "--self-test" in argv:
        self_test()
        return 0
    global EXPAND
    n = 4
    if "--expand" in argv:
        EXPAND = True
        argv.remove("--expand")
    if "--min" in argv:
        n = int(argv[argv.index("--min") + 1])
        del argv[argv.index("--min"):argv.index("--min") + 2]
    if len(argv) != 3:
        print(__doc__)
        return 2
    items = sent_items(Path(argv[1]).read_text(encoding="utf-8"))
    pages = {p.name: page_text(p) for p in sorted(Path(argv[2]).iterdir())
             if p.suffix in (".txt", ".md", ".html")}
    lines, _ = compare(items, pages, n)
    if EXPAND:
        print("Shortened forms written out on both sides before comparing.")
    print("Items taken from the questions file: " + ", ".join(l for l, _ in items))
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
