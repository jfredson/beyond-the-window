# The sealed capture: a third check of the capture script

Written 2026-11-18 by Claude (Fable 5.2), an AI model, in the session that wrote the first two
checks (`check-2026-11-18-capture-script.md` and `check-2026-11-18-capture-script-second.md`).
This is a check by a session that did not write the script. The script's author answered the
second check in commit 3dda42d (the script, its plan, its rehearsal and its README) and commit
b0c5bf7 (the rehearsal's result, 299 checks). I read every line of the difference since the
second check, and the parts of the script that difference touches.

I changed nothing in `capture/` and nothing in any other session's file. No model and no
service's programming interface was called. I did not run `capture.py run`. No key was handled,
nothing was spent, and the real answers folder still does not exist. Every reply in my tests is
constructed; none came from any model. This file quotes no question and no word of the opening
note.

## Verdict

**The Anthropic run: yes. Nothing must be fixed, and nothing should be fixed first.**

The one fix I asked for before the first run is made and holds: a reply holding half of a
two-part symbol is now saved at the first try, exactly as the service gave it, and reads back.
The other six should-fix findings are each fixed. What is sent is unchanged, to the byte. The
rehearsal I ran matches the committed result line for line.

Four small things are noted below. None needs a change before the run.

**Google and OpenAI: still not ready,** for the reasons in the first check. Nothing in this
round changes that.

The step list John will follow has three places that are now out of date. They are set out
under "The step list" with the words that would be right. None would lead him to do anything
unsafe.

## How I checked

- Read the whole difference in `capture/capture.py` (72 lines), `plan.toml` (comments only),
  `rehearsal.py` and the README.
- Ran `python3 -I capture/rehearsal.py`: 299 checks, none failed, the same as
  `capture/rehearsal-result.txt` apart from the temporary folder's name. Its last line carries
  the checksums of the script and plan as committed. Every one of the second round's 274
  checks is still there; 25 are new.
- Ran `show` for the Anthropic run: the same address, the same three headers and the same body
  as before.
- Ran my own tests against the real script with constructed replies and the rehearsal's network
  tripwire on.
- Made 14 broken copies of the script in the scratchpad, aimed at this round's changes, and ran
  the rehearsal against each.
- Read the README and `what-john-needs-to-do.md` against the script and against John's ruling
  of four points (`docs/rulings/2026-11-18-capture-script-four-points.md`).

## The half of a two-part symbol

**Fixed.** `capture/capture.py`, `Engine.write_new_file`, `Engine.write` and `Engine.save`.

The file is now written as bytes. A lone half is written as the escape the service sent, which
is valid inside the file and reads back as the same half. Seven constructed replies of my own:

| The constructed reply held | Saved at the first try, under its ordinary name | Reads back the same | The saved stream rebuilds it |
|---|---|---|---|
| A lone first half | Yes | Yes | Yes |
| A lone second half | Yes | Yes | Yes |
| Nothing but a half | Yes | Yes | Yes |
| Nothing but two halves the wrong way round | Yes | Yes | Yes |
| A half after a backslash and a quotation mark | Yes | Yes | Yes |
| A whole symbol, a zero byte and unusual line ends | Yes | Yes | Yes |
| The six plain characters that spell out the escape | Yes | Yes | Yes |

In every case there was no wait, no warning and no empty file left behind; a restart read the
folder, made no further call and finished; and the fault list and the `labels` command both
read the file.

**Is anything altered or dropped?** No. One thing to know. When the two halves of one symbol
arrive in two separate pieces of the stream, the reply text reads back from the file as the one
whole symbol, which is what the service meant. Both halves are also in the file exactly as
sent, inside the saved stream.

**Can reading it back fail?** Not that I could make happen. The file is plain text throughout.

The second part of the fix also works. When I made the ordinary write fail for a reason other
than the folder or the disk, the script went straight to a plainer form of the same record,
with no wait, and saved it at the second try with the reply in it and no key.

## The other six should-fix findings

| Finding | Now |
|---|---|
| S2. Ctrl-C part way through a reply used one of the question's two askings | Fixed. A reply cut short by hand is kept and no longer counts as an asking. My test: cut short by hand twice, then two empty replies, and the question was left only after the two empty ones. It is still counted at $0.48, and the README now says so in place of "safe at any time" |
| S3. A count the service could not have reported was used | Fixed. A count below zero, above the length limit sent, or above what the message could hold is not used, and the call is counted at the most it could cost. At the edges: a count equal to the bound was used, one above it was not. See note 3 |
| S4. The network code handed back what arrived only for named kinds of error | Fixed. Any other kind after the service has begun to answer now hands back what arrived and names the kind. Before any answer, the error is raised as before, so the rehearsal's tripwire still trips |
| S5. Three gaps in the rehearsal | Fixed, all three. The real network code is now run against a constructed connection that opens nothing, and the figure for an unreadable file is written out |
| S6. Two loose ends in John's go | Fixed, both. "$5,000" and "$5k" no longer match words ending "up to $5". Where a developer has more than one run, the words must carry the run's withdrawal date |
| S7. Three gaps in the README's steps for the day | Two fixed: the top folder is named, and Ctrl-C is described as it is. The third, the command that sets the key's variable, is still left out of the README on purpose, because where the key's file is has not been settled. The step list has that command, as a proposal |

**The eight notes.** Note 6 is acted on: a reply folder that cannot be written to before the
first call now gives a plain refusal. Notes 2 to 5 (the `labels` command, the new things in the
answers folder, the three outcomes with no row in the method, and a reply the script could not
take apart) are written into the README for John and shown as things he should know, not as
ruled. Notes 1, 7 and 8 needed nothing.

## Everything else in the difference

- **What is sent:** not touched. The code that builds and checks a request has no changed line.
- **The cost counting:** one change, S3 above. It can only raise what is counted, never lower
  it.
- **Where a reply or the key can go:** no new place. The plainer form of a record still has
  the key taken out before it is written.
- **Guards and rehearsal cases:** none weakened or removed. The rehearsal's constructed
  messages were made longer, because the new bound on tokens sent would otherwise have
  rejected the stand-in's own counts. That is a change to the rehearsal's made-up data and not
  to any check.
- **`plan.toml`:** comments only. The two settings John ruled are now marked as ruled.
- **Not asked for by a finding:** nothing.

## The rehearsal

It cannot reach the network: the same tripwire. It matches the committed result.

Fourteen broken copies, one change each:

| Change | Caught? |
|---|---|
| A lone half is refused again | Yes |
| A lone half is silently dropped | Yes |
| A lone half is turned into a question mark | Yes |
| The network code no longer hands back what arrived after an unnamed kind of error | Yes |
| The network code swallows an error before any answer | Yes |
| A reply count above the limit sent is used | Yes |
| **A sent count above what the message could hold is used** | **No** |
| A reply cut short by hand counts as an asking again | Yes |
| OpenAI's go need not carry the date | Yes |
| A figure followed by "k" is accepted | Yes |
| No plainer form is tried | Yes |
| **The plainer form leaves the key in** | **No** |
| A hand stop is forgotten on a restart | Yes |
| An unwritable folder is not a plain refusal | Yes |

The second and third rows are the ones that answer "nothing altered or dropped": the rehearsal
would notice either.

## Notes

1. **Two gaps in the rehearsal,** the two rows in bold above. Neither is a fault in the script:
   in the real script the bound is applied and the key is taken out. Worth one case each when
   the script is next changed for another reason.
2. **If both forms of a record fail to write for a reason other than the folder or the disk,**
   the script still tries 65 times over half an hour and tells the reader to check the folder.
   I could only reach this by breaking Python's own writer on purpose.
3. **The new bound on tokens sent is one more thing a real call will test.** The script now
   refuses to use a count of tokens sent that is larger than the message's size in bytes plus
   64. For the first real message that bound is 838, and I would expect a count near 200, so
   there is wide room. If the service ever reported more than the bound, every call would be
   counted at $0.48 and the run would stop after eight askings. No money would be at risk.
4. **A go that says "$5 thousand" in words** would still match "up to $5". It errs low.

## The README against the ruling

The README's section "Ruled by John on 2026-11-18" gives the four points as the ruling gives
them: the exception for errors that trying again cannot cure, the first Anthropic run by
2026-11-26, the key through a setting in the shell, and the two settings (20 words; the same
length limit). His words "Approve all four" and "decided by: mixed" are quoted correctly. It
says plainly that the script does not enforce the 2026-11-26 date, only the last safe day,
which is true.

Nothing is shown as ruled that is not. The ceilings are marked as still proposed. The three
things the script adds beyond the method's words are marked as things John should know of. The
three remarks from my second check on the exception are marked as things the ruled words do not
spell out, which is what they are.

One small mismatch between two documents, not an error in either: the README's first step for
the day says the command that sets the variable cannot be given yet, while the step list gives
that command as a proposal.

## The step list, `what-john-needs-to-do.md`, as it stands after commit f4a3d57

Read against the script and README as they now stand. The commands in "The Anthropic run, step
by step" are right: the folder, the command that sets the variable, `show`, the one call with
`--stop-after 1`, `labels`, and the rest. The table of what each first line means matches what
the script prints. The four lines after one call are in the right order. The sums in step 7
about the ceiling are right. Setting the variable once is enough for all the commands, because
the script removes the key only from its own copy of the settings, not from the window.

Three places are out of date:

**1. Lines 363 to 370, the Ctrl-C line under "While it runs".** It says a reply cut short by
hand "uses one of that question's two askings", and that the change which ends this is "not yet
committed". That change is committed (3dda42d) and I have tested it. Words that would be right:

> Ctrl-C is safe between calls and during the minute's wait after a failed attempt. While a
> reply is arriving it loses nothing already received, and the cut-short reply does not use up
> either of that question's two askings, but that call is counted at $0.48 of the ceiling, and
> two calls counted that way in the first round can end the run for good at $5. Do not press it
> while a reply is arriving unless you must.

**2. Lines 37 to 40, the first of the things left for John at the top.** It asks him to decide
whether the half-symbol finding is fixed before the first run. It is fixed (3dda42d), rehearsed
(b0c5bf7) and checked here. Words that would be right:

> The second check's first should-fix finding (a reply holding half of a two-part symbol could
> not be saved) is fixed, with its other six, in commit 3dda42d. The rehearsal was run again
> (commit b0c5bf7, 299 checks) and a third check found the fix sound and nothing that must be
> fixed (`check-2026-11-18-capture-script-third.md`). Nothing here is left for you to decide.

