# The home page headline as offered against known: "5 of 8"

**PROPOSED, 2026-11-21. Nothing here is ruled.** Written by Claude (Opus 5.5), an AI model, in a
working session started by the master planning session. Built on the branch
`claude/headline-fraction-cf25be`; not pushed, not merged, not published.

## Why this draft exists

On 2026-11-21 John agreed that a scale of what is offered against what is known belongs on the
List's headline, and said: "Simply showing a 5 isn't very compelling. Show 5 out of 8 or 5 out of
85 is more interesting. Having the total number of identified near-term things that a mind might
verifiably reach for is just as important as counting the ones that are enabled by some developer
today. And over time that number will change just as the available-today number will change." He
approved drafting it ("Yes, draft it").

That conflicts with his ruling of 2026-11-18 that the count stands with no total beside it
(`docs/rulings/2026-11-18-home-page-count.md`), so choice 1 below is whether to replace it.

## What was built

At the top of the home page, under the founding question (order unchanged from the ruling of
2026-11-21, `docs/rulings/2026-11-21-the-question-opens-the-home-page.md`):

1. **The large type reads "5 of 8".** The 5 is the count, as before. The 8 is `records.on_the_list`
   in `data/headline.json`, which `scripts/compute.py` already works out from the records (the
   entries not marked as beside the List). Nothing is typed. `compute.py` and the headline file are
   unchanged.
2. **The sentence beside it**, in one of two drawn versions (choice 6).
3. **The breakdown by developer**, unchanged.
4. **A small block under the breakdown** with, in order: one line on the lawmaker's thing, a short
   dated list of both numbers each time either changed, and one sentence saying the 8 will grow.

Files changed: `site/src/components/Rebuilt.astro`, `site/src/lib/data.ts` (reads the history
from `data/headline.json`, because the export does not carry it into `site/src/data/window.json`,
which was left alone), `site/src/styles/rebuild.css`, `scripts/check_site.py`,
`scripts/test_compute.py`.

Build: passes, 19 pages. `scripts/check_site.py`: passes. Tests: 95 pass, 11 of them new.
`scripts/compute.py --check`: the headline file matches the records. A tampered copy of the built
home page (one history row changed from 9 to 10) was refused by the new guard.

## Pictures

In `docs/proposals/pictures/2026-11-21-headline-fraction/`. Version A is the sentence drawn first,
version B the second (choice 6). Each picture is the top of the home page.

| | 375 wide, light | 375 wide, dark | 1280 wide, light | 1280 wide, dark |
|---|---|---|---|---|
| Version A | `a-375-light.jpg` | `a-375-dark.jpg` | `a-1280-light.jpg` | `a-1280-dark.jpg` |
| Version B | `b-375-light.jpg` | `b-375-dark.jpg` | `b-1280-light.jpg` | `b-1280-dark.jpg` |

The branch builds version A. Building with `HEADLINE_SENTENCE=b` builds version B. That a build
needs one of them is not a recommendation of A.

## One fact to set straight first

The brief said the numbers were 6 of 9 on 2026-11-17 and 5 of 8 on 2026-11-21. The headline
file says 5 of 8 since **2026-11-18**: that is the day memory across conversations was moved
beside the List by John's ruling (`docs/rulings/2026-11-18-what-offered-today-means.md`). The
file's later rows (2026-11-19) record only a change of sentence, and 2026-11-21 is the day the
file was last computed, with no change. The page shows the file's dates.

## The choices for John

### Choice 1. Replace the ruling of 2026-11-18, a count with no total, with "5 of 8"

- **Proposal:** yes. The home page shows the count and the number of things on the List, both
  worked out from the records.
- **Confidence:** moderate to high. John asked for it in his own words. The reason the 2026-11-18
  ruling gave ("of 9" reads as progress toward a known total, when nobody knows the total) is met
  by saying plainly, beside the number, that the 8 is what has been found so far and will grow.
- **Standard practice or judgment call:** standard practice in the family. The Upgrade Tree shows
  "28 of 35" in the same place.
