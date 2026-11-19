# Second check: the count of 5, the printed meaning of "offered today", and the first-person wording

Written 2026-11-18 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. **This is a check by a session that did not make the changes.** The same
session wrote the first check (`docs/reviews/2026-11-18-check-of-count-and-authorship.md`), so
it is also checking how its own suggestions fared, and one of them turns out to have been
wrong (finding 2).

It reads commit `d47e6eb` against:

- John's ruling on what "offered today" means and on the memory record
  (`docs/rulings/2026-11-18-what-offered-today-means.md`, "Yes to both");
- his ruling on a third caution (`docs/rulings/2026-11-18-a-third-caution.md`), only for the
  About page's account of what he has ruled;
- the nine findings of the first check.

**A reading, not a ruling.** Nothing was fixed. A model wrote this check of a site about
models, and the project's first guideline applies to it.

## Verdict

**Not yet fit to show John. Two sentences must be fixed first, and both are small.** Everything
else is fit: the sentence at the top, the printed definition, the notice, the memory record's
move and the count.

The two:

1. The reason printed for the entries about the setting, "None is a thing a developer of AI
   models can offer", is no longer true under the meaning John ruled. One of those entries is a
   thing developers do: publish their rules for how their models speak about themselves.
2. The About page says in John's voice that the pages follow "two of" his working positions,
   and links the public page of those positions. The two it names are not on that page.

## What was done

- The diff of `d47e6eb` was read in full, picture files apart.
- The repository was copied into a scratch folder at commit `3a3367c` and built there. No file
  under `site/`, `scripts/` or `data/` differs between `d47e6eb` and that commit.
- `python3 scripts/compute.py --check` passed: 13 records, 8 on the list, 5 beside it, count 5.
  The 24 tests passed. The export ran. `python3 scripts/check_site.py` passed: 18 pages.
- Eight changed copies of the built site were put to the site checker. In the scratch copy one
  counted record was unmarked and the count script was run with no reason given, to see whether
  it would write.
- The eight records on the list and the five beside it were read against the printed
  definition.
