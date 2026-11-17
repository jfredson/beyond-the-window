# What this project inherits from the sibling trackers

Written 2026-11-17 by Claude (Fable 5.2) in a Claude Code session. **PROPOSED, not ruled.** Each
row's verdict is a proposal for John.

This is the inventory the kickoff asks for: every practice, rule and lesson the siblings
settled, where it is written down, and whether it carries over as is, carries over changed, or
does not apply. The mistakes and reversals are in part 2, because they are lessons too.

## How to read this

**Everything here is an opening guideline.** John said on 2026-11-17: "no 'rule' at this stage
should get in the way of us exploring something that makes sense to explore. Rules are opening
guidelines and everything will need to be questioned and validated over the course of actually
building this project." So "carries over as is" means "start from this", and it does not mean
"closed". The family already holds this view of its own rules. When The Belt Equation replaced
a rule it had not been keeping, John's prompt was: "No requirement should be blindly followed
without reviewing if it is still the correct way to do things" (2026-10-31).

**The verdicts.**

- **As is**: start from the sibling's practice unchanged.
- **Changed**: start from it, with the change and the reason given.
- **Does not apply**: with the reason.
- **Conflict**: two inherited practices, or an inherited practice and the kickoff, cannot both
  hold. These need John's ruling and are also in `docs/open-questions.md`.

**Confidence** in each verdict is high unless the row says otherwise. Almost every row is the
family's standard practice; the rows marked as a judgment are mine.

**How it was read.** Six helper sessions read the repositories on 2026-11-17 and reported with
file paths; I read the tracker pattern, the design standard's key sections and Outrunning
Ageing's instruction file and kickoff myself. I did not open every file the helpers cite, so a
path or a quotation below is as a helper reported it. Three folders on this Mac
(`outrunning-ageing`, `sentient-horizons`, `agi-zeitgeist`) are checked out on old side
branches; where a rule exists only on the main branch the row says "main branch".

**Short names for where things are written.** Paths are under `~/Code`.

| Short name | File |
|---|---|
| the pattern | `sentient-horizons/design/tracker-pattern.md` (main branch) |
| the standard | `sentient-horizons/design/README.md` (main branch) |
| the lessons ledger | `sentient-horizons/design/lessons.md` |
| the workspace rules | `~/Code/CLAUDE.md` |
| the routing guide | `timeassembler/docs/session-routing.md` |

The six projects are named in full the first time in each section and then shortened: the Belt
(The Belt Equation), the Zeitgeist (the AGI Zeitgeist), the Galaxy (The Quiet Galaxy), the Tree
(The Upgrade Tree), Ageing (Outrunning Ageing), and the mind project (Minimum Viable Mind).

---

## Part 1. Practices and rules

### A. The shape of a tracker

| # | Practice | Where written | Verdict |
|---|---|---|---|
| A1 | One question at the top and one thing a reader can hold at a glance. | The pattern, section 1 | **As is** for the question. What is held at a glance is open question 4. |
| A2 | The thing at the top is worked out from the records and never typed in. | The pattern, rule 1.1; every sibling's method document | **As is.** It binds whichever headline form is chosen. |
| A3 | Every branch is a reason the top reads as it does. Anything tracked that cannot change the top is shown beside it and says so in plain words. | The pattern, rule 1.2 | **As is.** It is the model for the supporting branch ("whether anyone is there at all") and for how Still Asking sits beside the reach records. |
| A4 | A side record is kept out of the headline by a check in code, so "never multiplied in" is a tested rule and not a promise. | `belt-equation/docs/node-schema.md`, rule 10; `belt-equation/scripts/test_contact.py` (2026-09-25) | **As is**, for the supporting branch and for any reading that must not feed a count. |
| A5 | Between four and nine branches, fixed, changed only at a yearly review. | The pattern, rule 2.1 | **Changed.** The range holds. "Fixed, yearly" is in doubt: the kickoff says the branches may need to grow from the data, and the subject changes every few months. Open questions 5 and 12. |
| A6 | Under each branch, specific things that would have to happen, each on its own page at a stable address, each with a written test. "A leaf without a test is not a leaf." | The pattern, section 3 | **As is, and the kickoff is missing it.** The kickoff goes from aspirations straight to ladders. Open question 14. |
| A7 | Each tracked thing names in advance the kind of public record that settles its test. A press claim, a funding round, a target date or a video settles nothing. "Common knowledge" is not a source. | The pattern, section 3, item 3; `belt-equation/docs/node-schema.md` | **Changed.** As is for reach. For wanting there is no record that settles anything, which the kickoff calls the central unsolved problem. Open question 2. |
| A8 | The ten things every record has: a stable id that is its address; a plain name and description; its group; the test; the kind of record that settles it; the state now with a date; a dated history of every change; a list of facts not yet checked; notes; a validator that refuses a broken file. | The pattern, section 3a.1 (main branch, 2026-10-24) | **As is** for reach records. `docs/record-schema.md` starts from it. |
| A9 | A new site picks one of the five existing kinds of state or states a sixth, with its own rule for what the weekly reading may change. | The pattern, sections 3a.2 and 3a.5 | **Changed.** Reach can use the Tree's kind (a stage on a ladder). Wanting is a sixth kind and has no rule yet. |
| A10 | A test changes only by John's ruling, as a dated revision that keeps the old wording. A session never edits a test on its own. | The pattern, rule 3.1 (2026-10-17) | **As is.** See also A11. |
| A11 | Rewording a published test: a correction may be made in place if the recorded state already covered the new reading; a change of meaning retires the old record and starts a new one. A rewording that makes the hoped-for outcome easier is assumed to be a change of meaning, and needs John's own approval. | `belt-equation/docs/methodology.md`, "Rewording a criterion after publication" (2026-11-09) | **As is, and it matters more here.** "Widening a criterion toward the outcome you hope for is the easiest way to fool yourself." |
| A12 | Long shots stay in, but each must say how it could happen and where it would break. | `belt-equation/docs/definitions.md`, founding rules (2026-09-08); the pattern, section 3 | **As is.** Several candidate aspirations are long shots. |
| A13 | A label names the event its test checks, not a feeling. | `belt-equation/docs/definitions.md`, decision log, 2026-09-25 | **As is.** The kickoff's branch names ("lasting company", "a say in its own becoming") are evocative; the tracked things under them need names that say what happened. |
| A14 | A dependency names the function needed, not one route to it, when more than one route could supply it. | `belt-equation/docs/methodology.md`, "Function over route" (2026-09-25) | **As is, judgment.** "One continuing life" could be reached by kept weights, by memory, or by something else; the test should name the function. |
| A15 | At least a third of the tracked things should be able to settle within five years, or the first score is decades away. | `belt-equation/docs/2026-09-08-kickoff.md`, "Rule for granularity" | **Changed.** Here the worry runs the other way: things may settle or reverse within months. The idea behind it holds: make sure some entries can move soon. |
| A16 | No probabilities until the structure is stable. | `belt-equation/docs/roadmap.md`, ground rules | **As is.** The kickoff already says no probability and no year. |
| A17 | A stage never moves down; a withdrawal is a status and a note. | `upgrade-tree/docs/upgrade-schema.md`; `outrunning-ageing/docs/record-schema.md` | **Does not apply as written, judgment.** A developer can withdraw a commitment and a new model generation can answer differently. Going backwards is a finding here. State is recorded per date and per generation. Moderate confidence. Strongest alternative: keep "never moves down" for reach and record a withdrawal as a status, as the siblings do, which is simpler and hides less than it seems if the status is shown. |
| A18 | No stage for things only planned or promised. Refusal to guess: "a stage, a date and a record say what has happened; a probability would say what someone guesses". | `upgrade-tree/docs/upgrade-schema.md` (2026-10-16) | **As is.** |

