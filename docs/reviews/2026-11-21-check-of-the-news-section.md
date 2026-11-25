# Check of the news section and its proposal

Written 2026-11-21 by Claude (Opus 5.5) in a Claude Code session that did not write the work.
What was checked: commit `4b45b72` on branch `claude/news-section-79b5f4` (the news section,
copied from Outrunning Ageing, with no real post), and its proposal,
`docs/proposals/2026-11-21-news-section.md` on that branch, with its nine pictures. The branch
starts from `main` as it stood at `6de3687` (the founding question ruling) and `main` has not
moved since.

**How it was checked.** The commit was unpacked into a scratch folder with `git archive`; neither
the main checkout nor the writing session's worktree was touched. Read first: the two instruction
files, `docs/inheritance.md` (rows L1 to L14 and K1 to K14), and the family's news rules in the
tracker pattern (`sentient-horizons/design/tracker-pattern.md`, master, rules 4.10 to 4.23).
Each sibling was read from its `origin/main` of 2026-11-21 (several local `main` branches were
behind). Outrunning Ageing's news files were compared with the build line by line; the other
three sites built with the same generator were compared with Outrunning Ageing's by size of
difference and, for two files, line by line. Then the site was built clean, the news tests and
the record tests run, the guards tried with made-up posts, the nine pictures looked at, and my own
pictures taken at phone width in the dark theme and at computer width in the light theme.

## Must fix

**M1. The proposal leaves out the opening post, and two choices rest on a wrong account of how
the siblings started.** Rule 4.13 says each news section "opens with one longer post", and every
sibling did: all four sites built with the same generator have a `2026-10-18-start-here.md`, and
`sentient-horizons/ops/tracker-news/opening-posts/README.md` records the five openers drafted and
placed on 2026-10-18, the day the sections were built. No sibling ever went live with an empty
News page. So:
- Choice 7 says the strongest alternative is to add News to the bar "as the siblings did on their
  first day", at the cost of "a link on every page to 'No post yet'". The siblings' first day had
  an opening post, so that cost belongs to neither of the options as they really stand.
- Choice 9 (may the empty page go live) gives "hold the merge until the opening post is written"
  as the alternative, but not the family's own practice, which is to open the section and its
  opening post together.
- There is no choice about the opening post itself: who writes it, when, and the three things
  that make it harder here than on the siblings: whose voice it is in (choice 4), whether it may
  name the developers and models (choice 5), and the reading against John's published positions
  that every new page now needs.

Fix: add the opening post as a choice, and restate choices 7 and 9 with the family's practice as
one of their options. Choices 7, 8 and 9 and the opening post are really one decision (when and
how the section goes live) and read better put to John together.

**M2. Choice 12 does not carry the four things, and it states the family's rule on unchecked
facts more narrowly than the family does.** Choice 12 gives no confidence, does not say what is
standard and what is judgment, and gives no alternative. Inside it, the rule is given as "no post
goes out while a fact in it is on `docs/verify-list.md`". The family's rule (rule 4.11, and rule
3.3 part 4 it points to) is wider: "no post is published while any record on the site carries an
open verify entry", and this site's inventory takes it over as is (row L4). This site already
keeps every record with something left to verify off the site entirely (`scripts/compute.py`,
which shows only records with nothing to verify), and the news check refuses a post that names an
entry the site does not show. That changes what the family rule would mean here: read strictly,
no post could go out while any record still waits off the site; read as the Zeitgeist enforces
it, the rule is already half kept in code. Which reading holds is John's to rule, and the choice
should set out both, with the four things.

**M3. The news check counts the day an entry was checked as the day it changed.** This is the one
guard the build weakens. On Outrunning Ageing, a post may name a record only if that record shows
a real change within fourteen days of the post: a revision, a stage reached, or a reading item
resolved or moved. The copy here (`scripts/check_news.py`, `entry_dates`) takes every date in an
entry's record of checks as a change. That record holds changes (`changed`, `added_to`,
`corrected`, `fixed`) and also the days a session checked them (`against_sources`,
`changes_checked`, `additions_checked`, `corrections_checked`, `fixes_checked`). Counting the
second kind means a post could announce a change the record does not show, as long as someone
re-read the entry within the fortnight, which is what the guard exists to prevent. Fix: count only
the keys that record a change, and add a test with an entry that was only checked.

## Should fix

