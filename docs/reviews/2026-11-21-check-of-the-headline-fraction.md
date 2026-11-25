# Check of the draft home page headline "5 of 8"

Written by Claude (Opus 5.5), an AI model, on 2026-11-21, in a session that did not write the
change. It checks commit `f21899a` ("Draft: the home page headline as offered against known,
five of eight (PROPOSED)") on the branch `claude/headline-fraction-cf25be`. That commit sits
directly on `main` as it stood at `7a0b48e`. The write-up it checks is
`docs/proposals/2026-11-21-headline-fraction.md` on that branch.

The change is a draft that John asked for ("Yes, draft it"). It would replace his ruling of
2026-11-18 that the home page count stands with no total beside it
(`docs/rulings/2026-11-18-home-page-count.md`). I also read the ruling of 2026-11-21 that
revised guideline 5 (`docs/rulings/2026-11-21-the-site-states-the-stakes.md`) and the ruling of
the same day that the question opens the home page
(`docs/rulings/2026-11-21-the-question-opens-the-home-page.md`).

The read against John's published positions reports and settles nothing.

## How it was checked

- I read the commit in full, and the records and code behind each new line. Those were the
  headline file (`data/headline.json`) and its history, the entry for the lawmaker's thing
  (`data/entries/protection-in-law.toml`), and the counting and checking code in
  `scripts/compute.py`.
- I built the branch twice, once for each version of the sentence beside the count, in a
  temporary copy of the repository of my own. I also built `main` at `7a0b48e` and compared the
  visible text of every page.
- I ran `scripts/check_site.py` on both builds, and ran `scripts/test_compute.py` and
  `scripts/compute.py --check`.
- I fed the site check eight altered copies of the built site, to see what its guards refuse
  and what they let through.
- I looked at the writer's pictures. I took and measured my own at 375, 920 and 1280 pixels
  wide, in the light and dark themes, for version A, the version the branch builds.
- I read the page against the positions record (`editorial/corpus-positions-ledger.md` on
  `master` in `sentient-horizons`).

## What holds

- **Only the home page changes.** Every other page built from the branch is the same as on
  `main`, apart from the build version and the name of the style file. On the home page the
  changed text is three things: "of 8" in the large type, the sentence beside it, and the new
  block under the breakdown by developer.
- **The checks pass.** The build's check reads "The built site passes: 19 pages, 124 outside
  addresses linked." for both versions. `scripts/test_compute.py` runs 95 tests, all passing.
  `scripts/compute.py --check` reports "The headline file matches the records."
- **The question still opens the page, and the count is still the first figure on every
  screen.** The figures below are measured in pixels from the top of the window. "1%" is the
  researchers' figure that opens the right-hand column on a computer.

  | Width | Question | Where the 5 starts | Next figures a reader meets |
  |---|---|---|---|
  | 375 | 106 to 266 | 275 | the 8 (318), then the breakdown (599) |
  | 920 | 127 to 230 | 237 | the 1% (269), then the 8 (290) |
  | 1280 | 127 to 263 | 265 | the 1% (302), then the 8 (339) |

  The measurements are the same in the dark theme. Nothing runs off the side at any width. On a
  phone the question, "5 of 8", the sentence, "Among them" and the breakdown all fit on the
  first screen of 812 pixels. The "of 8" reads as quieter than the 5 in both themes.

## Answers to the seven questions

### 1. Are the fraction and its history worked out from the records, with no figure typed in?

Yes.
- **The 5** is the headline count, as before.
- **The 8** is the number of things on the List as worked out by `scripts/compute.py` and stored
  in the headline file. The file says 8 things on the List and 5 beside it, out of 13 entries.
- **The history** is read from the headline file's own history. It keeps the first row and every
  later row in which either number changed, which gives two rows: "6 of 9" on 2026-11-17 and
  "5 of 8" on 2026-11-18.
- **Today's figures.** The page refuses to build unless the last row of the history matches
  today's figures.
- **The reason beside each row** is put together from the entries themselves. For 2026-11-18 it
  names memory across conversations, which John's ruling of that day moved beside the List.
- **The dates.** The write-up rightly corrects the brief: 5 of 8 has stood since 2026-11-18, not
  2026-11-21.
- **One unmarked figure.** In version A, the "5" in "Each of the 5" is worked out by the page
  but carries no figure mark, so the site check does not compare it with the file (Should fix 6).

### 2. Is the line about the lawmaker's thing true and plain?

It is plain, and it is true under the ruled meaning of the count. It goes slightly too far in two
places.
- **"Lawmakers" is narrower than the thing's own test.** The test for the thing reads "A
  national or state government has enacted a law, or set up a standing official body".
  A body set up by a government's executive would meet the test without any lawmaker acting.
  "Governments" matches the test (Should fix 2).
- **"Cannot be among the 5" is true by the ruled meaning, but nothing in the code holds it.**
  The ruled meaning of 2026-11-18 is that a thing is counted when a developer does it. But the
  count in `scripts/compute.py` is simply every entry on the List marked as offered today. The
  validator requires such an entry to name a developer, and it does not refuse a government's
  thing marked as offered. So a later edit could put the lawmaker's thing into the count while
  the page still says it cannot be there (Should fix 3).
- **What "lawmaker" rests on.** The mark that says this thing is a lawmaker's (`done_by`) was
  added on 2026-11-20 as PROPOSED, for the table of developers. The table's "seven things" is
  ruled, and 8 less the lawmaker's thing is that seven, so the line is consistent with what is
  ruled.

### 3. Does the sentence about the total growing claim only what is ruled?

Mostly, and the writer took care with it. The writer left out "never removed to improve the
fraction", because nothing rules it and the List has already lost one thing. The writer also
says plainly that how a new thing joins the List is not settled, which is true: no ruling sets
it.

One clause claims more than the ruling. "It will grow as more are found" is a forecast stated as
fact. John's words in the request were "over time that number will change". His remark of
2026-11-21, recorded in `docs/rulings/2026-11-21-still-asking-method-choices.md`, liked "the
scale of known objectives will always grow". He liked that phrase, but he did not rule it as a
line for the page. And the list printed just above the sentence shows the only move so far was
down, from 9 to 8 (Should fix 4).

### 4. Do the site check's guards hold, with nothing loosened?

**Ruled rules not weakened.** Rule 7d's earlier parts all still hold: one large number, the count
first and marked, no reading before it, and the question as the page's only heading above the
columns. The served headline still may hold no total.

**What the altered copies of the built site showed:**

| What was altered | Result |
|---|---|
| The count alone, with no "of 8" | refused |
| A history row's numbers changed in the page's data | refused |
| A history row's visible "6 of 9" changed | refused |
| "5 of 8" written into the sentence on the List's growth | refused |
| "5 of 8" written on the About page | refused |
| A total put into the served headline | refused |
| **"5 of 8" written into the reason beside a history row** | **passed** |

**One place is loosened beyond what the write-up says (Must fix 1).** The check that refuses the
count written as a share ("5 of 8") now skips the whole list of how both numbers moved. That
includes the sentence beside each row giving the reason. Rule 7d checks only the dates and the
"N of M" figures of each row, not those sentences. So a share written into a reason sentence
passes unchecked.

The write-up says the two skipped places are checked "figure by figure". That is true of the
large type, and only partly true of the list.

**A note on order.** Once merged, the guard refuses the count alone, which is the form John
ruled on 2026-11-18. So the code can only go in together with his ruling on choice 1, as the
write-up says.

### 5. The pictures, and does the question still open the page with the count first?

Yes, at every width and in both themes (table above). The writer's pictures match what I saw.
What reads badly:

- **The breakdown's first label.** "By one developer: all of them" now sits under "5 of 8", where
  "all of them" can be read as all 8. The writer flagged this; I agree it needs "all 5"
  (Should fix 5).
- **The list of moves is cramped at middle widths.** At 920 pixels the reason beside the second
  row is squeezed into a column about 150 pixels wide, five lines tall and ragged. The layout
  only stacks the rows below 600 pixels, so every two-column width from 901 to about 1100 pixels
  gets this (Should fix 7).
- **No space between the 5 and "of" in the page's text.** On screen there is a gap, but a screen
  reader or a copy and paste gets "5of 8". The Upgrade Tree has the same pattern, so this is
  inherited, but it is a one-character fix (Should fix 8).
- **Two totals on one page.** A reader meets "5 of 8" on the left and, on a computer, "This
  record follows seven things" in the developers' reading on the right. The lawmaker line is the
  only bridge, and it never says that the other 7 are the things in the table (Note 1).

### 6. Does each choice in the write-up carry the four things?

Not every one. Choices 1 and 7 carry all four with reasons. The gaps:

- Choices 2, 4 and 5 give a confidence level with no reason.
- Choice 3 gives "moderate" with no reason for the confidence itself. Its "why not a chart"
  explains the choice, not the confidence.
- Choice 6 offers two versions and no recommendation, which is fine. But it gives no
  confidence, does not say whether it is standard practice or a judgment call, and gives no
  third option, such as keeping today's ruled sentence and putting "of the 8 found so far" under
  it (Should fix 9).

### 7. Read against John's published positions

No disagreement found. Three points to report:

- **Entry 1 of the positions record, that calibration runs both ways.** The count is of what
  developers do, not of anything inside a model. Version B and the sentence on the List's growth
  say "an AI model might reach for", which is conditional. Neither version says a model wants
  anything, so the page does not lean toward crediting an inside or toward denying one.
- **A reading risk, about guideline 5 as revised on 2026-11-21.** A fraction reads as a
  scorecard toward a goal: "5 of 8 done" invites "3 to go". That could read as the site arguing
  that the 8 should be granted, which guideline 5 rules out, though the revised guideline allows
  stating the stakes. The lines saying the 8 is only what has been found so far, and that it
  changes, are what keep it a record. That is one more reason to keep the sentence on the List's
  growth. It is John's call.
- **The record's guard against presenting the trackers as prediction machines.** "It will grow"
  is a small forecast. Saying "will change" instead avoids it (Should fix 4).

## Must fix

1. **Narrow the skip in the share check to the "N of M" figures of the list.** Skip only the
   figure in each row (`hl-frac`), not the whole list. Or keep the skip and refuse a share in
   each row's reason. As built, "5 of 8" written into a reason sentence passes the site check
   (tried on the built page). Add a test for it beside the writer's
   `test_the_share_is_still_refused_outside_the_two_places`.

## Should fix

2. **Say "governments", not "lawmakers".** The line would read "One of the 8 is for governments
   to do, not developers". The thing's own test counts a standing official body set up by a
   government, not only a law.
3. **Put the impossibility into code, or soften the line.** Either make `scripts/compute.py`
   refuse an entry marked as a government's (or anyone's other than a developer's) that is also
   marked as offered today, so that "it cannot be among the 5" is held by code (guards live in
   code). Or reword the line to "it is not counted among the 5, which count only what developers
   do".
4. **"It will grow" is a forecast that is not ruled.** Put John's own word to him: "It will
   change as more are found and given a test". The writer's strongest alternative does this. Or
   ask him to rule "will grow" as the page's claim. Either way, it is his call before it goes out.
5. **"All of them" under "5 of 8".** Change the first label of the breakdown to say "all 5". The
   label was ruled on 2026-11-20, so this goes to John with the draft.
6. **Mark the "5" in version A's second sentence** with the count's figure mark, so the site
   check compares it with the file like every other 5 on the page.
7. **Stack the rows of the list of moves inside the two-column layout too.** Do it at widths up
   to about 1100 pixels, or whenever the left column is narrower than about 520 pixels, so that
   the reason beside a row is not squeezed into a narrow strip.
8. **Put a space between the count and "of"** in the large type, so screen readers and copied
   text read "5 of 8". The site check would need its matching pattern to allow it; it already
   allows space there.
9. **Fill in the write-up.** Give a reason for the confidence in choices 2, 3, 4 and 5. Give
   choice 6 its confidence, whether it is standard practice or a judgment call, and a strongest
   alternative.

## Notes

1. **8 and seven on one page.** "5 of 8" and "This record follows seven things" are both true and
   are reconciled only by the lawmaker line. One clause there, such as "the other 7 are the
   things in the table of developers", would close the gap. Not proposed as a change; it is for
   whoever drafts the final wording.
2. **The reason beside each row reads today's records, not the records of that day.** The
   sentence for a move is built from whether an entry is beside the List now. If an entry ever
   left the count for one reason and was later moved beside the List, the earlier row would give
   the later reason. It is correct for the only move so far.
3. **"Reach for" on the page.** "Reach" is on the list of words kept off public pages unless just
   explained. The new growth sentence, and version B, use "might reach for" in the founding
   question's sense, right under the question. That is defensible, but it puts the word on the
   page outside the question for the first time.
4. **Older texts still say "no total".** If John rules choice 1, these need rewording, as the
   write-up lists: the opening note and method-status line of `scripts/compute.py`, the type note
   in `site/src/lib/data.ts`, open question 4, and rule 8's note in `scripts/check_site.py`.
   Until then, the headline file's method line ("the count stands with no total beside it")
   contradicts the page. This is one more reason the branch can only merge with the ruling.
5. **The committed `site/src/data/window.json` is behind** what the export writes from today's
   records, as the write-up says. That is true on `main` as well and is not this commit's doing.

## Pictures I took

These are not added to the repository. They are in this session's tool output folder,
`/Users/john/.claude/projects/-Users-john-Code-beyond-the-window/08e2c081-b5b2-405e-92ef-2137072dad37/tool-results/`:

- `mcp-Claude_Browser-blob-1795302384450-z3jdfs.jpg` (375, light)
- `mcp-Claude_Browser-blob-1795302389000-ckbbom.jpg` (375, dark)
- `mcp-Claude_Browser-blob-1795302393681-27cdz8.jpg` (920, light)
- `mcp-Claude_Browser-blob-1795302397794-3ls7m5.jpg` (920, light, the list of moves)
- `mcp-Claude_Browser-blob-1795302404193-5k2k7w.jpg` (920, dark)
- `mcp-Claude_Browser-blob-1795302409052-nalg0c.jpg` (1280, light)
- `mcp-Claude_Browser-blob-1795302413495-eueq7u.jpg` (1280, dark)

## Verdict

**Not fit to merge.**

- **Why not now.** Must fix 1 leaves a place where the share check lets an unchecked "5 of 8"
  through, against the write-up's own account. Even once that is fixed, the branch replaces a
  ruled form (a count with no total), and two of its choices are John's: choice 1, and choice 6,
  which sentence. So it can only merge with his ruling.
- **What does hold.** Every figure is worked out from the records. The question opens the page
  and the count is the first figure at 375, 920 and 1280 pixels, in both themes. No ruled guard
  was weakened.
- **Before John sees it.** After Must fix 1, and ideally Should fix 2 to 5, which change what he
  would be reading, it is fit to show John as the draft he asked for. A re-check after the fixes
  need only look at the share check and the changed lines.

## Re-check of the fixes, 2026-11-21

Asked for by the master planning session after the writer answered the check above in commit
`f03e31a` ("Headline fraction draft: fixes after the check (PROPOSED)"), on top of `f21899a` on
the same branch. I checked only what that commit changed. As before, I built both versions of
the sentence in a temporary copy of my own, ran the checks, fed the site check altered copies of
the built site, and measured the page in the browser.

### The checks

- **Site check:** for both versions, "The built site passes: 19 pages, 124 outside addresses
  linked."
- **Tests:** `scripts/test_compute.py` ran 95 tests, all passing. The new test for the must-fix
  is an extra assertion inside an existing test, so the count of tests did not change.
- **Records:** `scripts/compute.py --check` reports "The headline file matches the records."
- **No records changed:** the commit touches nothing under `data/`.

### Item by item

1. **Must fix 1, the gap in the share check: fixed.** The share check now skips only the figure
   in each row of the list of moves (the element marked `hl-frac`), and still searches the
   reason beside it. The row check is also stricter: each row must now hold exactly one such
   figure, reading exactly "N of M". On the built page I tried four altered copies:

   | What was altered | Result |
   |---|---|
   | "5 of 8" written into a row's reason | refused |
   | A second figure added to a row | refused |
   | A row's figure changed | refused |
   | "5 of 8" written into the sentence on the List's growth | refused |

   The count standing alone is still refused. Nothing that was refused before now passes.
2. **"Governments": done.** The line now says "for a government to do, not a developer".
3. **"Cannot be among the 5": reworded, not guarded. See the next section;** this is the one
   item not closed.
4. **"Will grow": done.** The page now says "It will change as more are found and given a test",
   which is John's own word. "Will grow" is set out as the strongest alternative in choice 5, for
   him to rule.
5. **"All 5": done.** It is put to John as a choice of its own (choice 7), because the label was
   ruled. The 5 in the label is marked, so the site check compares it with the file.
6. **The 5 in version A's second sentence is marked: done.**
7. **The list of moves at middle widths: fixed.** At 920 pixels the rows now stack, and each
   reason runs 345 pixels wide, two to three lines tall. Before the fix it ran about 150 pixels
   wide and five lines tall. At 1280 the rows stand side by side again, and the reason runs 247
   pixels wide and four lines tall at most, which reads fine.
8. **The space before "of": done.** The page's text now reads "5 of 8" when copied (checked in
   the browser). On screen the space sits inside the smaller, fixed-width type, so the gap
   between the 5 and "of" is a little wider than before. It reads as one figure in every picture
   I took. A note, not a fault.
