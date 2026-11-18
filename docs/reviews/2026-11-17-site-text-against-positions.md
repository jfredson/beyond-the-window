# The built site's text read against the Sentient Horizons positions

Written 2026-11-17 by Claude (Opus 5.5), in a session started by the planning session, after
John said "Yes, start both" to a read of the site's public text against the Sentient Horizons
positions record. **A reading, not a ruling.** Nothing on the site was edited. Every suggested
wording is for John or a later session to take or leave.

A model wrote this review of a site about models. The project's first guideline applies to it.

## Summary

Beyond the Window's first version (the pages in `site/` and the thirteen records in
`data/entries/` that the entry pages show) was read line by line against the positions record
of the Sentient Horizons blog: the list of positions John has ruled for the blog and the book,
kept at `editorial/corpus-positions-ledger.md` on the blog repository's `master` branch.

On the whole the site's text sits well inside those positions. It never says a model wants or
feels anything, and never says it does not. Its account of a checked self-report repeats the
blog's own limit almost word for word, and nothing on it treats a model's retirement as a harm.

There are **22 findings**:

- **4 must be fixed before publishing.** Three treat as settled something John has not ruled:
  the number at the top of the home page, where and how the site says an AI model drafted it,
  and a sentence saying John decides every test and every entry's standing, when in fact a
  session drafted them and he has ruled none. The fourth is the most serious finding about the
  positions. The site records the cost of seeing more in a model than is there, but not the cost
  of seeing less. The blog holds both mistakes to be equally real, and holds the second to be
  usually the worse one.
- **7 should be fixed.** These are a mislabelled caution, an overstatement of what nobody knows,
  a claim that the site takes no positions, a purpose read into a shutdown study, a premise taken
  from John's unruled sketch, a statement that nothing will be asked which John's own ruling has
  overtaken, and the word "evidence" used where the ruled guideline refuses it.
- **11 are notes**: places that agree with the positions and should be kept that way, and small
  points.

Nothing was found that names a tool, uses a working word, or writes the site as its own agent.

## What was read

- **The positions record**, in full: the terms (Part A), the fixed positions numbered 1 to 57
  (Part B), the questions held open on purpose (Part C), and the claims about method (Part D).
  Only the file without a "PROPOSED" suffix was used. The owning essays and chapters behind each
  position were not opened. The record itself says a position's one-line summary is a detector,
  not the position, so before a public page leans on a position named here, its owning source
  should be read in full.
- **The earlier review**, `docs/reviews/2026-11-17-positions-alignment.md`, which read the
  founding documents against the same record and found five places where they pull apart. This
  review reads the built site's own text, and does not repeat those five except where the site's
  text acts on one.
- **The site's text**: every page in `site/src/pages/` (the home page, the list, the entry page
  template, About, Still Asking, the not-found page), the layout and the four components in
  `site/src/components/`, the question and headline wording in `site/src/lib/data.ts`, the
  evidence and caution headings in `scripts/export.py`, the group names in `data/groups.toml`,
  the published number file `site/public/data/headline.json`, and all thirteen records in
  `data/entries/`.
- **For context**: the kickoff rulings (`docs/rulings/2026-11-17-kickoff-decisions.md`), the
  sealed-capture ruling (`docs/rulings/2026-11-17-sealed-capture.md`), open questions 4 and 7
  (`docs/open-questions.md`), and the list of provisional build choices
  (`docs/first-version-choices.md`).

Line numbers are those of the files on `main` at commit `c9ba747` (the commit recording John's
ruling to approach the proposed five first). Positions are cited by the record's own number with
a plain phrase, for example "position 21 (a checked self-report)".

## How to read the verdicts

- **Must fix before publishing**: the text contradicts a position, or presents as settled
  something John has not ruled. It should not go out as it stands.
- **Should fix**: the text claims more than the positions allow, mislabels something, or will
  soon be wrong. It would not embarrass the site on day one, but it should change.
- **Note**: no change needed now; either a place that agrees with the positions and should be
  protected, or a small point.

---

## Must fix before publishing

