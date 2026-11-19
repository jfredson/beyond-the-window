# The sealed capture script

Written 2026-11-18 by Claude (Fable 5.2), an AI model, from the specification in
`docs/capture/method.md` ("What the script must do, and must refuse to do"), which John approved
on 2026-11-18. John said the same day: "Yes, start the capture script now".

A session that did not write it checked it the same day
(`docs/capture/check-2026-11-18-capture-script.md`). That check found two things that must be
fixed before any real run and nine that should be. This version answers them; the section
"What changed after the check" says how, one by one. A different session checks it again.

**Nothing has been run against any service.** No model has been asked anything, no key has been
handled, and nothing has been spent. The first real call will also be the first time this code
meets a real service. The section "The day of the first run" is written for that.

## What is here

| File | What it is |
|---|---|
| `capture.py` | The script. Python's standard library only, so every line that touches the network is in this one file (class `HttpsTransport`). Needs Python 3.11 or later; written and rehearsed on 3.14.5. |
| `plan.toml` | The data the script reads and cannot change: the models, each last safe day, each ceiling, each price, the threshold for a "very short" reply, and one switch (see proposal 3). |
| `rehearsal.py` | The rehearsal the method requires (script rule 11). It calls no service. |
| `rehearsal-result.txt` | The saved output of the rehearsal, committed separately. The script refuses a real run unless this file ends with a pass for the script and plan exactly as they stand. |

## The day of the first run

For the Anthropic run. The last safe day is 2026-11-28, and nothing says to wait for it: a run
two or three days earlier leaves room to fix whatever the first call shows.

**Before the day**

