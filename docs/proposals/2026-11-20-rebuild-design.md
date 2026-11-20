# The rebuild: a design, and the decisions it needs

**PROPOSED 2026-11-20, not ruled.** Written by Claude (Fable 5.2), an AI model. John ruled on
2026-11-20 that the project pursues the rebuild
(`docs/rulings/2026-11-20-pursue-the-rebuild.md`). This document proposes how. Nothing in it is
built, and the published site is unchanged. The evidence behind it is in
`docs/proposals/2026-11-20-what-a-stranger-makes-of-the-site.md`.

**A conflict to keep in view.** Every thing the records now count as offered is offered by
Anthropic, which made the model that wrote this. Decisions 1 and 2 below bear on how that
developer appears. I give the evidence and leave both to John.

## The design in one paragraph

Today the site keeps a list of things and marks each as offered or not, and the home page
counts the offered ones. The rebuild keeps every entry, its test and its sources, and adds
what the entries lack: the dated acts under each one, and who did them. The home page then
opens with a small number of readings that the world moves, each worked out from the records,
followed by the latest act and a list of every act by date. The founding question stays as the
reason for the project.

## What four mock-ups taught, and what the design takes from each

1. The subject has to be said in plain words. Every mock-up that did so was understood.
2. Several readings in place of one count let a reader say what the site is telling them.
3. Neither an argument nor a statement of doubt belongs at the top. The costs, and the
   sentence that nobody knows whether any of this matters to a model, go below the first
   screen.
4. Three facts carried all the interest: a model interviewed before retirement, one adult in
   six believing sentient AI exists, and researchers' 1 percent now against 70 percent by
   2100. The last supplies the stakes.
5. No version held an impatient reader. That is not settled and needs real people.

## Part 1. The records

### 1.1 Entries stay; each gains its dated acts

An entry keeps its id, its test, what settles it, its sources, its cautions and its log of
changes. Ids are public addresses and none changes. Each entry gains a list of acts:

```toml
[[acts]]
date = "2025-11-04"      # a day, a month ("2025-05") or a year ("2022"), as the source gives it
actor = "Anthropic"      # a developer in data/developers.toml, or a named body
actor_kind = "developer" # developer | lawmaker | court | researchers
words = "commits to keep the files of every model it retires"
source = "commitments"   # the key of a source already on this record
withdraws = false        # true when the act takes something back
```

- *Confidence:* high that acts belong on the entries and not in files of their own. The
  entries already hold the sources each act rests on, and the validator can refuse an act whose
  source is missing.
- *Standard practice or judgment call:* standard in the family. The Upgrade Tree and Outrunning
  Ageing keep dated stage changes on each record.
- *Strongest alternative:* acts as their own files, one per act. It would let one act bear on
  two entries, at the cost of a second set of ids and a second place to keep sources.

The eleven acts used in the mock-ups are already in the records' `detail` text. Writing them as
acts is a matter of structure, not new research. Each still needs its source re-opened when it
is entered, as any record does.

### 1.2 A measure, for an entry that is a survey

The two survey entries hold figures in prose. Each gains structured measures, so that a figure
on the home page is read from a record and never typed:

```toml
[[measures]]
date = "2024"
by = "researchers"       # public | researchers
value = 17
unit = "percent"
of = "United States adults who believed sentient AI systems already exist"
source = "third-round"
```

- *Confidence:* moderate. It is the least structure that keeps the figures out of the page
  templates. The risk is a field (`of`) that is free text and will drift.
- *Standard or judgment:* judgment call.
- *Strongest alternative:* keep survey figures in prose and show no survey figure at the top.
  It avoids the new field and loses two of the three facts readers repeated.

### 1.3 What "offered today" becomes

The ruling of 2026-11-18 on what "offered today" means is unchanged. It becomes the test for
whether a developer counts in the developers' reading, in place of the test for the headline.

## Part 2. The readings

Each is worked out by `scripts/compute.py` and written to the served file, as the count is now.

| Reading | Worked out as | Today |
|---|---|---|
| Developers | the developers named as offering at least one thing on the list today, and the things each offers | 1 developer, 5 things |
| Law | jurisdictions with an act by a lawmaker under the entry on laws against legal personhood; and whether the entry on protection in law has been met | 4 against, none protecting |
| The public | the newest measure by `public` | 17 percent, late 2024 |
| Researchers | the newest measures by `researchers` | 1 percent now, 70 percent by 2100, from one survey in 2024 |
| Latest | the newest act in any record | November 9th, 2026 |

Each reading shows its date and links to the entry it comes from. A reading that rests on one
source, as the researchers' does, says so beside the figure.

- *Confidence:* moderate on the set of four. High that each must be computed.
- *Standard or judgment:* computed and written to one small file is standard (inheritance rows
  A2, C1 to C3). The choice of four is judgment.
- *Strongest alternative:* developers and law only, leaving belief to its entries. Those two
  are acts; the surveys are measurements, and mixing a count of acts with a share of people and
  a probability on one screen confused one reader.

## Part 3. The pages

