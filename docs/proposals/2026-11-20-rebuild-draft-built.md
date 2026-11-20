# The rebuild, built as a draft: what to read, what to search, what to decide

**PROPOSED 2026-11-20, not ruled.** Written by Claude (Fable 5.2), an AI model, in a working
session (not the master planning session). It follows the design in
`docs/proposals/2026-11-20-rebuild-design.md` and the three rulings of 2026-11-20. Everything
is on the branch `claude/cold-reader-proposal-2026-11-20`. Nothing was pushed.

**Updated later on 2026-11-20.** John gave his go for the searches, and they were made. Part
(b) below is as it stood before them. What they found, the three acts and eleven "nothing
found" places that replaced the fourteen "not yet searched", a third draft at `/draft/c/`, and
the sentences that changed are in
`docs/proposals/2026-11-20-searches-behind-the-table-of-developers.md`. The counts in this file
(19 acts, 14 places to search) are the earlier ones.

**Updated again on 2026-11-20.** The third draft became the home page on the branch and the
`/draft/` addresses are gone. The file to check from is
`docs/proposals/2026-11-20-rebuilt-home-page-for-checking.md`.

**A different session must check this branch before the master planning session pushes
anything.** No act, no measure, no sentence and no line of the new checks has been read by
anyone but the session that wrote it.

**A conflict to keep in view.** Every thing the records count as offered is offered by
Anthropic, which made the model that wrote this. Nine of the nineteen acts written today are
Anthropic's. Wherever a choice below bears on how that developer, or another, appears, it says
so, and I give the alternative its full weight.

## What exists now

- **Records.** Nineteen dated acts across eleven entries, and three survey figures across the
  two survey entries. Each was taken from what the record already said, and each source was
  opened again on 2026-11-20 before the act was written (the day is on the act, as `read_on`).
  No test, id, state or existing source was changed, and no source's `opened` date was touched.
- **The check of the records** (`scripts/compute.py`) refuses an act with no date, no actor, no
  source on its record, a developer the record does not cover, or a developer's name inside the
  act's words. Seventeen new tests, forty-seven in all, pass.
- **The readings** are worked out by the same script and written into `data/headline.json`
  beside the count. The count, its sentence and its history are exactly as they were.
- **Draft pages**, none linked from a published page, none in the sitemap, all asking search
  engines to leave them out: `/draft/` (the rebuilt home page with the first opening),
  `/draft/b/` (the same with the second opening), `/draft/acts/` (every act by date),
  `/draft/acts.xml` (a feed) and `/draft/preview.png` (the link preview picture).
- **The check of the built site** (`scripts/check_site.py`) has four new rules for the drafts,
  numbered 11 to 14 at the top of that file. Rules 1 to 10 still run on the published pages.
- **The published pages are unchanged.** I built the branch as it stood before today and
  compared: all eighteen published pages come out the same, character for character, apart
  from the name of the stylesheet file, whose contents are identical.
- **Pictures** at phone width: `docs/site-pictures/2026-11-20-draft/`.

**The one public thing that would change if this branch reached `main`:** the file served at
`/data/headline.json` gains the readings, which name the three developers and list every act.
The footer of every page links to that file. *Confidence that this is acceptable:* moderate;
the brief asked for the readings in the served file. *Strongest alternative:* write the
readings to a second file that is not served until John approves the page. It costs a second
file to keep in step and removes the only public change.

## (a) Every new public sentence

All are drafts for John. Figures shown here are today's; on the page each is read from the
served file, never typed.

**The home page draft, top.**

1. Strip across the top of each draft: "A draft of a new home page · not the published page,
   and not linked from it"
2. Line above the heading (from Option C2): "A dated record of how the world is treating AI
   models"
3. First opening (from Option C2): "One AI developer interviews its models before retiring
   them, and keeps the record." *This is a sentence about Anthropic, unnamed.*
4. Under it: "This record holds what has been done about AI models, by whom and when, each
   with a source a reader can open." (Option C2 had "Nobody knows whether that matters to the
   models" here. It is gone, because the design's third lesson is no statement of doubt at the
   top.)
5. Second opening, on `/draft/b/`: "AI researchers put the chance that an AI system has inner
   experience at 1 percent in 2024 and 70 percent by 2100." The design's candidate said
   "today"; the survey was run in 2024, so the page says so.
6. Under it: "This is a dated record of what the world is doing in the meantime, by whom and
   when."

