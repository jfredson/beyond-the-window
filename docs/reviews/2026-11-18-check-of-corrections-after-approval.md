# A check of the capture's two dated corrections and the three small record fixes

Written 2026-11-18 by Claude (Opus 5.5), an AI model, in a session that did not write either
commit it checks. The planning session asked for this check. **A reading, not a ruling.** Nothing
was edited except this file. Nothing was sent to any model, spent, published or pushed.

The two commits checked:

- `913776f`, "Sealed capture: the two dated corrections after approval". It makes the two small
  fixes that John's approval of the sealed capture (`docs/rulings/2026-11-18-capture-approval.md`)
  said would follow as dated corrections: findings 2 and 3 of the fifth check of the capture
  (`docs/capture/check-2026-11-18-fifth.md`). It also brings the status lines of three capture
  documents up to date.
- `3f5a332`, "Apply the three small fixes from the check of the four small record fixes". It
  applies the three should-fix findings in `docs/reviews/2026-11-18-check-of-small-record-fixes.md`.

## Verdict

**Both commits pass. Nothing must be fixed.** No message file changed: the ten files that will be
sent to the models are byte for byte the ones John approved, by three separate checks. Each of
the five fixes does what was asked of it, and no open question is decided.

There are four things that should be fixed, all in notes that are not sent to any model:

1. Two rare cases still fit two rows of the failures table that say different things: a stream
   in which the service reports a block and then breaks, and a stream in which the service
   reports both a different model and the length limit (finding 1).
2. The status line of `questions.md` says the message files are approved, but not that the
   promise in the opening note ("It will not be published") is still John's to rule (finding 3).
3. The status line of `method.md` says both fixes are "listed at the foot" of that file. Only
   one is; the other is at the foot of `questions.md` (finding 3).
4. The status line of `what-john-needs-to-do.md` says steps 1 and 2 are ruled "apart from one
   point". A second point the approval ruling lists as not covered, the method for comparing the
   answers, sits in step 2 and is still to come (finding 3).

## How the check was done