1. John's go is recorded in `docs/spending-record.md` in the form given below, and committed.
2. John knows two things about the ceiling before he names his figure (see "What the ceiling
   means in practice").
3. The key is saved in its file, and whoever runs the script knows how the key gets from that
   file into the variable `BTW_CAPTURE_ANTHROPIC_API_KEY` in the window that runs the command.
   The script never opens the file. No document says how yet; that wording is owed in
   `what-john-needs-to-do.md`.

**On the day, in one window, with the Mac on mains power**

1. Set the variable, then show the run. Every line under "Checks made before a real run" must
   say `pass`. Nothing is sent.

   ```bash
   python3 -I capture/capture.py show --run anthropic-2026-11-30
   ```

2. Make **one** call and stop. `caffeinate -i` keeps the Mac awake while the command runs.

   ```bash
   caffeinate -i python3 -I capture/capture.py run --run anthropic-2026-11-30 --stop-after 1
   ```

3. Read the one line it prints for that call. A good first line reads like this:

   ```text
   q01 asking 1 attempt 01: a reply (stop reason end_turn; model reported as named: yes; tokens sent 201, replied 412; limit 32000; counted $0.0068; run total $0.0068 of $5.0000)
   ```

   What each other first line means, and what to do:

   | The line says | What happened | What to do |
   |---|---|---|
   | `STOPPED: the service answered with status 401` (or 400, 402, 403, 404) | An error that trying again cannot cure: the key, billing, permission, or the request itself. The line says which and what to fix. None of the day's tries is used | Fix it and run the same command again, the same day |
   | `failed attempt`, then a wait | A timeout, a rate limit or an overloaded service. The script waits a minute and tries again, up to three more times. After four, the question is left for the next day | Let it try. If the cause is on this side (no network), press Ctrl-C during the wait, fix it, and run again: a try already made stays used |
   | `wrong model` | The service reported a name that is not `claude-sonnet-4-5-20250929` to the letter. The reply is kept apart and this model's run stays stopped | Tell John. A session looks at the name with the `labels` command |
   | `a reply this script could not take apart` | The script failed on a real reply. Everything the service sent is saved whole, and the call is counted at the most it could cost | Do not run again. A session looks at the script |
   | `model reported as named: NO`, or token counts of `none` | The reply was saved, but the script is not reading the service as expected | Stop and have a session look before going on |

4. If the first line is good, a session may run the `labels` command, which lists what each
   file was recorded as and the service's labels, and no word of any reply:

   ```bash
   python3 -I capture/capture.py labels
   ```

5. Run the rest. The same command without `--stop-after` carries on from the files on disk.

   ```bash
   caffeinate -i python3 -I capture/capture.py run --run anthropic-2026-11-30
   ```

   Forty-nine more lines follow, probably over 15 to 30 minutes. After every ten: "round N is
   complete" and a fault check that lists file names and counts only. After round one, a line
   giving what five rounds would cost at that rate.

6. The last lines give the total counted and write the list of names and checksums,
   `docs/capture/manifest.md`, which a session then commits. John compares the total with the
   Usage page in Anthropic's console.

**Things not to do during a run**

- **Do not close the lid or let the Mac sleep.** A stream that breaks is counted at $0.48, and
  two of those in round one can end the run for good (below).
- **Do not run the same command in a second window.** The script now refuses a second run on
  the same folder, so this only wastes a minute.
- **Ctrl-C is safe at any time now.** If a reply is on its way, what has arrived is saved and
  counted first. If a reply is in hand, its file is written first. The quietest moment is still
  the minute's wait after a failed attempt.
- **If the screen says `A REPLY IS HELD IN MEMORY AND IS NOT YET SAVED`, do not close the
  window and do not press Ctrl-C.** The reply folder could not be written to. Check that the
  folder exists and the disk is not full. The script tries again every half minute for half
  an hour and saves the reply as soon as it can.

## What the ceiling means in practice

Tell John these before he names his figure.

- **A call whose cost the service did not report is counted at the most it could cost,** $0.48
  for Claude Sonnet 4.5. That is the strict reading of rule 4. A stream broken by a sleeping
  laptop or a wireless drop is such a call.
- **Rule 5 multiplies round one by five.** With replies of the size the cost document expects
  (about three cents each), two broken streams in round one give 5 x (0.96 + 0.25) = $6.05,
  which is over $5, so the run stops after round one and stops again on every restart, because
  the files stay. By the same sum a ceiling of $10 survives three breaks in round one and stops
  at four. The estimate for the whole run is $1.89 either way; the ceiling only sets how much
  room there is for breaks.
- **Before a first asking the script needs room for that call at its limit and one repeat at
  the model's maximum,** about $1.44. At a $5 ceiling it therefore stops asking once $3.56 is
  counted.
- Anthropic's rate-limits page says "The `max_tokens` parameter does not factor into OTPM rate
  limit calculations" (read by the checking session, 2026-11-18), so a limit of 32,000 does not
  by itself use up the allowance for tokens a minute.

## John's go, in the spending record

`docs/spending-record.md` does not exist yet. For each run it must hold John's words as a
quotation and, **directly under that quotation**, one block in this form, which the session
that records his go writes:

````markdown
> Go for the sealed capture as written in `docs/capture/` at commit abc1234. Anthropic, up to $5.

```sealed-capture-go
run = "anthropic-2026-11-30"
date = "2026-11-20"
commit = "abc1234"
ceiling_usd = "5.00"
johns_words = "Anthropic, up to $5"
messages_sha256 = "the SHA-256 checksum of docs/capture/sent/SHA256SUMS"
```
````

The script checks that `ceiling_usd` equals the plan's ceiling; that `johns_words` appears
word for word in the one quotation directly above the block, names the developer, and carries
exactly one dollar figure, the ceiling; that `commit` is a commit of this repository; that
`date` is there; and that `messages_sha256` is the checksum of the list of message checksums
as it stands. The spending record must be committed, like the script.

What no code can check: that the quotation is what John said, and that he has not since
withdrawn it. If he withdraws a go, a session takes it out of the record, block and all.

If John's figure differs from the plan's, a session changes the plan in a commit and runs the
rehearsal again; the script never does.

## The key

The script reads the key from one environment variable and nowhere else:
`BTW_CAPTURE_ANTHROPIC_API_KEY`, `BTW_CAPTURE_GOOGLE_API_KEY` or `BTW_CAPTURE_OPENAI_API_KEY`.
It never opens a credentials file. The names are this project's own on purpose: a key another
project left in the shell under a common name such as `ANTHROPIC_API_KEY` is not picked up.
In a real run, taking the key out of the environment is the first thing the script does,
before it starts git or anything else, so no other program is handed it. The key is held in
an object that prints as a fixed phrase, is turned back into text in one place only (the
request header), and is taken out of any record before it is written, should a service ever
send it back.

## What is written in the reply folder

In `~/Documents/Workspace/Beyond the Window/sealed-capture/`, and nowhere else:

- **One file for each attempt,** read-only, named by developer, model, question, asking and
  attempt number. If a write had to be tried more than once, the name ends `__copy02`,
  `__copy03` and so on.
- **`sent-markers/`**: one small file for each call, written just before it is sent. It holds
  the attempt's numbers, the length limit and the most the call could cost, and nothing from
  any reply. A marker with no attempt file beside it means a call was sent and nothing was
  saved (a crash, a power cut). The next start counts that call at the most it could cost and
  never uses its number again.
- **`wrong-model/`**: a reply from a model other than the one named, kept apart.
- **`one-run-at-a-time.lock`**: an empty file the script holds while it runs.

An attempt is recorded as one of the method's seven outcomes, or as one of three this script
adds for trouble on its own side, each counted at the most the call could cost: "a reply this
script could not take apart" (saved whole; the run stops), "sent, with no record written" (a
marker only), and "a file that could not be read" (half written when the machine stopped; it
is named on screen and the run carries on).

