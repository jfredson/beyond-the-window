# The sealed capture: a second check of the capture script

Written 2026-11-18 by Claude (Fable 5.2), an AI model, in the session that wrote the first
check (`check-2026-11-18-capture-script.md`, commit 04cad04). This is a check by a session that
did not write the script. The script's author answered the first check in commit 05b4516 (the
script, its plan, its rehearsal and its README) and commit f23c238 (the rehearsal's result, 274
checks). I read the whole of the changed script as it stands, not only the difference.

I changed nothing in `capture/`. No model and no service's programming interface was called. I
did not run `capture.py run`. No key was created, read or handled, nothing was spent, and
nothing was written in the real answers folder, which still does not exist. Every reply in my
tests is constructed; none came from any model. This file quotes no question and no word of the
opening note.

## Verdict

**The Anthropic run: yes. Nothing must be fixed.** Both must-fix findings of the first check
are answered, and I could not reopen either. What is sent is unchanged, to the byte. The
rehearsal I ran matches the committed result line for line.

Seven things should be fixed. I would make the first before the first run, because it is two
lines and there are eight days in hand: **a reply that holds half of a two-part symbol can
never be saved** (S1 below). I do not expect Anthropic's service to send one, and the call is
counted if it does, which is why it is not a must fix.

**Google and OpenAI: still not ready,** for the reasons in the first check. They share the
fixed engine. One new finding concerns OpenAI alone (S6).

John has since ruled four points (`docs/rulings/2026-11-18-capture-script-four-points.md`,
"Approve all four"; decided by: mixed), which cover the first check's first finding, the key,
and the two settings. What he must still rule or do is at the foot.

Counts: 0 must fix, 7 should fix, 8 notes.

## How I checked

- Read all 2,180 lines of `capture/capture.py`, the changed parts of `rehearsal.py`, the plan's
  one new setting and the whole README.
- Ran `python3 -I capture/rehearsal.py`: 274 checks, none failed, the same as
  `capture/rehearsal-result.txt` apart from the temporary folder's name. Its last line carries
  the checksums of the script and plan as committed.
- Ran `show` for the Anthropic run. The request it prints is the one it printed before the
  changes: the same address, the same three headers, the same body.
- Ran ten groups of my own tests against the real script with constructed replies and the
  rehearsal's network tripwire on, each group in its own process.
- Ran the script's real network code against a constructed connection that opens nothing, to
  see what it hands back when a reply breaks part way.
- Made 22 broken copies of the script in the scratchpad, aimed at the new code, and ran the
  rehearsal against each.
- Checked the list of error statuses against Anthropic's errors page, which I opened on
  2026-11-18 for the first check and quoted there.

## The first check's first finding: four failed tries shut the model out for the day

**Fixed.** `capture/capture.py`, lines 650 to 661 (the list) and 1541 to 1555 (what is done).

- **My own test, repeated.** A constructed wrong-key error at the first question: one call, no
  wait, and the run stopped with one plain line naming the status, what to fix, and that the
  same command can be run again the same day. The same command later that day, with the
  stand-in healthy: all 50 askings made.
- **The attempt is saved** as a failed attempt, marked as one that trying again cannot cure and
  as not one of the day's tries.
- **The three-tries rule is kept where it belongs.** Three overloaded errors, then a wrong key,
  then one more overloaded error after a restart: the question was left for the next day, so
  the wrong key did not reset or use up the count. A rate limit (429), a conflict (409), a
  request too large (413) and a connection that could not be made each still took four tries
  and were left for the next day.
- **The setting that turns it off restores the old behaviour exactly.** With
  `stop_at_errors_trying_again_cannot_cure = false`: four tries a minute apart, the question
  left for the next day, no call on a restart the same day, and 50 calls the next day. That is
  what the first check found. The rehearsal covers both settings, and a broken copy that
  ignored the setting was caught.
