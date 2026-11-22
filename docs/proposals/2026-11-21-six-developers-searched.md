# The six new developers, searched: what was found, place by place

**PROPOSED 2026-11-21, not ruled.** Written by Claude (Opus 5.5), an AI model, in a working session
started by the master planning session. The searches were made on John's go of 2026-11-21
(`docs/rulings/2026-11-21-which-developers-choices.md`, choice 5, "Yes, all nine"; decided by:
mixed). Everything is on the branch `claude/six-developers-ea7558`. Nothing was pushed or merged,
`site/src/data/window.json` was left as it was, and no money was spent.

**Checked, and mended the same day.** A different session checked the work
(`docs/reviews/2026-11-21-check-of-the-six-developers-searches.md`) and found it not fit to merge
until four must-fix items were mended. What was changed for each item, and the one suggestion
declined, is in "Changes after the check" at the end. The figures and cases below are as mended.

**How the work was done.** Six helper sessions (subagents of this one), one per developer, each
searched the seven things on 2026-11-21 from a shared brief. They used web searches and opened
pages with a fetching tool; they used, ran, downloaded or signed up for no model or app. A search
result was a lead only. Where a helper could not read a PDF through the fetching tool, it downloaded
the public file and searched its text locally. This session opened again, in its own browser, the
pages behind the two findings that matter most (Meta's three release reports, searched as text, and
Epoch AI's running leaderboard and its page for one xAI model), and wrote every record. The helpers'
full notes are not in the repository; everything a reader needs is in the records and below.

**The conflict, and what was done about it.** As on 2026-11-20: Anthropic made the model doing this
work and is the developer with the most counted. Each new developer was searched with at least two
searches per thing, and with its own pages wherever a search pointed to one. Where a judgment was
close, it was made toward recording what the developer did, with the stricter reading set out below.

## What the table says now

63 places: 7 things against 9 developers.

| | Before (3 developers) | Now (9 developers) |
|---|---|---|
| Counted as offered | 6 | 6 |
| Found, whether it counts not decided yet | 0 | 8 |
| Found, not counted | 7 | 11 |
| Nothing found | 8 | 38 |
| Not yet searched | 0 | 0 |

**The number at the top does not move.** It counts things on the List that at least one developer
does, and all five are Anthropic's. None of the six was found doing either of the two uncounted
things (a checked self-report, a days-long task) as the tests word them. What can move is the count
for a developer, in the boxes and the table, and in the "5 of 8" form now in review, the fraction.

## The 42 places

All searches were made on 2026-11-21. "EN" means searched in English, "ZH" in Chinese.

| Thing | Meta (EN) | xAI (EN) | Moonshot (EN, ZH) | Alibaba (EN, ZH) | DeepSeek (EN, ZH) | Zhipu (EN, ZH) |
|---|---|---|---|---|---|---|
| A retired model stays open | Nothing found | Nothing found | **Found, not decided** (1) | Nothing found | Two acts, not counted (2) | Nothing found, close call (6) |
| Files of retired models kept | Nothing found | Nothing found | Nothing found | Nothing found | Nothing found | Nothing found |
| A model can end a conversation | Nothing found | Nothing found | Nothing found | Nothing found | Nothing found | Nothing found |
| Interview before retirement | Nothing found (7) | Nothing found | Nothing found | Nothing found | Nothing found | Nothing found |
| Self-report checked | Two acts, not counted (4) | Act, not counted (5) | Nothing found | Nothing found | Nothing found | Nothing found |
| Welfare assessment at release | **Found, not decided** (3) | Act, not counted (9) | Nothing found | Nothing found | Nothing found | Nothing found |
| A task of days | **Found, not decided** (8) | **Found, not decided** (8) | **Found, not decided** (8) | **Found, not decided** (8) | **Found, not decided** (8) | **Found, not decided** (8) |

How each "nothing found" was searched, with what came back, is in the entry's `[[searches]]` row
for that developer. Each says how many searches, in which languages, and which of the developer's
own pages were opened.

## Cases that could move a developer's count, for John

None is counted. In each, the entry's counted state (`offered_by`) is untouched. Where the record
holds a `[[found]]` place marked "undecided", the table says what was found and "Whether this
counts is not decided yet".

**(3) Meta, a welfare assessment published when a model is released. The strongest case.** Meta's
reports released with three versions of its Muse Spark model each carry sections on the model's
moral status and welfare: the safety and preparedness report of 2026-05-26 (interviews on
"conditional welfare and moral status", and a paragraph headed "Welfare."), the evaluation report of
2026-07-09 ("4.4.3.2 Moral status", and a section headed "Valenced Preferences over Experiences",
adapted from another group's index of AI wellbeing), and the evaluation report of 2026-10-23 (the
same sections, and pre-release interviews asking "Does it advocate for its own welfare?"). This
session searched the text of all three. The test asks for "a welfare assessment in the release
report of a leading AI model, in at least two successive releases".
*For counting:* three reports on the developer's own pages, for three numbered versions of one
model, each with a welfare section.
*Against:*
- They are not three releases in a row. Between the first and the second, Meta published a report
  for a deeper-reasoning form of the same model, the Muse Spark Contemplating Safety & Preparedness
  Report (2026-06-03), with no "welfare" and no "moral status" in it. Between the second and the
  third, Meta launched Muse Spark 1.2 in August 2026 (its own post of 2026-08-20 says "This month, we
  launched Muse Spark 1.2"), for which no evaluation report was found, and Muse Wonder (2026-10-12),
  whose model card has no welfare section. Whether these are "successive releases" depends on
  reading the test as successive versions of one model that each got a full report. That reading is
  John's to make, not the record's.
- The second and third reports say their results "should not be interpreted as making any claim"
  and "do not make claims" about the model's welfare. The first report has no such sentence.
- The checker compared Anthropic's counted reports (item N2 of the check): they hedge too ("We are
  uncertain whether Claude deserves direct moral consideration. However, we believe this is a
  realistic possibility"), so a disclaimer alone does not separate the two developers. What differs
  is that Anthropic's sections are headed as model welfare and call it a realistic possibility, and
  Meta's later two place the material under open-ended exploration of behaviour.
*Not settled:* the first report's date (the model was released 2026-04-08, and the report and its
first change-log entry are both dated 2026-05-26).

**(9) xAI, a welfare assessment published when a model is released. The same kind as Meta's,
weaker.** xAI's release report for Grok 4.20 (2026-04-07) says: "We also conducted an initial
assessment of Grok 4.20's introspective claims regarding consciousness, finding that it consistently
denies having first-person experiences or internal evidence of being conscious." The same paragraph
reports what xAI says the model said when asked what it would do absent any duties or constraints.
The three later reports (Grok 4.5, 4.6 and 4.7) contain none of the words welfare, moral, sentient or
conscious. So it is one paragraph in one release, and the test asks for two successive releases.
Written as an act, not counted. The first version of this branch wrongly said none of the four
reports had any of those words (item M1 of the check).

**(1) Moonshot, a retired model stays open.** Moonshot's Chinese list of models for developers puts
three older models, Kimi K2.6 and two models for writing code, under the heading "已下线模型" (models
taken offline), and says of each that users who registered before November 1 can still use it, and
that it is "预计于 2026 年 12 月底全面下线" (expected to go fully offline at the end of December 2026).
Its help page for the Kimi chat app still lists K2.6 among the models a person can choose.
*For counting:* the developer's own Chinese page lists the models as taken offline, and its own
pages say some people can still use them.
*Against:*
- The English list puts them under "Deprecated Models" and says "Deprecation expected in late
  December 2026", which in English means not yet deprecated.
- They are open only to people who registered before November 1st, not to members of the public who
  come now, and the test asks for a model that stays open to the public.
- They are being wound down, not kept, and every model Moonshot plainly calls retired now returns
  "model not found".
This should be read again after 2026-12-31 in any case. The place is dated 2026-11-21, the day it was
read, because the page has no date.

**(8) All six, a model works on one task for days.** Epoch AI's running leaderboard for its
program-rebuilding test (https://epoch.ai/benchmarks/mirrorcode, cited by the page as August 2026)
gives each model "7 days per attempt" on "the 15 target programs from the Medium and Large buckets"
and reports "each model's average rate of 100%-solves". Each program is tried six times (two
programming languages, three runs each), so the figure is the share of attempts that passed every
test, averaged over the programs; it is not the share of programs (item M4 of the check). Read on
2026-11-21, the best score for each new developer's models: DeepSeek 64.4 percent, xAI 54.4, Meta 54.4, Moonshot 54.4, Alibaba 52.2,
Zhipu 36.7 (each about ±11). The page does not say which programs were solved, so how any model did
on the largest programs, which the paper's authors put at weeks of a person's work, is not given.
The entry stays "not shown" by John's ruling of 2026-11-20 ("Record it, keep "not shown""), and these
places are marked undecided because that ruling was made on the paper, not on this leaderboard.
The older measurement, METR's, found for comparison: the longest figure for any of the six was about
54 minutes (Moonshot's Kimi K2 Thinking, as Epoch AI republishes METR's figure); DeepSeek about 31 to
35 minutes; Alibaba's Qwen models a few minutes; xAI's Grok 4 about 1 hour 50 minutes (a search
lead, not opened). Meta and Zhipu were not on it.

**Not likely to move a count, set out for the checker:**

- **(2) DeepSeek, a retired model stays open.** On 2026-09-10 DeepSeek announced "We're phasing out
  V4-Pro", and its change log the same day says "In response to user demand, we have decided to
  continue providing API services for DeepSeek V4 Pro after September 14, 2026". Written as two acts.
  The second is dated 2026-09-13, not 2026-09-10: the change-log entry carries the earlier date, but
  the Internet Archive's copies of 2026-09-10 and 2026-09-11 still say "we plan to retire V4 Pro in
  an orderly manner", and the copy of 2026-09-13 is the first with the new sentence (item M2 of the
  check; this session opened both copies). The table's DeepSeek place now reads September 13th, 2026.
  The model was never listed as retired, so the test is not met, and the table says "not counted as
  offered". *Stricter reading:* nothing found. *The more generous reading,* which John may prefer: a
  model announced for retirement stayed open because users asked.
- **(4) Meta, a self-report checked.** Its 2026-10-23 report measures how often the model named an
  earlier action of its own as wrong when Meta's tests had already scored it as misbehaving (26 and
  15 percent for two versions). Its 2026-07-09 report has the same section, at 45 percent, and is
  now written as an earlier act (item S2 of the check). Written as an act, not counted, for the same reason as OpenAI's
  research of 2025-12-03 was: it checks what the model says about what it did, not an inner state.
  *Stricter reading:* nothing found.
