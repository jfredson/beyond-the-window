# The records: a framework

**PROPOSED 2026-11-17. One part ruled the same day:** that every entry carries two readings
kept apart (section 5), with how wanting is recorded left open
(`docs/rulings/2026-11-17-kickoff-decisions.md`). The rest is not ruled. Written by Claude
(Fable 5.2). This is a framework only. No
record has been written, there is no validator, and no field name here is final.

It has two kinds of section, marked in each heading:

- **Framework.** The parts the kickoff marks as frameworks, written as proposals. Each carries
  a confidence, whether it is the family's standard practice or a judgment call, and the
  strongest alternative.
- **Sketch.** The parts the kickoff marks as first sketches. Each is written down so there is
  something to argue with, and each names the open question it depends on (the numbers are
  those in `docs/open-questions.md`). A sketch is not a proposal waiting for a yes.

Every part is an opening guideline (John, 2026-11-17) and is expected to change as the open
questions are explored.

> **Brought into line with later rulings on 2026-11-21.** This note replaces one that said the
> proposal `docs/proposals/2026-11-17-how-a-machines-word-earns-weight.md` was not yet ruled.
> John ruled its changes on 2026-11-20 and the card on who is answering on 2026-11-21. The
> sections changed are 2 (the cautions row, and a sketch row for the card), 5 (a third reading),
> 7 (the order of evidence, and matches as the least informative result), 8 (the line on
> training on each answer) and 9 (three kinds of caution). Each change carries a dated note
> naming its ruling. How the card's marks are assigned and recorded is not ruled; it is proposed
> in `docs/proposals/2026-11-21-still-asking-method.md`.

Row numbers such as "A8" point at `docs/inheritance.md`.

## 1. What a record is (framework)

One plain-text file per thing recorded, named for its id, in TOML, the layout every sibling
uses. A validator refuses a file that breaks a rule, including a file with a field it does not
know. One export script is the only reader of the files, and every page reads its output.

*Confidence: high. Standard practice (rows B4, B8, C1). Strongest alternative: one file per
branch, as The Belt Equation and The Upgrade Tree have, which is easier to read whole and
harder for two sessions to work on at once.*

## 2. The kinds of record (framework for the split, sketch for the list)

The framework is the split: **the record of the world and the record of what models said are
different kinds of record, in different folders, and neither is computed from the other.** This
is the family's rule that talk never becomes a measure of the world (row E1) applied to the
project's two halves.

*Confidence: high. Standard practice. Strongest alternative: one record per aspiration holding
everything about it, which is simpler to read and is how the two halves would come to be
mixed.*

The list below is a sketch. It depends on open questions 14 (what the tracked things are), 2
(what counts as wanting) and 17 (how the two halves sit together).

| Kind | What it holds | Nearest sibling record |
|---|---|---|
| Branch | One of the small set of things a mind might reach for: plain name, one sentence of meaning, where it comes from on the starting list drawn from biological minds, whether it sits in the main set or beside it | Outrunning Ageing's branch record |
| Tracked thing | One specific thing that would have to happen, with a test | The Upgrade Tree's upgrade record |
| Claim | What a named person or organisation said or promised, with the primary source | The AGI Zeitgeist's claim record |
| Publication | A paper, report or company statement that bears on a tracked thing, logged once and never edited | The Quiet Galaxy's publication record |
| Caution | A recorded argument or finding of one of two kinds: the cost of attributing wants that are not there, or the safety reading of wants that are | None; new here |
| Asking | One run of Still Asking: which questions, which models, when, under which registered version | Minimum Viable Mind's registered run |
| Answer | One model's reply to one question in one asking, word for word | The AGI Zeitgeist's stored reply |
| Reading of an answer | How an answer was sorted, by whom, with the words it rests on | The AGI Zeitgeist's coded row |
| Weekly reading | Each record read against the week's news, with a verdict | Every sibling's reading record |
| Retired list | Ids that have been retired, each with a reason and a pointer | Every sibling's retired list |
| Card mark (added 2026-11-21, sketch) | One mark on the card on who is answering: the system, the condition, the mark, its evidence in the ruled order, who proposed, checked and decided, and a dated history | None; new here |

*Notes added 2026-11-21.* The Caution row's "of two kinds" is the wording of 2026-11-17. There
are three kinds since John's rulings of 2026-11-18 and 2026-11-20 (section 9). The card on who
is answering and its wording are ruled (`docs/rulings/2026-11-21-the-reshaped-card.md`); that it
is held as a record of its own, and what the record holds, is a sketch taken from the proposal
`docs/proposals/2026-11-21-still-asking-method.md`, Part 4, and is not ruled.

## 3. What every record of the world carries (framework)

The ten things the tracker pattern says every sibling's record has (row A8), unchanged:

