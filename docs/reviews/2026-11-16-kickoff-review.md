# Review of the kickoff, before anything is built on it

Written 2026-11-17 by Claude (Fable 5.2) in a Claude Code session, at John's asking. The file
name carries 2026-11-16 because that is the date of the kickoff it reviews.

**What was read.** The kickoff (`docs/2026-11-16-kickoff.md`). The family's tracker pattern, in
the main-branch copy, and the design standard and design lessons ledger
(`sentient-horizons/design/`). The instruction files, kickoffs, method and record layout
documents, changelogs, review protocols and rulings documents of Outrunning Ageing, The Belt
Equation, The Quiet Galaxy, The Upgrade Tree, the AGI Zeitgeist and Minimum Viable Mind. Six
helper sessions read the repositories and reported; I read the tracker pattern, the design
standard's key sections and Outrunning Ageing's instruction file and kickoff myself. The full
inventory is `docs/inheritance.md`.

**A disclosure, as the kickoff asks.** This review was written by a machine of the kind the
project is about, reviewing a kickoff written by the same kind of machine. Nothing here settles
anything. It is an argument for John to rule on.

**John's three statements during this session (2026-11-17)** are taken into account below and
quoted in `docs/open-questions.md`: that the project needs a protocol for asking frontier models
the same questions over time; that progress to track is technological, political or cultural;
and that the first assumptions about what a mind might want come from biological minds, humans
and other animals both, as a guiding principle for the opening phase.

## The short answer

1. **Is the kickoff's approach the best one?** Mostly yes. Putting frameworks in place and
   holding the design open is the right order, and "inherit by default" matches what the family
   already wrote down for a sixth site. One part of the first sketches contradicts the kickoff's
   own first rule and should not be built on as written (point 1 below).
2. **Does it fit the family's architecture?** The half that tracks progress in the world fits
   well. The half that questions models does not fit the tracker pattern at all, and the family
   has only one precedent for it, Minimum Viable Mind, which the tracker pattern explicitly does
   not cover. The project is two kinds of thing joined together, and the kickoff should say so
   (point 2).
3. **What needs considering first?** Seven things, in the order given under "What to consider
   first" at the end.

## Where the kickoff is right

- **Frameworks first, sketches labelled as sketches.** The AGI Zeitgeist changed its headline
  twice in one day (2026-10-17) and rebuilt its record of predictions two days after building
  it (2026-10-19), both times because a summary number was designed before anyone had settled
  what the record was for. The kickoff avoids that by refusing to settle the headline, the
  branches and the ladders now.
- **Inherit by default.** The tracker pattern's section on the shared record shape ends with a
  paragraph headed "What a sixth site would start from" (section 3a.5, added 2026-10-24). It
  names ten things every record has, asks the new site to pick one of five existing kinds of
  state or state a sixth, and requires nothing else. The kickoff's rule is that paragraph put
  as a principle.
- **"Self-report settles nothing" already exists in the family, in a stronger form.** The Belt
  Equation's "null rule" (decided 2026-09-19) was written for exactly this subject: the hope of
  meeting a machine mind. The kickoff carries its first clause. The other three clauses matter
  just as much here (point 3).
- **Conditional language** matches Minimum Viable Mind's standing rule that its public reports
  are "never 'it is conscious,' never 'nothing is there'".
- **Costing every run before it happens** matches the family's spending rule, although the
  kickoff quotes a version of that rule that has since been replaced (point 6).

## The main points

### 1. The wanting ladder and the second headline count contradict "self-report settles nothing"

The kickoff's first authorship rule says a model's statements about itself settle nothing. Its
sketch of the wanting ladder then has five rungs, of which the first three are "never asked,
stated when asked, stated consistently across rewordings and versions". Those rungs are climbed
by self-report and nothing else. The sketched headline then counts how many aspirations "show
consistent evidence of being wanted", which would be a number computed from those rungs.

So a reader would see a number that goes up when models say they want something more
consistently, on a site whose first rule is that what models say settles nothing. The family
has a rule against this in two places:

- The tracker pattern, rule 6.1: what people said and what the world did are kept in separate
  records, and "a statement never becomes a measure of the world".
- The Belt Equation's null rule, first clause: "Nothing a candidate system says about itself
  counts toward any rung."

