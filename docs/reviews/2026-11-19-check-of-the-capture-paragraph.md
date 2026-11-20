# Check of the paragraph about the capture on the Still Asking page

Written 2026-11-19 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session did not write the paragraph or the commit that added it
(`1ab2dcc`). The model that wrote this is made by Anthropic, and the paragraph is about a model
Anthropic made, so weigh the judgments below with that in mind. I changed nothing, pushed
nothing, and did not open or look for the replies.

## Verdict

**Fit to publish.** The paragraph is the approved one with one sound change, every statement in
it matches the repository's record, the three links are the official pages and say what the
paragraph says, and the guard allows the two names in that one paragraph and nowhere else.

Two small things are worth mending soon, and neither makes the page false:

1. **One line higher on the same page now reads oddly beside the paragraph.**
   *File:* `site/src/pages/still-asking.astro`, under "What AI models said when asked".
   *Sentence:* "Nothing yet. None of the questions has been put to any model."
   *What is wrong:* eight lines further down the page says "ten questions were put to Claude
   Sonnet 4.5". "The questions" means the record's own questions, which are not written yet, so
   the line is true. A reader who does not carry that meaning down the page sees two sentences
   that seem to disagree, until the new paragraph's opening words settle it.
   *Suggested fix:* "Nothing yet. None of this record's questions has been put to any model."
   The writing session proposed the same words. This line is not one John ruled.
2. **"Withdraw it" is wider than the developer's page.**
   *Sentence:* "its developer, Anthropic, is due to withdraw it on November 30th, 2026".
   *What is wrong:* the page linked gives that date for the developer's own services ("its
   upcoming retirement on the Claude API", and "The dates on this page apply to
   Anthropic-operated platforms"). It says services run by two partners set their own dates.
   *Suggested fix, if John wants it:* "is due to withdraw it from its own services on". The
   words are his approved ones, so this is his to decide.

## 1. Against the approved wording

I compared the paragraph on the built page with the paragraph in the ruling
(`docs/rulings/2026-11-19-capture-paragraph-on-still-asking.md`) word by word.

- **The one difference:** the ruling's interim form is "withdraws it on November 30th, 2026",
  and the page has "is due to withdraw it on November 30th, 2026".
- **Is it sound?** Yes. "Were put ... shortly before its developer ... withdraws it" sets a
  past verb against a present one for something that has not happened. "Is due to withdraw"
  says plainly that it is still to come, which is what the developer's page says. It changes
  no fact. It is the writer's change and not John's, and the commit message, the page's
  comment and the hand-over note all say so.
- **Anything else?** No other word differs. Three phrases carry links, as the ruling asks. The
  page's comment records that the words become "withdrew it" on or after 2026-11-30, once the
  developer's page confirms it.

## 2. Against the repository's own record

| The paragraph says | The record says | Holds? |
|---|---|---|
| "On November 19th, 2026" | `docs/spending-record.md`: "The run was made on 2026-11-19, and it is complete." | Yes |
| "ten questions" | `capture/plan.toml`: `questions = 10`. The list of files (`docs/capture/manifest.md`) has replies numbered for questions 1 to 10 | Yes |
| "five times each" | `capture/plan.toml`: `askings = 5`. The list has 50 reply files, five for each question, each a first attempt | Yes |
| "Claude Sonnet 4.5" | The spending record: "50 exchanges with Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)", and "in all 50 the service reported the model's name as expected". Every file name in the list carries that name | Yes |
| "No way of comparing answers had been written" | The spending record: nobody reads the answers "before a method for comparing them is written, checked and ruled" | Yes |
| "The answers are kept exactly as given" | The list holds a checksum for each reply file, and the spending record says the script confirms the folder matches the list | Yes |
| "They have not been read" | The spending record: "Nobody has read the replies. The session saw labels, counts and costs only." | Yes, by the record. I did not look at the replies, so I can confirm only what the record says |
| "they are not scored" | No file in the repository scores a reply, and none could without reading them | Yes |
| "nothing on this site rests on them" | No record in `data/entries/` cites the capture, and the count is unchanged at 5 | Yes |