**S1. The back links from an entry to the posts about it are standard, and should be built or put
to John as a choice, not left as a side note.** Rule 4.14 says a post's back links "are computed,
never written into a record", and every sibling built with the same generator shows an "In the
news" line on a record's page and links the post from its dated story of changes. The proposal
mentions this only as "a side effect to know" under choice 3, and leaves the line unbuilt so as
not to touch the entry pages. The helper for it (`postsAbout`) is copied. Here the dated list of
acts (`/acts/` and its feed, `site/src/pages/acts.xml.ts`) is the nearest thing to the siblings'
story of changes, so the family's practice would be an "In the news" line on an entry's page and a
link from an act to the post that explains it. Either build both, or make them a choice of their
own with the four things.

**S2. Mark which choices need no ruling, and change the order.** Five choices are already settled
by family practice or by this project's own rules, and can be told to John as done rather than
asked: choice 1 (copy Outrunning Ageing), choice 6 (a picture per post, rule 4.15; only the timing
of the drawing script is open), choice 10 (the "Follow the news" line, as all siblings have it),
choice 11 (made-up posts, which follows the project's own rule on the word "constructed"), and the
part of choice 3 that keeps news and the list of acts apart (rule 4.15's one news feed, and the
family's habit of keeping what was said and what was done in separate records). The ones that
need John, in the order I would put them, one at a time:
1. When and how the section goes live: the opening post, News in the bar, the home page panel,
   and whether the empty page may go live first (M1; choices 7, 8 and 9).
2. Whether a post may name the developers and models it is about (choice 5), because the opening
   post can hardly be written without it.
3. Whose voice a post is in (choice 4), for the same reason; it touches open question 7.
4. The kinds of post (choice 2).
5. The back links (S1).
6. The reading of the rule on unchecked facts (M2).
Choice 3's two feeds can go with the first, since the bar and the footer are where a reader meets
them.

**S3. Two sentences on the News page need rewording for a stranger.** The page's lede says a post
is written when "the count" moves. Someone who lands on `/news/` from a feed or a shared link has
not met the home page's count, so the phrase is an inside term used before it is explained (the
workspace's "a stranger could say it back" rule). The same lede says each post "names the entries
it is about", which is not true of the opening post or of a story, neither of which need name an
entry. Both are changes of wording, so they need no public note.

**S4. Guideline 4 (conditional language) has no guard in code, and news posts are where it will
first be tested.** The check of the built site refuses a phrase that writes the site as its own
agent (rule 3 there), but nothing refuses "the model wants", "it feels", or "it does not really
want". Entry pages have been written slowly and checked; posts will be written the day something
happens. The family's rule is that guards live in code once there is code. This is not a fault of
this build, which publishes no post, but it belongs on the list for before the first post, beside
the drawing script of choice 6.

## Notes

**N1. The copy is faithful.** Every news file in the build was compared line by line with
Outrunning Ageing's `origin/main`. The differences are the ones the comments and the proposal
state: this site's own kinds; the record line linking entry pages (this site has no weekly reading
and no story entry to link); `constructed` in place of Outrunning Ageing's `stand_in`; a preview
picture used only if one has been drawn; the folder setting for made-up posts; the News page's foot
pointing at "Everything, by date" in place of "the story so far"; the "what it does not mean"
phrase dropped from the descriptions (which fits John's amendment of 2026-11-09 to rule 4.19); and
a stylesheet class renamed so as not to clash with this site's own. I found no difference that is
not stated. The Quiet Galaxy and The Upgrade Tree say in their own files that they were "copied
from Outrunning Ageing's, the model", which bears out choice 1's reason. Nothing the family treats
as standard was lost by choosing Outrunning Ageing, apart from what S1 and M1 name.

**N2. Build, tests and guards.** A clean build of the commit passes: 20 pages, the check of the
built site passes, the news feed is built with no items, and the sitemap lists `/news/`. The 16
news tests and the record tests pass. No line of any existing check was removed or weakened (the
only removed lines are in `Base.astro` and the sitemap, replaced by their wider forms). Built with
the three made-up posts, the check of the built site refuses the build for exactly those three
pages. A made-up post copied into the folder the site publishes from is refused by the news check.
A post placed in a subfolder of that folder escapes the news check (it reads only the top level,
as the siblings' does), but the build then fails outright, so it cannot be published either.

**N3. Small things about the guard on made-up posts.** The news check reads `constructed: True`
(capital T) as words, not as yes, so it would let such a post through; the site generator reads it
as yes, the page shows the notice, and the check of the built site then refuses it. The guard
holds, by the second line rather than the first. The README's warning about the generator's cache
is right, and the publishing workflow starts clean.

**N4. Public text.** The only public text the build publishes is the News page with no post: its
title, lede, empty-page line, the foot pointing at "Everything, by date" and the "Follow the news"
line. It names no AI model or tool, uses none of the project's working words, says nothing a
machine wants or feels or does not, and is impersonal. The made-up posts also pass all of these,
apart from their being made up.

**N5. Inherited from the family, not this build's doing.** The News list shows dates as
`2026-11-21` while the post's eyebrow and the side list write them out; every sibling does the
same, against the family's rule that public dates are written out. The opening-post box prints
"about 0 words" for a very short opener (it rounds to hundreds), visible in picture 1; a real
opener of 800 words or more is unaffected. The generator warns "the collection news does not
exist or is empty" while there is no post. The footer's "Feed" link means the feed of acts, and
with two feeds it may want a clearer name when News joins the footer (choice 7).

**N6. The pictures.** The nine pictures match what the code builds. Mine agree: at 375 pixels in
the dark theme the post page has no sideways scroll and "Recent news" moves under the post; at
1280 pixels in the light theme the News page matches picture 3.

## John's published positions

Read against the positions record (`sentient-horizons/editorial/corpus-positions-ledger.md`,
master). This reports and settles nothing.

- Nothing on the pages the build publishes conflicts with any position. They say almost nothing.
- **The story kind and the method claim that a post carries nothing the record does not.** Part
  D's second claim (the record is built so the story can be told) carries the guard that a news
  post "never carries a fact the record does not carry", and rule 4.10 says the same. A story post
  is, by definition, one that may tell news the record does not hold. Outrunning Ageing has the
  kind, and this site's inventory takes it over (row L6), but the tension is real and stronger
  here, because the field's news will often be what a developer or a model said.
- **A story about what a model said.** Position 21 (a model's bare report of itself is screened
  off; a report that matches an independent reading of the system carries real information) and
  this site's guideline 2 as revised on 2026-11-20 both bear on any post that reports a model's
  words. The proposal raises this under choice 2; the post format has no field to mark which kind
  of report a post carries.
- **The two kinds of error.** Position 1 holds that over-attribution and dismissal are twin
  failures. The kinds of post are neutral between them, and nothing in the build leans either way.

## Verdict

**The proposal is not yet fit to put to John.** It needs the opening post added and choices 7 and
9 restated against what the siblings actually did (M1), choice 12 given its four things and the
family's rule on unchecked facts stated in full (M2), and the back links made a choice (S1). With
those, and the order in S2, it is a good proposal: eleven of the twelve choices already carry the
four things, and the account of the siblings is otherwise accurate.

**The build is fit to merge once John has ruled, after M3 is fixed.** M3 is a few lines and a
test. Everything else in the build is a faithful copy, the guards against a made-up post hold, and
no existing check was loosened.

## Second check, 2026-11-21: the writer's answer in commit `d34d806`

Written 2026-11-21 by the same session (Claude, Opus 5.5), which did not write the work. Only what
`d34d806` changed was checked: the news check and its tests, the News page's opening paragraph,
two comments, the two redrawn pictures, and the proposal, now six questions for John.

**The fix to the news check (M3) is sound and loosens nothing.** The check now counts only four
keys of an entry's record of checks as changes: `changed`, `added_to`, `corrected` and `fixed`.
These are exactly the change fields `scripts/compute.py` defines, and the other five are the
days a session checked those changes. Across the 13 entries, every key in use is one of those
nine, plus `some_unchecked`, which is not a date. Because the list names what counts rather than
what doesn't, a change field added to the record later would be left out, and the check would
grow stricter, not looser. The new test proves both directions: a post near a mere check is
refused, and a post near the real change passes. The reader now takes `constructed: True` as
yes, which closes note N3 at the first line of defence. All 18 news tests pass, and a clean build
passes the check of the built site (20 pages). One aside on note N2: a build of mine failed until
I also cleared `site/node_modules/.astro`, because the generator had cached my subfolder test.
The README in `scripts/fixtures/news/` already names both caches.

### Must fix

**M4. Question 6 gives the Zeitgeist's practice the wrong way round, and recommends against it.**
The proposal calls reading two (the rule covers only the records the site shows) "the
Zeitgeist's". The Zeitgeist's check does the opposite. It reads every file in `data/claims/`,
and its own words are "the count across the site must be none" and "The rule is kept strict".
The strict form was added on John's ruling of 2026-11-09, after posts went out on 2026-10-19 and
2026-10-21 while ten checks were open (agi-zeitgeist, `scripts/check_news.py`, lines 21 to 27;
this site's inventory, part 2, lesson 9). So the Zeitgeist is the family's precedent for reading
one, set by John. The question should say so. It should also say that reading one costs nothing
today: the headline file counts no record left out with facts to verify. Reading one can be kept
in code at once, by refusing a post while that count is above none, which suits "guards live in
code". Reading two leaves the post's own facts to be checked by hand. The recommendation may
still be reading two, but only if it sets out why this site should differ from a ruling of
John's. Since the question is the session's to put, the safer recommendation is reading one.
Under either reading, the question should also say whether an entry flagged `some_unchecked`
(three entries today: changes made after a check that the check did not cover) counts as a fact
waiting to be checked.

### Should fix

**S5. The reworded opening paragraph of the News page does not use the home page's words for the
count.** It now reads "the number of things past an AI model's ordinary limits that a developer
offers today". The home page counts things "a developer can do in how it treats the AI models it
builds", which are "done, or publicly committed to, by at least one developer today". The new
phrase coins a description ("past an AI model's ordinary limits"), and "offers" is narrower than
"done, or publicly committed to". A reader who follows the link home would not recognise the same
number. Use the home page's own words. This is a change of wording only.

### The six questions

- **The four things.** All six carry them: what is proposed, confidence with a reason, standard
  or judgment, and the strongest alternative with its cost. Question 1 and question 5 split
  their confidence and their standard-or-judgment by part, which is the right way to do it.
- **The order** follows the check's suggestion and works when the questions are put one at a
  time. Question 1 says that the opening post waits on questions 2 and 3, so John knows the answer
  to 1 is not the end of it. One alternative order is defensible: 2 and 3 first, since the opening
  post cannot be drafted without them. Either works.
- **Question 1 now states the siblings' practice correctly** (M1 is fixed), and it adds a
  proposal of its own: to rename the footer's "Feed" as "Feed of acts". It is fine for that to sit
  inside question 1, since John sees it there.
- **What was dropped from the twelve, and whether it should have stayed.** Old choices 1, 6, 10
  and 11 and the first part of 3 are now told as settled, which is right. Old choice 8's
  alternative (a block below the first screen) is settled by John's family-wide ruling of
  2026-11-14 for the right-hand panel, so it was right to drop it. Old choice 12 is now split
  between part 2, F and question 6, which fixes M2 except for M4 above. One small thing was lost.
  The first version noted, under old choice 10, that rule 4.15 asks for a "Follow on X" link in
  every tracker's footer, and that no sibling has one. Part 2, D now says only "as every sibling
  has it". That is true of the line on the news pages, but the gap from the written rule should
  stay as one sentence, so John is not told the footer is settled when the rule and the practice
  differ.

### Verdict after the second check

**The proposal is fit to put to John once M4 is fixed.** That means restating question 6 with the
Zeitgeist as the precedent for the strict reading, ideally recommending that reading, and saying
whether `some_unchecked` counts. The missing sentence on the footer link to X should go back in
at the same time. **The build is fit to merge once John has ruled**, after the one-sentence rewording
in S5. The fix to the news check is sound and loosens nothing.

## Third check, 2026-11-21: commit `c1e8801`

Both points are fixed. **M4:** question 6 now cites the AGI Zeitgeist, by John's ruling of
2026-11-09, as the precedent for the strict reading. It recommends that reading, kept in code,
and gives the loose reading as the alternative, with its cost. It answers the question about
`some_unchecked`: three entries carry it today (protection in law, the public belief survey,
memory across conversations), and the proposal blocks only a post that names one of them. That
treatment is marked as a judgment. All four things are present. **S5:** the News page now
describes the count in the home page's own words, and a clean build passes the check of the built
site (20 pages). The footer sentence on "Follow on X" is back in part 2, D. Nothing else changed
in the code.

**Final verdict.** The proposal is fit to put to John, as six questions in the order given. The
build is fit to merge once he has ruled. The fix to the news check loosens nothing, and the
guards against a made-up post hold.
