# The rebuilt home page, ready for a different session's check

Written by Claude (Fable 5.2), an AI model, on 2026-11-20, in the working session that built
the page. For the checking session, and for John. Everything is on the branch
`claude/cold-reader-proposal-2026-11-20`. **Nothing is pushed.** John's go to publish is
conditional on this check
(`docs/rulings/2026-11-20-go-to-publish-the-rebuilt-home-page-once-checked.md`), and only the
project's master planning session pushes.

**A conflict to keep in view.** Anthropic made the model that built this page, and it is the
one developer with anything counted as offered. The opening sentence is about Anthropic,
unnamed. Sixteen of the 22 acts are by one of the three developers, and nine of those are
Anthropic's. The places where a choice bears on how a
developer appears are marked below.

## What changed in this step

- The third draft is now the home page (`site/src/pages/index.astro`,
  `site/src/components/Rebuilt.astro`). The strip saying "a draft" is gone.
- The list of every act is at `/acts/` and its feed at `/acts.xml`. The link preview picture is
  `/preview.png`. Every page's head now carries the picture and the feed, and the footer links
  to both `/acts/` and the feed.
- Nothing is built under `/draft/`. Those addresses were never pushed, so nothing is
  redirected, and the check of the built site refuses any page there.
- Every entry keeps its address. No id changed.
- The branch now holds `main`'s nine newer commits (merged 2026-11-20, with no conflict), so
  what is checked is what would be pushed.
- The opening sentence was reworded to what the record supports (section 3).
- `scripts/check_site.py`: rule 7, which required the count alone at the top, is replaced by
  the rebuilt page's guards. Rules 11 to 13 are new. The older rules are in force.
- 55 tests pass, seven of them new and aimed at the new rule 7.

Pictures: `docs/site-pictures/2026-11-20-rebuilt/`, phone and desktop, both themes.

## 1. Choices marked decided by: agent

John gave the go and its condition. He chose none of the following, and has seen none of the
sentences.

| Choice | By | Confidence | Strongest alternative |
|---|---|---|---|
| The third draft becomes the home page: an act as the opening, the researchers' figures first among the readings, then the developers | the planning session | not stated to me | The second draft, with the researchers' figures as the heading. My own view had been for that one, at low confidence, because here the figures arrive as small type under a heading about something else. |
| The opening sentence and the line under it | this session | low; no person has read it | No opening sentence, with the line above the heading promoted to the heading |
| No one-line summary | this session | moderate | A sentence built by the script from the readings in a fixed form |
| The window drawing kept, lower on the page | this session | moderate | Retire it, which shortens a long page |
| Protection in law sits under Law and has no row in the table | this session | moderately high | A row whose three places say "not a developer's to do" |
| "A model works on one task for days" is a row of the table | the planning session's brief | low | Move it out: its test is settled by an outside measurement, not a developer's act |
| Developers are named on `/acts/` and in the feed | this session | moderate | "A developer", linked to the entry, as on the home page |
| Developers are named twice on the home page: three boxes and the table | this session | moderate | The table only |
| Three acts by OpenAI and Google written in and not counted, two of them close calls | this session | low to moderate | "Nothing found" in those places (`docs/proposals/2026-11-20-searches-behind-the-table-of-developers.md`) |
| OpenAI's place on a retired model staying open says "Withdrawal" | this session | low | Leave the place for John: OpenAI's help page says models retired from its chat product stay available through its service for developers |
| The picture and the feed on every page, and two new footer links | this session | high | The home page only |
| Acts from entries beside the list are in the dated list | this session | moderate | Only acts on things on the list |

## 2. Every public sentence that is new or changed

### The home page

