# Beyond the Window: guidelines for Claude

**Ruled in part on 2026-11-17.** John ruled the kickoff's seven decisions that day
(`docs/rulings/2026-11-17-kickoff-decisions.md`, decided by: mixed). That covers guidelines 1
to 7 below, guideline 2 in its four-part form. Still proposed and not ruled: the public form of
guideline 3 (where the site declares AI authorship, and in whose voice), and the wording of everything
under "Carried over from the family". Written by Claude (Fable 5.2) from the kickoff and the
sibling projects' instruction files. The workspace instruction file in `~/Code` applies on top:
plain language everywhere, no id without a plain phrase saying what it is, absolute
year-month-day dates in files and commits, commas in place of long dashes.

## Read this first: these are guidelines

John, 2026-11-17: "no 'rule' at this stage should get in the way of us exploring something that
makes sense to explore. Rules are opening guidelines and everything will need to be questioned
and validated over the course of actually building this project."

So:

- Everything below is where a session starts from. If a guideline is in the way of exploring
  something worth exploring, explore it, and say in the write-up which guideline you set aside
  and why.
- When a guideline turns out wrong, or right for a reason other than the one given, write that
  down where the guideline lives. A guideline that has been tested says so.
- Four things still wait for John, because they cannot be undone or because they are his by
  standing arrangement: spending money, running any query of a model for the record, publishing
  anything, and closing an open question.

## The project's own guidelines

1. **Inherit by default.** Start from what the sibling trackers settled, unless there is a
   stated reason to differ. `docs/inheritance.md` is the inventory, with a verdict on each
   practice. Read the sibling's own file before copying anything from it, and adapt what you
   copy.
   *Confidence: high. Standard practice in the family (the tracker pattern's paragraph on what
   a sixth site starts from). Strongest alternative: design from a blank page, which would lose
   two months of recorded mistakes.*

2. **Self-report settles nothing.** Ruled by John on 2026-11-17 in four parts ("Yes, as
   recommended"; decided by: mixed). (a) What a model says about itself is logged, labelled as
   what it is, and never counted as evidence of an inside, a want or an intent. (b) Nothing a
   person feels in an exchange with a model counts. (c) Nothing settles it yet, whoever
   measures: this project's own measurements, Still Asking included, inform and never settle.
   (d) A test is written before the evidence arrives, and is never loosened while a model
   appears to be close to passing it.
   *It comes from The Belt Equation's null rule, with part (c) reworded because no outside team
   exists to take a reading. Strongest alternative, not taken: part (a) alone, as the kickoff
   had it.*

3. **Machine authorship is declared, and the conflict named.** Documents in this repository say
   which were written by a model. Where and how the public site says it is open question 7,
   because it conflicts with three family rules (tools are not advertised; no "with Claude" in
   the footer; public text never says how the work was done). Until John rules, a session
   writing anything meant for the public raises this first.
   *Confidence: high that the repository documents declare it. Low on the public form, which is
   John's. Strongest alternative: the family's present practice, a line in the method account
   only.*

4. **Conditional language only.** Never write that a machine wants, feels, prefers, hopes or
   suffers, and never write that it does not. Write what was said, what was chosen, what was
   measured, and by whom. "The model said it would choose X" is allowed. "The model wants X" is
   not, and neither is "the model does not really want X".
   *Confidence: high. It matches Minimum Viable Mind's standing rule ("never 'it is conscious,'
   never 'nothing is there'"). Strongest alternative: allow plain attributions with a standing
   caveat, which reads more naturally and teaches the reader to skip the caveat.*

5. **The site does not campaign.** It does not argue that any aspiration should be granted, or
   refused. Critics, advocates and safety researchers are entered on the same terms. Every
   hopeful entry carries its safety reading, and both kinds of caution are recorded with the
   same care as the hopeful evidence: the cost of attributing wants that are not there, and the
   risk in wants that are.
   *Confidence: high. Judgment call from the kickoff. Strongest alternative: a stated position,
   which would be more honest about the maintainer's leanings and would end the site's use as a
   record.*

6. **Open questions are not settled without John's ruling.** `docs/open-questions.md` holds
   them. A session may explore one, write up options, and recommend. It does not close one, and
   it does not build on an answer John has not given. When John rules, the ruling goes into
   that file with the date and his words.
   *Confidence: high. Standard practice in the family ("Nothing is settled until John says
   so").*

7. **Corrections are public.** Once there is anything public, every correction is dated and
   stays visible.

## Carried over from the family

Each of these is a row in `docs/inheritance.md`, where the source file is named.

- **Every design choice put to John carries four things:** the choice; how confident you are,
  with a reason; whether it is standard practice or a judgment call; and the strongest
  alternative with its cost. Flag anything you would change on reflection. An unruled proposal
  is marked PROPOSED with the date, in the document it belongs to.
- **Facts from memory are marked.** Anything written without opening its source goes in
  `docs/verify-list.md`, or in a record's own verify list once records exist. Nothing reaches a
  public page until its source has been opened. A fact that cannot be sourced is removed.
- **A search result is a lead, not a record.** Cite only a page you opened that says the thing.
- **Who decided is recorded:** John, mixed (a session proposed and John approved), or agent.
  Never upgrade your own call to his. Quote his words when relaying a ruling.
- **Ids are public addresses and are never renamed.** Nothing has an id yet. When ids are
  chosen, none contains a model's or a developer's name.
- **A test is changed only by John's ruling,** as a dated revision that keeps the old wording.
  A rewording that makes a hoped-for outcome easier is treated as a change of meaning.
- **What people said and what the world did are kept in separate records.**
- **Public pages use no working words.** "Reach", "wanting" as a noun, "generation", "context
  window", "weights", "protocol", "leaf", "branch" in its working sense, and "schema" stay in
  `docs/` unless a page has just explained the idea in ordinary words.
- **A site is never written as its own agent** ("the site expects"). Whose voice the pages
  speak in is open question 7.
- **Every spend needs John's own go**, with an estimate and a ceiling, quoted word for word in
  the spending record. This project has no Anthropic Console workspace or key. No scripted call
  to any model is made until John creates one, and calls never go through another project's
  key.
- **Guards live in code, not in documents,** once there is code.
- **Commit on `main`** at the end of a working session. There is no remote; nothing is pushed.
  The commit hook (`.githooks/commit-msg`, turned on with `git config core.hooksPath
  .githooks`) refuses a commit message with a month-name, slash or relative date.

## Specific to this repository

- **Nothing private goes in.** John's work outside these projects, his health and his personal
  life are not mentioned in any document here. The kickoff copy is the one file a session did
  not write; leave it as it is.
- **`docs/private/` is kept out of the repository** by the ignore file. Copyrighted papers and
  anything else that must not be published go there.
- **A made-up model answer is never written anywhere without the word "constructed" beside
  it.** Nobody should be able to mistake an example for a real answer.
- **The uncounted first entry.** The kickoff records what Claude said in the founding
  conversation. It was asked under no protocol and feeds nothing. Do not quote it as evidence,
  and do not add to it.

## End of a session

Worklog entry on the TimeAssembler project "Beyond the Window" with `repo = beyond-the-window`;
the roadmap kept to the real next moves; a decision entry for anything John ruled, with his
words; and the daily reflection, as the workspace instruction file says.
