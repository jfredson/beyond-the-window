# The sealed capture: a check of the corrections made after John's ruling on four points

Written 2026-11-18 by Claude (Fable 5.2), an AI model, in the session that wrote the check
before this one (`check-2026-11-18-method-corrections.md`). This is a check by a session that
did not make the edit. I did not write the ruling, the method, the steps document, the capture
script or either check of the script. I read the commit that applied the ruling ("Capture
documents: the four ruled points on the script, the script's status, and the run's step list",
`da4691a`) against John's ruling of 2026-11-18 on four points of how the capture script applies
the method (`docs/rulings/2026-11-18-capture-script-four-points.md`, "Approve all four",
decided by: mixed), against my own earlier findings, and against the script as it is committed
(`capture/`). I worked from the files and the differences between them, not from the commit's
own account. I changed no file but this one. No model or outside service was called, no key
was handled, nothing was spent or published, and no reply file was opened or made.

## Verdict

**The commit applies the ruling correctly and answers all eleven of my earlier findings. The
step list for the day would work as written, with one sentence that must be corrected before
John follows it.**

- The four ruled points are each in the method where they belong, in the ruling's words, with
  "Approve all four" quoted exactly. Nothing the ruling leaves open is stated as ruled.
- Nothing sent changed. The ten checksums are the ten John approved.
- No document says the script is approved or fit to run. The documents now say less than is
  true: they say the script is waiting for a second check, and that check was committed twelve
  seconds before this commit (should-fix finding 1).
- **Must fix, one:** the step list tells John "Ctrl-C is safe at any time". The second check of
  the script found that pressing it while a reply is arriving costs $0.48 of the ceiling and
  one of that question's two askings.
- **The key-loading command is safe.** It puts the key neither in the shell's history nor on
  the screen. I recommend John approve it, with two small additions. My view is in its own
  section below.

Counts: 1 must fix, 5 should fix, 9 notes.

## How I checked

- **The bytes.** `shasum -a 256 -c SHA256SUMS` inside `docs/capture/sent/`: all ten OK. The ten
  lines of `SHA256SUMS` compared by program with the ten in John's second approval
  (`docs/rulings/2026-11-18-capture-approval-second.md`): the same. `sent_files.py` in its
  check mode: passed.
- **What the commit touches.** Three files, all changed and none added or removed:
  `method.md`, `what-john-needs-to-do.md` and `cost-and-terms.md`. Nothing in `capture/`,
  `docs/rulings/`, `docs/capture/sent/`, no earlier check and no open question.
- **The quoted exception.** A short program took the quoted block from the ruling and the
  quoted block from `method.md` and compared them: 1,043 characters each, identical.
- **John's words.** "Approve all four" appears seven times in `method.md` and five in
  `what-john-needs-to-do.md`, the same each time.
- **The step list against the code.** I read the parts of `capture/capture.py` the list
  depends on, as committed: how commands are read (`main`), how the key is read (`read_key`),
  what `show` prints, the checks made before a run (`start_checks`, `check_tree_is_committed`,
  `check_last_safe_days`, `check_prices`, `check_go`, `check_rehearsal_passed`), and where the
  reply folder is made. I read the whole of `capture/README.md` and both checks of the script.
- **The script's `show` command,** which sends nothing and reads no key. Both checks that
  compare the plan with the two documents this commit edited still pass: "the last safe day
  equals the one in what-john-needs-to-do.md" and "the prices equal the dated price list in
  cost-and-terms.md". So the edit did not break the table the script reads.
- **The key-loading command,** on eight made-up files in my scratch folder, each holding the
  word "constructed" in place of a key. No real key file was opened; the real one does not
  exist yet.
- **The key-saving script** in the TimeAssembler repository
  (`tools/rotate-key/rotate-key.sh`), read for the form of the line it writes. I opened no key
  file.

## What passes

**1. The four ruled points.**

| Point | Where it is now | Right? |
|---|---|---|
| The exception to the first row of the failures table | `method.md`: a pointer in the row itself, and the exception under the table (lines 198 to 220), quoted from the ruling. `what-john-needs-to-do.md`: the status (lines 22 to 23) and the first row of the day's table | Yes, word for word. The row is left as approved |
| The first Anthropic run no later than 2026-11-26; 2026-11-28 stays the last safe day | `method.md`, script rule 6 and "Before anything is asked". `what-john-needs-to-do.md`: the status, the head of the step list, and a correction under the table of last safe days | Yes. The table is left alone, rightly: the script reads it. The date "by 2026-11-25" for finishing the earlier steps is marked as the session's own arithmetic and not part of the ruling |
| The key reaches the script through a setting in the shell; the script opens no credentials file | `method.md`, script rule 1, old words struck through. `what-john-needs-to-do.md`, steps 4 and 6 and the step list | Yes. The three names given are the ones `read_key` uses |
| Fewer than 20 words is very short; the same length limit after a broken stream | `method.md`: the faulty-files paragraph and the broken-stream row of the failures table, old words struck through | Yes. The correction notes that the figure is held in `capture/plan.toml` and not in the script |

