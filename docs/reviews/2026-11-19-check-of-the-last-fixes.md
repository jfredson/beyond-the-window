# Check of the last fixes before the first release

Written 2026-11-19 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This is the session that made the full check
(`docs/reviews/2026-11-19-full-check-before-publishing.md`, called "the full check" below). It
wrote none of the work checked here. The model that wrote this is made by Anthropic, five
entries count things Anthropic does, and the cautions are about systems like the one writing,
so weigh the judgments below with that in mind. Nothing is published, pushed or deployed. No AI
model was asked any of the project's questions, no key was touched and nothing was spent.

Checked: the commit of fixes after the full check (`c167905`) and the commit that revised the
deploy note (`e14693d`).

## Verdict

**Fit to publish as it stands.** Nothing on the pages still must be fixed.

- All eleven must-fix items of the full check were made correctly. The eight sentences now say
  what their sources say.
- The name paragraph on the About page stays within John's words on record.
- The site can be listed by search engines, in The Quiet Galaxy's form, and every address in it
  is at beyondthewindow.org.
- The licence files match the sibling's.
- The deploy note carries the second deploy check's one must-fix point and four of its five
  should-fix points. The fifth is out of date, not wrong.
- The four checks pass on a fresh build.

**One condition is left, and it is not a fault:** John reads the sentences that are his
(section 6). The rulings make that a condition of the go.

**One sentence in the README is untrue,** and one section of it is John's to look at now that
the repository is public (section 3). Neither is on the site, and neither holds the release.

## What I changed

The task allowed one change: where an entry's fixes in commit `c167905` are right, record the
date they were checked. They are right on all eight entries that had fixes, so I set
`fixes_checked = 2026-11-19` on the eight records: the public survey, the interview before
retirement, the days-long task, the kept files, memory across conversations, ending a
conversation, protection in law and the welfare assessment. I added one dated line to
`CHANGELOG.md` saying so. The build rewrote `site/src/data/window.json`, which carries the new
dates. I changed no sentence, no page and no script.

Each of the eight pages now ends: "A full check of the site on November 19th, 2026 found more
to fix in this entry, and the fixes were made that day. Those fixes were checked on November
19th, 2026." The About page now reads: "That check found more to fix in 8 entries, and those
fixes have since been checked."

## 1. The full check's must-fix items 1 to 11

| Item | Made correctly? | Against the source |
|---|---|---|
| 1, the sample of 1,099 | Yes. "It surveyed 1,099 adults in a representative sample and 1,510 more from an online recruitment site, to compare the two" | The report: "we surveyed 1,099 U.S. American adults from Ipsos and 1,510 U.S. American adults from Prolific". Read again by me. |
| 2, the two 2024 figures | Yes. "Both figures are for the 2024 round alone", and the limit is now whether the change from 2023 is more than chance | I opened the report's first table as text myself. Its columns are the 2024 representative sample, the 2024 comparison sample, 2023 and 2021. Sentient now: 17.33, 10.85, 18.82, 18.06. A ban on developing sentience: 66.46, 57.25, 61.54, 57.68. The table's two columns of test results compare the two 2024 samples, so "The report does not say" holds. |
| 3, the interview records | Yes. "The developer has published short quoted passages and not the full records. Neither page says whether anyone outside the developer has read them." | Neither page says who has read the records. |
| 4, the days-long task | Yes. "No maintained public measure of anything longer was found." | It now agrees with the entry's own line that a successor measure is not known. |
| 5, the kept files | Yes. "took actions it calls "misaligned" when faced with replacement and given no other recourse" | The page: "motivated to take misaligned actions when faced with the possibility of replacement with an updated version and not given any other means of recourse". |
| 6, memory | Yes, in the record and in the group's sentence. "and is under the user's control" is on the home page, the list page and the entry's page, and "to view and delete" is on none | All three developers' pages say the user is in control. |
| 7, the two links | Yes. The three notes are gone. The site check now counts 76 outside addresses, two fewer | The writing session dropped the notes where I had offered linking the announcement pages, and reports that the page "Introducing Claude 4" does not link the developer's own report. I had said both announcements do. I had only searched that page for the report's address and did not read the link, so its reading may well be the right one. Dropping the notes is right either way. |
| 8, the Guardian writer's tie | Yes, on all three entries, in the words the entry on the survey uses | Nine authors on the survey's page; two advisors and one member of staff on the group's team page, which I read. |
| 9, search engines | Yes. Section 2. | |
| 10, README and licences | Yes for the licences. One untrue sentence is left in the README. Section 3. | |
| 11, the checked dates | Yes. `additions_checked` is on all 13 records and `corrections_checked` on all ten that were corrected. The fixes of this commit were given their own pair of dates, which is the honest way to do it: the page could not otherwise say that the newest text was unchecked. | |