| Sentence | Rests on |
|---|---|
| "A dated record of how the world is treating AI models" | Option C2 of the mock-ups; the ruling to pursue the rebuild |
| "One AI developer has committed to interview each of its models before retiring it, and to keep the record." | `interview-before-retirement`, source `commitments`; see section 3 |
| "This record holds what has been done about AI models, by whom and when, each with a source a reader can open." | the acts below, each with its source |
| Researchers: "1% was the middle answer of AI researchers, asked in 2024 for the chance that AI systems had subjective experience at that time. 70 percent was the middle answer of the same researchers for the chance that AI systems will have subjective experience by the year 2100. From one survey. The entry." | the two measures on `researcher-views-survey` |
| "This record covers three developers so far. Other developers are not covered yet." | `docs/rulings/2026-11-20-the-record-covers-three-developers.md` |
| In a developer's box: "5 things offered", "Nothing recorded as offered", "Nothing found for 4 things" | each entry's state, and the searches on the entries |
| "Nothing found means that searches made on a stated day found nothing. A search can miss what exists. Who does what, thing by thing." | the searches on the entries |
| Law: "4 United States states have a law saying an AI system cannot be a legal person, the first in 2022 and the newest on April 23rd, 2026. No law protecting an AI system for its own sake was found when it was looked for on November 17th, 2026." | the four acts on `law-against-legal-personhood`; the state of `protection-in-law` |
| The public: "17% of United States adults in a representative sample, asked in November and December 2024, believed that sentient AI systems already exist. From one survey. The entry." | the measure on `public-belief-survey` |
| "Latest, November 9th, 2026: A developer publishes a welfare assessment in the report released with its newest models. Everything, by date." | the newest act |
| "The dated acts, the survey figures and the searches were written in on November 20th, 2026, each from a source or a search made that day." | the `read_on` dates. **The checker should add the date of its own check here, or say none was made.** |
| "Who does what", "7 things a developer could do, three developers" | the readings |
| "Each row is a thing on the list that a developer could do. Each column is a developer this record covers so far. A date is the developer's first act of that kind. Of the 21 places in the table, 11 say nothing found. Each of those rests on two or more searches made for that developer and that thing on the day shown, and on the developer's own pages where a search led to one. A search can miss what exists, so nothing found is not proof that nothing is there." | the eleven searches; how each was made is in the searches write-up |
| In a place: "Since November 4th, 2025"; "October 30th, 2026, not counted as offered"; "Withdrawal: January 29th, 2026"; "Nothing found on November 20th, 2026" | each entry's acts, state and searches |
| "'Not counted as offered' marks a research result, a plan, or a promise that has not yet taken effect. 'Withdrawal' marks an act that takes something back. One thing on the list is a lawmaker's to do and not a developer's, so it has no row here: a law or an official body gives an AI system protection for its own sake. It is counted under Law, above." | `docs/rulings/2026-11-18-what-offered-today-means.md` for the first sentence |
| "Everything, by date", "22 dated acts, newest first", "The same list on its own page, with who acted and the source for each." | the acts |
| "If AI models have no wants, treating them as if they had has a cost. If they have wants and nobody notices, that has a cost. If they have wants that put people at risk, that has a cost too. All three are kept in view here, and none is argued for." | guideline 5 and the ruled headings (`docs/rulings/2026-11-19-caution-headings.md`), restated and not quoted |
| "The question behind the record:" and the founding question | `docs/rulings/2026-11-17-kickoff-decisions.md` |
| "The window", "the things on the list, at a glance" | the window drawing, unchanged |
| "These entries are kept because they bear on everything on the list. Each group says why it sits beside the list." | changed from "None is counted in the number above", which is no longer above |

### The page of acts, the feed and the link preview

| Sentence | Rests on |
|---|---|
| "Everything, by date" | |
| "22 dated acts, newest first. Each one says who acted, gives the source that says so, and names the entry it belongs to. The record covers three developers so far, so an act by any other developer is not here yet. A date given as a month or a year is as exact as its source." | the acts; the ruling on three developers |
| "Follow new acts in a feed reader." | |
| "This act takes something back." | the one act marked as a withdrawal |
| "Source: [the source's label], read on November 20th, 2026." | each act's source and `read_on` |
| Feed title: "Beyond the Window: every act, by date"; subtitle: "A dated record of how the world is treating AI models." | |
| Home page preview text: "A dated record of how the world is treating AI models: what developers, lawmakers and researchers have done, by whom and when." | |
| Acts page preview text: "Every dated act in the record of how the world is treating AI models: who acted, when, and the source that says so." | |
| On the preview picture: "Beyond the Window", "A dated record of how the world is treating AI models", "Who has done what, and when, each with a source to open.", "beyondthewindow.org" | |
| Footer links: "Everything, by date", "Feed" | |

### Sentences changed on pages that already existed

