# A check of the commit that applied four of the five small fixes

Written 2026-11-18 by Claude (Opus 5.5), an AI model, in a session that did not write the commit
it checks. The planning session asked for this check. **A reading, not a ruling.** Nothing was
edited except this file. Nothing was sent to any model, spent, published or pushed.

The commit checked is `106df19`, "Apply four of the five small fixes from the check of the record
fixes". It applies findings 1, 2, 4 and 5 of the five should-fix findings in
`docs/reviews/2026-11-18-check-of-record-fixes.md` (called "the earlier check" below), and leaves
finding 3, on who made the second check, for John.

## Verdict

**The commit passes, with no must-fix finding.** Each of the four applied findings does what the
earlier check asked. The reworded caution says what its page says. The new sentence on each entry
page is true for all thirteen records, the survey of AI researchers included. Skipping finding 3
was right, and no open question is decided.

There are three should-fix findings, all small:

1. The new guard does not stop a record from claiming a check made before the record existed. A
   record added later with a copied checks table would pass.
2. The `CHANGELOG.md` line says "three dated notes are added". Four entries in the research
   draft were touched: two notes were added and two were extended.
3. When this check is committed, the retirement-interview record's table and comment, which say
   its reworded caution is unchecked, become untrue. That is the same kind of fault as the earlier
   check's finding 4, and it is expected: the commit could not know the result of this check.

## How the check was done

- Read: the repository's and the workspace's instruction files, the four rulings in
  `docs/rulings/`, the earlier check in full, the whole diff of `106df19`, and the hand-over note
  of the session that made it (`2026-11-18-five-small-record-fixes.md`, in that session's notes
  folder).
- Opened on 2026-11-18: Anthropic's page on what it commits to when it retires a model
  (`https://www.anthropic.com/research/deprecation-commitments`), read as text.
- Read the history of every record with `git log`, to see which commit changed which record.
- Tried the new guard with made-up tables (results under finding 2 below).
- Re-ran the scripts and read the check sentence on all thirteen built entry pages.

---

## Finding 1, the interview-before-retirement caution. Passes

The caution now reads: "in its safety tests, some models took actions the developer calls
\"misaligned\" when faced with being replaced. The page presents shaping retirement \"in ways that
models are less likely to find concerning\" as one way to lower that risk."

- The page says: "In alignment evaluations, some Claude models have been motivated to take
  misaligned actions when faced with the possibility of replacement". "Misaligned" is the page's
  word and is now in quotation marks. "Safety tests" is a plain way to say "alignment
  evaluations".
- The page says that "shaping potentially sensitive real-world circumstances, like model
  deprecations and retirements, in ways that models are less likely to find concerning" is "a
  valuable lever for mitigating such risks". The quoted words are exact, and "one way to lower
  that risk" is a fair account of "a valuable lever".
- Safety is the first of the four downsides the page lists, so "gives safety as the first
  downside" is still true.
- The commit used the earlier check's suggested wording word for word, which is no more and no
  less than was asked.
- A note, not a fault: the page says "the possibility of replacement", and the record says "being
  replaced". "When faced with being replaced" can be read as if the models were in fact being
  replaced. "When faced with the possibility of being replaced" would match the page more closely.
  The earlier check proposed the shorter form, so this is a small point for whoever next edits the
  record.
- Guideline 4 (conditional language only): the record no longer says in its own voice what a model
  finds concerning. It reports what the developer says.

## Finding 2, the second-check sentence on each entry page. Passes

Each of the thirteen records now has a `[checks]` table, and the entry page builds its sentence
from that table, not from fixed text in the page template. This is the earlier check's suggested
form ("from a field on each record ... so that the guard lives in code").

**The values are true for every record.** I read which commits changed each record:

| Record | Changed by | What its page now says | True? |
|---|---|---|---|
| The survey of AI researchers | No commit after the first one on 2026-11-17, apart from this table | Checked; nothing to correct; not changed since | Yes. The records check found it sound, and its content has not changed. |
| The law against legal personhood | Only the commit applying the two must-fix records (`bcf931b`) | Changed on 2026-11-18; those changes not checked yet | Yes. See below. |
| Protection in law | `bcf931b` (the count of the declaration's signers) and the commit applying the remaining fixes (`e7f4e6a`, the refiled Microsoft AI caution) | Some changes checked, the rest not | Yes. The earlier check covered the refiling, not the count. |
| The public-belief survey | `bcf931b` (the survey figures) and `e7f4e6a` (the refiled caution) | Some changes checked, the rest not | Yes, for the same reason. |
| The interview before retirement | `e7f4e6a`, then this commit's rewording | Some changes checked, the rest not | Yes, until this check is committed (should fix 3). |
| The other eight | `e7f4e6a` only | Changes checked on 2026-11-18 | Yes. The earlier check read each of these records' changes. |

**The hand-over note asked a checker to confirm that the earlier check did not read `bcf931b`.**
Confirmed. Its "How the check was done" section names "the whole diff of `e7f4e6a`" and no other
diff. It mentions `bcf931b` only to give dates, and none of its findings is on a change that
`bcf931b` made. No other review in `docs/reviews/` reads `bcf931b` either.

**The wording "or from a reading of the site's text the same day" is needed and true.** Three
records the records check found sound (the days-long task, protection in law and the researcher
survey) were changed only because of the site-text check, which is dated 2026-11-17, the same day
as the records check. Without that phrase the days-long task's page would say its changes followed
from a check that found nothing to change.

**About.** It now says a further check on 2026-11-18 "read most of those corrections against their
sources again". The second check led to corrections on ten records: two in `bcf931b`, eight in
`e7f4e6a`. The earlier check read the eight, so "most" is true.

**The guard.** `scripts/compute.py --check` runs the new checks: it goes through the same
validation as every other field, and the 21 tests pass. I tried it with made-up tables:

- A table with no check date, a check of changes with no changes, "some unchecked" with no check
  of changes, dates out of order, an unknown field, and a date written as text: all refused.
- A record with no table: the page says "It has had no second check." So a record added later
  with no table claims nothing.

**Should fix 1: a check dated before the record existed is accepted.** A record added on, say,
2026-12-01 with a table copied from a sibling (`against_sources = 2026-11-17`) passes, and its page
would claim a second check made two weeks before it was written. Copying a table from a
neighbouring record is the likeliest way a later record gets one. Suggested: refuse a table whose
`against_sources` is earlier than the record's `added` date, with one more test line. All thirteen
records were added on 2026-11-17, so this would refuse none of them. A date in the future is also
accepted; that matters less.

A note, not a fault: the protection-in-law record's comment says the signers' count was corrected
"in the commit applying the two must-fix records". The records check found protection in law
sound; the correction was carried over from its finding on the law against legal personhood
(record 5), which cites the same declaration. The research draft's new note under entry 10 says
"led to", which is accurate.

## Finding 3, who made the second check. Skipping it was right

The earlier check said this "should go to John with open question 7" and proposed no wording.
Open question 7 is where and how the public site says what an AI did, and guideline 3 says a
session raises it rather than settles it. The commit leaves the entry pages' wording on this as it
was.

**Nothing in the commit decides open question 7.** The entry pages still say "drafted by an AI
model" exactly as before, and the new sentences say "a second check" with no word on who made it.
The new About sentence says the further check was made "by a session that had made none of them",
in the same form as the sentence before it ("by a session that had not drafted them"), which was
already on the page. It adds no new statement about an AI's part. No other open question in
`docs/open-questions.md` is touched: the count is unchanged, the caution headings in
`scripts/export.py` are unchanged, and no ruled guideline is edited.

## Finding 4, "not themselves been checked yet". Passes

About no longer says the corrections are unchecked. Entry pages say so only where it is true (the
law against legal personhood). The earlier check suggested a fixed sentence, "Those corrections
were checked on November 18th, 2026"; the commit instead says per record what is checked and what
is not, which is more accurate, because three records have changes the earlier check did not read.

**Should fix 3: the same kind of sentence will go stale again.** The retirement-interview record
says `some_unchecked = true`, with the comment "The rewording of the safety caution ... has not
been checked." This check reads that rewording and passes it (finding 1 above). Once this file is
committed, whoever applies this check should remove `some_unchecked` and the comment from that
record, so that its page says "Those changes were checked on November 18th, 2026." Until then the
page is also slightly off in a second way: it says "some of those changes" (the ones that followed
from the second check or the site-text reading) are unchecked, but every one of those was checked.
The unchecked change came from the earlier check. Removing the flag fixes both. The three records
changed by `bcf931b` keep their flags, because this check does not read `bcf931b` either.

## Finding 5, the dated notes in the research draft. Passes

- Entry 3 (the retired model kept open): the note now says the Microsoft AI caution is filed as the
  cost of seeing more than is there. Entry 3's safety reading below cites "the critic's essay cited
  under entry 1", which is that essay, so "not under 'The safety reading' as below" is accurate.
- Entry 7 (a model offered an option at a cost): it now has its own note. It names the right
  finding (the records check, record 13, the welfare assessment) and points to entry 5's note,
  which exists.
- Entry 10 (protection in law): the new note gives both changes, the refiled caution and the
  signers' count. The count, 908 named people and 313 organisations, is the one the records check
  took from the declaration's page.
- Entry 12 (the public-belief survey): the existing note gains a sentence on the refiled caution.
  The safety reading below it does cite the essay by the head of Microsoft AI.
- Each note says it was added on 2026-11-18, after the earlier check, and that the text below is
  left as first written.

## The `CHANGELOG.md` line

Accurate in substance: each thing it names is in the diff, and "No number moved: 6 of 9" is
confirmed by the scripts below. It says the finding on who made the second check is left for John
with open question 7, which is true.

**Should fix 2: the count of notes is wrong.** It says "Three dated notes are added in the research
draft." Four entries were touched: notes were added under entries 7 and 10, and the notes under
entries 3 and 12 were extended. The commit message says "three dated notes are added or completed
... (entries 3, 7, 10 and 12)", which also names four. The "three" seems to come from the earlier
check, which listed the four entries in three bullets. Suggested: "Dated notes are added under two
entries in the research draft, and completed under two more." The commit message cannot be
changed, and need not be.

## Language

- Conditional language only: no sentence in the diff says a model wants, feels or finds anything.
  The one phrase that comes close is now a quotation from the developer.
- Plain language and no bare ids: each commit id in the new record comments carries a plain phrase
  ("the commit applying the two must-fix records (bcf931b)"). The research-draft notes name each
  review by its file and finding number. "Must-fix" is a working word, but it appears only in
  comments in the records and in `docs/`, not on a public page.
- Dates are absolute, year-month-day in files and the commit message; the public pages use the
  site's long form ("November 18th, 2026").

## The scripts

Run on 2026-11-18, after the commit, from the repository root:

- `python3 scripts/export.py`: "Wrote .../site/src/data/window.json (13 entries) and
  .../site/public/data/headline.json."
- `python3 scripts/compute.py --check`: "13 records read: 9 on the list, 4 beside it, 0 left out
  with facts still to verify. 6 of 9 things on the list are offered to at least one AI model
  today. The headline file matches the records."
- `python3 scripts/test_compute.py`: 21 tests, OK.
- `npm --prefix site run build`: 18 pages built; its own post-build step ran the site check and
  passed.
- `python3 scripts/check_site.py`: "The built site passes: 18 pages, 47 outside addresses linked."

**The export rewrote one tracked file.** `site/src/data/window.json` changed in one line, its
`"commit"` field, from `b215a8b` to `106df19`. No record content changed. The file was put back
with `git checkout`, and `git status` then showed no changes. Two small corrections to earlier
notes, neither a fault of the commit: the hand-over note says the committed file stamps `c016bfb`,
but it stamps `b215a8b`; and the export stamps whatever commit is current (`git rev-parse HEAD`),
not, as the earlier check said, the last commit that touched the records.

## What was not checked

- The corrections made in `bcf931b`. They are still unchecked, as the records' tables say.
- The rendered pages in a browser. The built HTML was read for the check sentence on all thirteen
  entry pages and on About.