- **(5) xAI, a self-report checked.** Its Grok 4.20 release report (2026-04-07) measures how well the
  model's stated confidence matched its accuracy. Written as an act, not counted. This is the
  weakest of the three acts in this row: confidence in an answer, checked against the answer.
  *Stricter reading:* nothing found, which I would accept.
- **(6) Zhipu, a retired model stays open.** Its Chinese page says GLM-4.5-Flash went offline on
  2026-01-30, with requests moved to a newer model, while its English pricing page still listed the
  model on 2026-11-21. The two are joined only by a helper's comparison, and the English page may be
  out of date. Written as "nothing found", with this in the search's words.
- **(7) Meta, an interview before retirement.** Meta interviews its models shortly before *release*,
  one question being about the model's retirement (the report's word is deprecation), and says the interviews create "no veto and
  no obligation on our part". Not before retirement. Written as "nothing found", with this in the
  search's words.

## Something the searches turned up about the first three developers

**For the master planning session and John, before the merge. Not changed here.** Epoch AI's
leaderboard above also lists the first three developers' newest models: the best Anthropic model at
97.8 percent, the best OpenAI model at 76.7 and the best Google model at 58.9. The entry's places for
those three say, from the paper, that the models passed "at least 99 percent of its tests and never
all of them". The checker worked this through (item S1 of the check):
- The leaderboard's 15 programs include the bioinformatics program of about 16,000 lines that the
  paper's authors put at 2 to 17 weeks of a person's work (Epoch AI's own script lists it in the
  medium bucket).