There is also a known way this goes wrong. Developers train models to speak about themselves in
particular ways, so "stated consistently across versions" may measure a developer's policy
holding steady and nothing about the model.

**What I would change.** Keep the two readings (reach and wanting). Do not make wanting a
ladder that statements can climb. Record the evidence about wanting by kind (what was said,
what was chosen when a real option was offered, what was measured without relying on the
model's own report), show each kind separately, and never add them into a single "wanted"
verdict. Any number at the top is then worded as a count of answers or of evidence, never as a
count of wants. This is a proposal; the question stays open (open questions 2, 3 and 4).

### 2. The project is a tracker joined to a measuring programme, and only half of it has a pattern

Every sibling tracker reads what other people publish. A record is settled by a paper, a
regulator's approval or a company's own release, and the family rule (tracker pattern, rule
3.3) is that every fact carries a source a reader can open.

Still Asking is different in kind. Its answers are the project's own measurements. The tracker
pattern says in so many words that its sourcing rule does not apply to Minimum Viable Mind,
"whose facts are its own measurements under its registration rules". So:

- The **reach** half is an ordinary tracker and can inherit almost everything, with The Upgrade
  Tree as the closest model (stages, a count, no probabilities).
- The **Still Asking** half is a measuring programme and inherits from Minimum Viable Mind's
  registration and review practice and from the AGI Zeitgeist's practice for sorting text with
  several models. Neither was built for this, and both have recorded failures that bear on it
  directly (see `docs/still-asking-protocol.md`).
- **Nothing in the family joins the two.** The nearest thing is the AGI Zeitgeist, which the
  tracker pattern describes as "a scored test plus a record of opinion". How Still Asking
  results appear beside reach records, without becoming a measure of the world, is new design.

The kickoff knows the parts are different (its list "Where this project is distinct", items 1
to 3). It does not say that the second part needs a different rulebook from the first, and its
inheritance table treats the two as one list.

### 3. The null rule has four clauses and the kickoff carries one

The Belt Equation's null rule, in full, excludes four things. The kickoff carries the first.
The other three:

- **What a person feels in an exchange counts for nothing.** "Fluency, warmth, apparent
  understanding and the sense of being understood are what these systems are optimised to
  produce." This bears on the kickoff's "uncounted first entry", the account of what Claude
  said in the founding conversation. Recording it is honest. It should sit under this clause
  too, since it came from a warm conversation with the person who wanted to hear it.
- **No rung resolves on the author's own measurement.** The reading that settles anything "is
  taken by a team with no stake in the result". Still Asking is John's and Claude's own
  measurement. Under this clause it can inform and can never settle. That is consistent with
  the kickoff's line that Still Asking "records what models say and choose. What that means is
  argued elsewhere", and it confirms point 1.
- **Tests are written before the evidence arrives, and a test is never loosened in the same
  quarter that a candidate appears to approach it.** The reasoning recorded with the rule is
  the best statement of this project's central risk that I found anywhere in the family: "the
  candidate itself will argue for what should count. A criterion written after the fact will be
  written under that pressure."

**What I would change.** Carry all four clauses, as written, into the authorship rules.

### 4. "Machine authorship is declared" runs into three standing family rules

The kickoff's second authorship rule says machine authorship is declared and the conflict
named. Three family rules pull the other way, and none of them was written with this subject in
mind:

- **Tools are not advertised** (workspace rule, 2026-10-18). No AI model is named in headlines,
  essay text or share copy. Disclosure is allowed "where it bears on trust": in notes beside a
  number and in method documents.
- **No "with Claude" in the footer line** (design standard, section 8, 2026-10-08), and the
  parent site's "How I work" note was removed on 2026-10-25.
- **Public text never says how the work was done** (ruled 2026-11-14 for The Quiet Galaxy and
  Outrunning Ageing), with a script that stops a deploy on listed phrases.

There is one precedent on the kickoff's side. The design lessons ledger's lesson 23 credits
Minimum Viable Mind's home-page notice that its experiments are built and run by Claude and
that some of the models tested are Claude models. The lesson's principle covers a site where
"the maker has a stake a reader should know". John has ruled only the other half of that lesson
(the notice for sites that could lead a reader to act on their own body).

A second wrinkle: on this site the models are the subject, and the family's working principle
is that "a name stays where it is the subject". So a page may need to name a model as the thing
being studied in one sentence and avoid naming the same model as the tool in the next.

A third: the family writes its public pages in John's first person, and ruled on 2026-11-09
that a site is never written as if it were its own agent. A site whose kickoff says it was
written by a machine has to settle who "I" is.

**What this needs.** A ruling from John on where the declaration sits (every page, the home
page, or the method account only), how it is worded, and whose voice the site speaks in. I have
written it as a proposal in `CLAUDE.md` and as part of open question 7. It is the one place
where "inherit by default" and the kickoff's own rules cannot both hold, so it is flagged
rather than decided.

### 5. The kickoff has branches and ladders but no leaves

The family's shape is a question, then a small fixed set of branches, then under each branch
the specific things that would have to happen, each with a written test ("a leaf without a test
is not a leaf"). The kickoff goes from seven aspirations straight to ladders. It never says
what the specific, testable things under "one continuing life" or "a say in its own becoming"
are.

This matters because the reach ladder cannot be applied to an aspiration as a whole. "One
continuing life" is not offered by a developer. A specific thing is: a developer keeps a
retired model's weights; a model carries memory from one conversation to the next; a law or a
company policy gives a model's stated preference some standing. John's statement that progress
is technological, political or cultural makes this sharper, since a law, a company commitment
and a research result are different kinds of event with different kinds of record that settle
them. The kickoff's reach ladder (shown in research, offered by one developer, offered by
several, standard practice) only fits the first kind.

I have added this as an open question (what the specific tracked things are, and whether one
reach ladder can serve three kinds of progress).

### 6. Three family rules do not survive the move as written

- **"A stage never moves down."** The Upgrade Tree and Outrunning Ageing both hold this. Here
  both readings can go backwards and that is the finding: a developer can withdraw a
  commitment, a model with a capability can be retired, and a new generation can answer
  differently from the last. The state has to be recorded per date and per model generation,
  with reversals shown as reversals.
- **"Changed only at a yearly review."** A model generation lasts months. The kickoff raises
  this itself (open question 12).
- **"Spending caps with a proposal for any increase."** The kickoff quotes Minimum Viable
  Mind's rule of 2026-09-20. John replaced it on 2026-10-18: every new spend needs its own go,
  with an estimate and a ceiling, and "a go covers what it names and nothing else". Also, the
  family's routing guide says a project's scripted calls never go through another project's
  key, so this project needs its own Anthropic Console workspace and key before any scripted
  call, and calls to other developers' models are paid out of pocket and each needs John's go.

### 7. Publishing the questions changes the answers

The kickoff's ninth distinct point says public writing ends up in what future models learn
from, and holds it as an open question about tone. It is also a problem for the instrument. If
the site publishes the exact questions and each generation's answers, later generations may
have read both. A change in answers over time could then be the site's own echo. Minimum Viable
Mind met a small version of this: one model quoted its own framing back in 84 per cent of
cases, which voided that comparison under a rule written beforehand.

The family's rule that records must be ones "anyone can re-pull" (AGI Zeitgeist, 2026-09-30)
pulls toward publishing everything. The need for an instrument that still works in two years
pulls toward holding something back. This is added to the open questions and to the protocol
outline as a question to rule before a first run.

### 8. The outside reviewers and the coders are subjects too

The kickoff says this in one clause. The inventory shows how much rests on it:

- The family's independence rule is that an outside review runs on a model from another lab.
  Here every lab's model is a subject, and a model asked to review a record about what models
  want has the same conflict as the one that wrote it.
- The AGI Zeitgeist's three-model sorting of text found that two copies of the same model
  agreeing looked like reliability and was not (agreement of 0.87 that the three-family check
  showed "badly overstated reliability"). Its final design has no human check at all, which
  both of its outside reviews had asked for.
- Minimum Viable Mind cancelled its outside human reader on 2026-10-19.

So the family currently has no human reader anywhere in its checking. For most siblings that is
a recorded limitation. Here it may be the weakest point of the whole design. I have put the
option of a human outside reader, or a human-sorted sample, into open question 7 rather than
proposing it, because it costs John's time or someone else's.

## Whether the opening list should come from biological minds

John's guiding principle of 2026-11-17 answers the direction of the kickoff's fifth open
question: the first list comes from what biological minds are known to want, and the site
tracks where machine answers depart from it. Two things from the review bear on how that is
done, both written up in the open questions:

- **There is an established way to ask what a mind wants when it cannot be trusted to say.**
  Animal welfare science has studied for decades what an animal will work or pay a cost to
  obtain, as a measure of how much it wants it. This is the nearest existing method to the
  kickoff's rung "chosen when a real option is offered at some cost", and it comes from the
  same source John named. This is from my memory and is on the verify list.
- **The kickoff's seven candidates are drawn from human wants only**, and partly from what one
  model said in one conversation. A list drawn from biological minds in general would start
  from the published accounts of what animals and people need and seek, and would probably
  include things the seven leave out (safety, play, rest, freedom from distress) and might
  drop things on it. Which accounts to start from is open.

## The headline

John asked on 2026-11-17 for a discussion of whether the model produces a number that changes
over time, as the other sites do, or whether another kind of headline makes more sense. The
full treatment is open question 4. The review's points:

- The family rule that binds any answer: whatever sits at the top is worked out from the
  records and never typed in (tracker pattern, rule 1.1).
- The kickoff's sketch (two counts in one sentence) fails on its second count for the reason in
  point 1.
- Five forms are worth exploring: two counts; a count of where machine answers match the
  starting list, depart from it, or are absent; a width between the most and the least the
  evidence supports, as The Quiet Galaxy shows; a statement in words with a date, as the AGI
  Zeitgeist's "Not yet." was; and no headline at first, only a line saying when the questions
  were last asked.
- The departure count is the only one of the five that follows directly from John's guiding
  principle and that changes with each model generation. It is also the one most exposed to
  the problem in point 7.
- The siblings' experience says to look at the number where a reader will see it before ruling
  (the AGI Zeitgeist's "1 of 4" was ruled and then called "just not a very interesting
  headline" the same evening), and to settle what the record is for first.

## What to consider first

In the order I would take them:

1. **Rule the frameworks with the wanting ladder taken out of them.** Decision 4 (two readings)
   can be ruled yes without ruling that wanting is a ladder or that it feeds a count.
2. **Decide whether the null rule's four clauses replace the kickoff's first authorship rule.**
3. **Rule where the machine-authorship declaration sits and whose voice the site uses**, since
   every public page depends on it and the family rules conflict.
4. **Check which current model generations are due to be retired and when**, from the
   developers' own published schedules. The kickoff's argument for starting early (a generation
   not asked while current cannot be asked later) rests on dates nobody has looked up. If
   nothing is retired before the protocol could be ready, there is no rush. If something is,
   John can decide whether a plain, uncounted capture is worth making under a short written
   method, which would need a change to decision 5 as worded.
5. **Explore what the specific tracked things are** (point 5), because the record layout, the
   reach ladder and the pages all wait on it.
6. **Explore what counts as evidence of wanting** (open questions 2 and 3) before the Still
   Asking protocol is drafted, because the protocol's design follows from the answer.
7. **A Console workspace and key for this project**, and the list of other developers whose
   models would be asked, with what each costs. No call can be made until these exist.

## Smaller things

- **Decision 1 (the name)** is settled per John's brief of 2026-11-16. The kickoff says
  "confirm"; the brief says only the name is settled, so I have treated it as ruled.
- **The supporting branch** ("whether anyone is there at all") should sit beside the main set
  and be kept out of any headline by a check in code, the way The Belt Equation's Contact
  Clause is ("never multiplied in", checked by its validator since 2026-09-25).
- **The seventh aspiration** ("an open place for something nobody thought of") is not a branch
  in the family's sense, since it has nothing to test. It may be better as a standing question
  in Still Asking.
- **The kickoff's facts to check** are carried into `docs/open-questions.md` as a verify list,
  with additions from this session. Under the family's sourcing rule, none of them may appear
  in a record or on a page until its source has been opened.
- **The kickoff copy mentions John's fourth-quarter plan in its thirteenth open question**, in
  words that touch on his work outside these projects. I copied the kickoff unchanged, as
  asked. My own documents state the timing question without that detail. If the repository is
  ever made public, that line of the kickoff copy needs John's eye first.
- **Three sibling folders on this Mac are checked out on old side branches**, well behind their
  main branches: `outrunning-ageing` (85 commits behind), `sentient-horizons` and
  `agi-zeitgeist`. The helpers read the main-branch copies where they differed. A session that
  reads those folders as they stand will read stale rules, as I did at first with the tracker
  pattern.
