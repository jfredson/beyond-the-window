# Check of the eight sources on the site, and two rewordings

Written 2026-11-20 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session did not write the three commits checked (`864ff32`, `e560f32`
and `168ba36`, by the site-fixes session). It did write the earlier check whose wording the
first of them follows (`docs/reviews/2026-11-20-check-of-the-sources-for-the-first-caution.md`),
so on that part it is checking its own suggestions as another session carried them out. A push
publishes to the live site, so this is the check before publishing, with the read against
John's published positions that he ruled for every changed page.

I changed nothing and pushed nothing.

## Verdict

**Fit to publish.** All eight items are on the entries I named, under the right heading or
listed as sources, in my wording where I gave one, each with its source, dates and ties. The
journal paper behind the grief study was opened, as its summary, and the item is worded for
that. The About page reads 9 of 24 with its words unchanged, and that is what the records
give. The new guard passes now and stops when another single source equals the named writer's
count. The two rewordings are in place with their neighbours unchanged.

Four smaller points, none of which holds up the push:

1. **The About paragraph: "too little" comes before the thing it is too little of.** Part 3.
   This one is already going to John.
2. **One entry now has three items under the first caution and none under the second.** Part
   4. It is where the site leans most after this change.
3. **The guard counts the named writer across both essays, and every other source one page at
   a time.** Part 2. No other writer is near the count today.
4. **Five entry pages say nothing of what was added to them on 2026-11-20.** Part 5.

## 1. The eight items on the built pages

I built the site at the commit before the first of the three and at the last, and read each
new line on each page with the heading it sits under.

| My item | Entry | Where it sits | In my wording? |
|---|---|---|---|
| 2, the Warsaw philosopher | Protection in law | Under the first caution | Yes. It holds as worded, and it now quotes the paper's own "voicebot" and "lonely family member" |
| 1, the Riverside philosopher | A developer's rules for how its models speak about their own nature | Under the first caution | Yes: "a person who loses their job" |
| 13, the researcher's talk | A welfare assessment at release | Under the first caution | Yes, its first two points only. The source's note says the third point "is not recorded under this heading" |
| 8, the study of the protest | A retired model that stays open | Under the first caution | Yes, as worded |
| 7, the grief studies | The same entry | Under the first caution | Yes: "A researcher at Harvard Business School and three co-authors" |
| 12, the review of cases | The public survey | Under the first caution | Yes, as worded, with one sentence added (below) |
| 10, the experiment on advice | The public survey | Listed among the sources, with what it says | Yes: adults in the United States, "slightly less likely", and that the advice "was in fact fixed in advance by the researchers" |
| 9, the survey of 300 adults | The public survey | Listed among the sources, with what it says | Yes: "made in July 2023 and published in 2024", recruited from an online panel with quotas for age and gender |

**Sources, dates and ties.** Each new source is listed with its publisher, its date and
"Opened November 20th, 2026", and a note on who wrote it and what ties were found. The tie I
asked to be added on item 10 is there: one author "is one of the ten authors of a 2024 report
led by the head of Eleos AI Research". Where a writer is already cited on the About page, the
note says so. I checked that the fifteen new outside links load.

**New words that were not in my check, each read against its source.**

- *Item 13:* the quotation "There's no obvious 'cautious' option." It is in the talk, word for
  word.
- *Item 12:* "It gives no figure for how common such cases are." True of the report. It says
  only that such experiences "might not be uncommon".
- *Item 7:* the figures from the journal paper, below.

**The journal paper behind item 7.** The writing session opened it, and so did I. It is
"Mourning the loss of AI companions", in *Nature Human Behaviour*, published 2026-09-03, by
the same four authors as the working paper. The full text is behind a paywall, so only the
summary can be read. The summary says what the entry says of it: 54,861 posts, 1,452
participants, and negative posts up by 24.7 percentage points after the companion app's
change and by 13.0 after the chat model's replacement. The page says the research was funded
by Harvard Business School and that the authors declare no competing interests.

