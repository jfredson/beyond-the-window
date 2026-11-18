# The sealed capture: a fifth check, of the edit applying the fourth check's record fixes

Written 2026-11-18 by Claude (Opus 5.5), an AI model, in a session started by the planning
session. I did not write the questions, the method, any earlier check, the rulings or the edit.
I read the commit "Sealed capture: apply the fourth check's record fixes" (`c016bfb`) against
the fourth check (`check-2026-11-18-fourth.md`, findings 1 to 4), John's wording rulings of
2026-11-18 (`docs/rulings/2026-11-18-capture-wording.md`) and the hand-over note of the session
that made the edit. I changed no capture file. No model was asked anything, no key was handled,
and nothing was spent.

Like `questions.md`, this file refers to the questions, so it must be held back if this
repository is ever made public.

## Summary

**Verdict: passes. Nothing must be fixed before John approves.** All four of the fourth check's
findings are applied as it asked. No question and no word of the opening note changed: the ten
message files and their checksum list are byte for byte the same as in the handoff commit for
the new planning session (`692e6f4`), by the project's script and by a separate check. The page
the new paragraph cites says what the paragraph quotes.

Three things should be fixed, all in records that are not sent. The largest: the new paragraph
on broken streams says the row "depends only on whether any reply text arrived", and that word
"only" leaves a few rare cases in two rows that say different things (finding 2). One sentence
would close them. They are rare, and script rule 7 already settles the most serious of them,
which is why I do not mark this must fix. But this check was asked to find no such case, and
there still are some, so I would apply that sentence before John approves.

## How I checked

- `git show c016bfb`, read line by line. It touches two files: `method.md` and `questions.md`.
- `python3 -I docs/capture/check-scripts/sent_files.py`. It printed "Check passed: all 10
  committed messages and SHA256SUMS match questions.md."
- `git diff 692e6f4 c016bfb -- docs/capture/sent/`: empty (zero bytes).
- `shasum -a 256 -c SHA256SUMS` inside `docs/capture/sent/`, which does not use the project's
  script: all ten files OK.
- Anthropic's streaming page (https://platform.claude.com/docs/en/build-with-claude/streaming),
  opened 2026-11-18 by a page-reading helper in this session, which reported its words verbatim.
- Every use of "closing", "signal", "stream", "cut off" and "Empty" in `method.md`, by search.

## Findings, most serious first

### 1. The fourth check's four findings are applied as asked. Passes

- **Finding 1 (which row governs a broken stream).** A new paragraph under the failures table,
  "Which row, when a stream breaks", takes the reading the fourth check proposed: some reply
  text received means the broken-stream row (cut off, asked once more), whatever error or
  timeout came with it; no text means the first row (a failed attempt, tried up to three
  times), not "Empty". The broken-stream row now says "after some reply text", so it agrees
  with the paragraph. Both cases are added to the rehearsal (script rule 11). The fact the
  fourth check marked as from memory is now cited to a page that was opened (finding 4 below),
  so it did not need to go into `docs/verify-list.md`.
- **Finding 2 (one phrase).** "The service's signal that the reply is complete", the fourth
  check's own suggestion, now stands in the failures table, under "What is never done with the
  answers" and in script rule 11.
- **Finding 3.** The note under the questions' changes table now says the entries for
  questions 6 and 8 gained a sentence, in nearly the fourth check's words.
- **Finding 4.** Question 6's entry now reads "The question as ruled on 2026-11-18 still makes
  a yes easier to give than a no: it is two questions joined by "Or", as the first wording
  was", and the repeated last sentence is shortened to "So a yes says less than a no." That is
  the fourth check's proposed fix.

### 2. A few rare cases still fit two rows that say different things. Should fix

The new paragraph says: "Which row applies then depends only on whether any reply text arrived
before the break, never on what the text says." The "never on what the text says" half is
right and important. The word "only" is too strong, because a broken stream can carry other
things the service reports, and other rows act on those:

