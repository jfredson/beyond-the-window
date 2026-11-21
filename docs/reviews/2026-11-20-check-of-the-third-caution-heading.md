# Check of the reworded heading for the third caution

Written 2026-11-20 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session did not write the two commits checked (`3a56833` and `1252e50`,
by the site-fixes session). A push of them publishes to the live site, so this is the check
before publishing, and it includes the read against John's published positions that he ruled
for every changed page.

I changed nothing and pushed nothing.

## Verdict

**Fit to publish.** The new heading is on all thirteen entry pages word for word. The two
sentences on the home page and the About page are the ruled ones, with nothing else in their
paragraphs changed. The old wording of the third caution is nowhere in the built site. No
caution moved and no count moved. The new wording answers the contradiction the earlier read
found, and it takes no side.

**One thing for John to know, which follows from the ruling and is not a fault in the
commits: the third heading now overlaps the first.**

- *Before,* the three headings could not overlap. The first was about a system with no wants,
  and the third was about a system with wants.
- *Now* the third covers a system with or without wants. So a caution that says "treating a
  model as if it had wants makes AI harder to control" fits the first heading, where it
  stands, and also fits the third, because loss of control is a risk to people.
- *How many:* six cautions under the first heading say that, all from the two essays by the
  head of Microsoft AI. They are listed in part 3.
- *Why it matters beyond tidiness:* the About page says "Of the 18 items recorded under the
  first caution, 9 come from two essays by the head of Microsoft AI", and the build stops if
  that share falls below half. Moving any of those six would move both figures.
- *What I suggest:* nothing moves. They were filed under the first heading because the cost
  they name comes from the treating, and that is still the better home. It would help to have
  that said once in the working documents, so that a later session does not refile them one
  at a time.

## 1. The built site

I built the site in scratch copies at the commit before the first of the two and at the
second, and compared every built file.

- **The heading.** Each of the 13 entry pages carries "If an AI system puts people at risk,
  whether or not it has wants" exactly once, and the old heading not at all.
- **The home page,** under "Why keep this record". As built: "If AI models have no wants,
  treating them as if they had has a cost. If they have wants and nobody notices, that has a
  cost. If they put people at risk, whether or not they have wants, that has a cost too. All
  three are kept in view here, and none is argued for." Only the third sentence differs from
  before, and it is the ruled one.
- **The About page.** As built: "if an AI system has no wants, and is treated as if it had; if
  it has wants, and they go unnoticed; if it puts people at risk, whether or not it has
  wants." Only the last clause differs, and it is the ruled one.
- **The old wording is gone everywhere.** I searched every built text file, the feed and the
  page of acts among them, for the old heading and for both old sentences, and found none.
  The headings were never part of any share or preview text.

## 2. Does any other sentence disagree with the new heading, or lean on the old one?

I listed every sentence on the 19 built pages that speaks of wants, of risk to people, or of
the three cautions.

- **"That is a larger matter than the wants the three headings speak of"** (About,
  `site/src/pages/about.astro`, line 234). Still true: all three headings still speak of
  wants, the third now to say that risk does not depend on them. John was shown it and left
  it.
- **"Each is headed by an 'if', and none of the three says that the 'if' is so"** (About).
  Still true. The third heading's "if" is now about putting people at risk.
- **"None of them settles whether an AI model wants anything, in either direction"** (every
  entry page). Unaffected.
- **In the records' own prose** no caution, description or note says "if it has wants" or
  leans on the old heading.

So I found no other sentence on a page to list.

**In the working documents,** which are not pages, the old description of the third caution
still stands in these places: `docs/method.md`, line 92; `docs/record-schema.md`, lines 55 and
202 to 203; and `docs/first-version-choices.md`, line 368. Guideline 5 in `CLAUDE.md` already
carries a dated note. The kickoff copy and the research notes are records of their day and
are not counted.

## 3. Does every caution sit under the right heading?

Listed as candidates only. Nothing moves without John.

**Under the third heading now: 13 cautions, and all can stay.** Nine fit plainly, and fit
better than under the old wording: the study of models interfering with a shutdown mechanism
and the paper on why almost any goal gives reason to keep running (the entry on days-long
tasks); the developer's tests in which models took "misaligned" actions when faced with being
replaced (two entries); the safety reason given for keeping a retired model open; the safety
testing of memory; the warning that a model might learn to hide its reasoning; the test in
which blackmail became more likely; and the argument that a model secure in its sense of
itself behaves more predictably.