- **The list of statuses is right.** Anthropic's errors page gives 400, 401, 402, 403 and 404
  each a thing to fix (the request, the key, billing, permission, the address) and no advice to
  retry. It says of 409 "Resolve the conflict, then retry the request", of 500 "Retry the
  request with exponential backoff", and of 529 that the service "is temporarily overloaded".
  Those are rightly left off.

**The method correction the author wrote out, which John has now ruled word for word, is
accurate.** Two things it does not say, neither of which changes what he approved:

- The stop is for the whole run, so for OpenAI a wrong key stops every model of that run, not
  only the one being asked. That is the sensible reading and is what the script does.
- Two errors that trying again also cannot cure are not on the list and keep the three tries:
  a request too large (413), which cannot happen with messages of three kilobytes, and the
  form of 429 that means the organization's monthly spend cap is reached, which the errors page
  says "keeps failing until access resumes". The second would use up a day. It needs $500 of
  spending in the month to arise, so I only record it.

One thing to know: a 403 that comes from the service's front door and not from the service
itself is treated the same. In my test the line then read "status 403 (none)" with the advice
about the key's permission. The advice may be off the mark in that case, but stopping without
using up the day is right.

## The first check's second finding: a reply that has arrived can be lost and not counted

**Fixed.** `capture/capture.py`, lines 1475 to 1512 (`Engine.ask`), 1690 to 1776 (the marker
and the writing), 1170 to 1250 (`read_folder`).

Each row of my table of five, repeated:

| What happened | Before | Now |
|---|---|---|
| The stream's first event had an unexpected shape | No file, $0 counted | One file, recorded as "a reply this script could not take apart", everything received saved whole, $0.48 counted, the run stops with a plain line |
| A token count arrived as text | No file, $0 counted | Saved as a reply and counted at $0.48, the run carries on |
| The folder could not be written to | No file, $0 counted | Five quick tries, a plain line that a reply is held, then a try every half minute for half an hour. If the folder is never put right the reply is lost, the run says so, and the next start counts the call from its marker and asks again under a new number |
| The reply's words were also part of the file name | Refused, no file | Saved; 50 files; the list of names is written; one screen line is withheld |
| Ctrl-C while a reply was on its way | 51 calls for 50 askings, one never counted | 51 calls, all 51 counted. With the real network code, what had arrived is handed back and saved first |

I also tried: a count of "Infinity", a negative count, a model name that is a list, and a piece
of the stream that is text where a record is expected. Each was saved and counted, and none put
any word of a constructed reply or the constructed key on the screen, in a marker, in a file
name or in the list of names.

**Is every call now saved, or counted at the most it could cost?** Yes, on every path I could
build:

- **A crash between the marker and the send:** counted at $0.48 on the next start, though
  nothing was sent. The strict direction.
- **Two markers for one attempt:** cannot happen. A marker is created new and an existing name
  is an error, and a number with a marker is never used again.
- **A marker left by a run on another day:** counted, named in a notice at the start, and it
  does not use up that day's tries. The asking is made afresh as attempt 02.
- **A half-written marker:** counted at $0.96, the model's maximum, because nothing says what
  limit was sent.
- **A marker beside a good attempt file:** counted once, from the file.
- **A restart after Ctrl-C:** as in the table.

**Can the new counting refuse a run that should go ahead?** Yes, in three ways. All err toward
not spending, and none can be undone, because no file is ever removed:

1. Two calls with no record in the first round stop the run for good at a $5 ceiling, by the
   same sum as two broken streams (rule 5 multiplies round one by five). With replies of the
   expected size: one such call and the run finished; two and it stopped after round one.
2. Anything that goes wrong in the network code after the marker and before the send leaves
   $0.48 counted for a call that was never made.
3. A nonsense count from the service (S3 below).

The README tells John the first of these before he names his figure, under "What the ceiling
means in practice". Its sums are right.

**A sixth way a reply is lost.** I found one: S1 below.

## Should fix

**S1. A reply that holds half of a two-part symbol can never be saved.**
`capture/capture.py`, lines 1722 to 1723 and 1736, and the loop at 1753 to 1776.

