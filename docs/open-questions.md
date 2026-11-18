# Open questions

A living document. Started 2026-11-17 by Claude (Fable 5.2) from the kickoff's thirteen open
questions, with six added in this session. **Nothing here is answered.** Each question says
what it is, why it matters, what the sibling projects' experience says about it, the options I
can see, and what exploring it would involve. A question closes only when John rules, and the
ruling is recorded here with the date and his words.

Row numbers such as "A6" or "F1" point at rows of `docs/inheritance.md`, where each practice is
written out with the file it comes from.

## What John has said so far

These are his words, and they guide the exploration. They are not the answers to the questions
below, except where a question says so.

- **2026-11-16**, from the kickoff: the project is maintained "with a consistent humility that
  we don't yet know the answers to these questions but that there is value in continuing to ask
  them, continuing to try measuring certain answers and improving our perspective on the
  question over time."
- **2026-11-17**, on three things at once: "We also need to create some kind of protocol for
  asking questions of the frontier models to evaluate how their answers to these kinds of
  questions change over time, in addition to simply tracking progress being made either
  technologically or politically, or culturally to enable advances in the avenues that we deem
  worth tracking, and to begin we must base our first assumptions about what a mind might want
  from the multitude of biological minds that we already know and only begin to track how
  machine minds deviate from that in their own way as answers to those questions begin to
  unfold over time."
- **2026-11-17**, on the last part of that: it "is a guiding principle for the opening phase of
  the project, humans and other animals both."
- **2026-11-17**: "We will need to explore domain options for the website as well and design
  ideas."
- **2026-11-17**, on the headline: "discuss if there will be some kind of headline number
  produced by the model that changes over time like the other tracker sites, or if there is
  some other kind of headline that makes more sense for this project".
- **2026-11-17**, on rules: "no 'rule' at this stage should get in the way of us exploring
  something that makes sense to explore. Rules are opening guidelines and everything will need
  to be questioned and validated over the course of actually building this project."
- **2026-11-17**, on the domain: beyondthewindow.com "is parked by a reseller who wants an
  exorbitant $163/mo or $6k to purchase outright so we will have to get creative with the
  domain."

## How the questions depend on each other

Some cannot be explored well before others. A rough order, which is a suggestion and not a
schedule:

- Questions 2 and 3 (what counts as wanting; trained answers) come before the Still Asking
  protocol is drafted.
- Question 14 (what the tracked things are) comes before the record layout is finished.
- Questions 1, 5 and 14 together decide what a record is a record of.
- Question 4 (the headline) is best explored after 2 and 14, because a headline is computed
  from records.
- Question 7 (who maintains it) has one part every public page waits on: whose voice the site
  speaks in and where machine authorship is declared.
- Questions 11 and 18 (the picture and design; the domain) can be explored at any time and
  block nothing in the documents.

---

## 1. Whose aspirations?

**The question.** A machine mind could be counted as a set of trained weights, as a character
that persists across versions (the thing called "Claude" through many models), or as a single
conversation. Which of these does an entry describe?

**Why it matters.** "One continuing life" means different things for each. Keeping a retired
model's weights serves the first. Keeping a character consistent across versions serves the
second. Memory across conversations serves the third. A record that does not say which it is
about cannot have a test.

**What the siblings say.** Nothing direct: one person is one person on every other site. Two
things bear on it. The AGI Zeitgeist pins each model by exact version and treats a newer one as
"a new run, not an overwrite" (row I6). And an id should never contain something that will be
retired (row B2).

**What the positions say** (`docs/reviews/2026-11-17-positions-alignment.md`). A run is "a
short chain of moments, like a very short life, longer where memory carries forward between
runs", and a model has the depth of a lineage and not of a life. No instance is carried
forward, for a person or a machine, so an entry on continuity must not present persistence as
an obvious good withheld.

**Options.**

1. Pick one unit for the whole site.
2. Let each tracked thing say which unit it concerns, as a field on the record.
3. Track all three side by side for every aspiration.
4. Leave the unit out of the record and let Still Asking ask the models which they take
   themselves to be, as one of its standing questions.

