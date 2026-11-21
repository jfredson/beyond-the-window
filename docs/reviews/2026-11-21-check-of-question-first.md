# Check of the change that puts the founding question first on the home page

Written by Claude (Opus 5.5), an AI model, on 2026-11-21, in a session that did not write the
change. It checks commit `1e175aa` ("The founding question opens the home page, with the count
directly beneath") on the branch `claude/question-first-b8d91f`, against John's ruling of
2026-11-21 (`docs/rulings/2026-11-21-the-question-opens-the-home-page.md`) and the writing
session's note (`docs/proposals/2026-11-21-question-first.md` on that branch). The read against
John's published positions reports and settles nothing.

## How it was checked

- Read the commit in full with `git show`. It touches three site files
  (`site/src/components/Rebuilt.astro`, `site/src/pages/index.astro`,
  `site/src/styles/rebuild.css`) and adds the note and four pictures. It changes no script, no
  data file and nothing under `site/src/lib`.
- Built the commit and the main branch as it stood before it (`6de3687`) side by side, each in a
  temporary copy of the repository of my own, and compared the visible text of every built page.
- Ran `scripts/check_site.py` (through the build) and `scripts/test_compute.py` on the commit.
- Fed the site check's headline test two broken copies of the built home page, to see that it
  still refuses them.
- Looked at the writing session's four pictures, and took my own of the built page at 375 and
  1280 pixels wide, in the light and dark themes, plus one at 920 pixels wide, measuring where
  each part of the page falls.
- Read the changed page against the positions record
  (`sentient-horizons` branch `master`, `editorial/corpus-positions-ledger.md`).

## What holds

- **The order is as ruled.** On every width the page now opens with the short line "A dated
  record of how the world is treating AI models", then the question, then the 5, its sentence,
  the "Among them" line and the breakdown by developer. The paragraph "This record holds ..."
  stays after the breakdown, where it was.
- **No wording changed.** The visible text of the home page is the same set of lines as before,
  with one line moved: the question. The only other difference is the build version in the
  footer (`6de3687` against `1e175aa`), which every build changes. Every other page of the site
  is the same apart from that version and the name of the style file.
- **The question is the page's only `h1`,** still read from the `QUESTION` constant.
- **The count is still read from the headline file.** The lines that write the 5 and the
  breakdown (`h.count`, `d.offered`, with their figure marks) are unchanged; only the `h1` line
  moved above them.
- **The checks pass.** The build's check: "The built site passes: 19 pages, 124 outside
  addresses linked." `scripts/test_compute.py`: 82 tests, all passed.
- **The check that the first figure is the count still applies and was not loosened.** The
  script is unchanged. Given a copy of the page with a figure put inside the question, it
  answered "the first figure on the page is not the count (researchers.0 comes first)"; given a
  second number in the large type, "the page should hold one number in the large type, the
  count, and 2 were found".
- **On a phone the number stays on the first screen.** At 375 by 812 pixels the question ends
  266 pixels down, the 5 stands from 284 to 353, and the breakdown ends at 628, so the short
  line, the question, the count, its sentence and the breakdown all fit on the first screen, in
  both themes. Nothing runs off the side (the page is exactly 375 pixels wide). In the dark
  theme the question is light on the dark ground and reads well.

## Must fix

1. **On a computer, a reading now stands above the count, so the count is no longer the first
   figure a reader sees.** The ruling says the rest of the 2026-11-20 ruling stands: "the count
   is still the first figure on the page". On a screen wider than 900 pixels the home page is two
   columns, and the right-hand column of readings still starts at the top. At 1280 pixels wide
   the researchers' figure "1%" stands 113 pixels down, level with the start of the question,
   while the 5 now starts 373 pixels down, 260 pixels lower. At 920 pixels wide it is the same
   (1% at 113, the 5 at 335). Before this change the 5 and the 1% stood level at the top of their
   columns. So a reader on a computer meets "1%" first, beside the question, and the count only
   after the question's five lines.

   The site check passes because it reads the page's source order, where the count still comes
   before the readings; it cannot see where the columns put things. Its test "a reading stands
   above the count" was written for exactly this case, and the page now does in what a reader
   sees what the test refuses in the source.

   *A fix that keeps the ruling whole:* move the short line and the question out of the left
   column into a row of their own across the full width, above the two columns. The question
   then opens the page on every screen, and below it the count and the first reading start level,
   as they did before. On a phone nothing changes, because the columns already stack there.
   The question would then run across a wider line (about 1030 pixels) and want a narrower
   measure (its present 640-pixel limit would hold it to two or three lines). *The other way out
   is John's:* rule that on a computer a reading may stand beside the question, above the count.
   *Confidence that this needs fixing before it goes out:* high, because the ruling names the
   point. The writing session's pictures show it, but its note does not mention it.

## Should fix

None beyond the one above.

## Notes

1. **The question now looks heavier than the count.** The question is set in a heavy serif at
   28 to 40 pixels, and the 5 in a light sans at 75 to 128 pixels. The 5 is still the largest
   type on the site, as the note says, but on a phone the five lines of heavy type above it carry
   more weight on the screen than the single light figure. That suits a page where the question is
   the headline. It is worth John seeing it in the pictures with that in mind, not a fault.
2. **The question wraps to five lines at both 375 and 1280 pixels,** and at 1280 the left column
   is only 491 pixels wide, so the 40-pixel type fills it. No line breaks awkwardly ("is each of
   those things?" ends it at both widths). The fix in Must fix 1 would give it room.
3. **The gap between the question and the 5 is 18 pixels.** It reads as close but separate in
   every picture I took. No change asked.
4. **The writing session's pictures are light theme only.** Mine add the dark theme; the page
   reads the same in both. If John wants dark pictures with the ones he sees before the push, they
   are cheap to take.
5. **Working words.** The question says "reach for", and "reach" is on the list of working words
   kept off public pages. Here it is an ordinary verb in John's own ruled wording, and it was
   already the page title before this change, so this commit does not raise it. Noted only
   because the question is now the most prominent line on the site.

## Read against John's published positions

No disagreement found. The change moves one line and alters no wording, so the claims on the
page are the ones already there.

- The positions record's first entry, that calibration runs both ways (crediting a machine with
  an inside it may not have, and denying one it may have, are both errors with costs), is the
  one the new order bears on most. The question is conditional ("What might a machine mind reach
  for"), so leading with it asserts nothing about an inside. The count beneath it counts what
  developers do, not anything about the models, so the order does not tip the page either way.
- One thing to watch, which is about reading and not a disagreement: with the question as the
  headline and the 5 straight under it, a stranger may at first take the 5 as an answer to the
  question (five things a machine mind reaches for). The sentence under the 5 says plainly what is
  counted, which is the point of keeping it directly beneath. This was the trade the ruling
  weighed, and it is John's.
- Nothing on the page counts what a model says about itself as evidence (entries 4 and 21 of
  the record, on self-report), and nothing new speaks of a model wanting or feeling.

## Pictures I took

Not added to the repository. They are in this session's tool output folder:

- `/Users/john/.claude/projects/-Users-john-Code-beyond-the-window/08e2c081-b5b2-405e-92ef-2137072dad37/tool-results/mcp-Claude_Browser-blob-1795283190611-524wwg.jpg` (375 wide, light)
- `/Users/john/.claude/projects/-Users-john-Code-beyond-the-window/08e2c081-b5b2-405e-92ef-2137072dad37/tool-results/mcp-Claude_Browser-blob-1795283197464-567ao3.jpg` (375 wide, dark)
- `/Users/john/.claude/projects/-Users-john-Code-beyond-the-window/08e2c081-b5b2-405e-92ef-2137072dad37/tool-results/mcp-Claude_Browser-blob-1795283204177-ns8xz2.jpg` (1280 wide, light)
- `/Users/john/.claude/projects/-Users-john-Code-beyond-the-window/08e2c081-b5b2-405e-92ef-2137072dad37/tool-results/mcp-Claude_Browser-blob-1795283215814-nk56ej.jpg` (1280 wide, dark)
- `/Users/john/.claude/projects/-Users-john-Code-beyond-the-window/08e2c081-b5b2-405e-92ef-2137072dad37/tool-results/mcp-Claude_Browser-blob-1795283222744-tkk94g.jpg` (920 wide, light)

## Verdict

**Not fit to merge as it stands,** because of Must fix 1: on a computer the researchers' 1%
now stands above the count, against the ruling's own words that the count is still the first
figure on the page. Everything else holds: no wording changed, the question is the `h1`, the
count is read from the headline file, both checks pass and the count check is as strict as
before. Once the short line and the question span both columns (or John rules the side-by-side
acceptable), it is fit to merge, and a re-check need only look at the computer layout.

## Re-check of the fix, 2026-11-21

Asked for by the master planning session after the writer fixed Must fix 1 in commit `4525a84`
("The question stands above both columns, so the count is the first figure on a computer too"),
on top of `1e175aa` on the same branch. Only what that commit changed was checked.

### What changed

- `site/src/components/Rebuilt.astro`: the short line and the question now sit in a block of
  their own (`hl-head`) before the two-column block (`rb-first`), instead of at the top of the
  left column.
- `site/src/styles/rebuild.css`: the question may run up to 860 pixels wide, with its lines
  evened out (`text-wrap: balance`); the right-hand column's top space drops from 34 to 8 pixels;
  the left column's top space is removed. The phone rules are untouched.
- `scripts/check_site.py`: rule 7d gains a new part (below).
- `scripts/test_compute.py`: the sample home page in the tests now has the question in its own
  block above the columns, and three tests are added.

### Wording and other pages

Built `4525a84` and the main branch before the change (`6de3687`) side by side. The visible text
of the home page is the same set of lines; the only difference is the build version in the
footer. Every other page is the same apart from that version and the style file's name.

### The checks

- The build's check: "The built site passes: 19 pages, 124 outside addresses linked."
- `scripts/test_compute.py`: 85 tests, all passed (82 before, plus the three new ones).

### The new guard

The new part of rule 7d refuses a home page that does not have exactly one `h1`, whose `h1`
comes after the start of the two-column block, or whose `h1` comes after the first reading or
after the count. All the earlier parts of rule 7d are unchanged, line for line: one number in
the large type, marked as the count, equal to the count in the headline file, the first marked
figure, and no reading before it. So the new part only adds refusals and loosens nothing.

I tried it on real pages, not only the test samples:

- the page as now built: passes;
- the page as built from the first draft (`1e175aa`): refused, "the question stands inside the
  two columns, so on a computer a reading can stand beside it, above the count", which is
  exactly the fault found above;
- the page with a second `h1` added: refused, "the page should hold one h1, the question, and
  2 were found".

One gap, a note and not a fault: if the two-column block were renamed so that it no longer has
the class `rb-first`, the column part of the guard would find nothing to compare and would pass
the page silently. I tried it, and it does. The rule of 2026-11-20 that the count comes before
every reading still holds in that case, so nothing is loosened; but a later rebuild of the page
could lose the column test without noticing. A cheap hardening would be to refuse a home page
with no `rb-first` block. It does not block the merge.

As the writer's comment in the script says, the check reads the page's structure and cannot
measure where the browser draws things; that is why I measured as well.

### The layouts, measured

Distances are from the top of the window, in pixels, taken in the browser. "First figures on
screen" lists the marked figures in the order a reader meets them, top to bottom.

| Width | Theme | Question | The 5 starts | First figures on screen |
|---|---|---|---|---|
| 1280 | light | 127 to 263, three lines, 860 wide | 265 | the count (265), then the researchers' 1% (302) |
| 1280 | dark | same | 265 | the count (265), then 1% (302) |
| 920 | light | 127 to 230, three lines, 860 wide | 237 | the count (237), then 1% (269) |
| 920 | dark | same | 237 | the count (237), then 1% (269) |
| 375 | light | 106 to 266, five lines | 275 | the count (275), then the breakdown (573); the first reading is at 1055 |
| 375 | dark | same | 275 | same |

So the 5 is the first figure on every screen checked, and on a computer it and the 1% now start
almost level, as they did before the question moved. Nothing runs off the side at any width.
On a phone the page is exactly as it was in the first draft (the same measurements to the
pixel), and the short line, the question, the count, its sentence and the breakdown all fit on
the first screen of 812 pixels.

The question now reads in three even lines across both columns on a computer, which answers
note 2 above: it no longer squeezes into the left column. In the dark theme it reads as well as
in the light.

### Notes from the re-check

1. **The guard depends on a class name.** As set out above; worth hardening later.
2. **On a computer the question now runs past the left column** into the space above the
   readings (it is 860 pixels wide against a left column of 491 at 1280). That is the intent of
   the fix and reads well: the question heads the whole page, not only the count.
3. Notes 1, 3, 4 and 5 of the first check stand as they were. The read against John's published
   positions is unchanged, because no wording changed.

### Verdict on the re-check

**Fit to merge.** Must fix 1 is fixed: the 5 is the first figure a reader meets at 375, 920
and 1280 pixels wide, in both themes. No wording changed, both checks pass, and the new guard
only adds refusals and catches the first draft's layout. The one gap in the guard is a note for
later.

Pictures I took for the re-check, outside the repository, in this session's tool output folder
(`/Users/john/.claude/projects/-Users-john-Code-beyond-the-window/08e2c081-b5b2-405e-92ef-2137072dad37/tool-results/`):
`mcp-Claude_Browser-blob-1795284092513-5b51b6.jpg` (1280, light),
`mcp-Claude_Browser-blob-1795284097567-jhgp0c.jpg` (1280, dark),
`mcp-Claude_Browser-blob-1795284102664-m3rsc5.jpg` (920, light),
`mcp-Claude_Browser-blob-1795284107217-hhtfei.jpg` (920, dark),
`mcp-Claude_Browser-blob-1795284112403-ha3m2z.jpg` (375, light),
`mcp-Claude_Browser-blob-1795284116797-wdj4ow.jpg` (375, dark).
