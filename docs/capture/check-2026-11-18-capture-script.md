# The sealed capture: a check of the capture script

Written 2026-11-18 by Claude (Fable 5.2), an AI model, in a session started by the planning
session. This is a check by a session that did not write the script. I did not write the
method, the questions, the plan, the rehearsal or any earlier check. I read the two commits
that hold the script (8aa9f13, "the capture script, its plan and its rehearsal", and 0e4442c,
"the rehearsal's result") against `docs/capture/method.md`.

I changed nothing in `capture/`. No model and no service's programming interface was called, by
me or by anything I ran. I did not run `capture.py run`. No key was created, read or handled,
no credentials file was opened, nothing was spent, and nothing was written in the real answers
folder, which still does not exist. This file quotes no question and no word of the opening
note, so it does not need to be held back with `questions.md`.

## Verdict

**The Anthropic run: not yet. Two things must be settled first, and then I would say yes.**

What is sound, and I tried to break each: the bytes that would leave the machine are exactly
the approved message file, as the one user message, with nothing added; the key has no path to
the screen, a file, a file name, the list of names and checksums or the repository; no reply
text has a path to anywhere but the one ruled folder; and a run that goes as planned cannot
spend past its ceiling. The cost arithmetic is right, and the rehearsal I ran matches the
committed result line for line.

What must be settled:

1. **Four failed tries shut the model out for the rest of the day, even after the cause is
   fixed.** On 2026-11-28 that would end the capture for Claude Sonnet 4.5 with nothing asked.
   The first real call is also the first time this code meets the service, so a first-call
   failure is the likeliest thing to go wrong.
2. **A reply that has arrived can be lost before it is saved, and its cost is then not
   counted.** Five different things between "the reply came back" and "the file is written" can
   stop the script, and in each the reply is thrown away. This is the one way I found to spend
   past a ceiling.

**Google and OpenAI: not ready, and not checked to the same depth.** The same two findings
apply. Beyond them, the Google request's field names are still not confirmed on any page (the
reference page lists the reply's fields and not the request's), the name each service reports
for each model is unknown, and I did not reopen OpenAI's model and price pages. OpenAI is not
needed until 2026-12-09. The method already says Google will very likely refuse a new project.

Counts: 2 must fix, 9 should fix, 12 notes.

## How I checked

- Read all 1,718 lines of `capture/capture.py`, all of `rehearsal.py`, `plan.toml`, the README,
  the method, the steps document, the cost document and the writing session's hand-over note.
- Before running anything, read enough to be sure it could not reach the network. `show` builds
  a request and never hands it to the network code. The rehearsal replaces Python's ways of
  opening a connection before the script is loaded.
- Ran `python3 -I capture/rehearsal.py`: 193 checks, none failed, and its output is the same as
  `capture/rehearsal-result.txt` apart from the name of the temporary folder. The two checksums
  on its last line are those of the script and plan as committed.
- Ran `python3 -I capture/capture.py show --run anthropic-2026-11-30`. It sent nothing.
- Made 16 changed copies of the script in the scratchpad, one change each, and ran the
  rehearsal against each to see whether it noticed.
- Wrote 12 hostile tests in the scratchpad that drive the real script's engine with constructed
  replies and the rehearsal's network tripwire on. Every reply in them is constructed; none came
  from any model.
- Opened the developers' own pages on 2026-11-18 (listed under "Facts about the three
  interfaces"), and loaded the workspace's reference for Anthropic's interface.
- Compared the ten checksums in `docs/capture/sent/SHA256SUMS` with the ten in John's second
  approval (`docs/rulings/2026-11-18-capture-approval-second.md`) and with the files themselves.
  All three agree.

## Must fix before any real run

### M1. Four failed tries shut the model out for the rest of the Pacific day

`capture/capture.py`, lines 1221 to 1223 (`next_step`) and 1397 to 1401 (`run_model`).

When a question brings no reply, the script tries three more times a minute apart, then leaves
the question "for the next day" and stops that model's run. The count of failed tries is read
from the files on disk, so it survives a restart. I tested it: four constructed "wrong key"
errors at the first question, then the same command again later the same day with the stand-in
service healthy. The second run made no call at all and stopped at once. Only on the next day
did it carry on.