The same goes for lines 252 to 254, which say the list "may still change once more, when the
script's author commits the changes that answer that check", and for the first point under
"Before the day" (lines 264 to 267). Both are answered by the same sentence.

**3. Lines 210 to 212, what the script needs of a go.** True as far as it goes. Since 3dda42d
the script also needs one more thing, which matters only for OpenAI. A sentence to add:

> For OpenAI, which has two runs, your words for each run must also carry that run's withdrawal
> date, as the form above does ("OpenAI's models due 2026-12-11, up to $15").

Nothing else in the list is wrong.

One thing the list does not say and should: **`what-john-needs-to-do.md` and
`cost-and-terms.md` are themselves among the files the script requires to be committed with no
changes since.** If either is edited and not committed, `show` reports a failed check and the
run refuses. So the corrections above must be committed before the day, and nobody should edit
those two files on the day.

## Which commit John's go should name

The script checks only that the commit named in the go exists in this repository. It does not
check which commit it is. So the choice is for the record, and it should be the one that says
truthfully what he approved.

**It should name the commit that is the latest in the repository at the moment he gives the
go,** after the step list's corrections above are committed. The form he is offered says "as
written in `docs/capture/` at commit ______", and the documents will have changed after the
script did, so the script's own commit would name an older state of the documents.