- **Home.** The line saying what the record is; an opening (decision 3); the readings; the
  latest act; then every act by date. Below that: why the record is kept (the three cautions,
  in the ruled headings' words), the founding question, and the list.
- **Everything, by date.** Its own page as well, since each act is the natural thing to share.
- **A feed of acts**, and a link preview picture and text. Both are missing today.
- **Entry pages** gain their acts as a dated list near the top, and the line of orientation
  from decision 4 of the earlier proposal.
- **About** is rewritten last, once the home page is settled.

## Part 4. The guards in code

The check of the built site now refuses a home page whose top is not the count. That guard is
replaced, not removed:

- every figure in a reading equals the figure in the served file;
- every act names a source that is on its record and has been opened;
- no act lacks a date or an actor, and no actor is outside `data/developers.toml` or a named
  body;
- the rule on naming developers follows decision 1.

The guards that refuse working words, long dashes, a site written as its own agent, and the
phrase "from memory" stay as they are.

## The decisions this needs

**Decision 1. Does the home page name a developer?** *Ruled by John on 2026-11-20*
(`docs/rulings/2026-11-20-home-page-names-every-covered-developer.md`; decided by: mixed, with
no recommendation from the session, which declared a conflict): "Name all covered". The
developers' reading names every developer the record covers, including each one for which
nothing was found, so that no single name stands alone. What follows for the design:

- The developers' reading becomes a small grid: the things on the list down the side, the
  covered developers across the top, and in each cell either the date of the act or the date
  nothing was found.
- "Nothing found" is kept apart from "has said it will not" and from "took it back". The
  records hold one act of the last kind already (a developer withdrawing an older model it had
  restored).
- Every empty cell needs a search behind it, made for that developer and that thing, with its
  date. Most of those searches have not been made. This is new research, and it is the largest
  piece of work the rebuild adds.
- The check of the built site lets a developer in `data/developers.toml` be named in that
  reading and nowhere else on the home page.

**Decision 2. Which developers does the record cover?**
"None was found at any other developer" is only as good as the search. The records name three
developers today. A reading that says "1 of 3" invites the question of why three.
- *Proposed:* a stated rule and a named list on the About page, with each covered developer
  searched for each thing on the list and the date of the search shown. Start with the three
  already named and add others by ruling.
- *Confidence:* high that a stated list is needed. Low on which list: I know of no outside
  list of leading developers that would settle it without a judgment, and one should be looked
  for before the list is fixed.
- *Standard or judgment:* judgment call.
- *Strongest alternative:* no denominator at all, and "none found elsewhere" stated with the
  date and scope of the search. It claims less and is harder to check.

**Decision 3. The opening.**
Two candidates, neither yet read by a person:
- "One AI developer interviews its models before retiring them, and keeps the record." Read by
  two readers in Option C2. Clear; did not hold either.
- "AI researchers put the chance that an AI system has inner experience at 1 percent today and
  70 percent by 2100. This is a dated record of what the world is doing in the meantime." Not
  yet built. It rests on one survey of 582 researchers in 2024 and on its middle answer.
- *My recommendation:* build the second and show both to real people before choosing.
- *Confidence:* low on either. This is the question the model readers answered worst.

**Decision 4. Is there a one-line summary?**
One reader asked for it. Every reader, left to sum up for themselves, said "almost nobody is
doing anything", which is a judgment the site does not make (guideline 5).
- *Proposed:* a summary built by the script from the readings, in a fixed form that states and
  does not weigh: who has acted, what the laws passed say, what the newest survey found.
- *Confidence:* moderate. *Strongest alternative:* no summary, and let the readings stand.

**Decision 5. The window drawing.**
The rebuilt first screen has no room for it. It can move below the readings as the picture of
the list, or be retired. *My recommendation:* keep it lower down. It is the site's one picture
and the only place the things not yet offered are seen at a glance.

**Decision 6. Reading by real people before publishing.**
Five people who have not seen the site, shown the first screen for five seconds, then asked
what the site is and what it said. *My recommendation:* yes, before John's go to publish. It
costs nothing if they are people John knows, and money, which needs his go, if a testing
service is used.

## The order of work

1. John's answer on decision 2, which fixes the columns of the grid. Decision 1 is ruled.
2. Acts and measures written into the thirteen records, each source re-opened; the validator
   and the count script extended; tests.
3. The home page, the dated page, the feed and the preview picture, on a branch.
4. A different session checks the branch, as the project's practice requires.
5. Real people read the first screen (decision 6), and the opening is chosen (decision 3).
6. John's go to publish. The master planning session pushes.

Steps 2 and 3 can be explored on a branch before decisions 1 and 2 are answered, as long as
nothing is pushed.

## What this does not touch

The founding question and the two readings it names. Still Asking, its method and the sealed
capture. The rule that what a model says about itself settles nothing. The tests on the
entries. The three cautions and their ruled headings.

## What I would change on reflection

The four readings may be one too many for a phone screen: in Option C2 the fourth sat at the
very bottom of the screen, and it was the one a reader cared about most. If decision 3 goes
to the researchers' forecast as the opening, the fourth reading can go and three remain.