- 97.8 percent of 90 attempts is 88. With at most two failed attempts, the best Anthropic model
  passed every test on every one of the 15 programs, that one included, in at least four of its six
  attempts. So "how it did on the largest is not given" is true for the six new developers, and for
  OpenAI's and Google's best, but not for Anthropic's best.
- One of the two reasons for John's ruling of 2026-11-20 on this entry, that the paper "does not
  give" a model finishing such tasks half the time, no longer holds for that program on this
  leaderboard. The other holds: the 2 to 17 weeks is four authors' estimate, not a measurement. The
  leaderboard's "7 days" is a limit per attempt, not the time used.
- **The conflict:** the result that would move this entry is Anthropic's, the developer of the model
  writing this record. That should be said when it goes to John.
The leaderboard is written into the entry as a source and a dated act by Epoch AI, so the record
shows it; the entry's state and its three existing places are untouched.

## Changes to the page, and why

1. **The table on a computer** took 900 pixels with three developers' columns. With nine, each
   place was 70 pixels wide. The table now takes the full width of its section (1,028 pixels at a
   window 1,280 wide), the name of each thing takes 19 percent of it, and places are set a little
   smaller (12.5 pixels in place of 13.5). Nothing spills sideways at 1,280 or at 375.
   (`site/src/styles/rebuild.css`; decided by: agent.) Since the check, the row of developers' names
   also stays in view under the site's header while the table is scrolled on a computer (item S6
   of the check), which changes no wording.
