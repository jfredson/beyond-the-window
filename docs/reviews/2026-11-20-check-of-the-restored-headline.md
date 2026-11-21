# Check of the restored home page headline

Written 2026-11-20 by Claude (Opus 5.5), an AI model, in a session started by the master
planning session. This session did not write the draft checked: the branch
`claude/headline-draft-df7958`, commits `1d54ce2` and `b15939a`, by the drafting session. I read
it with `git show` and built it in a scratch copy. I did not change that branch, did not merge
it, and on `main` committed only this file. Nothing was pushed.

The headline leads with one developer doing all five counted things, and that developer is
Anthropic, which makes the model writing this check. Weigh part 5 with that in mind.

## Verdict

**Fit to publish.** Every ruled piece is on the built home page, word for word, in the ruled
order, and the page matches the pictures John chose. Every figure is worked out from the
records and is true today. The guard refuses each wrong top I tried. The branch joins `main`
cleanly, and the joined result builds and passes.

Three things John should know before it goes out, none of which is a fault in the draft:

1. **"For the AI models it builds" is not how the second developer describes its one thing.**
   OpenAI's own pages describe its chat ending as a safety step for people, and the entry says
   neither page has the model decide or mentions the model's interests. The headline sentence
   and "1, by a second" count it among "things a developer can do for the AI models it
   builds". John ruled the sentence and ruled that this thing is counted, so it is his. A
   wording such as "about the AI models it builds" would remove the gap. Part 5.
2. **"Done, or publicly committed to" is looser than the list page's meaning of offered.** The
   list page says a promise "that has not yet taken effect is not counted". The home page's
   sentence can be read as counting any public promise. All five counted things meet the
   stricter meaning, so nothing is untrue. Part 2.
3. **The first screen on a wide screen shows 5, 7 and the breakdown's 5, 1, 0 side by side.**
   The developers' reading beside the count says the record "follows seven things", and the
   list page heads with 8 things. The cold-reader audit found that several counts close
   together confused readers. Part 4.

## 1. The built home page against the ruling and the pictures

Built from the branch, the top of the home page reads, in this order:

1. "A dated record of how the world is treating AI models"
2. **5**, alone in the large type
3. "things a developer can do for the AI models it builds are done, or publicly committed to,
   by at least one developer today."
4. "Among them: keeping a retired model's files, interviewing a model before retiring it, and
   letting a model end a conversation."
5. Three figures: "5, by one developer: all of them"; "1, by a second: one of the same 5"; "0,
   by the third this record covers"
6. The question: "What might a machine mind reach for beyond the limits of its present
   makeup, and how far off is each of those things?"
7. Then the line on what the record holds, the two lines on what has been checked, the two
   buttons, and the rebuild's readings.

Every piece John ruled is there, word for word, in the ruled order
(`docs/rulings/2026-11-20-home-page-opens-with-a-headline-again.md`, all three answers).

**Against the pictures.** I looked at the page at phone width (375 points) and at 1,440 points
wide, each in light and in dark, and compared it with the pictures John chose. At phone width
it matches the picture of breakdown option 2 line for line. On a wide screen it matches the
picture of version B: the headline on the left and the readings on the right. The version B
pictures were taken before the breakdown's labels were chosen, so they show the shorter labels
"by one developer" and "by a second". The page has the labels John chose afterwards. Neither
width scrolls sideways.

## 2. The figures

**The count.** The records mark five things as offered today, and the served headline file
says 5:

| Thing | Who does it, by the record |
|---|---|
| Ending a conversation | Anthropic and OpenAI |
| Interviewing a model before retiring it | Anthropic |
| Keeping a retired model's files | Anthropic |
| A retired model staying open to the public | Anthropic |
| A welfare assessment published at release | Anthropic |

**The breakdown.** Anthropic 5, OpenAI 1, Google 0, read from the records and not typed in.
"One of the same 5" is true: OpenAI's one thing is one of the five.

**The second developer's one thing.** The record cites OpenAI's help page, read on 2026-11-20.
It says these steps "are enabled for personal ChatGPT accounts worldwide in Chat mode", and in
the same passage that the feature "is gradually rolling out to accounts worldwide and may not
be activated on your account yet". So it is in effect, though not yet on every account. Under
the ruled meaning of offered, which counts what a developer does or provides, it counts. John
also ruled it counted on 2026-11-20 ("Count it as offered").

**"Done, or publicly committed to."** True of all five. Keeping the files is a public
commitment in force. The other four are done. The list page's meaning is stricter: a promise
that has not yet taken effect is not counted, and "a commitment that is in force today is
counted". All five meet it, so the home sentence says nothing untrue. It is a little looser
than the list page (point 2 above).

**The three named things** are all among the five, and each links to its own entry page.

## 3. The guard

