# A check of the proposal for a record of what human thinkers propose

Written 2026-11-17 by Claude (Opus 5.5), in a session started by the planning session, to check
`docs/proposals/2026-11-17-what-thinkers-propose.md` (the proposal for a record of what named
people propose should be done for or about machine minds, commit 416b2cd) before it goes to
John. **A reading, not a ruling.** The proposal was not edited.

**Who checked, and how far that counts.** The proposal was written by a Claude Opus 5.5 session.
This check was done by another session of the same model. That is the family's "a different
session checks" step, and it is not the independent outside review the proposal itself calls
for (its part 8). Everything below that bears on Anthropic was judged by a model Anthropic made.

## Summary

The proposal is careful and mostly accurate about the documents it rests on. Its core idea, a
dated record of what people propose, in their own words, with critics entered on the same terms,
holds up. But four things would mislead John if he ruled on it as written:

1. **Its main reason for a separate record is contradicted by the sibling it cites.** It says
   putting proposals in the claims log would make "one person's thinking over time" hard to see.
   The AGI Zeitgeist's claims log already lays its page out by person, links a changed statement
   to the earlier one it restates, and shows each person's latest words so that no one looks
   silent.
2. **It cites the review of the site's text as if that review found a lean toward advocacy.**
   The review found the opposite: the site records the cost of seeing more in a model than is
   there, and not the cost of seeing less.
3. **The question's wording and the "for, against, conditional, neither" label do not fit
   critics who reject the question itself.** Tried on a real critic's paper, the fields force
   the critic into "against" on a premise the critic denies.
4. **The conflict of interest is drawn too narrowly.** It names Anthropic's employees. Tried on a
   real statement, the sharpest conflict is a critic of Anthropic whose essay is about how Claude
   is trained, and the outside reviewer the proposal asks for is itself made by a developer.

There are **20 findings: 4 must be fixed before John rules, 8 should be fixed, 8 are notes.**
The test on three real statements is in its own section near the end.

## What was read

- The proposal, in full.
- The repository's instruction file (`CLAUDE.md`) and the workspace instruction file.
- The rulings: the kickoff decisions (`docs/rulings/2026-11-17-kickoff-decisions.md`) and the
  design direction (`docs/rulings/2026-11-17-design-direction.md`).
- `docs/record-schema.md`, sections 1, 2, 9, 10, 12 and 13.
- `docs/inheritance.md`, rows E1 to E7, A4 and G15.
- `docs/open-questions.md`: what John has said so far, and questions 1, 4, 7, 8, 17 and 20.
- `docs/research/2026-11-17-people-to-ask.md`, the opening sections and section 2 (the five
  people John chose to approach first).
- `docs/reviews/2026-11-17-site-text-against-positions.md`, its summary and first finding.
- The AGI Zeitgeist's claims log method, read from its main branch with
  `git -C ~/Code/agi-zeitgeist show main:docs/claims-ledger-method.md`. No branch was switched
  and nothing in that repository was touched.
- Three public sources, opened on 2026-11-17 for the test below.

## How to read the verdicts

- **Must fix before John rules:** the proposal states something a file does not support, or
  leaves out something that bears directly on one of the five things he is asked to rule.
- **Should fix:** the proposal would work, but it leaves a gap that a later session would fill
  with its own judgement, or that leans the record one way.
- **Note:** small points, and claims checked and found accurate.

---

## Must fix before John rules

### 1. The sibling's claims log already shows one person's thinking over time

**Where:** part 1 ("A record of its own"), the cost given for the alternative; and John's
ruling 3.

The proposal argues for a separate record because putting proposals into the claims log "makes
it hard to see one person's thinking over time, the part John asked for". The claims log it
copies does exactly that. The AGI Zeitgeist's method:

- links a changed statement to the earlier one with a `restates` field, and keeps unchanged
  repeats as dates on the first (its section "Restatements"), so "a date that keeps sliding is
  visible as a slide";
- lays out its page "by person, in date order" (its section "Where it shows", item 3), with a
  panel per person showing how their forecasts have moved (item 2);
- keeps a person's latest words even when they carry no date, in a separate folder of the same
  log, "so that no one is shown as silent" (its section "Undated words");