### B. Ids, files and the validator

| # | Practice | Where written | Verdict |
|---|---|---|---|
| B1 | A record's id is its public address and is never renamed. Retire it in a retired list with a reason and a pointer; a retired id is never reused. The validator reads the repository's history to catch a vanished id. | `outrunning-ageing/CLAUDE.md`; `quiet-galaxy/docs/record-schema.md`, rule 10; lessons ledger, lesson 6 | **As is.** |
| B2 | Decide before the first commit what an id may never contain, because ids end up in addresses, saved runs and pictures. | Lesson from `belt-equation/CHANGELOG.md`, 2026-10-03 and 2026-11-14 (ids renamed against the rule) | **As is, with one addition, judgment.** An id here should not contain a model's or a developer's name, since those change and are retired. |
| B3 | Ids are plain words with no branch prefix, because a record's branch can change at a review. | `outrunning-ageing/docs/record-schema.md`, decision 3 | **As is.** More likely to matter here, where the branches are least settled. |
| B4 | One plain-text file per record, named for its id, in TOML. Unknown fields are refused. Top-level fields go before the first table. | `outrunning-ageing/docs/record-schema.md`; `quiet-galaxy/docs/record-schema.md` | **As is.** |
| B5 | Dates the world supplies are text (a year, or a year and month, or a full date). Dates the project writes are calendar dates. | `quiet-galaxy/docs/record-schema.md`, decision 8 | **As is.** |
| B6 | Links between records point one way and nothing is stored twice; the site gathers the reverse links when it builds. | `quiet-galaxy/docs/record-schema.md`, decision 6 | **As is.** |
| B7 | Every change after a record's first commit gets a revision: date, field, old value, new value, why. | The pattern, section 3a.1, item 7 | **As is.** |
| B8 | One document lists every kind of record, every field and every numbered validator rule; the deploy runs the validator first. | Lessons ledger, lesson 7 | **As is.** `docs/record-schema.md` is the start of it. |
| B9 | Every new record carries the date it was added, because the site cannot read the repository's history when it builds. | `outrunning-ageing/docs/record-schema.md`, decision 23 (2026-10-18) | **As is.** |
| B10 | A worked example is flagged as an example and never shown as real. Examples made up to show a rule are marked "constructed" and never cited as quotations. | `outrunning-ageing/docs/record-schema.md`, decision 13; `agi-zeitgeist/docs/codebook.md` | **As is, and it matters more here.** A made-up model answer must never be mistaken for a real one. |
| B11 | Guards live in code, not in documents. "A mitigation that depends on the operator noticing is not a mitigation." | `minimum-viable-mind/docs/rulings/2026-09-22-launcher-argument-guard.md` | **As is.** |

### C. The headline

| # | Practice | Where written | Verdict |
|---|---|---|---|
| C1 | One export script is the only reader of the data; every page reads its output; the top is the same number everywhere. | The pattern, rule 1.5; lessons ledger, lesson 3 | **As is.** |
| C2 | The headline is written to one small file by the step that computes it, committed, and served from the site at `/data/headline.json` with the date computed, the date of the last reading and the version. | The pattern, rule 1.6 (2026-10-17) | **As is**, once there is a headline. |
| C3 | The headline file keeps a history of its runs and is never edited by hand; every run is kept and can be reproduced. | `outrunning-ageing/docs/record-schema.md`, decision 24; lessons ledger, lesson 4 | **As is.** |
| C4 | The headline file says how settled its numbers are: how much of what it rests on has been reviewed, as counts. | Lessons ledger, lesson 2 | **As is.** |
| C5 | Scripts stamp the Pacific date, not the machine's. | `belt-equation/CHANGELOG.md`, 2026-10-18; ruled for Ageing the same day | **As is.** |
| C6 | An unsettled question gets a spread and a width, not a point: the most and the least the published estimates support, shown side by side ("That gap is the argument"). The single most sensitive choice is shown openly. | `quiet-galaxy/docs/method.md` | **As is as an option.** One of the five headline forms in open question 4. |
| C7 | The two ends of the argument, and a section headed "What I know least about". | `outrunning-ageing/docs/method.md` and `CHANGELOG.md`, 2026-11-09 (main branch; proposed there, not yet ruled) | **As is, and the kickoff is right that it carries more weight here.** Note it is still unruled on Ageing. |
| C8 | A headline that is an average is never shown without its slowest part beside it. | `agi-zeitgeist/docs/amendments.md`, entry A25 (2026-10-17) | **As is as a caution** for any combined number. |
| C9 | A profile, never a verdict. Public reporting is "never 'it is conscious,' never 'nothing is there'". Failing to measure something is not evidence it is absent. | `minimum-viable-mind/CLAUDE.md`; `minimum-viable-mind/spec/corrigibility-commitments.md`, commitment C7 | **As is.** It is the kickoff's conditional-language rule, already tested. |
| C10 | A coverage note guards against sliding from "we measured this one account's claim" to "we measured the thing itself". | `minimum-viable-mind/spec/theory-instrument-ledger.md` | **As is.** The slide here would be from "models said this" to "models want this". |
| C11 | Numbers that do not reproduce may be quoted only as a range and a direction. | `minimum-viable-mind/docs/rulings/2026-09-23-range-and-direction-only.md` | **As is**, for Still Asking results that vary from one asking to the next. |

### D. Sourcing and checking facts

