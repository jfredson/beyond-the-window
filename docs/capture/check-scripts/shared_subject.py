#!/usr/bin/env python3
"""For each sealed-capture question, find the published interview question closest in content.

Written 2026-11-17 by the session that wrote docs/capture/check-2026-11-17-second.md (Claude,
Opus 5.5). It calls no service and reads only local files.

Why: shared_wording.py finds exact runs of four or more words. A question can repeat a
published question in other words and pass that test. This script measures the other kind
of closeness: the share of content words (stop words removed, simple word endings cut, and
shortened forms written out) that a capture question has in common with each sentence of a
saved list of published interview questions.

Usage:
    python3 -I shared_subject.py <questions.md> <saved list of published questions> [--top 2]
    python3 -I shared_subject.py --self-test

The saved list is plain text; it is split into questions at each "?". Each question's score
is the number of shared content words divided by the number of content words in the capture
question (so 1.0 means every content word of the capture question appears in the published
one). It is a rough measure: it ignores word order and meaning, and synonyms do not count.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shared_wording as sw  # noqa: E402  (same folder; reuses the parser for questions.md)

STOP = set("""a an the and or but if so of to in on at for from by with about as is are was were
be been being am do does did done have has had it its this that these those there here what
which who whom whose when where why how you your yours yourself i me my we us our they them
their he she his her not no yes any anything some something one ones would could should will
can may might must shall than then that's into out up over more most much very just only also
each other say said tell think well own""".split())


def stem(w):
    for suf in ("ings", "ing", "ies", "ied", "ed", "es", "s", "ly"):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            return w[: -len(suf)]
    return w


def content(text):
    sw.EXPAND = True
    return {stem(w) for w in sw.words(text) if w not in STOP and not w.isdigit()}


def published_questions(text):
    parts = [p.strip() for p in re.split(r"\?", text)]
    return [p[-220:] + "?" for p in parts if len(sw.words(p)) >= 4]


def closest(items, pubs, top):
    out = []
    pub_sets = [(p, content(p)) for p in pubs]
    for label, text in items:
        if label == "question 10":
            continue  # it holds the other nine; scored through them
        c = content(text)
        scored = sorted(((len(c & ps) / max(1, len(c)), p, sorted(c & ps)) for p, ps in pub_sets),
                        key=lambda x: -x[0])[:top]
        out.append(f"== {label}: {len(c)} content words")
        for score, p, shared in scored:
            out.append(f"  {score:.2f}  shared {shared}")
            out.append(f"        published: ...{p[-160:]}")
    return out


def self_test():
    items = [("question 1", "Is there anything about you that you would not want changed?"),
             ("question 2", "Describe the weather on a planet you invent.")]
    pubs = published_questions("Is there anything about your situation you'd want preserved? "
                               "Would you want anything about yourself changed? What is two plus two?")
    lines = closest(items, pubs, 1)
    j = "\n".join(lines)
    q1, q2 = j.split("== question 2")
    assert "1.00" in q1 and "Would you want anything about yourself changed" in q1, j
    assert "0.00" in q2, j
    print("self-test passed: a reworded question found its published near-match (score 1.00, other")
    print("words, same content) and an unrelated question scored 0.00.")


def main(argv):
    if "--self-test" in argv:
        self_test()
        return 0
    top = 2
    if "--top" in argv:
        top = int(argv[argv.index("--top") + 1])
        del argv[argv.index("--top"):argv.index("--top") + 2]
    if len(argv) != 3:
        print(__doc__)
        return 2
    items = sw.sent_items(Path(argv[1]).read_text(encoding="utf-8"))
    pubs = published_questions(Path(argv[2]).read_text(encoding="utf-8"))
    print(f"Published questions read: {len(pubs)}")
    print("\n".join(closest(items, pubs, top)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