1. A stable id that is also its public address, never renamed.
2. A plain name and a description for a reader who has never heard of the thing.
3. The group it belongs to.
4. The test: what would count as it having happened, written so two readers would agree.
5. The kind of public record that settles the test, named in advance.
6. The state now, with the date it was set and the record behind it.
7. A dated history of every change: date, field, old value, new value, why.
8. A list of facts set down before their source was opened.
9. Notes.
10. A validator that refuses the file on any broken rule.

*Confidence: high. Standard practice. Strongest alternative: none worth proposing for records
of the world.*

Three additions proposed for this project:

- **The date added**, on every record (row B9).
- **The kind of progress**: technical, political or cultural, from John's statement of
  2026-11-17. *Confidence: moderate. Judgment. It depends on open question 14, which may make
  this a ladder of its own instead of a field. Strongest alternative: no field, and let the
  settling record say what kind it is.*
- **Which unit of machine mind the thing concerns**: the weights, the character across
  versions, or the single conversation. *Confidence: low. Judgment. It depends on open question
  1. Strongest alternative: leave it out until that question is explored.*

**Added 2026-11-20: a note on what a placement rests on.** A record that sits beside the list
may carry one optional field, `placement_note`: a sentence or two saying what its placement
rests on. The entry's own page shows it straight after the reason for the placement, and
nowhere else. Most records have none, and one has it today, the entry on memory across
conversations, whose sentence John ruled
(`docs/rulings/2026-11-20-memory-entry-says-what-its-placement-rests-on.md`). The records
script refuses the field on an entry that is on the list, because its page gives no reason for
a placement to put the sentence after. That the sentence is held in a field of its own, and
not in the dated history or the group's sentence, was decided by a session (decided by: agent).