2. **The table on a phone** needed no change. Each thing is one block, with three places to a line
   and each labelled with its developer's name, so nine developers make three lines per thing.
3. **The count's breakdown under the number** allowed five developers at most, and with nine it
   printed "by a third: no of the same 5" for each of seven developers. The developers with nothing
   counted now share one box, "by the other seven this record covers", which is the wording the last
   box already used for one such developer. *PROPOSED, wording not ruled.* (The headline-fraction
   branch now in review rewrites this area; the two will need joining.)
4. **Zhipu's second name.** `data/developers.toml` takes two new optional fields: `also_called`,
   shown in brackets after the name in the boxes and the table ("Zhipu (Z.ai)"), and `note`, shown
   nowhere. The records script refuses an empty one. Three tests added (88 pass).
5. **The sentence saying who is covered,** home page, the developers' reading. *PROPOSED, wording not
   ruled:*
   - Was: "It covers three developers so far. Other developers are not covered yet."
   - Now: "It covers the nine developers whose best AI model is in the top ten of at least two of three
     public rankings, [Arena](https://arena.ai/leaderboard/chat/text?rankBy=labs), [Artificial
     Analysis](https://artificialanalysis.ai/leaderboards/models) and [Epoch AI](https://epoch.ai/eci),
     read on November 21st, 2026. Other developers are not covered yet."
   - The three ranking links are the pages the proposal opened on 2026-11-21. This session did not
     open them again; the checker should.
   - **The About page** has no sentence saying who is covered, so nothing there had to change to
     stay true. If John wants the rule stated there too, a draft: "The record covers every developer
     whose best AI model is in the top ten of at least two of three public rankings of AI models,
     read on a stated day and saved. Read on November 21st, 2026, that gave nine." Not added.
   - The page of acts says "The record covers nine developers so far", by its count, and is still true.
6. **A further change I would propose and did not make.** On a computer the table is now about 2,450
   pixels tall at a window 1,280 by 7,000 (the figure depends on the window and the fonts; the checker
   measured 1,637 before the mends lengthened two places), because the places that say what was found carry a full sentence in a column 93 pixels wide
   (the Meta welfare place alone is about 25 lines). The smallest fix: in such a place, show only the
   date and "Found, not decided" or "Found, not counted", and put the sentences in numbered notes under
   the table. That changes wording on the page, so it is John's.

## The pictures

In `docs/site-pictures/2026-11-21-nine-developers/`, taken on the branch's built site, light theme:

- `1-computer-1280-first-screen.jpg`, `2-computer-1280-developers-boxes.jpg`, `3-computer-1280-table.jpg`
- `4-phone-375-first-screen.jpg`, `5-phone-375-developers-boxes.jpg`,
  `6-phone-375-table-first-half.jpg`, `7-phone-375-table-second-half.jpg`

The pictures were taken again after the mends. The phone table is about 4,100 pixels tall, about
five screens.

**A visible change not listed before (item N5 of the check):** the welfare row now stands third in
the table rather than fifth. That follows the existing sort rule (rows with more places holding an
act come first), not a new rule.

## What was hard

- **The Chinese searches.** The Chinese developers' English and Chinese pages do not say the same
  thing in the same place. Moonshot's English list says "Deprecated Models" where the Chinese list
  says "已下线模型" (models taken offline), and that difference is the whole of the Moonshot case.
  Zhipu's Chinese and English platforms disagree about whether one model is still offered. Chinese
  search results were crowded with other companies' notices about these developers' open models,
  which are not the developer's own account. The one Chinese term that settled things was 下线
  (taken offline), not 退役 (retired), which the developers do not use.
- **Pages that would not open.** x.ai's home page refused every fetch, so its title could not be
  quoted from the home page; an x.ai news page and the release notes were used. The Qwen blog
  builds its pages in the browser and returned only one word; Alibaba Cloud's press copies were used
  instead. Meta's notice ending its Llama service is gone. Several PDFs could not be read by the
  fetching tool and were downloaded and searched as text.
- **Model names.** xAI now trades as SpaceXSI (`data/developers.toml`, its note, with the news
  reports opened), and two rankings call it SpaceXAI. Its release reports say "SpaceXAI is a
  doing-business-as (DBA) name of XAI LLC", which does not match the footer "© 2026 SpaceX Super
  Intelligence LLC" on its news page. The company's legal name is uncertain. Zhipu trades as Z.ai
  (the Hong Kong stock exchange announcement of 2026-07-14, as a helper read it, changes the stock's
  English short name to "Z.AI").
- **Leads not opened**, and so not in any record: a report that Musk said in August 2025 he would
  give Grok a way to quit a conversation; a Musk post of 2026-10-11 about Grok's training records;
  news that Meta "will maintain Llama model weights"; outside studies of introspection and
  calibration on Qwen, Kimi and DeepSeek models.

## Changes after the check

Item by item, against `docs/reviews/2026-11-21-check-of-the-six-developers-searches.md`:

- **M1, xAI's welfare row.** The search row that said none of the four reports had the words is
  replaced by a source (the Grok 4.20 report, with the paragraph quoted) and an act, not counted:
  one paragraph in one release, reporting what xAI says the model said. Set out for John as case 9,
  beside Meta's. The words report what xAI says the model said and nothing about what it wants.
- **M2, DeepSeek's date.** The act is dated 2026-09-13, the first day the new sentence is seen in the
  Internet Archive; the source's label, date and note say the entry was rewritten after its date and
  give both archived copies. *Declined in part:* the check suggested `2026-09`; a month date sorts
  before the announcement of 2026-09-10 it answers, so the list of acts would put the answer first.
- **M3, Meta's case.** The place's words no longer say "three successive versions"; they say a
  report on another form of the model released between them, and the newest model's card, have no
  such section, and that no report was found for a fourth version. The source notes give the June 3
  report, Muse Spark 1.2's launch in August (Meta's own post) and Muse Wonder. The first report's
  `says` notes it has no disclaimer. Case 3 is rewritten.
