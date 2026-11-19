# Hand-over: the pages no longer say that an AI model helped build the site

Written 2026-11-19 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This is the writing session's note for the session that checks the work and
for John. **Nothing here has been checked by anyone but the session that wrote it,** beyond the
project's own scripts. Nothing is published, pushed or deployed. No AI model was asked
anything, no key was touched and nothing was spent.

It carries out John's ruling of 2026-11-19
(`docs/rulings/2026-11-19-no-public-mention-of-ai-help-in-building.md`, decided by: John):
public pages do not mention that an AI model took part in building the project, and they do
say plainly when a model has been asked the questions that make up the project's data.

Every wording choice below was **decided by: agent**. None is ruled.

## 1. The About page section, in full, as it now reads

John reads and owns each sentence of this before release. The number "5" and the words "all 5"
are worked out from the records when the site is built, and so is "13".

> **Who Decides, and What Has Been Checked**
>
> I am [John Andrew Fredrickson](https://johnandrewfredrickson.com/), and I decide what stands.
> I have ruled the question, the name, the direction of the pages' look, the rules the pages
> are written under, how the home page opens and the sentence beside its number, what "offered
> today" means, and that memory across conversations sits beside the list. I have also ruled
> that every entry records three cautions, and how the three are headed. The list, each test,
> and where each of the other entries stands are drafts, and have not yet had my ruling.
>
> Several entries count things [Anthropic](https://www.anthropic.com/) does or has committed
> to, and all 5 things counted as offered rest on Anthropic's own pages. Most of what is
> recorded under the first caution comes from two essays by the head of another developer's AI
> group. Most of what is recorded under the second comes from one research group, from people
> who advise it or have written reports with its head, and from people at Anthropic. So the
> record so far shows two small camps more than a settled field.
>
> All 13 entries are a first pass. Each was drafted from sources that were opened and read. On
> November 17th, 2026 a second check opened every source again and compared it with what each
> entry says. The corrections that check found were made on November 18th, 2026. In a further
> check that day, most of those corrections were read against their sources again. On November
> 19th, 2026 the third caution was added to every entry, with the sources that stand under it,
> and that addition has not been checked yet. Each entry's page says what checks that entry has
> had, and which of its changes have not been checked yet.
>
> I also write essays about minds, machine minds among them, at
> [Sentient Horizons](https://sentient-horizons.com/), and argue for
> [my working positions](https://sentient-horizons.com/positions/) there. I do not argue for
> them here. The way these pages weigh what is on record, set out above, is the way I weigh it
> in one of those essays,
> [*What a Report Is Evidence Of*](https://sentient-horizons.com/essays/what-a-report-is-evidence-of/):
> what an AI model says about itself counts for little on its own, and a report checked against
> an independent reading counts for more.

The fourth paragraph is unchanged.

## 2. Passages removed, with nothing put in their place

The first seven are the ones the ruling lists.

1. **The notice, whole** (`site/src/components/Notice.astro`, deleted; it stood on the home
   page and at the foot of the Still Asking page):
   > Who wrote this. I am John Andrew Fredrickson, and I direct the work on this site. An AI
   > model drafted much of the text, and that model is one of the kind of thing the site is
   > about. I decide what stands, and most of this first version has not yet had my ruling.
   > Who does what.

   The ruling names only the middle sentence. The rest went too, for the reason in section 6,
   point 1. The notice's styles in `site/src/styles/site.css` went with it, and the Still
   Asking page's last block, which held nothing else.
2. **Every entry page** (`site/src/pages/list/[id].astro`): "It was drafted by an AI model from
   the sources above."
3. **About, first paragraph:** ", and where and in whose voice the site says an AI model
   drafted much of it".
4. **About, the whole second paragraph:**
   > Much of the text, the records and the code were drafted by an AI model, under my
   > direction. That model is one of the kind of thing the site is about. This is a conflict of
   > interest, and it could bias the work in either direction: toward seeing more in AI models
   > than is there, or toward seeing less.
5. **About, the opening of the next paragraph:** "The conflict is sharper than that. The model
   that drafted the text is made by Anthropic."
6. **About, the paragraph on checks:** ", by a session that had not drafted them," and ", by a
   session that had made none of them,".
7. **About, "What Is Not Known Yet":** the list item "Who should check a site on this subject,
   when many of the available checkers are AI models."

Found by searching, and not in the ruling's list:

8. **About, first paragraph:** "under my direction" (see the rewording in section 3, row 2).
9. **The headline file the site serves** (`/data/headline.json`, which the About page links as
   "one small file that anyone can read"): the words "decided by a session and" in its line on
   what is ruled (section 3, row 7).

## 3. Sentences reworded, before and after

| # | Where | Before | After |
|---|---|---|---|
| 1 | About, heading of the section | Who Does What | Who Decides, and What Has Been Checked |
| 2 | About, first paragraph | The list, each test, and where each of the other entries stands were drafted under my direction and have not yet had my ruling. | The list, each test, and where each of the other entries stands are drafts, and have not yet had my ruling. |
| 3 | About, first paragraph | ... what "offered today" means, that memory across conversations sits beside the list, and where and in whose voice the site says an AI model drafted much of it. | ... what "offered today" means, and that memory across conversations sits beside the list. |
| 4 | About, paragraph on sources | The conflict is sharper than that. The model that drafted the text is made by Anthropic. Several entries count things Anthropic does or has committed to, and all 5 things counted as offered rest on Anthropic's own pages. | Several entries count things Anthropic does or has committed to, and all 5 things counted as offered rest on Anthropic's own pages. |
| 5 | About, paragraph on checks | On November 17th, 2026 a second check, by a session that had not drafted them, opened every source again and compared it with what each entry says. The corrections it found were made on November 18th, 2026. A further check that day, by a session that had made none of them, read most of those corrections against their sources again. | On November 17th, 2026 a second check opened every source again and compared it with what each entry says. The corrections that check found were made on November 18th, 2026. In a further check that day, most of those corrections were read against their sources again. |
| 6 | About, the description a search engine or link preview shows | Why Beyond the Window exists, how it is made, who does what, and what is not known yet. | Why Beyond the Window exists, how it is made, who decides what stands, and what is not known yet. |
| 7 | The served headline file, its line on what is ruled | Provisional, decided by a session and not ruled: no ladder, no probability and no year | Provisional and not ruled: no ladder, no probability and no year |
| 8 | Every entry page, last paragraph | This entry is a first pass, added on November 17th, 2026. It was drafted by an AI model from the sources above. A second check compared it with those sources on ... Who does what. | This entry is a first pass, written from the sources above and added on November 17th, 2026. A second check compared it with those sources on ... Who decides, and what has been checked. |

Notes on the rows:

- *Row 4.* The link to Anthropic's page moved to the name's first mention, which is now in the
  sentence about what the entries count. The rest of that paragraph is word for word as it
  was. It is no longer framed as a conflict of interest of the site's own: it states where the
  things counted and the cautions come from, and its closing sentence on "two small camps" is
  unchanged.
- *Row 5.* "The corrections it found" became "the corrections that check found", so that "it"
  cannot be read as the source.
- *Row 7.* The script that writes the file (`scripts/compute.py`) holds the line. Rewriting the
  file changed that one line and added no row to its history, because the count, the entries
  counted and the sentence did not change.
- *Row 8.* "Those sources" in the sentence about the second check used to point back at "the
  sources above" in the sentence that was removed, so "written from the sources above" keeps
  something for it to point at. The link's words now match the heading it leads to.

## 4. Sentences that are new

None is wholly new. The only new words are in section 3: the heading (row 1), "are drafts, and"
(row 2), "who decides what stands" (row 6), "written from the sources above and" and the link's
words (row 8). No opening sentence was written for the paragraph on sources, although it now
starts without one, because any opener would be a new claim for John to own.

## 5. What was searched, and what was left as it is

Searched for "draft", "session", "wrote", "written", "checker", "direction", "by hand", "alone",
"notice", "conflict", "who does what" and the names of models and tools: every file under
`site/src/`, the text fields of `data/entries/*.toml`, `data/groups.toml`, `data/headline.json`,
`scripts/export.py`, page titles and descriptions, and every built page in `site/dist` with the
served headline file.

Left as they are, because they say what was done and not by what:

- About, "How It Is Made": "The first tests were drafted during the first reading of the
  sources."
- About: "Each was drafted from sources that were opened and read."
- The entry on a days-long task: "The threshold of 40 hours is a choice made when this entry was
  drafted."
- The home page: "A second check against their sources was made on November 17th, 2026, and its
  corrections were made on November 18th, 2026."
- Each entry's sentences on its own checks.
- Every other use of "draft" is about a source (a paper's first draft, Microsoft AI's draft
  code). The one use of "sessions" is in the entry on interviews before retirement, and means
  the developer's interview sittings with its model.

Kept exactly as it was: everything on the Still Asking page about asking AI models, the About
page's "No AI model has been asked anything for this site", and the same sentence on each entry
page.

No sentence was added that says or implies that no AI model took part, that John wrote or
checked the work himself, or that anything was done by hand. The footer's copyright line and
the page's author tag carry John's name as before; neither was changed.

## 6. What I was unsure of

1. **The whole notice is gone, not only its middle sentence.** With that sentence out, what was
   left was "Who wrote this. I am John Andrew Fredrickson, and I direct the work on this site.
   I decide what stands, and most of this first version has not yet had my ruling." Under the
   heading "Who wrote this" that would read as a claim that John wrote it all, which the ruling
   forbids implying. So the home page and the Still Asking page now carry no statement in John's
   voice, and the home page no longer says that most of the first version is not ruled. It
   still says that all 13 entries are a first pass. If John wants a short line on the home page
   saying who decides, it would be a new sentence for him to rule.
2. **The developer's name stays on the About page.** The ruling keeps the fact "how many of the
   things counted rest on that developer's own pages" and does not say whether the developer is
   named. The earlier allowance for the name came from the ruling that is now replaced, where
   it was tied to the drafting. I kept the name, with its link, because the sentence is weaker
   as "one developer" and the entries name it anyway. The check still allows that one name in
   that one paragraph only.
3. **The first person stays in the About section.** That it is in John's first person was also
   part of the replaced ruling. Nothing in the new ruling speaks to it, and the task said to
   keep his name and that he decides, so the voice is unchanged.
4. **The new heading.** "Who Does What" promised a division of work that the section no longer
   describes, and with one person named it could be read as "John does all of it". "Who
   Decides, and What Has Been Checked" fits three of the four paragraphs. The paragraph on
   sources sits under it a little loosely.
5. **"are drafts".** Row 2 calls the list, the tests and the entries' standings "drafts". It is
   the plainest true thing I could put where "were drafted under my direction" stood.
6. **What the master session flagged once in the ruling stands:** a reader is no longer told
   that the entries counting one developer's commitments were drafted with that developer's
   model. Nothing on the pages replaces it. That is the ruling's effect and I did not soften or
   work around it.
7. **The served headline file still points at files inside the repository** (for example
   `docs/rulings/2026-11-18-what-offered-today-means.md`), which a reader cannot open because
   the repository is private. This is not about AI help, so I left it. It is a follow-up.
8. **Choice 18 in `docs/first-version-choices.md`** still describes the allowed name by the old
   mark `id="conflict"`. My task let me change choice 5 only, so the correction is in the note
   added to choice 5.

## 7. The guard

`scripts/check_site.py` has a new rule 10. It refuses a built page, or the served headline
file, that contains one of six phrase patterns: "drafted by an AI"; a model that "drafted",
"wrote", "helped" or "checked"; "by a session", "of a session", "a session's", "session that";
"under my direction"; "who wrote this"; "checker" or "checkers". Source titles inside `<cite>`
are not read, as for the other rules. "An AI model was asked" is not refused.

It is a tripwire for the removed sentences, and it is not a test of whether a page keeps the
ruling. A new sentence that mentions AI help in other words would pass it.

Tried on copies of the built site:

- On the built site as it was before this change, the rule refused every passage in section 2
  (the About page six times, the notice on both of its pages, all 13 entry pages, and the
  served headline file).
- A second developer's name written into the paragraph on sources was refused. The allowed name
  written elsewhere on the About page was refused. "An AI model wrote this, said a checker"
  written onto the Still Asking page was refused twice. "An AI model was asked nothing" was let
  through.

Other changes to the same script: the allowance for the first person in the notice is gone, so
the first person is now refused everywhere but the About page's block marked `id="who"`; and
the one allowed name is tied to the paragraph marked `id="sources"`.

In the About page's code, the constant `DRAFTER` is now `MOST_COUNTED_DEVELOPER`, and the build
stops if that developer is no longer the one most of the things counted rest on.

## 8. Checks run

- `python3 -I scripts/test_compute.py`: 28 tests, all pass.
- `python3 -I scripts/compute.py --check`: "The headline file matches the records." The number
  did not move: 5.
- `npm run build` in `site/`: 18 pages built.
- `python3 -I scripts/check_site.py`: "The built site passes: 18 pages, 67 outside addresses
  linked."
- I read the built home page, About page, Still Asking page and two entry pages as text, top to
  bottom, after the build.

Not done: the pages were not looked at in a browser, so the home page's spacing where the
notice stood has not been seen. No outside link was opened, because none was added or changed.

## 9. Files changed

- `site/src/components/Notice.astro` (deleted)
- `site/src/pages/index.astro`, `site/src/pages/still-asking.astro`,
  `site/src/pages/about.astro`, `site/src/pages/list/[id].astro`
- `site/src/styles/site.css`
- `scripts/check_site.py`, `scripts/compute.py`
- `data/headline.json`, `site/src/data/window.json` (both rewritten by the scripts)
- `docs/first-version-choices.md` (a note at the end of choice 5)
- this note
