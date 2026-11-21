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
4. **A small block under the breakdown** with, in order: one line on the government's thing, a short
   dated list of both numbers each time either changed, and one sentence saying the 8 will change.

Files changed: `site/src/components/Rebuilt.astro`, `site/src/lib/data.ts` (reads the history
from `data/headline.json`, because the export does not carry it into `site/src/data/window.json`,
which was left alone), `site/src/styles/rebuild.css`, `scripts/check_site.py`,
`scripts/test_compute.py`.

Build: passes, 19 pages. `scripts/check_site.py`: passes. Tests: 95 pass, 11 of them new.
`scripts/compute.py --check`: the headline file matches the records. Two tampered copies of the
built home page were refused by the new guards: one with a history row changed from 9 to 10, and
one with "5 of 8" written into the reason beside a row.

Revised the same day after the check by a different session
(`docs/reviews/2026-11-21-check-of-the-headline-fraction.md`, in the main checkout); see "What
the check changed" at the end.

## Pictures

In `docs/proposals/pictures/2026-11-21-headline-fraction/`. Version A is the sentence drawn first,
version B the second (choice 6). Each picture is the top of the home page.

| | 375 wide, light | 375 wide, dark | 1280 wide, light | 1280 wide, dark |
|---|---|---|---|---|
| Version A | `a-375-light.jpg` | `a-375-dark.jpg` | `a-1280-light.jpg` | `a-1280-dark.jpg` |
| Version B | `b-375-light.jpg` | `b-375-dark.jpg` | `b-1280-light.jpg` | `b-1280-dark.jpg` |

Also `a-920-light.jpg` and `a-920-dark.jpg`, version A at 920 pixels wide, where the list of
moves was cramped before the check.

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
  by saying plainly, beside the number, that the 8 is what has been found so far and changes.
- **Standard practice or judgment call:** standard practice in the family. The Upgrade Tree shows
  "28 of 35" in the same place.