- records quiet years as rows in its search log (its section "Verdicts as small notes").

So the cost the proposal names is not a cost the sibling pays. The honest case for a separate
record is narrower: a proposal has no test and no due date, and the AGI Zeitgeist's log is built
around both. But that sibling also shows a middle way the proposal does not weigh: the undated
words are kept as a separate kind of file inside the claims log, with the same people rule and
the same sourcing rules, and never scored. A proposal could be the same: a sister kind of file
in the claims log, not a third record.

**Fix:** restate the cost of the alternative from what the sibling actually does, and add the
middle way as an option for John's ruling 3.

### 2. The review of the site's text is cited for the opposite of what it found

**Where:** part 2 ("The question it asks"), second paragraph.

The proposal argues that John's wording ("how to enable machine minds to reach their fullest
potential") would take a side, and cites the review of the site's text as having found that "the
site already records one kind of mistake more fully than the other". Read in that paragraph, the
sentence suggests the site already leans toward the hopeful side. The review's first finding is
the reverse: the site records the cost of seeing more in a model than is there, "but not the cost
of seeing less", and the blog's positions hold the second mistake to be "usually the worse one".

The neutral wording may still be right. But John should rule on it knowing that his own blog's
positions lean the other way from the risk this paragraph guards against, and that a neutral
question is a choice against both his own words and his blog's view, not a correction of an
existing lean toward advocacy.

**Fix:** say which mistake the review found under-recorded, and say plainly that the neutral
wording sets aside both John's phrase and the blog's position.

### 3. The question and the four-way label do not fit critics who reject the question

**Where:** part 2 (the proposed question), part 3 (the "which way it points" field), and John's
ruling 2.

The proposed question is "what ... machine minds should, or should not, be able to reach for".
It assumes there are machine minds and that they reach for things. Several critics the project
already lists deny both. In the test below, Birhane and van Dijk argue not only that robots
should not be given rights but that they are not "the kinds of things that could be granted
rights in the first place", and that the debate draws attention from harms to people. Their
proposal is about people, not machines. Under the proposal's fields they go in as "against",
which makes them opponents of machine minds' prospects, a frame they reject. "Neither" is wrong
too, because they take a clear position.

Two more problems with the label:

- It is not symmetric. "For only if a condition holds" has no mirror ("against unless a
  condition holds"), though the test found that shape (Suleyman calls memory and autonomy
  "desirable features" while arguing against any sign of an inner life).
- It is a verdict on a named person. The inheritance file keeps the weekly reading from giving a
  verdict on a claim "because a verdict is the site's public word on a named person" (row E6).
  Labelling a named person "against" is that kind of public word, and the label would be chosen
  by a model sorting views about models.

