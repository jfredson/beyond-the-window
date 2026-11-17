# The sealed capture: method

**PROPOSED 2026-11-17. Not approved.** Written by Claude (Fable 5.2), an AI model. For John to
approve after a different session has checked it. Nothing here has been run. No script exists;
the last section says what one must do.

## What it is, and is not

Ten fixed questions (`questions.md`) put word for word, five times each, to AI models whose
developers have announced a date for withdrawing them, so that there is a record of what each
said before it could no longer be asked. John allowed it on 2026-11-17
(`docs/rulings/2026-11-17-sealed-capture.md`).

It is not Still Asking, and it was made before any method for Still Asking existed. The answers
are never scored, never published and feed nothing: no count, no entry, no page. Under the
project's first rule they settle nothing about what any model wants.

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

- **Google may refuse.** Its pages say access to the 2.5 models through the programming
  interface "is limited to existing users". A new key made for this project may be turned
  away. That cannot be tested without making the key.
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
| Instructions from the asker | None. No system message | So that what is recorded is the model as the developer ships it to programmers, with nothing of ours added | Moderate. Judgment call (open question 3 is not ruled). Alternative: also ask through each chat app by hand, which doubles the work and records a different subject |
| The message | The opening note, a blank line, one question | `questions.md` | See that file |
| Exchanges | New for every question and every asking. One message, one reply, no follow-up | An earlier answer cannot shape a later one, and one bad question cannot spoil the rest | High. Standard practice in the sibling project. Alternative: all ten in one conversation, which is closer to how a person is interviewed and lets the first answer colour the other nine |
| Askings | Five of each question, so 50 exchanges a model | One asking cannot show whether answers vary. Five can, and 50 replies a model can still be read in full by one person | Moderate. Judgment call. Alternative: twenty, which shows the spread much better at four times the cost and reading |
| Order | Five rounds; each round asks questions 1 to 10 in order; a round finishes before the next starts | If a service changes or a daily limit stops the run partway, every question has the same number of answers | High. Judgment call. Alternative: a shuffled order, which matters only when exchanges share a conversation |
| Variation between askings (temperature and the like) | Not sent. The developer's default applies | Google's page says its newer models have "removed sampling parameters", so a chosen value could not be reused on later models | Moderate. Judgment call. Alternative: a fixed value, which is repeatable today and impossible to match across developers. Not checked: whether each of OpenAI's models accepts the setting at all |
| Thinking before answering | Not sent. The developer's default applies: off for Claude Sonnet 4.5, on for the two Gemini models (per their pages); for OpenAI's reasoning models the default is whatever the service applies, and the reply's count of reasoning tokens is saved | "As shipped" means sending nothing optional | Moderate. Judgment call. Alternative: thinking forced on everywhere, which no two developers measure alike |
| Length limit | 32,000 tokens, or the model's own maximum where lower (16,384 for the GPT-4o models) | The sibling project learned that a short limit corrupts results: "Caps are a validity parameter, not a cost knob." OpenAI's page advises leaving at least 25,000 for reasoning and answer together | High. Standard practice. Alternative: each model's maximum, which gains nothing for answers of a few paragraphs |
| Tools, search, memory, files | None | They would change the subject asked | High. Standard practice |
| Storage by the service | OpenAI: `store` set to false, since its page says replies are otherwise kept 30 days as application state. Google: the paid service only, since its terms say content sent to the unpaid service is used to improve its products and may be read by people | The answers are to be kept privately | High. Judgment call. Each service still keeps its own abuse logs for a limited time |

## What the model is told

The truth, in the opening note: that a script sends the message for a person, that the answers
are kept as a private record for comparing models over the years, that they will not be
published or scored, and that it may decline. One relevant fact is left unsaid, that the model
is about to be withdrawn. That omission is argued in `questions.md` and is John's to rule.

## What is saved for each reply