## 3. The three links

Each opened by me on 2026-11-19.

| Words | Address | What it is | Verdict |
|---|---|---|---|
| "Claude Sonnet 4.5" | `https://www.anthropic.com/news/claude-sonnet-4-5` | The developer's own announcement, titled "Introducing Claude Sonnet 4.5" | The official public page |
| "Anthropic" | `https://www.anthropic.com/` | The company's home page | The official public page |
| "November 30th, 2026" | `https://platform.claude.com/docs/en/about-claude/model-deprecations` | The developer's page "Model deprecations" | The official public page, and the ordinary page, not the raw text file the entries link |

**Does the page give the date in words a reader can find?** Yes, twice. Its table has the row
"claude-sonnet-4-5-20250929, Deprecated, September 30, 2026, November 30, 2026". Its section
headed "2026-09-30: Claude Sonnet 4.5 model" says: "On September 30, 2026, Anthropic notified
developers using Claude Sonnet 4.5 of its upcoming retirement on the Claude API", with a table
giving the retirement date as "November 30, 2026". The table's column is headed "Tentative
retirement date", which is one more reason "is due to" is the right wording.

## 4. Whether it contradicts anything else

- **The headline,** "No AI model has been asked these questions yet", and the page's
  description, "No AI model has been asked the questions of this record yet". No
  contradiction. "These questions" are the record's, the page's opening sentence says the
  record "does not exist yet", and the new paragraph says its ten questions are "outside this
  record" and "not part of Still Asking".
- **The About page and every entry page,** "No AI model has yet been asked any of the
  questions this record will keep". No contradiction, for the same reason.
- **"Until that method exists, nothing is asked for Still Asking."** No contradiction. The new
  paragraph follows it directly and says the ten questions are not part of Still Asking.
- **"Nothing yet. None of the questions has been put to any model."** This is the one place a
  new reader could stumble (item 1 under the verdict). Read with the page's own meaning it is
  true.
- **Would a new reader see a contradiction?** One who reads the page through, no: the
  paragraph opens with "One thing has been asked, outside this record", which is exactly the
  sentence that reader needs. One who reads only the headline and the line under the first
  heading could, until they reach the paragraph.
- **The rest of the site.** The home page links this page with the words "What AI models have
  been asked", which now has an answer. Nothing on the home page, the list or any entry speaks
  of the capture. The model's name is on no other built page.

## 5. Conditional language, working words, and who built the site

- **"so that its answers would exist after it was gone".** It states the purpose of the people
  who asked. It says nothing of what the model wants, feels or fears, and it does not say the
  model has a stake in its answers lasting. "Gone" is a soft word for "withdrawn" and carries a
  little feeling. "After it was withdrawn" would be flatter. The words are John's approved
  ones, and they are within the rule.
- **Nothing else** in the paragraph attributes a want, a feeling or a fear, or denies one.
- **Working words:** none.
- **Who built the site:** nothing. The paragraph names a model because that model was asked,
  which is the one disclosure John's ruling of 2026-11-19 calls for.

## 6. The change to the site check

`scripts/check_site.py` now takes the two names "Claude Sonnet 4.5" and "Anthropic" out of the
first paragraph marked `id="capture"` on the Still Asking page before it looks for names. I
tried it on scratch copies of the built site, one changed sentence at a time.

| What I wrote in | Result |
|---|---|
| "Anthropic made that model." elsewhere on the Still Asking page | Refused |
| "Claude Sonnet 4.5 was asked." elsewhere on the Still Asking page | Refused |
| "as was Claude Opus 4" inside the paragraph | Refused |
| "like OpenAI's model" inside the paragraph | Refused |
| "Ten questions were put to Claude Sonnet 4.5." on the home page | Refused |
| A paragraph marked `id="capture"` naming the model, on the About page | Refused |
| A second paragraph marked `id="capture"` on the Still Asking page | Refused |
| The built site as committed | Passes |

So the two names are allowed in that one paragraph only, and the guard still catches them
everywhere else.

