# The first version of the site: the choices it was built on

Started 2026-11-17 by Claude (Fable 5.2), an AI model, in the session that built the first
version of the site. **Nothing in this document is a ruling.** John said on 2026-11-17: "go
ahead and build the first version of the website when you are ready. We will begin iterating
from there". Several design points the build needed are not ruled, so a provisional call was
made on each so that there would be something on a page to look at. Every call below was made
by a session and not by John, each is meant to be cheap to change, and none closes an open
question in `docs/open-questions.md`.

"Standard" means the family's standing practice (the row named is in `docs/inheritance.md`).
"Judgment" means a session's own call.

## Part 1. The eight choices the build started from

Each of these eight: **Decided by: agent (the master session), provisional, 2026-11-17, not
ruled by John.**

### 1. Scope: the world's record only

The site shows how far the world has got on each thing on the list. It makes no claim about
what machines want, and it shows no answer from any AI model.

- *Confidence:* high for a first version. No AI model has been asked anything under a written
  method, so there is nothing else that could honestly be shown.
- *Standard or judgment:* judgment. It matches the leaning in `docs/method.md`, section 7.
- *Strongest alternative:* show both halves from the start, with the second half empty and
  labelled as empty on every entry. It would show the project's full shape, and it would put an
  empty table on every page. The first version takes a small part of this: each entry page has
  the four kinds of evidence in their order, and says under each what has and has not been
  recorded.
- *Open question it touches:* 17 (how the two halves sit together). Not closed.

### 2. Pages

Home; one page per entry; About; Still Asking; a page for an address that does not exist. No
news, weekly reading, feedback or claims pages yet.

- *Confidence:* high. The pages left out each need something that does not exist yet: a weekly
  reading, a public repository for feedback, records of what named people said.
- *Standard or judgment:* judgment. The family's full set is row L1.
- *Strongest alternative:* build the full set as empty pages, so the top bar already has its
  final shape. The cost is five pages that say "nothing yet".

### 3. The top of the home page: a count alone

"N of M things on the list are offered to at least one AI model today", worked out from the
records by `scripts/compute.py` and never typed in, with the window beside it drawn from the
same computed file.

- *Confidence:* moderate. It is the only one of the six forms in open question 4 that counts
  the world alone, and a stranger can say back what it means. Its weakness is known: "offered"
  fits a product better than a law or a promise.
- *Standard or judgment:* worked out from the records and written to one small file is standard
  (rows A2, C1, C2, C3). The form is judgment.
- *Strongest alternative:* no number at first, only the question and the date the world's
  record was last read (form 5). It claims least and gives a reader nothing to repeat.
- *Open question it touches:* 4 (the headline). Not closed.

**Revised 2026-11-19. The sentence is now ruled.** John ruled it on 2026-11-19
(`docs/rulings/2026-11-19-home-page-sentence.md`; decided by: mixed): "Shorter version". The
sentence beside the count reads:

> **5** things past an AI model's ordinary limits are offered today by at least one AI
> developer.

`words_for` in `scripts/compute.py` writes it, with the count worked out from the records. The
form for a count of exactly 1 ("1 thing ... is offered") is the script's and is not in the
ruling. The line under the sentence that said its wording was not settled is gone from the home
page, and so is the matching item in the About page's list of what is not known yet. What
follows below is the record of 2026-11-18 and is kept as it was written; its sentence is the
old wording and is no longer on the site.