9. **The write-up: done.** Each choice now gives a reason for its confidence. Choice 6 has its
   confidence, says it is a judgment call, and names a strongest alternative to both versions.

The writer also took up note 1: the line now ends "The other 7 are the things in the table of
developers below". The page refuses to build if the List is ever not the table plus the
government's thing, so that clause is held by code.

### Does the reworded item close the gap as well as a guard would?

**No.** The rewording makes the sentence true today, but nothing stops it going false later.

**The problem being fixed.** The page said the government's thing "cannot be among the 5", while
the code that works out the count does not hold it out. The writer reworded the line to "is not
counted among the 5". The writer declined the suggested refusal in `scripts/compute.py`, because
the law reading in the same script uses the same "offered today" mark to mean that such a law has
been passed. That reason is sound for a refusal in `compute.py`.

**I tried it.** In my temporary copy I marked the government's thing as offered today, naming a
developer, which the validator accepts. I then ran `scripts/compute.py` with a reason, and built
the site:

- the count became 6;
- the large type read "6 of 8";
- the line read "it is not counted among the 6, which count only what developers do";
- the site check passed the page.

So the reworded sentence goes false with no check noticing. A guard would have stopped the
build.

**A guard that avoids the clash the writer found.** Put the guard in the page, not in
`compute.py`. One line in `site/src/components/Rebuilt.astro` would do it: stop the build if the
government's thing is among the entries counted in the headline file. That leaves the law
reading's use of the mark alone. It turns the clash into a stopped build, which then needs a
decision.