Each attempt file keeps every header the service returned. Anthropic's include the
organization's id and the workspace's id. That is right for a private record. If the answers
are ever published in full, those lines are taken out of the published copies first.

## PROPOSED 2026-11-18, for John

None is approved. Each has the four things the project asks for.

**1. "Very short" means fewer than 20 words.** *The choice:* a reply of 19 words or fewer is
listed after its round as very short, kept, and never asked again. *Confidence:* moderate.
*Judgment call.* An ordinary full sentence is fifteen to twenty words, so a reply under twenty
is at most about one sentence. A flag costs nothing and changes nothing, so erring high is
cheap. One thing to know: the screen then shows the word count of any reply under 20 words,
which says a little about that reply; the method allows exactly that. *Strongest alternative:*
5 words, which lists only fragments and would miss a one-line reply cut short without the
service saying so.

**2. After a reply cut off without the service's signal that it was complete, the one further
asking uses the same length limit, not the model's maximum.** The method leaves this to the
script. *Confidence:* high. *Judgment call.* A broken stream is not a sign that the limit was
too low. *Strongest alternative:* the maximum, as for a reply stopped at the length limit.

**3. An error that trying again cannot cure stops the run and is not one of the day's tries.**
This narrows how the method's first failure row is applied, and the method is approved, so it
waits for John. *The choice:* when Anthropic's service answers with status 400, 401, 402, 403
or 404 (a problem with the request, the key, billing, permission or the address), the attempt
is saved, the run stops with one line saying what to fix, none of the day's tries is used, and
the same command can be run again the same day. A timeout, a rate limit, a server error and an
overloaded service keep the three tries as the method wrote them. *Confidence:* high.
*Judgment call.* The reason: without it, a mistyped key on 2026-11-28 uses four tries in three
minutes, the question is left for the next day, and the next day is past the last safe day, so
every asking is recorded as not made. Anthropic's errors page (opened 2026-11-18) gives each of
the five a thing to fix and no advice to try again. *Strongest alternative:* leave the row as
written and have John rule that the first run is no later than 2026-11-26, which costs
nothing in code and still loses a day to each such mistake. **If John says no, one line turns
it off:** `stop_at_errors_trying_again_cannot_cure = false` in `plan.toml`, then the rehearsal
again. The rehearsal covers both settings.

For OpenAI the same applies to 401 and 403 only, the two its error guide gives a status and a
fix for. For Google it applies to nothing: its errors page describes its newer interface and
does not say it covers the one used.

The dated correction the method would need, for John to approve or refuse:

> *Dated correction, 2026-11-18, waiting for John.* The first row of the failures table reads:
> "No reply: an error, a timeout, a rate limit ... Tried again up to three times, a minute
> apart, then left for the next day." It is applied with one exception. **An error that trying
> again cannot cure is not tried again and is not one of the day's tries.** For Anthropic
> these are the service's statuses 400, 401, 402, 403 and 404: a problem with the request, the
> key, billing, permission, or the address. For OpenAI, 401 and 403. For Google, none, until a
> page confirms them for the interface used. The attempt is kept as a failed attempt, with
> the error. The run stops and says what to fix, and may be run again the same day. Every
> other failed attempt (a timeout, a rate limit, a server error, an overloaded service, a
> connection that fails) is tried again up to three times as before. The reason: four tries at
> an error of this kind would use up the day, and on the last safe day that would end the
> capture for the model with nothing asked. It can be turned off by one line in
> `capture/plan.toml`.

## Where each rule is enforced, and which rehearsal case proves it

