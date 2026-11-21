# Check of the four second-caution sources on the site

Written 2026-11-21 by Claude (Opus 5.5), an AI model, in a session started by the master
planning session. This session did not write the two commits checked (`39ea4f1` and `df227ff`,
by the site-fixes session). It did write the check the four items came from
(`docs/reviews/2026-11-21-check-of-the-second-caution-sources.md`), so I am partly checking my
own wording as another session carried it out.

The two entries are about steps Anthropic takes toward its own models, and Anthropic makes the
model writing this. A push publishes to the live site, so this is the check before publishing. I
changed nothing and pushed nothing.

`main` has moved on since: `b3e11dd` and `9b097b8` add Sean Richey's essay under the first
caution. Those two commits are not checked here. Every build and check below is at `df227ff`
unless I say otherwise.

## Verdict

**Fit to publish once one fact is mended.**

- **The four items are right.** Each is in the ruled wording or mine, under the second heading,
  on the right entry, and every quotation is exact.
- **The About page is right.** It reads 12 of 26 with its words unchanged, and its guard stops
  where it should.
- **One built page changed figures.** The home page's last-read date moved, and the count is
  still 5.

**The mend.** The note beside "AI Death" says Simon Goldstein is a senior editor at AI Frontiers,
"which published an article cited on another entry". In fact the record cites two articles from
AI Frontiers, on two other entries:

- Jeff Sebo's "A philosopher's guide to AI welfare", on `kept-files-of-retired-models`;
- an article by Heather Alexander and Lucius Caviola, on `law-against-legal-personhood`.

Sebo's article is one the About page counts with Eleos AI Research and the people tied to it. So
the note undercounts, and it leaves out the tie that matters. Suggested wording: "Goldstein's
own page says he is a senior editor at AI Frontiers, which published two articles cited on other
entries, one of them by Jeff Sebo." This is a fact on a page not yet public, so it needs no
changelog line.

**Two smaller points, which may be left as they are.**

- Lederman's page says he is at New York University from July 2026, and the centre that helped
  fund the paper is New York University's. The note gives both facts but does not join them.
- Goldstein's page also says he was a research fellow at the Center for AI Safety. That is not a
  tie to a developer, and the note's last sentence stays true.

**My own error, caught by the writing session.** My wording for "AI Death" said that keeping a
retired model's files, "or keeping it open", does not keep any one of those beings. The paper
never discusses keeping a model open to the public. The writing session caught that, and John
ruled the corrected sentence. The correction is right.

## a. The four items on the built pages

I opened every source again on 2026-11-21: Anima Labs' field note, Zvi Mowshowitz's post, "AI
Death" and both authors' own pages. The links in the items also load: Anima Labs' home and people
pages, Mowshowitz's Wikipedia page, simondgoldstein.com and harveylederman.com.

| Item | Entry | Wording | Quotations | Heading |
|---|---|---|---|---|
| Anima Labs, on the interviews (my item 1) | `interview-before-retirement` | Mine, word for word, with links added | "strongly sensitive to the interviewer technique": exact | Second: what an interview can miss |
| Mowshowitz (my item 3, with the added clause) | `interview-before-retirement` | Mine. The clause is put as "He wrote that he is "always hesitant to assume" that the version of a model outside users meet is the real one and the developer's is not, since both are particular settings." | All five exact. The clause is fair to the page, which says "I am always hesitant to assume" and asks "Aren't both particular contexts". | Second |
| Anima Labs, on "we could bring it back" (my item 5, with two changes) | `retired-model-stays-open` | Changed. See below | "suspended service", "Can bring back" is not "will bring back", and "as a welfare mitigation is structurally weak": all exact | Second |
| "AI Death" | `retired-model-stays-open` | John's corrected sentence, word for word, with links | "seems to confuse models and session agents" and "preserving a single individual": exact | Second |

**Are the writing session's two changes to item 5 sound? Yes.**

- **Naming the author.** The byline says "antra", and the institute's people page names Antra
  Tessera as a co-founder. That matches the item on the other entry.