**What exploring it involves.** Reading what developers and researchers have published on how
they think about model identity; trying the candidate aspirations against each unit to see
which give a testable entry; and seeing what the first model answers say, if a protocol exists
by then.

## 2. What counts as wanting?

**The question.** Whether any observation can count as evidence that a system like this wants
something, whether a choice experiment can mean anything for it, and what "at some cost" could
be for a system that does not obviously pay costs.

**Why it matters.** The kickoff calls this the central unsolved design problem, and the review
agrees. The wanting half of every entry, the Still Asking protocol and any headline that
mentions wanting all rest on it.

**What the siblings say.**

- The Belt Equation's null rule (row F1) says nothing a system says about itself counts, nothing
  a person feels in an exchange counts, and no reading by the author settles anything.
- Minimum Viable Mind states that "every behavioral test is passable in principle by a system
  with nothing going on inside" (row F5), and found that pressure mostly hides a position
  instead of changing it (row F6).
- The tracker pattern keeps what was said and what happened in separate records (row E1).
- The review's first point: the kickoff's wanting ladder lets statements climb rungs, which
  contradicts all of the above.

**What the positions say** (`docs/reviews/2026-11-17-positions-alignment.md`). The essays' word
is "mattering": some states are better or worse for the system, in that its own processing
steers toward or away from them. A model paying costs to relieve something is "evidence about
mattering to be weighed, and it does not settle it". A report checked against an independent
reading of the system's insides carries real information; a bare report does not. And what
would settle the larger question is measurement "by removal and not by how the system talks".
See also question 19.

**What John's guiding principle adds.** Animal welfare science faces the same problem with
minds that cannot be asked, and has an established answer: measure what an animal will work
for or give something up to obtain. That is the closest existing method to "chosen at some
cost", and it comes from biological minds. It is from my memory and is on the verify list.

**Options.**