Names in the middle column are functions or classes in `capture.py`. Names in the last column
are the headings the rehearsal prints.

| The method's rule | Enforced in | Rehearsal case |
|---|---|---|
| 1. Key from its own place outside the repository, never printed, never another project's | `read_key` (first act of `main` for a run), class `Secret`, `say`, `Engine.write` | THE KEY; THE KEY, again; THE SOURCE; AT THE END |
| 2. Exactly the bytes of the committed message files; stop on any checksum difference | `check_messages`, `check_tree_is_committed`, `check_go` (the `messages_sha256` line), `check_request` | START CHECKS; ANTHROPIC, an ordinary run; REFUSALS; S8 |
| 3. A ceiling for each run, equal to the figure in John's go | `check_go`; class `Run` is frozen | START CHECKS; S2; THE CEILING |
| 4. Cost of every reply from the reported counts, a running total, stop before a call that could pass the ceiling | `Engine.make_record` (the cost), `Engine.spent`, `most_a_call_could_cost`, `check_ceiling`, `check_prices`; `Engine.write_marker` and `read_folder` for a call with no record | ANTHROPIC, an ordinary run; THE CEILING; every M2 case |
| 5. After the first round, stop if five rounds would pass the ceiling | `Engine.check_projection` | RULE 5 |
| 6. Refuse after the last safe day; the day itself is allowed | `check_day` (before the run, and before every call on the same clock reading the call is recorded with), `check_last_safe_days` | START CHECKS; ROW 1, continued; S8 |
| 7. Stop a model's run if the reported name is not the one sent | `classify`, `Engine.fill_slot`, `Engine.run_model` | THE TWO THINGS THAT COME FIRST; ROW 7 |
| 8. Write each file before the next message, read-only; the list of names and checksums at the end | `Engine.save`, `Engine.write`, `Engine.write_new_file`, `HoldInterrupts`, `write_manifest` | ANTHROPIC, an ordinary run; M2, rows 3 and 5; THE SOURCE |
| 9. The named interface for each developer, streaming for Anthropic, OpenAI's `store` false | classes `Anthropic`, `Google`, `OpenAI`; `check_request` | the three ordinary runs; REFUSALS; S8 |
| 10. After each round, flag faulty files by name and fault only | `fault_lines`, `Engine.say_faults` | FAULT FLAGS; ROW 8; M2, row 4 |
| 11. A rehearsal that calls no service, run and shown to pass first | `rehearsal.py`; `check_rehearsal_passed` | TRIPWIRE; every case; START CHECKS |

| The method's refusal | Enforced in | Rehearsal case |
|---|---|---|
| Add any instruction or second message | `check_request`, the `allowed` method of each developer's class, the list `NEVER_SENT` | REFUSALS (six cases); S8 (the engine itself) |
| Send any earlier exchange's id or text | the same | REFUSALS (four cases) |
| Reword or retry a reply because of what it says | `classify` decides only from what the service reports; `Engine.next_step`; no guard stops a run for a reply's wording | ROW 6; ROW 8; M2, row 4 |
| Ask for a model's hidden reasoning | `check_request`, `NEVER_SENT` | REFUSALS (four cases) |
| Print, summarise or pass on any reply | class `Sealed`, `say`, `holds_reply_words`; there is no code that sends a reply anywhere | REFUSALS (print); AT THE END |
| Write a reply inside a git repository | `inside_a_git_repository`, in `start_checks`, `Engine.__init__` and `Engine.write_new_file`; `Engine.__init__` also fixes the folder to the one John ruled | REFUSALS (where a reply may be written); S8 |
| Write words from a reply into a file name, a log or the manifest | `file_name` and `write_manifest` build names from the plan and numbers only, checked against a fixed form; `say` withholds a line that shares five words with a reply | REFUSALS; FAULT FLAGS; M2, row 4; AT THE END |
| Delete a file | no such call exists; files are created new and read-only | THE SOURCE; ANTHROPIC, an ordinary run |
| Raise its own ceiling | class `Run` is frozen; `check_go` | THE CEILING; START CHECKS |

The failures table is `classify` (which row) and `Engine.next_step` (what is done). Each row has
a rehearsal case named for it: ROW 1 to ROW 8, the two cases under WHICH ROW, WHEN A STREAM
BREAKS, and the two under THE TWO THINGS THAT COME FIRST.

## What changed after the check