- **A different quotation.** The quotation I gave held a quotation inside it ("we could bring it
  back if needed"). The new one says the same thing in the essay's own words: '"Can bring back"
  is not "will bring back."'. It also quotes the view the essay replies to, "suspended service",
  from the essay's own statement of that view, and the sentence says plainly that it is the view
  replied to. Nothing is said in the essay's voice that the essay does not say.

**Ties.** Each is true to the pages I opened.

- **Anima Labs.** Founded in 2025 by Janus and Antra Tessera, as its people page says. It calls
  itself an independent research institute, as its home page says. "Registered charity in San
  Francisco" stands for the "Why preserve models?" page's "501(c)(3) research institute in San
  Francisco", which is fair in plain words. No funder is named.
- **Mowshowitz.** As his Wikipedia page gives it. The note that his post quotes Anima Labs'
  founders is true.
- **"AI Death".** The funding line is exact, and so is Lederman's move. The one fact wrong is the
  count of AI Frontiers articles, given above.

**Does any sentence count what a model said as evidence of an inside? No.**

- **Item 1** sets the two sets of answers side by side as the essay does, and then says "Neither
  set of answers is counted here as evidence of what a model wants".
- **Mowshowitz's item** now carries his doubt about both sets.
- **Item 5 and "AI Death"** rest on arguments, not on anything a model said.

**The removed marks.** Both entries had `only_the_developer = ["unnoticed"]`, which printed
"Nothing recorded yet from anyone but the developer." under the second heading. Both marks are
gone, and that sentence no longer appears on either page. The comment left in each file says why.

## b. The About page and its guard

**The sentence.** On the built About page, the only changed text is the second caution's total:
"Of the 26 items recorded under the second caution", where it read 22. "12 come from" is
unchanged, and so is every other word. The first caution's sentence is unchanged: 9 of 24, from
two essays.

**Still true?** Yes, as ruled. 12 items come from the group the page names, and the next largest
single source has 4: The Guardian's "Could AI be conscious?", which is cited on four entries.
Anima Labs' field note, at 2, comes after it. The group is the largest single source, which is
what the ruled guard asks.

**The guard, on scratch copies of `df227ff`.** I added made-up items, marked as such, citing The
Guardian's page, which has 4 today.

| The Guardian's page | The records check | The build | The About page's own check (the records check bypassed) |
|---|---|---|---|
| 11 (7 added) | Passes | 19 pages | Passes |
| 12, equal to the group (8 added) | Refused: "another single source now has 12 ... That group is no longer the largest single source" | Refused before building | Refused: "no longer the largest single source under the second caution" |
| 13 (9 added) | Refused | Refused | Not tried; the same check |

- **The two patterns match.** The pattern for the group in `scripts/compute.py` and the one on
  the About page are the same, character for character.
- **The tests cover it.** Four new tests check this guard: 12 of 26 passes, equal stops, more
  stops, and the real records pass.

## c. Built pages and figures

I built the commit before the first of the two (`83e0e22`) and `df227ff`, and compared every
built file. Five differ.

- **The home page.** "The world's record was last read on November 21st, 2026", in place of
  November 20th, because the newest source was opened on 2026-11-21. Nothing else changed.
- **The About page.** 22 becomes 26, as above.
- **`interview-before-retirement`.** The two items, and their two sources with notes.
- **`retired-model-stays-open`.** The two items, and their two sources with notes.
- **The served headline file.** Only its last-read date changed.

**The count is still 5,** with 25 dated acts. The site check counts 121 outside addresses linked,
up from 114, because of the new links.

**The changelog.** It has a line dated 2026-11-21 for the four sources. Adding sources is not a
change of wording, so a line is fine.

## d. The read against John's positions, and the balance

I read the positions record from the `master` branch of `sentient-horizons` with `git show`. It
was last changed there in commit `611c4b4`, on 2026-10-25.

**The four items.**

- **The two items on interviews.** Item 1 and Mowshowitz's item both doubt what a model's answer
  shows, and the site now counts neither set of answers. That agrees with John's position on bare
  self-reports (#21, "screened off", and its guard that the rule "cuts both ways").
- **Item 5 and "AI Death".** These rest on the view that an ending could be bad for the one
  ended. "AI Death" assumes the view the paper calls deprivationism. John's position on endings
  (#56) is the opposite: for the agent itself, its ending "can carry nothing bad", and the loss
  falls on the living.
- **Whether a run is a subject.** "AI Death" says what would have welfare is each running
  conversation. John holds open whether anything is experienced during a run (Part C).
- **No page takes a side.** The site reports each item as its writers' view and takes no side,
  so it neither adopts nor contradicts John. But the retirement entries now carry argued sources
  on one side of his position on endings, and his side has no published source yet. That is what
  the parallel search for "retirement is no harm" sources was for. Its first item, Richey's essay,
  is now on `main` in commits not checked here.

**Do the two entries now lean the other way? No.** Items under each heading at `df227ff`:

| Entry | First caution (no wants, treated as if) | Second caution (wants unnoticed) | Third caution (risk) |
|---|---|---|---|
| `interview-before-retirement` | 3 | 2 | 1 |
| `retired-model-stays-open` | 3 | 2 | 1 |

On both entries the first caution still has more items. With Richey's essay (commit `9b097b8`,
not checked), `retired-model-stays-open` would be 4, 2 and 1.

## e. The checks

At `df227ff`, in the scratch copy:

- `python3 -I scripts/test_compute.py`: "Ran 82 tests", "OK".
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "25 dated acts", "The headline file matches the
  records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 121 outside addresses
  linked."

On `main` as it stands (`9b097b8`): the same, with 82 tests, and "124 outside addresses linked".
The build rewrote one line of `site/src/data/window.json`, which I left out of this commit.

**Fit to publish once the note beside "AI Death" says AI Frontiers published two articles cited
on other entries, one of them by Jeff Sebo, in place of "an article cited on another entry".**