Why this matters. The method's first row says "left for the next day", so the script is
faithful. But three minutes of failures now cost a whole day, whatever the cause: a key pasted
wrong, a workspace with no credit, an overloaded service. Anthropic's withdrawal page (opened
2026-11-18) says "Deprecated models are likely to be less reliable than active models." If the
first run is on 2026-11-28, the next day is past the last safe day and every asking is recorded
as not made. The hand-over note says a failure that retrying cannot cure "costs nothing and
wastes three minutes". That is not right: it uses up the day.

Suggested change, either of these, and the second needs John's ruling because the method is
approved:

- **In the script:** treat an error that trying again cannot cure as a stop and not as a try.
  For Anthropic these are status 400, 401, 402, 403 and 404 (Anthropic's errors page: a problem
  with the request, the key, billing, permission, or the address). The attempt is still saved.
  The run stops with a line saying what to fix, and the same command can be run again the same
  day. The three-tries rule then covers what it was written for: a timeout, a rate limit, an
  overloaded service.
- **Without touching the script:** John rules that the first Anthropic run happens no later
  than 2026-11-26, so that two spare days remain. Nothing in the method says to wait for the
  last safe day.

Either way, one habit helps on the day: if the first line says "failed attempt", press Ctrl-C
during the one-minute wait that follows. Nothing is in flight during the wait, so nothing is
lost, and only one of the day's four tries is used.

### M2. A reply that has arrived can be thrown away, and its cost is not counted

`capture/capture.py`, lines 1259 to 1344 (`Engine.ask`) and 1358 to 1381 (`Engine.write`).

The script receives the whole reply (line 1259), then takes it apart, works out the cost,
builds the file name, and only then writes the file (line 1344). Anything that goes wrong in
between stops the script with the reply still in memory. Nothing is saved, and the running
total does not include the call. I produced each of these with constructed replies:

| What happened | Result |
|---|---|
| The stream's first event had a shape the script did not expect (line 669 to 672) | Stopped with `AttributeError`. One call made, no file, $0 counted |
| A token count arrived as text and not a number (line 1268) | Stopped with `TypeError`. One call made, no file, $0 counted |
| The folder could not be written to (line 1375) | Stopped with `PermissionError`. One call made, no file, $0 counted |
| The reply's words were also part of the file name (line 1068) | Refused. One call made, no file |
| Ctrl-C while a reply was on its way | Two files for three calls. After a restart, 51 calls had been made for 50 askings, and one was never counted |

So the method's "Every attempt is kept, failed ones included" does not hold on these paths, and
neither does script rule 4's running total. Each lost call can cost up to $0.48 for Claude
Sonnet 4.5 and is counted as nothing. It takes a crash each time, so the amount is small, but
it is a way past the ceiling and the script cannot see it.

Suggested change:

- Wrap the taking-apart, the cost and the name in a guard, so that whatever goes wrong the
  record is still written with everything the service returned. A reply that could not be
  taken apart is recorded as such and counted at the most the call could cost, as a broken
  stream already is.
- Before sending, write a small "sent" marker for the attempt. On the next start, any marker
  with no attempt file beside it is counted at the most that call could cost and its attempt
  number is not reused. That covers Ctrl-C, a crash and a power cut.
- If the write itself fails, try again a few times before stopping, and say plainly that a
  reply is held and unsaved.

## Should fix

**S1. A half-written file stops every later run.** `capture/capture.py`, lines 1102 to 1103
(`read_folder`). If the process dies during a write, a partly written, read-only file is left.
On the next start `json.load` fails and the script stops with "an unexpected error of the kind
JSONDecodeError", every time. The script may not delete, and sessions may not open reply
files, so only John moving the file by hand clears it. Suggested: a file that cannot be read is
named on screen, counted at the most its call could cost, and its attempt number treated as
used, and the run carries on.

**S2. John's go can be matched to words that were about something else.** `capture/capture.py`,
lines 465 to 472 (`check_go`). The check joins every quoted line in the whole spending record
into one string and looks for the go's words anywhere in it. I tested six cases. Accepted, and
should not be: words that are only "$5" when the quotation is about something else; a go
quoted for Google used for the Anthropic run; words that run across two separate quotations;
a go John later withdrew in a second quotation; a quotation of "$50" matched by "up to $5"
(this one errs low, so it is safe). Refused, correctly: a figure written as "5 dollars". Also,
`check_tree_is_committed` (line 382) looks only at `capture/` and `docs/capture/sent/`, so the
spending record, the steps document and the price list can all be edited and not committed and
every start check still passes; I confirmed that for the spending record. Suggested: the
quotation must sit directly above its block with nothing between; the block gains the date and
the commit John named; and the three documents the plan is checked against must be committed
and unchanged, like the script.