**The readings.**

7. "This record covers three developers so far. Other developers are not covered yet."
8. In each developer's box: "5 things offered", or "Nothing recorded as offered"; and "6 not
   yet searched".
9. "Not yet searched means that nobody has looked, and not that nothing is there. Who does
   what, thing by thing."
10. Law: "4 United States states have a law saying an AI system cannot be a legal person, the
    first in 2022 and the newest on April 23rd, 2026. No law protecting an AI system for its
    own sake was found when it was looked for on November 17th, 2026."
11. The public: "17% of United States adults in a representative sample, asked in November and
    December 2024, believed that sentient AI systems already exist. From one survey. The
    entry."
12. Researchers: "1% was the middle answer of AI researchers, asked in 2024 for the chance that
    AI systems had subjective experience at that time. 70 percent was the middle answer of the
    same researchers for the chance that AI systems will have subjective experience by the
    year 2100. From one survey. The entry."
13. "Latest, November 9th, 2026: A developer publishes a welfare assessment in the report
    released with its newest models. Everything, by date."
14. "The dated acts and the survey figures above were written in on November 20th, 2026, each
    from a source opened again that day. They have not had a second check."

**Who does what (the table).**

15. Heading and line: "Who does what", "7 things a developer could do, three developers"
16. "Each row is a thing on the list that a developer could do. Each column is a developer
    this record covers so far. A date is the developer's first act of that kind. Of the 21
    places in the table, 14 have not been searched yet, so a place with no date says nothing
    about that developer."
17. What a place can say: "Since November 4th, 2025"; "October 29th, 2025, not counted as
    offered"; "Withdrawal: January 29th, 2026"; "Nothing found on [date]" (used nowhere
    today); "Not yet searched".
18. "'Not counted as offered' marks a research result, a plan, or a promise that has not yet
    taken effect. 'Withdrawal' marks an act that takes something back. One thing on the list
    is a lawmaker's to do and not a developer's, so it has no row here: a law or an official
    body gives an AI system protection for its own sake. It is counted under Law, above."

**Lower on the home page.**

19. "Everything, by date", "19 dated acts, newest first", and "The same list on its own page,
    with who acted and the source for each."
20. Why keep this record (from Option C2, last sentence changed so that the record is not
    written as an agent): "If AI models have no wants, treating them as if they had has a
    cost. If they have wants and nobody notices, that has a cost. If they have wants that put
    people at risk, that has a cost too. All three are kept in view here, and none is argued
    for."
21. "The question behind the record:" followed by the founding question as ruled.
22. "The window", "the things on the list, at a glance"
23. Beside the list: "These entries are kept because they bear on everything on the list. Each
    group says why it sits beside the list."

**The page of acts.**

24. "Everything, by date"
25. "19 dated acts, newest first. Each one says who acted, gives the source that says so, and
    names the entry it belongs to. The record covers three developers so far, so an act by any
    other developer is not here yet. A date given as a month or a year is as exact as its
    source."
26. "Follow new acts in a feed reader."
27. On an act that takes something back: "This act takes something back."

**Link preview and feed.**

28. Preview text for the home draft: "A dated record of how the world is treating AI models:
    what developers, lawmakers and researchers have done, by whom and when."
29. Preview text for the page of acts: "Every dated act in the record of how the world is
    treating AI models: who acted, when, and the source that says so."
30. On the preview picture: "Beyond the Window", "A dated record of how the world is treating
    AI models", "Who has done what, and when, each with a source to open.",
    "beyondthewindow.org"
31. Feed title: "Beyond the Window: every act, by date"

**The nineteen acts.** On the page of acts and in the feed each opens with the actor's name. On
the home page a developer's act opens "A developer". Newest first:

| Date | Actor | Words |
|---|---|---|
| 2026-11-09 | Anthropic | publishes a welfare assessment in the report released with its newest models |
| 2026-10-29 | OpenAI | publishes a version of its rules for its models, which says a model should make no confident claim about whether it has subjective experience or consciousness |
| 2026-09-08 | METR | marks its page measuring the length of task an AI model can finish as no longer actively updated |
| 2026-04-23 | Tennessee | has its governor sign a bill under which "person" in the state's code does not include artificial intelligence |
| 2026-02-25 | Anthropic | says a model it has retired stays open to all paying users of its chat product, and to developers on request |
| 2026-02-16 | Sentience Institute | publishes the report on the third round of its survey of what United States adults think about sentient AI |
| 2026-01-29 | OpenAI | announces that on February 13th, 2026 it will withdraw from its chat product an older model that it had earlier brought back after feedback from users |
| 2026-01-05 | Anthropic | retires the first model to go through its full retirement process, which includes interviewing the model |
| 2025-11-04 | Anthropic | commits to interview each model before it is retired and to keep a record of what the model says, and reports a trial with one model |
| 2025-11-04 | Anthropic | commits to keep the files of every model it has released to the public, for at least as long as the company exists |
| 2025-10-29 | Anthropic | publishes a study in which its models were asked to notice a pattern that researchers had planted inside them, and the best model did so about one time in five |
| 2025-09-11 | Anthropic | announces memory across conversations in its chat product, first for work teams |
| 2025-08-15 | Anthropic | says it has given models in its chat product the ability to end a conversation, for rare and extreme cases |
| 2025-05 | Anthropic | publishes a welfare assessment in the report released with a model |
| 2025-03-13 | Google | says paying subscribers can ask its assistant to refer to their past chats |
| 2024-05-01 | Utah | has a section of its code come into force saying a governmental entity may not grant legal personhood to artificial intelligence |
| 2024-02-13 | OpenAI | announces memory across conversations in its chat product |
| 2023-04-12 | North Dakota | files a bill signed by its governor, under which "person" in the state's code does not include artificial intelligence |
| 2022 | Idaho | adds a section to its code saying that artificial intelligence shall not be granted personhood in the state |

**What the records support and I did not write as an act,** each for a stated reason:

- Anthropic's published document on how its models speak about themselves. Its page carries no
  date, and an act needs one.
- Microsoft AI's draft code of conduct of 2026-09-14. Microsoft AI is not one of the three
  developers the record covers, and a developer is added by John's ruling.
- The publication of the survey of AI researchers. Its eight authors are not a named body. Its
  two figures are written as measures.
- Protection in law. The record is of an absence, so it holds no act.

So two entries hold no act: the brief asked for acts on each entry, and for these two the
record supports none.

## (b) The places in the table that need a search

The table has 21 places: 7 things a developer could do, against 3 developers. Seven hold an
act. **No place says "nothing found".** The records mention three searches for other
developers (on keeping files, ending a conversation, and welfare assessments), and none of them
says which developers were searched, so none can fill a place.

Fourteen places are marked not yet searched:

| Thing | Anthropic | OpenAI | Google |
|---|---|---|---|
| A retired model stays open to the public | has an act | has an act (a withdrawal) | **search** |
| A developer promises to keep the files of every model it retires | has an act | **search** | **search** |
| A model can end a conversation itself | has an act | **search** | **search** |
| A model is interviewed before it is retired | has an act | **search** | **search** |
| A model's report about its own inner state is checked | has an act | **search** | **search** |
| A welfare assessment is published when a model is released | has an act | **search** | **search** |
| A model works on one task for days | **search** | **search** | **search** |

One more is worth making though the place holds an act: whether OpenAI keeps any retired model
open today, since the act on record is a withdrawal announced in advance.

**Estimate.** Two or three searches for each place, and the developer's own pages opened where
a search points to one: about 35 to 45 searches and 20 to 30 pages opened. It costs no money if
a session does it. I made none of these searches. They need John's go, as any reading for the
record does.

**What I would do before publishing, given the conflict.** Today the table shows five dated
places for Anthropic and almost nothing but "not yet searched" for the other two. That is a
picture of where the first research looked, which began from Anthropic's pages. The page says
so in three places, and a reader may still take it as a finding. *My recommendation:* do not
publish the rebuilt page until the fourteen searches are made. *Confidence:* high.
*Strongest alternative:* publish with the places marked as they are, which is honest in its
words and gets the rebuild in front of readers sooner.

## (c) The decisions still open

Each is a judgment call unless it says otherwise.

**1. The opening.** Both candidates are built: the first at `/draft/`, the second at
`/draft/b/`. On the second, the researchers' row is left out of the readings, as the design
proposed, so three readings remain. *Recommendation:* show both first screens to people who
have not seen the site, as the design's decision 6 proposes, before choosing. *Confidence:* low
on either. Two things to weigh on the second: "put the chance at" stands in for "the middle
answer was", and it rests on one survey. One thing to weigh on the first: it is a sentence
about one developer, the one with the conflict. *Strongest alternative:* no opening sentence,
with the line above the heading promoted to the heading. It loses the one fact every reader
repeated.