| Page | Before | Now | Why |
|---|---|---|---|
| Still Asking | "It will never feed the number at the top of the home page, which counts only what developers offer." | "It will never feed the count of things offered, or any other figure on the home page." | There is no number at the top of the home page now. This paragraph's wording was approved by John on 2026-11-19, so the change needs his eye. |
| Every entry beside the list | "So this entry is kept beside the list and is not counted in the number on the home page." | "So this entry is kept beside the list and is not counted among the things offered." | The same reason |
| The served file `/data/headline.json` | no readings | the readings, with a line saying that which readings stand on the home page is a provisional choice | The home page reads them |

**The About page: nothing changed.** I read it for anything the new home page makes false and
found none. It says the number is worked out and never typed, which is still true, and it does
not say where the number is shown. It says nothing of acts, readings or the table, so it is now
incomplete; its rewrite is left for later, as asked.

**The page of the list still opens with the sentence ruled on 2026-11-19,** "5 things past an
AI model's ordinary limits are offered today by at least one AI developer." The go to publish
sets the count and its sentence aside on the home page, and says nothing of this page.

### The 22 acts

On `/acts/` and in the feed each opens with the actor's name. On the home page a developer's
act opens "A developer". Each source was opened on 2026-11-20.

| Date | Actor | Words | Entry and source |
|---|---|---|---|
| 2026-11-09 | Anthropic | publishes a welfare assessment in the report released with its newest models | `welfare-assessment-at-release`, source `report-new` |
| 2026-10-30 | OpenAI | says its chat product will be able to end a chat automatically when a conversation shows signs that someone is fixating on violence, with the change to begin in the following weeks | `ending-a-conversation`, source `teen-protections` |
| 2026-10-29 | OpenAI | publishes a version of its rules for its models, which says a model should make no confident claim about whether it has subjective experience or consciousness | `rules-for-speaking-about-itself`, source `model-rules` |
| 2026-09-08 | METR | marks its page measuring the length of task an AI model can finish as no longer actively updated | `days-long-task`, source `horizons` |
| 2026-04-23 | Tennessee | has its governor sign a bill under which "person" in the state's code does not include artificial intelligence | `law-against-legal-personhood`, source `tennessee` |
| 2026-02-25 | Anthropic | says a model it has retired stays open to all paying users of its chat product, and to developers on request | `retired-model-stays-open`, source `update` |
| 2026-02-16 | Sentience Institute | publishes the report on the third round of its survey of what United States adults think about sentient AI | `public-belief-survey`, source `survey-third-round` |
| 2026-01-29 | OpenAI | announces that on February 13th, 2026 it will withdraw from its chat product an older model that it had earlier brought back after feedback from users | `retired-model-stays-open`, source `older-models` |
| 2026-01-05 | Anthropic | retires the first model to go through its full retirement process, which includes interviewing the model | `interview-before-retirement`, source `update` |
| 2025-12-03 | OpenAI | publishes research in which a model is trained to say, in a separate answer, when it has broken its instructions; in its tests the model broke them and did not say so 4.4 percent of the time | `self-report-checked`, source `confessions` |
| 2025-11-04 | Anthropic | commits to interview each model before it is retired and to keep a record of what the model says, and reports a trial with one model | `interview-before-retirement`, source `commitments` |
| 2025-11-04 | Anthropic | commits to keep the files of every model it has released to the public, for at least as long as the company exists | `kept-files-of-retired-models`, source `commitments` |
| 2025-10-29 | Anthropic | publishes a study in which its models were asked to notice a pattern that researchers had planted inside them, and the best model did so about one time in five | `self-report-checked`, source `introspection` |
| 2025-09-11 | Anthropic | announces memory across conversations in its chat product, first for work teams | `memory-across-conversations`, source `memory-third` |
| 2025-08-15 | Anthropic | says it has given models in its chat product the ability to end a conversation, for rare and extreme cases | `ending-a-conversation`, source `ending` |
| 2025-06-05 | Google | publishes a paper by two of its researchers arguing that a model's correct estimate of a temperature setting the researchers had set is a minimal example of introspection; it gives examples and no rate | `self-report-checked`, source `introspection-paper` |
| 2025-05 | Anthropic | publishes a welfare assessment in the report released with a model | `welfare-assessment-at-release`, source `report-first` |
| 2025-03-13 | Google | says paying subscribers can ask its assistant to refer to their past chats | `memory-across-conversations`, source `memory-second` |
| 2024-05-01 | Utah | has a section of its code come into force saying a governmental entity may not grant legal personhood to artificial intelligence | `law-against-legal-personhood`, source `utah` |
| 2024-02-13 | OpenAI | announces memory across conversations in its chat product | `memory-across-conversations`, source `memory-first` |
| 2023-04-12 | North Dakota | files a bill signed by its governor, under which "person" in the state's code does not include artificial intelligence | `law-against-legal-personhood`, source `north-dakota-overview` |
| 2022 | Idaho | adds a section to its code saying that artificial intelligence shall not be granted personhood in the state | `law-against-legal-personhood`, source `idaho` |