**S3. No way to make one real call and stop.** The first real call is the first test of the
real network code, the real stream and the real reported model name, and the script goes
straight on to the other 49. Stopping it by hand between calls risks M2. Suggested: a
`--stop-after N` option, so the first run is one asking. A session can then check that file's
labels (recorded as "a reply", a stop reason, token counts present, the model name as reported)
without reading the reply.

**S4. Guards against reply words can stop a run because of what a reply says.**
`capture/capture.py`, lines 96 to 106, 167 to 177, 1068, 1504 and 1526. Every reply's runs of
five words are remembered for the life of the process, and three places refuse outright if
their own text shares such a run. With constructed replies: one that shared five words with
the heading of the list of names and checksums meant the list was never written by `run` (all
50 files were safe, and the separate `manifest` command still works); a short one whose words
also appear in its own fault line stopped the run after round one, and again on every restart.
Real replies are very unlikely to do either. But a guard that halts a run on a reply's wording
is the wrong way round. Suggested: these three places leave the line or name out and say so,
as `say` already does, and never raise.

**S5. Two or three broken streams in round one end the run for good at a $5 ceiling.** Lines
1184 to 1196 and 1275 to 1277. A stream that breaks before the counts arrive is counted at
$0.48, and rule 5 multiplies round one by five. The README says three such breaks stop the run.
My test agrees for the rehearsal's tiny constructed replies: two breaks and the run finished,
three and it stopped, and it stopped again on every restart because the files stay. With
replies of the size the cost document expects (about three cents each), the sum is tighter:
two breaks give 5 x (0.96 + 0.25) = $6.05, which is over $5, so two are enough. A laptop going
to sleep or a wireless drop is enough to break a stream. This is the strict reading and I would
keep it. Suggested: tell John before he names his figure, so he can choose a ceiling with room
for it (by the same sum, $10 survives three breaks in round one and stops at four), and keep
the Mac awake during the run.

**S6. The key is in the environment while git runs.** Lines 1684 and 1702. The start checks
run git five times before `read_key` removes the key from the environment, so each of those
git processes is handed it. The docstring at lines 1560 to 1564 says the opposite. Git does
nothing with it, but the claim is untrue as written. Suggested: take the key out of the
environment as the first act of `run`, before any other program is started.

**S7. Two runs at once are not prevented.** Nothing stops the same command running in two
windows. Each keeps its own total. They collide on the first file name and one dies with its
reply lost (M2), but between collisions both spend. Suggested: a lock file in the reply folder.

**S8. The rehearsal misses seven of sixteen deliberate changes.** See "The rehearsal" below.
The two that matter most: it does not prove the engine calls the last check before sending,
and its test that another project's key is not used passes even when the script is changed to
use one.

**S9. The capture documents still say no script exists.** The writing session's hand-over note
lists the wording changes `method.md`, `what-john-needs-to-do.md` and `cost-and-terms.md` need.
I agree with its list. Two matter before John is asked for keys: step 4 of the steps document
still gives the variable names `ANTHROPIC_API_KEY` and the like, and the script reads only
`BTW_CAPTURE_ANTHROPIC_API_KEY`, `BTW_CAPTURE_GOOGLE_API_KEY` and `BTW_CAPTURE_OPENAI_API_KEY`;
and nothing yet tells whoever runs it how the key gets from its file into that variable.

## Notes

1. **The interface version is real.** The script sends `anthropic-version: 2026-10-21`. I
   doubted it and checked. Anthropic's versions page lists it as the latest, "Available on the
   Claude API", and says "Anthropic recommends using the latest API version whenever possible".
   Its examples send the key in `x-api-key` with that version, as the script does. The three
   changes it makes to the Messages interface do not touch this request. The only model limit
   on the page is for Amazon's service, which is not used.
2. **A header the method does not name.** Line 69 adds `user-agent: Python-http.client/3.14.5`.
   Python's own library would send none. It is honest and harmless, but it is one more thing
   sent than the method's table lists, and whether the service's front door accepts it is
   unknown until a real call.