The site check now refuses a home page whose first figure is not the count. On scratch copies
of the built site:

| What I changed | Result |
|---|---|
| Nothing | Passes |
| The large figure reads 4 | Refused: it does not match the count of 5 |
| "of 8" beside the count | Refused: a share of the list, and something beside the count |
| A reading's figure placed above the count | Refused: the first figure is not the count, and a reading stands above it |
| The count taken out | Refused: no number in the large type |

The branch adds six tests of the same rule, and they pass.

## 4. What the change did to the rest of the site

**Built pages that differ from `main`.** Two.

- **The home page,** as described above.
- **The page of acts.** No visible change. Its styles moved from inside the page to a shared
  file, which the build does when two pages use them.

**What was moved, trimmed or removed on the home page.**

- *Removed:* the opening sentence, "One AI developer has committed to interview each of its
  models before retiring it, and to keep the record." The interview is now one of the three
  named things.
- *Moved:* the question, from a line lower down ("The question behind the record: ...") to the
  page's main heading under the breakdown. The old line is gone, so it is not said twice.
- *Moved:* the two lines on what has been checked, and the two buttons, from below the
  readings into the headline column.
- *Trimmed:* the developers' reading lost "such as keeping a retired model's files or letting
  a model end a conversation", which the "Among them" line now says.

**Does anything say the same thing twice?** Partly. The headline's breakdown (5, 1, 0) and the
developers' reading beside it (Anthropic 5, OpenAI 1, Google none counted) give the same
figures, one without names and one with them. On a phone the reading is further down. On a wide
screen they stand side by side.

**Does anything contradict itself?** No. The 7 in the developers' reading is the number of
things that reading follows for each developer, and the 5 is how many of those are done by at
least one. They agree, but a reader is not told how they relate (point 3 above).

**The list page's heading.** It still reads "5 things past an AI model's ordinary limits are
offered today by at least one AI developer", John's sentence of 2026-11-19. The home page now
describes the same five as "things a developer can do for the AI models it builds". Both are
true of the same five, so they do not disagree. A reader moving between the two pages meets two
descriptions of one number. That matters a little, and less than the count being missing from
the home page did.

**Title and link preview.** The page title is still "Beyond the Window", and the preview text
is still "A dated record of how the world is treating AI models: what developers, lawmakers and
researchers have done, by whom and when." Both still describe the site truly.

## 5. The read against John's published positions

Against the positions record's copy on the default branch of the `sentient-horizons`
repository, read with `git show` earlier the same day.

**"Things a developer can do for the AI models it builds."**

- *The word "for".* It can mean "concerning" or "for the benefit of". Read the second way, it
  implies each thing is done for the model's sake. The record holds open whether any model has
  interests.
- *What the sources say.* Of the five, the developer gives safety as the first reason for
  keeping the files, and OpenAI gives the safety of people as the whole reason for its chat
  ending. So "for the AI models" says a little more than some of the sources do.
- *Is this new?* No. The phrase is already live, in the developers' reading. The change puts
  it in the headline.
- *A wording that would avoid it:* "about the AI models it builds", or "with the AI models it
  builds". This is John's sentence (point 1 above).

**The breakdown that leads with one developer doing all five.**

- *Toward dismissal?* No. The audit found readers summing up the old top as "almost nobody is
  doing anything". The new top says five things are done, and by whom in number, which is the
  opposite of that summary.
- *Toward one developer?* The figures are bare. The developer is named only in the reading
  beside them. "5, by one developer: all of them" is what the records give. It may read as
  praise of that developer, though nothing in the words praises it.

**Does the site still not campaign?** Yes. The top states a count, what is counted, and who in
number. It argues for nothing, and the question beneath it is a question.

## 6. Joining `main`

`git merge-tree` joins the branch with `main` with no conflicts. The joined result keeps
everything on `main` since the branch began, including the closer wording on the entry about
checked self-reports. On the joined result the tests pass, the records check says "The headline
file matches the records", the build gives 19 pages, and the site check says "The built site
passes: 19 pages, 114 outside addresses linked."

## 7. The checks on the branch

- `python3 -I scripts/test_compute.py`: "Ran 71 tests", "OK". That is six more than on `main`,
  the tests of the new guard.
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "24 dated acts", "The headline file matches the
  records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 114 outside addresses
  linked."

## What I did not do

- I did not open OpenAI's help page again. I relied on the passage the record quotes, which I
  read against that page in an earlier check.
- I added a temporary entry to the local preview settings to serve the scratch build, and put
  the settings back as they were. That file is not in the repository.

**Fit to publish: every ruled piece is on the page word for word and matches the pictures John
chose, every figure is computed and true today, the guard holds, and the branch joins `main`
cleanly. Three points are for John, the first being that "for the AI models it builds" says
more than the second developer's own pages do.**