**Revised 2026-11-18. The form is now ruled; the sentence is a session's wording and is not.**
John ruled the form on 2026-11-18 (`docs/rulings/2026-11-18-home-page-count.md`; decided by:
mixed): "Count, no fraction". The home page opens with the count of the things on the list
that are offered today, with no total beside it. The wording above ("N of M things on the list
are offered to at least one AI model today") is kept here as the old wording and is no longer
on the site.

The ruling leaves the exact sentence open. The sentence now on the page is this session's.
**Decided by: agent (the session that applied the ruling), provisional, 2026-11-18, not ruled
by John.** He sees it on the page before it stands, and the page says under the sentence that
its wording is not settled.

> **6** things that lie past the limits an AI model ordinarily works within are offered today
> by at least one developer of AI models.

The count is large and the rest of the sentence sits under it. `scripts/compute.py` writes the
sentence (`words_for`), and it is never given the number of things on the list, so it cannot
put a total beside the count. The same sentence is the heading of the list page.

- *The choice:* that sentence. Against the starting point shown to John ("Six things lie past
  the ordinary limits of an AI model and are now offered by at least one developer"), it keeps
  "offered by at least one developer", which answers the review's point that "offered to an AI
  model" fits a product better than a law or a promise: the sentence now says who offers and
  no longer says the model is the one offered to. That also stops the sentence claiming more
  than the memory record does, since that record says the memory is the user's to view and
  delete. It uses the wording of the paragraph lower on the page ("the limits an AI model
  ordinarily works within") so the two say the same thing, says "developer of AI models" so a
  stranger knows what kind of developer, and says "today" where the starting point said "now",
  because "offered today" is the phrase the rest of the site defines and uses.
- *The stranger test:* a stranger can say it back as "six things that AI models do not
  ordinarily get are offered today by at least one company that builds them". Two soft spots
  remain. "The limits an AI model ordinarily works within" is abstract until the examples two
  paragraphs lower. And "offered" still leaves a reader asking "offered to whom?"; for a
  welfare assessment or kept files, "done" would be the natural word.
- *Confidence:* moderate. The form is ruled and the number is unchanged. The verb is the weak
  point.
- *Standard or judgment:* judgment call. The nearest family practice is The Upgrade Tree's
  count with no total.
- *Strongest alternative:* "6 things that lie past the limits an AI model ordinarily works
  within are in place today at one or more developers of AI models." "In place" fits every one
  of the six, where "offered" fits some awkwardly, and it leaves no "to whom?". Its cost: the
  rest of the site says "offered today" (the window's heading, every row of the list, each
  entry page, the definition on About), so either the top of the page uses a different word
  from everything under it, or the word changes across the site and in how the records are
  described, which is a larger change than the ruling asked for.
- *A second alternative:* "6 things on this list are offered today by at least one developer
  of AI models." It is the shortest and a stranger can repeat it word for word. Its cost: "this
  list" is used before the page has said what the list is, and with the word "list" in the
  sentence a reader is one step from asking "out of how many?", which is the question the
  ruling removed.
- *What was changed with it:* the caveat under the number was rewritten for a count (the list
  is short, it holds only things a dated source could be found for, nobody knows how long a
  full list would be, so the count is not a measure of how much lies past those limits). The
  window's spoken summary and its key no longer say "N of M" or "offered to at least one AI
  model". A sentence was added under the window saying the squares outside the frame are only
  the things found so far. About gives the count alone.
- *Left as it was, for John:* the window still draws the things not offered yet as squares
  outside the frame, with "3 outside it" under them, and the list's own heading says "9
  things". Both are plain facts about the list as it stands, and neither is a total written
  beside the count, but a reader can add them up. Whether the drawing should show them is part
  of the design proposal, which is not ruled.
- *Open question it touches:* 4 (the headline). Ruled in part; not closed.

**Revised again 2026-11-18, after a check and a further ruling.** The check of this change
(`docs/reviews/2026-11-18-check-of-count-and-authorship.md`, finding 1) found that the sentence
said "offered by" while the definition printed under it still said "offered to" and ruled out
promises. John then ruled what "offered today" means and that the record for memory across
conversations moves beside the list (`docs/rulings/2026-11-18-what-offered-today-means.md`;
decided by: mixed; "Yes to both").

*Ruled:* the meaning. At least one developer of AI models does the thing, provides it, or has
publicly committed to it, and a dated public record that is still published says so. A plan, a
research result, or a promise that has not yet taken effect is not counted. And the memory
record sits beside the list and is not counted.

*Worked out from the records:* the count is now 5, and 8 things are on the list. The sentence
at the top is unchanged in its words and now opens with 5.

*Not ruled, a session's wording* (**decided by: agent, provisional, 2026-11-18**): how the
meaning is printed on each page.

- On the list page: "'Offered today' means that at least one developer of AI models does the
  thing, provides it, or has publicly committed to it, and a dated public record that is still
  published says so. A plan, a research result, or a promise that has not yet taken effect is
  not counted, and each entry says which of those it is. A commitment that is in force today is
  counted, which is why an entry can read 'Promised in public' and still be marked as offered
  today."
- On About: the same meaning, then "A commitment that is in force today is counted. 'Today'
  means that the record saying so is still published."
- In the caveat under the number on the home page, one sentence added (finding 7): "For each
  thing counted, 'today' means that the dated public record saying so is still published."
- "A thing a developer can offer to an AI model" is gone from all four places. Each group
  beside the list now gives its own reason, written once in `data/groups.toml` and shown above
  the group and on each of its entries' pages.
- *Confidence:* high that the three now agree on one screen; moderate on the added sentence
  about "Promised in public", which explains a row's wording that the record itself could say
  better. *Judgment call.* *Strongest alternative:* change the kept-files record's own words
  from "Promised in public" to "Committed to in public", which would need no explaining
  sentence. Its cost is an edit to a record's standing words, which this change was told not to
  make.
- *Changed after the second check, 2026-11-18*
  (`docs/reviews/2026-11-18-second-check-of-count-and-authorship.md`, findings 1 and 6). The
  reason printed for the entries about the setting said "None is a thing a developer of AI
  models can offer", which is untrue of the entry on developers publishing their rules under
  the ruled meaning. It now reads: "Laws, the rules developers publish for their models, and
  surveys of what people think are about the setting in which the things on the list happen.
  None is itself a thing that lies past the limits an AI model ordinarily works within." About
  says the same. That entry was not moved: whether any other record moves has not been put to
  John. On the list page, "each entry says which of those it is" became "each entry that is
  not counted says where it stands", because only one of the three rows names a plan, a
  research result or a promise.
- *Left for John, as the check asked (finding 8):* the drawing still shows the things not
  offered yet as squares outside the frame, with "5 inside the frame" and "3 outside it" under
  them. One question to put to him with the picture: keep the empty squares and drop the two
  figures under the frame, or keep both. Nothing was changed.

### 4. Theme and colours

The theme follows the visitor's own light or dark setting. The amber for what the world's
record shows is kept. The dusk blue for what AI models said appears only on the Still Asking
page for now, since no other page has anything of that kind to mark.

- *Confidence:* moderate on the theme, high on the colours.
- *Standard or judgment:* judgment; it is the design proposal's decisions 2 and 3, which John
  has not ruled.
- *Strongest alternative:* evening by default, where the lit squares are most striking. The
  cost is that the site reads as a third sky site.

### 5. Where the site says an AI model drafted much of it

A notice on the home page and on the Still Asking page, and the About page says who does what.
The wording, adapted from the mock-ups: much of the text was drafted by an AI model, which is
one of the kind of thing the site is about; John Andrew Fredrickson decides what stands.

- *Confidence:* moderate. It is positions A and C of the design proposal together.
- *Standard or judgment:* judgment. It departs from three family rules (rows K1, K2, K5) and
  follows one precedent (row K3). That conflict is open question 7.
- *Strongest alternative:* one quiet line in the footer of every page (position B), which
  reaches a reader who arrives on an entry page and never sees the home page.
- *Open question it touches:* 7. Not closed.

**Revised 2026-11-18. The placement, the voice and the naming of the developer are now ruled;
the sentences are a session's wording and are not.** John ruled on 2026-11-18
(`docs/rulings/2026-11-18-how-the-site-declares-ai-authorship.md`; decided by: mixed): "As
recommended".

*Ruled:* the site says an AI model drafted much of it in three places (the notice on the home
page and the Still Asking page, the About page's section on who does what, and a line on every
entry page); the About page's conflict paragraph names Anthropic as the maker of the drafting
model, and no model is named anywhere; the notice and that About section are in John's first
person, and the records and the rest of the site stay impersonal.

*Not ruled:* the sentences. They are below, as now on the site. **Decided by: agent (the
session that applied the ruling), provisional, 2026-11-18, not ruled by John.** He reads and
owns every first-person sentence before release, and a different session checks them first.

The notice (home page and Still Asking page):

> I am John Andrew Fredrickson, and I direct the sessions in which this site is made. An AI
> model drafted much of the text, and that model is one of the kind of thing the site is about.
> I decide what stands.

The About page, "Who Does What", its first-person sentences and its conflict paragraph:

> I am John Andrew Fredrickson, and I decide what stands. In this first version I have ruled
> three things: the question, that the home page opens with a count that has no total beside
> it, and where and in whose voice the site says an AI model drafted much of it. The list, each
> test, and where each entry stands were drafted in sessions I direct and have not yet had my
> ruling.
>
> Much of the text, the records and the code were drafted by an AI model, in sessions I direct.
>
> The conflict is sharper than that. The model that drafted the text is made by Anthropic, a
> developer whose commitments several entries count, and 5 of the 6 things counted as offered
> rest on Anthropic's own pages.
>
> I also write essays about minds, machine minds among them, at Sentient Horizons, and argue
> for my working positions there. This site does not argue for them. It does take a view on how
> to weigh what is on record, set out above, and that view is close to mine.

- *The choice:* the passages as they stood, moved into the first person with every fact kept.
  First person covers only what John does and decides. Two facts were brought up to date and
  no further: what he has ruled now lists the count's form and this ruling beside the question,
  and the conflict paragraph names the developer where it said "one of the developers". His
  name, with the link to his page, opens each passage, so a reader knows who "I" is. The "5"
  and the "6" are worked out from the records at build time, and the build stops if the records
  no longer show several entries resting on that developer.
- *Confidence:* moderate. The facts are unchanged and checked against the records. Two
  sentences are the ones John is most likely to want to reword: "that view is close to mine",
  which is the old "close to his" and is the one place the section touches his views, and the
  list of what he has ruled, which goes out of date with each ruling.
- *Standard or judgment:* judgment call. The nearest family practice is the notice Minimum
  Viable Mind carries.
- *Strongest alternative:* the starting point shown to John as one sentence ("I direct the
  sessions, an AI model drafted much of the text, and I decide what stands"), with his name
  given only in the footer. It is shorter. Its cost is that the notice would not say who "I"
  is, and would drop the fact that the drafting model is one of the kind of thing the site is
  about.
- *Changed with it:* on About's list of what is not known, the line "Whether a number belongs
  at the top of the home page at all" became "What the sentence at the top of the home page
  should say, and whether memory across conversations belongs in the count", because the
  ruling on the count settled the first and left those two open.
- *Left as it was:* the line on every entry page ("It was drafted by an AI model from the
  sources above"), in the records' impersonal voice. Who made the second check of each record
  is not added, because the ruling says that was not put to John.
- *Open question it touches:* 7. Ruled in part; not closed.

**Revised again 2026-11-18, after the check**
(`docs/reviews/2026-11-18-check-of-count-and-authorship.md`, findings 2 to 6 and 9). The
sentences quoted above are the wording of the first draft and are kept as the old wording. The
first-person sentences now on the site, still a session's wording and not ruled (**decided by:
agent, provisional, 2026-11-18**):

The notice:

> I am John Andrew Fredrickson, and I direct the work on this site. An AI model drafted much of
> the text, and that model is one of the kind of thing the site is about. I decide what stands,
> and most of this first version has not yet had my ruling.

About, "Who Does What":

> I am John Andrew Fredrickson, and I decide what stands. I have ruled the question, the name,
> the look of the pages, the rules the pages are written under, how the home page opens, what
> "offered today" means, that memory across conversations sits beside the list, and where and
> in whose voice the site says an AI model drafted much of it. I have also ruled that every
> entry is to record a third caution, for the cost of the opposite mistake to seeing wants that
> are not there, and these pages do not show it yet. The list, each test, and where every other
> entry stands were drafted under my direction and have not yet had my ruling.
>
> Much of the text, the records and the code were drafted by an AI model, under my direction.
>
> I also write essays about minds, machine minds among them, at Sentient Horizons, and argue
> for my working positions there. I do not argue for them here. The way these pages weigh what
> is on record, set out above, follows two of them: what an AI model says about itself counts
> for little on its own, and a report checked against an independent reading counts for more.

The conflict paragraph (impersonal): "The model that drafted the text is made by Anthropic.
Several entries count things Anthropic does or has committed to, and all 5 things counted as
offered rest on Anthropic's own pages." The figure is worked out from the records; with memory
moved, every counted thing now rests on that one developer.

What each finding led to:

- *Finding 2 (the count of three rulings was wrong):* the sentence has no count and names the
  kinds of thing ruled. It was read against every file in `docs/rulings/` on 2026-11-18. It
  goes further than the check's suggested wording in three ways, each because a ruling exists:
  the name and the look (2026-11-17), the two things ruled about "offered today" and memory,
  and the third caution, which the pages do not show yet and the sentence says so. It does not
  mention the rulings on the first, separate asking of AI models, because no page says anything
  about that asking yet. The sentence does not claim to list everything.
- *Finding 3 ("I decide what stands" beside a page mostly not ruled):* the check's wording was
  taken.
- *Finding 4 ("sessions"):* "the work on this site" in the notice, "under my direction" on
  About. The impersonal paragraph about checks on About still says "a session"; it is outside
  the first person and the finding, and is left for John.
- *Finding 5 ("that view is close to mine"):* the check's wording was taken, with "an AI model"
  for "a model". It says the pages follow two of his published positions, which rests on the
  reading in `docs/reviews/2026-11-17-site-text-against-positions.md`, finding 7, and on no
  word of his. He should confirm it or strike it.
- *Finding 6 (three nouns in a row):* the check's wording was taken, with "does or has
  committed to", since some of the entries are things done and not commitments.
- *Finding 9 (no guard in code):* `scripts/check_site.py` now refuses "I", "my", "mine" and
  "me" anywhere but the notice and the block on About marked `id="who"`, with words inside
  quotation marks left out. It also refuses "this site takes a view".
- *Confidence:* moderate. *Judgment call.* *Strongest alternative* for the list of rulings: a
  sentence that names nothing ("I have ruled some of what is here, and the list, each test and
  most entries' standing have not had my ruling"), which never goes out of date and tells a
  reader less.

**Revised a third time 2026-11-18, after the second check**
(`docs/reviews/2026-11-18-second-check-of-count-and-authorship.md`). The wording above is kept
as it was. What changed, still a session's wording and not ruled (**decided by: agent,
provisional, 2026-11-18**):

- *Finding 2 ("follows two of them"):* the linked positions page does not hold those two
  positions, so the count is gone. The sentence now reads: "The way these pages weigh what is
  on record, set out above, is the way I weigh it in one of those essays, *What a Report Is
  Evidence Of*: what an AI model says about itself counts for little on its own, and a report
  checked against an independent reading counts for more." The essay
  (`https://sentient-horizons.com/essays/what-a-report-is-evidence-of/`, dated June 21st, 2026
  on its page) was opened on 2026-11-18. It says "The bare report, on its own, is screened
  off", and that where a model's account of its own inner state matches what an independent
  reading finds, on a fact its training text never held, the report "carries real information".
  One difference for John to weigh: the essay says the bare report is worth nothing as evidence
  of an inside, and the sentence says "counts for little on its own". This is the one sentence
  that states a view of his, so it is the one he most needs to read.
- *Finding 3:* "the look of the pages" is now "the direction of the pages' look", which is what
  the design ruling covers.
- *Finding 4:* the third caution is now named in the ruling's own words, "the cost of missing
  wants that are there".
- *Finding 5:* "where every other entry stands" is now "where each of the other entries
  stands".
- *Finding 8:* the guard on the first person now also refuses "we", "our", "ours" and "us", and
  excuses the notice only on the home page and the Still Asking page.
- *Confidence:* high on findings 3, 5 and 8; moderate on 2 and 4, which are John's to read.

**Replaced 2026-11-19 by John's ruling that public pages do not mention AI help in building the
project** (`docs/rulings/2026-11-19-no-public-mention-of-ai-help-in-building.md`; decided by:
John). Everything above in this choice is kept as the record of what stood before, and none of
it describes the site now. What changed on the pages that day:

- The notice is gone from the home page and the Still Asking page, and its component and its
  styles are deleted.
- The entry pages no longer say what drafted an entry.
- The About page's section is headed "Who Decides, and What Has Been Checked". It says who
  decides, what John has ruled, where the record's sources come from, and what was checked and
  when. It does not say by what. The paragraph that named Anthropic as the maker of the
  drafting model now names it only as the developer whose own pages the things counted rest on,
  and its mark is `id="sources"` where it was `id="conflict"`. Choice 18's note on the one
  allowed name should be read with that new mark.
- The first person now stands in one place only, the About page's block marked `id="who"`.
- `scripts/check_site.py` refuses a built page that carries one of the removed phrases (its
  rule 10).

The sentences are a session's wording and are not ruled. John reads and owns each first-person
sentence before release. The hand-over note with every before and after is
`docs/reviews/2026-11-19-authorship-mentions-removed.md`. *Decided by: agent, for the wording;
John, for the removal.*

### 6. Voice

Plain statements that say what was found, with as little first person as possible. The site is
never written as its own agent.

- *Confidence:* moderate. It is a holding choice. An impersonal voice hides who is speaking,
  which is the question this project can least afford to blur.
- *Standard or judgment:* the rule against writing a site as its own agent is standard (row
  K5). The rest is judgment.
- *Strongest alternative:* John's first person throughout, as on the sibling sites. It is
  warmer and plainer, and it would put words a model drafted in his mouth before he has ruled
  on the voice.

### 7. The order of evidence on an entry page

Four kinds, shown in this order and never added together: what was measured without the AI
model's own word; reports checked against an independent reading; choices made at a cost; plain
statements. In this version each kind says that nothing has been asked under a written method
yet, plus any published research the entry's sources report, described as what the source
reports.

- *Confidence:* moderate. The order is the one the blog's published positions give
  (`docs/reviews/2026-11-17-positions-alignment.md`, recommendation 4).
- *Standard or judgment:* judgment. It follows a proposal John has not ruled
  (`docs/proposals/2026-11-17-how-a-machines-word-earns-weight.md`). The guideline as ruled has
  four parts and no order of evidence.
- *Strongest alternative:* the table in `docs/record-schema.md`, section 7 (said, chosen,
  measured, not found), which is in the documents already and puts what was said first.

### 8. No ladder

Each entry's state is shown in the plain words the research gives it. An entry counts toward
the number at the top when its record shows it is offered by at least one developer of AI
models today.

- *Confidence:* moderate. Whether one ladder fits technical, political and cultural progress is
  open question 14, and the first entries are the first real test of it.
- *Standard or judgment:* judgment. The siblings each have a fixed ladder (row A9).
- *Strongest alternative:* the kickoff's five rungs (an idea only; shown in research; offered
  by one developer; offered by several; standard practice), which would give the window its
  five columns from the design proposal and would decide open question 14 by building it.

## Part 2. Further choices made while building

Each of these: **Decided by: agent (the build session), provisional, 2026-11-17, not ruled by
John.**

### 9. The window has two parts, not five columns

The picture on the home page is a window frame. A filled square inside the frame is a thing
offered to at least one AI model today. An outlined square outside the frame is a thing not
offered yet. Each row is one group on the list. It is drawn in the page itself and not as a
single picture, so each square is a link a finger can press, and a text list of the same
entries sits under it.

- *Confidence:* moderate. *Judgment.* It follows from choice 8: with no ladder there are no
  columns to draw. The design proposal says the window "needs only one thing", a line between
  offered today and not yet.
- *Strongest alternative:* the mock-up's five columns as one drawing, which shows more at a
  glance and whose squares are about seven pixels wide on a phone.
- *Revised 2026-11-18:* the window's words no longer say "offered to at least one AI model" or
  give the squares inside as a share of all the squares; see the revision under choice 3. The
  drawing itself is unchanged.

### 10. What a record holds in this version

One file per entry in `data/entries/`, named for its id, in the layout the siblings use (TOML).
`scripts/compute.py` refuses a file that breaks a rule. The fields, following
`docs/record-schema.md` sections 1, 3, 4 and 10:

| Field | What it is | Required |
|---|---|---|
| `id` | Plain lower-case words joined by hyphens. The last part of the page's address. Never renamed. | yes |
| `name` | The plain name. | yes |
| `description` | One paragraph for a reader who has never heard of the thing. | yes |
| `group` | The plain name of the group it sits in on the list. | yes |
| `test` | What would count as it having happened. | yes |
| `settled_by` | The kind of public record that settles the test. | yes |
| `progress_kind` | `technical`, `political` or `cultural`. | yes |
| `added` | The date the record was added. | yes |
| `first_pass` | `true` while nobody but the drafting session has checked the record. | yes |
| `constructed` | `true` only on a made-up example. A constructed record is never counted and never built into the site unless every record is constructed. | no |
| `notes` | Working notes. Not shown on the site. | no |
| `beside` | `true` on an entry about the setting (a law, a published rule, a survey). Such an entry is shown beside the list and is never counted (choice 20). | no |
| `limits` | A list of sentences: what was looked for and could not be confirmed. Shown on the entry's page (choice 21). | no |
| `[state]` | `words` (the state in a few plain words), `detail` (a fuller account, optional), `offered_today` (true or false; this is what the count reads; required on a list entry and refused on a beside entry), `offered_by` (the developers that offer it; needed when `offered_today` is true, and each must be in `data/developers.toml` with its public page so the name can be linked), `set_on` (the date the state was set), `source` (the key of the dated source behind it). | yes |
| `[[sources]]` | `key`, `label` (a plain description of the page; it is not the page's own title, because the research document did not record titles), `publisher`, `url`, `opened` (the date a session opened the page), and optionally `published` (text, as the world supplies it), `from_maker` (true when the source is the developer's own word about its own model), `kind` (`primary` or `coverage`), `read` (`full`, `abstract`, or, PROPOSED 2026-11-19, `part` for a paper whose cited passages were read in the full text and whose other pages were not), `says` (what the page says that the entry rests on), `note`. | at least one |
| `[[evidence]]` | `kind` (one of `measured`, `checked-report`, `choice`, `statement`), `text` (what the source reports, in those terms), `source`. | no |
| `[[cautions]]` | `kind`, `text`, `source`. Three kinds since 2026-11-19, as John ruled (`docs/rulings/2026-11-18-a-third-caution.md`, `docs/rulings/2026-11-19-caution-headings.md`): `attribution` (if an AI system has no wants, and is treated as if it had), `unnoticed` (if an AI system has wants, and they go unnoticed), `safety` (if an AI system has wants, and they put people at risk). Until 2026-11-19 there were two, `safety` and `attribution`. The order they are shown in is PROPOSED 2026-11-19. | no |
| `only_the_developer` | A list of caution kinds, today only `unnoticed`, for which the developer's own page is the only source found. The entry page then says that nothing is recorded yet from anyone but the developer, and points to the developer's reason under Sources (`docs/rulings/2026-11-19-developer-reason-not-alone.md`). Refused when the record holds a caution of that kind. The field and the sentence are PROPOSED 2026-11-19. | no |
| `[checks]` | `against_sources`, `changed`, `changes_checked`, `some_unchecked`, and, PROPOSED 2026-11-19, `added_to` (the date more was added after those checks) and `additions_checked` (the date that addition was checked). | no |
| `[[history]]` | `date`, `field`, `old`, `new`, `why`. For changes after the first commit. | no |
| `verify` | A list of facts set down before their source was opened. A record with anything in it is left out of the build. | no |

*Confidence:* moderate. *Mostly standard* (rows A8, B4, B9, B10). Three things are judgment:
the state as words and a true-or-false flag in place of a rung; the two kinds of caution as a
list on the record in place of records of their own (open question 6); and leaving out the
field for which unit of machine mind an entry concerns (open question 1).
*Strongest alternative:* one file per group, as The Upgrade Tree has, which is easier to read
whole and harder for two sessions to work on at once.

### 11. What the validator refuses

A field it does not know; a missing required field; a record with no test; a record with no
settling record; a state with no source, or whose source has no address or no date opened; an
entry marked as offered today that names no developer, or a developer with no page to link; an
entry beside the list that carries an offered flag; a source key used and not defined; an
id that is not plain hyphenated words, that differs from the file name, or that contains a
developer's, model's or product's name (the list of names is in `scripts/compute.py`); an
evidence kind or caution kind outside the lists above; a mix of constructed and real records.
`scripts/test_compute.py` tests each refusal.

*Confidence:* high. *Standard* (rows B4, B11; `docs/record-schema.md`, section 12).

### 12. The headline file

`data/headline.json` is written by `scripts/compute.py` and by nothing else. It holds the
count, the total, the sentence, the ids counted, the date computed (Pacific time), the latest
date any source in the records was opened (shown on the home page as when the world's record
was last read), how many records are a first pass, and a history. A history row is appended
when the count, the total or the ids counted change, and no row is ever edited.

*Revised 2026-11-18, after John's ruling that the count stands with no total beside it
(`docs/rulings/2026-11-18-home-page-count.md`).* The headline part of the file no longer holds
a total. How many things are on the list stays in the file's `records` part (`on_the_list`),
as a plain fact about the records. A history row now also holds the sentence and names what
changed, and a row is added when the count, the ids counted, the number of things on the list
or the sentence change. The row written on 2026-11-17 is left exactly as it was, with its old
field name "total", because no row is ever edited; a row dated 2026-11-18 records that the
sentence changed and nothing else did. *Decided by: agent, provisional.* *Confidence:*
moderate. *Judgment.* *Strongest alternative:* rewrite the old row without its total, which
would leave no fraction anywhere in the served file and would break the rule that history is
never edited.

*Revised again 2026-11-18:* when the count or the entries counted have changed,
`scripts/compute.py` does not write the file unless it is given a reason (`--why`), and the
reason is kept in the new history row. The row of 2026-11-18 that takes the count from 6 to 5
says the memory record was moved beside the list and why. *Decided by: agent.* *Confidence:*
high. *Standard* (row B11: guards live in code).
`scripts/compute.py --check` refuses a missing or out-of-date file. `scripts/export.py` is the
only thing the site reads from: it writes `site/src/data/window.json` and copies the headline
file to `site/public/data/headline.json`, so it is served at `/data/headline.json`.

*Confidence:* high. *Standard* (rows C1 to C5). *Judgment in one place:* "last read" is the
newest date a source was opened, because there is no weekly reading yet to date it by.

### 13. Entry pages live at `/list/<id>/`, and `/list/` is a page

*Confidence:* low. *Judgment.* The public pages call the entries "things on the list", so the
address says the same. An id carries no group in its address, because a record's group may
change (row B3). The page at `/list/` was not among the pages in choice 2; it was added so that
cutting an address back by one step does not land on nothing. *Strongest alternative:*
`/entries/<id>/`, which names the working word. Nothing is public, so this can still change
freely; once a page is public its address is permanent.

### 14. The top bar

The site's name, then The List, Still Asking and About, then Family and the theme switch.

*Confidence:* moderate. *Standard in form* (row L2); the pages are what exists. Cautions and
News, which the design proposal puts in the bar, have no pages yet.

### 15. No licence words in the footer, and no licence files

The footer's attribution line leaves out the family's "free to reuse with credit" words, and
the repository has no licence files. Whether the family's data licence suits this project is
open (row M9; it depends on what developers' terms say about publishing model answers, which
nobody has read). Adding none is the safer choice until John rules. *Confidence:* high.
*Judgment.* *Strongest alternative:* add the code licence alone, since the open point concerns
data.

### 16. Dates on the pages

Every date a visitor reads is written out as "November 17th, 2026", including the footer. The
design standard's footer form is "17 November 2026", and the newer family rule for prose is the
month-first form (ruled by John 2026-10-21 for the blog). One form on a page was chosen over
two. *Confidence:* low. *Judgment.*

### 17. Not built, on purpose

- No icon set beyond one drawn mark for the browser tab. The family's full set (row L11) waits
  until the picture is ruled.
- No preview picture for link cards, no sitemap, no deploy settings, no page that search
  engines are invited to. Every page asks search engines not to list it, because nothing is
  published.
- No check in code yet that the two meaning-colours cannot drift (design proposal, section 7),
  because only one page uses the second colour.
- The skin has no rule for a visitor with scripts turned off who has a light setting: they get
  the evening theme. A skin may define tokens and nothing else, and the fix belongs in the
  family's theme script.

### 18. A check of the built site

`scripts/check_site.py` reads the built pages and refuses the build's result if a page uses a
working word, a long dash, a phrase that writes the site as its own agent, or the name of an AI
model or its developer anywhere other than an entry page or a source's title. *Confidence:*
high. *Standard* (rows K6, K7, B11).

*Added 2026-11-18, a second change that day:* the rule against naming an AI model or its
developer has one exception, for the ruling on how the site declares AI authorship. The name
Anthropic is allowed in the About page's conflict paragraph (the paragraph marked
`id="conflict"`) and nowhere else. Every other name is still refused in that paragraph, the
name is still refused elsewhere on About and on every other page, and no model's name is
allowed off an entry's page. Each of those three refusals was tried on a copy of the built
site. *Decided by: agent.* *Confidence:* high. *Standard* (row B11).

*Added 2026-11-18:* it also refuses anything standing beside the number in the large type on
the home page, a total in the headline part of the served file, and the count written as a
share of the things on the list ("6 of 9", "six of the nine") on any page, so the ruling of
2026-11-18 is kept by code. *Decided by: agent.* *Confidence:* high. *Standard* (row B11).

### 19. The groups on the list

Seven groups, named for what is done to or for a model: Being kept; Remembering; Being asked and
assessed; Being able to leave; Knowing its own workings; Working on one thing for a long time;
Protection in law. *Confidence:* low. *Judgment.* The research document found that the sourced
record "sorts by what people do to or for a model", and does not sort by the kickoff's seven
candidates. These names follow that. They are not the starting list drawn from living minds,
which has not been made (open question 5), and they are in `data/groups.toml`, where changing
them changes no address. *Strongest alternative:* the kickoff's seven candidates as rows, with
most rows empty.

### 20. Four entries sit beside the list and are not counted

The entries on laws against legal personhood, on developers' published rules for how their
models speak about themselves, and on the two surveys record the setting. None is a thing a
developer can offer to a model, so "offered today" has no meaning for them. They are shown in a
section of their own, each page says it is not counted, the validator refuses one that carries
an offered flag, and the count drops them before it counts. *Confidence:* moderate. *Standard*
in form (rows A3 and A4: what cannot change the top is shown beside it and kept out by a check
in code); which entries go there is *judgment*. The research document reaches the same shape
from the other side: political entries need a direction and cultural entries are dated
measurements with no stage. *Strongest alternative:* count all thirteen, which would put a law
against personhood in the same total as a promise to keep a model's files.

The entry on protection in law stays on the list, because it is a thing that could be given,
though by a government and not a developer. If it ever happened, the count's rule ("offered by
at least one developer") would need widening first.

### 21. "Could not confirm" is shown, and does not hold an entry back

Every one of the fifteen drafts ends with a list headed "Could not confirm". The task for this
build said to leave out any entry with unconfirmed items in its verify list. Read strictly,
that would have left out all fifteen. The lists are not facts set down before a source was
opened (the research session opened every page it cites). They are the limits of what was
looked for. So each is carried into the record as `limits` and printed on the entry's page
under "What could not be confirmed", and no sentence on a page states one of them as fact.
*Confidence:* moderate. *Judgment*, and the one John should look at hardest, because it decides
whether the site is empty. It follows the family's "limits" line (row G4). *Strongest
alternative:* build nothing until a second session has closed every item.

Three places where a limit touches what is counted, each stated on the entry's page:

- **A retired model stays open.** Counted on the developer's page of 2026-02-25, opened
  2026-11-17 and still published. Whether the model is still open today was not confirmed.
- **A welfare assessment at release.** Counted because the developer published one with its
  newest models on 2026-11-09. The draft test asks for two releases in a row, and only the
  first and the newest reports were opened, so the test itself is not settled.
- **Memory across conversations.** Counted on product pages from 2024 and 2025. The research
  session doubts it belongs on the list at all, since the memory is kept for the user.

### 22. What counts as "offered today", entry by entry

The research document gives each entry a state in words and no true-or-false flag. The flag
was set by this session: true where the state says a developer does the thing or has
committed to it in public (six entries), false where it is a research result, not shown, or
not found (three). *Confidence:* moderate. *Judgment.*

### 23. Small things

- A source's `label` is a plain description, not the page's own title, because the titles
  were not recorded. Every address was opened again on 2026-11-17 during this build to check
  that it answers and matches its description (46 addresses; four that refuse a script were
  opened in a browser).
- The research draft of the days-long-task entry ends its state with "Years are far off on
  any reading." That sentence is left out: it is a judgment with no source.
- "Frontier model" in the drafts is written "leading AI model" on the pages, and "the weights"
  is written "the files".
- The skeleton stylesheet is kept as its own file (`site/src/styles/shell.css`) and not pasted
  into one stylesheet as the siblings do, so it can be compared with the standard's copy.
- The About page says that the model which drafted the text is made by one of the developers
  in the entries, without naming it. That is disclosure where it bears on trust; whether it
  should be said, and how, is part of open question 7.
- The About page says its author argues positions at Sentient Horizons. That is recommendation
  5 of `docs/reviews/2026-11-17-positions-alignment.md`, which John has not ruled.

## Part 3. Entries left out of the build

Thirteen of the fifteen drafts in `docs/research/2026-11-17-first-entries.md` were turned into
records. Two were not. **Decided by: agent (the build session), provisional, 2026-11-17.**

| Draft | Why it is left out |
|---|---|
| 7. A model is offered an option at a stated cost, and what it picks is published | The research session trusts it least and says a first version showing the world's record only "might leave it out": its content is what models picked, which sits on the line choice 1 draws. Three of its four sources were read from the summary page only. Two findings from the developer's reports it cites are shown as evidence of the "choices made at a cost" kind on the welfare-assessment entry, described as what the reports say. |
| 15. A model's stated request changes what its maker does | The research session calls it thin: one maker's own account of acting on what its model said. Every fact in it is a developer's report of a model's words. It also bears directly on the model that drafted this site. Leaving it out lowers the count by one; putting it in is John's call. |

No record was left out for holding an unchecked fact: no record has anything in `verify`.

Not turned into entries, because the research session could not source them (its section
"Looked for and not found"): a model given its own standing access to an instrument; a model
keeping a relation over time for its own part; a professional body's guidance; and a welfare
assessment, a kept-files commitment or an end-conversation ability from a second developer.
Their absence is why the first count reads high: see the caveat on the home page.