Nothing the ruling's "Not covered" section leaves open is stated as ruled. The method says
"The ruling does not say the script is fit to run" (line 45). The steps document marks the
key-loading command PROPOSED and says that whether a session may type the commands in John's
place is not ruled. The other places where the script reads the method strictly are listed at
the foot of `method.md` as not changed.

**2. My eight out-of-date sentences and three should-fix findings.** All eleven are answered.
The three should-fix findings were applied in the words I suggested (`cost-and-terms.md`,
lines 189 to 192; `method.md`, lines 260 to 265, marked as the session's reading and not a
ruling; `what-john-needs-to-do.md`, step 1). Each of the eight sentences is struck through or
answered beside itself. None overstates the script's standing.

**3. The step list, checked against the code.** These are right:

- The three commands exist as written: `show --run`, `run --run ... --stop-after 1`, and
  `labels`. The run's name, `anthropic-2026-11-30`, is the one in the plan.
- The variable name is the one the script reads. `show` prints a pass or FAIL line for whether
  it is set, without reading its value, so an empty setting is caught at step 3, before
  anything is sent.
- The form of the go matches `check_go`: the words must name the developer and carry exactly
  one figure with a dollar sign; "5 dollars" is refused; the quotation must sit directly above
  its block; the record must be committed.
- The script makes the reply folder itself, so no step is missing there.
- The table of what each first line means matches the README, which the second check of the
  script compared with what the script prints.
- The two things John is told about the ceiling ($0.48 for a call whose cost was not reported;
  the first round multiplied by five) match the README and both checks.

**4. Nothing sent changed,** and the commit touches nothing it should not. See above.

**5. Form.** Every change is a dated correction. The five passages that were replaced are
struck through and still readable. Nothing was deleted. The added lines hold no long dash.

## Must fix

### 1. "Ctrl-C is safe at any time" is not true, and following it can end the run

`docs/capture/what-john-needs-to-do.md`, line 320.

The line reads: "Ctrl-C is safe at any time. What has arrived is saved and counted first." It
follows the script's README, line 98. The second check of the script found that the README
overstates this (`check-2026-11-18-capture-script-second.md`, should-fix finding S2). Pressing
Ctrl-C while a reply is arriving does save what has arrived. It also records the attempt as cut
off, which uses one of that question's two askings, and counts the call at $0.48. Two calls
counted that way in the first round stop the run for good at a $5 ceiling, as the same
document says of broken connections three lines above.

The step list is the page John reads on the day, and this is the one sentence in it that could
lead him to do harm by following it. The table in step 5 already gives the right advice for
one case ("press Ctrl-C during the wait").

*Suggested change.* Leave the line, struck through, and add: "Corrected: Ctrl-C is safe
between calls and during the minute's wait after a failed attempt. While a reply is arriving it
loses nothing already received, but that call is counted at $0.48 and uses one of that
question's two askings (`check-2026-11-18-capture-script-second.md`, finding S2). Do not press
it while a reply is arriving unless you must." If the script is changed so that an attempt
stopped by hand no longer counts as an asking, the line is corrected again to match.

## Should fix

### 1. The documents say the script is waiting for a second check, and that check exists

`docs/capture/method.md`, lines 37, 325, 356 and 430, and lines 44 to 45.
`docs/capture/what-john-needs-to-do.md`, lines 17, 229, 240 and 365.

The second check of the script (`check-2026-11-18-capture-script-second.md`, commit `1420917`)
was committed at 19:10:16 Pacific on 2026-11-18. This commit followed at 19:10:28. So the
eight places were out of date when they were written, by seconds. They understate and do not
overstate, which is the safe direction. They still need correcting, because that check asks
things of John that the documents do not carry:

- Its verdict is yes for the Anthropic run with nothing that must be fixed, seven things that
  should be, and not ready for Google and OpenAI.
- It asks John to decide whether its first finding is fixed before the first run (a reply
  holding half of a two-part symbol can never be saved). Any change to the script means the
  rehearsal is run again, its result committed, and that difference checked.
- It asks that John know three additions the method has no words for: three outcomes with no
  row in the failures table, the marker and lock files in the answers folder, and the `labels`
  command, which shows every reply's word count.

