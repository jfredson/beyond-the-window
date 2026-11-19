# The sealed capture script

Written 2026-11-18 by Claude (Fable 5.2), an AI model, from the specification in
`docs/capture/method.md` ("What the script must do, and must refuse to do"), which John approved
on 2026-11-18. John said the same day: "Yes, start the capture script now". A different session
checks this work.

**Nothing has been run against any service.** No model has been asked anything, no key has been
handled, and nothing has been spent. The first real call will also be the first time this code
meets a real service, so the first run should be watched.

## What is here

| File | What it is |
|---|---|
| `capture.py` | The script. Python's standard library only, so every line that touches the network is in this one file (class `HttpsTransport`). Needs Python 3.11 or later; written and rehearsed on 3.14.5. |
| `plan.toml` | The data the script reads and cannot change: the models, each last safe day, each ceiling, each price, and the threshold for a "very short" reply. |
| `rehearsal.py` | The rehearsal the method requires (script rule 11). It calls no service. |
| `rehearsal-result.txt` | The saved output of the rehearsal, committed separately. The script refuses a real run unless this file ends with a pass for the script and plan exactly as they stand. |

It lives in `capture/` and not under `docs/capture/` because it is a program and not a document,
and because the method's refusal to write replies "inside a folder that is part of a git
repository" is easier to check when the program and its documents are apart.

## The commands

Each is run from the repository's top folder. `-I` tells Python to load nothing from the
current folder.

```bash
python3 -I capture/capture.py show --run anthropic-2026-11-30
```

Prints exactly what a run would send, to which model, how many times and at what estimated
cost, lists every check a real run makes and whether it passes now, and stops. It sends
nothing and needs no key. `--all-bodies` prints all ten requests.

```bash
python3 -I capture/capture.py run --run anthropic-2026-11-30
```

The real run. It refuses unless every check passes. The key must be in the environment
variable named in the plan for that run (see "The key" below). Stopped part way, the same
command carries on from the files already written.

```bash
python3 -I capture/rehearsal.py > capture/rehearsal-result.txt
```

The rehearsal. Run again, and its result committed, after any change to `capture.py` or
`plan.toml`.

The other commands: `faults` (the fault list for everything on file), `manifest` (write the
list of names and checksums again), `check-manifest` (compare the reply folder with the
committed list), and `record-not-made --run ...` (after a last safe day, record each asking
that was never completed as not made).

The four runs in the plan are `anthropic-2026-11-30`, `google-2026-12-01`, `openai-2026-12-11`
and `openai-2027-01-14`, each named for its developer and withdrawal date.

## What has to exist before a real run

1. **The script, the plan and the ten message files committed, with no changes since.**
2. **The rehearsal result committed,** for that exact script and plan.
3. **John's go in `docs/spending-record.md`.** That file does not exist yet. For each run it
   must hold John's words as a quotation and one block in this form, which the session that
   records his go writes:

   ````markdown
   > Go for the sealed capture as written in `docs/capture/` at commit abc1234. Anthropic, up to $5.

   ```sealed-capture-go
   run = "anthropic-2026-11-30"
   ceiling_usd = "5.00"
   johns_words = "Anthropic, up to $5"
   messages_sha256 = "the SHA-256 checksum of docs/capture/sent/SHA256SUMS"
   ```
   ````

   The script checks that `ceiling_usd` equals the plan's ceiling, that `johns_words` appears
   word for word inside the quotation and carries that dollar figure, and that
   `messages_sha256` is the checksum of the list of message checksums as it stands. The last
   ties his go to the exact messages he approved. If John's figure differs from the plan's, a
   session changes the plan in a commit and runs the rehearsal again; the script never does.
4. **The key in the environment**, under the name in the plan.
5. **John's approval of the proposed threshold** below.

## The key

The script reads the key from one environment variable and nowhere else:
`BTW_CAPTURE_ANTHROPIC_API_KEY`, `BTW_CAPTURE_GOOGLE_API_KEY` or `BTW_CAPTURE_OPENAI_API_KEY`.
It never opens a credentials file. The names are this project's own on purpose: a key another
project left in the shell under a common name such as `ANTHROPIC_API_KEY` is not picked up, which
is how the rule "never use another project's key" is enforced in code. The variable is removed
from the program's environment as soon as it is read. The key is held in an object that prints
as a fixed phrase, is turned back into text in one place only (the request header), and is taken
out of any record before it is written, should a service ever send it back.

## Where each rule is enforced, and which rehearsal case proves it

Names in the middle column are functions or classes in `capture.py`. Names in the last column
are the headings the rehearsal prints.

