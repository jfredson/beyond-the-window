# Check of the three cautions refiled on the entry about laws against legal personhood

Written 2026-11-20 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session did not write the commit checked (`c785b6d`, by the site-fixes
session) or the three sentences in it. A push of it publishes to the live site, so this is the
check before publishing, and it includes the read against John's published positions that he
ruled for every changed page.

I changed nothing and pushed nothing.

## Verdict

**Fit to publish, with one thing owed soon after.** The three sentences on the built page are
the ruled ones word for word, under the right headings. Both sources say what the sentences
say. The About page reads 9 of 18, which is what the records give, and no other word of its
paragraph changed. The build stops below half and passes at exactly half. Two built pages
changed and no count on any other page moved. Nothing contradicts a published position.

**The one thing owed: the entry's page does not say that anything on it was corrected on
2026-11-20.**

- *What the page says now,* in its closing part on what has been checked: corrections were
  made and "Those corrections were checked on November 19th, 2026." It names no later date.
- *What happened:* a sentence that has been live since 2026-11-19 said more than its source.
  It read "one sponsor's stated aim of stopping companies from shifting blame onto the AI",
  and the source gives only a writer's report in four quoted words. This commit corrects it.
- *Why it matters:* the project's seventh guideline is that every correction is dated and
  stays visible. The changelog in the repository dates this one. The page itself does not.
  The writing session saw this and said so in the record: the page's closing part "has no
  sentence for this change". The one dated field that could carry it prints a sentence about
  the full check before the first release, which would be untrue here.
- *Why it does not hold up the push:* publishing makes the page more accurate, and holding it
  back would leave the overstated sentence live.
- *Suggested fix:* one dated sentence on the entry's page saying that three cautions were
  refiled and one reworded on 2026-11-20, and that the change was checked that day. It is new
  wording on a page, so it goes to John first.

Two smaller points, both about wording John has ruled, so both are his to weigh:

1. **The third sentence joins two things the article keeps apart.** The article says an AI
   system might use rights such as owning property to gain wealth or power. Separately, on
   voting, it says "a single company could create very large numbers of digital 'persons' with
   a right to vote", which "might concentrate political power in the company or an AI hive
   mind". The sentence on the page says legal rights could help AI systems, "or the companies
   that make them, gain power through ownership and voting". A reader could take that as the
   article saying companies gain power through ownership too, which it does not say. The
   article also says "a single company", not the company that made the system.
2. **Half of that sentence is about companies, under a heading about an AI system's wants.**
   The reason given for moving the two liability items was that a company's conduct does not
   depend on the system having wants. The same is true of a company gaining votes. It is one
   clause, and splitting it again would be a fourth sentence.

## 1. The three sentences on the built page

I built the site and read the entry's page as built. Each sentence matches the corrected
wording in the ruling
(`docs/rulings/2026-11-20-liability-cautions-refiled-on-the-bans-entry.md`, its second part)
word for word, with its source named under it.

| Heading on the page | Sentence as built | Source | Matches the ruling? |
|---|---|---|---|
| "If an AI system has no wants, and is treated as if it had" | An opinion piece reports that the sponsor of the bill in Oklahoma framed it as preventing companies from shifting "accidents onto the AI". | The opinion piece in The Regulatory Review | Yes |
| The same heading | The article arguing that the bans are premature also discusses a risk they are aimed at: that laws granting AI systems legal status could shield their makers from liability. | The article in AI Frontiers | Yes |
| "If an AI system has wants, and they put people at risk" | The article arguing that the bans are premature also discusses the risk that legal rights could help AI systems, or the companies that make them, gain power through ownership and voting. | The article in AI Frontiers | Yes |

- **"Nothing recorded yet" is gone** from the first heading. Before the commit that heading
  read "Nothing recorded yet. No source was found for this caution on this entry."
- **The two old sentences are gone** from the third heading, which keeps its other item, the
  public declaration.
- **One small thing in the reading order:** under the first heading the page says "The article
  arguing that the bans are premature also discusses", before any article has been mentioned.
  The article is first introduced under the next heading. The source line under the sentence
  names it, so a reader is not lost.

## 2. The two sources

Each opened by me on 2026-11-20.

**The opinion piece** (The Regulatory Review, 2026-06-29). The writing session's report is
right. The piece says: "The sponsor of the bill in Oklahoma framed it as preventing companies
from shifting 'accidents onto the AI.'" That is the writer's report, and the four quoted words
are the only words given as the sponsor's. The word "blame" is not in it. The word "framed"
links to a news article at `san.com`, and that address now shows a farewell notice saying the
outlet stopped on November 6, 2026, so the sponsor's own statement cannot be read. The
sentence on the page says no more than the piece.

**The article** (AI Frontiers, 2026-09-01). The writing session's report is right, with the
detail in the first smaller point above.