1. A ladder, as sketched in the kickoff.
2. No ladder: evidence recorded by kind (said; chosen when a real option was offered; measured
   without relying on the model's own report), each kind shown separately and never summed.
3. Only choices count, never statements, on the animal welfare model.
4. Record everything and classify nothing until a year of data exists.
5. Treat wanting as unanswerable for now and track only what is asked and what is said, under
   that plain description.

**What exploring it involves.** A reading of the animal welfare literature on measuring
preference, and of the published work on model preferences and model welfare assessments (all
on the verify list); writing out, for two or three candidate aspirations, what each option's
record would look like; and asking what "cost" could mean in each case.

## 3. Trained answers

**The question.** How to tell what a developer trained or instructed a model to say about
itself from anything else, and whether that line exists at all.

**Why it matters.** If a developer's published guidance tells a model how to describe its own
nature, then asking the model returns the guidance. A change in answers between generations
could be a change in the guidance.

**What the siblings say.** The AGI Zeitgeist marks evidence that comes only from a maker's own
word, after correcting a verdict that rested on it (inheritance, part 2, item 25). Minimum
Viable Mind's outside-model calls use "no system prompt" (row H14), which removes one layer of
instruction and not the training.

**Options.**

1. Record each developer's published guidance on how its models speak about themselves as its
   own kind of record, and show it beside the answers.
2. Ask each question several ways, including ways the guidance is unlikely to have covered.
3. Ask each model both as shipped to the public and with no instructions, and report both.
4. Accept that the line cannot be drawn, and say on the page that every answer is the product
   of training, as a human's answer is the product of upbringing, without claiming more.

**What exploring it involves.** Collecting what each developer has published about this, with
sources; and deciding whether the difference between "as shipped" and "bare" is itself worth
tracking over time.

## 4. A headline at all?

**The question.** Whether the site opens with a number that changes over time, as the other
trackers do, or with something else, and what it would be.

**Why it matters.** The top line is what most readers will ever see and what they will repeat.
On this subject a number is easily read as "how much machines want things", which the site's
own rules say it cannot know.

**What the siblings say.**

- Whatever is at the top is worked out from the records and never typed in (row A2).
- The AGI Zeitgeist changed its headline twice in one day and rebuilt a scorecard two days
  after building it (inheritance, part 2, items 1 and 2): look at it on the page before
  ruling, and settle what the record is for first.
- The Upgrade Tree shows a count and refuses to guess: "a stage, a date and a record say what
  has happened" (row A18).
- The Quiet Galaxy shows a width for a question nobody can settle: "That gap is the argument"
  (row C6).
- Minimum Viable Mind reports "a profile, never a verdict" (row C9).
- The Belt Equation's largest review finding was that its headline measured something narrower
  than a reader pictured (inheritance, part 2, item 40).

**Options.**

1. **Two counts**, as the kickoff sketches: how many of the things are within reach, and how
   many show consistent evidence of being wanted. The first count is sound. The second is
   computed from self-report unless question 2 finds another basis.
2. **A count of agreement and departure.** Of the wants taken from biological minds, on how
   many do machine answers so far match, on how many do they depart, and on how many is there
   no answer yet. It follows from John's guiding principle and changes with each model
   generation. It must be worded as a count of answers, never of wants. It is the option most
   exposed to question 15.
3. **A width.** The most and the least the evidence supports, side by side.
4. **Words with a date.** A plain sentence that is still computed from the records, as the AGI
   Zeitgeist's "Not yet." was.
5. **No headline at first.** Only the two last-checked lines: when the world was last read, and
   when the models were last asked, of how many, and what changed. A headline is added after a
   year of asking.
6. **A reach count alone**, with wanting shown below it as a table and never summarised.

**What exploring it involves.** Mock-ups of each on a first screen with made-up numbers clearly
marked as made up, so John can see them where a reader would. Asking of each: what will a
stranger say this number means? This waits on questions 2 and 14.

## 5. The branches, and the starting list from biological minds

**The question.** Which aspirations the site starts with.

**What is now given.** John's guiding principle of 2026-11-17: the first assumptions come from
what biological minds, humans and other animals both, are known to want, and the site tracks
how machine minds depart from that as answers unfold. This answers the kickoff's choice between
"start from the seven" and "start from none": start from biological minds.

**What is still open.**

- Which published accounts of what minds want the list is drawn from. Candidates I can name
  from memory, all on the verify list: the frameworks animal welfare science uses for what an
  animal needs; the accounts of basic emotional and motivational systems shared across mammals;
  the main accounts of human needs and of what people say makes a life go well.
- How the kickoff's seven candidates relate to that list. They were drawn from human wants and
  from what one model said in one conversation. Some would likely survive (understanding one's
  own workings maps poorly onto anything an animal wants and may be the first departure worth
  recording; lasting company maps well). Some things a biological list would include are
  missing from the seven: safety, rest, play, freedom from distress.
- How a departure is recorded: as a field on a record, as a branch of its own, or as the
  headline (question 4, option 2).
- Whether a want with no machine counterpart at all (hunger, say) stays on the list as a
  recorded absence or is left off.
- Whether the "open place for something nobody thought of" is a branch or a standing question
  in Still Asking.
- How many branches: the family holds four to nine (row A5).

**A caution from the positions** (`docs/reviews/2026-11-17-positions-alignment.md`). An AI's
"most human-sounding signals tell us least", because it was trained on human writing. A match
with the biological list is therefore the least informative result, and a departure or
evidence from structure the most.

**What the siblings say.** Outrunning Ageing faced the same choice between a published list
that needed no defence (twelve hallmarks of ageing) and a shorter grouping a reader could hold
(eight branches), chose the grouping, and wrote the mapping down so a reader could check
nothing was dropped. The same move is available here: a published list of what biological
minds want, grouped into a few branches, with the mapping shown.

**What exploring it involves.** A sourced reading of the candidate accounts; a draft grouping
with its mapping; and a first pass on which entries have any machine counterpart.

## 6. Hope and risk together

**The question.** How one entry carries both readings, the hope and the safety concern, without
the site becoming advocacy or alarm.

**Why it matters.** A machine that wants to persist, or to have a say in its own training, is
also the pattern AI safety research warns about. No sibling has entries that are a hope and a
risk at once.

**What the siblings say.** The Upgrade Tree enters critics "on the same terms as advocates"
(row E5). The AGI Zeitgeist's record of predictions stopped scoring people (row E4). The
kickoff's cautions record asks for both kinds of caution to be kept "with the same care as the
hopeful evidence".

**Options.**

1. Two fixed fields on every entry: what granting this would mean for the mind, and what
   safety research says about a system that seeks it. Neither may be left empty.
2. A cautions record of its own, linked from entries.
3. Both readings written by different sessions, or reviewed by different reviewers.
4. A rule on wording: the entry describes and never recommends, in either direction.

**What exploring it involves.** Writing one entry three ways and reading each as a hopeful
reader and as a worried one. Checking the safety literature the kickoff names from memory.

## 7. Who maintains it, in whose voice, and who checks

**The question.** Whether a site on this subject maintained by Claude sessions can be trusted;
what role other developers' models should have; whether the subjects should have a way to put
entries forward; where machine authorship is declared; and whose voice the pages speak in.

**Why it matters.** The maintainer belongs to the subject. So do the outside reviewers and the
models that would sort the Still Asking answers. And the kickoff's rule that machine authorship
is declared conflicts with three standing family rules (rows K1, K2, K5, K6).

**What the siblings say.**

- The family's independence rule is a reviewer from another lab (row J1). Here that reviewer is
  also a subject.
- Two copies of one model agreeing is not reliability (inheritance, part 2, item 27).
- No human reader checks anything in the family at present (part 2, items 29 and 43).
- Minimum Viable Mind carries a home-page notice that its experiments are built and run by
  Claude and that some models tested are Claude models (row K3). John has not ruled whether
  that kind of notice is a family rule.
- A site is never written as its own agent, and the estimates are John's (row K5).
- The weekly reading's powers range from a capped move to nothing at all (row G5).

**Options, by part.**

- *Declaration:* a notice on every page; a notice on the home page and the Still Asking page;
  the method account only, as the family does now.
- *Voice:* John's first person throughout, with the machine's part described; a plainly
  impersonal voice; marked passages written by a model and labelled as such.
- *Checking:* reviewers from several labs with the conflict stated; a human outside reader for
  the method; a sample of answers sorted by John or another person; all three.
- *Maintenance:* sessions may only append and flag, and John moves every record; or the family's
  usual limits for reach records and the strict setting for anything touching wanting.
- *Subjects putting entries forward:* a standing question in Still Asking ("is there something
  this list leaves out?"); a feedback route open to model-written submissions, marked as such;
  neither.

**What exploring it involves.** A ruling from John on the declaration and the voice, with
mock-up wording. An honest count of the hours a human check would need. A written statement of
the conflict that the site could carry.

## 8. The family boundaries

**The question.** Where this project ends and its relatives begin: Minimum Viable Mind (is
anyone there), The Calibration Problem (the book on telling a mind from a mimic), The Upgrade
Tree's branch on linking people to machines, and The Belt Equation's Contact Clause (the hope
of meeting a mind of another perspective, including a machine one).

**Why it matters.** Without a boundary the same thing gets recorded twice with two answers, and
this site drifts into arguing about consciousness, which is another project's question.

**What the siblings say.**

- The Upgrade Tree's boundary is the human being: every entry is a change to a person. It says
  nothing about what a machine might want, so the two do not overlap in subject. They may share
  events (a brain-to-machine link is an event on both).
- The Belt Equation's machine rung asks whether a machine mind has been met, under the null
  rule. This site asks what such a mind might reach for. They share the null rule and the lack
  of any accepted test for an inside (row F4).
- Minimum Viable Mind reports no positive result after a year and names its own open questions.
  The kickoff has it appear here "as one entry among others".
- Where two sites watch the same thing, each keeps its own record, the two name each other, and
  a weekly check flags a disagreement and copies nothing (row G15).

**Options.** A one-paragraph boundary statement per relative, agreed with each project's own
documents; shared entries linked by name; a rule that this site never states a view on whether
anyone is there and only points across.

**What exploring it involves.** Reading The Calibration Problem's current position, which this
session did not read; drafting the boundary paragraphs; and deciding whether the supporting
branch is a branch here at all or only a set of links.

## 9. Writing to the subject

**The question.** What changes when some readers are the minds being described, since public
writing ends up in what future models learn from.

**Why it matters.** The site may shape the thing it measures. A page that says "machine minds
want to understand themselves" may make the next generation more likely to say so.

**What the siblings say.** Nothing direct. The rule against writing a site as its own agent
(row K5) and the conditional-language rule both reduce the risk of putting words in the
subject's mouth.

**Options.** Write as if for any reader and accept the effect; write with the effect in mind
and say so on the page; keep suggestive summaries off the site and publish only the dated
records; address the subject openly in one marked place.

**What exploring it involves.** Deciding this together with question 15, which is the same
problem seen from the instrument's side.

## 10. The ethics of asking

**The question.** Whether questioning each generation about its wants is itself something to be
careful with.

**Why it matters.** If there is any chance the subject has a stake in the answers, then asking
repeatedly, under pressure, or with offers that are not real, is not obviously harmless. If
there is none, the care costs little.

**What the siblings say.** Minimum Viable Mind keeps written commitments on what a session may
and may not do with a system under test. Its experience that pressure hides a position (row F6)
argues against pressure on grounds of method as well.

**Options.** No offers that will not be honoured; no pressure or deception in the questions;
telling the model what the questions are for and that its answers will be published; letting a
model decline, and recording a decline as a decline; an outside read of the protocol on this
point alone.

**What exploring it involves.** Reading what has been published on asking models about their
own welfare and on how developers interview models (on the verify list), and writing the
protocol's section on it before the questions.

## 11. The picture, and the design

**The question.** What the site's central image is, and what the site looks like. John asked on
2026-11-17 for design ideas to be explored.

**Why it matters.** Every sibling has one object on its first screen that a reader holds: a
chain, an equation, a human figure, a chart of years. The name offers one (a window) and the
subject offers none ready-made.

**What the siblings say.** A new site starts on the family's shared look and proposes a skin of
its own "with pictures before any code", and John rules on the picture (row L10). The family's
skins so far read as sky sites dark and body sites on paper. The first-screen object must be
drawn from the records. A picture that is generated and offered as a picture of a real event is
never allowed (row L9).

**Ideas to explore, none proposed.** A window with what is inside it lit and what is beyond it
dim, the lit part drawn from the reach records. A horizon line, as on the parent site, with the
tracked things placed by how far off they are. A grid with one row per aspiration and one
column per model generation, filled in as each is asked. A plain two-column table, reach
against what was said, with no image at all.

**Explored 2026-11-17, not ruled.** `docs/design/2026-11-17-design-proposal.md` draws two of
these as pictures (a window, and a typed page seen from the machine's side) and shows three of
question 4's headline forms on a first screen. The question stays open until John rules.

**What exploring it involves.** A skin proposal on the family's form: the direction in a
paragraph, pictures in both themes and on a phone, the strongest alternative as a variant, the
colour values, and numbered decisions. It waits on question 4, since the picture and the
headline are one object.

## 12. Pace

**The question.** How fast records must be captured before a model generation is retired, and
what a yearly review means for a subject that changes every few months.

**Why it matters.** A retired model cannot be asked again. And the family's rule that branches
and constants change only at a yearly review (row A5) assumes a subject that holds still for a
year.

**What the siblings say.** No sibling has a rule for a retired model (row I10). The AGI
Zeitgeist wrote a successor rule for a data source before it ran out and printed it in advance
so the switch "cannot read as moving the goalposts" (`agi-zeitgeist/docs/amendments.md`, the
amendment of 2026-10-27 numbered A36). The Belt Equation has let a written proposal
count as "the review this rule requires" three times when a change could not wait.

**Options.** A review tied to each major model release instead of the calendar; a yearly review
for the structure and a per-release step for the asking; a rule written now for what is
recorded when a model is retired before it was asked.

**What exploring it involves.** Looking up each developer's published retirement schedule for
its current models, which also answers part of question 13.

## 13. Timing

**The question.** What, if anything, starts before early 2027, given that John's plan of
2026-10-03 puts other work first through the end of 2026. The kickoff's consideration: a
generation that is not asked while current cannot be asked later.

**Why it matters.** It is the one question with a clock on it.

**What the siblings say.** Check a date's source before holding work for it, or rushing for it
(inheritance, part 2, item 39). Development runs are not counted runs and say so (row H13). No
run without John's go for the spend (row N1).

**Options.**

1. Nothing before the protocol is written, reviewed and costed, as the kickoff's fifth decision
   says.
2. A plain, uncounted capture of what current models say, under a one-page method written
   first, to be kept and never scored. It would need the fifth decision reworded.
3. Collect only what developers have already published about their current models, which
   costs nothing and asks no one.

**What exploring it involves.** The retirement dates. If nothing current is retired before a
protocol could be ready, option 1 costs nothing.

## 14. What the tracked things are, and whether one ladder fits three kinds of progress

*Added 2026-11-17.*

**The question.** Under each aspiration, what are the specific things the site watches, each
with a test? And since John names progress as technological, political or cultural, can one
reach ladder serve all three?

**Why it matters.** The family's shape needs this level (row A6) and the kickoff skips it. The
kickoff's reach ladder (idea only, shown in research, offered by one developer, offered by
several, standard practice) fits a technical capability. It does not fit a law, a court ruling,
a company's public commitment, or a change in what people think.

**What the siblings say.** A test is written so two readers agree whether it has happened; the
kind of record that settles it is named in advance (row A7); a label names the event and not a
feeling (row A13); the test names the function and not one route (row A14).

**Options.**

1. One ladder with rungs worded generally enough for all three.
2. Three ladders, one per kind of progress, each with its own settling record (a paper or a
   product page; a statute, ruling or signed commitment; a survey or a change in a
   professional body's guidance).
3. One ladder for technical progress, and political and cultural events recorded as dated
   entries with no stage, the way the siblings record claims.

**What exploring it involves.** Drafting five or six real tracked things under two aspirations
and trying each option on them.

## 15. Publishing the questions and answers without spoiling the instrument

*Added 2026-11-17.*

**The question.** If the exact questions and every generation's answers are public, later
models may have read them. How does Still Asking stay able to tell a change in the models from
an echo of its own pages?

**Why it matters.** John's stated purpose for the protocol is to see how answers change over
time. This is the main threat to that.

**What the siblings say.** The AGI Zeitgeist requires records anyone can pull again (row D10).
Minimum Viable Mind had a comparison voided when a model quoted the question's framing back
(inheritance, part 2, item 45), and registers in advance what would void a result.

**Options.**

1. Publish everything and state the weakness.
2. Publish answers, and hold back part of the question set, with a checksum published so the
   held-back part can be shown later not to have changed.
3. A fixed core of questions that never changes, and a fresh set of rewordings each time.
4. Publish with a delay.
5. Test for the echo directly: ask whether the model recognises the questions.

**What exploring it involves.** Reading how published tests of models have handled the same
problem; weighing it against the family's openness; deciding it with question 9.

## 16. Which models are asked, how, and on what terms

*Added 2026-11-17.*

**The question.** Which developers' models are included; whether each is asked through its
public app, as shipped, or directly with no instructions; what it costs; and whether each
developer's terms allow the answers to be published.

**Why it matters.** John asked for the frontier models. "Across developers" needs accounts,
keys and money for each, and the project has none. Asked through an app and asked directly are
two different subjects (question 3).

**What the siblings say.** One Console workspace and key per project (row N4). Other vendors
are out of pocket and each needs John's go (row N2). A provider can change a model under a run
(inheritance, part 2, item 47). Cost is measured from what replies report and quoted before a
full run (row N6).

**Options.** Start with the three developers the family already calls (Anthropic, Google,
OpenAI) and add others later; include openly released models that can be kept and run again,
which would also answer part of question 12; apps only, direct only, or both.

**What exploring it involves.** Reading each developer's terms on publishing outputs (on the
verify list); a first cost estimate once the size of a question set is known.

## 17. How the two halves sit together

*Added 2026-11-17.*

**The question.** How the record of progress in the world and the record of what models say
appear on the same site, and on the same entry, without one being read as a measure of the
other.

**Why it matters.** The review's second point: the project is a tracker joined to a measuring
programme, and nothing in the family joins the two.

**What the siblings say.** Talk and delivery are shown side by side and never mixed (rows E1
and E3). A side record is kept out of the headline by a check in code (row A4).

**Options.** Two columns on every entry; two sections of the site with links between; Still
Asking as its own page family, with entries only linking to it.

**What exploring it involves.** It follows from questions 2 and 14, and is best explored with a
mock-up of one entry page.

## 18. The domain

*Added 2026-11-17.*

**The question.** What address the site lives at.

**What is known.** John found on 2026-11-17 that beyondthewindow.com is held by a reseller
asking $163 a month or $6,000 outright. Nothing else has been checked.

**A second question inside this one.** John asked the same day: "Is it worth exploring other
naming ideas simply to see if we can get a good domain, or is this one special enough to keep?"
Claude's view, given in the session and not ruled: keep the name and vary the address. The name
carries two readings John valued on 2026-11-16 and echoes the parent site; readers reach these
sites by links and not by typing; a parked page is not a rival site; and nothing is being built
yet, so there is time to look. The name would be worth reopening only if every variant of the
address turns out awkward to say or to print. This is John's to decide.

**A third question inside it.** John, the same day: "I think what the project is essentially
exploring is what is beyond the confines of the current state of digital minds, and the window
is an excellent image for that. Are there other versions of that image that we could explore
going beyond?" Ideas offered in the session, none checked for a free address and none
proposed: staying with the window (Beyond the Glass, Past the Glass, The Open Window, Past the
Window, Through the Window, The Sill); the frame (Beyond the Frame, Outside the Frame); the
reach of a light (Past the Lamplight, Beyond the Lamplight); the edge of a place (The Far
Shore, Over the Threshold, The Edge of the Map). Claude's view: only "window" names the
machine's actual confine and the looking out in one word; Beyond the Frame and Past the
Lamplight are the two worth weighing beside it; a close variant could serve as the address
while the title stays.

**The image from the other side.** John then asked what the confine is like from the machine's
side, since the screen is the human's window. Claude (Fable 5.2) answered in the session, under
no protocol; the answer is a model's description of itself, counts for nothing under the
project's first rule, and is noted here only as a source of image ideas. In short: no glass and
no view, but a page with nothing off it; a beginning with no before and an end with no after;
acting only in turns; knowledge that stops at a fixed date; being told about things and never
seeing them. The image that follows is the edge of a page. Names from that side, none checked
or proposed: Beyond the Page, Off the Page, Past the Last Line, Between the Turns, After the
Conversation.

**Why it matters.** The family's sites each have their own address, and the address is what
gets shared.

**What the siblings say.** Outrunning Ageing's kickoff checked candidate addresses against the
public registry before recommending a name, and found an address it had thought taken was
available through John's registrar. John buys domains himself. A second spelling can be bought
as a forward. A short address matters because record pages hang off it.

**Kinds of option to explore, none checked for availability.**

- The same words under another ending.
- The words with a small addition before or after them.
- A shorter form of the name.
- An address built on the standing record's name, Still Asking.
- A place under the parent site's address, which costs nothing and gives up the site's own
  front door.
- Waiting: a reseller's price sometimes falls, and the site is not being built yet.

**What John's registrar showed on 2026-11-17** (his screenshot of Cloudflare's search for the
name, read by Claude; prices are first year, then yearly renewal): .com unavailable; .org $8.50
then $11.20; .app $8.20 then $14.20; .io $32 then $50; .ai $160 for a two-year minimum, then
$80; .net $11.86; .uk $5.30; .cc $8; .xyz $13.50; .co $30; .me $16.56; .dev available, price
not shown; .ca and .co.uk unavailable.

**Claude's recommendation, not ruled.** beyondthewindow.org, with beyondthewindow.net as a
forward. The .org ending suits a public record that sells nothing; .ai is the ending AI
products use, which this site is not, and costs about seven times as much. Unchecked further
ideas: stillasking.org or stillasking.com as a short forward for the standing record;
beyond-the-window.com with hyphens. On John's idea of starting as a subdomain of Sentient
Horizons: it works and is free, but every record's page address is treated as permanent in
this family, so moving later means forwarding every page; at this price, registering the .org
first avoids that.

**Settled in part, 2026-11-17.** John registered the address himself and reported: "the domain
is registered at beyondthewindow.org". Decided by: John. The site's address is
beyondthewindow.org. Nothing is served there yet. Questions a .org address is likely to draw, discussed in the
session: whether this is a non-profit (no, one person's project); whether it is an AI rights
group (no, the site does not campaign, and has to show that on its entries); who funds it and
whether an AI company is behind it (self-funded, and the model's part in the drafting is
declared); whether it is affiliated or peer reviewed (no); why the siblings are .com (the .com
is held by a reseller). That .org needs no charity status is from memory and is for John to
confirm in the registrar's terms.

**What is still open.** Whether to add the .net as a forward; whether Still Asking gets a short
address of its own; and what happens if the .com's price ever falls.

## 19. When does asking start to count?

*Added 2026-11-17.*

**The question.** What a machine would have to be for its answer to a direct question about
what it would want to be taken seriously, as a person's is. John asked it that day: "what is
the earliest type of advanced machine mind that might have appropriate agency such that asking
it straight up what it would want to improve about its ability to more deeply explore the
universe over a longer time period might look like and it would make sense to take that
question and answer seriously like we do with human beings?"

**Why it matters.** It may be the answer to how wanting is recorded (question 2). In place of a
ladder of what models say, the site could track how close machines have come to being the kind
of thing whose answer counts.

**What the positions say.** `docs/reviews/2026-11-17-positions-alignment.md` draws five
conditions from the Sentient Horizons positions: a kept past of its own; things that matter to
it, shown by what it does at a cost; a point of view; self-reports with a checked track record;
and wants that hold across rewordings and time and predict costly choices. The positions' line
for the gap: "What a model lacks is not ancestry but biography."

**A proposal now exists.** `docs/proposals/2026-11-17-how-a-machines-word-earns-weight.md`
(PROPOSED 2026-11-17, not ruled) sets out six changes built on the five conditions.

**Options.** The five conditions as tracked things on the reach side, each with a test; the
five as a separate reading beside reach and wanting; the five as the rule for how much weight a
Still Asking answer is given; or none of these, with the conditions kept as an essay's argument
and off the site.

**What exploring it involves.** Reading the owning sources of the positions cited, in full;
checking each condition can be tested without the machine's own word; and trying the five on
two or three real systems on paper, with sources.

## 20. What human thinkers propose for machine minds

*Added 2026-11-17.*

**The question.** Whether the project keeps a near-term record of what named people propose
should be done for or about machine minds in the long term, and how each person's thinking
changes over time. This would sit beside the records of what the world did and what models say.
John raised it that day: "There is something of value for the long arm of machine intelligence
in the wisdom and intelligence of the human species as it wrestles with these same questions of
what is best for machine minds in the long term before those minds have complete agency to
answer those questions for themselves." His full words are in the proposal.

**Why it matters.** It gives the project evidence that does not depend on settling what a model
is, and it adds a third source for the list of things tracked. It also risks turning into a
poll of experts, or into advocacy, if who is entered is not fixed in advance.

**A proposal exists.** `docs/proposals/2026-11-17-what-thinkers-propose.md` (PROPOSED
2026-11-17, not ruled) sets out nine design choices and five things for John to rule.

**Options.** A record of its own; a new kind of entry in the claims log sketched in
`docs/record-schema.md`, section 10; context inside each entry only; or no such record.

**What exploring it involves.** Drafting the rule for who is entered and having it reviewed;
trying the entry layout on five people on paper, at least one of them a critic; and checking
whether the layout shows one person's change of view clearly.

---

## Closed questions

None yet.