Some symbols, most emoji among them, can be sent by a service as two escaped halves. If the
two halves arrive in one piece Python joins them. If a reply holds one half alone, or the
service splits the pair across two pieces of a stream, the text cannot be written as the file
is written now. I gave the stand-in a constructed reply holding one half. Every one of the 65
tries failed with `UnicodeEncodeError`, the script held the window for half an hour of its own
clock telling the reader to check the folder and the disk, and then said the reply was lost. It
left 66 empty read-only files, and the next start printed 65 notices. The call was counted
once, at $0.48, and the asking was made again, so no money is at risk.

I do not expect Anthropic's stream to do this: as far as I know it sends such symbols whole,
and the script joins all the bytes before reading them. I cannot confirm that without a real
call. The cost if it does is one reply, half an hour, and $0.48 of the ceiling.

Suggested change, two parts. Write the record as bytes, encoded so that a lone half is kept as
its escape and not refused. And in `save`, try again only after an error of the folder or the
disk; after any other kind, go straight to a plainer form of the record that cannot fail the
same way.

**S2. Ctrl-C while a reply is arriving uses up one of that question's two askings, and the
README says Ctrl-C is safe at any time.** `capture/capture.py`, lines 1091 and 1430;
`capture/README.md`, line 98.

A reply cut short by hand, after some text, is recorded as "cut off without the signal that
the reply is complete", which the failures table allows one further asking. In my test that
further asking came back empty, and the question was then left for good with no whole reply in
that round. The cut-off attempt is also counted at $0.48, and two of those in round one stop
the run. So Ctrl-C part way through a reply loses nothing already received, but it is not free.

Suggested change: an attempt stopped by hand does not count as an asking, as it already does
not count as one of the day's tries. And the README says what Ctrl-C costs: safe between calls
and during a wait; during a reply it costs $0.48 of the ceiling.

**S3. A count the service could not truly have reported is used as given.** Lines 1523 to
1528. A negative count for the reply was used where the total still came out above zero, so
the call was counted at less than a tenth of a cent. A count of a million million million
million tokens was saved, and then the line that prints the total failed with an error of the
kind `InvalidOperation`, on that start and on every later one. Both need a nonsense figure from
the service. Suggested: a count below zero, or above the limit that was sent, is treated as one
that cannot be used, and the call is counted at the most it could cost.

**S4. The network code hands back what had arrived only for the kinds of error it names.**
Lines 1055 to 1065. With a constructed connection: a timeout, a dropped connection and Ctrl-C
after two pieces of a reply each handed back the 400 bytes received. An error of any other
kind did not, and those bytes were lost. The call is still counted, from its marker. Suggested:
one more catch, for any other kind, that hands back what arrived and names the kind.

**S5. Three gaps in the rehearsal.** Of 22 broken copies, 19 were caught. Not caught:

- **A marker that cannot be written no longer stops the send.** No case makes the marker's
  folder unwritable before a call.
- **The network code no longer hands back what arrived on Ctrl-C.** The rehearsal tests Ctrl-C
  with a stand-in, never with the script's real network code. A constructed connection, as in
  my test, would reach it without any network.
- **A file that cannot be read, with no marker, is counted as nothing.** The case that should
  catch this reads the expected figure from the very function under test
  (`capture/rehearsal.py`, lines 1310 to 1312), so it passes whatever that function returns.
  The figure should be written out: 64,000 tokens at $15 a million, plus the longest message.

**S6. John's go: two loose ends.** `capture/capture.py`, lines 478 to 486. My six cases from
the first check are now refused, and the spending record must be committed. Still accepted:

- A quotation of "$5,000" or "$5k" matched by words ending "up to $5". Both err low, so no
  money is at risk, but the go would not be his figure.
- For OpenAI: a go quoted for its December models was accepted for its January run when the
  figures were the same, because both name the developer. Before the OpenAI runs, the words
  should also have to carry the run's withdrawal date.

A go that says the opposite ("no go for Anthropic, up to $5 was too much") is accepted. No code
can read that, and the README says so.