- *On liability:* its part headed "The Case for Exclusion" says the bills answer "real and
  pressing public concerns", and that "AI personhood carries risks, such as reducing human
  accountability". Later it says laws granting AI legal status "might be written in such a way
  as to shield developers". So "a risk they are aimed at" and "shield their makers from
  liability" both hold.
- *Between the two risks* it puts a third, about marriage, so the earlier wording "a second
  risk" was a miscount, as the ruling says. The corrected sentence does not count.
- *On power:* it treats shielding makers from liability and gaining power as separate risks.
  On voting it names the company as well as the AI system.

## 3. The About page

- **It reads 9 of 18:** "Of the 18 items recorded under the first caution, 9 come from two
  essays by the head of Microsoft AI, another developer."
- **No other word of the paragraph changed.** I compared the built paragraph before and after
  the commit word by word, and the only difference is "16" to "18".
- **My own count from the records:** 18 items stand under the first caution across ten
  entries. 9 of them are sourced to that writer's site, from two essays. The two new items
  are the two on this entry.
- **Is the paragraph still true as written?** Yes. It gives counts and does not say "most".
  No sentence on the About page uses "most" of that writer. A reader can see for themselves
  that 9 of 18 is half.

## 4. The guard

The About page's build compares the writer's share with the whole.

- **At exactly half it passes.** The site builds as committed, with 9 of 18.
- **Below half it stops.** In a scratch copy I added one item under the first caution, marked
  as constructed, which made the share 9 of 19. The build stopped with this message: "fewer
  than half of the items under the first caution now come from the one writer the part on
  sources names, so that sentence goes back to John for rewording before the site is built".
- **The message says the sentence goes back to John,** and a comment beside the guard says not
  to loosen it again without his ruling.

The repository was not touched by this test.

## 5. Which built pages changed, and whether any other count moved

I built the site in scratch copies at the commit before this one and at this commit, and
compared every built file.

- **Two built files differ:** `/list/law-against-legal-personhood/` and `/about/`.
- **On the entry's page:** the three sentences described above, and the date each of the two
  sources was opened, now November 20th, 2026.
- **On the About page:** the one figure.
- **Nothing else differs.** The home page, the page of acts, its feed, the list, every other
  entry page, Still Asking, the sitemap, the published headline file and the preview picture
  are the same file for file. The count at the top is still 5, and the table of developers and
  the 24 dated acts are unchanged.

## 6. The read against John's published positions

I read the positions record's copy on the default branch of the `sentient-horizons` repository
(commit `82fb787`, 2026-11-15) with `git show`, without switching any branch there.

**Does this change answer the earlier read's finding?** Yes. That finding
(`docs/reviews/2026-11-20-live-pages-read-against-the-positions.md`, the fifth lean) was that
the case for the bans sat under the heading about a system that has wants, while the heading
about a system that has none stood empty. John's position on the two opposite mistakes names
a cost of seeing too much in a system, and a company moving an accident onto its software is
that cost whether or not the software wants anything. The two items now stand under the first
heading, so the case for the bans is no longer filed where it reads as conditional.

**Does it overshoot?** No.

- The record holds that the two mistakes are twins, and that missing something real is usually
  the costlier one, with a stated exception. After the change this entry shows two items under
  the first heading, three under the second and two under the third. Nothing is taken from the
  second heading, so the page does not now lean toward dismissal.
- The reworded first sentence claims less than the one it replaces, which is the direction the
  record's care about evidence points.
- The sentences report what two writers say. None says a ban is right or wrong, and none says
  whether any AI system has wants.

**The About page's sentence** gives two counts and touches no position.

**One part of the earlier finding is not acted on,** and the ruling does not cover it: the
suggestion to move the aside that most of these laws "also cover animals, rivers and objects"
out of the entry's description. It stands as it was.

## 7. The checks

Run on 2026-11-20 on the repository at this commit.

- `python3 -I scripts/test_compute.py`: "Ran 57 tests", "OK".
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "24 dated acts", "The headline file matches the
  records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 96 outside addresses
  linked."

The build rewrote one line of `site/src/data/window.json`, which I left out of this commit.

## What I did not do

- I did not read the sponsor's own statement, which can no longer be opened.
- I did not look at the pages in a browser at phone or desktop width. The change is sentences
  inside lists that were already there.
- I did not read the positions' owning essays or chapters. The record's own entries were
  enough for sentences that report what others say.

**Fit to publish: the three sentences are the ruled ones word for word and say no more than
their sources, the About page's 9 of 18 is what the records give, the guard passes at half and
stops below it, only two built pages changed, and nothing contradicts a published position.
Owed soon after: a dated sentence on the entry's page saying it was corrected on 2026-11-20,
with its wording put to John first.**