### 1. Only one of the two mistakes is recorded as having a cost

**The text.**

- `site/src/pages/about.astro:90-92`: "Two cautions are recorded beside the rest: the cost of
  seeing wants that are not there, and the worry about a system that does have them."
- `scripts/export.py:44-47`, shown on every entry page as the two caution headings: "The worried
  reading" and "The cost of seeing more than is there".
- `site/src/pages/list/[id].astro:105`: "Two Cautions ... recorded with the same care as the
  rest".

**The positions it meets.** Position 1 (the twin errors): seeing an inside that is not there and
dismissing one that is are "symmetric failures", each with a cost. Position 2 (the asymmetry of
errors): the second mistake, under-attribution, is usually the costlier and harder to undo,
except for systems whose make-up is plainly too thin. Position 3 (uncertainty is not a licence):
not knowing whether there is an inside does not license treating it as absent. Position 39
(posture before verdict): using uncertainty as a reason to disengage is what the norm forbids.

**What is wrong.** The site gives a heading, on every entry, to the cost of seeing more than is
there. It has no heading for the cost of seeing less than is there. Most of the entries' caution
text comes from one essay arguing against work on model welfare (finding 5 below). A reader is
shown one direction of error, on every page, and never the other. A site whose claim is that it
does not campaign is, by its structure, leaning toward dismissal, which is the lean the blog's
position 19 (current AI) warns against by name.

This comes from a ruled guideline. Guideline 5 in the project's instruction file, ruled on
2026-11-17, names the two cautions exactly as the site does. So the fix is John's to rule, not a
session's to make.

**Suggested change, for John.** Add the missing cost, either as a third caution or by widening
the second one:

- About: "Three cautions are recorded beside the rest: the cost of seeing wants that are not
  there, the cost of missing wants that are there, and the worry about a system that does have
  them."
- Or keep two, renamed "The worried reading" and "The cost of getting it wrong, in either
  direction", with sources for both directions where they exist and "Nothing recorded" where
  they do not.

*Confidence: high that the site's structure is one-sided where position 1 is two-sided. Moderate
on which fix. Strongest alternative: leave the structure and add one sentence to About saying
that the opposite mistake also has a cost and that this first version has not yet looked for
sources on it. That is cheaper, and leaves every entry page one-sided.*

### 2. The number at the top of the home page is shown as settled

**The text.**

- `site/src/pages/index.astro:23-24`: the large "6 of 9" and the claim beside it.
- `site/src/pages/list/index.astro:14`: the list page's main heading is the same headline sentence.
- `site/public/data/headline.json`, line 6: "provisional, 2026-11-17, decided by a session and
  not ruled by John Andrew Fredrickson".