3. **Client-side waits the method does not name:** 300 seconds between pieces of a stream for
   Anthropic, 45 minutes for a whole exchange. Nothing is sent for these.
4. **Tries start again at midnight.** A question that fails across midnight got six tries in a
   row in my test, not four. Harmless.
5. **The day check works on every call.** With a constructed clock starting at 23:58 on the
   last safe day, the script refused the first call after midnight. The rehearsal does not
   cover this (see below), so I record it here.
6. **Rule 5 looks only at models already asked.** For a run with several models the projection
   adds what the others have cost so far, and nothing for models not yet started. The ceiling
   check before every call still holds. Not relevant to Anthropic's one model. The hand-over
   note lists it; the README does not.
7. **Two stop reasons are filed without the README saying so:** Anthropic's
   `model_context_window_exceeded` and Google's `CONTINUATION` are treated as the length limit
   (lines 699 and 732). Google's `OTHER` and its tool and image reasons are treated as an
   ordinary reply. OpenAI's library now lists two more reasons a reply can be incomplete,
   `max_messages` and `steered`; the script treats both as no completion signal.
8. **Each record keeps every header the service returned.** Anthropic's include the
   organization's id and the workspace's id. That is right for a private record. If the answers
   are ever published in full, the records need those lines taken out first.
9. **The screen guard catches five words in a row, not fewer.** A changed script that printed
   the first word of each reply passed the rehearsal. No such print exists in the real script;
   the first protection, that a reply is an object that prints as a fixed phrase, does hold.
10. **The reply folder is not hard-coded.** It comes from `plan.toml` and is checked against
    nothing else. The rehearsal result pins the plan's checksum, so changing it takes a commit
    and a new rehearsal.
11. **The go is not tied to the script.** It is tied to the messages by checksum and to the
    ceiling by figure. The script can change after the go, which is intended, since fixes will
    follow this check.
12. **iCloud.** If the system ever replaces a reply file with a placeholder of another name,
    the script would not see that asking and would ask it again. Current systems keep the name
    and fetch the file when it is opened, and files written minutes ago are not sent away, so I
    do not expect it during a run.

## Every rule and refusal, against the code

| Rule or refusal | Enforced on every path? | What I found |
|---|---|---|
| 1. The key | Yes for printing and saving | One place turns it back into text (line 986). Not printed in any error: `main` prints only the kind of an unexpected error. S6 on git. A departure from the rule's words, see stricter reading 1 |
| 2. Exact bytes, checksums | Yes | Checked at the start and again before every send (line 929). The files, the list and John's ruling agree |
| 3. Ceiling equals John's go | The figure, yes. The words, weakly | S2 |
| 4. Cost, running total, stop before a call that could pass | Yes when every call is recorded | M2 is the gap. Arithmetic checked by hand below |
| 5. Projection after round one | Yes, and again after a restart | Note 6, S5 |
| 6. Last safe day | Yes, before the run and before every call | Note 5 |
| 7. Wrong model stops the run | Yes | Stays stopped on later runs. Counted toward the total |
| 8. File before the next message, read-only, list at the end | Yes on the ordinary path | M2, S1, S4 |
| 9. Interfaces, streaming, `store` false | Yes | Checked against the pages below |
| 10. Fault flags | Yes | S4 |
| 11. A rehearsal | Present and passes | S8 |
| No instruction or second message | Yes | Two layers: a list of things never sent, and an exact-shape check for each developer |
| No earlier exchange | Yes | Same |
| No rewording or retry for what a reply says | Yes | The only reading of a reply is "is it blank" and a word count. S4 is the one place wording can change what happens |
| No hidden reasoning asked for | Yes | Nothing is sent that asks for it |
| No printing or passing on a reply | Yes | Note 9 |
| No reply inside a repository | Yes, three times | Neither `~` nor `~/Documents` is a repository on this Mac |
| No reply words in a name, log or list | Yes | S4 |
| No deleting | Yes | No such call exists. The list of names is written whole each time |
| No raising its own ceiling | Yes | The plan is read-only once loaded |

The failures table: I traced each row through `classify` (lines 1029 to 1054) and `next_step`
(lines 1205 to 1231) and each does what the table says, including the order of "the two things
that come first". Row 1 is M1.

## The money