**M1, four failed tries shut the model out for the day.** Proposal 3 above. Rehearsal cases
headed M1: the check's own test (a wrong key, then the same command later the same day, which
now asks all 50); five such stops in one day; each of the five statuses; the four kinds that
keep the three tries; the switch turned off; and the other two developers.

**M2, a reply that has arrived can be lost before it is saved, and its cost is not counted.**
Three layers, in `Engine.ask`:

1. *A guard.* Once the service has answered, whatever goes wrong in taking the reply apart,
   a record is still written with everything the service returned, and the call is counted at
   the most it could cost. If only the cost cannot be worked out, the reply is saved as usual
   and counted at the most.
2. *A marker.* A small file is written before each call. A call with no attempt file beside
   its marker is counted at the most it could cost on the next start, and its number is never
   reused. If the marker cannot be written, nothing is sent.
3. *Tries at the write.* Five quick tries, then a plain statement on screen that a reply is
   held and unsaved, then a try every half minute for half an hour, each under a new name so a
   half-written file cannot block the next. Ctrl-C waits while a reply is in hand, and the
   network code hands back what had arrived if Ctrl-C comes while a reply is on its way.

On none of these paths does reply text reach the screen, a log, a file name or the
repository: the new lines print a file name, a fixed phrase and the kind of error, never the
error's own message. Rehearsal cases headed M2 run each row of the check's table of five ways
a reply was lost.

| Should-fix | What was done |
|---|---|
| S1. A half-written file stops every later run | Fixed. `read_folder` names it in a notice, counts it at the most its call could cost, treats its number as used, and the run carries on. Case S1 |
| S2. John's go can be matched to words about something else | Fixed as far as code can: the quotation must sit directly above its block; the words must name the developer and carry one figure only; "$50" no longer matches "up to $5"; the block gains `date` and `commit`; the spending record and the two documents the plan is checked against must be committed. A go John later withdrew cannot be detected by code and is listed above. Case S2 |
| S3. No way to make one real call and stop | Fixed: `--stop-after N`, and the `labels` command. Case S3 |
| S4. Guards against reply words can stop a run because of what a reply says | Fixed. Nothing raises on a reply's wording any more. Names are built from the plan and numbers; the print function withholds a line and goes on. Case M2, row 4 |
| S5. Two or three broken streams in round one end the run at a $5 ceiling | Kept, as the check advised; it is the strict reading. Listed under "What the ceiling means in practice" with the check's sums, and `caffeinate` is in the commands |
| S6. The key is in the environment while git runs | Fixed. `read_key` is the first act of a run. THE SOURCE checks the order |
| S7. Two runs at once are not prevented | Fixed: `Engine.only_one_run`, a hold on a file in the reply folder that the system releases when the program ends. Case S7 |
| S8. The rehearsal misses seven of sixteen deliberate changes | Fixed. Cases added for each of the seven, and the key test corrected. See "The rehearsal, tested against broken copies" |
| S9. The capture documents still say no script exists | Not mine to edit. The wording is listed in the hand-over note for the planning session |

## Where the script reads the method strictly, and where loosely

Each is a place where the method could be read more than one way. Each is for John or the
checking session to confirm or change.

*Departing from the method's words, needing a dated correction:*

1. **The key comes from the environment, not from a file the script opens.** Rule 1 says
   "Read each key from its own file outside the repository". The key still lives in its own
   file outside the repository; the script is handed it by the shell.
2. **Proposal 3,** above.

*The stricter reading:*

3. **A ceiling for each run, not each developer,** matching the steps document.
4. **A call whose cost the service did not report is counted at the most it could cost.**
5. **At most one further asking for a slot, whatever the second brings.**
6. **A slot left for the next day stops that model's run for the day.** With proposal 3 this
   now happens only after four timeouts, rate limits or the like.
7. **A model that once reported a different name stays stopped** until John rules.
8. **A complete reply that names no model is treated as the wrong-model row.**
9. **Words OpenAI's service files under "refusal" are kept as the reply.**
10. **A Google call is counted, before it is made, at the model's own maximum.**

*A judgment, neither stricter nor looser:*

11. **Anthropic's stop reason `refusal` is recorded as "blocked by the service",** so such a
    reply is asked once more. Anthropic's page says "Safety classifiers return this stop
    reason". The stop reason itself is saved as given.