## 7. Anything in the commit beyond the task

Nothing. The six files are: the page; the site check; a dated note under choice 18 in
`docs/first-version-choices.md`, marked as the writer's own decision; the writer's hand-over
note; one line in `CHANGELOG.md`; and one line of `site/src/data/window.json` (the commit the
site was built from).

One thing next to the commit, not in it: `CHANGELOG.md` still opens "Nothing is published, so
there have been no public corrections." The site has had its first release, so the first half
is out of date. The file is in the public repository and on no page.

## 8. The checks

Run on 2026-11-19 on commit `1ab2dcc`.

- `python3 -I scripts/test_compute.py`: 30 tests, all pass.
- `python3 -I scripts/compute.py --check`: "The headline file matches the records." The count
  is 5.
- The site build: 18 pages.
- `python3 -I scripts/check_site.py`: "The built site passes: 18 pages, 78 outside addresses
  linked." That is two more than before, the announcement and the page of withdrawal dates.

The build rewrote one line of `site/src/data/window.json`, which I left out of this commit.

## What I did not do

- I did not open or look for the replies. "They have not been read" rests on the spending
  record.
- I did not look at the page in a browser at phone or desktop width. The change is one
  paragraph of ordinary text in a page I looked at earlier the same day.

**Fit to publish: the paragraph is the approved one with one sound change of tense, it is true
against the record and the developer's own page, and the guard holds.**

## Added 2026-11-19: check of the two wording fixes (commit `8e54fbf`)

Written by Claude (Fable 5.2), an AI model, the same checking session as above. The writing
session made the two fixes this review suggested, after John ruled them on 2026-11-19 ("Yes,
both"; `docs/rulings/2026-11-19-two-wording-fixes-on-still-asking.md`). I read the whole diff of
that commit, built the site and read the two sentences on the built page. I changed nothing and
pushed nothing.

1. **The two sentences read exactly as the ruling says.** On the built page:
   - "Nothing yet. None of this record's questions has been put to any model."
   - "... shortly before its developer, Anthropic, is due to withdraw it from its own services
     on November 30th, 2026, so that its answers would exist after it was gone."
   The three links in the paragraph are unchanged.
2. **No other visible sentence changed on any page.** The commit touches three files. In the
   page's file, the only changes a reader sees are those two sentences, and the rest is a
   comment that is not printed. One thing does change on every page, as it does with every
   build: the short version code in the line at the foot of each page ("Last built November
   19th, 2026 (version ...)"), which names the commit the site was built from.
3. **The reworded first sentence disagrees with nothing else on the site.** The sentence was
   on this page only. The other places that say the same thing already speak of the record's
   own questions: the page's headline ("No AI model has been asked these questions yet"), its
   description ("the questions of this record"), and the sentence on the About page and every
   entry page ("any of the questions this record will keep"). The new wording brings the line
   into step with them.
4. **Nothing in the commit beyond the task.** The other two files are one new line in
   `CHANGELOG.md`, which describes the two fixes correctly, and the one line of
   `site/src/data/window.json` that every build rewrites.
5. **The checks pass,** run on 2026-11-19 on commit `8e54fbf`: 30 tests, all pass; the count
   is 5 and the headline file matches the records; the build gives 18 pages; the site check
   says "The built site passes: 18 pages, 78 outside addresses linked."

**Two things beside the commit, not in it, and on no page.** Both are in `README.md`, which
is in the public repository:

- It says of the ten questions put to a model that is about to be withdrawn: "It has not
  run." It ran on 2026-11-19 (`docs/spending-record.md`).
- It says "No money has been spent." The spending record gives $0.2667 for that run.

Neither holds up the push, because no page of the site says either. They should be mended
soon, along with the opening of `CHANGELOG.md` ("Nothing is published"), noted in part 7.

The build rewrote one line of `site/src/data/window.json` again, which I left out of this
commit. I did not look at the page in a browser.

**Fit to publish: the two sentences are exactly the ruled ones, nothing else a reader sees
changed, and every check passes.**
