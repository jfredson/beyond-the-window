# Check of the capture documents after five rulings of 2026-11-19

Written on 2026-11-19 by Claude (Fable 5.2), an AI model, in a session that wrote none of the
work checked. It checks two commits together, 91669af ("Capture documents: three rulings of
2026-11-19, two checks, and the run's list of what is done and what is left") and e786dba
("Capture step list: the key-loading command is ruled, the key is made, and what is left
before the Anthropic run, in order"). They change the step list
(`what-john-needs-to-do.md`), the cost document (`cost-and-terms.md`) and the method
(`method.md`). This session fixed nothing. No model was asked anything, no outside service
was called, no key was handled and nothing was spent.

## Verdict

**The two commits are right, and nothing must be fixed.** My three earlier findings are
answered, with sums that hold. Each of the five rulings appears with John's exact words and
"decided by: mixed", and none is stretched. The method's correction describes the script
truthfully and changes nothing that is sent. Nothing says the key-saving change is merged, the
key is saved or the go is given.

Counts: 0 must fix, 2 should fix, 7 notes. The first should-fix is about the order of John's
two merges, and is worth settling before he makes them.

## The seven things asked

### 1. My three should-fix findings, and the sums

All three are answered.

- **Reply size.** The two points under "While it runs" now say "if the replies are about the
  size expected", and step 7 has a sentence saying longer replies leave less room.
- **The row "All four".** $40 is struck through and $45 shown, "one figure ruled ($10 for
  Anthropic), three proposed".
- **"Naming that figure is done".** Struck through in both places, with "choosing that figure
  is done, and your go must still say it".

**The sums are right, and better than mine.** The step list now uses the sums from the check
of the plan change (`check-2026-11-18-ceiling-change.md`), which found something my check
missed: a question whose connection broke is asked once more in the same round, so all ten
questions add an ordinary reply to the first round, not seven or six. I read the script's rule
(`check_projection` in `capture/capture.py`), and it does add up every attempt of the first
round. My figure of about 5,000 tokens of room came from the smaller count and was too
generous. Worked again by this session:

| Broken connections in the first round | The step list | This session |
|---|---|---|
| Two | $1.27, times five $6.36 | 2 x 0.4824 + 10 x 0.0306 = 1.2708; $6.35 |
| Three | $1.75, times five $8.77 | 1.7532; $8.77 |
| Four | $2.24, times five $11.18 | 2.2356; $11.18 |
| Room left after three | $1.23 | 10 - 8.77 = $1.23 |
| Reply size at which three stop the run | about 3,600 tokens | (0.0306 + 1.234 / 50 - 0.0006) / 0.000015 = about 3,650 |

The one-cent difference in the first row is rounding. The conclusion is the documents': at $10,
with replies of about the expected size, the run goes on after three and stops at four.

### 2. The five rulings, and John's statement

Each appears with his exact words, "decided by: mixed" and the ruling file named. I compared
every quotation of his words and of the questions put to him with the ruling files.

| Ruling | His words | Where | Kept visible as not covered |
|---|---|---|---|
| The script's three additions | "Accept all three" | Method, three places; step list, top and status | That the script is not changed, and that a word count is not a reading |
| The Anthropic run within terms | "Yes, within terms" | Step list, step 3; cost document, Part 3 | Publishing; Google's and OpenAI's terms; the two documents nobody opened |
| The key-saving script | "Yes, Anthropic only" | Step list, step 4 | The merges; the OpenAI and Google keys; the key itself |
| The command that loads the key | "Approve it" | Step list, the run's step 2 | The matching commands for Google and OpenAI; who types it |
| The key test | "Yes, keep the test" | Step list, steps 4 and 6 | Any other call; that it is not the go to spend; tests of Google or OpenAI keys; who runs it |

"Done, no expiry" is given as John's word and not as a ruling, with what is not confirmed
written beside it: the key's name, the key saved on the Mac, and automatic top-up off. The
planning session's condition on the command is marked "decided by: agent", and is said to be
that session's and not John's. Two sentences go beyond the rulings, and each says it is the
writing session's reading (who may run the key check, step 6; a figure other than $10, step
7). The go to spend is said to be still John's in every place a ruling is entered.

### 3. The method

The dated correction is truthful against the script and its notes.

| What the method now says | Checked against |
|---|---|
| Three more outcomes, each counted at the most its call could cost, and what is done for each | The three names in `capture.py` and the README's "What is written in the reply folder", which say the same |
| A folder `sent-markers`, one small file for each call, written before it is sent, holding the attempt's numbers, the length limit and the most the call could cost | `write_marker` in `capture.py`. A marker also holds the developer, the model's name and the time sent, and nothing from a reply |
| An empty file, `one-run-at-a-time.lock` | The name in `capture.py` |
| The `labels` command shows the word count of every reply and no words | `label_lines` in `capture.py`, and see note 3 |
| "Seven outcomes in the table above" | The table has eight rows and seven different entries under "Recorded as", and the sentence gives the count as the script's notes' |

Nothing that is sent changes. The commits touch three documents and nothing in `capture/`,
`docs/capture/sent/` or `questions.md`. The ten message files match the ten checksums in
`SHA256SUMS`. The method does not feed the rebuild, `questions.md` does, and the project's own
check (`sent_files.py`, run with no arguments, which writes nothing) rebuilds all ten from it
and reports that they and the checksums match. The failures table and the script rules are
left as approved, with the additions marked and dated.

### 4. What is left before the Anthropic run