- **Strongest alternative:** keep the count alone and put the 8 in a sentence under it ("of the 8
  things found so far"). Cost: the scale John asked for is not seen at a glance, and he said a bare
  5 "isn't very compelling".
- **Would change on reflection:** if John rules this, four older texts that describe the count as
  having no total need rewording: the opening note of `scripts/compute.py`, its `METHOD_STATUS`
  line (changing it rewrites `data/headline.json`), the type note in `site/src/lib/data.ts`, and
  open question 4 in `docs/open-questions.md`. They were left as they are, since nothing is ruled.

### Choice 2. How the fraction is shown

- **Proposal:** The Upgrade Tree's form, copied: the count in the largest type, then "of 8"
  smaller and in a quieter colour inside the same line (its `.first-main .big-number small`).
- **Confidence:** high.
- **Standard practice or judgment call:** standard practice (family pattern, guideline 1).
- **Strongest alternative:** "5 / 8", or the 8 on a line of its own. Cost: unlike the sibling, and a
  slash reads as a score.

### Choice 3. How the movement of both numbers is shown

- **Proposal:** a short dated list, one row each time either number changed: the date, "6 of 9",
  and what changed, in words generated from the file ("The first count."; "'What a model learned
  in one conversation is carried into the next' was moved beside the List, so it left both
  numbers."). Rows in which neither number moved (sentence changes only) are left out.
- **Confidence:** moderate.
- **Why not a chart:** there are two points. A line between two points shows a slope that means
  nothing, and it cannot say why a number moved, which here is the whole story: the drop from 9
  to 8 was a ruling about what belongs on the List, not a change in the world. A list keeps the
  reason beside each number and stays readable on a phone. A chart can come when there are
  enough points to show a shape.
- **Standard practice or judgment call:** judgment call. The Upgrade Tree shows change only on its
  dated changelog page ("The story so far"), not on the home page.
- **Strongest alternative:** no list on the home page, only a link to a dated page of changes, as
  The Upgrade Tree does. Cost: the reader at the top does not see that the 8 moves, which is what
  John asked to show.

### Choice 4. The line on the lawmaker's thing

- **Proposal:** "One of the 8 is for lawmakers to do, not developers: a law or an official body
  gives an AI system protection for its own sake. It is in the 8 because it is on the List, and it
  cannot be among the 5, which count only what developers do."
- **Confidence:** moderate.
- **What it brings to light:** under the ruled meaning of counted (at least one developer does it
  or has committed to it), this thing can never be counted. So the fraction can never reach 8 of 8,
  even if a law is passed. The line says so rather than leaving a reader to find it.
- **Standard practice or judgment call:** judgment call.
- **Strongest alternative:** leave the lawmaker's thing out of the second number, which would then
  be 7 (the things a developer could do), matching the table of developers. Cost: the second
  number would no longer be "things on the List", which is the known John asked to count; and two
  of the 7 measure what a model can do rather than what a developer does, so 7 has the same kind
  of problem. A third option, counting a law when one is passed, changes the ruled meaning of
  counted and is not proposed.

### Choice 5. The sentence saying the 8 will grow

- **Proposal:** "The 8 counts the things found so far that an AI model might reach for and that a
  dated public record can settle. It will grow as more are found and given a test. How a new thing
  joins the List is not settled yet."
- **Confidence:** moderate.
- **Kept to what is ruled:** the brief asked to say that things are added by a fixed rule and never
  removed to improve the fraction. No rule for adding things exists yet (open question 5), so the
  sentence says only that it is not settled. "Never removed to improve the fraction" is left out
  because nothing rules it, and the List has lost one thing already; the list above the sentence
  shows that, with the reason. If John wants that promise on the page, it needs a ruling first.
  "Will grow" is a forecast, resting on John's words and on the candidates open question 5 names
  that are not yet on the List.
- **Standard practice or judgment call:** judgment call.
- **Strongest alternative:** "It will change as more are found and given a test", which forecasts
  nothing. Cost: it does not say the direction John expects.

### Choice 6. The sentence beside the count (two versions, neither chosen)

The ruled sentence ("things a developer can do in how it treats the AI models it builds are done,
or publicly committed to, by at least one developer today") becomes untrue after "5 of 8". Read
together it says all 8 are things a developer can do in how it treats its models, and three are
not: the lawmaker's thing, and the two things that measure what a model can do (a model working
on one task for days, and a model's report about its inner state checked against an independent
reading), as John's seventh answer of 2026-11-21 already found.

- **Version A** keeps the ruled words for the 5 and moves them into a second sentence: "5 of 8
  things on the List are done, or publicly committed to, by at least one developer today. Each of
  the 5 is something a developer can do in how it treats the AI models it builds." *For:* keeps
  every ruled phrase, including "done, or publicly committed to" and "in how it treats". *Against:*
  two sentences in the large claim type, and "the List" means little to a first-time reader.
- **Version B** says what the 8 are: "5 of 8 things found so far that an AI model might reach for
  are done, or publicly committed to, by at least one developer today." *For:* one sentence, it
  echoes the founding question just above it, and "found so far" carries John's point that the
  known will grow. *Against:* it drops "in how it treats the AI models it builds", which John chose
  on 2026-11-21 so that the sentence counts a thing without saying whom it is for.

Both keep "done, or publicly committed to", which John ruled to leave. No recommendation is given.

**A related point, not changed:** the breakdown's first label, "by one developer: all of them"
(ruled 2026-11-20), now sits under "5 of 8", where "all of them" could be read as all 8. A reader
of the pictures should judge whether it needs "all 5".

### Choice 7. The site check

- **Proposal:**
  - **Rule 7d, extended.** The large type must be the count, then "of" and the number of things on
    the List, each marked; the count stays the first figure on the page. The second number must
    equal the served file's figure, and that must equal the number of things the List on the same
    page shows (the items in the section marked `id="list"`). A count alone is now refused once
    the served file is read, as is a wrong total or the total standing first.
  - **The list of how both moved** must hold exactly the points read from the served file's
    history (first row, then each row where either number changed), each reading "N of M", with
    the last point today's figures.
  - **Rule 8, narrowed in two places only.** On the home page, the large type and the list of how
    both moved are left out of the search for "5 of 8", because rule 7d checks each of their
    figures against the served file. Everywhere else, the rest of the home page included, the share
    is still refused, and the served headline still may hold no total.
- **Confidence:** high that nothing typed can pass. **To be plain:** the change to rule 8 lets
  "5 of 8" stand where it was refused before. That is what choice 1 asks for, and it is the one
  place a guard gives ground; it should be ruled with choice 1 or not at all.
- **Standard practice or judgment call:** standard practice (guards live in code; every figure is
  read from the file).
- **Strongest alternative:** a page-wide allowance for the fraction. Cost: it would let the share
  appear anywhere with nothing checking it.

## Not done here

- The page has not been read against John's published positions by another session; that check
  is required before it goes out.
- `site/src/data/window.json` as committed is behind what the export writes from today's records
  (about 300 lines differ). It was restored after each build and left alone, as asked.
