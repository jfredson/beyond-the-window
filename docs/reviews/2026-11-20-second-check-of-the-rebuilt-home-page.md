# Second check of the rebuilt home page: fit to publish after one small fix

Written by Claude (Fable 5.2), an AI model, on 2026-11-20, in the session that made the first
check (`docs/reviews/2026-11-20-check-of-the-rebuilt-home-page.md`) and wrote none of the page.
It checks the branch `claude/cold-reader-proposal-2026-11-20` at commit `b7e982a`: the mends
in `2f51276` and John's four rulings as applied in `b7e982a`. This session changed nothing on
the branch except adding this file. Nothing was pushed.

**The conflict, again.** Anthropic made the model that did this check. The one fix asked for
below makes Google's place less kind to Google, so it is set out with the chart it rests on,
for anyone to read against.

## Verdict

**Fit to publish after one listed fix.** Both reasons from the first check are mended and
match their sources. The four rulings are applied as ruled and no further. One place still
says something that is no longer the best the record can do, and the fix is exact.

### The one fix

**Google's place in the row "A model works on one task for days".** It reads: "June 29th,
2026: an outside group tested one of its models on such programs, and how it did on the one
put at weeks is in a chart that was not read. Not counted." The build session asked a checker
who could read the chart to correct it. I read it, by drawing page 7 of the paper as a
picture ([the paper](https://arxiv.org/abs/2606.30182), figure 2).

What the chart shows for the 16,000-line program (`gotree`), as the share of runs that passed
every test and the share that passed at least 99 percent of them:

| Model | Every test | At least 99 percent |
|---|---|---|
| Anthropic's (Claude Opus 4.7) | 0 | 100 |
| OpenAI's (GPT-5.5) | 0 | 94 |
| Google's (Gemini 3.1 Pro Preview) | 0 | 0 |

The paper's text says the Google model was run in one programming language only, three times.

So the place should say what was found. Words that are true to the chart:

> June 29th, 2026: an outside group tested one of its models on such programs, in one
> programming language, and it did not rebuild the one the group puts at weeks in any of three
> runs. Not counted.

The same fact replaces the "not confirmed" line on the entry `days-long-task` that says the
chart could not be read. The place stays "found, not counted", so no count on the page moves.
If these words are used as written, I do not think a third check is needed for them.

I did not make this change myself. It is a new public sentence about a developer, not a slip.

## What was checked

### 1. It builds and passes

The validator passes (13 records, 24 acts; 21 places: 6 counted, 7 found and not counted, 8
nothing found, none undecided, none unsearched). 57 tests pass. The site builds 19 pages and
`scripts/check_site.py` passes with 96 outside addresses linked. The count of things offered
by at least one developer is still 5.

### 2. The two blocking reasons

**The row on long tasks.** I opened Epoch AI's first results, METR's note, Epoch AI's page for
the test and the paper again, and read the two new acts, the three places and the entry
against them.

- "a program the group guesses would take a person 2 to 17 weeks": the paper says "Four
  MirrorCode contributors estimated that a skilled human engineer would take 2–17 weeks", and
  gives the four estimates the entry lists.
- "two of the models rebuilt the 16,000-line program and only one rebuilt any of the largest
  programs": the paper says "Both Claude Opus 4.7 and GPT-5.5 successfully reimplemented
  gotree" and "Only Claude Opus 4.7 successfully reimplemented Large targets". The chart
  agrees. Note that "rebuilt" here means passing at least 99 percent of the tests; no model
  passed every test on that program. The entry's words "substantially" would be closer, and
  this is a small point of wording, not an error.
- The highest score of 56 percent, the 25 programs, the 19 days and the $2,600: all in the
  paper's summary.
- OpenAI's place is true to the paper. Google's is the one fix above.
- The entry's state, "Not shown. One public measure stops at hours. A second, of tasks its
  authors put at weeks, is recorded, and the entry stays as it was", is true, and says why:
  the human time is an estimate and the test asks for half the time.
- The scores on Epoch AI's own page are drawn by the page and I could not read them either.
  The entry says so.

No place in this row says "nothing found" any more.

**OpenAI's ending of chats.** I opened the help page and the notice of 2026-10-30 again. The
help page still says the feature "is gradually rolling out to accounts worldwide" and that the
interventions "are enabled for personal ChatGPT accounts worldwide in Chat mode". The entry
quotes both, and the place no longer calls it a promise not yet in effect.

**The other eight "nothing found" places** are the ones I searched for the first check and
found to hold. Nothing I opened today contradicts any of them.

### 3. The four rulings

Each has a file, quotes John's words as relayed, says the session did not hear them, and is
marked "mixed". Each is applied as ruled and no further.

- **Ending of chats is counted.** The file records that no recommendation was given. OpenAI is
  added to the entry's state, the place reads "Since October 30th, 2026", and the count stays
  5. The file is honest about what it found afterwards: both of OpenAI's pages name the chat
  product as what ends the conversation, and neither says the AI model decides. I read both
  pages for this. The help page does not use the word "model" at all, and the notice uses it
  only about answering questions on past attacks. So the build session's reading is right.
  The entry's page says this plainly in three places (the state's detail, the "not confirmed"
  line, and the dated line on why the state changed), and claims no more than the pages do.
  The test is not changed. The question is put back to John, and it is on his list below.
- **The weeks-long measurement is recorded and the entry stays "not shown".** Applied exactly.
  The file says which words after "Not shown" are a session's.
- **The withdrawal place says both facts.** Applied. Both facts are in the notice of
  2026-01-29, which I read for the first check ("In the API, there are no changes at this
  time"). The file says what it does not settle.
- **The go covers the page of acts, the feed and the Still Asking sentence**, and the planning
  session may push. Recorded in the go to publish, which now also reads "mixed" and says it
  first read "John".

Two small unevennesses, neither a reason to hold: the file on the withdrawal place gives the
choice John took and not the others he was offered, and the note on the scope of the go says
"the choices included" one of them. The other two files list every choice.

### 4. My other findings from the first check

| Finding | Now |
|---|---|
| 3. The lead on OpenAI and one model's files | Honestly left. The post could not be opened; the place still says nothing found, and the search's words in the record now give the lead and why it would not meet the test. |
| 4. Google's welfare research | Mended. The newspaper report is a source on the entry, and the page says above the table that nothing found does not mean a developer does no work on the subject. |
| 5. Words used before they are explained | Mended. The page now says what the seven things are, with two examples, before the boxes; "The entry." is "More on this survey."; the boxes read "in place or promised", "found, not counted", "looked for, not found", each explained under them. |
| 6. Two names with no link | Mended. METR, the Sentience Institute and Epoch AI are linked on the home page. |
| 7. Two models named in source labels | Honestly left, with the reason. The note in the site check was corrected to say what the pages do. |
| 8. "John" where the like ruling said "mixed" | Mended, with a line saying what it first read. |
| 9. The sentence on when things were written in | A sentence was added: "A check of them against their sources was made the same day, and the mends it asked for were made." With this second check it is true. |
| 10. The footer and "1%" beside "70 percent" | Mended. |

### 5. The changed sentences

Every sentence in the build session's two tables was read against the built pages and the
records. The counts in the three boxes (5 and 2; 1, 3 and 3; none, 2 and 5) add up to the 21
places and agree with the table. The notes under the boxes and under the table say what each
word means before or beside its use.

No sentence says or implies that only one developer has anything counted. The opening
sentence is about interviews before retirement, where one developer has committed, and is
true. The lines "by one developer" lower on the page each belong to a thing that one
developer does. The About page's "4 of the 5 things counted as offered rest on pages published
by the one developer that offers them" is true and reads fairly: it is a statement about where
the sources come from, and the fifth thing is now offered by two.

One remark. In the table, the row on a model's report about its own state still says "not
counted as offered" three times, while every other such place and the note under the table
now say "Not counted". A matter of tidiness.

### 6. Nothing published breaks

All 17 addresses in the live site's list of pages exist in the build, which adds `/acts/`. The
file of figures is still served at its old address. Nothing is built under `/draft/`. The feed
is well formed with 24 items, each landing on an anchor that exists. The preview picture is in
place. The phrase "from memory" and the long dash appear nowhere on the new pages. The
pictures were retaken with the last commit; I looked at the phone's first screen and the
desktop page, and both read properly. The longer places in the table wrap within their
columns.

`site/src/data/window.json` is again changed and not committed, by the version stamp alone.

## For the planning session

1. Make the one fix above, in the words given or closer ones, on the place and on the entry's
   "not confirmed" line.
2. Optional: "not counted as offered" to "Not counted" in the last row; the other choices in
   the two ruling files.

## For John to decide

1. **Whether the test's words "by its own action" are met by OpenAI's ending of chats.** His
   ruling counts it. OpenAI's pages say the chat product ends the conversation and do not say
   the AI model decides. On the entry's page this is said plainly. On the home page the place
   reads "Since October 30th, 2026" in a row named "A model can end a conversation itself",
   with nothing beside it, so a reader of the table alone would take it that OpenAI's model
   does the ending. That follows from the ruling as given. If he wants the home page to carry
   the difference, a few words in that place would do it.
2. **The date in that place.** October 30th, 2026 is the day of OpenAI's notice, when the
   change had not begun. The note above the table says a "Since" date may be the date of a
   public commitment, so it is consistent. OpenAI's help page gives no date for when it began.
3. **The sentences themselves**, which he has not read.
