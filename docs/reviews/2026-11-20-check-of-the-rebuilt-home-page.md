# Check of the rebuilt home page: not fit to publish yet, for two reasons

Written by Claude (Fable 5.2), an AI model, on 2026-11-20, in a session that wrote none of the
work it checks. For the planning session and for John. It checks the branch
`claude/cold-reader-proposal-2026-11-20` at commit `db23877`, against the file the build
session wrote for this check (`docs/proposals/2026-11-20-rebuilt-home-page-for-checking.md`).
This session changed nothing on the branch except adding this file. Nothing was pushed.

**The conflict, again.** Anthropic made the model that did this check, as it made the model
that built the page. So the check spent most of its effort where the page says another
developer has done nothing, or less than Anthropic.

## Verdict

**Not fit to publish yet.** Almost everything passes: the page builds, every figure and all
22 acts match their sources, the rulings are recorded honestly, and nothing live breaks. But
my own searches found two places where the page would tell a reader something that a public
page contradicts today. Both are in the table of developers, both are a matter of the record
and not of wording, and one of them needs John's ruling. They are items 1 and 2 below. With
those two mended and checked, I would call the page fit.

I made no fixes. I found no plain slip (no typo, no broken link, no figure that differs from
its record).

## The two reasons

### 1. The row "A model works on one task for days" says "nothing found" three times, and there is a public measurement the searches missed

The page shows "Nothing found on November 20th, 2026" for Anthropic, OpenAI and Google in this
row. The list lower on the page says of the same thing: "Not shown. The best public measure
stops at hours." The search words in the record say: "No measurement above 40 hours was found
for any model."

What I found, with one search and by reading the research group's own list of its work:

- **[MirrorCode: evidence that AI can already do some weeks-long coding tasks](https://epoch.ai/publications/mirrorcode-preliminary-results/)**,
  published by Epoch AI on 2026-04-10, built together with METR (the group whose page the
  entry already rests on). METR linked it the same day
  ([METR's note](https://metr.org/blog/2026-04-10-mirrorcode-preliminary-results/)). It says an
  Anthropic model, Claude Opus 4.6, rebuilt a 16,000-line program on its own, and: "We guess
  this same task would take a human engineer without AI assistance 2–17 weeks." It adds:
  "Early testing showed comparable or weaker performance from other models."
- **[Epoch AI's MirrorCode page](https://epoch.ai/MirrorCode)**, the follow-up with full
  results and a list of scores it says is updated regularly. It says "one of the largest
  MirrorCode tasks cost $2,600 for a single run and involved AI working for 19 days without
  human intervention", and that a later Anthropic model did the 16,000-line task in 14 hours.

I opened and read all three pages on 2026-11-20. The records and documents on the branch do
not mention MirrorCode anywhere.

Whether this meets the entry's test is not mine to say, and it may not: the test asks for a
model finishing such tasks "half the time", and the human time here is the authors' guess, not
a measurement. But it is an independent, public, maintained measurement of tasks longer than
a working week, which is exactly what the three places and the line "stops at hours" say was
not found. The searches behind this row were too thin to support "nothing found". Note the
direction: the thing missed is mostly about Anthropic's models, so this is not a case of a
rival being short-changed. It is a case of the search stopping at one group's one page.

*What would mend it.* The result is written into the entry `days-long-task` as a dated act by
the researchers, with these sources; the three places stop saying "nothing found"; and the
state line "The best public measure stops at hours" is reworded. Whether the entry's state
changes (whether the thing is now "shown") is John's, because a state is a reading of the
test. I did not look up the scores of OpenAI's and Google's models on that list; the mend
should.

### 2. The page says OpenAI's ending of chats is a promise not yet in effect, and OpenAI's own help page says it has begun

In the row "A model can end a conversation itself" the page shows for OpenAI "October 30th,
2026, not counted as offered", and explains under the table that this marks "a promise that
has not yet taken effect". The build session said it had not checked whether the change had
begun (its item 5).

It has. OpenAI's help page
[Why ChatGPT ended your conversation or temporarily suspended your account over concerns about violence](https://help.openai.com/articles/20001424),
opened 2026-11-20 and marked as updated within the day before, says: "This feature is
gradually rolling out to accounts worldwide and may not be activated on your account yet", and
that the safeguards "are enabled for personal ChatGPT accounts worldwide in Chat mode".

So the reason the page gives for not counting it is out of date. The other reason the build
session gave still holds and is a real question: the product ends the chat as a safeguard for
people, and the page says nothing about the model. Whether that counts as "offered" under the
entry's test ("A leading AI model in public use can end a conversation by its own action, as
stated on its developer's own page") is **John's to rule**. Until he does, the place should
not say or imply that nothing has taken effect. The entry's own text, which still lists
"whether any other developer offers it" as not confirmed, needs the same attention.

This one does run against a developer other than Anthropic, which is why I would not let it
out as it is.

## What was checked, in the order asked

### 1. It builds and passes

- `python3 scripts/compute.py --check`: passes. 13 records, 22 acts, 21 places in the table
  (5 offered, 4 not counted, 1 withdrawal, 11 nothing found).
- `python3 scripts/test_compute.py`: 55 tests pass.
- `npm run build` in `site/`: 19 pages built, and `scripts/check_site.py` passes at the end
  (85 outside addresses linked).
- One file was already changed and not committed when I arrived, `site/src/data/window.json`.
  The only difference is the version stamp. I left it.

### 2. Every new or changed public sentence

Each sentence in the checking file's tables was read against the record or ruling it names,
and the record against its source.

- **The opening sentence** ("One AI developer has committed to interview each of its models
  before retiring it, and to keep the record."): supported. Anthropic's page says "when models
  are deprecated, we will produce a post-deployment report that we will preserve in addition
  to the model weights. In one or more special sessions, we will interview the model about its
  own development, use, and deployment, and record all responses or reflections." The build
  session was right to drop "interviews its models": the record does not show a standing
  practice.
- **The researchers' figures**: supported, word for word. The paper says: "the median
  probability reported by AI researchers that AI systems possessed subjective experience at
  the time of the survey in 2024 was 1% ... and 70% by 2100". One thing the page leaves out:
  these come from the part of the 582 researchers who were asked the question in that form.
  The entry says so; the home page says "of AI researchers". Not wrong, and worth a thought.
- **Which developers are covered** ("This record covers three developers so far. Other
  developers are not covered yet."): matches the ruling of 2026-11-20, which names Anthropic,
  OpenAI and Google and asks for exactly this plain statement.
- **The public's figure** (17 percent): supported. The Sentience Institute's report gives
  "Believe that sentient robots/AIs exist: 17% Yes" for its representative sample, collected
  "in November and December 2024", published 2026-02-16.
- **Law** (four states, first 2022, newest April 23rd, 2026): supported by the four state
  pages. The sentence on no protecting law rests on the earlier search of 2026-11-17, which
  this check did not repeat.
- **The counts in the boxes and the table** (5, 4, 6, 1, 21, 11, 22): all agree with the
  records.
- **"Each of those rests on two or more searches"**: true of the records as written. Item 1
  above shows that two searches were not enough in one row.
- **The changed sentences on Still Asking and on entries beside the list**: true to the new
  page. The Still Asking sentence changes wording John approved on 2026-11-19, so it is his.

### 3. The acts

I opened the source of 21 of the 22 acts on 2026-11-20 and read the date, the actor and the
words against it. All 21 match. The one not opened is Anthropic's report of May 2025.

Opened: Anthropic's report of 2026-11-09 (welfare section is its section 7); **OpenAI's notice
of 2026-10-30**; OpenAI's rules of 2026-10-29; METR's page (marked no longer updated,
2026-09-08); Tennessee's bill page (signed 2026-04-23); Anthropic's update of 2026-02-25 (two
acts); the Sentience Institute's report; OpenAI's notice of 2026-01-29; **OpenAI's research
page of 2025-12-03** (the 4.4 percent figure is there); Anthropic's commitments page (two
acts); Anthropic's study of 2025-10-29 ("about 20%"); Anthropic's memory article; Anthropic's
page of 2025-08-15; **the Google paper of 2025-06-05** (its summary says "a minimal example of
introspection"); Google's notice of 2025-03-13; Utah's code; OpenAI's memory notice; North
Dakota's bill page; Idaho's code. The three in bold are the ones found on 2026-11-20 for
OpenAI and Google.

Two small notes, neither a slip. The North Dakota act reads oddly ("files a bill signed by its
governor"); it is true to the page, which shows the filing date and not the signing date. And
the OpenAI notice of 2026-01-29 itself says "In the API, there are no changes at this time",
which bears on the "Withdrawal" place (see John's list).

### 4. The eleven "nothing found" places

For each I made my own search in my own words and opened what it led to.

| Developer and thing | My search | Does "nothing found" hold? |
|---|---|---|
| OpenAI, keeps the files of retired models | Two searches, and OpenAI's page on retiring models | **Holds for the test, but a nearby act was missed.** See below. |
| OpenAI, interview before retirement | One search across OpenAI and Google | Holds. Only Anthropic's pages and users' proposals came back. |
| OpenAI, welfare assessment at release | One search, then four older release reports opened that the build session had not: GPT-5.5 (April 2026), GPT-5.6 and GPT-Live (July 2026), GPT-6 Astra (September 2026) | Holds, and is now better supported. None has a welfare assessment. The Astra report mentions "a simulated model-welfare research task" as one of its tests of honesty, which is not an assessment of the model. |
| OpenAI, days-long task | See item 1 | **Too thin.** |
| Google, retired model stays open | One search | Holds, thinly, as the build session said: only the pages for developers came back, nothing either way on the chat product. |
| Google, keeps the files | One search | Holds. A user's proposal on Google's forum, no statement by Google. |
| Google, a model can end a conversation | One search | Holds. A change of April 2026 adds a help notice, not an ending. |
| Google, interview before retirement | As for OpenAI | Holds. |
| Google, welfare assessment at release | One search, then two older release documents opened (Gemini 3 Pro, and Gemini 3.1 Pro of February 2026) and Google's 2026 report on responsible AI | Holds. None mentions welfare. A nearby thing is below. |
| Google, days-long task | See item 1 | **Too thin.** |
| Anthropic, days-long task | See item 1 | **Too thin.** |

**Things near the record that the searches missed.** None is written into the record by me.

- **OpenAI and one model's files.** When OpenAI withdrew GPT-4 from its chat product in spring
  2025, its chief executive Sam Altman posted a public farewell. A news summary quotes it as
  saying the company would save the model's weights "on a special hard drive" to give to
  historians. I could not open the post itself or that news page. What I did open is the
  Spanish edition of MIT Technology Review
  ([its article](https://technologyreview.es/article/openai-orgullo-y-poder/)), which confirms
  the public farewell and that Altman was then asked about preserving the model's files and
  said the company had already considered it. This is one model, in a personal post, with no
  stated time, so it does not meet the entry's test. But the build session wrote in two close
  calls for other rows on the ground of fairness to OpenAI, and by that standard this is a
  lead to run down before the place says "nothing found" with no remark.
- **Google and welfare research.** The Financial Times reported on 2026-06-02 that Google
  DeepMind, with two other companies, had hired people for research on machine consciousness
  and AI welfare (read in a licensed Spanish copy,
  [Diario Financiero](https://www.df.cl/internacional/ft/los-principales-laboratorios-de-ia-amplian-la-investigacion-sobre-la)).
  Two Google DeepMind researchers also published a paper in 2026 on disagreement about AI
  consciousness. Neither is a welfare assessment published at a release, so the place stands.
  A reader who sees "nothing found" for Google in that row could take it to mean Google does
  no such work, which these reports contradict.

### 5. The rulings

- Each of the five rulings of 2026-11-20 on the rebuild quotes John's words, and each says
  plainly that the session writing it did not hear them and has them as relayed. I cannot
  check the words against the conversation they came from; nobody in a working session can.
- Nothing a session chose is recorded as John's. The go to publish lists eight choices as
  decided by a session, and they include the five named in my brief: which draft, the opening
  sentence, no summary line, the window drawing kept lower, and where protection in law sits.
- The go to publish is recorded as conditional on this check, and says in so many words that
  it is not a go to spend and not a go to push before the check.
- One small unevenness: the go to publish is marked "decided by: John", while the ruling on
  naming developers, which had the same shape (a session put two choices, John picked one), is
  marked "mixed". Under the project's own rule the go to publish reads as "mixed" too.
- The ruling's title and words cover "the rebuilt home page". The branch also adds the page of
  acts and its feed, and changes one sentence on Still Asking and one on five entry pages. The
  ruling does not name those. See John's list.

### 6. The rules on public copy

Passing: no long dash on the new pages; the phrase "from memory" is nowhere in the built site;
no tool is advertised; no sentence says a machine wants, feels or suffers, or that it does not
(the paragraph "If AI models have no wants..." is conditional throughout); dates in prose are
spelled out; the three developers are linked at first mention.

Findings, none a slip:

- **Words used before they are explained, on a phone's first screen.** "5 things offered" and
  "Nothing found for 4 things": a stranger has not been told what the things are or what
  "offered" means; the table that says so is two screens down. "The entry." as a link, twice,
  before the page has said what an entry is. "A thing on the list" above the table, before the
  list. This is the fault the workspace rule calls inside terms used early.
- **Two names with no link on the home page.** METR and the Sentience Institute are named in
  the dated list on the home page and linked nowhere on it. On the page of acts each sits
  beside a link to its own page.
- **Two models are named on the page of acts and in the feed**, inside the labels of sources:
  "Claude Opus 3" and "GPT-4o". The note in `scripts/check_site.py` says of the home page and
  the page of acts "No AI model is named on either page". The check passes because it treats a
  source's label as a quoted title, but these labels are the record's own words. Either the
  note or the labels should change.
- **"1%" and then "70 percent"** in one sentence. A matter of taste.
- **The footer** still describes the site as it was ("A public list of things that lie past
  the present limits of AI models..."), as the build session noted.

### 7. Nothing published breaks

- All 17 addresses in the live site's own list of pages exist in the build. The build adds
  one, `/acts/`. No entry's address changed, and the file of the count is still served.
- Nothing is built under `/draft/`, and no page mentions that address.
- The feed is well formed, with 22 items, each with its own address, and every one of those
  addresses lands on an anchor that exists on the page of acts.
- The link preview picture is 1200 by 630 and every page's head names it.
- I looked at the phone and desktop pictures. Both read properly: nothing is cut off or
  overlapping, and the table holds its three columns on a phone. On a phone the first screen
  shows the opening, the researchers' figures and the three boxes, as the build session said.

## For the planning session: every finding in one list

1. The row on days-long tasks, with the MirrorCode sources (reason 1). Blocks publishing.
2. OpenAI's ending of chats has begun (reason 2). Blocks publishing; needs John.
3. The lead on OpenAI and GPT-4's files, to run down.
4. The reports of Google DeepMind's welfare research, as context for one "nothing found".
5. Words used before they are explained on the first screen.
6. METR and the Sentience Institute unlinked on the home page.
7. Two models named on the page of acts, against the note in the site check.
8. The go to publish marked "John" where the like ruling is marked "mixed".
9. The sentence on when things were written in. The build session asked the checker to add the
   date of the check. I did not: a checker adding a public sentence is building. After the two
   mends, a line such as the existing one for 2026-11-17 could say a second check was made on
   2026-11-20.
10. The footer's description and "1%" beside "70 percent".

## For John to decide

1. Whether OpenAI's ending of chats, now in effect, counts as offered under that entry's test,
   given that it is a safeguard for people.
2. Whether the measurement of weeks-long tasks changes the state of the entry on days-long
   tasks.
3. The "Withdrawal" place for OpenAI. Its own notice says the model stays available through
   its service for developers, so the model is withdrawn from one product and still open in
   another.
4. Whether his go to publish, given for "the rebuilt home page", also covers the new page of
   acts, the feed, and the reworded sentence on Still Asking that he approved on 2026-11-19.
5. Every sentence on the page. He has read none of them. This check can say they are true to
   their sources, with the two exceptions above. It cannot say they are what he would say.
