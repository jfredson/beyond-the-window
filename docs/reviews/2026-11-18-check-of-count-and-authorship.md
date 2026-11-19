# Check of the count with no fraction and of the first-person authorship wording

Written 2026-11-18 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. **This is a check by a session that did not make the changes.** It reads two
commits against John's two rulings of 2026-11-18:

- commit `726f9cb` (the home page opens with a count and no fraction) against
  `docs/rulings/2026-11-18-home-page-count.md` ("Count, no fraction");
- commit `561b1ec` (the notice and About in John's first person, About names the developer)
  against `docs/rulings/2026-11-18-how-the-site-declares-ai-authorship.md` ("As recommended").

**A reading, not a ruling.** Nothing was fixed. Every suggested wording is for John or a later
session to take or leave. A model wrote this check of a site about models, and the project's
first guideline applies to it.

## Verdicts

**The count (`726f9cb`): the ruling is applied, and the sentence is not ready to show as it
stands.** The total is gone from the large type, from the sentence, from the headline part of
the served file, from the window's spoken summary and from About. The number is still worked
out and never typed, and no guard was weakened. One thing must be fixed first: the sentence at
the top now says the six are offered *by* a developer, and the definition printed directly under
the same sentence on the list page, and again on About, still says "offered" means made
available *to* a model, and that a promise is not counted. Two of the six do not meet that
printed definition.

**The authorship wording (`561b1ec`): the ruling is applied, and one first-person sentence is
false by the record.** The placement, the voice and the naming are as ruled. Anthropic is named
in the conflict paragraph and nowhere else outside the entries, no model is named on any built
page, the first person has not spread, and the guard was loosened for that one name in that one
paragraph and no further. The sentence "In this first version I have ruled three things" is
wrong: the rulings folder shows more than three.

## What was done

- Both diffs were read in full, picture files apart.
- The repository was copied into a scratch folder at commit `89105e9` and built there
  (`npm --prefix site run build`), so nothing in the working folder was written. No site file
  has changed since `561b1ec`, so that build is the site the pictures show, with a different
  version id in the footer.
- `python3 scripts/compute.py --check` passed: 13 records, 9 on the list, 4 beside it, count 6.
  The 23 tests passed. The export ran. `python3 scripts/check_site.py` passed: 18 pages.
- The visible text of every built page, with the words in descriptions, hover titles and
  labels, was taken out and searched.
- Eleven changed copies of the built site and two changed copies of the headline file were put
  to the checkers, to see what they refuse.
- The six counted records were read against the sentence.
- Four outside addresses were opened: `https://www.anthropic.com/`,
  `https://johnandrewfredrickson.com/`, `https://sentient-horizons.com/` and
  `https://sentient-horizons.com/positions/`. All four answer, and each is the page the sentence
  says it is. The last is titled "Working Positions".
- Nine of the sixteen pictures were looked at: home in light, dark and phone width, the list in
  light and phone width, About, Still Asking in dark, and the two close-ups.

No AI model's programming interface was called. Nothing was spent, published, pushed or
deployed.

## Must fix before John is shown the sentences

### 1. The sentence says "offered by", and the definition under it still says "offered to" and rules out promises

**The text.**

- `site/src/pages/list/index.astro:14`, the list page's heading: "6 things that lie past the
  limits an AI model ordinarily works within are offered today by at least one developer of AI
  models."
- `site/src/pages/list/index.astro:23-25`, three lines under it: "'Offered' means that a
  developer of AI models makes the thing available to at least one of its models, and a dated
  public record that is still published says so. A plan, a promise for later, or a research
  result is not counted".
- `site/src/pages/about.astro:59-61`, the same definition under "'Offered today' has one
  meaning".
- `site/src/pages/index.astro:71`, `site/src/pages/list/index.astro:35`,
  `site/src/pages/about.astro:74` and `site/src/pages/list/[id].astro:74`: "a thing a developer
  can offer to an AI model".

**What is wrong.** The commit message and `docs/first-version-choices.md` (choice 3) say the
new sentence "no longer says the model is the one offered to", in answer to the earlier
review's point that "offered to an AI model" fits a product better than a law or a promise.
That is true of the sentence alone. The site's printed meaning of the word was not changed, so
a reader of the list page meets the new sentence and, straight after it, the old meaning. Read
against that printed meaning, by each record's own account:

- **Memory across conversations** is not made available to a model in the sense a reader will
  take. Its record says the memory is "about the user, and is the user's to view and delete",
  and "Nothing in the pages read presents it as kept for the model".
- **Keeping the files of retired models** is, in the record's own words on the same page,
  "Promised in public by one developer". The definition two paragraphs above says a promise for
  later is not counted. The promise is in force today, which is why it is counted, but the page
  does not say that, and a stranger sees a promise counted under a rule that says promises are
  not.
- **A welfare assessment at release** is published to the public, and **an interview before
  retirement** is done to a model. Neither is "made available to" one.

This is picture `11-list-light.jpg` and picture `13-list-phone.jpg`, which John will be shown:
the sentence, the definition and the row "Promised in public" sit on one screen.

**Suggested change.** Reword the definition to match the sentence, in both places: "'Offered
today' means that at least one developer of AI models does the thing, provides it, or has
publicly committed to it, and a dated public record that is still published says so. A plan,
a research result, or a promise that has not yet taken effect is not counted." And decide
whether "a thing a developer can offer to an AI model" in the four places above becomes "a
thing a developer can offer". If the verb in the sentence changes when John reads it ("in
place", the first alternative in choice 3), the definition changes with it. The meaning of
"offered today" decides what is counted, so a change to it is John's to rule.

### 2. "I have ruled three things" is not what the rulings folder shows

**The text.** `site/src/pages/about.astro:120-123`: "In this first version I have ruled three
things: the question, that the home page opens with a count that has no total beside it, and
where and in whose voice the site says an AI model drafted much of it. The list, each test, and
where each entry stands were drafted in sessions I direct and have not yet had my ruling."

**What is wrong.** It is a count of his own rulings, in his own voice, and it is short. By
`docs/rulings/` as of today he has also ruled:

- the name, and Still Asking as the standing record
  (`docs/rulings/2026-11-17-kickoff-decisions.md`, decision 1);
- the five rules the pages are written under: what a model says about itself settles nothing,
  machine authorship is declared, the site does not campaign, conditional language only, and
  corrections are public (the same file, decision 6). The About page states four of these as
  its own practice a few paragraphs higher (`about.astro:96-107`);
- the look, "Glass" (`docs/rulings/2026-11-17-design-direction.md`);
- a third caution (`docs/rulings/2026-11-18-a-third-caution.md`), ruled later the same day
  than this commit, so the sentence has also been overtaken.

The second sentence is accurate: no ruling covers the list, a test, or where an entry stands.

`docs/first-version-choices.md` (choice 5) names this list as one "which goes out of date with
each ruling". It went out of date within the day.

**Suggested change.** Drop the number and name the kinds of thing: "I have ruled the question,
the rules these pages are written under, how the page opens, and where and in whose voice the
site says an AI model drafted much of it. The list, each test, and where each entry stands were
drafted in sessions I direct and have not yet had my ruling." A sentence with no count does not
need rewriting at each ruling.

## Should fix

### 3. "I decide what stands" in the notice, with most of the page not yet decided

**The text.** `site/src/components/Notice.astro:16`: "I decide what stands."

**What is wrong.** It is something John does, and the repository's instruction file supports
it ("Nothing is settled until John says so"). But a reader of the notice alone will take it
that he has decided what is on the page in front of them, and About says the list, each test
and each entry's standing have not had his ruling. About carries the qualification. The notice,
on the two pages most readers see, does not.

**Suggested change.** "I decide what stands, and most of this first version has not yet had my
ruling." Or keep the three words and let "Who does what" carry it, as John chooses.

### 4. "The sessions" is an inside word, used in the notice before anything explains it

**The text.** `site/src/components/Notice.astro:14`: "I direct the sessions in which this site
is made." Also `about.astro:123` and `:126-127`, "sessions I direct".

**What is wrong.** A stranger does not know what a session is. The ruling's own starting point
used the word too, so this is flagged for John and not as a departure from what he approved.

**Suggested change.** "I direct the work on this site. An AI model drafted much of the
text ..."

### 5. "This site ... does take a view ... and that view is close to mine"

**The text.** `site/src/pages/about.astro:151-152`.

**What it rests on.** "My working positions" is sound: the linked page is John's own and is
titled "Working Positions". "That view is close to mine" rests on a model's reading and on no
word of his: `docs/reviews/2026-11-17-site-text-against-positions.md`, finding 7, found that
the site's order of evidence follows positions 21 and 53 of the blog's positions record, and
its conditional language follows position 19. He has ruled those positions for the blog. He
has not said the site's way of weighing is close to his, and recommendation 5 of
`docs/reviews/2026-11-17-positions-alignment.md`, which this paragraph carries out, is not
ruled.

**What is wrong.** Two things. The sentence states how near his own view is, which only he can
say. And it gives the site a view of its own, to set beside his, which is the site written as
its own agent. The checker's list of verbs does not include "takes a view", so the build does
not catch it.

**Suggested change.** In his voice the site's "view" can go: "I do not argue for them here. The
way these pages weigh what is on record, set out above, follows two of them: what a model says
about itself counts for little on its own, and a report checked against an independent reading
counts for more." That says what can be checked and leaves out how close.

### 6. "a developer whose commitments several entries count"

**The text.** `site/src/pages/about.astro:133`.

**What is wrong.** The sentence is true, and hard to read aloud: three nouns in a row before
the verb. The paragraph is otherwise plain, and nothing in it is promotional.

**Suggested change.** "The model that drafted the text is made by Anthropic. Several entries
count things Anthropic has committed to, and 5 of the 6 things counted as offered rest on
Anthropic's own pages."

### 7. "Today" claims more than two of the six records support

**The text.** The sentence at the top, and each record's own list of what could not be
confirmed.

- `data/entries/retired-model-stays-open.toml`: "Whether the retired model is still available
  today. The developer's page says so as of February 25th, 2026."
- `data/entries/memory-across-conversations.toml`: "How any of the three works today. The pages
  read are from 2024 and 2025."

**What is wrong.** On About, "today" means a dated record is still published. A stranger reads
"offered today" as offered now. For these two the record says only that a page from months or
years ago is still up. The other four are sound on this point: the ending of conversations and
the welfare assessment are both borne out by a report of 2026-11-09, and the two commitments
stand.

**Suggested change.** No change to the sentence is needed if the caveat says it: add "For each,
'today' means the developer's page saying so is still published" to the caveat at
`site/src/pages/index.astro:33-38`. This sits with the meaning of "offered today" in finding 1.

### 8. The drawing beside the number still gives the total in two additions

**The text.** `site/src/components/WindowGrid.astro:55-56`: "6 inside the frame" and "3 outside
it", under six filled and three empty squares, in the column beside the large 6. Also
`site/src/pages/index.astro:63`, "9 things, and how far the world has got on each", and the
footer of every page: "from a record of 13 entries, 9 of them things on the list".

**What is wrong.** None of these is the count written as a share, and the checker rightly lets
them pass. The applying session left them for John and said so (choice 3, "Left as it was, for
John"). But the ruling's reason was that a total "reads as progress toward a known total when
nobody knows the total", and on the home page in pictures 1, 2 and 3 the eye meets "6" on the
left and "6 inside, 3 outside" on the right at once. The new sentence under the drawing ("How
many more belong there is not known") is the right repair in words. Whether the three empty
squares and "3 outside it" stay is the question to put to John with the picture, as a named
question, not as a detail in a choices file.

**Suggested change.** Put it to him as one question with picture 1: keep the empty squares and
drop the two totals under the frame, or keep both. No change before he answers.

### 9. Nothing in code keeps the first person where the ruling put it

**The text.** `scripts/check_site.py`: no rule about "I", "my" or "mine".

**What is wrong.** The ruling limits the first person to the notice and one section of About.
Today it is so limited (see the list below). The project's guideline is that guards live in
code, and a later edit could put "I" on an entry page without the build stopping.

**Suggested change.** A rule that refuses "I", "my", "mine" and "me" outside the notice and the
section marked `id="who"`, with quoted source text left out as source titles already are.

## Notes

- **The count is worked out, not typed.** `scripts/compute.py` reads the one flag on each
  record, and `words_for` is no longer given the size of the list, so it cannot print a total.
  `--check` refused a headline file with the count changed to 7 and one with "6 of 9" typed
  into the sentence. The page throws at build time if the sentence stops opening with the
  count.
- **No guard was weakened and no test was bent.** The old rule 7 compared the count and the
  total; the new one compares the count and refuses anything else in the large type. Tests that
  read `headline.total` now read `records.on_the_list`, which is the same number under its new
  name. Two tests were added. The checker refused "6 of the 9" on the home page, a total put
  into the served headline, and a changed count. It does not catch "6/9" or "two thirds";
  neither is on the site.
- **The developer-name rule was loosened for one name in one paragraph only.** On changed
  copies of the built site the checker refused Anthropic elsewhere on About, Anthropic in the
  home page notice, a model's name and another developer's name inside the conflict paragraph,
  and a second paragraph given the same mark. A heading given the mark gained no exception.
- **Anthropic is named twice, both in the conflict paragraph, and no model is named on any page
  that is not an entry.** Searched: the home page, the list page, Still Asking, About and the
  not-found page, with their descriptions and labels.
- **"5 of the 6 things counted as offered rest on Anthropic's own pages" is right by my own
  count.** Five of the six name Anthropic alone as offering the thing: ending a conversation,
  the interview before retirement, the kept files, the retired model that stays open, and the
  welfare assessment. The source each one's standing cites is a page or report Anthropic
  published. Memory is the sixth, with three developers.
- **The history in the served file.** `/data/headline.json` keeps the row of 2026-11-17 with
  "count": 6 and "total": 9, and the new row has "count": 6 beside "on_the_list": 9. A reader
  of the file can see six of nine there. Each row is dated, the method line in the same file
  says the count stands with no total, and rewriting the old row would break the rule that
  history is never edited. It does not matter for the ruling, which is about what stands at
  the top of the page. One small thing: `records.total` is 13 and means all entries, so the
  word "total" still appears in the file with a different meaning.
- **The memory record is still counted,** as the ruling says it must be until John rules. The
  sentence claims of it only that at least one developer offers it today and that it lies past
  the limits a model ordinarily works within. Both are true by the record. The sentence no
  longer says it is offered to a model, which the record would not support. See finding 1 for
  the definition that still does.
- **The stranger test on the sentence and its alternatives.** The sentence can be said back.
  Its two soft spots are the ones choice 3 names: "the limits an AI model ordinarily works
  within" is abstract until the examples lower down, and "offered" leaves "to whom?". The first
  alternative ("in place today at one or more developers") fits all six better, and "in place"
  sits oddly on "happened once, for one model". The second ("6 things on this list") is the
  easiest to repeat and invites "out of how many?". My view, not a ruling: the sentence on the
  page is the best of the three once finding 1 is fixed.
- **The caveat reads well.** "Those limits" points back to the sentence two lines above, on a
  phone as well, where the drawing sits between them.
- **"A first count. The wording of the sentence above is not settled yet."** It is honest and
  it is a working note on a public page. It should come off when John rules the sentence. In
  the pictures it is small capitals at about ten pixels, readable in light and dark.
- **About still says "Two cautions are recorded"** (`site/src/pages/about.astro:104`). John
  ruled a third caution later on 2026-11-18, and that ruling says nothing on the site is
  changed by it yet. Another session has that work. Picture 7 will be out of date when it
  lands.
- **About's list of what is not known** (`about.astro:163`) now says the sentence and the
  memory record are open. That is right by the ruling.
- **The pictures match the built pages.** Text, order and numbers agree in the nine looked at.
  The footer in the pictures gives version `726f9cb`; a build today gives a later id, and no
  site file differs. Nothing reads wrongly in light, dark or phone width. Picture
  `8-still-asking-dark.jpg` is cut off at the top of the notice, so the notice cannot be read
  on that page from the pictures; it is the same component as on the home page.
- **Files changed that neither ruling called for.** `scripts/pictures.sh` gained a dark phone
  picture and four pictures of the list page, which serves showing John. One sentence was added
  under the drawing (`WindowGrid.astro:62`). `site/src/styles/site.css` gained the style for
  the "first count" line. None is outside the spirit of the rulings.
- **Not from these commits, seen in passing:** the definition's "a promise for later is not
  counted" beside "Promised in public" predates both commits. It is in finding 1 because the
  new sentence now sits on top of it.

## Every first-person sentence on the site

Found by searching the visible text of all 18 built pages. Two entry pages hold "our" inside
quoted source text and nothing else. There is no first person anywhere but these.

| # | The sentence, word for word | Where | What it rests on |
|---|---|---|---|
| 1 | "I am John Andrew Fredrickson, and I direct the sessions in which this site is made." | `site/src/components/Notice.astro:14` (home page and Still Asking) | Something he does. Close to the ruling's own starting point, "I direct the sessions". Finding 4. |
| 2 | "I decide what stands." | `Notice.astro:16` | Something he does, supported by the repository's instruction file. Finding 3. |
| 3 | "I am John Andrew Fredrickson, and I decide what stands." | `site/src/pages/about.astro:119` | As 2. On About the next sentences say what he has not ruled. |
| 4 | "In this first version I have ruled three things: the question, that the home page opens with a count that has no total beside it, and where and in whose voice the site says an AI model drafted much of it." | `about.astro:120-122` | Each of the three is on record. The count of three is wrong. Finding 2. |
| 5 | "The list, each test, and where each entry stands were drafted in sessions I direct and have not yet had my ruling." | `about.astro:122-123` | True by `docs/rulings/`. |
| 6 | "Much of the text, the records and the code were drafted by an AI model, in sessions I direct." | `about.astro:126-127` | A fact about how the work is done. Supported. |
| 7 | "I also write essays about minds, machine minds among them, at Sentient Horizons, and argue for my working positions there." | `about.astro:148-150` | Something he does. Both links open, and the second page is titled "Working Positions". |
| 8 | "This site does not argue for them. It does take a view on how to weigh what is on record, set out above, and that view is close to mine." | `about.astro:151-152` | "Close to mine" is a claim about his view that rests on a model's reading and no word of his. Finding 5. |

Sentences 1, 2, 3, 5, 6 and 7 say what he does or has decided. Sentence 4 misstates the record.
Sentence 8 puts a judgment in his mouth. No sentence gives him a feeling.
