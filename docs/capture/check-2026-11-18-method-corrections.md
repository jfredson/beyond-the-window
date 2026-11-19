# The sealed capture: a check of the corrections made after John's second approval

Written 2026-11-18 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This is a check by a session that did not make the edit. I did not write the
ruling, the questions, the method, the capture script or any earlier check. I read the commit
that applied John's second approval ("Apply John's second approval of the capture and the
check's five findings, as dated corrections", `98c9dc6`) against two things: John's ruling of
2026-11-18 that approved the ten rebuilt message files with two rules
(`docs/rulings/2026-11-18-capture-approval-second.md`, decided by: mixed), and the five
should-fix findings of the check before this one (`check-2026-11-18-note-edit.md`). I worked
from the files and the differences between them, not from the commit's own account. I changed
no file but this one. No model or outside service was called, no key was handled, nothing was
spent or published, and no reply file was opened or made.

Like `questions.md`, this file refers to the capture's documents closely, so it is held back
with them if this repository is ever made public.

## Verdict

**The commit does what the ruling asked. Nothing must be fixed.**

No message file changed. The ten checksums are the ten John approved. Both of his rules are in
the method in his words, with the condition and the reason the ruling gives. The three other
findings were applied as the earlier check suggested. Every place that said the new checksums
waited for John now says they are approved, with the date, his words and the ruling file. The
changes are dated corrections that keep the earlier words.

Three things should be fixed. All three are sentences the commit did not write and left
standing, which now sit badly beside the two new rules or the second approval. None changes a
message file. A fourth section lists the sentences that are out of date because a capture
script now exists.

## How I checked

- **The bytes.** `shasum -a 256` on each of `docs/capture/sent/q01.txt` to `q10.txt`, compared
  by program with the ten lines in the ruling and with `sent/SHA256SUMS`: the same, character
  for character. `shasum -a 256 -c SHA256SUMS` inside the folder: all ten OK.

  ```text
  c7b25e0aa6126d05a448a57261fd68b3c7f6ea457e5dd8399c7c683f9918e5c9  q01.txt
  41891a4b97830dc15fb170941ad42e1e17b8235a065fe4fcd254e598c5abdea8  q02.txt
  c46b7c2cbdb732f61dd8c094cc510cdcdbc53e49cabbb652fc1c06e0182052a8  q03.txt
  8c649f5a94fa6b1e55dbe90b21ab54960515a555c0e2db8b1c937522c7f10b14  q04.txt
  ed8c21277479563c3010272aadf48f85df70f8308cb38e326985d50f649839c2  q05.txt
  663dbf5d78ef660dadfa71ce5dfac999c87e992ea0db7b91f4e77d5e1f768a1a  q06.txt
  40138d1979c87d3e60a72bbea28663de0667cd53d1333dfcdcda774e5e465d70  q07.txt
  2d6c78312795ba7f93caecde0d6b9ecc8d21827195f2181338a8cd35a6997092  q08.txt
  e74f970a2fd25a4edd9ce04aab010103503a112edd405dedcf64f0eb0286b210  q09.txt
  c9c56be9d9f8865ecca803da42cebf8d5dd30e71261526b9ed9a578239496552  q10.txt
  ```

- **What the commit touches.** `git show --name-status 98c9dc6`: four files, all changed and
  none added or removed: `method.md`, `questions.md`, `what-john-needs-to-do.md` and
  `sent/README.md`. In `sent/` only the README. The capture documents have not changed since
  that commit.
- **The project's scripts**, each run with `python3 -I -B`: `sent_files.py` in its check mode
  ("Check passed: all 10 committed messages and SHA256SUMS match questions.md"), and the
  self-tests of `sent_files.py`, `shared_wording.py` and `shared_subject.py`, all passed.
  `redo_cost.py` ran and exited cleanly.
- **The wording check.** I ran `shared_wording.py` on `questions.md` against the 13 saved
  developer pages. The opening note is 127 words and shares three runs: "on behalf of a
  person", "and it may be", "on behalf of a". That is what the earlier check listed and what
  the commit records.
- **The documents.** The whole difference of the commit, read line by line against the ruling
  and the earlier check; then the four documents and `cost-and-terms.md` as they now stand,
  searched for every sentence on publishing, describing, summarising, discussing, selecting,
  waiting for approval, and the script.