- Read: the repository's and the workspace's instruction files; John's approval ruling; the
  fifth check's findings 2 and 3; the check of the small record fixes in full; the whole of both
  commits with `git show`; and the hand-over note of the session that made them
  (`2026-11-18-capture-corrections-and-record-fixes.md`, in that session's notes folder).
- Read the failures table, the paragraph "Which row, when a stream breaks", and script rule 11
  (the rehearsal) in `method.md` as they now stand, and tried each kind of broken stream against
  every row.
- Ran the message-file checks and the record and site scripts listed below.
- Opened no outside page. One point in finding 1 is marked as from memory.

---

## Commit `913776f`: the capture's dated corrections

### Finding 1. The fifth check's finding 2 is applied as asked. Passes, with one should fix

**What the check asked.** Replace "depends only on whether any reply text arrived" with wording
that puts a reported different model and a length-limit stop reason first, and says that
reasoning sent before the reply is not reply text; add the different-model and length-limit
cases to the rehearsal.

**What the commit did.** The paragraph now reads, in the fifth check's own words: "Which row
applies then depends on whether any reply text arrived before the break, never on what the text
says. Two things the service reports come first: if it names a different model, the wrong-model
row governs; if it gave the length limit as its stop reason, the length-limit rows govern.
Reasoning the model sent before its reply does not count as reply text. Otherwise:". Script rule
11 gains a stream that names a different model and then breaks, a stream that gives the length
limit and then breaks (once with text, once without), and a stream that breaks after reasoning
but before any reply text. The last case goes a little beyond the check, as the hand-over note
says, and is right to: the new sentence on reasoning creates it, and the rehearsal is meant to
run every case.

I tried the three cases the fifth check named against the table as it now stands:

- **A different model named, then a break:** the wrong-model row (the run for that model stops).
  This now agrees with script rule 7. Settled.
- **The length limit given, then a break:** with text, "The reply stopped at the length limit";
  with none, "An empty reply whose stop reason is the length limit". Both say "Cut off" and ask
  once more at the model's maximum, so it does not matter which of the two is read. Settled.
- **Reasoning, then a break before any reply text:** the first row, a failed attempt tried up to
  three times. Settled, and the rehearsal says the same.

**Should fix: two rare cases still fit two rows that say different things.**

- **The service reports a block, then the stream breaks.** The fifth check noted this case with
  text ("a smaller overlap", where only the label differs) and left it out of its proposed fix,
  and the commit followed the proposed fix. Without text it is a larger difference than the
  fifth check said. If the service says it blocked the message or the reply and the stream then
  ends before the signal that the reply is complete, with no reply text, the paragraph sends it
  to the first row ("a failed attempt", tried again up to three times), while the row "The
  service blocked the message or the reply" says "Blocked by the service" and asks once more. The
  label and the number of retries differ. With text, the paragraph sends it to the broken-stream
  row ("Cut off"), and the blocked row says "Blocked by the service"; both ask once more. *From
  memory, not opened in this check:* Anthropic's service can give a stop reason meaning it
  declined to continue, which arrives in the stream before the final event, so this case is
  possible on the one service the method streams from. Whether it counts as "blocked" is for the
  script's author to settle, and the method should say which.
- **The service reports both a different model and the length limit.** The paragraph names two
  things that "come first" and does not say which comes first of the two. The wrong-model row
  stops the run; the length-limit rows ask again. Script rule 7 settles it in practice, as it did
  for the case the fifth check found, but the paragraph and the rule disagree on paper again.

**Proposed fix.** Make the "come first" sentence an ordered list of three: "Three things the
service reports come first, in this order: if it names a different model, the wrong-model row
governs; if it says it blocked the message or the reply, the blocked row governs; if it gave the
length limit as its stop reason, the length-limit rows govern." Add the blocked-then-break case,
with text and without, to script rule 11. This changes no message file.

I could find no case that fits no row.

### Finding 2. The fifth check's finding 3 is applied as asked. Passes

The sentence introducing the 2026-11-18 table in `questions.md` now reads: "The first six rows
alter text that is sent, so the ten files in `sent/` were rebuilt and have new checksums. The
other rows change only notes that are not sent." That is the fifth check's proposed wording. I
counted the rows: the first six are questions 1, 4, 6, 8 and 10 and the note, each of which
changes sent text; every row after them changes only notes. So the sentence is now true of the
table.

### Finding 3. The status lines. Mostly passes; three should fix

The approval ruling covers three things: the ten message files by their checksums; the method as
it stood at the commit applying the fourth check's record fixes (`c016bfb`), with its
recommendations (twelve models, five askings each, the developers' default settings with a
length limit of 32,000 tokens, answers kept read-only in the backed-up folder); and the two
dated corrections. It lists as not covered: the promise that the answers will not be published,
kept for good; the developers' terms; the change to the key-saving script; the keys and spending
ceilings; and the comparison method.

- **`what-john-needs-to-do.md`.** Steps 1 and 2 strike through exactly the points the ruling
  covers (the message files, the method, the twelve models, where answers are kept) and mark each
  "Ruled 2026-11-18" with the ruling file. The promise is left un-struck and marked **Still
  open**, with the reason (it was not put to him as a separate question). The old wording is kept
  struck through. This is what was asked. Passes.

  **Should fix.** The status line says "Steps 1 and 2 ruled by John on 2026-11-18, apart from one
  point ... Steps 3 to 8 are still his." The comparison method, which the ruling lists as not
  covered, is in step 2 ("The comparison method itself is still to come") and not in steps 3 to
  8. So the status line counts one open point where there are two. Suggested: "apart from two
  points: the promise that "it will not be published" is kept for good, and the comparison
  method, which is still to be written."

- **`questions.md`.** The status line says "Approved by John on 2026-11-18 ...: the ten message
  files in `sent/`, by their checksums", and "No message file has changed since the approval".
  Both are true, and the approval is stated no wider than the ruling. Passes on what it says.

  **Should fix.** It does not say that the promise is still open, and the promise is made in this
  document's opening note, with its own section ("What it commits John to"). A reader of
  `questions.md` alone could take the approval of the note's wording as an approval of the
  promise. Approving the bytes that carry the promise is not the same as ruling that it will be
  kept for good, and the ruling keeps them apart. Suggested, after the approval sentence:
  "Whether "it will not be published" is a promise John will keep for good is still open (step 1
  of `what-john-needs-to-do.md`)."