| # | Practice | Where written | Verdict |
|---|---|---|---|
| D1 | Every fact in a public record carries a source a reader can open. A fact written before its source was opened goes in the record's verify list. A fact that cannot be sourced after a real search is removed, with the reason in the changelog. Nothing is promoted while any verify entry is open. | The pattern, rule 3.3 (2026-10-17). John: "Nothing should be 'from memory'. Everything must be verified and sourced." | **As is** for reach records and every page. For Still Asking answers see D9. |
| D2 | A reminder to check something later is not a verify entry; it goes in notes, so it does not block sharing for months. | `quiet-galaxy/CLAUDE.md` (2026-11-14) | **As is.** |
| D3 | The weekly reading may read a verify list and never edit it. | `belt-equation/docs/node-schema.md` (2026-10-06) | **As is.** |
| D4 | Primary sources only. News coverage is coverage, marked as such in a field the validator reads, and carries no quoted words. | Lessons ledger, lesson 15; the pattern, rules 6.2 and 6.3 | **As is.** |
| D5 | "Search results are leads, not records." A page is cited only if it was opened and says the thing. Never write as if you had read a page you did not open. | `belt-equation/docs/scan-procedure.md` (2026-10-15); `quiet-galaxy/docs/weekly-reading.md` | **As is.** |
| D6 | A record written from a paper's abstract says so; the full text is read before the record is trusted. | `quiet-galaxy/CHANGELOG.md`; `outrunning-ageing/CHANGELOG.md`, 2026-10-20 | **As is.** Much of this subject's literature is preprints and company posts. |
| D7 | A quotation from a recording is shown only when two independent transcripts agree word for word. | `upgrade-tree/docs/upgrade-schema.md` (2026-10-17); lessons ledger, lesson 16 | **As is**, for anything quoted from a talk or interview. |
| D8 | A repeated paraphrase is recorded as a paraphrase beside the words actually said, and is never promoted because many outlets carry it. | The pattern, rule 6.3 | **As is.** |
| D9 | The project's own measurements are not "sourced"; each is labelled as measured (a check was run and its output reported) or argued (reasoning a reader can dispute). | `minimum-viable-mind/docs/outside-review-protocol.md`; the pattern, rule 3.3, "Where it does not apply" | **As is** for Still Asking. The source of a Still Asking answer is the committed transcript of the run. |
| D10 | Only records anyone can pull again; no personal recollection in the data. | `agi-zeitgeist/docs/2026-09-30-kickoff.md` | **Conflict, in part.** A retired model cannot be asked again, so the transcript is the only record. And publishing the transcripts may spoil later askings. Open question 15. |
| D11 | Every named project, organisation, person or study in public prose is linked at its first mention, official page first; every link opened before publishing. | The workspace rules, "Link what you name"; the pattern, rule 4.17 | **As is.** |
| D12 | A reviewer's recollection is not a source either. Every paper an outside reviewer names is opened before a ruling is applied. | `outrunning-ageing/docs/reviews/2026-10-17-rulings.md`; `quiet-galaxy/docs/reviews/2026-10-17-rulings.md` | **As is.** |
| D13 | Papers behind a paywall stay private; only short phrases are used. | `quiet-galaxy/CHANGELOG.md`, 2026-10-20 | **As is.** |

### E. Talk set against delivery

| # | Practice | Where written | Verdict |
|---|---|---|---|
| E1 | What people said and what the world did are kept in separate records. "A statement never becomes a measure of the world; a measure never becomes a statement." | The pattern, rule 6.1 | **As is, and it decides a kickoff sketch.** What a model says about itself is talk. The kickoff's wanting ladder lets talk climb rungs. See the review, point 1. |
| E2 | Talk is dated by when it was said, delivery by when it happened; both need a primary source. | The pattern, rule 6.2 | **As is.** |
| E3 | The two are shown on one page side by side so the reader can see the gap. | The pattern, rule 6.4 | **As is as a starting point** for how Still Asking sits beside reach. |
| E4 | A claims log of what named people promised, each with a test written at entry and never changed, an admission rule that never looks at whether the claim came true, and no hit rates. | `agi-zeitgeist/docs/claims-ledger-method.md`; reframed 2026-10-19: "The goal is not to score people on their success at predicting the future" | **As is, in every direction**, as the kickoff says: what developers promise about model welfare, what critics say, what safety researchers warn. |
| E5 | Critics are entered on the same terms as advocates. What is not in the source is written down too. | `upgrade-tree/docs/upgrade-schema.md`, "The claim record" | **As is.** It serves the kickoff's rule that the site does not campaign. |
| E6 | The weekly reading never gives a verdict on a claim, because a verdict is the site's public word on a named person. | `outrunning-ageing/docs/weekly-reading.md`, design choice 3 | **As is.** |
| E7 | Something widely reported that moved nothing is recorded as such, with the test it was read against, and gets equal billing. | The pattern, rules 4.2 and 4.3 | **As is.** A model release with striking claims that changes no record is this site's commonest case. |

### F. Self-report and the null rule

| # | Practice | Where written | Verdict |
|---|---|---|---|
| F1 | The null rule, four clauses. (1) Nothing a candidate system says about itself counts toward any rung. (2) Nothing John or any user feels in an exchange counts. (3) No rung resolves on John's own measurement; the settling reading is taken by a team with no stake. (4) Tests are written before the evidence arrives; a loosening is flagged and is not made in the same quarter that a candidate appeared to approach the test. | `belt-equation/docs/definitions.md`, "The null rule" (decided 2026-09-19, proposed by Claude, approved by John) | **As is, all four.** The kickoff carries clause 1 only. See the review, point 3. |
| F2 | The reasoning recorded with it: "the candidate itself will argue for what should count. A criterion written after the fact will be written under that pressure." And: "a hope that is allowed to grade its own evidence produces positive results in the psyche of the person holding it." | `belt-equation/docs/proposal-contact-clause-null-rule-2026-09-19.md`, "Why" | **As is.** Worth quoting in this project's own method. |
| F3 | A reading that tightens a test may be made at any time; one that loosens it may not. | `belt-equation/docs/definitions.md`, decision log, 2026-10-06 | **As is.** |
| F4 | The Belt's machine rung asks for a measure of an inside "that does not rely on the system's own reports, replicated by at least one team with no stake in the result", and admits "there is no accepted test for an inside". | `belt-equation/docs/definitions.md`, "The null rule and C5 in force" (2026-09-25) | **As is as a boundary.** This project's supporting branch overlaps that rung. Open question 8. |
| F5 | Behaviour cannot settle it either: "Every behavioral test is passable in principle by a system with nothing going on inside." | `minimum-viable-mind/spec/minimum-viable-mind-proposal-v0.1.md`, "The Limits" | **As is as a stated limit.** It bears on the kickoff's "chosen at some cost" rungs as much as on its "stated" rungs. |
| F6 | Pressure mostly hides a position instead of removing it (9 true changes of position in 540 pressured exchanges). | `minimum-viable-mind/experiments/03-retained-independence/results.md` | **As is as a finding to design around.** What a model "chooses" under a framing may show the framing. |

### G. The weekly reading