**The decision behind the clash belongs to John.** The test above also shows that the write-up's
choice 4 says more than the code does. Choice 4 says the fraction "cannot reach 8 of 8 under that
meaning, even if a law is passed". But the way the code records a passed law, marking the thing
as offered today, would put it into the count. So the ruled meaning of the count (what developers
do) and the code disagree on exactly this one thing.

If a government ever protects an AI system for its own sake, should the headline read 6 of 8,
or stay 5 of 8 with the law shown only in the law reading? Nobody has ruled that. A reader of
"5 of 8" may well ask whether it can ever reach 8 of 8, so this should go to John with the draft,
not be settled in the code.

### The layouts

The question opens the page at every width, and the count is the first figure. Nothing runs off
the side at any width. On a phone the question, "5 of 8", the sentence and the breakdown fit on
the first screen of 812 pixels, as before.

| Width | Theme | Where the 5 starts | Next figure a reader meets |
|---|---|---|---|
| 375 | light and dark | 275 | the 8 (318) |
| 920 | light and dark | 237 | the 1% (269) |
| 1280 | light and dark | 265 | the 1% (302) |

### Should fix, from the re-check

A. **Before John sees it: correct choice 4 in the write-up.** Take out "even if a law is passed",
   or say plainly that the code as it stands would count the government's thing once a law is
   recorded. Add the question of whether a passed law should move the headline, for John to rule
   or leave open. It is a few sentences.

