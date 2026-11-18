# Changelog

Every change to the records, the method or the site gets a dated line here, saying which
number moved or that none did. Nothing is published, so there have been no public corrections.

## 2026-11-18

- **Four of the five small fixes from the check of the record fixes are applied**
  (`docs/reviews/2026-11-18-check-of-record-fixes.md`). The retirement-interview caution uses its
  page's word "misaligned" and quotes "in ways that models are less likely to find concerning".
  Each record now carries a `[checks]` table saying when it was checked against its sources,
  when it was changed, and when those changes were checked, and the entry page builds its
  sentence from that table, because the fixed sentence in the page template was untrue for the
  survey of AI researchers (nothing to correct) and would have been untrue for any later record;
  `scripts/compute.py` refuses a table with missing or out-of-order dates. About no longer says
  the corrections are unchecked. Three dated notes are added in the research draft. The finding
  on who made the second check is left for John, with open question 7. No number moved: 6 of 9
  things on the list are still offered to at least one AI model today.
- **The remaining fixes from the two second checks are applied** to eight records and to the
  site's text: the welfare-assessment record now files the 2026 trade-off answers as statements,
  not choices made at a cost; two cautions now say what their pages say; the retired-model
  record says the other developer announced a withdrawal, not that it made one; the Microsoft AI
  arguments are filed as the cost of seeing more than is there; and the entry pages say a second
  check was made. No number moved: 6 of 9 things on the list are still offered to at least one
  AI model today. Notes are in `docs/research/2026-11-17-first-entries.md`.

## 2026-11-17

- **First version of the site built, on this Mac only.** Nothing is published, pushed or
  deployed. Pages: home, the list, one page for each of thirteen entries, About, Still Asking,
  and a page for an address that does not exist.
- **Thirteen records added**, all a first pass, turned from the drafts in
  `docs/research/2026-11-17-first-entries.md` with no fact changed. Nine are things on the
  list and four sit beside it and are not counted. Two drafts were left out
  (`docs/first-version-choices.md`, part 3).
- **The number is worked out for the first time: 6 of 9** things on the list are offered to at
  least one AI model today. It is in `data/headline.json`, written by `scripts/compute.py`.
  The list holds only things a dated source could be found for, so the number reads high and
  the home page says so.
- **Scripts added:** `scripts/compute.py` (checks the records, works out the number),
  `scripts/export.py` (the only reader of the data for the site), `scripts/check_site.py`
  (refuses a built page that breaks a rule of public text), `scripts/test_compute.py`
  (20 tests) and `scripts/pictures.sh`.
- **Every design point the build needed is a provisional choice by a session**, not a ruling,
  and is listed in `docs/first-version-choices.md`.
- No licence files were added (choice 15 in that document).