**The name paragraph.** "A window is an image for a limit, and for what can be seen past it.
The name points past the limits AI systems now work within. Nothing here presumes that a
machine mind reaches for anything." John's words on record: the project explores "what is
beyond the confines of the current state of digital minds, and the window is an excellent image
for that" (2026-11-17), and the name "reinforces the idea that we are building structures to
study beyond the window or horizon of our current vantage point" (2026-11-16). The first
sentence rests on the first quotation (the window as an image, for a limit) and the second
(looking beyond it). The second sentence is his "beyond the confines of the current state of
digital minds" in plainer words. The third is the site's standing caution and gives no reason
for the name. It stays within his words. It is a paraphrase, so it is still his to read.

**"What Has Been Checked", sentence by sentence,** as built after my change:

1. "All 13 entries were written from sources that were opened and read, and on November 17th,
   2026 every source was opened again and compared with what its entry says." True by the
   records.
2. "On November 19th, 2026 every page, link and fact was checked again before the site was
   first published." True in substance, with two small notes. "Before the site was first
   published" is true from the day of release, which is when a reader meets it. "Every fact"
   is a little wide: the sentences about the project's own searches ("One search found none")
   have no source to check against. "Every page, every link and every sentence that rests on a
   source" would be exact.
3. "That check found more to fix in 8 entries, and those fixes have since been checked." True.
   As committed in `c167905` it read "have not been checked yet", which was true then.
4. "Each entry's page says what checks that entry has had and how far each of its sources was
   read." True.

**A leftover on four entry pages, for after release.** The pages for the public survey, memory
and protection in law still say of the changes of 2026-11-18: "A check on November 18th, 2026
covered some of those changes. The rest have not been checked yet." The page for the law
against legal personhood says: "Those changes have not themselves been checked yet." The full
check compared every sentence on those four pages with its source, so the lines understate
what has been checked. They err on the careful side. I was asked to set the date for the fixes
of `c167905` and left these.

## 2. The site made listable, against The Quiet Galaxy

| Thing | This site now | The sibling | Verdict |
|---|---|---|---|
| The line asking to be left out | Gone from every page. Only the page for a missing address carries it | The same | Right |
| `robots.txt` | "Allow: /" and "Sitemap: https://beyondthewindow.org/sitemap.xml" | The same form | Right. Its comment, "The site is public", is true from the day of release |
| The site check | Refuses a page that asks to be left out, a page without its own address, a robots file that turns search engines away or does not name the sitemap, and a sitemap that does not list exactly the built pages | The sibling has no such rule | Right, and stricter than the sibling |
| The sitemap | 17 addresses: the home page, the list, Still Asking, About and the 13 entries. No dates | The same form, with dates only on news posts | Right. It matches the built pages one for one |
| Each page's own address | On every page, at beyondthewindow.org | The same | Right |
| The text a link preview reads | The site's name, the page's title, its description and its address. The small kind of card, with no picture | The same, with a picture | Right |
| `_headers` | The sibling's five lines, unchanged | | Right. The two files are the same to the byte. The host is the same, so there is no reason to expect it to behave differently here. It cannot be tried before release |

- **Anything that names a tool:** none. The titles and descriptions in the preview text are the
  ones the pages already had. Model names appear only in the entries that are about those
  models.
- **Any address that is not beyondthewindow.org:** none among the page addresses, the sitemap
  and the robots file. The only other address in any page's head is
  `https://johnandrewfredrickson.com/`, as the author's link, which the sibling carries too.
- **Three small things, for after release.** An entry's preview description is its whole
  opening paragraph, up to 400 characters and more, and a preview will cut it. The comment at
  the head of `site/src/layouts/Base.astro` still says the footer has no licence words because
  the licence "has not been decided"; it has been, and the sibling's footer names its licence.
  The page for a missing address gives `https://beyondthewindow.org/404.html` as its own
  address, as the sibling's does.

Still not there, as the writing session lists: a preview picture, the set of icons, the block
that tells search engines what the site is, and a place for corrections to the three main
pages. None holds the release.

## 3. `LICENSE`, `LICENSE-DATA` and `README.md`

**`LICENSE`** is the sibling's file, the same to the byte.