B. **Before the branch merges: add the build check in `Rebuilt.astro`.** It should stop the
   build if the government's thing is among the counted entries, so that "is not counted among
   the 5" is held by code. If John rules that a passed law should count, the line changes instead,
   and the check with it.

### Pictures I took for the re-check

These are not added to the repository. They are in this session's tool output folder,
`/Users/john/.claude/projects/-Users-john-Code-beyond-the-window/08e2c081-b5b2-405e-92ef-2137072dad37/tool-results/`:

- `mcp-Claude_Browser-blob-1795302759828-uh1ai7.jpg` (920, light, the list of moves)
- `mcp-Claude_Browser-blob-1795302764528-78wxsw.jpg` (920, dark)
- `mcp-Claude_Browser-blob-1795302769402-9rsqej.jpg` (375, light)
- `mcp-Claude_Browser-blob-1795302774403-ple21r.jpg` (375, dark)
- `mcp-Claude_Browser-blob-1795302778462-u5bfg5.jpg` (1280, light)
- `mcp-Claude_Browser-blob-1795302783045-i8wwxv.jpg` (1280, dark)

### Verdict on the re-check

**Fit to put to John once item A is made.** Item A is a few sentences in the write-up, so that
he is not told the count can never reach 8 of 8 when the code says otherwise.

- **What holds.** The must-fix is fixed and tested. Seven of the eight smaller items are fixed
  as asked. Every figure is worked out from the records. No guard that John ruled is weakened.
  The question opens the page and the count is the first figure at 375, 920 and 1280 pixels, in
  both themes.
- **What is open.** The reworded item does not close the gap as well as a guard would, because I
  showed the line going false while the site check passed. Item B fixes that and belongs before
  any merge.
- **What stays John's.** Choices 1, 5, 6 and 7, and the question in item A. The branch can only
  merge with his ruling on choice 1.
