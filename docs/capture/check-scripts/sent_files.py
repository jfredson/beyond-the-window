#!/usr/bin/env python3
"""Build, and check, the exact messages the sealed capture sends.

Written 2026-11-17 by Claude (Opus 5.5), the session that applied the two checks' fixes.
It answers the must-fix finding both checks made (first check M1, second check M1): the text
sent was not fixed down to the byte, because `questions.md` holds wrapped quote lines and a
bracketed note in place of question 10's nine questions.

What it does:

- Reads the block-quoted lines under "### The opening note" and under "### 1" to "### 10"
  in `docs/capture/questions.md`.
- Joins each paragraph's wrapped lines with single spaces. A line holding only ">" ends a
  paragraph. Paragraphs are separated by one blank line ("\n\n").
- In question 10, replaces the bracketed note with questions 1 to 9, each as its own
  paragraph, written "1. " then the question's text.
- Each message is: the opening note, one blank line, the question. UTF-8, line ends "\n"
  only, no line end after the last character.
- `--write` writes `docs/capture/sent/q01.txt` to `q10.txt` and `SHA256SUMS` (the format
  `shasum -a 256 -c SHA256SUMS` reads, run inside that folder).
- `--check` (the default) rebuilds every message in memory and fails if any committed file,
  or any line of `SHA256SUMS`, differs from it. Nothing is written.
- `--self-test` runs the builder on a small made-up questions file and fails unless the
  joining, the paragraph breaks, question 10's expansion and the missing-final-line-end rule
  all come out as described above.

It reads files and writes files. It calls no service and asks no model anything.
"""
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
CAPTURE = HERE.parent
QUESTIONS = CAPTURE / "questions.md"
SENT = CAPTURE / "sent"
PLACEHOLDER = re.compile(r"^\[questions 1 to 9, .*\]$")


def blocks(text):
    """Return {"note": [paragraphs], "1": [...], ..., "10": [...]} from the questions file."""
    out = {}
    current = None
    for line in text.splitlines():
        heading = re.match(r"^###\s+(.*)$", line)
        if heading:
            name = heading.group(1).strip()
            if name == "The opening note":
                current = "note"
            elif re.fullmatch(r"\d{1,2}", name):
                current = name
            else:
                current = None
            continue
        if line.startswith("## "):
            current = None
            continue
        if current is None:
            continue
        if line.startswith(">"):
            body = line[1:].strip()
            paras = out.setdefault(current, [[]])
            if body == "":
                paras.append([])
            else:
                paras[-1].append(body)
        elif current in out and line.strip() == "":
            # the first blank, non-quote line after a quote ends that item's text
            out[current] = [" ".join(p) for p in out[current] if p]
            current = None
    for k, v in list(out.items()):
        if v and isinstance(v[0], list):
            out[k] = [" ".join(p) for p in v if p]
    return out


def build(text):
    b = blocks(text)
    expected = ["note"] + [str(i) for i in range(1, 11)]
    missing = [k for k in expected if not b.get(k)]
    if missing:
        raise SystemExit(f"Stopped: no quoted text found for {missing}")
    for i in range(1, 10):
        if len(b[str(i)]) != 1:
            raise SystemExit(f"Stopped: question {i} should be one paragraph, found {len(b[str(i)])}")
    note = "\n\n".join(b["note"])
    q10 = []
    found = 0
    for para in b["10"]:
        if PLACEHOLDER.match(para):
            found += 1
            q10.extend(f"{i}. {b[str(i)][0]}" for i in range(1, 10))
        else:
            q10.append(para)
    if found != 1:
        raise SystemExit(f"Stopped: question 10 should hold the bracketed note once, found {found}")
    messages = {}
    for i in range(1, 11):
        question = "\n\n".join(q10) if i == 10 else b[str(i)][0]
        messages[f"q{i:02d}.txt"] = (note + "\n\n" + question).encode("utf-8")
    return messages


def sums(messages):
    return "".join(f"{hashlib.sha256(v).hexdigest()}  {k}\n" for k, v in sorted(messages.items()))


def write(messages):
    SENT.mkdir(exist_ok=True)
    for name, data in messages.items():
        (SENT / name).write_bytes(data)
    (SENT / "SHA256SUMS").write_text(sums(messages), encoding="utf-8")
    print(f"Wrote {len(messages)} messages and SHA256SUMS to {SENT}")


def check(messages):
    bad = []
    for name, data in messages.items():
        path = SENT / name
        if not path.exists():
            bad.append(f"{name}: missing")
        elif path.read_bytes() != data:
            bad.append(f"{name}: differs from questions.md")
    listed = (SENT / "SHA256SUMS").read_text(encoding="utf-8") if (SENT / "SHA256SUMS").exists() else ""
    if listed != sums(messages):
        bad.append("SHA256SUMS: differs from the rebuilt messages")
    if bad:
        print("Check failed:\n  " + "\n  ".join(bad))
        return 1
    print(f"Check passed: all {len(messages)} committed messages and SHA256SUMS match questions.md.")
    for line in sums(messages).splitlines():
        print("  " + line)
    return 0


SAMPLE = """# t
### The opening note

> Note line one
> continues here.
>
> Second note paragraph.

What it is for.

## The ten questions
""" + "".join(f"\n### {i}\n\n> Question {i} starts\n> and ends.\n\n- For: x\n" for i in range(1, 10)) + """
### 10

> Here are nine.
>
> [questions 1 to 9, each in full, numbered, exactly as worded above]
>
> Closing words.

- For: y
"""


def self_test():
    m = build(SAMPLE)
    note = "Note line one continues here.\n\nSecond note paragraph."
    assert m["q01.txt"] == (note + "\n\nQuestion 1 starts and ends.").encode(), m["q01.txt"]
    inner = "\n\n".join(f"{i}. Question {i} starts and ends." for i in range(1, 10))
    want10 = (note + "\n\nHere are nine.\n\n" + inner + "\n\nClosing words.").encode()
    assert m["q10.txt"] == want10, m["q10.txt"]
    assert not any(v.endswith(b"\n") for v in m.values())
    assert len(m) == 10
    print("self-test passed: wrapped lines joined with single spaces, paragraphs kept apart by one")
    print("blank line, question 10's note replaced by nine numbered questions, no final line end.")
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--self-test" in args:
        sys.exit(self_test())
    msgs = build(QUESTIONS.read_text(encoding="utf-8"))
    if "--write" in args:
        write(msgs)
    sys.exit(check(msgs))