`method.md`, lines 44 to 45, says "What is still his about the script now is his go for each
run". After the second check that is too little: the first two points above are his as well.

*Suggested change.* A dated addition beside each of the eight places, or one paragraph in each
document that the others point to: the second check is done, with its verdict in its own
words, and what it leaves for John. In the step list's "Before the day" (line 240), name the
check, and add: "its findings are dealt with as you decide; if the script changed, the
rehearsal was run again and its result committed". No document should say "approved to run".
What allows a run is John's go.

When I looked, `capture/capture.py`, `plan.toml` and `rehearsal.py` had changes not yet
committed, by another session. Until they are committed with a new rehearsal result, `show`
fails two of its checks. That is the script working as designed, and it is a reason not to
write the correction until that work lands.

### 2. Step 8 tells John to close the window before he has read what it shows

`docs/capture/what-john-needs-to-do.md`, lines 308 to 312.

Step 8 opens "Close the Terminal window, which removes the key from it", and then says the
last lines of the run give the total, which he is to compare with Anthropic's console. Read in
order, he closes the window first and the total is gone. It is still in the list of file names
a session commits, so nothing is lost, but the step is in the wrong order.

*Suggested change.* Put the reading first: "Read the last lines: the total counted, and that
the list of names and checksums was written. Note the total. Then close the Terminal window,
which removes the key from it."

### 3. The command in step 2 is proposed, and nothing in "Before the day" says it must be ruled first

`docs/capture/what-john-needs-to-do.md`, lines 238 to 243 and 255 to 267.

The step list is meant to be followed on the day. Step 2 carries a block marked "PROPOSED
2026-11-18, not ruled" in the middle of it. John would meet an unruled choice while typing
commands.

*Suggested change.* Add to "Before the day": "You have ruled the command in step 2." When he
rules, replace the PROPOSED block with the ruling, keeping the block's words struck through.

### 4. Step 5 says "the one line", and the screen shows more

`docs/capture/what-john-needs-to-do.md`, line 282.

The second check of the script says that after `--stop-after 1` the screen shows a line naming
the model, the line for the call, a line saying it stopped as asked, and the total. It also
says a line beginning NOTICE at the start of a run names a call or file from an earlier run
that was counted at the most it could cost. Someone told to read "the one line" will see four
or more and may think something is wrong.

*Suggested change.* "Four lines are printed: the model's name, the line for the call, a line
saying the script stopped as asked, and the total. Read the second. A line beginning NOTICE is
about an earlier run's call counted at its highest possible cost; tell a session what it says."

### 5. Nothing says which Python the commands need

`docs/capture/what-john-needs-to-do.md`, step list, steps 3 to 7.

The script needs Python 3.11 or later (`capture/README.md`, line 20). On this Mac `python3`
resolves to version 3.14.5 from Homebrew in the shell I ran, so the commands work here. The
Mac's own `/usr/bin/python3` is 3.9.6, and under it the script stops at once with an error
about a missing part named `tomllib`. A Terminal window set up differently would hit that.

*Suggested change.* One line in "Before the day": "In the Terminal window you will use,
`python3 --version` says 3.11 or higher."

## The key-loading command

The command, as proposed in step 2 of the list:

```bash
export BTW_CAPTURE_ANTHROPIC_API_KEY="$(sed -n 's/^BTW_CAPTURE_ANTHROPIC_API_KEY=//p' ~/.config/sentient-horizons/beyond-the-window.env)"
```

**Is it safe? Yes.**

- **The shell's history.** The history records what is typed. What is typed holds the file's
  path and the variable's name, and no part of the key. The key is read by the shell while the
  command runs and is never written there.
- **The screen.** Nothing is printed. `sed -n` prints only the matching line's value, and that
  goes into the setting, not to the window.
- **Other programs' view.** The key is not an argument of any command, so a list of running
  programs does not show it.
- **Only one key is loaded.** The other two lines of the file are not read into the window.
  This is the command's advantage over the workspace's usual one, which loads every line.

**What I tried.** On made-up files, each with a constructed value and no key:

| How the line is written in the file | What the setting holds | What happens next |
|---|---|---|
| `NAME=value`, as step 4's correction says and as the key-saving script writes | The value | Works |
| The same with a Windows line end | The value and one stray character | Works: the script trims it |
| `export NAME=value`, or a space before the name, or spaces round the equals sign | Nothing | `show` in step 3 says FAIL for the setting. Nothing is sent |
| `NAME="value"`, in quotation marks | The value with its quotation marks | `show` passes. The first call is refused with status 401, the script stops and says the key is at fault, and none of the day's tries is used |
| The line twice | Both values, on two lines | `show` passes. I did not test what the script does with it |
| No file | Nothing, and one line from `sed` saying there is no such file | `show` says FAIL |