**S7. The README's day-of-run steps have three gaps for someone who has not read the code.**
See "The README's instructions for the day" below.

## Notes

1. **A guard was removed, and the reason holds.** The first version refused outright if a file
   name, a fault line or the list of names shared five words with a reply. That is gone from
   all three places, with its rehearsal case. Names are now built only from the plan and
   numbers and checked against a fixed form, and anything printed still goes through the one
   print function, which withholds such a line. I found no path by which a reply's words reach
   a name or the list.
2. **A new command, `labels`, shows the word count of every reply,** not only of faulty ones,
   with its token counts and what it was recorded as. The line for each call during a run now
   shows the token counts too. No words are shown. The method's rule on fault flags says only a
   faulty file's count is printed, so this goes a little further than the method's words. I
   asked for a way to check the first call without reading it; this is that. John should know.
3. **New things in the answers folder:** a folder of markers, one for each call; a lock file;
   and, where a write had to be tried again, files ending `__copy02` and so on. The list of
   names and checksums now includes the markers. A marker holds numbers and a cost, and nothing
   from any reply or the key. The method's section on where replies are kept does not mention
   any of these.
4. **Three outcomes the method has no row for:** "a reply this script could not take apart",
   "sent, with no record written", and "a file that could not be read". Each is counted at the
   most its call could cost. The README lists them.
5. **A slot whose reply the script could not take apart is asked once more and then left,**
   like any other reply that is not whole. Everything received is in the file, so the reply is
   not lost, but it is not labelled as a reply. If that ever happens, a session should say so
   in the record of the run.
6. **An unwritable folder before the first call** gives "an unexpected error of the kind
   PermissionError" from the lock (line 1334), not a plain line. Nothing is sent.
7. **The key.** It is now taken out of the environment before git is started, and a broken
   copy that moved it back was caught.
8. **The looser readings I listed in the first check** (the extra header, the two waits, tries
   starting again at midnight, rule 5 and models not yet asked, the stop reasons filed as the
   length limit) are now each listed in the README, numbers 12 and 16 to 19, with reasons I
   agree with. None was changed in the code, which is right: none spends money or changes what
   is sent.

## The first check's should-fix findings

| Finding | Now |
|---|---|
| S1. A half-written file stops every later run | Fixed. Named in a notice, counted at $0.96, its number not reused, the run carries on. See S5 above for the weak test |
| S2. John's go matched to words about something else | Fixed as far as code can. See S6 above |
| S3. No way to make one real call and stop | Fixed: `--stop-after 1` made one call and stopped between calls; the same command without it made the other 49 |
| S4. Guards that stop a run for a reply's wording | Fixed. Note 1 |
| S5. Broken streams in round one end the run at $5 | Kept, as I advised. The README tells John, with the right sums |
| S6. The key in the environment while git runs | Fixed. Note 7 |
| S7. Two runs at once | Fixed: a second run on the same folder is refused, and a broken copy without the lock was caught |
| S8. The rehearsal missed seven of sixteen changes | Fixed for those seven. Three new gaps, S5 above |
| S9. The capture documents still say no script exists | Not the author's files. Still owed, and now more is owed: see the foot |

## What changed that I did not ask for

I read the whole difference. Beyond the fixes: notes 1 to 5 above; the day check before each
call now reads the same clock reading the call is recorded with, which closes a gap of a few
thousandths of a second at midnight; each record now holds the two waits set on this machine;
and a record that holds something Python cannot write as plain data is written with that thing
turned into text, which for a key or a reply gives the fixed phrase and never the value.

**What is sent is unchanged.** The parts of the code that build and check a request were not
touched. `show` prints the same request as before. Run against a constructed connection, the
real network code sent four headers (`content-type`, `anthropic-version`, `user-agent` and the
key) and the body exactly as built.

Of the first rehearsal's 193 checks, all are still present except the one for the removed
guard (note 1). Nine others were reworded, most because a count in their text changed, and each is still there under its new wording.