The list is true, as far as I could see without calling any service.

| What the list says | What I saw |
|---|---|
| The key-saving change exists and is being checked | The branch is in the local copy of the TimeAssembler repository, two commits on top of the older branch. `check-2026-11-19-key-saving-change.md` is not written yet |
| Neither pull request is merged | The local copy's `main`, as last fetched, holds neither branch. I did not open GitHub |
| The key is not saved | The key file does not exist. I looked only for whether it exists |
| The go is not given | `docs/spending-record.md` does not exist |
| The run by 2026-11-26 | John's ruling of 2026-11-18; the script's last safe day is 2026-11-28 |

The changed script on that branch knows the key as `beyond-the-window-capture`, writes the
line as the name, an equals sign and the key with no quotation marks, and tests a key with the
one call the ruling names. That agrees with what the step list reports and with what the
command in step 2 expects. It is a glance, and the other session's check is the one that
counts.

The order works: the check, the merges, saving the key and top-up, the go, the run. Two things
about it are under "Should fix" 1 and note 1.

### 5. Does anything say the change is merged, the key saved or the go given

No. I searched the three documents for each claim. Every mention says the opposite: "Neither
is merged", "not yet saved on this Mac", "the go in step 7 is still yours to give". One
sentence is now wrong in the other direction, should-fix 2.

### 6. The script's start checks

They still pass against these documents. The command that shows a run
(`python3 -I capture/capture.py show --run anthropic-2026-11-30`) sends nothing and reads no
key, and I ran it with the key's setting unset. It printed nine checks:

- **Seven say pass:** everything is as committed; the ten message files match their
  checksums; the last safe day equals the step list's; the prices equal the cost document's;
  the rehearsal passed for this script and plan; the reply folder is outside every repository;
  the date is not after the last safe day.
- **Two say FAIL, as they should:** there is no spending record, so no go to check the ceiling
  against; and the key's setting is not set.

It gave the ceiling as $10 and the estimate as $1.89 with one fifth added.

### 7. Plain language

No long dash, no month name, no slash date and no relative date in the added lines. The one
commit id carried over (a57a212) has its plain phrase. Struck-out wording is kept throughout,
and the lists that were written out again have their earlier words quoted under "Earlier
wording of the run's step list". The two pull requests are linked by name each time. About a
dozen added lines of prose run past the file's width of 100 characters, the longest to 199.

## Should fix

1. **The order of the two merges can leave the change out of `main`** (the step list, lines 24
   to 27, and "Before the day", point 2, at line 539). The list says to merge the older pull request first
   and then the new one, "which is open against the older one's branch". A pull request merges
   into the branch it is open against. If the older branch is still there when John merges the
   new one, the change lands in that older branch and not in `main`, and the script he then
   runs from `main` cannot save this key. Whether GitHub removes the older branch and points
   the new pull request at `main` by itself depends on a setting of the repository that I did
   not look at. Suggested: one sentence telling John to look at the new pull request before
   merging it and see that it says it merges into `main`, or to merge the new one first and
   the older one second, which carries both. The session checking the pull request is the
   right one to say which.

2. **"'still not made' still holds" is no longer true** (the step list, line 278). The same
   point says two lines earlier that the change is made. Nearby, two sentences written before
   the pull request existed are left standing without a mark: "A session in the TimeAssembler
   repository is making it on its own branch and will open a pull request" (lines 67 and 275)
   and "the new one when it exists" (line 72). Each is corrected by the sentence after it, so a
   careful reader arrives at the truth, but line 278 says the opposite of it. Suggested: strike
   the three through.

## Notes

1. **The step that writes the saving commands is not in the list of what is left.** Step 6 says
   the exact commands for saving the key are added to the step list as a dated correction once
   the check of the key-saving change lands. That is a change to a document the script requires
   to be committed, and John's go names a commit. So it belongs between points 1 and 3 of the
   list, before the go is recorded. The list is still workable without it.
2. **The script's own notes are now behind the documents in two places** (`capture/README.md`,
   not touched by these commits, rightly). Its sums still read $8.10, $10.35 and $5.80, and it
   still says of the three additions that "John should know of them". The check of the plan
   change already asked for the sums. Both are the script session's.
3. **The `labels` command shows more than the method's sentence names.** Beside the word count
   and what each file was recorded as, it shows the service's status number, the stop reason,
   the model's name as reported, the counts of tokens sent and replied, and the cost counted.
   None is a word of a reply, and the run prints the same things on screen for every call. The
   count of tokens replied is a second measure of a reply's length, so what John was told
   about a word count applies to it too.
4. **One earlier sentence in the method is out of date and not marked** (line 32): "Still
   John's before any run: the terms, the keys, the spending ceilings and the capture script."
   For the Anthropic run the terms and the ceiling are now ruled. The status paragraphs above
   and below it give the present state.
5. **The cost document adds a sentence the ruling does not hold:** "This document is not legal
   advice and the ruling does not make it so." It claims nothing for John and narrows nothing
   he ruled.
6. **An unusual case the sums leave out.** They take a broken connection as one call counted
   at the most it could cost. A connection that breaks before any reply text arrives is a
   failed attempt, which is tried again up to three more times. I did not work out what each
   of those tries is counted at.
7. **What I did not do.** I did not open GitHub, the Claude Console or any terms page, and
   did not read the key file's contents, which do not exist. What is said above about the two
   pull requests comes from the local copy of the TimeAssembler repository as it was last
   fetched.