**One Anthropic call, by hand.** Prices in `plan.toml`: $3 a million tokens sent, $15 a
million replied. At the document's guesses of 500 sent and 2,000 replied: 500 x 3 / 1,000,000 =
$0.0015, and 2,000 x 15 / 1,000,000 = $0.03, so $0.0315. Fifty calls: $1.575. With one fifth
added: $1.89. `show` prints $1.5750 and $1.8900, and `cost-and-terms.md` has $1.58 and $1.89.
They agree.

**The most a call could cost.** At the 32,000 limit: 32,000 x 15 / 1,000,000 = $0.48, plus the
message. The ten messages are 10,288 bytes; the script counts each at its bytes plus 64, so
10,928 x 3 / 1,000,000 = $0.0328 for one round. Five rounds: 50 x $0.48 + 5 x $0.0328 =
$24.1639, which is what `show` prints. The cost document says $24.

**The ceiling check.** Before a first asking the script needs room for that call at its limit
($0.48) and one repeat at the model's maximum of 64,000 ($0.96), so about $1.44. At a $5
ceiling it therefore stops asking once $3.56 is counted. The estimate is $1.58, so there is
room as long as replies average under about 4,600 tokens.

**Can it spend past the ceiling?** Not while every call is recorded: each call is checked
first, at the most it could cost, and counted afterwards at what was reported or, where nothing
was reported, at the most. The paths past it are M2 (a call made and never recorded) and S7
(two runs at once).

**Counted as free: a request answered with an error status.** The README calls this an
unchecked assumption. What the pages say, opened 2026-11-18:

- Google's billing page: "If your request fails with a 400 or 500 error, you won't be charged
  for the tokens used."
- Anthropic's errors page and pricing page: nothing either way. The pricing page says only that
  a web search that fails "is not billed", which is a different thing.
- OpenAI: I did not open a page on this.

If Anthropic did bill a failed request, it could bill only the message sent, about a fifth of
a cent each. So the exposure is cents. An error that arrives inside a stream that began with a
200 status is already counted at the full $0.48.

## The bytes sent

For Anthropic the body is `model`, `max_tokens`, `stream` true and one message with role
`user` whose content is the file's text, and nothing else (line 626). The text is decoded from
the file's bytes and encoded again without escaping to plain letters, and line 942 checks the
round trip. Anthropic's reference says a plain string for `content` "is shorthand for an array
of one content block of type \"text\"". The headers are `content-type`, `anthropic-version`,
`user-agent` and the key. No system text, no thinking setting, no sampling setting, no tools.

For OpenAI the body is `model`, `input` as the plain text, `max_output_tokens` and `store`
false. OpenAI's reference, opened 2026-11-18, says of a string `input`: "A text input to the
model, equivalent to a text input with the `user` role." The README marks this not checked; it
is now checked.

For Google the body is one `user` entry in `contents` and `maxOutputTokens` inside
`generationConfig`. The reference page confirms the address, that a role "Must be either 'user'
or 'model'", and the name `maxOutputTokens`. It does not list the request body's own fields, so
`contents`, `parts` and `text` rest on my memory and the writing session's, which agree.

## The key and the replies

**The key** goes: the environment, to a `Secret` object, to one request header. It is removed
from any record before writing if a service echoes it (tested by the rehearsal). `say` withholds
any line that holds it. An error from Python's library that might quote a header value is
never printed, because `main` prints only the error's kind. Ctrl-C prints a traceback of code
lines, which hold no values.

**A reply's text** goes: the network, to memory, to one file in the ruled folder. In a real run
the engine refuses any folder but the one in the plan (line 1127), and checks three times that
it is outside every repository. Printed lines hold the outcome, a short label from the service
that is restricted to plain characters (line 199), numbers and money. The list of names and
checksums holds only those. The rehearsal result holds no constructed reply text.

**If the write fails,** the reply is lost: M2.

## The rehearsal

It cannot reach the network. The tripwire is installed before the script loads, and the test
that runs the script's real network code against it does trip. All 989 constructed attempt
files carry the word "constructed" in their names and their records, and every stand-in reply
has it in its own text.

Sixteen changed copies of the script, one change each:

| Change | Caught? |
|---|---|
| The ceiling check ignores the possible repeat | Yes |
| The ceiling check compares against twice the ceiling | Yes |
| The ceiling check only stops after the ceiling is passed | Yes |
| A second message is let through for Anthropic | Yes |
| A broken stream is counted as free | Yes |
| A very short reply is asked again | Yes |
| Rule 5 is skipped | Yes |
| An empty system text is also sent | Yes |
| A wrong model no longer stops the run | Yes |
| **The day check before every call is removed** | **No** |
| **The engine no longer calls the last check before sending** | **No** |
| **The key falls back to `ANTHROPIC_API_KEY`** | **No** |
| **The length limit is looked at before the wrong model** | **No** |
| **The repository check inside `write` is removed** | **No** |
| **The running total leaves out wrong-model files** | **No** |
| **The first word of each reply is printed** | **No** |

Why each of the seven slips through, and the test that would catch it:

- The refusals are tested by calling `check_request` directly, never by showing that the
  engine calls it. Add a case where a stand-in receives a request and the test confirms the
  engine refused a doctored one first.
- The key test removes `ANTHROPIC_API_KEY` from the environment before it tests the case where
  this project's variable is missing, so a fallback is never exercised
  (`capture/rehearsal.py`, lines 583 to 590). Test the missing variable while the other is
  still set.
- No case has a stream that both names a different model and gives the length limit.
- The day check is tested only at the start of a run, not part way through.
- No case checks that a wrong-model file's cost is in the total.
- The end check looks for one marker word and one phrase from the constructed replies, and the
  first word of each is neither.
- The repository check in `write` is a third copy of a check tested twice elsewhere. Fine.

So the 193 checks do test what their names say, with one exception: "a key another project
left in ANTHROPIC_API_KEY is not used" would pass whatever the code did.

## Facts about the three interfaces

Pages opened by me on 2026-11-18.

| Fact, as the script uses it | Page | Result |
|---|---|---|
| Anthropic: address, the three headers, `"stream": true` | Streaming page | Confirmed, with the same version header in its own example |
| Anthropic: event names; "A final `message_stop` event"; counts in `message_delta` "are *cumulative*"; an `error` event can arrive in the stream; `ping` events | Streaming page | Confirmed |
| Anthropic: the reported model sits in `message_start` | Streaming page | Confirmed in the example. The exact text for this model is not shown anywhere |
| Anthropic: the seven stop reasons; refusal is "a normal HTTP 200 response" from "Safety classifiers" | Stop reasons page | Confirmed |
| Anthropic: `claude-sonnet-4-5-20250929`, "Deprecated", retirement "November 30, 2026" (2026-11-30); "Requests to retired models fail" | Withdrawal page | Confirmed |
| Anthropic: 64,000 maximum, $3 and $15 | Models overview, pricing page | Confirmed |
| Anthropic: version `2026-10-21` | Versions page | Confirmed, note 1 |
| Anthropic: a high `max_tokens` does not count against the rate limit | Rate limits page: "The `max_tokens` parameter does not factor into OTPM rate limit calculations" | Confirmed. The README does not mention it; it matters at a 32,000 limit |
| Google: address, reply fields, finish and block reasons, token counts | Reference page | Confirmed. The page now also lists a `modelStatus` field, which the script ignores |
| Google: $1.25 and $10.00, $0.30 and $2.50, thinking charged as reply | Pricing page | Confirmed. The same page says requests to both names go to other models from 2026-12-01 |
| Google: thinking counts inside the limit | Thinking page, which describes only the newer interface | Says a limit includes "thought tokens". Not stated for the interface used |
| OpenAI: a plain `input` is one user message | Reference page | Confirmed |
| OpenAI: `store` "Defaults to true when omitted"; the states; the reasons | OpenAI's Python library | Confirmed, with two new reasons (note 7) |
| OpenAI: each model's maximum and price | Not reopened by me | Not checked in this check |

## What cannot be known before a real call

For each: what the script does if it turns out wrong, and what that costs.

1. **The exact model name Anthropic reports.** If it is not `claude-sonnet-4-5-20250929` to
   the letter, the first reply is kept apart and the run stops for good until John rules. Cost:
   one reply, about one cent, and the time to change the plan and rehearse again.
2. **Whether the service accepts this request at all:** the version header with a deprecated
   model, the `user-agent`, the key's workspace, its credit. If not: four failed tries and the
   day is gone (M1). Cost: nothing in money.
3. **Whether Python's library reads the real stream as the stand-in suggests.** If pieces are
   lost: replies recorded as cut off, each asked once more, each first attempt counted at
   $0.48, and rule 5 stops the run after round one (S5). Everything received is still saved.