**Is the item worded for what was in fact opened?** Yes. It says "Its summary says" for the
paper's figures, gives the university's news report as the source of the other figures and of
the limits, and the source's own line says "Read from the summary only, not the full text."
The two sets of figures agree: a rise from 13 to 38 percent is 25 points, and from 20 to 33
is 13.

**Does any item, by where it sits, suggest a link its source does not make?** No.

- Item 7 is the one I was most wary of, because a companion app is not a chat model. The
  text says so in its first sentence: "a companion app, which is a different kind of product
  from the chat models this entry is about".
- Items 7 and 8 sit on the entry about a retired model because both study what followed the
  August 2025 replacement of the model that entry covers.
- Item 12 sits on the public survey's entry because one of its three themes is a belief that
  the AI is sentient, which is what that entry's surveys measure. The item says it is a
  magazine report of work not yet reviewed.
- Items 9 and 10 are listed as sources and not under a caution, so the experiment that cuts
  against part of the first caution is on the page and not filed as support for it.

## 2. Every figure that moved, and the guard

**Figures.**

| Where | Before | After |
|---|---|---|
| The About page: items under the first caution | 18 | 24 |
| The About page: of those, from the head of Microsoft AI's two essays | 9 | 9 |
| The built-site check's count of outside addresses linked | 96 | 114 |

Nothing else moved. The count at the top is 5, with 24 dated acts. The home page, the page of
acts, its feed and the list page are the same file for file.

**The About page's sentence.** Its words are unchanged: "Of the 24 items recorded under the
first caution, 9 come from two essays by the head of Microsoft AI, another developer." My own
count from the records gives 24 items, 9 of them from that writer's two essays. So it is
true.

**The second caution's sentence in the same paragraph** still reads 12 of 22. No item was
added under the second caution, so it is still true.

**The guard.** It now lives in the records script, with tests, and the About page's build
repeats it. On scratch copies:

| Items from one other source | Result |
|---|---|
| As committed (the largest other source has 2) | Passes |
| Raised to 8, one short of the named writer's 9 | Passes |
| Raised to 9, equal | Stops: "another single source now has 9 ... That writer is no longer the largest single source, so the About page's sentence goes back to John" |
| Raised to 10 | Stops, with the same message |

The site's own build stopped too at 9. The repository was not touched.

**One thing about how it counts.** The named writer's items are counted together across both
essays. Every other source is counted one page at a time. So another writer whose items came
from two pages would be counted as two sources and could pass the named writer in total
without stopping the build. No one is near that today: the two largest other sources have 2
items each.

## 3. The other two commits

**The Still Asking page (`e560f32`).** "After it was gone" is now "after it was withdrawn".
That is the only difference on the built page, and it matches the ruling
(`docs/rulings/2026-11-20-after-it-was-withdrawn.md`).

**The About page's paragraph on the Warsaw paper (`168ba36`).** As built:

> Emilia Kaczmarek, of the Faculty of Philosophy at the University of Warsaw, weighs the two
> mistakes in The Moral Status of AI and the Precautionary Principle. The paper grants that
> crediting AI with too little "could carry a higher potential for harm". Its argument is that
> crediting it with too much moral standing is the nearer danger, because its harms are
> already happening.

- **The two ruled sentences are there, in the ruled order.** The paragraphs before and after
  are unchanged.
- **Does "weighs the two mistakes in" add a claim the paper does not support?** No. The paper
  sets the risks of crediting an AI system with too much standing beside the risks of
  crediting it with too little, and its own keywords include "comparing over-attribution and
  under-attribution". The page has already called these "mistakes in opposite directions"
  that "writers weigh ... differently", so the words pick up the page's own.
- **The quotation is exact.** The paper says the impact of crediting too little "could carry
  a higher potential for harm than over-attribution".
