# Check of the three labels on entry pages

Written 2026-11-20 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session did not write the commit checked (`6ffc0d6`, by the site-fixes
session). A push of it publishes to the live site, so this is the check before publishing. It
is also the first read of a changed page against John's published positions, as he ruled on
2026-11-20 (`docs/rulings/2026-11-20-positions-check-before-a-page-goes-out.md`).

I changed nothing and pushed nothing.

## Verdict

**Fit to publish.** The commit does what John ruled ("Yes, drop it";
`docs/rulings/2026-11-20-progress-dropped-from-the-kind-labels.md`) and nothing more. On each
of the 13 entry pages one label lost the word "progress". No other built file differs. No
sentence on any page leans on the old labels. A bare "Technical", "Political" or "Cultural"
contradicts no published position and leans toward none.

One thing for John to know, which is not a fault in the commit:

- **The label now stands with nothing on the site saying what it sorts.** It is the first of
  up to three small labels under an entry's title, beside "Not counted" and "First pass". No
  page says that an entry is sorted by whether the movement is in technology, in law and
  commitments, or in what people think. "Political progress" told a reader that much. A bare
  "Political" above a developer's own promise to keep a model's files may leave a reader
  asking what is political about it. The ruling foresaw this ("a bare 'Political' tells a
  reader a little less") and John took the change knowing it, so it is recorded here and
  nothing more.

## 1. What changed on the built site

I built the site twice in scratch copies, once as it stood at the commit before this one and
once at this commit, and compared every built file.

- **13 built files differ, and they are the 13 entry pages:** `/list/days-long-task/`,
  `/list/ending-a-conversation/`, `/list/interview-before-retirement/`,
  `/list/kept-files-of-retired-models/`, `/list/law-against-legal-personhood/`,
  `/list/memory-across-conversations/`, `/list/protection-in-law/`,
  `/list/public-belief-survey/`, `/list/researcher-views-survey/`,
  `/list/retired-model-stays-open/`, `/list/rules-for-speaking-about-itself/`,
  `/list/self-report-checked/` and `/list/welfare-assessment-at-release/`.
- **On each, exactly one thing differs:** the label. Four pages went from "Technical progress"
  to "Technical", seven from "Political progress" to "Political", and two from "Cultural
  progress" to "Cultural".
- **Nothing else differs.** The home page, the page of acts, its feed (`/acts.xml`), the list
  page, the About page, the Still Asking page, the page for a missing address, the sitemap,
  the published headline file and the link preview picture are the same file for file.
- **The old labels are gone everywhere.** I searched every built text file for the three old
  labels and found none. The word "progress" now appears nowhere in the built site at all.
- **Share and preview text:** the labels were never part of it. Each entry page's description
  and link preview text is the entry's own description, unchanged.
- **The labels were shown on entry pages only.** The three words appear nowhere else in the
  built site, in either case.

In the source, the commit changes one line of `site/src/pages/list/[id].astro` with a comment
naming the ruling, and adds one line to `CHANGELOG.md` that describes the change correctly. The
records' field `progress_kind` keeps its name, and nothing under `docs/` or `data/` changed.

## 2. Does any sentence lean on a label that is no longer there?

No. I listed every sentence on the 19 built pages that uses "kind", "technical", "political",
"cultural" or a word from "technology".

- None speaks of "kinds of progress", or of technical, political or cultural anything.
- The sentences that do say "kind" are about other things: "the kind of public record that
  would settle it" (About, and the list page), the "four kinds" of what is on record about AI
  models (About, Still Asking and every entry page), and single uses inside entries.
- In the source, the only other mention is the field's name in `site/src/lib/data.ts`, line
  38, which the ruling leaves alone.

So there is nothing to list with a file and a line.

## 3. The read against John's published positions

I read the positions record's copy on the default branch of the `sentient-horizons` repository
(commit `82fb787`, 2026-11-15) with `git show`, without switching any branch there. I read its
headings, its list of questions held open on purpose, and every position that mentions
progress, politics, culture, technology, law, standing in law, or what is owed to an AI
system.

**There is nothing to find.** A bare "Technical", "Political" or "Cultural" says what field a
movement is in. It takes no side on any position, and it settles none of the questions the
record holds open.

**What the change removes is the lean.** Three things in the record bear on the old wording,
and I give each in my own words:

- The record holds that new kinds of mind are worth wanting, on stated conditions, and that
  building deeper minds is a bet worth making though not a safe one. Those are John's views,
  argued elsewhere. "Progress" on every entry lent the site those views by its wording, on a
  site that says it recommends nothing. Without the word, the label no longer does.
- The record holds that progress is something kept up, and is not simply added to. A label
  that called each step "progress" sat a little oddly beside that. The bare label does not.
- The entry on laws that say an AI system cannot be a legal person carried "Political
  progress". Nothing in the record calls such a law progress or its opposite, so the old label
  said more than John has said. The new one says only that the matter is one of law.

One limit on this read: it covers the three labels and nothing else on the pages. The wider
finding that the site's frame speaks of movement toward these things is the ruling's own
"not covered", and is not judged here.

## 4. The checks

Run on 2026-11-20 on the repository as it stands, one commit past the one checked (the later
commit is a ruling file and changes no page).

- `python3 -I scripts/test_compute.py`: "Ran 57 tests", "OK".
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "24 dated acts", "The headline file matches the
  records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 96 outside addresses
  linked."

Both scratch builds, before and after the commit, gave the same last line. The build rewrote
one line of `site/src/data/window.json`, which I left out of this commit.

## What I did not do

- I did not look at the pages in a browser at phone or desktop width. Each label is two
  syllables shorter and sits in the same place.
- I did not read the positions' owning essays or chapters. For three bare words the record
  itself is enough.
- I did not judge the other commit not yet pushed, a ruling about one entry's cautions, which
  is outside what I was asked.

**Fit to publish: the old labels are gone from all 13 entry pages and from nowhere else,
because they were shown nowhere else; no other built file changed; no sentence leans on them;
the bare labels contradict no published position; and every check passes.**