**`LICENSE-DATA`** differs from the sibling's in four lines and nowhere else: what the records
are ("the entries, the groups and the developers named"), the code folders (it adds
`capture/`), the sibling's sentence about books and films (left out, rightly), and the line on
how to credit ("Beyond the Window, by John Andrew Fredrickson, a Sentient Horizons project,
https://beyondthewindow.org/"). The licence text is unchanged.

**`README.md`.** The rewritten parts are true as of this commit: the opening, the status, what
is settled and what is not, and the licences. The repository is public, the site has not had
its first release, no AI model has been asked any of the project's questions, and nothing has
been spent.

*Untrue as of this commit:*

- "How and where the public site declares this is not yet decided (open question 7)." It is
  the last line of "Who wrote this". John ruled it on 2026-11-19
  (`docs/rulings/2026-11-19-no-public-mention-of-ai-help-in-building.md`), and the README says
  so itself further down: "that public pages do not say how the site was built". Suggested:
  remove the line, or replace it with "Public pages do not say how the site was built, by
  John's ruling of 2026-11-19."

*Out of date, in the parts left as they were:*

- The table says of `docs/open-questions.md`: "None is answered." Several are ruled in part.
- The table says of `docs/first-version-choices.md`: "each decided by a session and not
  ruled." Several have since been ruled.
- "Two readings, kept apart" says the project keeps both readings apart "on every entry". The
  site keeps only the first so far, as its About page says.
- "No protocol exists yet" is true of Still Asking. The repository also holds a written method
  for the sealed capture (`docs/capture/method.md`), which the README does not mention.
- "The steps are in `.github/workflows/deploy.yml`." John's steps are in the deploy note. The
  workflow file holds the steps GitHub runs.
- The table of files has no row for `capture/`, `docs/capture/` or the rulings after the first.

*Should it be in a public repository?* Nothing in the README is private. The section "Who
wrote this" names the model and its maker. That is allowed: the ruling on public pages covers
the site and says documents inside the repository still say which were written by a model.
That ruling also says that if the repository is made public, the point is put to John first.
The session that made the repository public told him the working documents say this, and he
ruled the repository public all the same. The README is the first thing a visitor to the
repository reads, so it is worth his seeing this one section.

## 4. The deploy note, against the second deploy check

`docs/reviews/2026-11-19-deploy-files-written.md`, fourth version, against
`docs/reviews/2026-11-19-second-check-of-deploy-files.md`.

| The second check's point | In the note now? |
|---|---|
| Must fix 1: the take-down steps left the site reachable at the address each release gets | Yes. The note counts the addresses (the two names, the plain Cloudflare address, and one more for every release), and the take-down has a fourth step that switches those off, with Cloudflare's own sentence that the third step does not do it. It also says that the third and fourth steps do not survive the next release, which is why switching the workflow off comes first. |
| Should fix 1: what to do if the key is refused when attaching the addresses | Yes. The steps to attach the two addresses by hand are there, and so is the warning that the site can already be public at the plain Cloudflare address under a red cross. |
| Should fix 2: a stranger's proposed change | Yes, as a standing caution. |
| Should fix 3: three facts now backed by GitHub's pages | Yes. They are out of the list of unbacked facts. |
| Should fix 4: "Write" for "Edit" | Yes, in the step that makes the key. |
| Should fix 5: the robots file, the README and the licence files | The note's section "Outside these files, before a first release" still describes all three as they were, and adds that no page names its own address. Commit `c167905` mended all four after the note was written. The section says "they may have changed since", so it is out of date and not wrong. One line saying they were mended in `c167905` would close it. |

**John's four steps** come first in the note, in order: look at the records for the two names,
make the key, add the two secret values, tell the master session to go. They say that steps 1
to 3 publish nothing, and that from the moment both values are set the next push publishes.
That matches the rulings. What he will see when it works, and what to do when it does not, are
each set out by what he would see on the screen.

**One thing the take-down steps cannot do,** worth a line in the note: copies kept by search
engines and web archives stay after the site is down. Now that the site is listable, that
applies from the first day.

I did not read `.github/workflows/deploy.yml` or `site/wrangler.jsonc` again; neither changed
in these two commits.

## 5. The build, the checks and the pages

Run on 2026-11-19, on commit `c167905` and again after my change.

- `python3 -I scripts/test_compute.py`: 30 tests, all pass.
- `python3 -I scripts/compute.py --check`: 13 records, 8 on the list and 5 beside it. "The
  headline file matches the records." The count is 5.
- The site build: 18 pages and a sitemap.
- `python3 -I scripts/check_site.py`: "The built site passes: 18 pages, 76 outside addresses
  linked."

I compared the text of all 18 built pages with the text I read for the full check, line by
line. Every sentence that changed is one of the fixes above, a date a source was opened, or a
line about checks. Nothing else moved. I then looked at the home page, the About page, Still
Asking, the public survey's entry and the memory entry in the browser pane at a width of 375
points and of 1,280. No page is wider than the screen at either width and nothing is cut off.
The sitemap and the robots file are served.

## 6. What John reads before the go

Unchanged in substance from the full check's item 12.

- The five sentences in his first person, in "Who Is Asking". The full check's note on the
  fourth still stands: "the argument is laid out thing by thing" on a site that says "Nothing
  here argues".
- The name paragraph, quoted in section 1.
- "No AI model has yet been asked any of the questions this record will keep", which replaces a
  sentence his ruling kept by name.
- The four sentences of "What Has Been Checked", quoted in section 1.
- If he wishes, the README's section "Who wrote this".

## What I did not do

- I opened again only the sources behind the changed sentences that I had not read myself
  before: the 2024 report's table. For the others I relied on what I and the helpers read for
  the full check earlier the same day.
- The full check's list of things to mend after release is as it was, apart from the two this
  commit settled (the chart that "could not be read as text", and the stale check lines).
- I did not test the pages with a screen reader or in the light theme.