Four fit loosely, as they did before. None is made worse by the change.

| Entry | Caution | Why it fits loosely |
|---|---|---|
| Laws against legal personhood | The declaration's line that AI systems "must not be granted legal personhood" | It is a position on law, with safety researchers among the signers. It names no risk |
| Protection in law | The same declaration's line that AI systems should not be designed so that they come to deserve personhood | The same |
| The public survey | The declaration's own poll, whose figures "concern control and liability, not sentience" | It is about what people think of control |
| Laws against legal personhood | Legal rights could help AI systems, "or the companies that make them", gain power | The half about companies is a risk from people. The new heading suits it better than the old one did |

**Under the first heading: six candidates for the third,** as the verdict says. Each has the
head of Microsoft AI arguing that treating models as owed something makes advanced AI harder
to control: on the entries about the interview before retirement, kept files, protection in
law, the retired model that stays open, and rules for how a model speaks about itself (where
the caution adds that such a system "may be impossible to control"). The sixth is weaker: on
the entry about ending a conversation, a writer argues the ability could lead to more of what
has been called AI psychosis, which is a risk to the people who use the product.

**Under the second heading: two weak candidates.** On the public survey, the authors name
"conflict between advanced AI systems and people" as a harm of crediting a system with too
little. On laws against legal personhood, two researchers write that rights to own property or
to vote "look too risky for now". Each sits inside a caution whose main point belongs where
it is.

## 4. The read against John's published positions

I read the positions record's copy on the default branch of the `sentient-horizons` repository
(commit `82fb787`, 2026-11-15) with `git show`, without switching any branch there. I read
again the two positions named in the request, and the ones beside them.

**Does the new wording answer the earlier read's second contradiction?** Yes. That finding
(`docs/reviews/2026-11-20-live-pages-read-against-the-positions.md`, "Risk to people is filed
under 'has wants'") was that John holds a system can resist with nothing at stake for it, in
the record's words "'No stakes' never means 'no resistance'", while the page filed a study of
models interfering with a shutdown mechanism under a heading that began "If an AI system has
wants". The study now stands under a heading that does not hang on wants. The position that
depth is not safe says the same from the other side, that no hidden inside never means safe,
and the heading now agrees with it too.

**Does it overshoot into taking a side?** No.

- The heading is still an "if". It does not say that any AI system puts people at risk.
- "Whether or not it has wants" says that the risk does not wait on that question. It says
  nothing on whether any system has wants, which the record holds open on purpose and the
  site says it does not know.
- It does not carry over the rest of John's view. His positions go on to say what kind of
  resistance each kind of system shows, and that building deeper minds is a bet worth making.
  None of that is in the heading or the two sentences.
- The home page's closing words still hold: "All three are kept in view here, and none is
  argued for."

**One thing the read cannot settle:** the earlier read's finding had a second half, that
duties can come from a system's role before anyone knows whether it has an inside, and that
the three headings leave no place for it. This change does not touch that half, and the
ruling does not claim to.

## 5. Which built pages changed, and whether any count moved

- **15 built files differ across the two commits:** the 13 entry pages, the home page and the
  About page.
- **On each entry page** the only difference is the one heading.
- **On the home page and the About page** the only difference is the one sentence each.
- **Nothing else differs:** the page of acts, its feed, the list, Still Asking, the sitemap,
  the published headline file and the preview picture are the same file for file.
- **No count moved.** The count at the top is 5. The records hold 18 cautions under the first
  heading, 22 under the second and 13 under the third, as before. The About page still reads
  9 of 18.

## 6. The checks

Run on 2026-11-20 on the repository at the second commit.

- `python3 -I scripts/test_compute.py`: "Ran 57 tests", "OK".
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "24 dated acts", "The headline file matches the
  records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 96 outside addresses
  linked."

The build rewrote one line of `site/src/data/window.json`, which I left out of this commit.

## What I did not do

- I did not open the sources behind the 53 cautions again. The question here was where each
  sits, and I judged that from the records' own words.
- I did not look at the pages in a browser at phone or desktop width. The new heading is a
  few letters longer than the old one and sits in the same place.
- I did not read the positions' owning chapters. The ruling records that the master planning
  session read the section the position rests on before proposing the words.

**Fit to publish: the new heading is on all thirteen entry pages and the two sentences are the
ruled ones, the old wording is gone from the built site, no caution or count moved, and the
new wording answers the earlier contradiction without taking a side.**
