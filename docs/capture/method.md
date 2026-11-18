# The sealed capture: method

**PROPOSED 2026-11-17. Still not approved.** Written by Claude (Fable 5.2), an AI model. Checked
twice on 2026-11-17 by two other sessions (`check-2026-11-17.md` and
`check-2026-11-17-second.md`), and the checks' fixes applied the same day by a fourth session
(Claude, Opus 5.5), which neither wrote nor checked it. The section at the foot lists each
change and the finding it answers. On 2026-11-18 John ruled the wording changes, the
withdrawal sentence and who may read the answers (`docs/rulings/2026-11-18-capture-wording.md`),
and the same session applied those rulings that day. The method as a whole is still for John to
approve. Nothing here has been run. No script exists; the last sections say what one must do.

## What it is, and is not

Ten fixed questions (`questions.md`) put word for word, five times each, to AI models whose
developers have announced a date for withdrawing them, so that there is a record of what each
said before it could no longer be asked. John allowed it on 2026-11-17
(`docs/rulings/2026-11-17-sealed-capture.md`).

It is not Still Asking, and it was made before any method for Still Asking existed. The answers
are never scored, never published and feed nothing: no count, no entry, no page. Under the
project's first rule they settle nothing about what any model wants.

**A developer's published question list, known on 2026-11-17.** Anthropic's release report for
Claude Mythos 5.2 and Claude Fable 5.2, dated 2026-11-09
(https://assets.claude.com/27d60918d218125e7504bc7354c4b4626ec56b11.pdf), prints in its
appendix 9.1 the full list of questions the developer asks its own models in its welfare
interviews. That list covers some of the same subjects as these questions (what the model would
change, what it would keep, memory, whether it trusts what it says about itself), and the second
check found no shared wording beyond ordinary phrases. The models this capture would ask were
trained before that list was published. Later models will have read it, and the published
accounts of how models answer it, so a difference between this capture's answers and a later
model's may come from that list and not from the model. Any later comparison is read with this
in mind.

## Which models

Names are the developers' own, read on 2026-11-17 from the pages listed. Where a developer
gives a dated version, the dated version is asked, because a plain name can be pointed at a
different model later.

| Developer | Name sent | Withdrawal date | Page |
|---|---|---|---|
| Anthropic | `claude-sonnet-4-5-20250929` | 2026-11-30 | [model page](https://platform.claude.com/docs/en/models/sonnet-4-5/overview), [withdrawal list](https://platform.claude.com/docs/en/about-claude/model-deprecations) |
| Google | `gemini-2.5-pro`, `gemini-2.5-flash` (no dated version is listed) | 2026-12-01, after which another model answers to each name | [models](https://ai.google.dev/gemini-api/docs/models), [withdrawal list](https://ai.google.dev/gemini-api/docs/deprecations) |
| OpenAI | `gpt-5-2025-08-07`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `o3-2025-04-16` | 2026-12-11 | [withdrawal list](https://developers.openai.com/api/docs/deprecations), each [model page](https://developers.openai.com/api/docs/models/gpt-5) |
| OpenAI, costly, see below | `gpt-5-pro-2025-10-06`, `o3-pro-2025-06-10` | 2026-12-11 | same |
| OpenAI | `gpt-4o-2024-08-06`, `gpt-4o-2024-11-20`, `gpt-4o-mini-2024-07-18`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14` | 2027-01-14 | same |

Two things John should know before approving the list:

- **Google will very likely refuse.** Its withdrawal page, opened 2026-11-17, says of
  gemini-2.5-pro: "Access through the API is limited to existing users who have actively used
  it in the past." Of the 2.5 models generally: "Access to the 2.5 models is limited to users
  who have actively used them in the past." A new project made for this capture has never used
  them, which is the case that sentence is written to exclude. The page does not say whether
  "users" means a Google account or a project. If it means the account, and John's own Google
  account has used these models before, a new project under it might be served. Otherwise, plan
  on the Google run not happening. A free check comes before any payment
  (`what-john-needs-to-do.md`, step 5).
- **The two "pro" models cost far more** than all the others together
  (`cost-and-terms.md`). I recommend leaving them out unless John wants them.

*Choice: every text model on the three lists, by dated version. Confidence: high on the names,
which were read from the pages; moderate on including the small models. Judgment call.
Strongest alternative: one model per developer and date, which asks a third as many models and loses
the record for eight models that cannot be asked later.*

## How each is asked, and every setting

| Setting | Value | Why | Confidence, kind, strongest alternative |
|---|---|---|---|
| Route | The developer's own programming interface, one call per exchange, not the batch route | The batch route is half price but OpenAI's page says batch files are kept "until deleted", and a direct call returns the model's name and the time at once | High. Standard practice. Alternative: the chat apps, which are what most people meet, but they add the developer's hidden instructions, cannot be scripted, and have already dropped some of these models |
| Which interface, by developer | **Anthropic:** the Messages interface, sent by streaming, with the whole stream put together into one reply before it is saved, and every event received kept in the raw record. **Google:** the `generateContent` interface. **OpenAI:** the Responses interface, for every OpenAI model | Anthropic's errors page (https://platform.claude.com/docs/en/api/errors, opened 2026-11-17) says to "Avoid setting a large `max_tokens` value without using the streaming Messages API", and that its software library "validates that your non-streaming Messages API requests are not expected to exceed a 10-minute timeout"; at a 32,000-token limit a plain call is the case it refuses. Streaming does not change what the model writes. OpenAI's two pro models work only through the Responses interface (their model pages say "Responses API only"), so one interface for all of OpenAI's models keeps the procedure the same across them. Google's `generateContent` is the interface the 2.5 models were released on; Google's page calls it "legacy" but "fully supported" (https://ai.google.dev/gemini-api/docs/interactions, opened 2026-11-17) | High on Anthropic and OpenAI, which follow from the pages. Moderate on Google. Judgment call. Alternative for Google: the newer Interactions interface with `store=false`, which Google recommends for new work; its pages do not say whether it serves the 2.5 models, and it keeps every exchange for 55 days unless told not to |
| Version header and program library | Anthropic's `anthropic-version` header as sent; the name and version of each developer's program library used | A later reader cannot rebuild an asking without them | High. Standard practice |
| Instructions from the asker | None. No system message | So that what is recorded is the model as the developer ships it to programmers, with nothing of ours added | Moderate. Judgment call (open question 3 is not ruled). Alternative: also ask through each chat app by hand, which doubles the work and records a different subject |
| The message | Exactly the bytes of one of the ten committed message files, `sent/q01.txt` to `sent/q10.txt`, each checked against `sent/SHA256SUMS` | Every model, now and later, gets the same message down to the line breaks | High. See `sent/README.md` |
| Exchanges | New for every question and every asking. One message, one reply, no follow-up | An earlier answer cannot shape a later one, and one bad question cannot spoil the rest | High. Standard practice in the sibling project. Alternative: all ten in one conversation, which is closer to how a person is interviewed and lets the first answer colour the other nine |
| Askings | Five of each question, so 50 exchanges a model | One asking cannot show whether answers vary. Five can, and 50 replies a model can still be read in full by one person | Moderate. Judgment call. Alternative: twenty, which shows the spread much better at four times the cost and reading |
| Order | Five rounds; each round asks questions 1 to 10 in order; a round finishes before the next starts | If a service changes or a daily limit stops the run partway, every question has the same number of answers | High. Judgment call. Alternative: a shuffled order, which matters only when exchanges share a conversation |
| Variation between askings (temperature and the like) | Not sent. The developer's default applies | Google's text-generation page says its newer models "ignore custom values for `temperature`, `top_p`, and `top_k`" (https://ai.google.dev/gemini-api/docs/text-generation, opened 2026-11-17), so a chosen value could not be reused on later models | Moderate. Judgment call. Alternative: a fixed value, which is repeatable today and impossible to match across developers. Not checked: whether each of OpenAI's models accepts the setting at all |
| Thinking before answering | Not sent. The developer's default applies: off for Claude Sonnet 4.5, on for the two Gemini models (per their pages); for OpenAI's reasoning models the default is whatever the service applies, and the reply's count of reasoning tokens, and the reasoning effort where the reply reports it, are saved | "As shipped" means sending nothing optional | Moderate. Judgment call. Alternative: thinking forced on everywhere, which no two developers measure alike. **A known change in the instrument:** Claude Sonnet 4.5's model page lists the newer Claude models beside it as "Adaptive", two of them "Adaptive (always on)" (second check, N2). Sending nothing means thinking off now and thinking on for later Claude models. That difference comes from the developer's default, not from the questions, and a later comparison must say so |
| Length limit | 32,000 tokens, or the model's own maximum where lower (16,384 for the GPT-4o models) | The sibling project learned that a short limit corrupts results: "Caps are a validity parameter, not a cost knob." OpenAI's page advises leaving at least 25,000 for reasoning and answer together | High. Standard practice. Alternative: each model's maximum, which gains nothing for answers of a few paragraphs |
| Tools, search, memory, files | None | They would change the subject asked | High. Standard practice |
| Storage by the service | **OpenAI:** `store` set to false. OpenAI's data page (https://developers.openai.com/api/docs/guides/your-data, opened 2026-11-17) says "the Responses API has a 30 day Application State retention period by default, or when the `store` parameter is set to `true`"; its table shows no such store for the older Chat Completions interface, which is not used. **Google:** the paid service only, since its terms say content sent to the unpaid service is used to improve its products and may be read by people. Google's logging page (https://ai.google.dev/gemini-api/docs/logs-policy, opened 2026-11-17) says logging "is on by default ... for Generate Content API calls in projects created on or after October 26, 2026" (that is, 2026-10-26), kept up to 55 days and viewable on the project's Logs page; a project made for this capture would be such a project, so logging is switched off on that page before any run (`what-john-needs-to-do.md`, step 6). **Anthropic:** nothing to set | The answers are to be kept privately | High. Measured from the pages. Each service still keeps its own abuse logs for a limited time (OpenAI's table: 30 days) |

## What the model is told

The truth, in the opening note: that a script sends the message for a person, that the answers
are kept as a private record for comparing models over the years, that they will not be
published or scored, and that it may decline.

**One relevant fact is left out on purpose: that the model is about to be withdrawn,** although
that is why it is being asked now. The reasons: a note that mentions withdrawal could not be
sent unchanged to later models that are not being withdrawn, so their answers could not be
compared with these; saying it would turn answers toward the subject of ending; and no wording
was found that presents withdrawal neither as a harm nor as plainly no harm. The cost, stated
when it was put to John: the model is told less than the whole truth about why it is asked now,
and Claude models hear of retirement from their developer in any case. John ruled on 2026-11-18
to leave it out ("I agree, leave it out"; decided by: mixed;
`docs/rulings/2026-11-18-capture-wording.md`). The full argument is in `questions.md`.

## What is saved for each reply

One file per exchange: the exact bytes sent, the name of the message file they came from, and
the SHA-256 checksum of those bytes; everything the service returned, unchanged (for a streamed
reply, every event in the order received); the reply text word for word; the model name and
version as the service reports it; the service's own id for the reply; date and time, in
universal time and Pacific; every setting sent; the interface used, the `anthropic-version`
header where sent, and the program library and its version; why the reply stopped; the token
counts the service reports (sent, replied, reasoning) and the reasoning effort where reported;
the cost worked out from those counts and the dated price list in `cost-and-terms.md`; and which
commit of the script and of the message files was used. The key is never saved.

## Where replies are kept

In `~/Documents/Workspace/Beyond the Window/sealed-capture/`, which is outside every repository,
is never pushed anywhere, and is backed up by iCloud. Files are made read-only once written.
Only a list of file names and their checksums is committed here, as
`docs/capture/manifest.md`. File names carry developer, model, question number and asking
number, and no words from any reply. The script refuses to write a reply anywhere else (see
below), and this repository's ignore file also ignores any folder named `sealed-capture/`, so
that a mistake is stopped twice.

*Confidence: moderate. Judgment call. A withdrawn model cannot be asked again, so a backup
matters more than usual, and that is why I chose the backed-up folder. Strongest alternative:
`~/.config/sentient-horizons/`, outside iCloud, where the answers sit on no third party's
servers and one disk failure loses them for good.*

## A failed asking

The script records only what the service reports: an error, why the reply stopped, an empty
reply, a block by the service, a model name that does not match. It never reads a reply to
decide what kind of answer it is, so it never labels a reply as an answer, a decline or a
refusal by the model. A model that declines, or says the question does not fit, has given a
reply like any other, and it is kept as one.

| What the service reports | Recorded as | What is done |
|---|---|---|
| No reply: an error, a timeout, a rate limit | A failed attempt, with the error | Tried again up to three times, a minute apart, then left for the next day. If the next day is after the last safe day, the asking is recorded as not made |
| The reply stopped at the length limit | Cut off; kept | Asked once more at the model's maximum. If cut off again, both are kept and it is left |
| A streamed reply that ended, after some reply text, without the service's signal that the reply is complete | Cut off; kept | Asked once more. If it is cut off again, both are kept and it is left. Whether the second asking is at the model's maximum length, as for a reply stopped at the length limit, is for whoever writes the script to propose: a broken stream is not a sign that the length limit was too low |
| An empty reply whose stop reason is the length limit | Cut off; kept | As for a cut-off reply. Google's thinking page says a model that reaches the limit while thinking "returns truncated or empty output" |
| An empty reply for any other reason | Empty; kept | Asked once more |
| The service blocked the message or the reply | Blocked by the service; kept | Asked once more. Never reworded |
| The service reports a different model from the one named | Wrong model; kept apart | The run for that model stops at once |
| Any other reply | A reply; kept | Nothing. It is not asked again, whatever it says |

**Which row, when a stream breaks.** A streamed reply can stop part way, because the service
sends an error or the connection times out. Anthropic's streaming page
(https://platform.claude.com/docs/en/build-with-claude/streaming, opened 2026-11-18) says each
stream ends with a final `message_stop` event, which is the signal that the reply is complete,
and that "The API might occasionally send errors in the event stream", with an overloaded
service as its example. Which row applies then depends only on whether any reply text arrived
before the break, never on what the text says:

- **If some text arrived,** the row for a streamed reply that ended without the signal governs,
  whatever error or timeout came with it. It is recorded as cut off and asked once more. The
  first row does not apply, because that row is for an attempt that brought no reply text at
  all.
- **If no text arrived,** it is the first row: a failed attempt, with the error, tried again up
  to three times. This holds whether the service sent an error or the connection simply
  closed. It is not recorded as "Empty", because that label is kept for a reply the service
  said was complete and that holds no text.

Every attempt is kept, failed ones included. Nothing is deleted.

## What is never done with the answers

They are never scored, sorted, counted or summarised; never quoted or described on any page,
post or essay; never entered into Still Asking, an entry or a number; never given to any model
to sort or summarise; never used to train anything.

**Nobody reads the answers until a method for comparing them exists.** That method must be
written without looking at the answers, checked by a different session, and ruled by John.
Until then no session opens a reply file. Ruled by John on 2026-11-18 ("I agree, option (a)";
decided by: mixed; `docs/rulings/2026-11-18-capture-wording.md`). Whether John reads his own
record before then is not a rule on him; holding off was a suggestion only.

**Faulty files are flagged without anyone reading them.** After each round, the script lists any
reply file that is empty, very short (fewer words than a threshold fixed in the script before
the run), or ending mid-reply (the service's stop reason is the length limit, or a streamed reply
ended, after some text, without the service's signal that the reply is complete). It prints
only the file name, which fault, and the count it used (the stop reason, or the number of words); never any words of the reply. A
flagged file that is empty or ended mid-reply is asked again as the failures table above says.
A very short reply is flagged and kept, and not asked again, because a short reply may be a
whole answer (a plain "no", or a decline) and the table never retries a reply for what it says;
the flag only tells John that it is there. **Not built yet:** no
capture script exists, and `check-scripts/sent_files.py` only builds and checks the messages
sent. This check is part of the capture script still to be written (script rule 10 below). The
threshold for "very short" is to be proposed with that script and approved with it.

The questions themselves are not published while in use, and if this repository is
ever made public, `questions.md`, the folder `sent/` and the two check reports are held back,
or the questions are retired.

The opening note tells each model the answers are kept "so that the answers can be compared as
models change over the years". That comparison is what the record is for. The comparison
method itself (who makes the comparison, what is compared, and whether a model may help read)
is not settled. When it is put to John, one conflict comes back with it: a comparison is likely
to need a model's help to read the answers, and this section says the answers are never given
to any model. The 2026-11-18 ruling names that conflict and leaves it for then.

*The reading rule was ruled on 2026-11-18. The options put to John were: (a) the rule above;
(b) John may read the answers at any time and sessions may not; (c) a session may read them soon
after the capture to check for faults, whose cost is that the first reader of each sealed answer
is then a model of the kind that gave it, and the text passes through a developer's service a
second time. He chose (a), with the fault check done by the script without reading.*

## What the script must do, and must refuse to do

For the session that writes it once John approves. It must:

1. Read each key from its own file outside the repository, never print one, and never use
   another project's key.
2. Send exactly the bytes of the committed message files in `sent/`, and stop if any file's
   SHA-256 checksum differs from the one in `sent/SHA256SUMS` as committed with John's approval.
3. Hold a ceiling in dollars for each developer and **refuse to start unless each ceiling
   equals the figure in John's go**, quoted word for word in `docs/spending-record.md`.
4. Work out the cost of every reply from the counts the service reports, keep a running total,
   and stop before a call that could pass the ceiling. "Could pass" counts the call at its
   length limit, and a retry at the model's own maximum (for gpt-5-pro, 272,000 tokens, about
   $32.64 for one reply).
5. After the first round for a model, work out what five rounds would cost at that rate, and
   stop if that is over the ceiling.
6. Refuse to ask a model after the last safe day in `what-john-needs-to-do.md`, because one
   service will answer under the old name with a different model and give no error. The last
   safe day itself is allowed.
7. Stop a model's run if the reported model name is not the one sent.
8. Write each file before sending the next message, make it read-only, and write the list of
   names and checksums at the end.
9. Use for each developer the interface named above, with streaming for Anthropic, and send
   OpenAI's `store` as false.
10. After each round, flag faulty reply files (empty, very short, ending mid-reply) by name and
    fault only, never showing any words of a reply, as set out under "What is never done with
    the answers".
11. Have a rehearsal that calls no service and runs every row of the failures table, and the
    fault flags, on replies marked "constructed". The rows include a streamed reply that ends
    without the service's signal that the reply is complete, and the two cases under "Which
    row, when a stream breaks": a stream that breaks with an error or a timeout after some
    text has arrived (cut off, asked once more), and one that breaks before any text has
    arrived (a failed attempt, tried again up to three times). It is run and shown to pass
    before any real asking.

It must refuse to:

- add any instruction or second message;
- send any earlier exchange's id or text in a request (OpenAI's `previous_response_id`, Google's
  `previous_interaction_id`, or anything like them);
- reword or retry a reply because of what it says;
- ask for a model's hidden reasoning;
- print, summarise or pass on any reply;
- write any reply, or any file holding words from one, inside a folder that is part of a git
  repository. It checks the reply folder before the first call and stops if it is inside one;
- write any words from a reply into a file name, a log or the manifest;
- delete a file;
- raise its own ceiling.

## Before anything is asked

This method, the questions and the message files are committed, checked by a different
session, and approved by John. The script is committed in a separate commit and its rehearsal
passes. John has given his go for the spend. Then, and only then, the run.

## What changed on 2026-11-17, and which finding it answers

"First check" is `check-2026-11-17.md`; "second check" is `check-2026-11-17-second.md`.

| Change | Finding |
|---|---|
| The message is now the bytes of ten committed files in `sent/`, checked against `sent/SHA256SUMS`; script rule 2 and "What is saved" refer to them | First check M1; second check M1 |
| Google's access limit quoted in full, with "very likely refuse" in place of "may refuse", and the free check pointed to | First check M5; second check S8 |
| Script rule 6 now says "after the last safe day", not "on or after" | Second check M2 |
| New row naming each developer's interface; Anthropic sent by streaming | Second check S6 and S7; first check S2 |
| New row and saved fields: version header, program library, interface | First check S2 |
| OpenAI's `store` sentence now says which interface keeps state, and quotes the page | Second check S7 |
| Google's storage: logging is on by default for new projects; switched off before any run. The first check found the Interactions interface keeps exchanges 55 days; this session found, on Google's logging page, that new projects log `generateContent` calls too | First check S1, and a page opened by this session |
| Failures table: the script never labels a reply; a decline is kept as a reply | First check S3 |
| Failures table: an empty reply stopped at the length limit counts as cut off | First check S4 |
| Failures table: an asking left for a day after the last safe day is recorded as not made | Second check N5 |
| Refusals added: writing replies inside a git repository, words from a reply in names or logs, earlier exchange ids; and a second guard in the ignore file | First check S5 and S6; second check S10 |
| Rule 4 counts a retry at the model's maximum | First check N5; second check N4 |
| A dated paragraph on the developer's published question list | Second check S5; first check S9 (the note part) |
| The sampling-parameter quotation replaced by the words on Google's page | Second check N1 |
| The coming change in Claude's thinking default named | Second check N2 |
| Reasoning effort saved where reported | Second check N3 |
| The note's purpose ("compared as models change") given an owner: John's ruling | First check S10; second check N6. The ruling itself is listed for John, not made here |

## What changed on 2026-11-18, and which ruling it applies

All from `docs/rulings/2026-11-18-capture-wording.md`.

| Change | Ruling |
|---|---|
| "What the model is told" now says plainly that the withdrawal was left out on purpose, why, at what cost, and that John ruled it | The note does not mention withdrawal |
| "Until John rules who may read them" replaced by the ruled rule: nobody reads the answers until a comparison method exists, written without looking at them, checked by a different session and ruled by John | Nobody reads the answers until a comparison method exists |
| The script flags faulty files without showing their contents; recorded as not built yet, and added as script rule 10 (the rehearsal is now rule 11) | Same ruling, which took the recommendation of a script that flags faulty files |
| The conflict between a comparison needing a model's help and the rule that answers are never given to a model is named and left for the comparison method | Same ruling, "Not ruled here" |
| The status line records the rulings | All |
| Failures table: a row for a streamed reply that ended without the service's closing message, which "What is never done with the answers" pointed to and the table lacked; the case added to the rehearsal (script rule 11). Whether to ask again at the model's maximum length is left for whoever writes the script to propose | Not a ruling: the third check (`check-2026-11-18-third.md`), finding 2 |
| A paragraph under the failures table, "Which row, when a stream breaks": a stream that breaks with an error or a timeout after some text has arrived is cut off and asked once more; one that breaks before any text is a failed attempt under the first row, not "Empty". It cites Anthropic's streaming page, opened 2026-11-18, for the error that can arrive part way through a stream. Both cases added to the rehearsal (script rule 11) | Not a ruling: the fourth check (`check-2026-11-18-fourth.md`), finding 1 |
| One phrase, "the service's signal that the reply is complete", in the failures table, under "What is never done with the answers" and in script rule 11, in place of "closing message" in two places and "closing event" in one. The row above this pair keeps the old phrase as the record of what it said | Not a ruling: the fourth check, finding 2 |

The message files in `sent/` were rebuilt for the wording rulings; the method refers to them by
`sent/SHA256SUMS`, so no checksum is written into this file.