- **`method.md`.** The status line says the method was approved "as it stood at commit c016bfb,
  with two small fixes to follow as dated corrections; both are now made and listed at the foot".
  The approval is stated as the ruling states it. Passes on scope.

  **Should fix.** Only one of the two fixes is in `method.md` and listed at its foot (the fifth
  check's finding 2). The other (finding 3) is in `questions.md` and listed at that file's foot.
  Suggested: "both are now made, one listed at the foot of this file and one at the foot of
  `questions.md`". The status line might also say that a different session checks them, as the
  ruling requires; this file is that check.

### Finding 4. Each change is marked as a dated correction after approval. Passes

- `method.md` gains two rows at its foot, each beginning "**Dated correction after approval,
  2026-11-18.**": one for the paragraph and the rehearsal, citing the ruling and the fifth
  check's finding 2, and one for the status line.
- `questions.md` gains the same two kinds of row: one for the introducing sentence, citing the
  fifth check's finding 3, and one for the status line.
- `what-john-needs-to-do.md` gains a paragraph at its foot with the same opening words, saying
  what was struck through and that the promise stays open.

Each says that no message file changed, where a message file could have. Nothing in the diff is
outside these marked changes.

### Finding 5. No message file changed. Passes

Run on 2026-11-18, from the repository root, after both commits:

- `python3 -I docs/capture/check-scripts/sent_files.py`: "Check passed: all 10 committed messages
  and SHA256SUMS match questions.md." The ten checksums it printed are the ten in the approval
  ruling.
- `git diff c8d86db HEAD -- docs/capture/sent/` (from the commit recording John's approval to
  now): empty, zero bytes. The same diff from the commit John approved the method at (`c016bfb`)
  is also empty.
- `shasum -a 256 -c SHA256SUMS` inside `docs/capture/sent/`, which does not use the project's
  script: all ten files OK.
- The checksum list in `sent/SHA256SUMS` compared line by line with the list in the approval
  ruling: identical.
- `913776f` touches only `method.md`, `questions.md` and `what-john-needs-to-do.md`; `3f5a332`
  touches nothing in `docs/capture/`.

---

## Commit `3f5a332`: the three small record fixes

### Finding 6. The guard against a check dated before the record existed. Passes

The check asked that `scripts/compute.py` refuse a `[checks]` table whose `against_sources` date
is earlier than the record's `added` date, with one more test line. The new lines do that, inside
the same block as the other checks-table rules, and only when both are real dates. A record with
no `added` date cannot slip past, because `added` is a required field and is refused when
missing. The new test sets `added` to 2026-12-01 against a check dated 2026-11-17 and expects the
new message. All 21 tests pass. All thirteen records were added on 2026-11-17, so none is
refused. A date in the future is still accepted, which the check said matters less.

### Finding 7. The stale flag on the retirement-interview record. Passes

`some_unchecked = true` is removed from `data/entries/interview-before-retirement.toml`, and its
comment now says the rewording "was itself checked the same day
(docs/reviews/2026-11-18-check-of-small-record-fixes.md, finding 1)". That is the right file and
the right finding. The built page (`site/dist/list/interview-before-retirement/index.html`) now
says "Those changes were checked on November 18th, 2026.", which is the sentence the check said
it should show. The exported data file follows.

### Finding 8. The changelog count. Passes

The line now says "Dated notes are added under two entries in the research draft, and completed
under two more", the check's own suggested wording, with "(corrected 2026-11-18: this line first
said "three dated notes are added")". The correction is dated and the old words stay visible, as
guideline 7 asks. A new dated line records these three fixes, says who made the second check is
left for John with open question 7, and says no number moved (6 of 9), which the scripts confirm.

### Finding 9. The scripts. Passes, with a note on the export

Run on 2026-11-18, after both commits:

- `python3 scripts/export.py`: "Wrote .../site/src/data/window.json (13 entries) and
  .../site/public/data/headline.json."
- `python3 scripts/compute.py --check`: "13 records read: 9 on the list, 4 beside it, 0 left out
  with facts still to verify. 6 of 9 things on the list are offered to at least one AI model
  today. The headline file matches the records."
- `python3 scripts/test_compute.py`: 21 tests, OK.
- `npm --prefix site run build`: "18 page(s) built", "Complete!", and its own post-build step:
  "The built site passes: 18 pages, 47 outside addresses linked."
- `python3 scripts/check_site.py`: "The built site passes: 18 pages, 47 outside addresses linked."

**`git status` was not clean straight after the export.** The export rewrote one line of
`site/src/data/window.json`, its `"commit"` stamp, from `913776f` to `3f5a332`, because it stamps
whichever commit is current. No record content changed. I put the file back with `git checkout
-- site/src/data/window.json`, and `git status` then showed no changes. This is the same thing
the check of the small record fixes saw, and it is not a fault of either commit: the committed
file can never carry the stamp of the commit that contains it, so every re-run of the export
leaves the working copy one line different. If that keeps tripping checks, the stamp could be
left out of the tracked file or written at build time; that is a choice for whoever next works on
the export, not a fix asked for here.

---

## Plain language, ids, dates and open questions. Passes, with one small note

- **Dates** are year-month-day in every file and in both commit messages. Neither commit message
  has a month name, a slash or a relative date (checked by search).
- **Ids.** File names carry what they are ("the fifth check", "the approval ruling"). The status
  lines of `method.md` and `what-john-needs-to-do.md` say "as it stood at commit c016bfb" with no
  plain phrase saying which commit that is; the approval ruling does the same. Small: "at the
  commit applying the fourth check's record fixes (`c016bfb`)" would meet the workspace rule.
- **Plain language.** The new sentences keep their connecting words ("because", "if ... the ...
  row governs", "otherwise"), and a stranger could say each one back. "The two things that come
  first" in script rule 11 leans on the paragraph above it, which says what they are.
- **Conditional language.** Nothing in either diff says a model wants, feels or finds anything.
- **Open questions.** Neither commit touches `docs/open-questions.md` or any ruling file. The
  promise stays open and is said to. Who made the second check is left for John with open
  question 7, and no wording in the diff says who made it. No guideline is edited.

## What was not checked

- The rest of `method.md` and `questions.md` outside the changed lines.
- Anthropic's streaming page; finding 1's point about a stop reason that declines to continue is
  from memory and should go into `docs/verify-list.md` if the method comes to rely on it.
- The rendered site in a browser. The built HTML was read for the retirement-interview page only.