| The method's rule | Enforced in | Rehearsal case |
|---|---|---|
| 1. Key from its own place outside the repository, never printed, never another project's | `read_key`, class `Secret`, `say`, `Engine.write` | THE KEY; THE KEY, again; AT THE END |
| 2. Exactly the bytes of the committed message files; stop on any checksum difference | `check_messages`, `check_tree_is_committed`, `check_go` (the `messages_sha256` line), `check_request` | START CHECKS; ANTHROPIC, an ordinary run; REFUSALS (a reworded message, a message not among the ten) |
| 3. A ceiling for each developer, equal to the figure in John's go | `check_go`; class `Run` is frozen | START CHECKS (nine refusals); THE CEILING |
| 4. Cost of every reply from the reported counts, a running total, stop before a call that could pass the ceiling, counting the call at its limit and a repeat at the model's maximum | `Engine.ask` (the cost), `Engine.spent`, `Engine.most_a_call_could_cost`, `Engine.check_ceiling`, `check_prices` | ANTHROPIC, an ordinary run; THE CEILING; WHICH ROW, no text arrived (a call with no counts is counted at the most it could cost) |
| 5. After the first round, stop if five rounds would pass the ceiling | `Engine.check_projection` | RULE 5 |
| 6. Refuse after the last safe day; the day itself is allowed | `check_day` (before the run and before every call), `check_last_safe_days` | START CHECKS; ROW 1, continued |
| 7. Stop a model's run if the reported name is not the one sent | `classify`, `Engine.fill_slot`, `Engine.run_model` | THE TWO THINGS THAT COME FIRST; ROW 7; GOOGLE and OPENAI, the failures table |
| 8. Write each file before the next message, read-only; the list of names and checksums at the end | `Engine.write`, `write_manifest` | ANTHROPIC, an ordinary run; THE SOURCE |
| 9. The named interface for each developer, streaming for Anthropic, OpenAI's `store` false | classes `Anthropic`, `Google`, `OpenAI`; `check_request` | the three ordinary runs; REFUSALS |
| 10. After each round, flag faulty files by name and fault only | `fault_lines`, `Engine.say_faults` | FAULT FLAGS; ROW 8 |
| 11. A rehearsal that calls no service, run and shown to pass first | `rehearsal.py`; `check_rehearsal_passed` | TRIPWIRE; every case; START CHECKS |

| The method's refusal | Enforced in | Rehearsal case |
|---|---|---|
| Add any instruction or second message | `check_request`, the `allowed` method of each developer's class, the list `NEVER_SENT` | REFUSALS (six cases) |
| Send any earlier exchange's id or text | the same | REFUSALS (four cases) |
| Reword or retry a reply because of what it says | `classify` decides only from what the service reports; `Engine.next_step` allows one further asking and only for a cut-off, empty or blocked reply | ROW 6 (byte for byte the same); ROW 8 |
| Ask for a model's hidden reasoning | `check_request`, `NEVER_SENT` | REFUSALS (four cases) |
| Print, summarise or pass on any reply | class `Sealed`, `say`, `holds_reply_words`; there is no code that sends a reply anywhere | REFUSALS (print); AT THE END |
| Write a reply inside a git repository | `inside_a_git_repository`, in `start_checks`, `Engine.__init__` and `Engine.write`; `Engine.__init__` also fixes the folder to the one John ruled | REFUSALS (where a reply may be written) |
| Write words from a reply into a file name, a log or the manifest | `file_name`, `no_reply_words`, `fault_lines`, `write_manifest` | REFUSALS; FAULT FLAGS; AT THE END |
| Delete a file | no such call exists; files are created new and read-only | THE SOURCE; ANTHROPIC, an ordinary run |
| Raise its own ceiling | class `Run` is frozen; `check_go` | THE CEILING; START CHECKS |

The failures table is `classify` (which row) and `Engine.next_step` (what is done). Each row has
a rehearsal case named for it: ROW 1 to ROW 8, the two cases under WHICH ROW, WHEN A STREAM
BREAKS, and the two under THE TWO THINGS THAT COME FIRST.

## PROPOSED 2026-11-18, for John

Neither is approved. Each has the four things the project asks for.

**1. "Very short" means fewer than 20 words.** *The choice:* a reply of 19 words or fewer is
listed after its round as very short, kept, and never asked again. Words are counted as runs
of characters between spaces. *Confidence:* moderate. *Judgment call.* The reason: an ordinary
full sentence is fifteen to twenty words, so a reply under twenty is at most about one
sentence. A whole answer of that length is possible, and so is a fault, and it is the length
at which John would want to know the file is there. Replies to these questions are expected to
run to hundreds of words, so the list should stay short enough to read. Since a flag costs
nothing and changes nothing, erring high is cheap. *Strongest alternative:* 5 words, which
lists only fragments and bare refusals, and would miss a one-line reply that is cut short
without the service saying so.

**2. After a reply cut off without the service's signal that it was complete, the one further
asking uses the same length limit, not the model's maximum.** The method leaves this to the
script. *Confidence:* high. *Judgment call.* A broken stream is not a sign that the limit was
too low, and the maximum would cost more for nothing. *Strongest alternative:* the maximum, as
for a reply stopped at the length limit, which treats both kinds of cut-off alike.

## Where the script takes the stricter reading