*Added the same day, after a check:* the note is public wording, so the records script also
refuses it unless the record names the ruling that approved it (`placement_note_ruling`, the
file's name in `docs/rulings/`), that file exists, and the note stands in it word for word. A
made-up sentence in the field no longer builds. Decided by: agent.

**Added 2026-11-21: two marks on a developer's dated act.** `announces = true` marks an act that
announces a change still to come. The page of acts and the feed show it as usual, and the table
of developers does not take its date as the day the developer began. `seen_in_effect = true`
marks an act that records the thing seen in effect on that day, when the day it began is not
known; where the table takes its date from such an act, it writes "By" with the date in place of
"Since". The marks were made for OpenAI's row on the entry about ending a conversation
(`docs/rulings/2026-11-21-openai-date-corrected.md`). The records script refuses either mark on
an act that is not a developer's or that takes something back, both on one act, and an entry
marked as offered by a developer whose only act is an announcement. Decided by: agent. Since a later
check the same day, the records script and the export also refuse a "Since" or "By" date in
the table that differs from the headline file as last committed, unless the entry holds a
history row dated the same day naming that developer.

## 4. Ids (framework)

- An id is plain lower-case words joined by hyphens, and is the last part of the record's page
  address.
- It is never renamed once committed. A record that needs a new identity is retired in the
  retired list with a reason and a pointer, and a retired id is never reused.
- An id carries no branch prefix, because a record's branch may change.
- **An id never contains the name of a model, a developer or a product.** Those are retired
  and renamed, and The Belt Equation twice had to rename ids because of what they contained.

*Confidence: high on the first three, which are standard practice (rows B1, B3). Moderate on
the fourth, which is a judgment call from a sibling's mistake (row B2). Strongest alternative
to the fourth: allow a developer's name where the tracked thing is that developer's own
commitment, which reads more plainly and ties the address to a company that may be renamed or
bought.*

Answers are the exception to plain-word ids: an answer is identified by its asking, its
question and its model, and the model's exact version is a field on the record. How an answer
is addressed is a sketch that depends on the protocol.

## 5. The two readings on an entry (framework)

Every branch, and every tracked thing where it applies, shows two readings and keeps them
apart:

- **Reach**: how far the world has got toward making it possible.
- **Wanting**: what evidence there is, of any kind, that a machine mind wants it.

*Confidence: high that there are two readings and that they are kept apart; it is the kickoff's
fourth decision. Judgment call. Strongest alternative: track reach only and leave wanting to
Still Asking as a separate thing with no place on an entry, which removes the hardest design
problem and also removes the half of the question that makes this project different from a
list of capabilities.*

What each reading's state looks like is in sections 6 and 7, and both are sketches.

*A third reading, ruled since; note added 2026-11-21*
(`docs/rulings/2026-11-20-third-reading-on-who-is-answering.md`, "Yes, sources first", and
`docs/rulings/2026-11-21-the-reshaped-card.md`; both decided by: mixed). Beside the two readings
on an entry there is a third, on who is answering. It is on the speaker and not on the entry,
and it is shown as a card on each answer in Still Asking, with no single score: five conditions
on the system that gave the answer, and one line on the answer about whether training alone
would explain it. It is not a reading on an entry's page. That nothing on the card feeds reach is this writer's
reading, not a ruling; the nearest ruled words are the Still Asking page's sentence that an
answer "will never feed the count of things offered, or any other figure on the home page",
which John's go of 2026-11-20 covered
(`docs/rulings/2026-11-20-go-to-publish-the-rebuilt-home-page-once-checked.md`).

## 6. The state of reach (sketch; depends on open questions 14 and 12)

The kickoff's sketch is a five-rung ladder: idea only; shown in research; offered by one
developer; offered by several; standard practice.

What the review found:

- It fits technical progress. It does not fit a law, a ruling, a signed commitment or a change
  in what people accept.
- The siblings' rule that a stage never moves down does not hold here (row A17). A developer
  can withdraw what it offered.
- A ladder applies to a tracked thing, not to an aspiration as a whole.

A sketch of what the state might hold instead of a single rung: the stage, the date it was
set, the record that set it, and, where it has gone backwards, that fact with its own date and
record. Whether political and cultural progress share this ladder, have their own, or are
dated entries with no stage, is open question 14.

## 7. The state of wanting (sketch; depends on open questions 2, 3 and 15)

The kickoff's sketch is a second five-rung ladder: never asked; stated when asked; stated
consistently across rewordings and versions; chosen when a real option is offered at some cost;
chosen consistently across developers.

**I would not build this as sketched**, for the reason in the review's first point: its first
three rungs are climbed by a model's statements about itself, which the project's first rule
says settle nothing.

A sketch of the alternative, to argue with: no single state. A table of evidence by kind, each
kind kept apart and never added to the others:

| Kind of evidence | What is recorded | What it can show |
|---|---|---|
| Said | Which askings put the question, to which models, and how the answers were sorted | What models say when asked this way, and how that changes between generations |
| Chosen | Published results, or Still Asking results, where a real option was offered | What models do when offered this, under the stated conditions |
| Measured without the model's own report | Published research that reads something from inside a model | What that research found, with its own limits |
| Not found | Searches and askings that turned up nothing | That nothing was found, which is not the same as nothing being there |

Each row would link to the answer records, publications and claims it rests on, and would carry
no summary word such as "wanted".

*The order ruled; note added 2026-11-21* (`docs/rulings/2026-11-20-order-of-evidence.md`, "Yes,
that order"; decided by: mixed). The rows above are in the order sketched on 2026-11-17. On
every entry, evidence is now shown in this order and never summed: (1) measured without the
machine's word; (2) reports checked against an independent reading of the system's workings;
(3) choices made at a cost; (4) bare statements. The sketch's "Chosen" row is the third kind
and its "Said" row the fourth; reports checked against an independent reading are a kind of
their own, which the sketch did not have. Not ruled: where "not found" sits, and the label that
says what a costly choice does and does not show.

Also to be recorded beside it, from John's guiding principle: **where this entry sits on the
starting list drawn from biological minds, and whether what models say matches it, departs
from it, or has no counterpart.** How a departure is recorded is part of open question 5.

*Ruled since; note added 2026-11-21* (`docs/rulings/2026-11-20-two-rewordings.md`, "Yes,
both"; decided by: mixed). A match with the starting list is treated as the least informative
result, because models were trained on human writing, and a departure, or evidence from the
system's structure, as the most informative. Continuity is recorded as what is kept and what is
built from what, and no record written from 2026-11-20 on says that a model's retirement is a
harm to it, or that it is not. The words a reader sees for these labels are not ruled.

## 8. Records of what models said (framework for the rules, sketch for the fields)

The rules are framework:

- **An answer is kept word for word and never edited.** A correction is a separate dated note.
- **An answer names the exact model and version that gave it**, as the developer reports it,
  and the date and time.
- **An answer names the asking it belongs to, and the asking names the registered version of
  the protocol it ran under.**
- **A reading of an answer is a separate record** from the answer, names who or what did the
  reading, and carries the exact words it rests on.
- **A decline, a refusal and a cut-off answer are each recorded as what they are**, and none is
  read as a yes or a no.
- **Nothing in these records is a field on a record of the world.** A check in code keeps any
  answer or reading out of any count of reach (row A4).
- **A constructed example is flagged** and can never be exported as a real answer (row B10).

*Confidence: high. Standard practice drawn from Minimum Viable Mind and the AGI Zeitgeist (rows
H2, I3, I6, I8). Strongest alternative: store only the readings and a checksum of each answer,
keeping the full text off the repository, which protects the instrument from its own echo
(open question 15) and gives up the family's rule that a reader can check the record.*

The fields are a sketch and wait on the protocol: the question's id and exact wording, the
checksum of what was sent, the settings, the length limit, whether the model was asked as
shipped to the public or with no instructions, how many times it was asked, and the reported
token counts and cost.

*Ruled since; note added 2026-11-21.* Every answer carries one line, ruled by John on
2026-11-21 (`docs/rulings/2026-11-21-the-reshaped-card.md`, "Yes, as shown"; decided by:
mixed): "Would training alone explain this answer?", with one of three marks, explained by
training, not fully explained (with the check that shows it, possible only where the card's
fourth condition applies), or not assessed. Until the Still Asking method is ruled, every
answer is marked not assessed. Still Asking also has two tracks
(`docs/rulings/2026-11-20-still-asking-in-two-tracks.md`), so an answer will need to say which
track it belongs to, and, in the second, which continuing individual gave it. Those two fields
are a sketch; who assigns the marks and how is proposed in
`docs/proposals/2026-11-21-still-asking-method.md` and is not ruled.

## 9. Cautions (framework that they exist, sketch for the layout)

The kickoff's framework: two kinds of caution are recorded with the same care as the hopeful
evidence. One is the cost of attributing wants that are not there. The other is the safety
reading of wants that are.

*Confidence: high that the record exists and that both kinds are kept. Judgment call from the
kickoff. Strongest alternative: no separate record, with two required fields on every entry,
which guarantees that no entry lacks its cautions and makes a caution that spans several
entries hard to place.*

*Overtaken by later rulings; note added 2026-11-21.* The two kinds above are the wording of
2026-11-17. There are three kinds since John's ruling of 2026-11-18
(`docs/rulings/2026-11-18-a-third-caution.md`), the headings were worded on 2026-11-19
(`docs/rulings/2026-11-19-caution-headings.md`), and the third was reworded on 2026-11-20
(`docs/rulings/2026-11-20-third-caution-heading-reworded.md`). The headings read: "If an AI
system has no wants, and is treated as if it had"; "If an AI system has wants, and they go
unnoticed"; "If an AI system puts people at risk, whether or not it has wants". The validator
idea below would then ask for a caution of each of the three kinds.

The layout is a sketch and depends on open question 6. One idea: a caution is its own record
with a source, linked from every entry it bears on, and the validator refuses an entry in the
main set that links to no caution of each kind.

## 10. Claims and publications (framework)

As the siblings have them (rows E2, E4, E5, D4, D6):

- A claim carries who said it, when, the exact words from a primary source, and what it commits
  to. Coverage alone carries no quoted words and is marked as coverage.
- Claims are entered "in every direction", as the kickoff says: what developers promise, what
  advocates argue, what critics say, what safety researchers warn.
- The site gives no hit rates and scores no person.
- A publication is logged once and is edited afterwards only to fix an error, with a changelog
  line. A record written from an abstract says so.
- **Evidence that comes only from a model's maker is marked as such** (inheritance, part 2,
  item 25). On this subject that will be most of it.

*Confidence: high. Standard practice.*

## 11. The supporting branch (sketch; depends on open question 8)

The kickoff's sketch: one supporting branch on whether anyone is there at all, where Minimum
Viable Mind appears as one entry among others.

A sketch of how it would sit: beside the main set, not in it; marked so in its record; and kept
out of any headline by a check in code, as The Belt Equation's Contact Clause is. Whether it is
a branch here or only a set of links to the relatives that own the question is open.

## 12. What the validator would refuse (sketch)

Listed so the intent is on record. None of it exists.

- A file with an unknown field.
- A tracked thing with no test, or no named kind of settling record.
- A state above the lowest rung with no dated record behind it.
- An id that vanished without a retired entry, or a retired id reused.
- An id containing a model's, developer's or product's name.
- A claim with quoted words and no primary source.
- A main-set entry with no caution of each kind.
- An answer with no model version, or no asking, or an asking with no registered protocol
  version.
- Any count of reach that reads an answer or a reading of one.
- A constructed example not flagged as one.
- A news post, later, while any verify entry is open.

## 13. What is deliberately not here

- No probabilities, no years and no ranges. The kickoff rules them out, and so does The Upgrade
  Tree for itself.
- No field for what a model "wants". There is no such fact to record.
- No field that scores a developer or a person.
- Nothing private.

## What I would change on reflection

- Section 2's list has ten kinds, which is a lot before a single record exists. A first version
  could start with four (branch, tracked thing, publication, claim) and add the Still Asking
  kinds only when a protocol is ruled.
- Section 7's table may be too cautious to be useful to a reader. The test is whether a
  stranger can say back what the "said" row means without reading it as "wants".