## The rehearsal

It cannot reach the network: the same tripwire, installed before the script loads. It matches
the committed result.

Twenty-two broken copies, one change each, aimed at the new code:

| Change | Caught? |
|---|---|
| A rate limit is put on the list of errors that stop the run | Yes |
| Billing (402) is taken off the list | Yes |
| The setting in the plan is ignored | Yes |
| A call with no record is counted as nothing | Yes |
| **A marker that cannot be written no longer stops the send** | **No** |
| Ctrl-C is not held while a reply is in hand | Yes |
| **The network code no longer hands back what arrived on Ctrl-C** | **No** |
| `--stop-after` allows one call too many | Yes |
| Two runs at once are allowed | Yes |
| The go need not name the developer | Yes |
| The spending record need not be committed | Yes |
| A run stopped by hand uses one of the day's tries | Yes |
| A reply that cannot be taken apart no longer stops the run | Yes |
| Every try at the write uses the same name | Yes |
| The key is read after the start checks | Yes |
| `labels` prints the reply's first three words | Yes |
| Counts that cannot be used are counted as nothing | Yes |
| **A file that cannot be read, with no marker, is counted as nothing** | **No** |
| A number is reused after a call with no record | Yes |
| A reply that cannot be taken apart is counted as nothing | Yes |
| The marker also holds the key | Yes |
| The go's figure may be followed by more digits | Yes |

## The README's instructions for the day

They are right in what they say, and safe to follow. The sample first line is correct to the
cent (201 tokens sent and 412 replied come to $0.0068). The table of what each first line means
matches what the script prints. Three gaps:

1. **Step 1 says "Set the variable" and gives no command.** The README admits no document says
   how yet. Someone who has not read the code cannot do this step. It should give the one line
   that sets `BTW_CAPTURE_ANTHROPIC_API_KEY` from the key's file, once that file's place and
   form are settled in `what-john-needs-to-do.md`.
2. **It does not say the commands are run from the repository's top folder.** The first
   README did. Run from anywhere else, the command is not found.
3. **"Ctrl-C is safe at any time now" overstates it** (S2 above).

Two smaller things it could add: what the screen shows after `--stop-after 1` besides the one
line (a line naming the model, the line for the call, a line saying it stopped as asked, and
the total); and that a line beginning NOTICE at the start of a run names a call or a file from
an earlier run that was counted at the most it could cost.

## What cannot be known before a real call

The first check's list stands. One addition: whether the service ever sends a symbol as two
halves split across pieces of a stream (S1). If it does, that reply is lost after half an hour,
and counted.

## What John must still rule or do before the first run, in order

1. **Decide whether S1 is fixed first.** I would. Any change to the script needs the rehearsal
   run again and its result committed, then a short check of that difference alone.
2. **Know what the three additions are, and say if he objects:** the three outcomes the method
   has no row for, the markers and lock file in the answers folder, and the `labels` command
   that shows every reply's word count (notes 2 to 4). They belong in the method as dated
   corrections beside the four he ruled today.
3. **Step 3 of `what-john-needs-to-do.md`:** read the cost and terms document and decide the
   run is within the terms as far as he is concerned.
4. **Step 4:** yes or no to the change to the workspace's key-saving script, which settles
   where the key's file is and what the variable is called in it. The README's missing command
   follows from this.
5. **Step 5 and 6:** create the workspace and the key in Anthropic's console, save the key,
   switch automatic top-up off, and look at the credit left for the month.
6. **Name the ceiling,** knowing that at $5 two calls counted at the most in the first round
   stop the run for good, and that at $10 it takes four. If his figure is not $5 a session
   changes the plan, runs the rehearsal again and commits both.
7. **Give the go in his own words, naming Anthropic and one dollar figure.** A session records
   it in `docs/spending-record.md` directly above its block, with the date and the commit, and
   commits it.
8. **The run, no later than 2026-11-26** as he ruled: `show`, then one call with
   `--stop-after 1`, then `labels`, then the rest.