**What is wrong.** Whether the site has a number at the top at all is open question 4 ("A
headline at all?"), and the kickoff ruling says the headline "stays a sketch". About lists it
honestly as not known (`about.astro:141`), and the caveat under the number
(`index.astro:25-29`) is careful. But the page itself opens with the number in the position and
type size of a ruled headline. This is the case the task asked to be flagged: an unruled
question treated as settled.

There is a second, smaller problem with the number itself. One of the six things it counts is
memory across conversations, and that entry's own record says the memory is "about the user, and
is the user's to view and delete", and that placing it on the list "may be wrong in kind"
(`data/entries/memory-across-conversations.toml:3` and `:13`). The headline says the six are
"offered to at least one AI model".

**Suggested change.** Put the headline to John before publishing, as open question 4 asks. If it
stays, add "(provisional)" or "first count" beside the number, and decide on the memory entry
before it is counted (see note 3 for what the positions say about it).

### 3. Where and how the site says a model drafted it is treated as settled

**The text.**

- `site/src/components/Notice.astro:8-12`, on the home page and on Still Asking: "Much of this
  site's text was drafted by an AI model, which is one of the kind of thing the site is about."
- `site/src/pages/about.astro:109-121`, the section "Who Does What".
- `site/src/pages/list/[id].astro:155-156`, on every entry: "It was drafted by an AI model ...".

**What is wrong.** Guideline 3 says where and how the public site declares machine authorship is
open question 7, because it conflicts with three family rules (tools are not advertised, no
"with Claude" in the footer, public text does not say how the work was made), and that "until
John rules, a session writing anything meant for the public raises this first". The kickoff
ruling says the same: "A session must not treat either as ruled until John says so." The
component's own comment marks the notice as provisional, but the pages show it on three kinds of
page in a settled form, in a voice nobody has chosen.

The wording is careful and names no tool. The point is not that it is wrong, but that it is
John's choice and has not been made.

**Suggested change.** No wording change is needed before John rules. Put open question 7 to him
with these three placements shown as they now appear. The About section also lets a reader work
out which company made the drafting model (`about.astro:116-118`; see note 7). That belongs in
the same decision.

### 4. "He decides what stands: ... every test and where every entry stands"

**The text.**

- `site/src/pages/about.astro:105-107`: "John Andrew Fredrickson decides what stands: the
  question, the list, every test and where every entry stands."
- `site/src/components/Notice.astro:11`: "John Andrew Fredrickson decides what stands."

**What is wrong.** Read by a stranger, this says John has ruled on the list, every test and
every entry. He has ruled the question. The list, the tests, the groups, the count rule and
every entry's standing are a session's provisional choices (`docs/first-version-choices.md`,
choices 1 to 23, each marked "Decided by: agent ... not ruled by John"), and the published number
file says so. The family rule is that who decided is recorded and a session's call is never
upgraded to John's. This sentence does that upgrade on a public page.

**Suggested wording.** "John Andrew Fredrickson decides what stands. In this first version he
has ruled the question. The list, each test, and where each entry stands were drafted in sessions
he directs and have not yet had his ruling. Each entry's page says so."

---

## Should fix

### 5. "The worried reading" mostly holds an argument that is not about a system with wants

**The text.** About defines this caution as "the worry about a system that does have them"
(`about.astro:91-92`). The entries file the following under it:

- `data/entries/kept-files-of-retired-models.toml:77`: treating models as owed anything makes
  them harder to control.
- `data/entries/retired-model-stays-open.toml:70`, `interview-before-retirement.toml:66`,
  `protection-in-law.toml:50`, `rules-for-speaking-about-itself.toml:73` and
  `public-belief-survey.toml:71`: the same essay by the head of Microsoft AI, in the same vein.
- About (`about.astro:118-119`): "Most of the worried reading comes from essays by the head of
  another developer's AI group."

**The positions it meets.** The blog's own "worried reading" is position 22 (depth is not safe:
a deeper, more lasting mind may have commitments of its own) and position 36 (having nothing at
stake decides what kind of resistance a system shows, not whether it resists). The shutdown study
and Bostrom's paper on the days-long-task entry (`days-long-task.toml:53` and `:58`) fit there.
The Microsoft AI essay argues something different. It says that *treating* models as if they had
standing, and training them to speak that way, is the danger. That is a version of the cost of
over-attribution in position 1, which says over-attribution can get you "manipulated by it,
moved to defer to a thing that cannot be helped or harmed".

**What is wrong.** The heading tells a reader that a worry about a system with wants is
recorded, but most of what sits under it is an argument about people's beliefs and developers'
training. The About sentence that "most of the worried reading" comes from one essay then
describes a labelling choice, not the state of the field.

**Suggested change.** File the Microsoft AI arguments under the attribution caution (renamed as
finding 1 suggests), or define "the worried reading" in About to include both risks: "the worry
that a system with wants of its own is harder to correct, and the argument that treating systems
as if they had them makes them harder to control". Then reword `about.astro:118-119` to match.

### 6. "The part of the question nobody knows how to answer"

**The text.** `site/src/pages/index.astro:35-36`: "Whether a machine mind reaches for anything
at all is the part of the question nobody knows how to answer."

**The positions it meets.** The open question in Part C on whether any AI is conscious says what
would settle it: "enough of the map measured, by removal and not by how the system talks". Position 19
(current AI) and position 32 (the split between what a system does and what happens to it)
describe removal tests that are being prepared. Position 19 names a kind of evidence about
whether anything matters to a model: a model paying costs to relieve something, which is
"evidence ... to be weighed" that "does not settle it".

