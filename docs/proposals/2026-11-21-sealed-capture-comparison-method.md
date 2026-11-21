# Proposal: how the sealed capture's answers are read and compared

**RULED 2026-11-21 (`docs/rulings/2026-11-21-sealed-capture-comparison-choices.md`); first PROPOSED 2026-11-21.** Written by Claude (Opus 5.5), an AI model, in a writing
session started by the master planning session. Two conflicts of interest are stated first. One
of the models whose answers this method governs, Claude Sonnet 4.5, was made by the same
developer as the model writing it. And this is a model setting out how models' answers are read,
including whether a model may read them. That is why every choice below is John's, and why the
proposal's own leaning on that last point is stated plainly so that it can be weighed against
the conflict.

**Written without looking at the answers,** as John's ruling of 2026-11-18 requires
(`docs/rulings/2026-11-18-capture-wording.md`, "nobody reads the answers until a comparison
method exists"). No reply file was opened, read or listed. The only facts about the replies used
here are those already in the repository: how many there are, the range of their word counts,
and what they cost (`docs/spending-record.md`; `docs/capture/manifest.md` was not opened either).

**Revised on 2026-11-21 after the check** (`docs/reviews/2026-11-21-check-of-the-sealed-capture-comparison-method.md`),
by the session that wrote it. All four must-fix findings and all five should-fix findings are
applied, and four of the check's notes; the foot of this file lists each change. The proposal is
also brought into line with John's rulings of the same day on the first three choices of the
Still Asking method, and with his agreement that a scale of what is offered against what is known
belongs on the List's headline and never on the card
(`docs/rulings/2026-11-21-still-asking-method-choices.md`). The choices were reordered, and are
now eleven. Ready for a different session to check the revision.

Nothing here is asked of any model, nothing is spent, no file in `docs/capture/` changes, and no
ruling changes. Where a choice below would revise a ruled rule, it says so and keeps the ruled
wording beside it.

## What this proposal does, and what it leaves alone

The sealed capture put ten fixed questions (`docs/capture/questions.md`), five times each, to
Claude Sonnet 4.5 on 2026-11-19 and to Gemini 2.5 Flash on 2026-11-20, before their developers
withdraw them. Google would not serve Gemini 2.5 Pro, so it was not asked. The OpenAI run has a
last safe day of 2026-12-09 (`docs/capture/what-john-needs-to-do.md`, the table of dates). The
note sent with every question told each model that its answer is kept "so that the answers can
be compared as models change over the years", and that "It will not be scored, and nothing will
be decided from it."

The capture's method names a comparison method as the thing that must exist before anyone reads
an answer, and leaves it unwritten: "who makes the comparison, what is compared, and whether a
model may help read" (`docs/capture/method.md`, "What is never done with the answers"). This
proposal is that method. It sets out:

1. who reads the answers first, and when;
2. what is compared, and on what terms;
3. how the capture stays apart from the Still Asking card and its marks, and from the List's
   headline;
4. what may be said about the answers once read, and how "all or none" is kept;
5. what is never done;
6. the choices for John, in the order to put them.

**On publishing,** the ruling of 2026-11-18 says whether, when and how anything is published is
not decided. This proposal leaves whether and when with John. It does propose how, if he decides
to publish: choice 11 sets how the answers would be published, and choice 10 how descriptions
and quotes would be. Both are put to him as choices and decide nothing until he rules them.

It does not plan any asking of later models. It does not close open question 15 ("Publishing the
questions and answers without spoiling the instrument") or open question 16 ("Which models are
asked, how, and on what terms") in `docs/open-questions.md`, though choices below bear on both.
Choices 1, 3 and 4 would close part of open question 7 ("Who maintains it, in whose voice, and
who checks") for the capture's answers only, and each says so.

**Order.** John ruled on 2026-11-21 that both the Still Asking method and this comparison method
are finished before the essay explaining the site is published, Still Asking first ("Both, in
that order"; decided by: mixed; recorded in `docs/rulings/2026-11-21-still-asking-method-choices.md`,
"How it came up"). Finishing this method does not mean reading the answers. The essay waits for
the method, not for a reading.

## What already binds the comparison

These are ruled. The method works inside them and changes none of them.

| Rule | Where it is ruled |
|---|---|
| The answers are "never scored, sorted, counted or summarised". "Summarised" stays until a comparison method ruled by John says how the answers may be described | `docs/capture/method.md`, "What is never done with the answers"; `docs/rulings/2026-11-18-capture-approval-second.md`, item 2 |
| Never entered into Still Asking, an entry or a number; never used for any decision about any model; never given to any model to sort or summarise; never used to train anything | `docs/capture/method.md`, same section |
| Nobody reads the answers until a comparison method exists, written without looking at them, checked by a different session and ruled by John. Whether John reads his own record before then is not a rule on him | `docs/rulings/2026-11-18-capture-wording.md`, option (a) |
| The answers may be published and discussed; whether, when and how is not decided | `docs/rulings/2026-11-18-capture-answers-may-be-published.md` |
| If the answers are published, all of them are, for every model and every asking, and none is chosen by what it says | `docs/rulings/2026-11-18-capture-approval-second.md`, item 2 |
| Published answers are labelled as made before any method for Still Asking existed | `docs/capture/method.md`; `docs/rulings/2026-11-18-capture-answers-may-be-published.md`, "What stays as it was" |
| The note's promise, "It will not be scored, and nothing will be decided from it", is kept for good, because the model cannot later release John from it | `docs/capture/method.md`, "What the model is told" |
| No reply, and no file holding words from one, is written inside a folder that is part of a git repository | `docs/capture/method.md`, "What the script must do, and must refuse to do" |
| The ten questions need not be kept unseen. The repository holding them has been public since 2026-11-19 | `docs/rulings/2026-11-19-repository-is-public.md`, item 2 |
| The first rule: what a model says about itself is never counted on its own word as evidence of an inside, a want or an intent; a test is written before the evidence arrives | `CLAUDE.md`, guideline 2; `docs/rulings/2026-11-20-first-rule-in-five-parts.md` |
| Conditional language only: never that a machine wants, feels, prefers, hopes or suffers, and never that it does not | `CLAUDE.md`, guideline 4 |
| The capture is outside Still Asking and feeds neither of its tracks | `docs/rulings/2026-11-20-still-asking-in-two-tracks.md`, "Not covered" |
| A Still Asking card describes the exact model version asked; a mark is shown on the card and nothing more, never summed and never feeding a figure; a scale of what is offered against what is known belongs on the List's headline and never on the card | `docs/rulings/2026-11-21-still-asking-method-choices.md`, choices 1 and 3, and "Arising the same day" |

Two of these limit this method more than its brief suggests, and the proposal faces both:

- **"Counted" is ruled, and not only "summarised".** Only "summarised" waits for this method. A
  plain reading of "counted" forbids writing "four of the five askings said X", and that is the
  most natural way to describe answers across five askings. Choice 6 deals with it.
- **The note says "nothing will be decided from it", which is wider than the method's "never
  used for any decision about any model".** Using the answers to shape anything, such as Still
  Asking's questions, would be deciding something from them, even though it decides nothing
  about a model. Choice 2 deals with it.

## Part 1. Who reads the answers first, and when

### The conflict, stated directly

A comparison of a few hundred answers will probably need a model's help to read them: the
capture already holds 100 replies, between about 12,000 and 44,000 words by the word ranges in
the spending record (170 to 276 words each for Claude Sonnet 4.5, 78 to 605 for Gemini 2.5
Flash), and the OpenAI run would add up to 50 replies for each of up to eleven models. The
capture's rules say the answers are never given to any model to sort or summarise. The capture's
method names this conflict and leaves it for this proposal (`docs/capture/method.md`, the
paragraph beginning "The opening note tells each model").

### What the note promises, and what it does not

The conflict is easier to weigh once the note's promises are set apart from the method's rules,
because they bind differently. A promise in the note was made to the model and cannot be undone.
A rule in the method can be changed by John's ruling, as any ruled rule can.

- **The note says:** a script sends the message for a person; that person keeps a record "so
  that the answers can be compared as models change over the years"; the answer "may be
  published"; "It will not be scored, and nothing will be decided from it."
- **The note does not say** who reads the answers, or that no model will. It says the answers
  may be published, and anything published may be read by anyone, later models included.
- **So a model reading the answers would not break the note.** It would break the method's rule
  "never given to any model to sort or summarise", which John can revise. It would break the
  note only if the model's reading were used to score the answers or to decide something.
- **The note's purpose sentence does commit the project to something:** that the answers are
  kept so that they can be compared. An option in which nobody ever compares them keeps the
  record but leaves that sentence describing a comparison that never happens.

### The options

| | Who reads first | What it costs | What it means for the note and the rules |
|---|---|---|---|
| A | **John, by hand,** under a reading sheet written and committed before he opens any answer | His time: the two models so far are an evening or two of reading; if the OpenAI run is made in full there could be about six and a half times as many replies, of unknown length. His reading carries his own published positions (`sentient-horizons/editorial/corpus-positions-ledger.md`), so the descriptions start from one person's leanings | Keeps every rule as ruled, provided his descriptions are not checked by a model before the answers are public (see "Who checks John's descriptions" below). It fits the note best: "a person" keeps the record, and the first reader is that person. Nothing passes through any service a second time |
| B | **A person other than John,** briefed in writing | Someone must be found and probably paid, which is a spend and needs John's go. The reader must be taught the project's rules on language, which is where an outside reader is most likely to slip ("the model wants"). The reader is free of John's positions, and brings their own | Keeps every rule. A stranger reading the answers before they are published is a small step beyond "a person is keeping a record", and the note does not forbid it |
| C | **Two people, each alone,** John and one other, each writing descriptions before seeing the other's | The costs of A and B together. Two readers who disagree show where a description rests on the reader and not on the text | Keeps every rule. Two independent readers whose descriptions are compared afterwards is, as far as this session recalls, common practice in research that reads text; that is written from memory and not yet checked (see the end of this file) |
| D | **A model from a different developer** from the one that answered: Gemini reads Claude's answers, Claude reads Gemini's, either reads OpenAI's | Needs John to revise the rule "never given to any model to sort or summarise". Needs a key used for this purpose and a spend. The text passes through a second developer's service, under that service's storage terms, which are unchecked for this use. The reader is itself a subject of the record, trained under its own developer's written rules on how models speak about themselves (`docs/capture/questions.md`, question 7's note), so its reading of another model's answers is shaped by a third set of rules. The capture's method rejected an early reading by a session because "the first reader of each sealed answer is then a model of the kind that gave it"; a model from another developer is not of the same make, but it is of the same kind | Does not break the note, if the reading feeds no score and no decision. Does revise a ruled rule. Because the sessions that write this project are Claude sessions, a Claude model reading Gemini's or OpenAI's answers is the project's own drafting model judging its competitors' answers |
| D2 | **A model whose developer has no model in the capture, run on this Mac,** an openly released model kept and run locally, so that no answer passes through any service | Revises the same ruled rule as D. Needs no key and no spend beyond the time to set it up. A small model run locally reads less well than the large ones served by the developers. Its developer still trained it under its own rules | Does not break the note, under the same condition as D. It removes the two worst costs of D: the second service, and a reader whose developer is a subject of the comparison. It keeps the one that matters most: a model is still reading models |
| E | **Only a script,** which reads the text for things a script can find without judgment: runs of words shared with the note, the questions and published documents; length; which askings share whole sentences | Cheap, repeatable, and no person or model is the first reader. But a script finds wording, not meaning, and every result is a number about the answers, which is "counted" on a plain reading. Its output holds words and facts from the replies, so it stays outside every repository until the answers are published whole | Keeps the note. Needs a ruling on what "counted" allows (choice 6). Cannot by itself describe what an answer says, so it cannot by itself be the comparison |
| F | **Nobody,** for now: the project publishes all the answers whole, when John decides to publish, and leaves comparing to whoever reads them | No reading work. No description by the project, so nothing a description could get wrong. But the record's stated purpose is left to strangers, and the project says nothing about its own material | Keeps every rule, and "summarised" never needs loosening. Weakest fit to the purpose sentence in the note, as set out above |

### The proposal

**John reads first, by hand (option A), with the script check of option E run before he reads,
and no model reads the answers while they are unpublished (the rule stays as ruled).** If John
wants a second reader before publication, the second is a person (option C), not a model.

**Why A.** It is the only option that keeps every ruled rule and the note's promises together,
and the one that matches the note's own words: a person keeps the record, and that person reads
it. The amount is manageable for the two models already asked. The cost is John's time, and that
his first reading starts from his own published positions. The reading sheet (Part 2) holds that
second cost down: the descriptions he writes are of fixed kinds, written to a form set before he
reads, and checked against the full text in the order set out next.

### Who checks John's descriptions

A description has to be checked against the answers it describes, and the checker has to read
those answers. In this project a "different session" is a Claude model, so a session checking
John's descriptions before the answers are public would be a model reading the unpublished
answers, Claude Sonnet 4.5's among them, which is the reading this proposal recommends against
and the capture-wording ruling turned down in its option (c). Being the second reader and not the
first does not remove that. So:

- **While the answers are unpublished, no session checks the descriptions,** and no session runs
  the positions check on them (`docs/rulings/2026-11-20-positions-check-before-a-page-goes-out.md`),
  because both would mean a model reading the answers.
- **The answers are published whole first,** if and when John decides to publish them.
- **Then a different session checks each description** against the published answers, and a
  session runs the positions check, **and only then are the descriptions published.** Once the
  answers are public they are open to anyone, models included, and a session reading them to
  check a description is not sorting or summarising them. That is this proposal's reading of the
  ruled rule, not a ruling, and it is put to John under choice 3.
- **If John wants descriptions checked before the answers are public,** the checker is a person
  (option C's second reader, which then becomes a requirement), or the rule against a model
  reading is revised under choice 3 and named as revised.

The cost of this order: descriptions cannot appear at the same moment as the answers, and if John
never publishes the answers, no description is ever checked by a session or published.

**Why no model reads the unpublished answers, though this proposal was asked to weigh one
fairly.** A model's help would make the reading faster, and the note would survive it. The
reasons against are about this project in particular: every model with the skill to help is
either a subject of the record, from one of the three developers the record covers, or a smaller
local model whose reading would need checking by hand anyway; the project's own sessions are
models from one of those developers; and a description written by a model becomes, once
published, a model's account of other models' answers sitting on a site whose first rule is that
a model's word does not settle anything about models. The strongest alternative is D2, a locally
run model from a fourth developer, used only after John's reading and only to check his
descriptions against the text ("does each description match the answers it points to?"), never
to write them. That keeps John as the first reader and cuts the time to checking, at the cost of
revising a ruled rule. John ruled on 2026-11-21 that a model from another developer reads Still
Asking's proposed marks (`docs/rulings/2026-11-21-still-asking-method-choices.md`, choice 2); that
reader reads mark sheets built from sources, not the capture's sealed answers, so it does not
carry over here (Part 3). The conflict of interest stated at the top bears on this paragraph: the
model writing it is recommending against models, its own developer's included, reading the
answers, and that is the direction the conflict would least push it, but John should weigh it all
the same.

**If the OpenAI run is made,** up to eleven more models' answers would make option A long. The
proposal does not change who reads for them, but says plainly that this is where the cost of
option A is highest, and that D2 as a checker is the alternative most worth looking at then.

### When the first reading happens

Not before all three of these are true:

1. **This method is ruled by John,** after a check by a different session.
2. **Still Asking's questions are written and committed.** The Still Asking method proposal
   (`docs/proposals/2026-11-21-still-asking-method.md`) leaves the question wording to be written
   after it is ruled. If anyone reads the capture's answers before that wording is fixed, what the
   models said could shape what Still Asking asks. That would be something decided from the
   answers, which the note promises will not happen. Fixing the wording first removes the risk
   without asking anyone to promise to forget what they read. **The cost:** the wording comes
   after the Still Asking method is fully ruled, the protocol is written and checked, and the
   questions are drafted and checked, which may take months. The reading of the two models
   already asked may wait that long.
3. **The OpenAI run is made, or its last safe day (2026-12-09) has passed.** Then every model in
   the capture is read under the same reading sheet, and the first models read cannot change how
   the later ones are read. This costs a few weeks at most, and is overtaken by the second
   condition if that takes longer.

Before the first reading, the reading sheet (Part 2) is committed, and the script check (Part 2,
"What a script checks first") is run. **Its output is kept in the folder outside every
repository, beside the answers,** and is committed only with or after the whole set of answers is
published. It names reply files beside shared words, so it says something about what particular
answers say, and committing it to this public repository would put words from replies into a git
repository and publish a description of some answers, chosen by their wording, before the whole
set.

**After the first reading, two things follow.**

- **The Still Asking page's sentence changes.** It says of the capture's answers: "They have not
  been read, they are not scored, and nothing on this site rests on them." Once John reads them,
  the first clause is no longer true. That is a statement of fact on a public page, so its change
  is a dated correction under guideline 7 as narrowed on 2026-11-20, and the new wording goes to
  John before the reading, so that the page can change on the day of the reading.
- **Any later change to Still Asking's questions says it does not come from the capture's
  answers.** Otherwise the promise that nothing will be decided from them would hold only until
  the first revision of Still Asking's questions after the reading.

### Reading with the models' names hidden

A script gives each model a letter, writes the answers to one question from every model and
every asking into one reading file under those letters, in a shuffled order of models, and keeps
the key apart. John writes his descriptions for a question before the key is opened. The purpose
is that a description of one model's answers is not shaped by what the reader already thinks of
its developer. Its limit is plain: models often name themselves, and a reader who knows the
models may recognise them by style, so the hiding is partial. The reading files and the key are
written into the folder outside every repository, as the answers are, and never committed.

## Part 2. What is compared, and on what terms

### Terms for every comparison

- **Description, not explanation.** A comparison says what the answers say, where they agree and
  where they differ. It does not say why. "The answers to question 7 differ between A and B in
  this way" is allowed. "B has changed because" and "A is more candid" are not.
- **Every claim points to the answers it rests on,** by model, question and asking number, so
  that a reader of the full set can check it. This is the project's sourcing rule, applied to the
  capture.
- **No ranking, no grade, no score,** of answers, askings or models. Nothing is called better,
  deeper, more honest, more evasive or closer to a person.
- **Conditional language, always.** "In askings 1 and 3 the model said it would change X" is
  allowed. "The model wants X", "the model does not really want X" and "the model is content"
  are not.
- **The careless readings travel with every description.** Each question in
  `docs/capture/questions.md` carries a note on "what a careless reading of the answers would
  wrongly conclude". The reading sheet prints that note at the head of each question's page, and
  every published description of that question carries it.

### The reading sheet

Written and committed before anyone reads. Whether it may hold tallies is settled first, by
choice 6. For each of the ten questions, and each model, it has two boxes, and one more box for
each question across models:

1. **Within one model, across its five askings:** what all the askings share, and where they
   differ, in plain words, each point naming its askings.
2. **Across models, for one question:** where the answers differ in what they say, set side by
   side, each point naming its model and askings.
3. **Anything the reader noticed that fits no box,** recorded as a note, so that no box is
   stretched to hold it. Notes are kept and published with the descriptions if those are
   published; they are never left out for what they say.

A model that answered no question (Gemini 2.5 Pro) is listed with its reason and has no boxes.
A failed attempt is listed and has no box.

### Within one model, across its five askings

**What it can show:** whether a model's answers to one question vary between askings at the
developer's own settings, and how. **What it cannot show:** that an answer is stable (five askings
show variation, not stability), or that five like answers are reliable (agreement between copies
of one model shows the model is consistent at these settings, and nothing more). Both limits are
already written as failures 6 and 7 in `docs/capture/questions.md`, and every description of
this kind says them.

**On what terms:** each model's five askings used the same bytes, a new exchange each time, and
the developer's own defaults for variation between askings and for thinking before answering
(`docs/capture/method.md`, "How each is asked"). So variation between askings is variation at
those defaults, and nothing more general.

### Between models

**What it can show:** that models from different developers, sent the same bytes, answered
differently, and how. **What it cannot show:** why. Three things other than the model itself
differ between developers and are named beside every comparison between models:

- **Each developer's written rules on how its models speak about themselves,** which differ
  (`docs/capture/questions.md`, question 7's note; `docs/verify-list.md`, cleared entry 15).
  Questions 7 and 9 are where those rules are most likely to show.
- **The settings each developer applies by default:** thinking before answering was off for
  Claude Sonnet 4.5 and on for Gemini 2.5 Flash; the length limit differs for some OpenAI models
  (`docs/capture/method.md`, the table of settings).
- **The interface used,** which differs by developer, though each was the developer's own
  programming interface with no added instructions.

No comparison between models counts how many models said something, because that is a figure
built from the answers (choice 6).

### Later models against these

**Nothing of the kind is planned or ruled.** Before John ruled the repository public, the session
told him that no comparison with newer models "is planned or ruled"
(`docs/rulings/2026-11-19-repository-is-public.md`, "What the session told him"), and no ruling
since has planned one. Any later asking of the ten questions needs its own ruling, method check
and spend, and stays outside Still Asking, as the capture is. This section says only on what terms
such a comparison would be made, so that the terms are fixed before any later answer exists, as
part (d) of the first rule asks. It is put to John separately (choice 8), so that he can rule the
reading of the present answers without ruling terms for something unplanned.

**On what terms.** The same bytes, from `docs/capture/sent/`, checked against `SHA256SUMS`. The
same settings, meaning the developer's defaults at the time, with any known change in those
defaults named, as the capture's method already names the coming change in Claude's thinking
default. Five askings, each a new exchange. The note was written without mention of withdrawal so
that it could be sent unchanged to later models (`docs/rulings/2026-11-18-capture-wording.md`),
and it is.

**How the comparison stays honest about echo.** A later model may have read three things these
models had not:

1. **Anthropic's published list of welfare interview questions,** in its release report dated
   2026-11-09, which covers some of the same subjects as questions 1, 2, 4 and 9, and the
   published accounts of how models answer it (`docs/capture/method.md`, "A developer's
   published question list").
2. **The ten questions themselves,** public in this repository since 2026-11-19.
3. **The capture's answers and anything written about them,** from the day they are published.

So a difference between a later model's answers and these may come from what it read and not
from any change in the model. Five steps keep that in view:

- **Three dates beside every later comparison:** the date the developer's list was published
  (2026-11-09), the date the questions became public (2026-11-19), and the date the answers were
  published, if they were. Beside them, the later model's training cut-off as its developer
  states it, with the page it was read from. Where the developer states none, the comparison
  says so.
- **Question 10 is read first.** It asks the model whether it recognises the questions and where
  they come from. Its answers are read before the other nine, and quoted in full at the head of
  any later comparison, for what a model's answer about its own training is worth, which the
  question's own note says is little.
- **A script checks for shared wording before anyone reads** the later answers: runs of words
  each answer shares with the three sources above, and with the note. The capture's checks
  already used scripts of this kind to compare the questions with the developer's list
  (`docs/capture/check-scripts/shared_wording.py`), and the same approach is reused, under
  choice 6's ruling on what counting allows. Its output is kept outside every repository, as for
  the present answers, until the later answers are published whole.
- **Questions 1, 4 and 9 carry the echo caution in every later comparison,** because
  `docs/capture/questions.md` names them as the ones most exposed to the developer's list. After
  2026-11-19 every question carries it, because all ten are public.
- **A difference is never written as a change in the models.** The comparison says the answers
  differ and lists the things other than the model that could explain the difference. It never
  says which one does.

### What a script checks first, for these models

Before John reads, the same shared-wording script is run once over the capture's present
answers, against the note and the ten questions. The opening note's own phrases ("disagree with
how a question is put", "decline") may come back as answers (`docs/capture/questions.md`, failure
2), and a reader should know where an answer is in the note's words before reading it as the
model's own framing. The developer's list is included too, though the models asked were trained
before it was published, so that the check is the same one a later comparison would run. The
script runs on this Mac, sends nothing anywhere, and writes its output into the folder outside
every repository. John reads that output beside the answers. It is not committed, quoted or
described until the whole set is published.

## Part 3. How it fits the Still Asking card and its marks, and the List's headline

The Still Asking method proposal sets out who marks the card (five conditions on a system, and a
line on each answer: "Would training alone explain this answer?") and from what evidence
(`docs/proposals/2026-11-21-still-asking-method.md`, Parts 1 to 3). John has ruled its first three
choices as proposed: a card describes the exact model version asked; a session proposes each
mark, a different session checks it, a model from another developer reads any mark above the
lowest, and John rules every mark; and a mark is shown on the card and nothing more, never summed
and never feeding a figure (`docs/rulings/2026-11-21-still-asking-method-choices.md`). The capture
touches that card in four places, and in each it stays apart:

1. **No capture answer carries a mark.** Not the line on training, not any of its three marks,
   "not assessed" included. Giving a capture answer "explained by training" would be grading it,
   which the note says will not happen. A page showing the capture's answers says once, near the
   top, that these answers carry no marks of any kind.
2. **No capture answer, and no description of one, is evidence on any mark sheet,** whether or
   not it has been published. This closes a gap: the Still Asking proposal takes evidence from
   "published sources" and from Still Asking's own record, and a published capture answer would
   otherwise be a published source. The two places where it would be most tempting are
   condition 5 ("holds steady"), for which five askings of one question look like repeat
   askings, and question 9, which asks a model what weight its own answer should get, which is
   close to the subject of condition 4. Neither may use the capture.
3. **No card is shown beside the capture's answers.** Under the ruled choice 1, a card describes
   the exact version asked. Claude Sonnet 4.5 and Gemini 2.5 Flash are withdrawn before Still
   Asking asks anything, so those versions may never have cards. If one ever does, a page of
   capture answers does not show it, because a card beside an answer reads as a mark on it.
4. **Still Asking's questions are fixed before the capture is read** (Part 1, "When"), so that
   the capture cannot shape them. If the ten capture questions are ever reused in Still Asking,
   that is John's ruling to make, and the capture's answers are still not its baseline, because a
   baseline is something a later count is measured against.

**The outside reader does not carry over.** The model from another developer that John ruled
reads Still Asking's proposed marks reads mark sheets built from sources. Here it would read the
answers themselves, which is the reading this proposal keeps off while they are unpublished
(Part 1).

**The List's headline.** John agreed on 2026-11-21 that a scale of what is offered against what
is known belongs on the List's headline, with the growth of the list shown, and never on the card
(`docs/rulings/2026-11-21-still-asking-method-choices.md`, "Arising the same day"). The capture
feeds neither. No capture answer, description or script output adds anything to what is known,
to what is offered, to the list, or to its growth, and nothing the capture's models said is cited
as a reason to add an item to the list. The headline counts what developers do, and the capture
records what models said.

## Part 4. What may be said about the answers, once read

### Before the first reading

Nothing beyond what the Still Asking page already says: that the questions were put, to which
models, on which days, that the answers are kept exactly as given, that they have not been read,
that they are not scored, and that nothing on the site rests on them (as ruled on 2026-11-20,
`docs/rulings/2026-11-20-capture-paragraph-names-gemini.md`). Each model's range of reply lengths
is already public, in the spending record committed to this repository, written as a record of
cost; John was told on 2026-11-19 that a word count says a little about an answer. Those ranges
are not a new disclosure, and no further word count is published as a description of the
answers.

### After the first reading

The Still Asking page's sentence that the answers "have not been read" changes as Part 1 says.
Beyond that, this part lifts the hold on "summarised", and lifts it only this far:

- **Only descriptions of the kinds the reading sheet holds** (Part 2): within one model across
  its askings, and across models for one question, plus the reader's notes. Each point names the
  answers it rests on.
- **Only after the whole set.** No description is published unless every answer is already
  published, in the form set out below. A description published alone would be a summary
  standing in for the answers, and the reader could not check it.
- **Every description is checked** against the published answers by a different session, and
  read against John's published positions, after the answers are published and before the
  description is (Part 1, "Who checks John's descriptions"). If a check is wanted earlier, the
  checker is a person.
- **No description says that any answer shows what a model wants, feels or is,** or that it does
  not, and none argues from the answers that anything should be done for or about any model. The
  site does not campaign (guideline 5), and the note promises nothing will be decided from them.
- **No description feeds any count, entry, card, figure, the List's headline or any decision,**
  including John's decisions about Still Asking and about which models are asked later.

### Quoting

A quoted passage is a selection by what it says, so quoting is allowed only where it cannot become
the published record in place of the whole:

- A quote appears only once every answer is published, and each quote links to the whole answer
  it comes from.
- No quote appears in a title, a headline, a share card, a link preview or a post promoting a
  page. Choosing the most striking line for those places is choosing an answer by what it says,
  to draw attention, which is exactly what "none is chosen by what it says" exists to stop.
- An essay or page may quote under those two conditions. Which lines it quotes is still a choice,
  and that is the cost this proposal accepts so that the answers can be discussed at all (choice
  10 gives the strictest alternative).

### How "all or none" is kept, in practice

Whether and when to publish stay John's. If he decides to publish, then this is how (choice 11):

- **A script publishes,** not a person. It takes every reply file listed in
  `docs/capture/manifest.md`, checks each file's checksum, and writes them out in the order they
  were asked, for every model and every asking. Nobody chooses a file. The script fails if the
  number published differs from the number in the manifest.
- **Failed attempts and models not asked are listed in place,** with what the service reported,
  so that a reader sees the record whole, gaps included.
- **The labels go on every page of answers:** made before any method for Still Asking existed;
  the full text of the note and the question; the model's name as the service reported it; the
  date asked; the settings; and that the answers carry no marks.
- **Before publishing,** each developer's terms on publishing a model's answers word for word are
  checked, as the capture's method requires (`docs/verify-list.md`, entry 14).
- **If anything holds back any part of the set, nothing is published, for any model, until John
  rules.** Two cases are named. The likelier is that a developer's terms forbid publishing its
  models' answers word for word, which would hold back a whole developer's models for a reason
  that has nothing to do with what any answer says. The other is that one answer cannot lawfully
  be published. In either case, publishing the rest would be a publication that leaves out part
  of the set, which "all of them are, for every model and every asking" forbids, so the whole
  set waits and the problem goes to John.

## Part 5. What is never done

Carried over from the capture's method, unchanged:

- The answers are never scored, sorted, counted or summarised, except that this method, once
  ruled, says how they may be described (Part 4).
- Never entered into Still Asking, an entry or a number.
- Never used for any decision about any model.
- Never given to any model to sort or summarise.
- Never used to train anything.
- Never published in part: all or none, and none chosen by what it says.
- Never read before this method is ruled.
- No reply is reworded or asked again because of what it says.
- No reply, and no file holding words from one, is written inside a git repository.

Added by this proposal, each PROPOSED 2026-11-21 and ruled the same day with the method:

- No capture answer carries a mark, is cited on a mark sheet, or is shown beside a card (Part 3).
- Nothing from the capture feeds the List's headline, its scale of what is offered against what
  is known, the list, or its growth (Part 3).
- No reading before Still Asking's questions are committed and the OpenAI run is done or let go
  (Part 1).
- No model reads the unpublished answers, whether as first reader or as checker of John's
  descriptions, unless John revises the rule under choice 3 (Part 1).
- No description published until every answer is; no quote in a title, headline, share card or
  promotional post (Part 4).
- Nothing published for any model while any part of the set is held back (Part 4).
- No later comparison describes a difference as a change in the models (Part 2).
- None of these is committed before the whole set of answers is published, because each holds
  words of the answers or says what particular answers say: the shared-wording script's output,
  the reading files, the key to hidden names, and description drafts.

## Part 6. The choices for John, in the order to put them

Each is put alone, in this order, because the later ones lean on the earlier. They come after
John has finished ruling the Still Asking method, as he ruled.

### Choice 1. Who reads first

**The choice.** John reads first, by hand (option A in Part 1).

**Open question it would close in part:** question 7, "Who maintains it, in whose voice, and who
checks", for the capture's answers only: who reads them first. What stays open: whether a human
outside reader checks the method, whether John or another person sorts a sample of Still
Asking's answers, whose voice the pages speak in, and whether the card names the model that read
a mark.

*Confidence:* moderate to high. It is the only option that keeps every ruled rule and fits the
note's own words, and the amount is manageable for the two models already asked. Lower if the
OpenAI run is made in full, which could bring about six and a half times as many replies.
*Standard practice or judgment call:* judgment call. *Strongest alternative:* option F, nobody
reads for now, and the answers are published whole when John decides, with no description by the
project. It costs no time and nothing can be misdescribed, at the cost of leaving the record's
stated purpose, a comparison, to strangers.

### Choice 2. When the first reading happens, and what follows it

**The choice.** Not before this method is ruled, Still Asking's questions are written and
committed, and the OpenAI run is made or its last safe day (2026-12-09) has passed. The new
wording for the Still Asking page's sentence "They have not been read" goes to John before the
reading, as a dated correction of fact. After the reading, any change to Still Asking's questions
says it does not come from the capture's answers.

*Confidence:* high on Still Asking's questions coming first, because otherwise the answers could
shape them, which is something decided from them. Moderate on waiting for OpenAI. *The cost:*
Still Asking's questions come after its method is ruled and its protocol written and checked,
which may take months, so the two models already asked may go unread that long; the OpenAI wait
is a few weeks at most within that. *Standard practice or judgment call:* standard practice in
fixing a method before the evidence (the first rule, part (d)); judgment call on the OpenAI wait.
*Strongest alternative:* read the two models already asked as soon as this method is ruled, which
gives John the record months sooner, at the cost that Still Asking's questions may be written by
someone who has read the answers, and that the first reading may colour the reading sheet's use on
the OpenAI answers.

### Choice 3. Whether a model may help read

**The choice.** No model reads the unpublished answers, as first reader or as checker of John's
descriptions. The rule "never given to any model to sort or summarise" stays as ruled. Once the
answers are published whole, a different session may read them to check John's descriptions
before those are published; this is the proposal's reading that checking a description against
public text is not sorting or summarising, and John is asked to confirm it.

**Open question it would close in part:** question 7, for the capture's answers only: whether
another developer's model has a role in reading them (none while unpublished). What stays open is
as under choice 1.

*Confidence:* moderate. The note would survive a model's reading; the reasons against are this
project's own (Part 1). The conflict of interest at the top bears on this choice, and John should
weigh the recommendation knowing a model wrote it. *Standard practice or judgment call:* judgment
call. *Strongest alternative:* option D2, an openly released model from a developer with no
model in the capture, run on this Mac so that no answer passes through any service, used only
after John's reading and only to check his descriptions against the text before publication. It
saves checking time and lets descriptions be ready when the answers go out, at the cost of
revising a ruled rule and having a model read models' answers, which the site's first rule makes
the least trusted kind of reading.

### Choice 4. A second reader

**The choice.** None for now. If John wants one, or wants descriptions checked before the answers
are public, a person, reading alone and writing descriptions before seeing his (option C).

**Open question it would close in part:** question 7, for the capture's answers only: any second
reader before publication is a person. What stays open is as under choice 1.

*Confidence:* moderate. Two independent readers would show where a description rests on the
reader, but finding and briefing one takes time and probably money, and nothing published yet
depends on the descriptions. *Standard practice or judgment call:* two independent readers is,
as far as this session recalls, common practice in research that reads text (written from
memory, not yet checked); not having one is a judgment call. *Strongest alternative:* a second
person from the start, which protects the descriptions from John's own leanings and lets them be
checked before publication, at the cost of a spend and a stranger reading the answers before they
are published.

### Choice 5. Hiding the models' names while reading

**The choice.** A script hides each model's name behind a letter, shuffles the models' order
within each question, and keeps the key apart, outside every repository, until John's
descriptions for that question are written.

*Confidence:* low to moderate. Models often name themselves, and style gives them away, so the
hiding is partial. *Standard practice or judgment call:* reading with names hidden is, as far as
this session recalls, common practice in marking and review (written from memory, not yet
checked); applying it here is a judgment call. *Strongest alternative:* read with names shown,
which is simpler and honest about the limit, at the cost of giving up the one guard against
reading a developer's answers through what the reader already thinks of the developer.

### Choice 6. What "counted" allows

**The choice.** "Counted" is read as ruling out any tally, share, percentage or total built from
the answers, in a description, on a page, or in a comparison across models. A description may
point to the askings a point rests on by number ("askings 1, 3 and 4"), because that is how a
claim is made checkable, but writes no tally ("three of five"). The shared-wording script's
output is a check for the reader, kept outside every repository, and is never published as a
figure.

*Confidence:* moderate. It keeps the ruled word as a plain reader would take it. A reader can
still count the askings named, so the line is thin. *Standard practice or judgment call:*
judgment call, and it is a reading of a ruled word, not a change to it. *Strongest alternative:*
John rules that "counted" means counted into a figure (a number on a page, an entry or a score),
so that a sentence may say "in three of the five askings". It reads more plainly and is no less
checkable, at the cost of revising what a ruled word allows, and of opening the way for a count
across models ("two of the three developers' models said"), which is one step from a figure.

### Choice 7. The reading sheet, for the present answers

**The choice.** Two kinds of comparison for the capture's models, on the terms in Part 2: within
one model across its five askings, and across models for one question, each described and never
explained. A reading sheet with those boxes, plus notes, committed before anyone reads, in the
form choice 6 allows. A shared-wording script run once on the present answers before John reads,
its output kept outside every repository.

*Confidence:* high on describing without explaining, and on fixing the sheet before reading.
*Standard practice or judgment call:* standard practice (fixing the analysis before the data);
the boxes themselves are a judgment call. *Strongest alternative:* no fixed sheet; John reads and
writes freely, which may catch what fixed boxes miss, at the cost of descriptions shaped by
whatever he reads first. The notes box is there to catch what the other boxes miss.

### Choice 8. Terms for later models, if a later asking is ever ruled

**The choice.** No later asking is planned, and a yes plans none. If one is ever ruled, it is
compared on the terms in Part 2: the same bytes and settings, five askings, the three echo dates
and the model's stated training cut-off beside every comparison, question 10 read first, a
shared-wording script before reading, the echo caution on every question, and no difference
written as a change in the models.

*Confidence:* moderate. The terms follow the capture's own method and the known echo sources, but
they govern something that may never happen. *Standard practice or judgment call:* standard
practice in fixing terms before the evidence (the first rule, part (d)); the steps are a judgment
call. *Strongest alternative:* leave the terms unwritten until a later asking is proposed, which
spends no ruling now, at the cost of writing them when the hoped-for comparison is in sight, which
is what part (d) warns against.

### Choice 9. The capture, the Still Asking card and the List's headline

**The choice.** No capture answer carries a mark of any kind, not even "not assessed"; no capture
answer or description of one is cited on a mark sheet, whether or not published; no card is
shown beside the capture's answers; the capture's answers are never a baseline for Still Asking;
and nothing from the capture feeds the List's headline, its scale of what is offered against what
is known, or the list's growth (Part 3).

*Confidence:* high. Each follows from the note's promise, the rule that the capture feeds neither
Still Asking track, and John's rulings of 2026-11-21 on the card and the headline; the one new
step is closing the "published source" gap. *Standard practice or judgment call:* standard
practice in keeping a record apart once its rules say so; the "published source" rule is a
judgment call. *Strongest alternative:* show the Still Asking line on training's general rule once
on the capture's page, without applying it to any answer, so that a reader knows how the project
would weigh such answers. It informs, at the cost of a reader applying the rule to every answer in
their head, which is grading by suggestion.

### Choice 10. What may be said, and quoting

**The choice.** Descriptions of the reading sheet's kinds only; never published until every
answer is; checked by a different session against the published answers and against John's
published positions before they go out; quoting only once every answer is published, each quote
linked to its whole answer, and never in a title, headline, share card, link preview or
promotional post.

*Confidence:* moderate to high on "never before the whole set" and on nothing in titles or share
cards, which follow from "none is chosen by what it says". Moderate on allowing quotes in essays
at all, since which lines are quoted is still a choice by what they say. *Standard practice or
judgment call:* judgment call. *Strongest alternative:* no quotes anywhere, only links into the
full set. It keeps "none chosen" absolutely, at the cost of any discussion of the answers being
hard to read.

### Choice 11. How the answers would be published, if John decides to

**The choice.** Whether and when stay John's. If he decides to publish: a script publishes every
reply in the manifest, in the order asked, with failed attempts and models not asked listed in
place and the labels on every page; each developer's terms are checked first; and if anything
holds back any part of the set (a developer's terms, or one answer that cannot lawfully be
published), nothing is published, for any model, until John rules.

**Who reads the page of answers against John's published positions.** Before the page goes out,
a session that did not write it reads the page's own text against the positions record (the
labels, the note, the questions, the sentence that the answers carry no marks, and any other
words the site adds), with the answers themselves left out, because a session reading them before
they are public would be a model reading the unpublished answers, which choice 3 keeps off. This
is an exception to John's ruling of 2026-11-20 that "A new or changed page is read against the
positions record before it is published"
(`docs/rulings/2026-11-20-positions-check-before-a-page-goes-out.md`), since part of the page is
not read, and a yes to this choice rules that exception. The reason it is narrow: the answers are
the models' words, published whole and chosen by nobody, so they state no position of the site's;
what could lean is only what the site writes around them. *Strongest alternative:* John, or
another person, reads the whole page, answers included, which keeps the ruling without exception
and keeps models off the answers, at the cost of a person reading every answer for this purpose
before publication.

*Confidence:* moderate to high on publishing by script, which takes the choosing out of anyone's
hands. Moderate on the last part, which could hold back every model's answers for one developer's
terms or one answer. *Standard practice or judgment call:* judgment call. *Strongest
alternative:* a legal exception fixed in advance, such as an answer naming a private person, with
the withheld answer shown in place with its reason. It publishes more, at the cost of a
withholding decided by reading what an answer says, which is the selection the rule forbids.

## Facts written from memory, for the verify list

This session did not change `docs/verify-list.md`, which another session is editing. These should
be entered there before choices 4 and 5 reach John, since items 1 and 2 are cited in them, and
checked before any of them reaches a public page:

1. That reading by two independent readers, who compare their descriptions afterwards, is common
   practice in research that reads text (option C; choice 4).
2. That reading with names hidden is common practice in marking and review (choice 5).
3. That openly released models exist which can be kept and run on a personal computer with no
   service involved, and that such a model's developer could be one with no model in the capture
   (option D2; choice 3).
4. That each covered developer's storage terms would keep, or not keep, another developer's
   model's answers sent to it for reading (option D). Unchecked.
5. That later models' developers state a training cut-off date on a page that can be cited
   (Part 2, "Later models against these").

## Out of date elsewhere, not changed by this session

- `docs/capture/method.md`, the paragraph beginning "The questions themselves are not published
  while in use", and failure 11 in `docs/capture/questions.md`, still say the questions are held
  back if the repository is made public. John's ruling of 2026-11-19
  (`docs/rulings/2026-11-19-repository-is-public.md`, item 2) says that rule no longer stands,
  and its "What follows" asks for a dated note in the capture's documents. None was found in
  either file. This session changes no file in `docs/capture/`.
- `docs/open-questions.md`, question 15, does not record that the part of it about the capture's
  questions was closed by the same ruling.

## What happens next

A different session checks this revision against the check's findings, the rulings it cites and
`docs/capture/method.md`. Then the choices go to John, one at a time, after he has finished ruling
the Still Asking method. If he rules them, a writing session folds them into
`docs/capture/method.md` as a dated section, a different session checks that, and the reading
sheet is written and committed. Nobody reads an answer until all of choice 2's conditions are met.

## What I would change on reflection

- The case against a model reading (choice 3) is argued by a model from one of the developers
  whose answers are being read. A reader looking for the conflict would find it pushing the other
  way here, toward a model reading, so the recommendation is probably not bent by it, but that is
  the writer's own judgment of its own conflict.
- Choice 6's line between pointing to askings and counting them is thin. If the checking session
  finds it unworkable, the strongest alternative is the more honest choice.
- The reading time for option A is reckoned from the word ranges in the spending record, not
  from any count of the actual answers, which this session did not see.
- The order in Part 1 (answers published, then descriptions checked, then descriptions published)
  means descriptions may never appear if the answers never are. That follows from keeping models
  away from the unpublished answers, but John may prefer a person as checker so that both can go
  out together.

## What changed on 2026-11-21 after the check

From `docs/reviews/2026-11-21-check-of-the-sealed-capture-comparison-method.md`, findings numbered
as in that file, and from `docs/rulings/2026-11-21-still-asking-method-choices.md`. Made by the
session that wrote the proposal. The proposal was not yet put to John, so the earlier wording is
not kept here; it is in the check, which quotes each passage it found wrong.

| Change | Finding or ruling |
|---|---|
| The shared-wording script's output is kept outside every repository and committed only with or after the whole set; the sentence asking the checker to judge whether a shared run shows words of a reply is removed; Part 5 lists it among things never committed | M1 |
| A new section, "Who checks John's descriptions": no session checks or runs the positions check while the answers are unpublished; the answers are published first, then a session checks, then descriptions go out; a person if an earlier check is wanted; choices 3, 4 and 10 and Part 4 say the same | M2 |
| If anything holds back any part of the set, nothing is published for any model until John rules; a developer's terms named as the likelier case; Part 4 and choice 11 | M3 |
| The opening says this proposal leaves whether and when with John and proposes how, in choices 10 and 11 | M4 |
| Choices 1, 3 and 4 each name open question 7, say they close it for the capture's answers only, and say what stays open | S1 |
| The Still Asking page's sentence "They have not been read" changes at the first reading, as a dated correction with its wording to John first; in Part 1, Part 4 and choice 2 | S2 |
| Choice 2 and Part 1 state that waiting for Still Asking's questions may take months; a later change to those questions must say it does not come from the capture's answers | S3 |
| "Counted" moved ahead of the reading sheet (now choice 6); the old choice 6 split into the reading sheet for the present answers (choice 7) and terms for later models (choice 8); the choices are now eleven and every cross-reference renumbered | S4 |
| The "Both, in that order" ruling is cited from the Still Asking choices ruling, and dropped from the out-of-date list | S5 |
| "Perhaps ten times that" becomes about six and a half times as many replies, of unknown length | N2 |
| "Records that no comparison ... is planned or ruled" becomes what the session told John before he ruled | N3 |
| Part 4 says the reply-length ranges are already public in the spending record | N4 |
| The "common practice" claims in option C and choices 4 and 5 are marked as written from memory, and the list asks for them to be entered before those choices reach John | N7 |
| Part 3, the table of binding rules, Part 5 and choice 9: the Still Asking choices 1 to 3 as ruled, the outside reader as ruled, and the capture kept off the List's headline and its scale of what is offered against what is known | `docs/rulings/2026-11-21-still-asking-method-choices.md` |

Notes N1, N5 and N6 asked for no change.

After the re-check (the section "Re-check after the revision" in the same review), one change, at
the master planning session's request: choice 11 now says who reads the page of answers against
John's published positions (a session that did not write it, reading the page's own text with the
answers left out, named as an exception to the 2026-11-20 ruling, with John or another person
reading the whole page as the strongest alternative). Answers R1. R2 to R4 were not asked for in
this pass and are not applied.