Each of these is a place where the method could be read two ways. The stricter one is built,
and each is for John or the checking session to confirm or change.

1. **The key comes from the environment, not from a file the script opens.** Rule 1 says
   "Read each key from its own file outside the repository". The script never opens a
   credentials file; the key reaches it through a variable set from that file by John's shell.
   The key still lives in its own file outside the repository, which is the rule's purpose.
2. **A ceiling for each run, not each developer.** Rule 3 says "for each developer";
   `what-john-needs-to-do.md` gives OpenAI two ceilings, one for each withdrawal date. The
   script has four runs and four ceilings.
3. **A call whose cost the service did not report is counted at the most it could cost.** A
   stream that breaks before the service sends its final counts is counted at the full length
   limit ($0.48 for Claude Sonnet 4.5). The consequence: three such breaks in the first round
   make rule 5 stop the run at a $5 ceiling, although the true cost is far lower.
4. **A request the service answers with an error status is counted as costing nothing.** This
   is an assumption, not checked against any developer's billing page.
5. **At most one further asking for a slot, whatever the second brings.** If an empty reply is
   asked again and the second is cut off at the length limit, both are kept and it is left; the
   script does not chain a third.
6. **A slot left for the next day stops that model's run for the day.** The method says a
   round finishes before the next starts, so the script does not go on to later questions.
7. **A model that once reported a different name stays stopped** on every later run, until
   John rules. Nothing in the script clears it.
8. **A complete reply that names no model is treated as the wrong-model row.**
9. **Anthropic's stop reason `refusal` is recorded under the row "The service blocked the
   message or the reply".** Anthropic's page says "Safety classifiers return this stop reason".
   The stop reason itself is saved as given.
10. **Words OpenAI's service files under "refusal" are kept as the reply.** Treating them as no
    reply would ask again because of what was said.
11. **"Empty" means no characters other than spaces and line ends.**
12. **A Google call is counted, before it is made, at the model's own maximum,** until it is
    checked whether the 2.5 models count their thinking inside the length limit sent.
13. **The "program library" saved in each record is "none".** The script uses no developer's
    library, only Python's standard library, and says so.

## Not checked against a page opened in this session

Pages were opened on 2026-11-18. Reading a documentation page asks no model anything.

| Fact, as used | Status | What to open to check |
|---|---|---|
| Anthropic: address, the three headers, `"stream": true`, the event names, the `error` event, `message_stop` as the final event, the stop reasons, 64,000 maximum, $3 and $15 | Checked | streaming, handling-stop-reasons, versioning, errors and models overview pages on platform.claude.com |
| Anthropic: that the service reports `claude-sonnet-4-5-20250929`, exactly, in `message_start` | **Not checked** | Only a real reply shows it. If it differs, the run stops after one call |
| Google: the path, the reply's field names, every finish reason and block reason, the token counts, 65,536 maximum, the prices | Checked | aistudio.google.com/api-reference/generate-content, the two model pages, the pricing page |
| Google: the host and the `x-goog-api-key` header | Checked for the same service's newer interface, not for `generateContent` itself | An example on the API reference page, which was cut off |
| Google: the request's field names (`contents`, `role`, `parts`, `text`, `generationConfig.maxOutputTokens`) | **Not checked**, written from memory | The "Request body" section of the reference page |
| Google: what `modelVersion` holds for each 2.5 model | **Not checked** | Only a real reply shows it |
| Google: whether thinking counts inside `maxOutputTokens` for the 2.5 models | **Not checked** | The thinking page now describes the newer interface |
| Google: the shape of an error body | Partly. The script prints only the status and one label | aistudio.google.com/docs/api-errors |
| OpenAI: address and `Authorization: Bearer` header | Checked | The example on the reasoning guide |
| OpenAI: request and reply field names, the states, the reasons a reply is incomplete, the two kinds of content part | Checked against OpenAI's Python library on GitHub, not the reference page | "Create a model response" in the reference, too long to read in full |
| OpenAI: each model's maximum and price | Checked | Each model's page on developers.openai.com |
| OpenAI: that a plain-text `input` reaches the model as one user message with nothing added | **Not checked** | The same reference page |
| OpenAI: what `model` holds in the reply when a dated name is sent | **Not checked** | Only a real reply shows it |
| OpenAI: with `store` false, the reply carries the model's reasoning in an encrypted form without being asked | Read on the reasoning guide. The script does not ask for it, read it or use it; it is in the saved raw reply | The reasoning guide |
| All three: that a request answered with an error status is not charged | **Not checked** | Each developer's billing page |

## What is finished for each developer

- **Anthropic: complete,** and rehearsed on every row of the failures table and every case
  rule 11 lists.
- **Google: complete,** and rehearsed on its own rows. Two facts above could stop it on the
  first call: the request's field names and the reported model name. And the method already
  says Google will very likely refuse a new project.
- **OpenAI: complete,** and rehearsed on its own rows, for both of its dates. It is the least
  checked of the three and is not needed until 2026-12-09.