- `https://sentient-horizons.com/positions/` was opened again and searched for the two
  positions the About page names. The blog's own positions record
  (`editorial/corpus-positions-ledger.md` in the blog's repository) was read for the same two.
- Five of the seventeen pictures were looked at: 1, 11, 15, 16 and 17.

No AI model's programming interface was called. Nothing was spent, published, pushed or
deployed.

## Must fix before John is shown the sentences

### 1. "None is a thing a developer of AI models can offer" is untrue of one entry under the ruled meaning

**The text.**

- `data/groups.toml:35`, printed on the home page, the list page and the page of each of the
  four entries in the group: "Laws, the rules developers publish for their models, and surveys
  of what people think are about the setting. None is a thing a developer of AI models can
  offer."
- `site/src/pages/about.astro:82`: "None of those is a thing a developer can offer."
- `site/src/pages/list/index.astro:23-24`, on the same screen as the first: "'Offered today'
  means that at least one developer of AI models does the thing, provides it, or has publicly
  committed to it, and a dated public record that is still published says so."

**What is wrong.** The first row under that reason is "A developer publishes its rules for how
its models speak about their own nature", standing at "Published by three developers". That is
a developer doing a thing, with a dated public record that says so. It meets the printed
definition word for word. A reader of picture `11-list-light.jpg` sees a welfare assessment
counted because a developer publishes it, and, lower on the same page, published rules set
aside because no developer "can offer" them.

Under the old, narrow meaning the sentence held: nothing in that group is made available to a
model. The ruling widened the meaning, and this sentence was carried over with "to an AI
model" cut off the end, which is what the first check asked for and is not enough.

The other three entries in the group pass: a law and two surveys are not things a developer
does.

Whether the rules entry belongs on the list is not this check's to say. The ruling's own words:
"Whether any other record should move on or off the list under the wider meaning. None was put
to him." The reason for keeping it beside the list is very likely the same as for memory: the
list is about what an AI model might reach for, and a developer's rule for how its model
speaks is a limit set on the model.

**Suggested change.** Give the true reason and drop "can offer": "Laws, the rules developers
publish for their models, and surveys of what people think are about the setting in which the
things on the list happen. None is itself a thing that lies past the limits an AI model works
within." The same on About. And tell John in one line that the rules entry meets the wider
meaning and is kept beside the list for that reason, so that he can say otherwise.

### 2. "follows two of them" names two positions the linked page does not hold

**The text.** `site/src/pages/about.astro:164-169`: "I also write essays about minds, machine
minds among them, at Sentient Horizons, and argue for my working positions there. I do not
argue for them here. The way these pages weigh what is on record, set out above, follows two of
them: what an AI model says about itself counts for little on its own, and a report checked
against an independent reading counts for more."

**What is wrong.** "My working positions" links `https://sentient-horizons.com/positions/`.
That page, opened today, holds seven positions and four open questions. None of the seven is
about what a model says about itself or about a report checked against an independent reading.
A reader who follows the link to find "two of them" finds neither.

The two are John's by his blog's own record: position 21 there says a model's bare report
about itself is set aside, and a report that matches an independent reading carries real
information. That record is not public. So the sentence is true of what he holds and cannot be
checked by a stranger, and the link does not go where the sentence says.

**This was the first check's suggested wording.** It was taken from the review of 2026-11-17
and offered without opening the positions page against it. The applying session used it as
given. The fault is the first check's.

**Suggested change.** Do not count them as "two of" the linked positions: "I do not argue for
them here. The way these pages weigh what is on record, set out above, is the way I weigh it in
those essays: what an AI model says about itself counts for little on its own, and a report
checked against an independent reading counts for more." Better still, link the essay that
argues it, opened first. Either way John reads the sentence, since it states his view.

## Should fix

### 3. "the look of the pages" claims more than he ruled

**The text.** `site/src/pages/about.astro:133`.

**What is wrong.** `docs/rulings/2026-11-17-design-direction.md` rules the direction, "Glass",
and says seven other points of the design are not ruled, among them the central picture, the
default theme and the colours.

**Suggested change.** "the direction of the pages' look".

### 4. "the cost of the opposite mistake to seeing wants that are not there"

**The text.** `site/src/pages/about.astro:136-137`.

**What is wrong.** It is hard to say back. The ruling has plain words for it.

**Suggested change.** "I have also ruled that every entry is to record a third caution, the
cost of missing wants that are there, and these pages do not show it yet."

### 5. "where every other entry stands"

**The text.** `site/src/pages/about.astro:138`.

**What is wrong.** "Every other entry" also means every second entry.

**Suggested change.** "where each of the other entries stands".

### 6. "each entry says which of those it is" is true of one row in three

**The text.** `site/src/pages/list/index.astro:25-26`: "A plan, a research result, or a promise
that has not yet taken effect is not counted, and each entry says which of those it is."

**What is wrong.** Of the three rows not offered yet, one reads "Shown in research". The others
read "Not shown" and "Not found. An idea only", which are none of the three.

**Suggested change.** "... is not counted, and each entry that is not counted says where it
stands."

### 7. The figures under the drawing are still to be put to John

**The text.** `site/src/components/WindowGrid.astro:55-56`, now "5 inside the frame" and "3
outside it"; `site/src/pages/index.astro`, "8 things, and how far the world has got on each";
the footer of every page, "13 entries, 8 of them things on the list".

**What it is.** The first check's finding 8. The applying session left it for John and said so,
and that reason holds: whether the drawing shows the things not offered is part of the design,
which is his. It should reach him as a named question with picture 1, and has not yet.

### 8. Two gaps in the new guard on the first person

**The text.** `scripts/check_site.py`, rule 9.

**What is wrong.** It refuses "I", "my", "mine" and "me". It let "We think ... our view"
through on the list page. And it exempts a paragraph of class "notice" on any page, so a notice
written onto an entry page would pass, where the ruling puts the notice on two pages.

**Suggested change.** Add "we", "our", "ours" and "us", and exempt the notice only on the home
page and the Still Asking page.

## What became of the first check's findings

| # | The finding | What was done | Sound? |
|---|---|---|---|
| 1 | The definition said "offered to" and ruled out promises | Put to John and ruled. The ruled meaning is printed on the list page and About, with a sentence on why "Promised in public" is counted. The four "offer to an AI model" phrases are changed | Yes, with finding 1 above left over from it |
| 2 | "I have ruled three things" | The count is gone and the rulings are named | Yes, with findings 3 to 5 above |
| 3 | "I decide what stands" in the notice | Changed as suggested | Yes |
| 4 | "the sessions" | "I direct the work on this site", and "under my direction" on About | Yes |
| 5 | "that view is close to mine" | Changed as suggested | No. The suggestion was wrong: finding 2 above |
| 6 | "a developer whose commitments several entries count" | Reworded as suggested | Yes |
| 7 | "Today" claimed more than two records support | The caveat on the home page and the definition on About now say what "today" means | Yes |
| 8 | The figures under the drawing | Left for John, with the reason given | Yes: finding 7 above |
| 9 | No guard on the first person | A rule was added, and the site-as-agent rule now catches "takes a view" | Yes, with finding 8 above |

## The definition against the records

The eight things on the list:

- **Keeping the files of retired models** (counted): a public commitment in force since
  2025-11-04. Meets "has publicly committed to it".
- **A retired model stays open** (counted): the developer provides it, by a page of 2026-02-25
  that is still published. Meets the definition as the page now defines "today".
- **An interview before retirement** (counted): the developer does it, under a standing
  commitment. Meets it.
- **A welfare assessment at release** (counted): the developer does it, most recently on
  2026-11-09. Meets it.
- **Ending a conversation** (counted): the developer provides it. Meets it.
- **A report about its own inner state is checked** (not counted): shown in one study. The
  definition leaves out a research result by name.
- **Working on one task for days** (not counted): not shown.
- **Protection in law** (not counted): not found, and not a developer's to do.

No counted record fails the definition.

The five beside the list: the law, the two surveys and memory do not raise a question. Memory
meets the definition and is beside the list by John's ruling, which the pages say. **The rules
entry meets the definition** and is beside the list by a reason the pages state wrongly:
finding 1.

## Notes

- **The memory record was moved and not otherwise altered.** Its group and the `beside` mark
  changed, the two fields that mark a thing as offered were removed, as the validator requires
  of any entry beside the list, and one line of "what could not be confirmed" was replaced
  because the move answered it. Both changes are shown on its page, dated, with the old words
  kept. Its name, description, test, standing, sources and caution are untouched. No other
  record changed.
- **The new line under "what could not be confirmed"** says no memory kept for the model was
  found "in the pages read". That is the three pages already cited, and no fresh search is
  claimed.
- **Its page says why it sits beside the list**, in words true to the ruling: developers offer
  it, by their own pages it is kept for the user, and the list is about what an AI model might
  reach for. Nothing says a model wants memory or does not. The line in its changes reads
  "Ruled on November 18th, 2026" and does not say by whom.
- **The count is 5 and is worked out.** The history in `data/headline.json` has one new row,
  with a reason, and the two older rows are untouched. In the scratch copy the script refused
  to write a moved count with no reason given.
- **Sentences that depend on the numbers are right:** "5 inside the frame", "3 outside it", "8
  things", "5 entries, not counted", "13 entries, 8 of them things on the list", "which gives
  5", and "all 5 things counted as offered rest on Anthropic's own pages". By my own count all
  five name Anthropic alone, and each one's standing cites a page or report Anthropic
  published. The guard on "several entries" still holds at three or more, and the records show
  five.
- **No guard or test was weakened.** The one test that changed now expects a refusal first and
  a pass once a reason is given. One test was added. The site checker refused the first person
  on an entry page and on About outside its block, "5 of the 8", Anthropic elsewhere on About,
  and a site that "takes the view".
- **Files changed that no ruling or finding called for:** entry pages gained a part, "Changes
  to This Entry", shown when a record has dated changes; the lists beside the list now show
  each group's name and reason; `scripts/pictures.sh` takes longer pictures of About and Still
  Asking and one of the memory page. Each serves the ruling or the showing. The group
  "Remembering" is now empty and is not drawn.
- **About still says "Two cautions are recorded"** (`about.astro:116`), which is right while
  the third is not yet in the records. The first-person sentence beside it now says so.
- **The pictures match the build.** The footers give version `f3bb8f6`, and no site file has
  changed since. John should look first at picture `11-list-light.jpg`, which holds the
  sentence, the definition, every row and both reasons for sitting beside the list on one
  screen. Then `1-home-light.jpg` for the number beside the drawing,
  `16-about-who-does-what-light.jpg` for the first-person sentences, `17-memory-beside-light.jpg`
  for the memory page, and `15-home-notice-light.jpg` for the notice.

## The sentence at the top, as printed

> 5 things that lie past the limits an AI model ordinarily works within are offered today by at
> least one developer of AI models.

Under it: "A first count. The wording of the sentence above is not settled yet."

## The definition, as printed

On the list page (`site/src/pages/list/index.astro:23-29`):

> "Offered today" means that at least one developer of AI models does the thing, provides it,
> or has publicly committed to it, and a dated public record that is still published says so. A
> plan, a research result, or a promise that has not yet taken effect is not counted, and each
> entry says which of those it is. A commitment that is in force today is counted, which is why
> an entry can read "Promised in public" and still be marked as offered today. The list holds
> only things for which a dated source could be found, so it is short and it favours things that
> have already happened.

On About (`site/src/pages/about.astro:66-71`):

> "Offered today" has one meaning. At least one developer of AI models does the thing, provides
> it, or has publicly committed to it, and a dated public record that is still published says
> so. A plan, a research result, or a promise that has not yet taken effect is not counted. A
> commitment that is in force today is counted. "Today" means that the record saying so is still
> published. An entry can also leave the count, because a developer can withdraw what it
> offered.

Both carry the ruled meaning word for word, and add to it only what the ruling implies.

## Every first-person sentence on the site

Found by searching the visible text of all 18 built pages. Two entry pages hold "our" inside
quoted source text. There is no first person anywhere but these.

| # | The sentence, word for word | Where | Only what he does or has decided, on the record today? |
|---|---|---|---|
| 1 | "I am John Andrew Fredrickson, and I direct the work on this site." | `site/src/components/Notice.astro:16` | Yes |
| 2 | "I decide what stands, and most of this first version has not yet had my ruling." | `Notice.astro:18` | Yes. No ruling covers the list, a test, or where the eight entries on the list stand |
| 3 | "I am John Andrew Fredrickson, and I decide what stands." | `site/src/pages/about.astro:132` | Yes |
| 4 | "I have ruled the question, the name, the look of the pages, the rules the pages are written under, how the home page opens, what "offered today" means, that memory across conversations sits beside the list, and where and in whose voice the site says an AI model drafted much of it." | `about.astro:133-136` | Yes for seven of the eight. "The look of the pages" is wider than the ruling: finding 3 |
| 5 | "I have also ruled that every entry is to record a third caution, for the cost of the opposite mistake to seeing wants that are not there, and these pages do not show it yet." | `about.astro:136-138` | Yes. The wording is hard to follow: finding 4 |
| 6 | "The list, each test, and where every other entry stands were drafted under my direction and have not yet had my ruling." | `about.astro:138-139` | Yes. "Every other" can be misread: finding 5 |
| 7 | "Much of the text, the records and the code were drafted by an AI model, under my direction." | `about.astro:142-143` | Yes |
| 8 | "I also write essays about minds, machine minds among them, at Sentient Horizons, and argue for my working positions there." | `about.astro:164-166` | Yes. Both links open |
| 9 | "I do not argue for them here." | `about.astro:167` | Yes. It is the ruled guideline that the site does not campaign |
| 10 | "The way these pages weigh what is on record, set out above, follows two of them: what an AI model says about itself counts for little on its own, and a report checked against an independent reading counts for more." | `about.astro:167-169` | No. The two are his by the blog's own record and are not among the positions on the linked page: finding 2 |

No sentence gives him a feeling. Sentence 10 is the only one that states a view of his, and it
is the one he most needs to read.