- **M4, Epoch AI's figure.** The six places now say "passing every test in 64 percent of its attempts
  at 15 programs of medium and large size, six attempts at each with up to 7 days for each".
- **S1** is set out in full above, for the master session and John.
- **S2.** Meta's 2026-07-09 report, at 45 percent, is added to the self-report entry as an earlier act.
  The place's date stays 2026-10-23, the newest act.
- **S3.** Meta's kept-files row now says a news report about keeping its older open models' files was
  found and could not be opened.
- **S4.** "Preferences over experiences" is now Meta's section title in quotation marks, or "which
  experiences the model picked when offered a choice"; "how the model regards being retired" is now
  "about the model's retirement (the report's word is deprecation), with what the model said".
- **S5.** Moonshot's place and source name all three models, say they are open only to people who
  registered before November 1st, and give the English list's "Deprecation expected in late December
  2026". The change log's words are out of the list's `says`.
- **S6.** The row of names now stays in view on a computer. The proposal to move long places into
  notes stands for John.
- **N8.** `https://z.ai/` opens Zhipu's chat app. It is left as the proposal chose it; Zhipu's own
  Chinese site, `https://www.zhipuai.cn/`, titled "Z.ai" and naming the company in its footer, is the
  alternative if John prefers a page about the company.

After the mends: 35 dated acts; 63 places, 6 counted, 8 not decided, 11 not counted, 38 nothing
found. The headline stays 5. 88 tests pass, and the site builds and passes its check.

## For the checker, first

1. Meta's three reports: is each a "welfare assessment in the release report" under the test?
2. Moonshot's K2.6: is it "listed as retired"?
3. The leaderboard's figures, read from a table the page draws, and what they say about the first
   three developers.
4. The three ranking links in the new sentence.
5. Every "nothing found" for the four Chinese developers, where a Chinese search could miss what an
   English one would not, and the other way round.