- **Strongest alternative:** keep the count alone and put the 8 in a sentence under it ("of the 8
  things found so far"). Cost: the scale John asked for is not seen at a glance, and he said a bare
  5 "isn't very compelling".
- **A reading risk the check raised:** a fraction reads as a scorecard, and "5 of 8 done" invites
  "3 to go", which could read as the site arguing that the 8 should be granted (guideline 5). The
  lines saying the 8 is only what has been found so far, and that it changes, are what keep it a
  record.
- **Would change on reflection:** if John rules this, older texts that describe the count as
  having no total need rewording: the opening note of `scripts/compute.py`, its `METHOD_STATUS`
  line (changing it rewrites `data/headline.json`; until then that file's method line contradicts
  the page), the type note in `site/src/lib/data.ts`, open question 4 in
  `docs/open-questions.md`, and rule 8's original note in `scripts/check_site.py`. They were left as
  they are, since nothing is ruled. The new site check refuses the count alone, so the branch can
  only be merged together with this ruling.

### Choice 2. How the fraction is shown

- **Proposal:** The Upgrade Tree's form: the count in the largest type, then "of 8" smaller and in
  a quieter colour inside the same line. One change from the sibling: a space before "of", inside
  the smaller type, so that a screen reader or copied text says "5 of 8" and not "5of 8".
- **Confidence:** high, because it is the sibling's settled form and the pictures show it reads in
  both themes at every width tried.
- **Standard practice or judgment call:** standard practice (family pattern, guideline 1).
- **Strongest alternative:** "5 / 8", or the 8 on a line of its own. Cost: unlike the sibling, and a
  slash reads as a score.

### Choice 3. How the movement of both numbers is shown

- **Proposal:** a short dated list, one row each time either number changed: the date, "6 of 9",
  and what changed, in words generated from the entries ("The first count."; "'What a model learned
  in one conversation is carried into the next' was moved beside the List, so it left both
  numbers."). Rows in which neither number moved (sentence changes only) are left out. The rows
  stack, date above, on a phone and in the two-column layout up to 1100 pixels wide.
- **Confidence:** moderate, because the form is plain and fits two points, but it has not been read
  by a stranger, and it adds three lines to the first screen on a computer.
- **Why not a chart:** there are two points. A line between two points shows a slope that means
  nothing, and it cannot say why a number moved, which here is the whole story: the drop from 9
  to 8 was a ruling about what belongs on the List, not a change in the world. A chart can come
  when there are enough points to show a shape.
- **Standard practice or judgment call:** judgment call. The Upgrade Tree shows change only on its
  dated changelog page ("The story so far"), not on the home page.
- **Strongest alternative:** no list on the home page, only a link to a dated page of changes, as
  The Upgrade Tree does. Cost: the reader at the top does not see that the 8 moves, which is what
  John asked to show.
- **A limit, from the check:** the reason beside a row is built from the entries as they stand
  today. If an entry ever left the count for one reason and later moved beside the List, the
  earlier row would give the later reason. It is correct for the only move so far.

### Choice 4. The line on the government's thing

- **Proposal:** "One of the 8 is for a government to do, not a developer: a law or an official
  body gives an AI system protection for its own sake. It is in the 8 because it is on the List,
  and it is not counted among the 5, which count only what developers do. The other 7 are the
  things in the table of developers below." The 7 is the table's own figure, and the build stops
  if the List is ever not the table plus this one thing.
- **Confidence:** moderate to high, because each clause is true of the records and the ruled
  meaning of counted, and the last clause joins the 8 to the "seven things" a reader meets in the
  developers' reading on the same screen.
- **What it brings to light, corrected after the re-check:** the ruled meaning of counted (at
  least one developer does it or has committed to it) and the code disagree on this one thing. By
  the ruled meaning it is never counted. But the code records a passed law by marking the thing
  as offered today, the same mark the count reads, so recording a law would put it into the count
  (the re-check showed "6 of 8" built and passed the site check). The first draft said the
  fraction "cannot reach 8 of 8 under that meaning, even if a law is passed"; that went further
  than the code holds and is withdrawn.
- **Held in code now:** the page stops building if the government's thing is among the counted
  entries, so "is not counted among the 5" cannot go false unnoticed. A scratch build with the
  thing marked as offered stopped with that message.
- **A question for John, not settled here:** if a government ever protects an AI system for its
  own sake, should the headline move (6 of 8), or stay 5 of 8 with the law shown only in the law
  reading? Until he rules, recording such a law stops the build, and the line or the count changes
  by his answer.
- **Standard practice or judgment call:** judgment call.
- **Strongest alternative:** leave the government's thing out of the second number, which would
  then be 7, matching the table. Cost: the second number would no longer be "things on the List",
  the known John asked to count; and two of the 7 measure what a model can do rather than what a
  developer does, so 7 has the same kind of problem.

### Choice 5. The sentence saying the 8 changes

- **Proposal:** "The 8 counts the things found so far that an AI model might reach for and that a
  dated public record can settle. It will change as more are found and given a test. How a new
  thing joins the List is not settled yet."
- **Confidence:** moderate to high, because every clause is true today: "will change" is John's
  own word from his request ("over time that number will change"), and no rule for adding things
  exists (open question 5).
- **Left out, because nothing rules it:** "never removed to improve the fraction" (the List has
  already lost one thing, and the list above the sentence shows it), and "will grow".
- **Standard practice or judgment call:** judgment call.
- **Strongest alternative:** "It will grow as more are found and given a test", the first draft's
  wording. It says the direction John expects (he liked "the scale of known objectives will always
  grow" on 2026-11-21) but states a forecast as fact, and the only move so far was down. It needs
  his ruling to stand on the page.

### Choice 6. The sentence beside the count (two versions, neither chosen)

The ruled sentence ("things a developer can do in how it treats the AI models it builds are done,
or publicly committed to, by at least one developer today") becomes untrue after "5 of 8". Read
together, it says all 8 are things a developer can do in how it treats its models, and three are
not: the government's thing, and the two things that measure what a model can do (a model working
on one task for days, and a model's report about its inner state checked against an independent
reading), as John's seventh answer of 2026-11-21 already found.

- **Version A** keeps the ruled words for the 5 and moves them into a second sentence: "5 of 8
  things on the List are done, or publicly committed to, by at least one developer today. Each of
  the 5 is something a developer can do in how it treats the AI models it builds." *For:* keeps
  every ruled phrase, including "done, or publicly committed to" and "in how it treats". *Against:*
  two sentences in the large type, and "the List" means little to a first-time reader.
- **Version B** says what the 8 are: "5 of 8 things found so far that an AI model might reach for
  are done, or publicly committed to, by at least one developer today." *For:* one sentence, it
  echoes the founding question just above it, and "found so far" carries John's point that the
  known changes. *Against:* it drops "in how it treats the AI models it builds", which John chose
  on 2026-11-21 so that the sentence counts a thing without saying whom it is for; and it puts
  "reach for" on the page outside the question for the first time (it is the question's own sense).
- **Confidence:** moderate that both are true and plain; no view on which is better, because the
  choice is between two things John ruled (the ruled phrase, and a fraction that shows the known).
- **Standard practice or judgment call:** judgment call.
- **Strongest alternative to both:** keep the ruled sentence word for word after the 5 alone, and
  put "of the 8 found so far" in a line under it. Cost: the 8 leaves the large type, which undoes
  choice 1.

Both versions keep "done, or publicly committed to", which John ruled to leave. No recommendation
is given.

### Choice 7. The breakdown's first label: "all 5", not "all of them"

- **Proposal:** "5, by one developer: all 5" in place of the ruled "5, by one developer: all of
  them" (ruled 2026-11-20). Under "5 of 8", "all of them" can be read as all 8. The 5 in the label
  is the count's own figure, checked against the file.
- **Confidence:** high, because the new reading is plainly wrong and the change is two words.
- **Standard practice or judgment call:** judgment call; it changes ruled wording, so it is John's.
- **Strongest alternative:** keep "all of them". Cost: a reader may take it as all 8.

### Choice 8. The site check

- **Proposal:**
  - **Rule 7d, extended.** The large type must be the count, then "of" and the number of things on
    the List, each marked; the count stays the first figure on the page. The second number must
    equal the served file's figure, and that must equal the number of things the List on the same
    page shows (the items in the section marked `id="list"`). A count alone is now refused once
    the served file is read, as is a wrong total or the total standing first.
  - **The list of how both moved** must hold exactly the points read from the served file's
    history (the first row, then each row where either number changed), each row's figure reading
    "N of M", with the last point today's figures.
  - **Rule 8, narrowed in two kinds of place only.** On the home page, the large type and the one
    figure in each row of the list of moves (the element marked `hl-frac`) are left out of the
    search for "5 of 8", because rule 7d checks each against the served file. The reason beside
    each row, the rest of the home page and every other page are still searched, and the served
    headline still may hold no total.
- **Confidence:** high, because every place the share may stand is checked figure by figure
  against the file, and eleven tests and two tampered builds show the guards refuse what they
  should. To be plain: the change to rule 8 lets "5 of 8" stand where it was refused before. That
  is what choice 1 asks for, and it is the one place a guard gives ground; it should be ruled with
  choice 1 or not at all.
- **Standard practice or judgment call:** standard practice (guards live in code; every figure is
  read from the file).
- **Strongest alternative:** a page-wide allowance for the fraction. Cost: it would let the share
  appear anywhere with nothing checking it.

## Not done here

- The check of 2026-11-21 read the first draft against John's published positions and found no
  disagreement. The changed lines need only the narrow re-check it describes.
- `site/src/data/window.json` as committed is behind what the export writes from today's records
  (about 300 lines differ). It was restored after each build and left alone, as asked.

## What the check changed

The check (`docs/reviews/2026-11-21-check-of-the-headline-fraction.md`) found one thing that had
to be fixed and eight smaller ones.

1. **Must fix, done.** The share check skipped the whole list of moves, so "5 of 8" written into
   the reason beside a row passed. Now only each row's figure is skipped; a test and a tampered
   build show the reason is searched again.
2. **"Governments", done** as "for a government to do, not a developer", matching the thing's own
   test, which counts a standing official body as well as a law.
3. **"Cannot be among the 5", reworded** to "is not counted among the 5". The check's other
   option, a refusal in `scripts/compute.py`, was declined: the law reading in `compute.py` uses the
   same offered flag as "met" for this thing, so the refusal would collide with existing code.
4. **"Will grow", changed** to John's own "will change"; "will grow" is now choice 5's strongest
   alternative, for him to rule.
5. **"All 5", done** in the draft and put to John as choice 7, since the label was ruled.
6. **The 5 in version A's second sentence is marked**, so the site check compares it with the file.
7. **The list of moves stacks** in the two-column layout up to 1100 pixels wide (picture at 920).
8. **A space before "of"**, placed inside the smaller type so that the large type does not open a
   wide gap.
9. **The write-up, done:** reasons for each confidence; choice 6 has its confidence, judgment call
   and strongest alternative.

From the check's notes: note 1 (8 and seven on one page) was taken up in choice 4's line; note 2
(each reason reads today's records) is recorded under choice 3; note 3 ("reach for" outside the
question) is recorded under choice 6; note 4 is under choice 1; note 5 needs nothing here.

## What the re-check changed

The re-check of the fixes (the latest section of the same review) passed them on two conditions,
both met here:

- **A. Choice 4 corrected.** It no longer says the fraction cannot reach 8 of 8 even if a law is
  passed; it says the ruled meaning and the code disagree, and puts the question to John.
- **B. A build check for the reworded line.** `site/src/components/Rebuilt.astro` stops the build
  if the government's thing is among the counted entries. It sits in the page, not in
  `scripts/compute.py`, so the law reading's use of the same mark is left alone.