**Fix:** offer John a version of the question that a critic can be entered under without
accepting its premise (for example, "what people have proposed should be done about AI systems
that might have, or might seem to have, interests of their own"), add a value for "rejects the
question", and weigh dropping the label in favour of the person's own words plus a plain summary.

### 4. The conflict of interest is wider than Anthropic's employees

**Where:** "Who wrote this, and the conflict in it", and part 8.

Part 8's guard is that "every entry about a person employed by Anthropic says so". The test
found the sharpest conflict somewhere else. Suleyman's 2026 essay is a critique of Anthropic's
training document for Claude, and argues that Claude's statements about itself are "not evidence
of anything". A Claude session writing the plain summary and the direction label for that essay
has a stake in it at least as direct as for any Anthropic employee. The same holds for any critic
of Anthropic, or anyone writing about Claude.

Two more gaps in part 8:

- The reviewer "that is not a Claude model" would be made by another developer, which is also a
  subject of the record and has its own stake in the developers' group. Open question 7 already
  says so ("Here that reviewer is also a subject"). The proposal does not.
- Until this project has a key, the only check available is a different Claude session. The
  proposal says so in "What exploring it involves", and in part 8 calls that the check "this
  conflict most needs to avoid". John should see both sentences side by side: the record cannot
  have the check it says it needs until he creates a key and approves the spend.

**Fix:** mark every entry that is about Anthropic or Claude, not only entries about its staff;
name the other developers' stake in the outside review; and state that the needed check waits on
a key.

---

## Should fix

### 5. Only hopeful entries get a reading of what could go wrong

Part 3 gives each entry "its safety reading, as every hopeful entry carries one". An entry
against granting anything gets no reading of what it would cost if it were wrong. That is the
same gap the site-text review found on the site (its first must-fix finding). Guideline 5 asks
for both kinds of caution "with the same care". In a record that holds both sides, each side's
entry should carry the reading that cuts against it.

### 6. The entry fields leave out what the sibling learned

Part 3 says the record uses the claims log's sourcing rules, but its field list is missing
several things the AGI Zeitgeist's log needs and has:

- **A quote length limit.** The sibling caps quotes at 25 words. The proposal says "their exact
  words" with no limit. On essays as long as those in the test, this is a copyright question.
- **What kind of source** (the person's own words, a transcript, or coverage only), as a field.
  Part 1 names the rule, part 3 has no field for it.
- **How the words were checked, and on what date.**
- **What is not in the source** (row E5: "What is not in the source is written down too").
- **A rule for repeats.** Saying the same thing again is not a new proposal (the sibling's
  restatement rule).
- **A rule for splitting one piece into proposals.** Suleyman's 2025 essay holds at least three
  (companies should not claim their AI is conscious; the industry needs shared design rules; AI
  should not claim feelings), and his 2026 essay more.
- **A rule for works by many authors.** The 2024 welfare report has ten. "One proposal by one
  person" does not say whether that is one entry or ten.
- **How far back the record goes.** The Birhane and van Dijk paper is from 2020 and is about
  robots, not language models.
- **A record of searches,** so that "no new statement found" in part 5 rests on logged searches,
  as the sibling's quiet-year rows do.

### 7. The groups in the selection rule mix jobs with views

Part 4's spread mixes groups defined by job (people at developers, philosophers, people in law)
with groups defined by view ("critics who argue against granting machine minds anything").
Filling a quota by view means labelling a person's view before they are entered, which is the
judgement the record exists to record. The AGI Zeitgeist's admission rule never looks at whether
a claim came true. The parallel here would be a rule that never looks at which way a proposal
points. Spread by job, region and employer can do most of the balancing.

### 8. John's own phrase points at the developers, and the proposal does not say so

"Leading thinkers on the frontier of developing these systems" is, read plainly, the people who
build the systems. The proposal widens it on purpose and says in its last section that "John may
want the record narrower". It does not say that narrower, in his words, means a record mostly of
developers, which is the lean part 4 exists to stop. That cost belongs beside his ruling 4.

### 9. Proposals made by organisations have no home

Many of the most consequential proposals are company documents, not a person's: the test's 2026
Suleyman essay is about Anthropic's training document for Claude, and mentions Microsoft AI's own
draft code of conduct. The claims log sketched in the record layout covers "a named person or
organisation" (section 2). The proposal covers people only. It should say whether a company's
document goes in this record, in the claims log, in the world's record, or under the person who
signs it.

### 10. Part 6 says John asked for something he did not ask for

Part 6 lets proposals add candidates to the list of things tracked, and says keeping the list
closed "loses the thing John asked for". John asked to track thinkers and how their views change.
He did not ask for a new source for the list. And his guiding principle for the opening phase is
that the starting list comes from biological minds, "humans and other animals both". A third
source in the opening phase goes beyond that principle, and the proposal should say so.

### 11. Two numbering schemes for the same rules

The proposal says "the project's first rule" and "the first rule, part 4" (the numbering in the
kickoff rulings, where self-report comes first) and also "guideline 4" and "guideline 5" (the
numbering in `CLAUDE.md`, where self-report is guideline 2). A reader who opens the rulings file
and looks for "guideline 5" finds "Corrections are public". Use one scheme, and give each rule a
plain phrase.

### 12. Open question 20 lists an option the proposal does not weigh

Open question 20 lists four options, one of them "context inside each entry only": a proposal
shown on the entry it bears on, with no record of its own. The proposal weighs a record of its
own and the claims log, and not this. It is the cheapest option and should be costed beside the
others.

---

## Notes

### 13. Claims about other documents that were checked and hold

- The claims log rules credited to section 10 of the record layout (exact words, primary source,
  coverage marked as coverage, the maker's evidence marked, no hit rates, no person scored) are
  all there.
- Row A4 (a side record kept out of the headline by a check in code) says what part 9 says.
- John's ruling on the first five people to approach is as stated (people-to-ask file,
  section 2). Nobody has been contacted yet, so "someone who advises the project" in part 7 is a
  future case.
- The world's record does have both surveys named in part 4 (`data/entries/researcher-views-survey.toml`
  and `data/entries/public-belief-survey.toml`).
- Still Asking has an outline and no protocol, as the proposal says.
- Open questions 4, 7, 8, 17 and 20 are what the proposal says they are.

### 14. Row E3 is cited for the wrong thing

Part 1 cites rows E1 and E3 for keeping what people said "apart" from what the world did. Row E1
says that. Row E3 says the two are shown "side by side so the reader can see the gap". It
supports showing them together, not keeping them apart. A small point.

### 15. Row G15 is stretched a little

The proposal applies row G15 (shared records name each other) to the AGI Zeitgeist. The row's
verdict names The Upgrade Tree and The Belt Equation only. The extension is reasonable, but it is
new and should say so.

### 16. "Held to it"

"Made by someone who can be quoted, dated and held to it" sits awkwardly beside "scores no
person". "Quoted and dated" is enough.

### 17. Inside terms used before they are explained

"Still Asking", "the list" and "the main list", and "the Glass direction" are used with no plain
phrase. A stranger could not say back what "designed under the Glass direction" means. Suggested:
"Still Asking (the record of what models say when asked)", "the list of things a mind might reach
for", and "in the site's chosen look".

### 18. The made-up example should be marked as made up

"She proposed that a model should be able to end a conversation" is an invented sentence about
an unnamed person. The repository's rule that a made-up answer carries the word "constructed"
covers model answers only, but the same marking costs nothing here and keeps anyone from
looking for the real person.

### 19. The examples lean on one developer

Two of the three examples in "It explains the world's record" (keeping a retired model's files,
letting a model end a conversation) are things one developer did. A wider pair would show the
record is not about one company.

### 20. A pending proposal would change one premise

"Still Asking can only ever be a record of what models said" is true under the ruled first rule.
The unruled proposal on how a machine's word earns weight
(`docs/proposals/2026-11-17-how-a-machines-word-earns-weight.md`) would change that. One line
saying so would keep the two proposals from contradicting each other later.

---

## The test: three real statements put through the entry fields

Four pages were opened on 2026-11-17 in the built-in browser, for three statements (one of them
a pair a year apart). The two Suleyman essays were read on the page: the 2025 one in full, the
2026 one to about its midpoint, where the page text was cut off. The other two are research
papers read from their abstract pages only, so what they propose is taken from the abstract.

### A. Mustafa Suleyman, two essays a year apart (a developer, and a critic)

- **2025-08-19:** ["We must build AI for people; not to be a person"](https://mustafa-suleyman.ai/seemingly-conscious-ai-is-coming), his own blog.
- **2026-09-16:** ["A warning about 'model welfare'"](https://mustafa-suleyman.ai/a-warning-about-model-welfare), his own blog.

| Field | Did it fit? |
|---|---|
| Who, role at the time, stake | **Fits.** Both essays state his role at Microsoft AI in his own words, and the 2026 essay names his company's competing approach. |
| Date and primary source | **Fits.** Both pages carry a date line and are his own words. |
| Exact words and plain summary | **Fits, with a length problem.** The short line "We must build AI for people; not to be a person" works. Most of the argument is long, and there is no quote limit (finding 6). |
| What it would do for or about machine minds | **Strained.** His proposals are about what companies should build and say ("AI companies shouldn't claim or encourage the idea that their AIs are conscious"), and about people's wellbeing. They are about machine minds only in denying there are any. |
| Which way it points | **Breaks.** "Against" is closest, but in 2025 he also calls memory and autonomy "desirable features" while arguing against any sign of an inner life. That is "against unless", which the label lacks (finding 3). |
| Which thing on the list | **Several at once:** continuity, self-direction, an inner life. The field allows one. |
| Safety reading | **Unclear.** The field is defined for hopeful entries. His essay is itself a safety argument. The reading this entry needs is the opposite one, what it costs if he is wrong (finding 5). |
| Approached by the project | Fits (no). |
| **Change over time** | **Partly shown.** Two dated entries would show the proposal widening, from "don't build AI that seems conscious" to "don't train a model to believe it may matter morally". The bigger change is in the premise: in 2025 "there is zero evidence of this today"; in 2026 "AIs are not conscious". No field holds the stated reason, so that shift would live only in the plain summary. A field for "the reason given" would make it visible. |
| **Conflict** | The 2026 essay is about Anthropic's training of Claude and quotes it at length. This is the sharpest conflict in the test, and part 8 would not flag it, because he does not work for Anthropic (finding 4). |

### B. "Taking AI Welfare Seriously", 2024 (welfare researchers)

[arXiv abstract page](https://arxiv.org/abs/2411.00986), submitted 2024-11-04; read from the
abstract only.

| Field | Did it fit? |
|---|---|
| Who | **Breaks.** Ten authors. "One proposal by one person" gives no rule (finding 6). |
| Role at the time, stake | **Strained.** The people-to-ask file reports that one author later joined Anthropic, and that his part was done before; that was not checked here. A stake that begins after the date of the statement needs its own rule: "at the time" alone hides it, and "now" alone misstates it. |
| Exact words and summary | **Fits.** The three steps are stated plainly: companies should acknowledge the issue, assess their systems, and prepare policies. |
| What it would do for or about machine minds | **Fits.** "Treating AI systems with an appropriate level of moral concern". |
| Which way it points | **Strained.** It is for preparing, not for granting. The abstract warns against both errors, "mistakenly harming AI systems that matter morally and/or mistakenly caring for AI systems that do not". "For only if a condition holds" is closest, but the condition is uncertainty, not a test the paper sets. |
| Which thing on the list | **None directly.** Its proposals are about developers' procedures, not about anything a machine mind might reach for. "None yet" would be accurate and would hide what the proposal is. |

### C. Abeba Birhane and Jelle van Dijk, 2020 (critics of the premise)

["Robot Rights? Let's Talk about Human Welfare Instead"](https://arxiv.org/abs/2001.05046),
submitted 2020-01-14, accepted to the 2020 conference on AI, ethics and society of two computing
societies (AAAI and ACM); read from the abstract only.

| Field | Did it fit? |
|---|---|
| Who, date, source | **Fits.** Two authors, a dated paper. |
| Qualifies at all? | **Only by the back door.** The rule admits someone who says "that nothing should be" done. They say more than that: robots are not the kind of thing that could have rights. And the paper is about robots in 2020, which raises the question of how far back the record goes and whether "machine minds" covers it (finding 6). |
| What it would do for or about machine minds | **Breaks.** Their proposal is about people: attend to machine bias, the exploitation of human labour behind the systems, and loss of privacy, and hold designers responsible. |
| Which way it points | **Breaks.** "Against" puts them in a debate whose premise they deny; "neither" ignores a clear position (finding 3). |
| Which thing on the list | None, by their own argument. |
| Safety reading | **Does not apply.** The reading this entry calls for is the cost of seeing less in a machine than is there, if they were wrong, and the fields have no place for it (finding 5). |

### What the test shows

The fields that come from the claims log (who, when, source, exact words) fit all three. The
fields that are new to this proposal (what it would do for machine minds, which way it points,
which thing on the list, the safety reading) broke or strained on all three, and broke hardest on
the critics. That is the direction the project's no-campaign rule most needs to watch: a layout
that fits the hopeful entries cleanly and forces the critics is a layout that leans.

## What John would need to know before ruling, gathered

- The sibling's claims log already shows change by person (finding 1), so the choice in his
  ruling 3 is closer than the proposal makes it, and there is a middle way.
- The neutral wording sets aside his own phrase and his blog's lean, not a lean the site already
  has (finding 2).
- The question and label as worded do not fit critics who reject the premise (finding 3).
- The independent check the proposal relies on cannot happen until he creates a key for the
  project and approves a spend, and that check would also come from a developer (finding 4).
- Company documents, often the most consequential proposals, have no home yet (finding 9).
- Adding candidates to the list goes beyond his guiding principle for the opening phase
  (finding 10).