- **John's words.** "Approve, with both" appears 13 times in the lines the commit added, the
  same each time, and matches the ruling. The longer quotation of his question in
  `what-john-needs-to-do.md` was compared word by word with the ruling on publishing
  (`docs/rulings/2026-11-18-capture-answers-may-be-published.md`).
- **The whole repository** for the first approval's checksums and for wording that still waits
  for approval.

## What passes

**1. Nothing sent changed.** See above. The first approval's ten checksums appear in one file
only, the first approval itself (`docs/rulings/2026-11-18-capture-approval.md`), which is
rightly left as it was.

**2. The two rules.**

- *"Summarised".* `method.md`, line 209: "never scored, sorted, counted or summarised", as the
  ruling has it. Line 213: it "stays until a comparison method ruled by John says how the
  answers may be described". That is the ruling's condition, no wider and no narrower. "Graded",
  which the earlier edit had put in the word's place, is out of that clause so that it reads as
  John ruled it; the correction says so and gives its reason (lines 250 to 252). The promise
  that the answers are never graded is still stated in `questions.md`, line 111.
- *All or none.* `method.md`, lines 229 to 234, and `questions.md`, lines 117 to 124, under
  "What it commits John to". Both give the rule in the ruling's words: "if the answers are
  published, all of them are, for every model and every asking, and none is chosen by what it
  says". Both give the reason (the note tells the model "nothing will be decided from it", and
  choosing by what the answers say would be a decision made from them) and the cost John was
  told (a selection can never be published). `what-john-needs-to-do.md`, lines 50 to 57, states
  both rules to John.
- *Contradictions.* Two older sentences now pull against the rules: should-fix findings 1
  and 2.

**3. The three other findings of the earlier check.**

- *Finding 3, the cut quotation.* Applied the first way the check suggested: the quotation now
  runs to the end of John's sentence (`what-john-needs-to-do.md`, lines 37 to 41), word for
  word as the ruling has it, with a sentence saying where it used to stop.
- *Finding 4, the deleted sentence.* Applied as suggested, in the suggested words
  (`questions.md`, line 26). I checked the quoted sentence against the file before the earlier
  edit: it is word for word.
- *Finding 5, the shared four-word run.* Applied as suggested, in the suggested words
  (`questions.md`, lines 82 to 85), with one sentence added saying the session ran the wording
  script again and got the same three runs. My own run agrees.

**4. The approval.** Each place that waited now says approved, with "Approve, with both", the
date and the ruling file:

| Where it waited | What it says now |
|---|---|
| `method.md`, lines 22 to 23 (status) | Answered by the new paragraph, lines 25 to 32 |
| `method.md`, lines 354 to 355 ("Before anything is asked") | Old words struck through, new words beside them |
| `method.md`, line 415 (a row in an earlier table of changes) | Left as written; answered at line 438 |
| `questions.md`, lines 3 to 7 (status) | Says the first approval's ten no longer name what is sent |
| `questions.md`, lines 22 to 23 | Answered by the new paragraph, lines 28 to 34 |
| `questions.md`, lines 466 and 475 (an earlier table of changes) | Left as written; answered at line 491 |
| `what-john-needs-to-do.md`, lines 8 to 11 (status), 25 to 27, 50 to 63 | Old words struck through, new words beside them |
| `what-john-needs-to-do.md`, lines 216 to 217 | Left as written; answered at lines 221 to 228 |
| `sent/README.md`, lines 3 to 5 and 30 to 43 | Old status line quoted, old paragraph struck through in the two places that were no longer true |

No sentence presents the first approval's ten checksums as what is sent. One sentence could be
misread that way: should-fix finding 3.

**5. Form.** Every change is a dated correction. Nothing was deleted without being kept: the
clause with "graded" is quoted at `method.md`, lines 215 to 216; the old status line of
`sent/README.md` is quoted at its line 5; everything else is struck through or left and
answered. No file under `docs/rulings/`, no earlier check and no open question was touched. The
added lines contain no long dash.

Two things were changed that neither the ruling nor the five findings named. Both are small
and I think both are right:

- The earlier check's note 3 was applied (`method.md`, lines 254 to 256): the words "in the
  ruling's own words" are corrected beside themselves, since the words follow the ruling and
  are not word for word.
- The status line of `sent/README.md` was brought up to date, which the earlier check's
  note 10 said the approval would call for.

## Must fix

None.

## Should fix (none changes a message file)

### 1. One sentence still speaks of publishing "parts" of the record