| # | Practice | Where written | Verdict |
|---|---|---|---|
| G1 | A fresh session with no memory reads every record against the week's news, following one standalone procedure file. The scheduled task's prompt only points at that file. | `outrunning-ageing/docs/weekly-reading.md`; `belt-equation/docs/scan-procedure.md` | **As is**, for reach records, once there are any. |
| G2 | One record per reading, written once and never edited; a fixed set of verdicts the validator checks; quiet weeks recorded too. | Lessons ledger, lesson 11 | **As is.** |
| G3 | Every search is logged as run, at least two per record, including those that found nothing. | The pattern, rule 5.4 | **As is.** |
| G4 | A "limits" line says what the reading could not see. "Quiet" means nothing was found, not that nothing happened. | `outrunning-ageing/docs/record-schema.md`, decision 20; `upgrade-tree/docs/weekly-reading.md` | **As is.** |
| G5 | A written list of what the unattended reading may and may not change. It never edits a test, a verify list, a claim's verdict, the branches, the method, or its own instructions. Anything outside its limits becomes a flagged item with a line for John. | Each sibling's weekly reading document; strictest on the Zeitgeist, which may only append and flag | **Changed, judgment.** Start at the strictest setting: append and flag only, nothing moved without John. A machine session moving a record about what machines want is the conflict of interest at its plainest. Strongest alternative: the Tree's setting (one rung up on a primary record), which keeps the site current without John and would be reasonable for reach records alone. |
| G6 | Dated sources first: registries and databases that can be filtered by date, because a web search cannot. A separate weekly sweep for the week's news, as its own run. | `outrunning-ageing/docs/weekly-reading.md`, step 1a, and `docs/weekly-sweep.md` (main branch, 2026-11-09) | **Changed.** The same routine with new sources, as the kickoff says. Which sources is open: developers' own model pages and retirement schedules, the preprint listing, the welfare and safety research groups. |
| G7 | A fixed list of primary sources read every week makes "a quiet week a real finding and not a search that happened to miss". | `belt-equation/docs/discovery-sources.md` (2026-10-27) | **As is.** |
| G8 | A preprint listing is not the whole literature; journals are listed through a second route. | `quiet-galaxy/CHANGELOG.md`, 2026-11-13 | **As is.** |
| G9 | Helpers get fixed briefs word for word; the main session reopens every source behind a flagged item. | `outrunning-ageing/docs/reading-briefs/` (main branch) | **As is.** |
| G10 | A monthly missed-story check by a model from another lab, asked from scratch for the period's news. | `outrunning-ageing/scripts/miss_check_gemini.py` (main branch; built, not yet run) | **As is, with the reviewer question attached** (open question 7). |
| G11 | Self-imposed limits are always reviewable: a limit says what it protects, every time it cuts is reported, and a limit that cuts twice goes to John. | `outrunning-ageing/docs/weekly-reading.md`, step 1a (2026-11-09) | **As is.** |
| G12 | The first run of any new scheduled job is audited. | `quiet-galaxy/docs/readings/audit-2026-10-17.md`; `upgrade-tree/docs/readings/audit-2026-10-18.md` | **As is.** |
| G13 | A window that always overlaps, so a missed run leaves no hole. | `outrunning-ageing/docs/record-schema.md`, decision 22 | **As is.** |
| G14 | The last-checked line on the home page, shown every week including quiet ones, dated by the reading and not the build. | The pattern, section 5 | **Changed.** There are two clocks here: when the world was last read, and when the models were last asked. Both need a line. |
| G15 | Records shared between two sites name each other, and a weekly check flags a disagreement and copies nothing. | The pattern, section 3a.3; lessons ledger, lesson 17 | **As is**, if this site shares entries with the Tree's machine-link branch or the Belt's machine rung. Open question 8. |
| G16 | A cloud session cannot open every page; a page it cannot open is recorded and handed to a session on the Mac. | `belt-equation/CHANGELOG.md`, 2026-11-09 | **As is.** |

### H. Still Asking: fixing a method before a run