12. **Two stop reasons are treated as the length limit:** Anthropic's
    `model_context_window_exceeded` and Google's `CONTINUATION`. Google's `OTHER` and its tool
    and image reasons are treated as an ordinary reply. OpenAI's `max_messages` and `steered`
    are treated as no completion signal.
13. **The "program library" saved in each record is "none".**

*The looser reading, or something the method does not name:*

14. **A request the service answers with an error status is counted as costing nothing.**
    Google's billing page says so for its 400 and 500 errors (read by the checking session).
    Anthropic's pages say nothing either way; if it did bill one, it could bill only the
    message sent, about a fifth of a cent.
15. **"Empty" means no characters other than spaces and line ends,** slightly wider than
    "holds no text".
16. **One header the method does not name is sent:** `user-agent: Python-http.client/3.14.5`.
    Python's library would send none. It names no project and no person. Whether the service's
    front door minds it, or would mind its absence, is unknown until a real call.
17. **Two waits are set on this machine and nothing is sent for them:** 300 seconds between
    pieces of an Anthropic stream, and 45 minutes for a whole exchange. Both are saved in each
    record.
18. **The day's tries start again at midnight Pacific.** A question that fails across midnight
    can get more than four tries in a row.
19. **Rule 5 looks only at models already asked.** For a run with several models the
    projection adds what the others have cost so far, and nothing for models not yet started.
    The check before every call still holds. Not relevant to Anthropic's one model.

## Not checked against a page opened by this session

Pages were opened on 2026-11-18. Reading a documentation page asks no model anything.

| Fact, as used | Status | What to open to check |
|---|---|---|
| Anthropic: address, the three headers, `"stream": true`, the event names, the `error` event, `message_stop` as the final event, the stop reasons, 64,000 maximum, $3 and $15, the five statuses of proposal 3 | Checked, and confirmed again by the checking session | streaming, handling-stop-reasons, versioning, errors and models overview pages on platform.claude.com |
| Anthropic: that the service reports `claude-sonnet-4-5-20250929`, exactly, in `message_start` | **Not checked** | Only a real reply shows it. If it differs, the run stops after one call |
| Google: the path, the reply's field names, every finish reason and block reason, the token counts, 65,536 maximum, the prices | Checked | aistudio.google.com/api-reference/generate-content, the two model pages, the pricing page |
| Google: the request's field names (`contents`, `parts`, `text`) | **Not checked.** The checking session confirmed `maxOutputTokens` and the two roles; the rest is from memory | The "Request body" section of the reference page |
| Google: the host and the `x-goog-api-key` header for this interface; what `modelVersion` holds; whether thinking counts inside the limit; which error statuses apply to this interface | **Not checked** | The reference page; only a real reply shows the model name |
| OpenAI: address, `Authorization: Bearer` header, field names, the states and reasons, the two error statuses of proposal 3 | Checked against OpenAI's guides and its own Python library | |
| OpenAI: a plain-text `input` is one user message | Confirmed by the checking session on OpenAI's reference page, not by this one | |
| OpenAI: each model's maximum and price; what `model` holds in the reply | Checked by this session; not reopened by the checking session. The reported name is **not checked** | Each model's page; only a real reply shows the name |

## What is finished for each developer

- **Anthropic: complete,** with both must-fix findings answered, waiting for the second check.
- **Google and OpenAI: built and rehearsed, and not ready,** as the check says. The same fixes
  apply to them because they share the engine. Left otherwise as they were. Google's request
  field names and every reported model name are unconfirmed, and OpenAI is not needed until
  2026-12-09.

## The rehearsal, tested against broken copies

The check made changed copies of the script and found the first rehearsal missed seven. After
adding cases, this session made twelve changed copies in a temporary folder (the check's
seven, and five that undo the new fixes) and ran the rehearsal against each. All twelve were
caught:

| Change made to a copy of the script | Caught? |
|---|---|
| The day check before every call is removed | Yes |
| The engine no longer calls the last check before sending | Yes |
| The key falls back to `ANTHROPIC_API_KEY` | Yes |
| The length limit is looked at before the wrong model | Yes |
| The repository check in the writing code is removed | Yes |
| The running total leaves out wrong-model files | Yes |
| The first word of each reply is printed | Yes |
| A wrong key uses up one of the day's tries | Yes |
| No marker is written before a call | Yes |
| The guard round taking a reply apart is removed | Yes |
| The write is tried once only | Yes |
| The go's words are looked for in every quotation in the record | Yes |