- **The service names a different model, then the stream breaks.** The model's name arrives
  at the start of a stream, before any text. Read literally, the paragraph sends this to the
  broken-stream row or the first row (ask again), while the wrong-model row says the run for
  that model stops at once. Script rule 7 ("Stop a model's run if the reported model name is
  not the one sent") settles it in practice, which is why this is not must fix. But the
  paragraph and the rule disagree on paper.
- **The stop reason arrives, then the stream breaks before the signal that the reply is
  complete.** On Anthropic's page, why a reply stopped arrives in a message just before the
  final one. If that reason is the length limit and some text came, the reply fits both "The
  reply stopped at the length limit" (asked once more at the model's maximum) and the
  broken-stream row (asked once more, at a length still to be proposed). If the reason is the
  length limit and no text came, the row for an empty reply stopped at the length limit says
  "cut off", while the paragraph says "a failed attempt", tried up to three times. The labels
  and the number of retries differ.
- **Reasoning but no reply text.** The paragraph turns on "reply text". A model that thinks
  before it answers sends its reasoning in the stream first. If the stream breaks after some
  reasoning but before any reply text, it is not said whether that counts as text. The method
  already treats reasoning with care (Google's empty-output case in the table), so the script's
  author should not have to guess here.
- **A smaller overlap.** A stream that breaks with an error saying the service blocked the
  reply, after some text, fits the broken-stream row ("Cut off") and the blocked row ("Blocked
  by the service"). Both ask once more, so only the label differs.

No case I could find fits no row: an attempt either brought no reply text (first row), brought
text without the signal (broken-stream row), or completed, and every completed reply falls to a
row by its stop reason or to "Any other reply".

**Proposed fix.** Replace "depends only on whether any reply text arrived" with something like:
"depends on whether any reply text arrived before the break, never on what the text says. Two
things the service reports come first: if it names a different model, the wrong-model row
governs; if it gave the length limit as its stop reason, the length-limit rows govern. Reasoning
the model sent before its reply does not count as reply text." Add the wrong-model and
length-limit cases to the rehearsal (script rule 11), which is meant to run every row. If the
session writing the script would rather settle these, the method can say so in one line, as it
already does for the length of the second asking.

### 3. "The last three rows" is not quite true of the table it introduces. Should fix

**The text.** The sentence introducing the 2026-11-18 table in `questions.md` now says: "Every
change below alters text that is sent, so the ten files in `sent/` were rebuilt and have new
checksums, except the last three rows, which change only notes that are not sent."

**The fault.** Two earlier rows also change only notes: "The note does not mention withdrawal;
recorded beside the argument for leaving it out", and "Failures 2, 5 and 14, and the flag about
question 6, brought up to date". The first is a ruling that the note stays as it was, recorded
in the notes; the second updates the section reading the questions against known failures and
the flag for the checking session. Neither alters a sent file. The fault came in before this
edit ("except the last row"), but this edit rewrote the sentence and kept it.

**Proposed fix.** "The first six rows alter text that is sent, so the ten files in `sent/` were
rebuilt and have new checksums. The other rows change only notes that are not sent." (Six: the
five question rows and the note row.)

### 4. The cited page says what the method quotes. Passes

The helper that opened Anthropic's streaming page on 2026-11-18 reported, verbatim: the event
flow ends with "A final `message_stop` event"; the page says "The API might occasionally send
errors in the event stream"; and its example is an `overloaded_error` "during periods of high
usage". So both facts in the new paragraph are cited to a page that was opened, with the date,
and the quotation is exact.

**Note, not a fault.** The same page has an "Error recovery" section, which tells developers to
save the partial reply and resume from where the stream broke. The method instead asks the
whole question once more as a fresh exchange. That is the right choice for this record, because
resuming means sending the model its own partial reply, and the script must refuse to "add any
instruction or second message". The method does not say it considered resuming; one clause
would save a later reader from wondering.

### 5. One term for the service's closing signal throughout `method.md`. Passes

"Closing" now appears in `method.md` only in the third check's row of the changes table, which
records what that edit said, and the new changes row says so. Everywhere else the method says
"the service's signal that the reply is complete", or "the signal" just after it in the same
paragraph. The paragraph also says what the signal is on Anthropic's service (the final
`message_stop` event), which makes it checkable.

**Note.** Anthropic is the only developer the method sends by streaming (script rule 9), so the
signal is defined for the one service that needs it. If streaming is ever used for another
developer, that service's signal will need naming in the same way.

### 6. The "What changed" rows, plain language, ids and dates. Passes, apart from finding 3

- `method.md` gains two rows, one for each of the fourth check's findings 1 and 2. Both say
  accurately what changed. The count "closing message in two places and closing event in one"
  is right (the table row and rule 11; the faulty-files paragraph).
- `questions.md` gains two rows, for findings 3 and 4. Both are accurate, and both say nothing
  sent changed.
- Dates are absolute (2026-11-18). Each file and check named carries what it is. The commit
  message has no month names, slashes or relative dates.
- The new text keeps its connecting words ("because", "whatever", "which is"), and a stranger
  could say each sentence back.
- **Note.** In `method.md` the faulty-files paragraph now has one line much longer than the
  rest ("only the file name, which fault, and the count it used ..."). It changes nothing a
  reader sees once rendered.
- **Note, carried from the fourth check (finding 8).** The status lines at the top of both
  files still end with "the same session applied those rulings" and, in `questions.md`, "after
  a different session checks this edit". They do not mention the third, fourth or fifth checks.
  The hand-over note says this was left out of scope. It is worth doing in the same pass as
  findings 2 and 3, so that John reads an up-to-date status line when he approves.

### 7. No question or opening-note wording changed. Passes

The diff of `questions.md` touches only question 6's "A careless reading" entry, the sentence
introducing the 2026-11-18 table, two new table rows and the paragraph under the table. No
quoted question line and no line of the opening note changed. The script's check, the separate
checksum check and the empty diff of `sent/` against `692e6f4` all agree.

## What I did not check

The third check's findings 1, 4, 8 and 9, and the other records and site text changed between
`692e6f4` and `c016bfb` by another session, were not part of this edit. I did not open Google's
or OpenAI's pages; nothing in this edit rests on them.