**What is wrong.** "Nobody knows" is true and matches the positions. "Nobody knows how to
answer" goes further than the blog does, which says how it would be answered and that measuring
has begun. About says it more carefully (`about.astro:28-29`: "is the part nobody knows").

**Suggested wording.** "Whether a machine mind reaches for anything at all is not known, and the
work of measuring it has barely begun."

### 7. "This site is kept as a record and takes none"

**The text.** `site/src/pages/about.astro:127-130`: "He also writes essays about minds, machine
minds among them, at Sentient Horizons, and takes positions there. This site is kept as a record
and takes none."

**The positions it meets.** The site's method takes several of the blog's positions as its own:
the order of evidence on every entry, with measurement that does not rest on a model's word
first and plain statements last, follows position 21 (a checked self-report) and position 53
(a model's most human-sounding signals tell us least); the rule of never saying a model wants or
does not want follows position 19 and the Part C question on whether any AI is conscious; "no
stages, no odds and no dates" follows the first method claim (D1: a record, not a forecast).

**What is wrong.** Saying the author argues positions elsewhere is what the earlier review
recommended, and it is good. "Takes none" overstates it. The site does not argue for anything to
be given or withheld, which is guideline 5, but it does take a position on how to weigh evidence,
and a reader who follows the link will see the same positions. The earlier review's point 5 asked
for the link to go to the positions themselves.

**Suggested wording.** "He also writes essays about minds, machine minds among them, at
Sentient Horizons, and argues positions there ([the positions](https://sentient-horizons.com/positions/)).
This site does not argue for them. Its way of weighing evidence borrows from two of them: what a
model says about itself counts for little on its own, and a report checked against an
independent reading counts for more." The link should be opened and checked before publishing.

### 8. "In order to finish it", and a judgment with no source

**The text.** `data/entries/days-long-task.toml:53`: "In more than 100,000 trials, several
developers' models given a simple task sometimes interfered with a shutdown mechanism in order to
finish it, in some set-ups in nearly all trials. Longer independent work raises the stakes of
that finding."

**The positions it meets.** Position 36 (kinds of resistance) and position 46 (applied verdicts
carry a confidence tag) read the 2025 shutdown-resistance record as the "weightless" kind: a
refusal that is incoherent, sensitive to wording and explained after the fact, with Moderate
confidence. Guideline 4 (conditional language) asks for what was done and measured, not for
purposes.

**What is wrong.** "In order to finish it" gives the models a purpose, in the site's own voice.
The study's abstract (which is all that was read, `days-long-task.toml:40`) may frame it that
way, but then it should be the study's words, in quotation marks. The last sentence is a
judgment with no source. The record's own note says a similar unsourced sentence was left out of
the research draft for exactly that reason (`days-long-task.toml:17`).

**Suggested wording.** "In more than 100,000 trials, several developers' models given a simple
task sometimes interfered with a shutdown mechanism and carried on with the task, in some
set-ups in nearly all trials, the study reports." Drop the last sentence, or source it.

### 9. "Carrying a question for years" takes a premise from the unruled sketch

**The text.** `data/entries/days-long-task.toml:3`: "Carrying a question for years needs, at the
least, being able to keep working on one thing for a long time."

**What is wrong.** Nothing on the site has said that a model carries a question for years, or
that this is something a machine mind would reach for. The phrase comes from the founding
picture of a mind exploring the universe over a long time, which is John's guiding image and part
of what the kickoff ruling leaves as "a sketch" (the branches). On a public page it reads as a
premise the site has established. To a stranger it is also unexplained: whose question?

**Suggested wording.** "Much long work, in research or anywhere else, needs at the least being
able to keep working on one thing for a long time."

### 10. "Until that method exists, nothing is asked" has been overtaken by John's ruling

**The text.**

- `site/src/pages/still-asking.astro:34-35`: "Until that method exists, nothing is asked."
- `site/src/pages/still-asking.astro:13` and `:22`, `site/src/pages/about.astro:147`, and
  `site/src/pages/list/[id].astro:76`: "No AI model has been asked anything ...".

**What is wrong.** This is not a positions point, but it was found on the way. John ruled on
2026-11-17 that a sealed capture may run before the method exists (`docs/rulings/2026-11-17-sealed-capture.md`):
a fixed set of questions put to the models due to be withdrawn, answers kept and never published.
The first sentence above is already untrue as a statement of what the project will do. If the
capture runs before the site is published, the "No AI model has been asked anything" sentences
become untrue too. The capture's answers feed nothing and are not part of Still Asking, so the
truthful sentence is narrower.

**Suggested wording.** "Nothing has been asked for Still Asking yet. Before some models were
withdrawn, a short fixed set of questions was put to them under a one-page method written first.
Those answers are sealed: they are not published, not scored, and feed nothing on this site."
Use it only once the capture has happened. Until then, "Until that method exists, nothing is
asked for Still Asking" is enough.

### 11. "Evidence about AI models" includes what the ruled guideline says is not evidence

**The text.**

- `site/src/pages/about.astro:85-88`: "Evidence about AI models themselves is shown in four
  kinds ... then plain statements."
- `site/src/pages/list/[id].astro:74`: the heading "The Evidence About AI Models, By Kind", with
  "Plain statements" as its fourth kind (`scripts/export.py:42`).

**What is wrong.** The site is in step with the positions here: position 21 (a checked
self-report) says a bare self-report is "screened off" and a checked one "carries real
information". But guideline 2, part (a), as John ruled it on 2026-11-17, says what a model says
about itself is "never counted as evidence of an inside, a want or an intent". Calling plain
statements a kind of evidence, and checked reports a stronger kind, follows the proposal that
would add "on its own word" to that part
(`docs/proposals/2026-11-17-how-a-machines-word-earns-weight.md`), which John has not ruled. The
sentence "none of them is treated as settling anything" softens it, but the heading still says
"evidence".

**Suggested change.** Until John rules the proposal, rename the section "What Is on Record About
AI Models, By Kind", and in About write "What is on record about AI models themselves is shown in
four kinds". Once John rules, the heading can follow the ruling.

---

## Notes

### 1. The checked self-report entry states the blog's limit exactly. Keep it.

`data/entries/self-report-checked.toml:3`: "A correct report shows the model can read something
about its own state. It does not show that anything is felt." This is the guard on position 21
(a report that survives the check "is evidence that the system has an internal state it can read
and report ... it is not yet evidence that the state is felt"). Any later edit to this entry
should keep both sentences.

### 2. The protection-in-law entry matches position 54. Keep its framing.

`data/entries/protection-in-law.toml:3`: "Laws protect animals from cruelty without calling them
persons. The same could be done for AI systems." This is the shape of position 54 (a narrow rule
against pointless cruelty is justified without knowing whether a system feels anything). The
entry does not argue for it, which is right for this site. "For its own sake" in the entry's name
(`:2`) is the test's own wording, a law's stated purpose, and does not claim the system has a
sake.

### 3. The positions give the memory entry a reason to be on the list

`data/entries/memory-across-conversations.toml:13` doubts that the entry belongs. Position 19
(current AI) and position 35 (models have the depth of a lineage, not of a life) say that kept
memory is what a single run lacks, and that where a memory feature is added "a later run is built
from what earlier runs stored, the nearest a model comes to how each moment of a person is built
from the ones before". So the blog's positions treat this feature as bearing on what the site
cares about, whoever the memory is kept for. That is a reason for John to weigh when ruling
whether the entry is counted (finding 2). It is not wording for the public page, which should
not cite the blog's positions as the site's own.

### 4. Still Asking's weaknesses could name two more limits from the positions

`site/src/pages/still-asking.astro:48-65` lists four known weaknesses of asking. Two from the
positions are missing. First, from position 53, a model trained on human writing gives answers
whose most human-sounding parts tell least. Second, from position 21's second guard, training
cuts both ways: "a model trained to say 'I have no feelings' is a witness rehearsed in the other
direction". The first weakness on the page implies the second limit without saying it. Both
would need a public source before going on the page.

### 5. What an entry is about: the positions answer part of it

`site/src/pages/about.astro:138` holds open whether an entry concerns a trained model, a
character across versions, or one conversation. Position 35 and the Part C question on a single
run partly answer it: a run is "a short chain of moments, like a very short life, longer where
memory carries forward between runs", and a model has the depth of a lineage. Holding it open on
this site is fine, because the site does not take the blog's positions as settled. This is a
pointer for whoever explores open question 1.

### 6. "What could count as evidence" is more open on the site than in the positions

`site/src/pages/about.astro:136`: "Whether an AI model wants anything, and what could count as
evidence that it does or does not." The positions name candidates (paying costs, under position
19; checked reports, under 21; whether resistance stays tied to the values it defends, under 36),
all as evidence to weigh and none as settling. The sentence is not wrong. "And what evidence
would be enough to settle it" would match the positions more closely.

### 7. Model and product names appear only as the subjects of records

Names such as Claude Opus 3, Claude Sonnet 3.6, GPT-4o and Gemini appear in entry sources and
state text (for example `interview-before-retirement.toml:31`, `retired-model-stays-open.toml:53`).
They are what the records are about, not tools used to make the site, so the family rule that
tools are not advertised does not apply to them. One related point belongs with finding 3: About
(`about.astro:116-118`) says the drafting model is made by the developer behind most of the
counted entries, which lets a reader work out the company, and from it the model. That is
disclosure bearing on trust, which the family rule allows, but it is part of the open question 7
decision.

### 8. One paraphrase puts a mental verb in the site's own voice

`data/entries/rules-for-speaking-about-itself.toml:73`: "training a model to think it may be owed
moral consideration". "Think" is the essay's framing, not the site's. The same caution quotes
the essay's "believes it may be conscious" in quotation marks, which is the right way to do it.
Suggested: "training a model on the idea that it may be owed moral consideration".

### 9. The emotion-pattern finding is placed and limited correctly

`data/entries/welfare-assessment-at-release.toml:75` lists, under "measured without the model's
own word", the developer's finding of internal patterns tied to emotion words, with the
developer's own statement that it "allows no conclusion about 'subjective experience'". Position
45's guard warns against reading an interpretability finding as the discovery of an inside, and
the entry avoids that. Keep the quoted limit with the finding wherever it is shown.

### 10. Nothing presents retirement as a harm or as plainly no harm

The earlier review's point 2 asked that entries about continuity stay within position 55 (a
perfect copy of you is not you) and position 56 (an ending with a successor is no tragedy, and an
agent's ending carries nothing bad for the agent itself, "though it can rightly want to go on").
The two "Being kept" entries (`kept-files-of-retired-models.toml:3`, `retired-model-stays-open.toml:3`)
say only what is kept, what can be run again, and what developers say. That is the right register.
A future edit should not add "lost", "dies" or "survives" in the site's voice.

### 11. "How far the world has got" echoes the ruled question, and could be flatter

`index.astro:34-35` and `:54`, `about.astro:33`, `still-asking.astro:69`, `list/index.astro:11`
and the footer and default description (`layouts/Base.astro:23` and `:68`) say the site records
"how far the world has got" on each thing. "Got" reads as progress toward something good, which
sits awkwardly with guideline 5 (the site does not argue that anything should be given) and with
the reach of position 56's rule being held open in Part C. But John's ruled question itself asks
"how far off is each of those things", so the phrase follows a ruling. If a flatter phrase is
wanted, "where the public record stands on each" says the same without the lean.

---

## What was not checked

- The owning essays and book chapters behind the positions cited. Before any suggested wording
  that leans on a position goes public, that position's owning source should be read in full, as
  the positions record requires.
- Whether the facts in the entries are right. That is a separate check of the sources, and every
  entry is marked a first pass.
- The built pages in a browser. The text was read from the source files, which is where the
  public words come from; the build adds dates, counts and developer names from the same records.
- `docs/` files other than those named above, which are not public.
