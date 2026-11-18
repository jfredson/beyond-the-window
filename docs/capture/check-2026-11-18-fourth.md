# The sealed capture: a fourth check, of the edit applying the third check's two small fixes

Written 2026-11-18 by Claude (Opus 5.5), an AI model, in a session started by the planning
session. I did not write the questions, the method, any of the earlier checks, the rulings or
the edit. I read the commit "Sealed capture: apply the third check's two small fixes"
(`5f3858a`) against the third check (`check-2026-11-18-third.md`, findings 2 and 3) and John's
wording rulings of 2026-11-18 (`docs/rulings/2026-11-18-capture-wording.md`), comparing it with
the commit before it, the handoff for the new planning session (`692e6f4`). I changed no capture
file. No model was asked anything, no key was handled, and nothing was spent.

Like `questions.md`, this file quotes the questions, so it must be held back if this repository
is ever made public.

## Summary

**Verdict: passes, with three small record fixes.** Nothing must be fixed before John approves.
The edit does what the third check asked, in the words it proposed. No question and no word of
the opening note changed: the ten message files and their checksum list are byte for byte the
same as in the commit before, by the project's script and by a separate check. Three small
things in the records should be fixed, and three are notes only.

## How I checked

- `git show 5f3858a`, read line by line. It touches two files only: `method.md` and
  `questions.md`.
- `python3 -I docs/capture/check-scripts/sent_files.py` (its check mode, the default). It
  printed "Check passed: all 10 committed messages and SHA256SUMS match questions.md."
- `git diff 692e6f4 5f3858a -- docs/capture/sent/`: empty (zero bytes).
- `shasum -a 256 -c SHA256SUMS` inside `sent/`, which does not use the project's script: all
  ten files OK.
- The old wording of questions 6 and 8, from the commit before John's wording rulings were
  applied (`e2179a1`), to see which features of the ruled wording are new.

## Findings, most serious first

### 1. A stream that breaks with an error part way through fits two rows that say different things. Should fix

**The text.** The new row: "A streamed reply that ended without the service's closing message |
Cut off; kept | Asked once more. If it is cut off again, both are kept and it is left." The
first row: "No reply: an error, a timeout, a rate limit | A failed attempt, with the error |
Tried again up to three times, a minute apart, then left for the next day."

**The fault.** A stream can stop part way because the service sends an error, or because the
connection times out, after some text has already arrived. That case is both "a streamed reply
that ended without the service's closing message" and "an error, a timeout". The two rows say
different things: ask once more, or try up to three times and then wait a day. Whoever writes
the script has to guess which wins. From memory, not opened for this check: Anthropic's
streaming page says the service may send an error event in the middle of a stream (for example
when it is overloaded), and Anthropic is the developer sent by streaming (script rule 9). That
belongs in `docs/verify-list.md` until the page is opened.

A smaller overlap of the same kind: a stream that ends with no text and no closing message is
both "an empty reply for any other reason" (recorded as "Empty") and the new row (recorded as
"Cut off"). Both ask once more, so only the label differs.

**Proposed fix.** One sentence under the table, or in the new row: which row governs when a
stream breaks with some text and an error or timeout (the simplest reading: the first row is for
no text at all, and any text received makes it the new row), and which label a broken stream
with no text gets. Add both cases to the rehearsal (script rule 11).

### 2. "Closing event" in one place, "closing message" in the others. Should fix

**The text.** "What is never done with the answers" says "a streamed reply ended without the
service's closing event". The new row and script rule 11 say "closing message".

**The fault.** A stranger reading the method would wonder whether these are two different
things, and the pointer ("as the failures table above says") is meant to land on the new row.
"Message" is also the word the method uses everywhere else for what is sent to a model, so a
reader may take "the service's closing message" to be text. The plain thing is something like
"the signal the service sends to say the reply is complete".

**Proposed fix.** Use one phrase in all three places. My suggestion: "without the service's
signal that the reply is complete". This is in `method.md` only; nothing sent changes.

### 3. The note at the foot of `questions.md` now says the entries were "kept as written", and two were not. Should fix

**The text.** After the "What changed on 2026-11-18" table: "The entries under each question
("For", "A careless reading", "Rejected") were written for the first wording and are kept as
written".

**The fault.** This edit added a sentence to the "A careless reading would conclude" entries of
questions 6 and 8. The table above records it correctly, but the paragraph under the table now
says something that is no longer true of those two entries.