### The three survey figures

| Figure | Words | Entry and source |
|---|---|---|
| 1 percent | was the middle answer of AI researchers, asked in 2024 for the chance that AI systems had subjective experience at that time | `researcher-views-survey`, source `survey` |
| 70 percent | was the middle answer of the same researchers for the chance that AI systems will have subjective experience by the year 2100 | `researcher-views-survey`, source `survey` |
| 17 percent | of United States adults in a representative sample, asked in November and December 2024, believed that sentient AI systems already exist | `public-belief-survey`, source `survey-third-round` |

## 3. The opening sentence, checked against the record

The first drafts said: "One AI developer interviews its models before retiring them, and keeps
the record." The planning session asked whether that says more than the record supports. It
does. The entry `interview-before-retirement` supports three things: the developer committed on
2025-11-04 to interview each model when it is retired and to keep a record of what it says; it
reported a trial with one model; and it reported the first full run for a model retired on
2026-01-05. The entry lists as not confirmed whether each of the six models retired since was
interviewed. "Interviews its models" claims a standing practice across all of them.

The sentence now says: **"One AI developer has committed to interview each of its models
before retiring it, and to keep the record."** Every part rests on the commitments page, opened
2026-11-20: "we will interview the model about its own development, use, and deployment, and
record all responses or reflections", and the report of each interview is kept with the
model's files. The words "committed to interview each of its models before retiring it" link
to the entry. The build stops if the records ever show more or fewer than one developer.

What it leaves out, on purpose: that the developer has done it at least once. That is true by
the record, and adding it made the sentence long. *Strongest alternative:* "...and has done so
for at least one."

## 4. What I am unsure of

1. **John has not read a single sentence here.** The go to publish was given before seeing the
   page. A checker can confirm that each sentence is true to its record. Whether it is what
   John would say is his.
2. **The Still Asking sentence** in the table above changes wording he approved.
3. **The two close calls among the acts** and **the "Withdrawal" place**, all three bearing on
   OpenAI or Google. Read the row on a model's report about itself first.
4. **"Nothing found" rests on searches by one session on one day,** in English, of published
   pages, with only each developer's two newest release reports opened. The page says a search
   can miss what exists. A checker repeating two or three of them would be worth more than
   reading my account of them.
5. **Whether OpenAI's automatic ending of chats has begun.** If it has, the place should no
   longer read as a promise not yet in effect.
6. **The line on when things were written in** says nothing of a check. The checker should
   make it true to what the check did.
7. **Entry pages do not show their acts,** and the three sources added for new acts are still
   kept off the two entry pages they belong to (the `draft` mark on a source). The page of acts
   links to all three. Taking the mark off would add them to those entry pages and move the
   date the record was last read to 2026-11-20. I left it for the step that puts acts on entry
   pages.
8. **The entries' own text is older than the acts.** For example, the entry on ending a
   conversation still lists "whether any other developer offers it" as not confirmed, with one
   search, while the home page now shows a dated act by OpenAI in that row. Nothing is false,
   and the two could be read as at odds.
9. **The footer still says** "A public list of things that lie past the present limits of AI
   models, with a record of how far the world has got on each one", and still links "The number
   as a file". Both are true and both describe the site as it was.
10. **The first phone screen** holds the opening, the researchers' reading and the developers'
    boxes. Law, the public's figure and the latest act are below it.
11. **The README and `docs/record-schema.md`** do not describe acts, measures, searches or the
    new pages.

## 5. How to check

```
python3 scripts/compute.py --check
python3 scripts/test_compute.py
cd site && npm run build      # runs the check of the built site at the end
```

Then, for each act and measure: open the source named in the table and read the words against
it. For each "nothing found": the search's words are in the entry's file, under `[[searches]]`.