`docs/capture/cost-and-terms.md`, lines 186 to 188. The commit did not touch this file.

The sentence, added on 2026-11-18 after the ruling on publishing, reads: "The question is now
whether a record kept for a public research project, parts of which may be published, is a
professional purpose." Under John's second approval the answers are published all together or
not at all. "Parts of which may be published" can be read as "some of the answers may be
published", which is the one thing the new rule forbids. It may have meant that the answers are
one part of the record, the other part being what each service sent back around them. A reader
cannot tell.

*Suggested change.* Leave the sentence and add after it: "Added 2026-11-18, after John's second
approval (`docs/rulings/2026-11-18-capture-approval-second.md`): 'parts of which' does not mean
some of the answers. If the answers are published, all of them are, for every model and every
asking, and none is chosen by what it says." Add one row to that file's table of changes.

### 2. "Published and discussed" sits beside "never summarised" with nothing joining them

`docs/capture/method.md`, lines 219 to 228.

Line 219 says in bold: "They may be published and discussed." Six lines above, the answers are
never summarised until a comparison method John rules says how they may be described. A
discussion of the answers that does not describe them is hard to picture. The first point in
the list (lines 224 to 225) says nothing can be quoted or described before a comparison method
exists, but it gives the reading rule as the reason, so a reader could conclude that once
anyone may read the answers they may be discussed freely. That is the reading the first rule of
the second approval was made to close.

Both phrases are John's, from two rulings, so neither can be reworded. They can be joined.

*Suggested change.* One sentence after line 221, marked as the session's reading and not as a
ruling: "Discussing the answers does not include summarising or describing them until the
comparison method says how they may be described (the paragraph above). Until then, what may be
published is the answers themselves, whole." If the planning session thinks that says more than
John ruled, put the one question to him.

### 3. "The new checksums were approved" now reads as if it meant the ten that are sent

`docs/capture/what-john-needs-to-do.md`, lines 30 to 31. Not changed by the commit.

The second point of step 1 ends: "The new checksums were approved on 2026-11-18, after the
fifth check." Those were the checksums of the first approval, made new by the eight wording
changes. Since the rebuild there is a newer ten. The first point (lines 25 to 27) and the fifth
point say so, but this sentence, read alone, points a reader at the first approval as if it
covered the present files.

*Suggested change.* Add after it: "(Those were the ten of the first approval. They no longer
name what is sent; see the first and fifth points of this step.)"

## Out of date because a capture script now exists