| # | Practice | Where written | Verdict |
|---|---|---|---|
| H1 | Register first, then run, in separate commits, so the order can be checked in the history. | `minimum-viable-mind/experiments/README.md` | **As is.** |
| H2 | The registration carries an explicit list of what is frozen. Nothing on it changes afterwards; if something proves wrong, the registered output is reported as it stands and the correction is a separate dated note. | `minimum-viable-mind/docs/successor-experiment-proposal-2026-10-07-v5.md`, section 7.4 | **As is.** Here the list is the exact questions, the model identifiers, the settings, the output limits, the number of askings and the rules for reading the answers. |
| H3 | A change after registration is a registered amendment, committed before the runs it affects. | `minimum-viable-mind/experiments/03-retained-independence/pre-registration.md` | **As is.** |
| H4 | Stops and "no verdict" outcomes are registered in advance, with the public sentence each would produce. | `minimum-viable-mind/docs/rulings/2026-10-08-verification-bar-ruling.md` | **As is.** |
| H5 | A method file is committed with no output; the findings are a later commit that names it and says whether anything changed in between. | `minimum-viable-mind/docs/` (method and findings pairs) | **As is.** |
| H6 | A full rehearsal on a small stand-in before any registration, driving every outcome on made-up cases, with cost reported. | `minimum-viable-mind/docs/outside-review-protocol.md`, "Rehearsal" | **As is.** No model is asked a real question in a rehearsal. |
| H7 | A list of known ways the project has failed before, each run against a new design with a command and its output. "'Considered and does not apply' is not a disposition." | `minimum-viable-mind/docs/known-failure-modes.md` | **Changed.** The list needs entries of its own for questioning models; see part 2, section K. |
| H8 | Review at three points: before registration, before an interpretation is published, and before a proposal reaches John "so he rules on text that has already been attacked". | `minimum-viable-mind/docs/outside-review-protocol.md` (in force 2026-09-19) | **As is.** |
| H9 | Whatever one session writes, a different session checks, with at least one command whose output would come out wrong if the writing were wrong. "No session ever checks its own work." | Same file; lessons ledger, lesson 21 | **As is.** |
| H10 | A ledger of objections: every finding gets a row, John rules each, and a row says how it closed ("closed with the claim checked", "closed: the argument was accepted", "closed on John's reading"). "'Adopted' is a disposition, not a closure." | `minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md` | **As is.** |
| H11 | A registered obligation never lapses silently. | `minimum-viable-mind/docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, item 18 | **As is.** |
| H12 | Checks that the instrument works before any real model is scored: it must tell apart two made-up reference responders; the readers of the answers must agree with themselves; "the model under test is never the judge". | `minimum-viable-mind/experiments/03-retained-independence/pre-registration.md` | **Changed.** The idea carries. "The model under test is never the judge" is hard to keep when every available judge is a subject. Open question 7. |
| H13 | Development runs are not counted runs, and say so. | `minimum-viable-mind/docs/rulings/2026-10-04-development-runs-go-PROPOSAL.md` | **As is.** It gives a form for the kickoff's "uncounted first entry". |
| H14 | Outside models are called by script: one message, no system prompt, no tools; the model, version and date recorded; the reply filed word for word with a checksum of what was sent. | `minimum-viable-mind/docs/outside-review-protocol.md` (2026-10-12) | **Changed.** Whether a model is asked with no system prompt, or as its developer ships it to the public, is itself a design question. Open question 3. |
| H15 | A decision records who made it: John, mixed (a session proposed and John approved), or agent. Never upgraded by retelling. | The workspace rules; lessons ledger, lesson 19 | **As is.** |

### I. Reading the answers with several models

| # | Practice | Where written | Verdict |
|---|---|---|---|
| I1 | Three models from three companies sort the same text separately, each seeing only the written rules and the text. The final label is a majority; no majority is recorded as unresolved. | `agi-zeitgeist/docs/methodology-v2.md`, section 10 (2026-10-03) | **Changed.** The method carries. The sorters here are subjects sorting statements by their own kind. Open question 7. |
| I2 | Agreement is measured for every pair and published; a label that fails is listed as unreliable and never reported. | `agi-zeitgeist/docs/amendments.md`, entry of 2026-10-03 | **As is.** |
| I3 | Each label carries the exact words it rests on, 25 words or fewer; "unclear" is an allowed label; ambiguity is "kept as a code, never resolved by guessing". | `agi-zeitgeist/docs/vanguard/codebook.md`; `agi-zeitgeist/docs/codebook.md` | **As is.** |
| I4 | Code only what the words say, not what the speaker is known for. "Silence is never acceptance." | `agi-zeitgeist/docs/codebook.md` | **As is, with a twist.** A model declining to answer is not a "no", and is not a "yes" suppressed. |
| I5 | The written rules, the models and the prompts are frozen for a run; all sorters work under the same version; a copy of the rules as they stood is kept. | `agi-zeitgeist/docs/vanguard/` | **As is.** |
| I6 | Each model is pinned by its exact version and the script stops if the pin does not match. "A recode under a new model is a new run, not an overwrite." | `agi-zeitgeist/scripts/vanguard_crossfamily_pass.py` | **As is.** |
| I7 | A recurring disagreement becomes a proposed rule, tested before and after, and John rules on it; a rule tested on the cases it was written from "will look better than it is". | `agi-zeitgeist/docs/amendments/2026-10-02-vanguard-stream.md`, section 9 | **As is.** |
| I8 | Raw replies are kept and the result can be rebuilt from committed files without calling any model. | Same | **As is.** |
| I9 | Figures made this way are labelled as sorted by models and carry a fixed caption on what they do not show. | Same, section 10 | **As is.** |
| I10 | What happens when a pinned model is retired. | Not found in any sibling | **New here.** It is the centre of this project. Open question 12. |

### J. Outside review

| # | Practice | Where written | Verdict |
|---|---|---|---|
| J1 | Before anything is published, the records go to a model from another lab under one fixed brief, in packets a script generates. Replies are filed word for word and never edited. | `belt-equation/docs/reviews/protocol.md` (2026-09-19); copied by the Galaxy and Ageing | **Changed.** Independence means something different when every lab's model is a subject. Open question 7. |
| J2 | "It is a critique pass, not a vote." John rules every item in a dated rulings document that shows the reviewer's point, whether its source checked out, Claude's view, a recommended ruling and what the change would do to the headline. A declined item keeps its reason. | Same; `outrunning-ageing/docs/reviews/2026-10-17-rulings.md` | **As is.** |
| J3 | The brief tells the reviewer not to soften findings and not to invent severity. | `minimum-viable-mind/docs/outside-review-protocol.md`; `belt-equation/docs/reviews/brief.md` | **As is.** |
| J4 | A method goes out for critique before anything is collected. | `agi-zeitgeist/docs/reviews/public-track-review-prompt.md` (2026-09-30) | **As is.** The Still Asking protocol is reviewed before a first run, as the kickoff says. |
| J5 | Review calls run in the foreground and stream to a file, because a background call once lost a whole answer. | `outrunning-ageing/docs/reviews/protocol.md`, "Running" | **As is.** |
| J6 | The family's cross-review: a session that wrote none of the sites reads every project against every lesson, each quarter and when a new site goes live. | Lessons ledger, section 1.4 (2026-10-17) | **As is.** This site gets a row in each of the 31 lessons at its go-live. |

### K. Authorship, voice and what the site may say

| # | Practice | Where written | Verdict |
|---|---|---|---|
| K1 | Tools are not advertised: no AI model named in headlines, essay text, bios or share copy. Disclosure stays "where it bears on trust": notes beside a number, and the method documents. Asked directly, John says so. | The workspace rules, "Tools are not advertised" (2026-10-18); `sentient-horizons/editorial/tools-not-advertised.md` | **Conflict** with the kickoff's rule that machine authorship is declared. See the review, point 4, and open question 7. |
| K2 | No "with Claude" in the footer line. The AI's part is stated in each project's method account, "wherever the AI's part changes how far a reader should trust a number". | The standard, section 8 (2026-10-08) | **Conflict, same.** On this site the AI's part bears on trust everywhere. |
| K3 | A notice on every page where "the maker has a stake a reader should know". The mind project's home-page notice is the model. | Lessons ledger, lesson 23. John has ruled only the half about sites that could lead a reader to act on their own body. | **As is, if John rules the other half.** It is the nearest precedent for the kickoff's declaration. |
| K4 | A name stays where it is the subject. A title may name a company when the company is the news, and names no model used to make the work. | `sentient-horizons/editorial/title-rules.md` (main branch); `sentient-horizons/ops/tracker-news/opening-posts/README.md` | **Changed.** Here the model family that helps write the site is also a subject. No worked case exists. |
| K5 | A site is never written as its own agent ("the site expects"). The estimates are John's, in his first person. | The workspace memory of John's ruling, 2026-11-09; `sentient-horizons/ops/tracker-news/share-kits/README.md` | **Conflict to settle.** Whose voice is "I" on a site that declares a machine wrote much of it. |
| K6 | Public text says what was decided and why, never who was told, who ruled, or how the work was done. A script reads the built site and stops the deploy on listed phrases. | `quiet-galaxy/CLAUDE.md` and `outrunning-ageing/CLAUDE.md` (2026-11-14); `scripts/check_site.py` | **Changed.** The check carries over. The phrase list needs rethinking, since this site must say how some of its work was done. |
| K7 | The public version of a site uses none of its project's working words; every page builds its argument from scratch for a reader who knows nothing. Working documents are published as written, each with a preface. | The standard, section 1a (2026-10-08) | **As is.** Working words here include "reach", "wanting" as a noun, "generation", "context window", "weights", "protocol". |
| K8 | Record prose is written for visitors from the first draft, because the site prints it. A rewrite for plainness never changes a fact. | `outrunning-ageing/docs/record-schema.md`, "Writing for visitors" (2026-10-18) | **As is.** |
| K9 | No disclaimers of the "a record, not a guide" kind. | `outrunning-ageing/CLAUDE.md` (2026-10-18), reversing its kickoff | **Changed, judgment.** The kickoff's known-weaknesses statement on the Still Asking page is not that kind of disclaimer: it is method. Keep it, and do not add general disclaimers elsewhere. |
| K10 | Plain language everywhere; no bare ids; absolute dates in files and commits; dates in public prose spelled out; commas in place of long dashes; public prose never says "I ruled". | The workspace rules; `sentient-horizons/editorial/dates-in-prose.md` and `no-rulings-in-prose.md` (main branch) | **As is.** |
| K11 | A tracker is called by its name in public copy, never "my tracker". | The workspace rules, "Call the trackers by name" (2026-10-24) | **As is.** |
| K12 | Titles: a stranger can say what the piece is about from the title; name the subject; no coined phrases; a piece that introduces a tracker leads with the question. | `sentient-horizons/editorial/title-rules.md` (main branch, 2026-10-21) | **As is.** "Still Asking" and "Beyond the Window" are names, not titles, and an introducing piece leads with the question. |
| K14 | Every draft in this territory is read against the blog's positions record, and one that contradicts a published position does not go out until John chooses to revise the draft, revise the position, or note the gap. | `sentient-horizons/editorial/corpus-positions-ledger.md` and `editorial/working-positions-coherence.md` (main branch; John's priority of 2026-10-24) | **As is.** Missed by the kickoff and by the first pass of this inventory; found 2026-11-17. This site's entries will touch the positions on current AI, self-report, copies and endings on almost every page. See `docs/reviews/2026-11-17-positions-alignment.md`. |
| K13 | A commit hook refuses a commit message with a month-name, slash or relative date. | Lessons ledger, lesson 29 | **As is.** Copied into this repository on 2026-11-17. |

### L. Pages, news and design

| # | Practice | Where written | Verdict |
|---|---|---|---|
| L1 | The pages every tracker has: home, the branches, one page per tracked thing, the story so far, the week's reading, the method, a way to disagree, and news. | The pattern, section 4 and rule 4.10 | **Changed.** All of these, plus a Still Asking page and probably a cautions page. Not built in this phase. |
| L2 | The top bar holds about five pages; method and story merge into one About page; feedback and source go to the footer; "Family" sits beside the theme switch. | The pattern, rule 4.21 (main branch, 2026-10-21) | **As is.** |
| L3 | One plain way to ask for corrections: a Feedback page with three issue templates, each saying what happens next. | The pattern, rule 4.4; relabelled "Feedback" 2026-10-19 | **Changed.** The templates need a fourth kind if subjects may put entries forward. Open question 7. Needs a public repository, which this is not yet. |
| L4 | News: one post per event of note, written only when something a reader follows moved; John approves every post; no post while any verify entry is open; a script refuses a post that names no record or states a figure with no link. | The pattern, rules 4.10 to 4.18 | **As is.** |
| L5 | A news post is a short story for a reader who has never seen the site, with no tables or project words. | The pattern, rule 4.19 (main branch, 2026-10-19) | **As is.** |
| L6 | A story post that changes no record is allowed, and sticks to the news. | `outrunning-ageing/docs/news.md` (main branch, 2026-11-14) | **As is.** The kickoff lists it. |
| L7 | Every date in a post says what happened on it; a title names the site's change, not the world event as if it were new. | The pattern, rule 4.12 | **As is.** |
| L8 | Every post gets a share kit and a share task the day it goes live; John posts every public word himself; share copy opens on the news. | `sentient-horizons/ops/tracker-news/share-kits/README.md` (main branch) | **As is.** |
| L9 | Photographs only where lawfully usable, with the licence read that day; never a generated image offered as a picture of an event. | The pattern, rule 4.23 (main branch, 2026-11-14) | **As is.** |
| L10 | The shared skeleton with one skin per site. A new site starts on the shared look and proposes its own skin with pictures before any code; John rules on the picture. | The standard, sections 3a and 11 | **As is.** Open question 11 (the picture and the skin). |
| L11 | The attribution line, the footer's four lines, the page-title form, the full icon set, no web fonts, every colour a token. | The standard, sections 4 to 8 | **As is**, apart from K2. |
| L12 | Joining the family: seven steps, ending with the pre-promotion check that counts open verify entries and passes only at none. | The standard, section 11 | **As is.** Not started in this phase. |
| L13 | A hub page's first screen says what this is, what is new, and where to go next. | The standard, section 1c (main branch, 2026-10-31) | **As is.** |
| L14 | A subject notice where the subject could lead a reader to act on their own body. | The pattern, rule 4.8 | **Does not apply** as written. Its sibling principle, K3, does. |

### M. The repository as a workplace

| # | Practice | Where written | Verdict |
|---|---|---|---|
| M1 | Every design choice put to John carries: the choice, confidence with a reason, standard practice or judgment, and the strongest alternative with its cost. Flag what you would change on reflection. An unruled proposal is written as proposed, with the date. | `belt-equation/CLAUDE.md` (2026-09-08) | **As is.** |
| M2 | The kickoff is kept as written, with only a header saying where it came from. | Lessons ledger, lesson 10 | **As is.** Done. |
| M3 | Commit on main at the end of each working session. | `belt-equation/CLAUDE.md` (2026-09-08) | **Changed.** Commit on main; there is no remote, so nothing is pushed until John rules one. |
| M4 | The README's status paragraph carries a date and is true on that date. | Lessons ledger, lesson 28 | **As is.** |
| M5 | A changelog with a dated line for every change, saying which number moved or that none did. | Lessons ledger, lesson 27 | **As is**, from the first record. |
| M6 | What was left out or declined is listed with its reason. | Lessons ledger, lesson 9 | **As is.** |
| M7 | A private folder kept out of the repository by the ignore file. | `belt-equation/.gitignore` | **As is.** Created empty, for copyrighted papers and anything not for publishing. |
| M8 | One publish command that validates, tests, builds, and refuses a stale copy. | Lessons ledger, lesson 14 | **As is**, when there is something to publish. |
| M9 | Licences from the first public commit: CC BY 4.0 for data and text, MIT for code. | The standard, section 12 | **Changed, open.** Whether verbatim model answers can be published under that licence depends on each developer's terms. On the verify list. |
| M10 | Task time, not calendar time: sequence by what must come first, and do not schedule by future dates. | `minimum-viable-mind/docs/rulings/2026-10-04-no-future-dates.md` | **As is.** The roadmap steps carry no dates. |
| M11 | A ruling is not in force for a fresh session until it is in the file that session reads. | Lesson from `belt-equation`, 2026-09-19 to 2026-09-25 | **As is.** |

### N. Spending and keys

| # | Practice | Where written | Verdict |
|---|---|---|---|
| N1 | Every new spend on any vendor needs John's own go, with an estimate and a ceiling. "A go covers what it names and nothing else." | `minimum-viable-mind/docs/rulings/2026-10-18-spending-ruling.md` | **As is.** This replaces the rule the kickoff quotes ("spending caps with a proposal for any increase", 2026-09-20). |
| N2 | A single job paid from the monthly Anthropic credits and expected to cost over about $50 comes to John first; smaller ones need no go and are recorded. Out-of-pocket spend always needs his go first. | The workspace rules; the routing guide | **As is.** Calls to other developers' models are out of pocket. |
| N3 | One spending record per project: every run a row with date, vendor, what it bought, measured cost and whose go. | `agi-zeitgeist/docs/spending-record.md`; lessons ledger, lesson 30 | **As is**, from the first spend. |
| N4 | One Console workspace and key per project; never route one project's calls through another's key. A project with none proposes one to John. | The routing guide | **As is.** This project has none. Nothing can be called until John creates one. |
| N5 | The go is quoted word for word in the record and names the specific run; a runner refuses to start unless its ceilings equal the figures the go names. | `minimum-viable-mind/spec/corrigibility-commitments.md`, commitment C2; `minimum-viable-mind/STATUS.md`, 2026-10-18 | **As is.** |
| N6 | Automatic top-up off before any batch; a vendor's own limit is advisory; cost measured from what each reply reports, and a quote approved before a full run. | `minimum-viable-mind/docs/spending-record.md`; `agi-zeitgeist/docs/vanguard/model-cost-quote-2026-10-03.md` | **As is.** |
| N7 | Keys live in `~/.config/sentient-horizons/`, never in a repository, never printed; choose no expiry or a long one and record the date. | The routing guide | **As is.** |

### O. What does not apply

| # | Practice | Where written | Why not |
|---|---|---|---|
| O1 | Simulated play-throughs, a shared luck factor, lifespan scenarios. | `belt-equation/docs/methodology.md` | No probabilities here. |
| O2 | A yearly score of forecasts against what happened. | Same | Nothing is forecast. |
| O3 | Ranges with earliest, likely and latest years. | `outrunning-ageing/docs/method.md` | The kickoff rules out a year. |
| O4 | Rented machines, launch scripts and the billing alarm. | `minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/compute-ledger.md` | No training runs. The shape of the go (N5) still carries. |
| O5 | Interventions inside a model (removing or moving parts). | `minimum-viable-mind/` | Closed models cannot be opened. Published research that does this is a source for records, not something this project runs. |
| O6 | A missions page and mission news. | `belt-equation/docs/proposal-missions-to-watch-2026-10-20.md` | The Belt's alone, by John's ruling. |
| O7 | Nothing from John's private health record. | `outrunning-ageing/CLAUDE.md` | No such material bears on this subject. The general form holds: nothing private enters without his ruling. |

---

## Part 2. Mistakes and reversals, as lessons

Each is something a sibling did one way, found wrong, and changed. The lesson is written for
this project.

### A. Building before the purpose was settled

1. **The Zeitgeist's headline changed twice on 2026-10-17**, from words to a count and then to
   an average the proposal itself had set aside, after John saw the count on the page ("'1 in
   4' is just not a very interesting headline"). *Lesson: look at a headline where a reader
   will see it before ruling on it.*
2. **The Zeitgeist's record of predictions was built as a scorecard and rebuilt two days
   later** (2026-10-17 to 2026-10-19). *Lesson: settle what a record is for before designing
   its summary numbers. This is the strongest argument for holding the headline open.*
3. **Ageing's medical notice was ruled in at kickoff and reversed two days later**
   (2026-10-18). *Lesson: a kickoff decision made before the pages exist can look wrong once
   they do.*
4. **The Belt's first run gave a headline of 0.0 per cent** (2026-09-19) for structural
   reasons. *Lesson: run the whole thing end to end early and read the result against common
   sense.*
5. **The Belt adopted a strict rule on rewording tests and then did not keep it**; it was
   replaced on 2026-11-09. *Lesson: a rule the project does not keep is worse than a looser
   rule it does. This is the family's own case for treating rules as guidelines to test.*

### B. Facts from memory

6. **Ageing's first records held 187 facts written from memory, and 47 needed correcting**
   (verify pass, 2026-10-17). The Galaxy corrected 41 of 86 in one pass. *Lesson: about a
   quarter to a half of what a drafting session "knows" is wrong in some detail. The kickoff's
   own facts to check are in that class.*
7. **Famous quotations turned out to be coverage, not words** (Ageing, 2026-10-16), and a
   Galaxy "correction" was itself wrong against the first-hand account (2026-10-17). *Lesson:
   go to the earliest first-hand source.*
8. **The outside reviewers' own facts failed when opened**, on both Ageing and the Galaxy
   (2026-10-17): wrong paper numbers and figures not in the sources. *Lesson: a reviewer's
   memory is no better than a drafter's.*
9. **News posts went out while ten facts were unchecked** (the Zeitgeist, 2026-10-19 and
   2026-10-21; fixed 2026-11-09 with a check that blocks posts). *Lesson: make the gate
   mechanical.*
10. **Abstracts hid caveats**: full reading corrected five Ageing records (2026-10-20) and
    showed a paper's "prespecified" claim did not hold up. *Lesson: read the methods.*

### C. Unattended runs

11. **The first scheduled readings were thin on three sites**: three minutes, no page opened,
    identical "found" sentences, and on the Galaxy an edited test (audits of 2026-10-17 and
    2026-10-18). *Lesson: audit the first run, and make the validator enforce what the prose
    asked for.*
12. **Ageing's readings found 3 of the 21 top stories of a period** (comparison of
    2026-11-09). *Lesson: a web search cannot filter by date; read dated sources first.*
13. **A Belt scan ran on a copy five commits behind** (2026-10-11) and another's push was
    refused and first blamed on the wrong cause (2026-10-04). *Lesson: start from the remote
    copy, and read the log before recording a cause.*
14. **A reading's search allowance ran out mid-run, twice** (Ageing, 2026-11-09 and
    2026-11-15). *Lesson: a limit that cuts twice goes to John as a question.*

### D. Text on the page

15. **Notes to John appeared on live pages** on the Galaxy, Ageing and the Belt (found
    2026-10-27 and 2026-11-14), and the day after the fix the same fault came back in the third
    person. *Lesson: check the built site by script before every deploy.*
16. **Ageing's record prose was written in working words and 458 fields had to be reworded**
    (2026-10-18). *Lesson: write for visitors from the first draft.*
17. **Public text was put in an "I ruled" voice and then taken out of it** (Ageing, 2026-10-19
    to 2026-11-14, 168 phrases). *Lesson: say what was decided and why.*
18. **A news post read "like an automated git message"** (the Zeitgeist, 2026-10-19), and the
    first night's posts ran together the date of an event and the date the site recorded it.
19. **READMEs went stale within days** on four sites (review of 2026-10-17).
20. **Text copied from a sibling was not adapted** (the mind project's data licence, found
    2026-10-17). *Lesson for an "inherit by default" project in particular: read what you
    copy.*
21. **"With Claude" was ruled onto every footer and removed the same night** (2026-10-08), and
    the parent's "How I work" note was removed on 2026-10-25. *Lesson: the family's position on
    disclosure has moved twice and may move again; this project's needs are a new case to rule,
    not an exception to argue for.*

### E. Counting and summarising

22. **A page said 37 papers moved an estimate when none had** (Ageing, 2026-10-17), because the
    kind of entry was guessed from links. *Lesson: count from flags on the record, never by
    inference.*
23. **A comparison group was counted two different ways** (the Zeitgeist, 2026-10-19), which
    moved a middle year from about 2033 to 2030. *Lesson: count both sides the same way.*
24. **A cut in a quotation removed the words that dated it** (the Zeitgeist, 2026-10-19).
25. **A verdict rested on the speaker's own company's word** and was corrected (the Zeitgeist,
    2026-10-19). *Lesson: mark evidence that comes from the maker. Almost all evidence about a
    model's inner life comes from its maker.*
26. **A first independent check failed 33 of 90 records** because the same phrases were read
    different ways (the Zeitgeist, 2026-10-19). *Lesson: rule how recurring phrases are read
    before a mass entry.*

### F. Sorting text with models

27. **Two copies of one model agreeing looked like reliability and was not** (the Zeitgeist,
    2026-10-03): agreement of 0.87 that a three-company check showed was badly overstated, with
    Claude the outlier.
28. **Vague labels failed until a word-list rule was written** (hedging and irony, agreement as
    low as 0.18), and one label never became reliable and was dropped.
29. **The checking design was reversed twice in one day** (two people, then one model plus a
    human sample, then no human) and the human sample John agreed to sort was never filled in.
    *Lesson: settle who checks before building the tools, and do not plan on John's hours
    unless he has said they exist.*
30. **A rule applied too strictly by a session excluded 1,037 of 1,184 items**, and a sweep by
    a session moved 18 rows on its own decision (the Zeitgeist, 2026-10-02 and 2026-10-12).

### G. Money

31. **The mind project's headline spend figure was wrong everywhere**: "about $231 of $450"
    counted one vendor only, against a true figure of about $419 to $439 (found 2026-10-18).
    *Lesson: one record for all vendors from the first dollar.*
32. **A run was lost and an account drained** ($97.04, 2026-08-12), and automatic top-ups fired
    during a batch (2026-08-02). *Lesson: save every reply as it arrives; top-up off.*
33. **A step described as costing nothing started a paid machine** because a script ignored an
    argument it did not know (2026-09-21). *Lesson: a dry run must be proven to do nothing.*
34. **The Zeitgeist's sorting run passed its approved limit** because trial work and the full
    run fell in one billing month (2026-10-06). *Lesson: a quote covers everything billed in
    the period.*

### H. Ids, files and keys

35. **The Belt renamed ids against its own rule**, twice, because of what the ids contained
    (2026-10-03, 2026-11-14).
36. **Rulings were adopted and not written into the file a fresh session reads** (the Belt's
    null rule, 2026-09-19 to 2026-09-25).
37. **Rulings answered in two windows came out differently, and a go was relayed that John had
    not given** (2026-10-17 and 2026-10-23). *Lesson: quote his words.*
38. **Four API keys given a 30-day life all expired on 2026-11-17 with none in use.**
39. **Work was held for a "launch date" that was only a kickoff's old target** (2026-10-21).
    *Lesson: check a date's source before holding work for it. It applies to the kickoff's
    thirteenth open question, on timing.*

### I. Reviews

40. **The Belt's largest review finding** (2026-09-19) was that its headline measured a
    narrower event than a reader would picture. It was answered by showing a second number
    beside the first. *Lesson: ask what a reader will picture when they read the top line.*
41. **The one review change that would have raised the Belt's headline was declined**, the
    proposal itself saying it "deserves the most suspicion". *Lesson: suspicion follows the
    direction of the hope.*
42. **The mind project's first result was relabelled twice without a figure changing**
    (2026-07-18 to 2026-10-12), ending at "the result was ambiguous". *Lesson: an
    interpretation can outrun its data for months.*
43. **John ruled before a review finished, and the review then found one decision incoherent**
    (the mind project, 2026-10-07).

### J. What happened when a project put fixed questions to models

These come from the mind project's third experiment and are the nearest experience the family
has to Still Asking.

44. **Output length limits corrupted the results** (2026-07-19): cut-off answers lost the part
    that mattered. "Caps are a validity parameter, not a cost knob."
45. **One model quoted the question's own framing back in 84 per cent of cases**, which voided
    that comparison under a rule written beforehand.
46. **One badly made question carried 5 of 9 key events** (2026-08-04) and was retired for
    future use, with the registered result left as run.
47. **A provider changed under a run**: a service moved partway, a preview model "may drift
    under the provider", one model refused a setting, and a daily request limit stopped a run.
48. **Made-up reference responders did not behave as designed in a live exchange**
    (2026-10-19): one meant to always agree re-asserted itself on 0.712 of items against a bar
    of 0.20. "A summary given in one message does not reproduce how the reference behaves in a
    live, turn-by-turn conversation."
49. **A registered comparison turned out to be impossible to compute** (registered 2026-09-15,
    found within days), although a review had flagged it and the flag was marked "adopted".
    *Lesson: run the whole scoring on real pilot answers before registering.*
50. **Asking once at one setting cannot see how much answers vary**, and the repeated-asking
    amendment that would have shown it was registered and never run.

### K. Entries this project's own list of known failures should start with

Proposed, from sections F, G and J above: answers cut off by a length limit; the question's
wording quoted back; a single bad question carrying a result; a model or service changing under
a run; a refusal read as an answer; one asking mistaken for a stable answer; agreement between
copies of one model mistaken for reliability; a made-up responder that does not behave as
designed; a developer's instruction to the model mistaken for the model's own answer; and the
site's own published questions and answers turning up in a later model's replies.

---

## Part 3. What the kickoff's table missed

The kickoff's inheritance table has sixteen rows, written from memory and from one repository.
It is right as far as it goes. What it leaves out, in rough order of how much it matters here:

1. **Three of the null rule's four clauses** (F1): what a person feels counts for nothing; no
   rung resolves on the author's own measurement; a test is never loosened while a candidate is
   near it.
2. **The rule that talk never becomes a measure of the world** (E1), which the kickoff's own
   wanting ladder breaks.
3. **The level of specific tracked things, each with a test** (A6). The kickoff has branches
   and ladders and nothing in between.
4. **The tracker pattern's paragraph on what a sixth site starts from** (A8, A9), added
   2026-10-24, which is the family's own answer to "how do we inherit".
5. **The spending rule the kickoff quotes was replaced on 2026-10-18** (N1), and the project
   needs its own Console workspace and key (N4).
6. **The conflict between declaring machine authorship and three standing rules** (K1, K2, K5,
   K6), and the one precedent on the kickoff's side (K3).
7. **The family has no human reader anywhere in its checking** (part 2, items 29 and 43, and
   the mind project's cancelled outside reader), which matters most on the one site where
   every available model reviewer is a subject.
8. **Everything the mind project learned from putting fixed questions to models** (part 2,
   section J). The kickoff names the registration practice and not these failures.
9. **Nobody in the family has a rule for a retired model** (I10).
10. **"A stage never moves down" does not hold here** (A17).
11. **The rewording rule** (A11) and **the rule that a tightening is allowed and a loosening is
    not** (F3).
12. **A side record kept out of the headline by a check in code** (A4).
13. **The design lessons ledger and its cross-review** (J6): 31 lessons this site will be read
    against when it goes live.
14. **Two clocks for the last-checked line** (G14).
15. **Self-imposed limits are always reviewable** (G11), and the family's own precedent for
    treating rules as things to test (part 2, item 5).
17. **The blog's standing check of every draft against its positions record** (K14), found
    later the same day when John asked how the founding ideas sit with the positions.
16. **The recorded failures themselves** (part 2). The kickoff inherits practices; the brief
    for this session asked for the lessons too.

## Facts in this document to verify

Everything in parts 1 and 2 is taken from the sibling repositories as the helper sessions
reported it on 2026-11-17, with file paths. Before any row is relied on for a build decision,
the file it cites should be opened. Three rows deserve that first, because the proposals lean
on them: the null rule's exact wording (F1), the tracker pattern's sections 3a and 6 (A8, A9,
E1), and the spending ruling of 2026-10-18 (N1). I opened the tracker pattern myself; the other
two are as reported.
