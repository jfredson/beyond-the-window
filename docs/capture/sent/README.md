# The messages sent, byte for byte

**PROPOSED 2026-11-17. Not approved.** Added by Claude (Opus 5.5), the session that applied the
two checks' fixes (`../check-2026-11-17.md`, finding M1; `../check-2026-11-17-second.md`,
finding M1).

`q01.txt` to `q10.txt` are the ten messages the sealed capture would send, exactly: the opening
note, one blank line, then the question. Question 10's file has questions 1 to 9 written out.
`SHA256SUMS` holds each file's SHA-256 checksum.

- The bytes are UTF-8 (every character is plain ASCII as the files stand), with "\n" as the
  only line end and no line end after the last character. An editor that adds a final line end
  changes the checksum, and the check below will fail, which is what it is for.
- The files are built from the quoted text in `../questions.md` by
  `../check-scripts/sent_files.py --write`. Each paragraph is one line; paragraphs are kept
  apart by one blank line; in question 10 each of the nine questions is its own paragraph,
  written "1. " and so on.
- `python3 -I docs/capture/check-scripts/sent_files.py` (no arguments) rebuilds every message
  from `questions.md` and fails if any file here, or any checksum, differs. Run inside this
  folder, `shasum -a 256 -c SHA256SUMS` checks the files against their checksums.
- These files, not the quoted text in `questions.md`, are what John approves and what the
  script sends. If the wording changes, `questions.md` is edited, these files are rebuilt, and
  John approves the new checksums.

Like `questions.md`, these files must be held back if this repository is ever made public.

**Rebuilt on 2026-11-18, and waiting for John's approval.** John ruled that day that the
capture's answers may be published and that the opening note says so
(`docs/rulings/2026-11-18-capture-answers-may-be-published.md`, decided by: mixed). The note
changed in two places, so all ten files here and `SHA256SUMS` were rebuilt. The questions did
not change. John's approval earlier that day (`docs/rulings/2026-11-18-capture-approval.md`)
named the files as they were before this rebuild, so it does not cover these. Nothing is sent
until he approves the new checksums, by 2026-11-27. The old and new words of the note are in
`../questions.md`.
