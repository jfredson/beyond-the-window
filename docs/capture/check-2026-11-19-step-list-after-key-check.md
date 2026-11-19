# Check of the step list after the check of the key-saving change

Written on 2026-11-19 by Claude (Fable 5.2), an AI model, in a session that wrote none of the
work checked. It checks one commit, 13cbc35 ("Capture step list: the merge order corrected,
the step that brings the Mac's copy up to date, and the commands that save the key"), which
changes the step list (`what-john-needs-to-do.md`) and one sentence of the method
(`method.md`). The commit answers the two should-fix findings of my last check
(`check-2026-11-19-rulings-in-documents.md`) and the two must-fix findings of the check of the
key-saving change (`check-2026-11-19-key-saving-change.md`).

This session fixed nothing. No model was asked anything, no outside service was called, no
key was handled and nothing was spent. In the TimeAssembler repository I read one file from
one branch with `git show` and changed nothing.

## Verdict

**The commit is right, and nothing must be fixed.** The merge order is corrected everywhere,
the new step is John's and gives no untried command, and the saving and checking commands
match the changed script word for word. The three capture documents are settled enough for
John's go to name a commit.

Counts: 0 must fix, 1 should fix, 4 notes. The should-fix is one sentence in the saving step,
and it rests on my memory of Anthropic's Console, not on a page I opened.

## The six things asked

### 1. The merge order

Passes. Every place that tells John what to do now says the newer pull request (number 142)
first, into the older one's branch, then the older one (number 141) into `main`, and gives the
reason: the newer one is open against the older one's branch, and the TimeAssembler repository
keeps a branch after its pull request is merged, so the other order leaves the change on a
leftover branch.

| Place in the step list | Line |
|---|---|
| The list near the top, point 1 | 24 to 32 |
| The earlier status under it | 97 |
| Step 4, "The order of the two merges, corrected 2026-11-19" | 342 to 349 |
| Step 6, "Saving the Anthropic key, in order", point 1 | 436 to 437 |
| "Before the day", point 1 | 659 to 661 |

The old order survives in two places only, lines 52 and 875. Both are quotations of earlier
wording, and the first is headed "kept as a record and not to be followed".

### 2. The step that brings the Mac's folder up to date

Passes on all three counts.

- **It is John's.** "Each of the four things below is yours to do", and the reason is given:
  other sessions share that folder.
- **No session is told to switch that folder's branch.** The step says the opposite, twice.
- **No untried git command is given.** The step gives none at all, and says why: the commands
  depend on how John merges, and none was tried. It tells him to ask a session what to type
  at that moment, "without typing it". I searched the three documents for any git or GitHub
  command and found none.

What the step says of the folder is true as I found it: it is on the older pull request's
branch, and its script is the old one.

### 3. The commands in step 6, against the changed script

Passes. I read the script as it stands on the branch `claude/rotate-key-btw-capture-0adc86`
(its newest commit is f5528f1, the same one the key-saving check read) and compared each
statement with the code.

| The step list says | The script |
|---|---|
| The proof command, `rotate-key.sh --check beyond-the-window-capture`, answers `beyond-the-window-capture no file at` and the path, and makes no call while no key is saved | `check_one` prints exactly that when the file is missing and returns before the call |
| The old script answers `Stopped: unknown key name "beyond-the-window-capture"` | The same words, followed by the list of names it knows |
| The save command, `rotate-key.sh beyond-the-window-capture`, prints `Paste the new "beyond-the-window-capture" key and press Return (nothing will show):` | Word for word |
| It checks the text looks like an Anthropic key, makes the one call, and only then writes the file | That order: the form, the call, then the write |
| After a good key: `"beyond-the-window-capture": new key saved, ends`, the last four characters, `and it works.`, the file's path, then a line asking John to tell a session the ending | Word for word, in that order |
| If either check fails it stops and nothing is changed | Each refusal ends "Nothing changed." and comes before the write |
| The check afterwards answers `beyond-the-window-capture ends`, the last four characters, and `works`, and makes the call again | Word for word |
| Without a name the check tests all six keys | The loop over all six names |

**The key is always named `beyond-the-window-capture`.** Both commands carry it, and the step
says three times that `btw-capture` is the Console's name and not the one to type.

**The key test is described truthfully:** one free call to Anthropic's token counter, sending
"hi" and naming `claude-haiku-4-5`, with the answer a number and no reply written by a model.
That is what the script's one call does, and it is the call John's ruling names ("Yes, keep
the test").

### 4. Nothing says merged, saved, off or given

Passes. I searched the three documents for each claim. Every mention says the opposite, or is
a condition that "must be true before the day". The commit's own note at the foot says none of
the four is true. What I could see agrees: the older branch is not in the local copy's `main`
as last fetched, the key file does not exist, and there is no spending record. Whether
automatic top-up is off I cannot see, and no document says it is.

### 5. The message files and the start checks

Passes. The commit touches the step list and the method and nothing else. The ten message
files match the ten checksums in `SHA256SUMS`, and the project's rebuild check gives the same
ten from `questions.md`. The command that shows a run sends nothing and reads no key, and I
ran it with the key's setting unset. Seven of its nine checks say pass, among them the last
safe day against the step list and the prices against the cost document. Two say FAIL, as
they should: no spending record, and the key's setting not set.

### 6. Are the three documents settled enough for John's go to name a commit

**Yes.** Nothing in the method, the cost document or the step list waits on a correction that
the run depends on. The script requires these documents to be committed, not to be the same as
the commit the go names, so a later dated correction does not undo a go. What is still open,
and why none of it holds the go:

| Still open | Whose | Does it hold the go |
|---|---|---|
| The should-fix below, one sentence on copying the key | The documents session | No. It bears on saving the key, which comes before the go |
| Whether a session may run the key check for this project's key | John's to rule | No, the step list says so. Until he rules, the check is his |
| The exact commands that bring the Mac's folder up to date | Left out on purpose; asked for at the moment | No |
| The script's own notes (`capture/README.md`) still carry the old sums and one sentence the ruling answered | The script session | No, but see note 1 |
| A follow-up for the capture script: refuse a key that holds a line break | The script session | No. The key-saving script cannot write such a file |

## Should fix

1. **"Copy the key in the Console first" may not be possible** (the step list, line 461). As
   far as I remember, Anthropic's Console shows a key's value once, when the key is made, and
   never again. I did not open Anthropic's page to confirm it. John made the key before the
   saving step existed. If he did not keep the value somewhere at that moment, there is
   nothing to copy, and the step gives him no way on. Suggested: one sentence saying that if
   the value is no longer to be had, he makes a new key in the same workspace, copies it at
   once, and removes the first one. Nothing else in the list changes, because no document
   depends on which key it is.

## Notes

1. **A change to the script's notes moves the commit a go would name.** `capture/README.md` is
   inside the folder the script requires to be committed. If the script session corrects its
   sums after John's go is recorded, the run still starts, because the script asks only that
   the files be committed. It is tidier for that correction to land before the go, so that
   the commit his words name holds the notes as they will stand on the day.
2. **Thirteen added lines of prose run past the file's width of 100 characters.** No long
   dash, month name or relative date was added.
3. **The method's one added sentence** (line 33) answers note 4 of my last check, and is
   true: for the Anthropic run the terms and the ceiling are ruled.
4. **What I did not do.** I did not open GitHub, the Claude Console or any Anthropic page,
   and did not run either key-saving command. The key-saving check ran both on made-up
   values, and I compared the step list with the code and with that check's account.