So every mistake in the file but one is caught by step 3 or by the first call, and costs
nothing. The key-saving script replaces a key's line and does not add a second, so the doubled
line should not arise unless the file is edited by hand.

**What stays true after the command, and John should know.**

- The key sits in that window until the window is closed or the setting is removed. Every
  program started from the window is handed it. The capture script takes it out of its own
  copy at once; `caffeinate`, which wraps the run, holds its copy until the run ends. Programs
  run by the same user on the same Mac can read that. This is ordinary for a key used from a
  shell, and I do not think it needs changing.
- Four things typed in that window would show the key: `echo` with the setting's name, `env`,
  `printenv`, and `export -p`. None is in the list.
- **The window should be the Mac's ordinary Terminal app, not the Terminal panel inside the
  Claude app.** A session can read that panel's screen and start commands in it. The command
  prints nothing, so reading the screen shows no key, but a session able to start commands in
  a window that holds the key is "a session handling the key", which the list rightly says is
  not ruled.

**What I recommend.** Approve the command as written, with two additions to the list:

1. In "On the day": "Use the Mac's own Terminal app, not the Terminal panel in the Claude
   app."
2. At the end, after the last lines are read, either close the window or type
   `unset BTW_CAPTURE_ANTHROPIC_API_KEY`. Either removes the key. Closing is simpler and is
   what the list says now; it only needs to come after the reading (should-fix finding 2).

*Confidence:* high that it keeps the key out of the history and off the screen, which I tested
on made-up files. Moderate on the whole, because the real file does not exist yet and its form
depends on a change to the key-saving script that is not made. *Judgment call.* *Strongest
alternative:* put the setting in front of each command instead of exporting it, so the key
exists only for that one program. It is tidier and leaves nothing in the window. Its cost is a
much longer line typed three times on the day, by a person, with more room for a slip, and I
would not trade that for the gain.

One thing follows for the change to the key-saving script (step 4 of the steps document): its
check should confirm that the file holds exactly one line for each name, written as
`NAME=value` with no quotation marks, since that is the form this command depends on.

## Notes

1. **The plan and the README still say "PROPOSED" for what is now ruled.** `capture/plan.toml`
   (the comments above `very_short_words` and above the switch for errors that trying again
   cannot cure) and `capture/README.md` ("PROPOSED 2026-11-18, for John. None is approved").
   This commit rightly did not touch `capture/`. It is for the session that maintains the
   script, and a change to the plan's comments changes the plan's checksum, so the rehearsal
   is run again after it.
2. **On the day, nobody else may be editing the script or the two documents it reads.** The
   script refuses to run if `capture/`, the message files, the spending record,
   `what-john-needs-to-do.md` or `cost-and-terms.md` has changes that are not committed. A
   session working on any of them at that hour would make `show` fail. Worth one line in
   "Before the day".
3. **Step 6 of the list** says a session may run `labels`. It should run it in its own shell,
   not in John's window, which holds the key. The command itself does not use the key.
4. **The second check of the script lists looking at the credit left for the month** among
   what John does before the run. The step list does not mention it. If the credit has run
   out, the first call stops with a status the script names, and nothing is lost.
5. **The method's rule 11** lists what the rehearsal must cover and does not mention the
   exception to the first row. The rehearsal does cover it (the cases the README heads "M1").
   A later correction could say so.
6. **"(the paragraph above)"** in `method.md`, line 263, points at the paragraph on
   "summarised", which is two paragraphs above it and not one. A reader will find it.
7. **The three variable names sit inside the correction marked "ruled by John"** (`method.md`,
   script rule 1). The ruling says "a setting in the shell" and names no variable. The names
   are facts about the script and not rulings; the sentence would be clearer if it said so.
8. **The file's place** (`~/.config/sentient-horizons/beyond-the-window.env`) is still marked
   "Proposed" in step 4 and waits for John's yes with the change to the key-saving script. The
   command in step 2 uses it. The list says the earlier steps must be done first, which covers
   this.
9. **The form of John's go** printed in step 7 still reads "as written in `docs/capture/` at
   commit ______". The correction under it explains that the commit covers the whole
   repository, the script included. That is enough, and the script checks only that the commit
   exists.

## What I did not do

I did not check the capture script itself; two checks by another session have. I did not run
`capture.py run`, and no service was called. I did not test what the script does with a key
holding a line break. I opened no developer's page. I fixed nothing.