Before giving him that id, a session confirms two things. First, that the last commit to touch
`capture/` or `docs/capture/sent/` is still b0c5bf7, the rehearsal's result for the script as
checked here (the script's checksum begins 2c38f8af and the plan's b08f8dee, as on the last
line of `capture/rehearsal-result.txt`). Second, that `show` reports every check as passed
except the go and the key. If anything in `capture/` changes after this check, the rehearsal is
run again, its result committed, and that difference checked before he is given an id.

The spending record is committed after his go, so it will always be in a later commit than the
one it names. That is as it should be.

## What cannot be known before a real call

The first check's list stands, with note 3 above added. The half-symbol question from the
second check no longer matters: whatever the service sends, it is saved.

## What John must still do before the first run, in order

1. **Know the three things the script adds beyond the method's words, and say if he objects:**
   three outcomes with no row in the failures table, the markers and lock file in the answers
   folder, and the `labels` command that shows every reply's word count without its words.
2. **Step 3 of the list:** read the cost and terms document and decide the run is within the
   terms as far as he is concerned.
3. **Step 4:** yes or no to the change to the workspace's key-saving script.
4. **Rule the proposed command that sets the key's variable** (step 2 of the day's list). A
   different session has judged it safe and recommends it.
5. **Steps 5 and 6:** make the workspace and the key in Anthropic's console, save the key,
   switch automatic top-up off, and look at the credit left for the month.
6. **Name the ceiling,** knowing that at $5 two calls counted at the most in the first round
   stop the run for good, and that at $10 it takes four. If his figure is not $5, a session
   changes the plan, runs the rehearsal again and commits both, and that difference is checked.
7. **Give the go in his own words, naming Anthropic and one figure with a dollar sign,** and
   the commit a session gives him. A session records it in `docs/spending-record.md` directly
   above its block and commits it.
8. **The run, no later than 2026-11-26,** in the Mac's own Terminal: the folder, the variable,
   `show`, one call with `--stop-after 1`, `labels`, then the rest.
