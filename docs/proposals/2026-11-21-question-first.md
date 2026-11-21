# The question opens the home page: the change as built

Written by Claude (Opus 5.5), an AI model, in a writing session on 2026-11-21. A draft on the
branch `claude/question-first-b8d91f`, not published. It carries out John's ruling of
2026-11-21 that the founding question opens the home page on every screen
(`docs/rulings/2026-11-21-the-question-opens-the-home-page.md`), which amends his ruling of
2026-11-20 that the page opens with the number
(`docs/rulings/2026-11-20-home-page-opens-with-a-headline-again.md`). A different session
checks it, and John sees the pictures before it is pushed.

## What changed

The top of the home page now reads, in this order, on every screen width:

1. the short line "A dated record of how the world is treating AI models";
2. the founding question, still the page's `h1` and still read from the `QUESTION` constant in
   `site/src/lib/data`;
3. the count (5) in the large type, its sentence, the line "Among them: ...", and the breakdown
   by developer, all as before, every figure still read from the headline file;
4. the paragraph "This record holds what has been done about AI models, by whom and when, each
   with a source a reader can open.", then the dated notes on when the record was read and
   checked, and the two buttons.

No wording changed anywhere on the page. The code comments in `site/src/pages/index.astro`,
`site/src/components/Rebuilt.astro` and `site/src/styles/rebuild.css` that said the page opens
with the number now say it opens with the question, and name the ruling of 2026-11-21.

**Where the paragraph "This record holds ..." went.** It stays after the number block, directly
under the breakdown, where it was before. It reads best there because it says what the record
as a whole holds, after the reader has met the question and the count, and it leads into the
dated notes on when the record was read, which are about the same record.
*Strongest alternative:* put it straight under the question, as a plain answer to "what is this
site", before the number. That would explain the site sooner, but it would push the count down
by three lines on a phone and put a paragraph between the headline and the figure the ruling
says follows "directly beneath".

## Second pass, after the check

The check of the first commit (`docs/reviews/2026-11-21-check-of-question-first.md`, kept in the
main checkout) found one thing that had to be fixed. On screens wider than 900 pixels the page
is two columns. With the question inside the left column, the right-hand column of readings still
started at the top, so the researchers' "1%" stood beside the question, about 260 pixels above
the 5. That broke the ruling's words "the count is still the first figure on the page". The
check named no should-fix items, so none were applied.

**The fix.** The short line and the question now stand in a row of their own across the full
width, above the two columns (`hl-head` in `Rebuilt.astro`). Both columns start below the
question. Measured in the browser from the top of each figure's drawn shape, the 5 starts
14 pixels above the 1% at 1280 pixels wide and 17 pixels above it at 920. On a phone nothing
moves, because the columns already stack there. Only the markup and the styles changed; no words
did.

**Type and spacing for the wider row.** The question's width limit went from 640 to 860 pixels,
so on a computer it takes three lines instead of five. Its lines are also evened out
(`text-wrap: balance`) so that "things?" does not sit alone on a last line at 920 pixels wide.
*Strongest alternative:* keep the 640 limit, which gives five short lines and leaves the right
half of the row empty above the readings. The right-hand column's top padding went from 34 to 8
pixels, because it no longer has to line up with the short line; that keeps the 1% just below
the top of the 5 rather than well below it. *Strongest alternative:* no padding, which would put
the 1% slightly above the drawn top of the 5.

**A guard in the site check.** The site check reads the built page as text and cannot measure
where a browser draws things, so it cannot test the pixel positions directly. It now refuses the
page structure that allowed the fault. Under rule 7d it requires exactly one `h1`, the question,
and requires it to come before the element that holds the two columns (`class="rb-first"`),
before every reading and before the count. Nothing that was checked before was loosened. Fed the
built page with the question moved back into the left column, the check answered "the question
stands inside the two columns, so on a computer a reading can stand beside it, above the count";
fed it with the question after the count, it also answered "the count stands above the
question". The check's sample home page in `scripts/test_compute.py` was brought up to the ruled
order (it had no question in it), and three tests were added for the new refusals.
*Limit:* a style rule that moved the question back beside the readings without changing the
markup would not be caught. Catching that would need a browser in the build, which the site
check does not run.

## Spacing and type-size choices (first pass)

All in `site/src/styles/rebuild.css`; each is the session's call, not John's.

- **The question is set larger:** from 22 to 29 pixels (the size it had as a line under the
  breakdown) to 28 to 40 pixels, scaling with the screen, with slightly tighter line spacing.
  *Reason:* it is now the headline, so it should read as the page's title, while staying well
  below the count's 72 to 136 pixels, so the count is still the largest type on the site.
  *Strongest alternative:* keep the old size, which keeps the number visually dominant but makes
  the headline look like a caption under the short line.
- **The thin rule that stood above the question now stands above the paragraph "This record
  holds ...".** *Reason:* a rule directly under the short line would cut the headline off from
  what says what the site is; moved down, it still closes the number block off from the prose
  beneath, as before. *Strongest alternative:* a rule between the question and the count, which
  separates them more clearly but reads as if the count began a new section.
- **18 pixels of space under the question,** before the count. *Reason:* enough to separate
  the serif headline from the tall figure without making the count look like it belongs to
  something else. *Strongest alternative:* a larger gap (about 28 pixels), which sets the
  count apart more but pushes it further down a phone screen.

On a phone 375 pixels wide the first screen now shows the short line, the question, the 5, its
sentence, "Among them", and the breakdown, in that order.

## Pictures

In `docs/proposals/pictures/2026-11-21-question-first/`, light theme, the top of the home page:

- `before-phone-375.jpg` and `before-computer-1280.jpg`: the page as it is on `main`.
- `first-draft-phone-375.jpg` and `first-draft-computer-1280.jpg`: the first commit, with the
  question inside the left column. The computer picture shows the fault the check found.
- `after-phone-375.jpg`, `after-computer-920.jpg` and `after-computer-1280.jpg`: the page as it
  is now.

The phone pictures are a frame 375 pixels wide and 812 tall. The computer pictures are windows
920 and 1280 pixels wide. All are taken at twice the pixel density. No "before" picture was taken
at 920 pixels wide.

## Checks

On the second pass:

- The site build ran `scripts/check_site.py`: "The built site passes: 19 pages, 124 outside
  addresses linked." That includes rule 7d with its new part on the question.
- `scripts/test_compute.py`: 85 tests, all passed (82 before, plus the three new ones).
- The build rewrote `site/src/data/window.json`; that change was put back and is not committed.