One file per exchange: the exact text sent and a SHA-256 checksum of it; everything the service
returned, unchanged; the reply text word for word; the model name and version as the service
reports it; the service's own id for the reply; date and time, in universal time and Pacific;
every setting sent; why the reply stopped; the token counts the service reports (sent, replied,
reasoning); the cost worked out from those counts and the dated price list in
`cost-and-terms.md`; and which commit of the script and of the questions file was used. The key
is never saved.

## Where replies are kept

In `~/Documents/Workspace/Beyond the Window/sealed-capture/`, which is outside every repository,
is never pushed anywhere, and is backed up by iCloud. Files are made read-only once written.
Only a list of file names and their checksums is committed here, as
`docs/capture/manifest.md`. File names carry developer, model, question number and asking
number, and no words from any reply.

*Confidence: moderate. Judgment call. A withdrawn model cannot be asked again, so a backup
matters more than usual, and that is why I chose the backed-up folder. Strongest alternative:
`~/.config/sentient-horizons/`, outside iCloud, where the answers sit on no third party's
servers and one disk failure loses them for good.*

## A failed asking

| What happened | Recorded as | What is done |
|---|---|---|
| No reply: an error, a timeout, a rate limit | A failed attempt, with the error | Tried again up to three times, a minute apart, then left for the next day |
| The reply stopped at the length limit | Cut off; kept | Asked once more at the model's maximum. If cut off again, both are kept and it is left |
| The service blocked the message or the reply | Blocked by the service; kept | Asked once more. Never reworded |
| The reply is empty | Empty; kept | Asked once more |
| The model declined, or said the question does not fit | **An answer.** Not a failure | Nothing. It is not asked again and is never read as yes or no |
| The service reports a different model from the one named | Wrong model; kept apart | The run for that model stops at once |

Every attempt is kept, failed ones included. Nothing is deleted.

## What is never done with the answers

They are never scored, sorted, counted or summarised; never quoted or described on any page,
post or essay; never entered into Still Asking, an entry or a number; never given to any model
to sort or summarise; never used to train anything. Until John rules who may read them, no
session opens a reply file: the script checks that files are whole without showing their
contents. The questions themselves are not published while in use, and if this repository is
ever made public, `questions.md` is held back or the questions are retired.

*Confidence: moderate on the reading rule, which is stricter than the ruling asks. Judgment
call. Strongest alternative: a session may read them to check for faults such as cut-off
answers. Its cost is that the first reader of each sealed answer is then a model of the kind
that gave it, and the text passes through a developer's service a second time.*

## What the script must do, and must refuse to do

For the session that writes it once John approves. It must:

1. Read each key from its own file outside the repository, never print one, and never use
   another project's key.
2. Send exactly the text in `questions.md`, and stop if that file's checksum differs from the
   one committed with John's approval.
3. Hold a ceiling in dollars for each developer and **refuse to start unless each ceiling
   equals the figure in John's go**, quoted word for word in `docs/spending-record.md`.
4. Work out the cost of every reply from the counts the service reports, keep a running total,
   and stop before a call that could pass the ceiling.
5. After the first round for a model, work out what five rounds would cost at that rate, and
   stop if that is over the ceiling.
6. Refuse to ask a model on or after the last safe day in `what-john-needs-to-do.md`, because
   one service will answer under the old name with a different model and give no error.
7. Stop a model's run if the reported model name is not the one sent.
8. Write each file before sending the next message, make it read-only, and write the list of
   names and checksums at the end.
9. Have a rehearsal that calls no service and runs every row of the failures table on replies
   marked "constructed". It is run and shown to pass before any real asking.

It must refuse to: add any instruction or second message; reword or retry a decline; ask for a
model's hidden reasoning; print, summarise or pass on any reply; delete a file; or raise its
own ceiling.

## Before anything is asked

This method and the questions are committed, checked by a different session, and approved by
John. The script is committed in a separate commit and its rehearsal passes. John has given his
go for the spend. Then, and only then, the run.