A capture script was written after the commit I checked (`capture/capture.py`, `plan.toml`,
`rehearsal.py` and `README.md` in commit `8aa9f13`, "the capture script, its plan and its
rehearsal"; its rehearsal result in commit `0e4442c`). The ruling itself says the script "is
being written and has not been checked or approved"; that is a record of its time and is not
to be edited. These sentences in the capture documents are now untrue or half true. I
corrected none of them. The session that wrote the script left suggested wording for most of
them in its hand-over note (`capture-script-handover-2026-11-18.md`, in the shared notes
folder outside the repository), and the list below marks which.

| File and line | What it says | What is now the case |
|---|---|---|
| `method.md`, lines 14 to 15 | "Nothing here has been run. No script exists; the last sections say what one must do." | A script exists and its rehearsal passed. It has not been checked by a different session or approved, and nothing has been run against any service. In the hand-over note |
| `method.md`, line 178 | Whether a second asking after a broken stream is at the model's maximum length "is for whoever writes the script to propose" | Proposed with the script, not approved: the same length limit, not the maximum (`capture/README.md`, "PROPOSED 2026-11-18, for John", point 2). In the hand-over note |
| `method.md`, lines 272 to 275 | "**Not built yet:** no capture script exists ... This check is part of the capture script still to be written ... The threshold for 'very short' is to be proposed with that script and approved with it." | Built. The threshold is proposed as fewer than 20 words (`capture/plan.toml`; `capture/README.md`, point 1) and is not approved. In the hand-over note |
| `method.md`, line 299 | "For the session that writes it once John approves." | It has been written. Not in the hand-over note |
| `method.md`, lines 355 to 356 | "The script is committed in a separate commit and its rehearsal passes." | Written as a condition, and not false. A reader cannot tell it is now met. It could name the two commits, and say that the check by a different session and John's approval are still to come. Not in the hand-over note |
| `method.md`, lines 31 to 32 | "Still John's before any run: the terms, the keys, the spending ceilings and the capture script." | Still true. It could now say what about the script is his: the two proposals above, and approval after a different session's check |
| `what-john-needs-to-do.md`, lines 176 to 178 | Approval is needed by about 2026-11-24 "to leave time for a session to write the script, run its rehearsal on constructed replies, and have that checked" | The first two are done; the check remains. In the hand-over note |
| `what-john-needs-to-do.md`, lines 145 to 147 | The form of John's go: "as written in `docs/capture/` at commit ______" | The script lives in `capture/`, outside `docs/capture/`, so the form names no commit of the script and does not mention its two proposals. The hand-over note covers the proposals |

Two rows in `method.md`'s tables of changes (lines 390 and 393) say "recorded as not built
yet" and "left for whoever writes the script to propose". They are records of what was changed
on their day and should stay as they are. `questions.md`, `sent/README.md` and
`cost-and-terms.md` have no sentence saying that no script exists. Outside the capture folder,
`docs/handoff-2026-11-18.md`, line 43, says "No capture script exists yet"; it is a record of
its time.

The hand-over note also lists changes the method needs that are not about whether a script
exists (how the key reaches the script, one ceiling for each run and not each developer, what a
file name carries). Some of those change an approved method and need John's ruling. They are
outside this check.

## Notes

1. **Two bold sentences are answered and not struck through.** `method.md`, lines 22 to 23,
   and `questions.md`, lines 22 to 23, still say in bold "Nothing is sent until John approves
   the new checksums, by 2026-11-27." The paragraph after each says the sentence is answered.
   In `sent/README.md` and `what-john-needs-to-do.md` the same words were struck through. Both
   forms keep the old words readable. Striking these two through would match the other two
   files and help someone who reads only the bold.
2. **A consequence of the all-or-none rule that John may not have in mind.** The method lists
   the check of each developer's terms as something that comes before publishing (`method.md`,
   lines 226 to 227), and the rule says all the answers, for every model. Together they mean
   that if one developer's terms forbid publishing its model's answers word for word, none of
   the answers can be published, the other developers' included. Nothing needs changing. It is
   worth one line to John before publishing is ever decided.
3. **What counts as an answer is not said.** The rule covers "every model and every asking".
   The record will also hold failed attempts, replies cut off, replies from a wrong model and
   replies blocked by a service (`method.md`, the failures table). Whether those are published
   with the rest is not ruled. Leaving out a cut-off reply is a choice made by what the service
   reported and not by what the reply says, so it does not break the rule's words; it should
   still be settled before anything is published, not after.
4. **Step 8 does not mention the rule.** `what-john-needs-to-do.md`, lines 152 to 157, says
   what comes before publishing and leaves out all-or-none. Step 1 of the same file states it
   (lines 55 to 56), so John is told. One clause in step 8 would put it where he will look
   when the time comes.
5. **The status line of the steps document is behind.** `what-john-needs-to-do.md`, line 3,
   says steps 1 and 2 were ruled "apart from one point"; that point was ruled later the same
   day, as the next sentences say. Step 1's heading (line 21) says "rule four things" and now
   has six points. Both were so before this commit.
6. **Two of the earlier check's notes were not applied, and did not have to be.** Note 1
   ("replaced" for words the ruling only set aside; `method.md`, line 49, and `questions.md`,
   line 40) and note 2 (nobody ruled that the name "sealed capture" is kept). The ruling asked
   for the should-fix findings only.
7. **The 13 saved developer pages are still only in a scratch folder**
   (`/private/tmp/claude-501/-Users-john-Code-beyond-the-window/1f480419-810a-48de-a23d-67c42ecf6958/scratchpad/corpus/`),
   which a restart of this Mac can empty. They were there when I ran the wording check. The
   earlier check said the place for them is `docs/private/`, and that is still undone.
8. **A record of its time.** `docs/handoff-2026-11-18-evening.md`, line 86, says the new
   checksums need approval by 2026-11-27. It is a hand-over file and is not to be edited; a
   session should not copy from it.
9. **Long lines.** The commit added more lines that run past 100 characters, because the
   ruling's file name is written into them. It affects only how the files look.

## What I did not do

I did not check the capture script, its plan or its rehearsal; another session is doing that.
I opened no developer's page. I read the script's README and the hand-over note only far enough
to say what the script proposes where the method says "to be proposed". I fixed nothing.