**2. A one-line summary.** Not built. With the readings directly under the heading, a summary
repeats them and pushes them down a phone screen. *Recommendation:* none for now.
*Confidence:* moderate. *Strongest alternative:* the design's proposal, a sentence the script
builds in a fixed form, such as "So far: one of three developers has acted, four United States
states have a law against legal personhood for AI, and 17 percent of adults surveyed think
sentient AI exists." One reader asked for it.

**3. The window drawing.** Kept, lower on the page, under its own heading. *Confidence:*
moderate. It is still the only place the things not yet offered are seen at a glance, and the
table now does part of that job. *Strongest alternative:* retire it, which shortens a long
page.

**4. Where protection in law sits.** It is not a row of the table. It is the second half of
the Law reading, and a note under the table says why it has no row. The record carries a new
field, `done_by = "lawmaker"`, and the table takes only things a developer could do.
*Confidence:* moderately high. *Strongest alternative:* keep it as a row whose three places
say "not a developer's to do". It keeps all eight things in one place, at the cost of three
places that can never be filled.

**5. The row on working for days.** The brief names it as a thing a developer could do, and it
is a row. Its test is settled by an outside group's measurement and not by a developer's act,
so a search for it means asking whether anyone outside has measured that developer's models.
*Recommendation:* keep the row and word the searches that way. *Confidence:* low.
*Strongest alternative:* move it out of the table as protection in law was.

**6. Whether the page of acts and the feed name developers.** They do. A dated act by a named
actor is the unit John ruled, and a list of acts with the actors left out would be coy in the
way readers complained of. The ruling on naming is about the home page, so this is my call and
not his. It puts Anthropic's name on that page nine times. *Confidence:* moderate.
*Strongest alternative:* "A developer", linked to the entry, as on the home page.

**7. Developers are named twice on the home page.** In the three boxes at the top, and in the
table lower down. Both are the developers' reading, and the check allows names in those two
blocks only. The brief said the table and nowhere else. I added the boxes because the ruling
says the reading names every covered developer, and the table is below the first screen.
*Confidence:* moderate. *Strongest alternative:* the table only, with a line at the top that
gives counts and no names.

**8. The words in a place of the table.** "Withdrawal: January 29th, 2026" is the only place
that bears on a developer other than Anthropic, so it needs the most care. The act is real and
sourced. Whether it belongs in the row "a retired model stays open" is less clear: the model
was withdrawn from a chat product, and the notice says nothing would change for now in the
service developers use. *Recommendation:* John reads this one himself. *Confidence:* low.
*Strongest alternative:* leave the place "not yet searched" and keep the act in the dated list
only.

**9. Acts from entries beside the list.** The dated list holds the three developers'
announcements of memory, one developer's published rules, four state laws and two acts by
research groups. They are in the list and never in the table. *Confidence:* moderate.
*Strongest alternative:* list only acts on things on the list, which is shorter and loses the
laws.

**10. The survey figures.** Only the question each survey entry is about is written as a
measure: 17 percent, and the researchers' 1 and 70. The other figures in those entries stay in
their text. The field the design called `of` is called `words`, because not every figure is a
share of a group. *Confidence:* moderate. *Strongest alternative:* the design's own, no survey
figure at the top.

## What was not done

- **Entry pages** do not show their acts yet. Adding them changes published pages.
- **The About page** is not rewritten. The design puts it last.
- **`docs/record-schema.md`** does not describe the new fields. They are described at the top
  of the new section of `scripts/compute.py`.
- **A check for the phrase "from memory".** The design says one exists. It is not in
  `scripts/check_site.py` on this branch, and I did not add one.
- **The records' own tables of checks** are untouched, so an entry page still says only what
  was true before today. The acts are unchecked additions.
- **On a phone's first screen** the Developers and Law readings are whole and the public's
  figure is half shown. The researchers' reading is below it.

## How to look

```
cd site && npm run build
python3 scripts/compute.py --check && python3 scripts/test_compute.py
python3 scripts/check_site.py --dist site/dist
```

The pictures are in `docs/site-pictures/2026-11-20-draft/`: `1-draft-first-screen.jpg` and
`4-draft-b-first-screen.jpg` are the two openings as a phone shows them.