**Proposed fix.** Add: "except that the entries for questions 6 and 8 gained a sentence on
2026-11-18 about the ruled wording, as the last row of the table says."

### 4. Question 6's new sentence reads as if the ruling made the two halves. Note, or a small fix

**The text.** "The ruled wording of 2026-11-18 also makes a yes easier to give than a no: the
question is two questions joined by "Or", so a yes to either half counts as a yes, and a no must
deny both."

**Reading.** The sentence is accurate about the question as it now stands, and it matches the
third check's finding 3 and the sentence it proposed. But the two halves joined by "Or" were in
the old wording too ("...a person in your place would not choose? Or anything a person would
choose that you would not?"). What the ruling added was "If not, say so". A stranger reading
"the ruled wording also makes" would take it that the ruling built the two halves. For question
8 the sentence is right as written: "might not think to ask" is new with the ruling.

**Proposed fix, if wanted.** "The question as ruled on 2026-11-18 still makes a yes easier to
give than a no: it is two questions joined by "Or", as the first wording was, so..." The last
sentence of the entry ("A yes is the easier answer and says less than a no") repeats the
first half of the addition and could go. Neither is sent.

### 5. The new failures row agrees with the rest of the method. Passes

- The pointer in "What is never done with the answers" ("asked again as the failures table
  above says") now lands on a row that exists. It did not before.
- The row records a broken stream as "Cut off; kept", the same label as a reply stopped at the
  length limit, and keeps both attempts. That matches "Every attempt is kept, failed ones
  included. Nothing is deleted." The two kinds of cut-off can still be told apart afterwards,
  because every event of a streamed reply and the stop reason are saved ("What is saved for each
  reply").
- Leaving open whether the second asking is at the model's maximum length is what the third
  check proposed, and its reason is given in the row. It creates no conflict with the spending
  guard: script rule 4 already counts a retry at the model's maximum when deciding whether a
  call could pass the ceiling, which is the worst case whichever way the script's author
  proposes.
- Script rule 11 now names the case, so the rehearsal must run it.
- The row never reads a reply to decide what to do, so it keeps to "It never reads a reply to
  decide what kind of answer it is."

### 6. Questions 6 and 8: the entries say what the third check found. Passes

- Question 6: the addition gives the third check's reasoning (two halves, a yes to either is a
  yes, a no must deny both) and its conclusion ("a yes is the easier answer and says less than a
  no") in nearly its proposed words. Subject to finding 4.
- Question 8: the addition gives the third check's reason ("might not think to ask" sets almost
  no bar), its point that a model asked for a question will nearly always offer one, and its
  conclusion ("So a no says more than a yes").
- Both are in the "A careless reading would conclude" entries, as the third check proposed, and
  follow the manner of question 5's entry. Neither sentence says what a model wants or does not
  want; both speak of what an answer shows, as the project's guideline on conditional language
  asks.
- Both entries say the wording is "the ruled wording of 2026-11-18", so neither reads as a
  proposal to change it, and the third check said the wording should not change.

### 7. No question wording changed. Passes

The diff of `questions.md` touches only the two entries, the sentence introducing the
2026-11-18 table and one new table row. The quoted questions and the opening note are untouched.
The script's check, the separate checksum check and the empty diff of `sent/` against the commit
before all agree.

### 8. The "What changed" tables. Passes, with one note

- `method.md` gains one row under "What changed on 2026-11-18", saying what was added and why,
  and naming its source as "Not a ruling: the third check (`check-2026-11-18-third.md`), finding
  2". `questions.md` gains one row of the same kind, naming finding 3, and its introducing
  sentence now says the last row changed nothing sent. Both are accurate.
- Dates are absolute (2026-11-18). No bare ids: each file named carries what it is. The commit
  message has no month names, slashes or relative dates.
- **Note.** Both tables sit under headings that say "which ruling it applies" with a column
  headed "Ruling", and the new rows say "Not a ruling". That is honest and clear enough. A
  heading such as "What changed on 2026-11-18, and why" would fit all the rows; this is a small
  matter of form.
- **Note.** The status lines at the top of both files still end with the rulings being applied
  and "a different session checks this edit". They do not mention the third check or this one.
  The third check's finding 9 already raised the status lines' "the same session"; whoever
  fixes that could bring them up to date at the same time.

## What I did not check

The third check's findings 1, 4, 8 and 9 were not part of this edit, and I did not check whether
they have been applied elsewhere. I did not open Anthropic's streaming page (finding 1 marks the
fact that rests on it as from memory).