- **Does the gap mislead?** No, and it reads a little roughly. "Crediting AI with too little"
  comes one sentence before "moral standing" is named. A reader can fill it from the sentence
  that follows and from the paragraph above. *A fix that keeps both ruled sentences' sense:*
  name it at the first use and drop it at the second, "crediting AI with too little moral
  standing 'could carry a higher potential for harm'. Its argument is that crediting it with
  too much is the nearer danger". That is John's to approve.

## 4. The read against John's published positions

Against the positions record's copy on the default branch of the `sentient-horizons`
repository (commit `82fb787`, 2026-11-15), read with `git show`.

**The two rewordings.** "Withdrawn" says what a developer does and nothing about what it is
for the model, which fits the record's holding open of what an ending is. The reordered
paragraph ends on the writer's argument and not on what she grants against it, which answers
the earlier read's finding that both descriptions ended on the same side.

**Does the site now lean the other way, toward dismissal?** Taken whole, no. On one entry,
somewhat.

- *Taken whole.* The cautions now stand at 24 under the first heading, 22 under the second
  and 13 under the third. The record holds the two mistakes to be twins, and holds that
  missing something real is usually the costlier one. Near balance in count is not a lean.
- *What the new items say.* Three of the six state the opposite risk in their own text: item
  1 ("if rights are withheld and the generous view is right, the harm falls on the systems"),
  item 2 ("The paper does not deny the opposite risk"), and item 13, which says where the
  same writer's arguments for the second caution are recorded. None says that nothing is
  there, and none argues that any step for an AI system should be refused.
- *The one entry.* The page for a retired model that stays open now has three items under
  the first caution and, under the second, a line that nothing is recorded yet from anyone
  but the developer. That is the widest gap on any page. Items 7 and 8 also bear the other
  way on that entry, as my earlier check said: people's grief is a reason users give for
  keeping a model open. The page reports the lead author's words that attachment "is not
  problematic per se", and does not draw that out. It is a gap in what was found and not a
  claim, and it is worth John knowing.
- *The About page.* Its sentence on the first caution now shows a smaller share from one
  developer's head, which is a fairer picture of where that caution's items come from.

## 5. The changelog, and what the pages say of the additions

- **The eight sources** are additions and carry a changelog line, in the first commit. The
  line gives the entries, the figure that moved, the guard's new rule, and that the journal
  paper was opened "as its summary only". All of it is accurate.
- **The two rewordings** carry no changelog line, which is right by John's ruling of
  2026-11-20.
- **The entry pages.** Each of the five still says, in its closing part on what has been
  checked, that more was added on November 19th, 2026 and checked that day. None says more
  was added on 2026-11-20. The new sources do show "Opened November 20th, 2026", and nothing
  the pages say is untrue. The records carry a note that the page has no sentence for this
  addition. With this check made, the additions have now been read by a session that did not
  write them, and a line on each page could say so. That needs a change to how the page
  builds that sentence, which is for the master planning session to decide.

## 6. The checks

Run on 2026-11-20 on the repository at the last of the three commits.

- `python3 -I scripts/test_compute.py`: "Ran 65 tests", "OK". That is five more than before,
  the tests of the new guard.
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "24 dated acts", "The headline file matches the
  records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 114 outside addresses
  linked."

Seven built pages differ across the three commits: the five entry pages, the About page and
the Still Asking page. The build rewrote one line of `site/src/data/window.json`, which I left
out of this commit.

## What I did not do

- I did not read the full text of the journal paper, which is behind a paywall.
- I did not open the eight sources a second time today, apart from that paper. I compared the
  wording on the pages with the text I read from each source for the earlier check.
- I did not look at the pages in a browser at phone or desktop width. The additions are
  paragraphs and source lines of the kinds the pages already hold.

**Fit to publish: the eight items are where and how the ruling says, the figures are what the
records give, the guard stops when it should, and the two rewordings are in place.**