4. **Whether the real counts arrive where the script looks.** If not: every call counted at
   $0.48, and the run stops after eight askings at a $5 ceiling. No overspend.
5. **How long a real reply runs.** The estimate is a guess. Rule 5 measures round one.
6. **Whether Anthropic bills a request it answers with an error.** If it does: cents.
7. **The names Google and OpenAI report, Google's request field names, and whether Google
   serves a new project at all.** If wrong: the run for that model stops after one call.
8. **How the answers folder behaves under iCloud while files are written** (note 12).

## The thirteen stricter readings and the two proposals

| | Is it the stricter reading? | Does the method allow it? | Ask John? |
|---|---|---|---|
| 1. Key from the environment | Neither. It departs from rule 1's words, "Read each key from its own file" | Not as written | Yes. The method is approved, so its words need a dated correction |
| 2. A ceiling for each run | Yes | Yes, it matches the steps document | No |
| 3. Unknown cost counted at the most | Yes | Yes | Tell him the consequence (S5) |
| 4. An error status costs nothing | No. It is the looser reading, and the README says it is an assumption | Not addressed | No. Confirmed for Google; cents for Anthropic |
| 5. At most one further asking | Yes | Yes | No |
| 6. A question left for the next day stops the model's run | Stricter on order, and it is what makes M1 costly | Yes | Yes, with M1 |
| 7. A wrong model stays stopped | Yes | Yes | No |
| 8. A complete reply naming no model is the wrong-model row | Yes | Not addressed | No |
| 9. Anthropic's `refusal` is "blocked by the service" | A judgment. The page supports it | Yes | Tell him: such a reply is asked once more |
| 10. Words OpenAI files under "refusal" are the reply | Yes | Yes | No |
| 11. "Empty" means only spaces and line ends | Slightly wider than "holds no text" | Yes | No |
| 12. A Google call counted at the model's maximum | Yes | Yes | No |
| 13. The program library is "none" | A fact | Yes | No, but the method's "What is saved" should say so |

**Proposal 1, "very short" is fewer than 20 words.** The method leaves this to be proposed and
approved with the script. A flag changes nothing and costs nothing, so a high threshold is the
safe side. I would approve it. One thing to tell John: after each round the screen shows the
word count of any reply under 20 words, which says a little about that reply. The method allows
exactly that.

**Proposal 2, the further asking after a broken stream uses the same limit.** The method leaves
this to the script. The reasoning is sound and it is the cheaper choice. I would approve it.

**Looser readings the README does not list:** notes 2, 3, 4, 6 and 7 above. None spends money
or changes what is sent to a model beyond the one header in note 2.

## What the first real run would look like

Assuming M1 and M2 are settled, John's go is recorded in `docs/spending-record.md` and
committed, and the key is saved.

1. **Set the key.** In the window that will run the script, the variable
   `BTW_CAPTURE_ANTHROPIC_API_KEY` is set from the key's file. No document yet says how (S9).
   If the name is wrong, the script refuses and nothing is sent.
2. **Run `show`.** Every line should say "pass". It prints the request for the first message.
3. **Run `run`,** with the Mac kept awake and on mains power. A lid closed during the run
   breaks a stream, and two or three of those in round one end the run (S5).
4. **Watch the first line.** It should read: question 1, asking 1, attempt 01, "a reply", stop
   reason `end_turn`, counted about one cent. If it says "failed attempt", press Ctrl-C during
   the minute's wait and find the cause (M1). If it says "wrong model", the run has stopped and
   nothing more is asked.
5. **Fifty lines follow,** probably over 15 to 30 minutes. After every ten: "round N is
   complete", and a fault check that lists file names and counts only. After round one, a line
   giving the projection for five rounds.
6. **The last lines** give the total counted and say the list of names and checksums was
   written. That list is `docs/capture/manifest.md`, which a session then commits.
7. **Afterwards** John compares the total with the Usage page in Anthropic's console.

Where it could go wrong for a reason the rehearsal cannot show: everything in "What cannot be
known before a real call"; the monthly credits having run low by late in the month, which
Anthropic answers with an error that uses up the day's tries (M1); a second window running the
same command (S7); and pressing Ctrl-C while a reply is on its way (M2). The one moment it is
safe to stop the run by hand is during a one-minute wait.
