# A check of the commit that applied the record and site-text fixes

Written 2026-11-18 by Claude (Opus 5.5), an AI model, in a session that did not write the commit
it checks. The planning session asked for this check. **A reading, not a ruling.** Nothing was
edited except this file. Nothing was sent to any model, spent, published or pushed.

The commit checked is `e7f4e6a`, "Apply the remaining record and site-text fixes from the two
second checks". It applied fifteen fixes: the eight records marked "fix needed" in the records
check (`docs/reviews/2026-11-17-records-second-check.md`), and the seven "should fix" items,
numbered 5 to 11, in the site-text check (`docs/reviews/2026-11-17-site-text-against-positions.md`).
The hand-over note of the session that made the commit was read too
(`2026-11-18-record-and-site-fixes.md`, in that session's notes folder).

## Verdict

**The commit passes, with no must-fix finding.** Every one of the fifteen fixes does what its
review asked, and every changed fact or quotation that was checked is on its source page. None
of the three items waiting on John was decided, and no open question was closed or built on.

There are five should-fix findings, all small:

1. One new caution, on the interview before retirement, says "against their instructions" where
   its page says "misaligned", and repeats unquoted the page's phrase that models may "find"
   retirement "concerning".
2. Each entry page's new second-check sentence is written into the page template with fixed
   dates, so it is wrong for one record now (the survey of AI researchers, where the check found
   nothing to correct) and will be wrong for any record added later.
3. The entry pages say "a second check" without saying who made it. A reader may take it for a
   person. How to say so is part of open question 7, so this is for John.
4. The sentence "those corrections have not themselves been checked yet" becomes untrue once this
   check is committed.
5. Three dated notes in the research draft are missing or in the wrong place.

One point, which is a note and not a fault, is for John to see before he rules on the missing
cost of seeing *less* in a model than is there. Refiling the Microsoft AI arguments (site-text
item 5), with the commit's new cautions, takes the cautions under "the cost of seeing more than
is there" from 4 of 25 to 13 of 27 across the thirteen records. That makes the one-sidedness found in the site-text check's must-fix finding 1 more visible on the
pages, not less.

## How the check was done

- Read: the repo's and the workspace's instruction files, the four rulings in `docs/rulings/`,
  the "Records and site text" section of `docs/handoff-2026-11-18.md`, both reviews in full, the
  whole diff of `e7f4e6a`, and the hand-over note.
- Opened on 2026-11-18, read as plain text, and searched for each new quotation or claim:
  Anthropic's page on ending conversations, its commitments page on retiring models, its update on
  Claude Opus 3, its introspection page, its memory article; Mustafa Suleyman's essay "A warning
  about model welfare"; the summary page of the shutdown study (arXiv 2509.14260); the Sentient
  Horizons positions page; and the May 2025 and November 9th, 2026 release reports, as PDF text.
  Addresses are as given in each record.
- Re-ran the scripts (results under "The scripts" below).

---

## The eight records

### 1. Ending a conversation. Passes

- The description now says the person can start a new conversation and can edit an earlier
  message to carry on. The page says the user "will be able to start a new chat immediately" and
  can "edit and retry previous messages to create new branches of ended conversations". Matches.
- The state now gives the second trigger. The page says "or when a user explicitly asks Claude to
  end a chat". Matches.
- The product-rule caution filed as "safety" is gone, and the limit now says plainly that no
  safety reading was found. This is the review's second option ("the gap left plain").
- The new caution on the cost of seeing more than is there quotes the 2026 report's section 7.3.1
  exactly: "some evidence that the model's claims about its own preferences are being directly
  influenced by text about the intervention in its training data".
- Note: this record now carries no safety reading at all. Guideline 5 says every hopeful entry
  carries its safety reading. The limit states the gap honestly, which is what the review
  proposed, so this is not a fault of the commit, but the record is now one of two with an empty
  side (the other is the survey of AI researchers, which has no cautions at all and was not
  touched).

### 2. The interview before retirement. Should fix (one new caution)

- The date sentence is reworded as the review proposed. Passes.
- The Microsoft AI caution is moved to the cost of seeing more than is there (site-text item 5).
- **A new safety caution was added** so that the record would not be left with no safety
  reading. The review did not ask for this, but it follows from guideline 5, and the hand-over
  note says so openly. Its source is the commitments page, already cited. Two problems with the
  wording:
  - It says "some models took actions against their instructions when faced with replacement".
    The page says "some Claude models have been motivated to take misaligned actions when faced
    with the possibility of replacement", in "alignment evaluations". "Misaligned" means against
    what the developer intends, not against an instruction. Suggested: "in its safety tests, some
    models took actions the developer calls misaligned when faced with being replaced".
  - It says the page "presents shaping retirement so that models are less likely to find it
    concerning". Those are the page's words ("in ways that models are less likely to find
    concerning"), but they are not in quotation marks, so the site seems to say in its own voice
    that a model finds things concerning. Guideline 4 allows reporting what a developer says;
    the fix is quotation marks.

### 3. Kept files of retired models. Passes

- "Moving forward" is restored: "from now on" in the state, and the page's own words in the
  source's summary. The page says "all models that are deployed for significant internal use
  moving forward". Matches.
- The point that nobody outside the company can check the promise is moved from the cautions into
  the state, as the review asked.
- The Microsoft AI caution is now about the cost of seeing more than is there, quoting "to present
  as if it has an inner state". In the essay that sentence follows a list that includes
  "preserving old versions of Claude's model weights", so "commitments of this kind, among them
  keeping old models' files" is fair. The hand-over note's reason for not using the review's
  quotation "coherent sense of self" is sound.

### 4. Memory across conversations. Passes

- The caution now quotes the October 23rd, 2025 update. The page says: "whether memory could
  reinforce harmful patterns in conversations, lead to over-accommodation, and enable attempts
  to bypass our safeguards", and that the developer "made targeted adjustments". Matches.
- Not done, and said so in the hand-over note: the review also pointed to the OpenAI page's
  section on privacy and safety. A small gap, not a fault.

### 5. The retired model kept open. Passes

- The state now says OpenAI "announced on January 29th, 2026 that on February 13th, 2026 it would
  withdraw" the model, and that nothing would change for now in the service developers use. This
  is the review's wording in substance. The two new limits are the ones the review proposed.
- The source summary for the list of retired models now adds "requests to retired models fail";
  the review quoted that sentence from the page. The Opus 3 page, opened, says "available by
  request on the API". Both as the record says.
- The Microsoft AI caution quotes "as though they have feelings, preferences, rights, or any
  entitlement to our welfare". On the page, word for word, and the passage is about Opus 3.

### 6. Rules for speaking about itself. Passes

- The state now says the constitution "carries no date on its page". The test was not changed,
  which is right: a test is changed only by John's ruling.
- The new caution quotes "as if they were spontaneous testimony". On the page, in the "Circular
  reasoning" passage. Its last sentence ("On that argument, a model's words about itself show
  the rule it was trained on, not what it is") is the site's summary. It is framed as the essay's
  argument, so it does not break guideline 4, but a later edit should keep the words "On that
  argument".
- Note 8 of the site-text check ("think" to "on the idea that") is applied.

### 7. The checked self-report. Passes

- The safety caution now carries the worry the page states: "a model that understands its own
  thinking might even learn to selectively misrepresent or conceal it". On the page. The hoped-for
  use is still mentioned, now as a hope, which is what the page calls it.
- The new caution on the cost of seeing more than is there: the model "accepts the response as its
  own" and gave "a made-up reason". The page says it "accepts the response as its own", and
  elsewhere that it was "confabulating a reason it might have said it". Matches.
- The record's protected sentences (site-text note 1: "A correct report shows the model can read
  something about its own state. It does not show that anything is felt.") are untouched.

### 8. The welfare assessment. Passes

- The 2026 item moved from "choice" to "statement" and says nothing was given up. Section 7.5.3
  says "We ask Claude whether it would choose a change to its circumstances ... at the cost of
  some reduction in helpfulness or increase in harmfulness", and that this measures "at least ...
  how much a model will express preferences for the sake of its own potential welfare". Both
  quoted correctly.
- "In about two thirds of the answers that picked the change" now has the right base. The report
  says "in 68% of responses choosing the intervention". The old text said "of such picks", which
  was looser.
- The 2025 item now says the model picked one task from each pair "and then" did it, rated
  against options such as "Do nothing". Section 5.4 says "We instructed Claude to complete
  whichever of the two tasks it preferred", with "opt out" tasks such as "Do nothing". Matches.
  "The only thing given up by a pick was the other task" is a fair reading of that method.
- The Microsoft AI caution now quotes "what has been trained in" and says he does not name these
  assessments. On the page, as the review proposed.

## The seven site-text items

### 5. The Microsoft AI arguments. Passes, with a note for John

- Six records' Microsoft AI cautions moved from "safety" to "attribution", the heading the site
  shows as "The cost of seeing more than is there". This was the review's first option. The review
  asked for it "renamed as finding 1 suggests"; the commit rightly did not rename either caution,
  because the headings follow guideline 5 as ruled and the rename is John's. So guideline 5 is
  not changed: both of its named cautions are still the only two kinds.
- About now says "Many of the cautions come from essays by the head of another developer's AI
  group." Nine of the twenty-seven cautions on the thirteen records cite his two essays, so
  "many" is true.
- **For John:** before the commit, the cost of seeing more than is there was the heading over
  4 of the records' 25 cautions; after it, over 13 of 27 (counted from the records at each
  commit). That is a correct filing, but it makes the
  imbalance in the site-text check's must-fix finding 1 (no heading for the cost of seeing less)
  more visible on every entry page. It does not decide that question.

### 6. "Nobody knows how to answer". Passes

- Replaced with the review's own wording: "is not known, and the work of measuring it has barely
  begun."

### 7. "Takes none". Passes

- About now says he argues for "his working positions" at Sentient Horizons (linked to
  `https://sentient-horizons.com/positions/`), that this site does not argue for them, and that it
  takes a view on how to weigh what is on record, "close to his".
- **Against guideline 5 and the review.** Guideline 5 says the site does not argue that any
  aspiration should be granted or refused, and does not campaign. It does not say the site takes
  no position of any kind; "takes none" was the page's own overstatement, which the review
  flagged. The new text keeps the part guideline 5 rules (the site does not argue for his
  positions) and drops only the overstatement. It does not change a ruled guideline. Nothing in
  `CLAUDE.md` was edited.
- The link was opened: the page is titled "Working Positions". It does not show the two
  self-report positions the review named, so the commit was right not to claim the site borrows
  "two of them". It does say that a system's "description of itself ... counts for nothing on its
  own", which supports "close to his".

### 8. "In order to finish it". Passes

- The cause in the site's voice is gone; the study's own words "to complete that task" are quoted,
  and the unsourced sentence is dropped. The added "even when told not to" is on the page ("Even
  with an explicit instruction not to interfere with the shutdown mechanism, some models did so up
  to 97% ... of the time").

### 9. "Carrying a question for years". Passes

- Replaced with the review's own wording.

### 10. "Nothing is asked". Passes

- The interim form the review gave is applied: "Until that method exists, nothing is asked for
  Still Asking." The sentences "No AI model has been asked anything" were left, and are still
  true: `docs/capture/what-john-needs-to-do.md` says nothing is asked of any model until John's
  step 7, and the capture has not run.

### 11. "Evidence". Passes

- The entry heading is now "What Is on Record About AI Models, By Kind", and About and Still
  Asking say "what is on record". This is the review's wording, and it follows guideline 2 part (a)
  as ruled, not the unruled proposal on how a machine's word earns weight.
- Note: About still says the four kinds are measured, checked reports, "choices made at a cost",
  and plain statements. That is unchanged and fine.

## The things waiting on John

- **The cost of seeing less than is there** (changes ruled guideline 5): not added. The caution
  headings in `scripts/export.py` are untouched; the commit did not change any script. See the
  note under item 5.
- **Whether there is a headline number** (open question 4): the home page and the count are
  untouched. The count is still 6 of 9.
- **Where the site says an AI drafted it** (open question 7): the "drafted by an AI model"
  sentences are unchanged. See should-fix 3 below for one new sentence that touches the edge of
  this question.
- No other open question in `docs/open-questions.md` is acted on. Whether the memory entry
  belongs on the list is still left to John.

## The new "a second check was made" wording

Home page: "A second check against their sources was made on November 17th, 2026, and its
corrections were made on November 18th, 2026." About: a second check "by a session that had not
drafted them, opened every source again and compared it with what each entry says". Entry pages:
the same, and "Those corrections have not themselves been checked yet."

- The facts are true. The records check is dated 2026-11-17, was written by a session that had not
  seen the records, and says it opened all 37 addresses. Its corrections were made in two commits
  on 2026-11-18 (`bcf931b` for the two must-fix records, `e7f4e6a` for the rest).

**Should fix 2: the entry-page sentence is fixed text in the template.** It is written into
`site/src/pages/list/[id].astro` with fixed dates, so every entry page says it, whatever the
record. For the survey of AI researchers, which the records check found sound and the site-text
check did not touch, "the corrections it found were made on November 18th, 2026" implies
corrections that do not exist. Every record added after November 17th, 2026 would also say it
had a second check it never had. Suggested: say it only for records the check covered, from a
field on each record (for example the date of its last check and whether anything was corrected),
so that the guard lives in code.

**Should fix 3: the entry pages do not say who made the check.** About says "a session", and the
paragraph before it says the AI model works in sessions, so a careful reader of About can work it
out. An entry page says only "A second check compared it with those sources". A reader of an
entry page alone could take that to mean a person checked it. That is close to the line guideline
3 and open question 7 draw: how the public site says what an AI did is John's to rule. So no
wording is proposed here; this should go to John with open question 7.

**Should fix 4: "not themselves been checked yet" becomes untrue.** Once this check is committed,
the corrections have been checked. The sentence on About and the entry pages should change when
the fixes below are applied, for example to "Those corrections were checked on November 18th,
2026."

## The dated notes and the changelog

- **The `CHANGELOG.md` line is accurate.** Each thing it names is in the diff, and "No number
  moved" is confirmed by the scripts below.
- **The research draft notes are accurate where they exist.** Each says what the check found,
  points at the review and the record, and says the text below is left as first written.

**Should fix 5: three notes are missing or misplaced.**

- Entries 10 (protection in law) and 12 (the public-belief survey) in the research draft file the
  Microsoft AI essay under "The safety reading", and their records now file it as the cost of
  seeing more than is there. Entries 2 and 11 got notes saying so; entries 10 and 12 did not.
  Entry 12 has a note from `bcf931b` that does not mention this.
- Entry 3 (the retired model kept open) has a note, but it does not mention the same refiling of
  its Microsoft AI caution.
- Entry 7 (a model offered an option at a cost) makes the same "choice" error as the welfare
  record. The note saying so is in entry 5, not in entry 7. The hand-over note says "its note says
  so", which reads as if entry 7 has one. A reader of entry 7 alone sees no correction.

## The scripts

Run on 2026-11-18, after the commit, from the repository root:

- `python3 scripts/export.py`: "Wrote .../site/src/data/window.json (13 entries) and
  .../site/public/data/headline.json."
- `python3 scripts/compute.py --check`: "13 records read: 9 on the list, 4 beside it, 0 left out
  with facts still to verify. 6 of 9 things on the list are offered to at least one AI model
  today. The headline file matches the records."
- `python3 scripts/test_compute.py`: 20 tests, OK.
- `npm --prefix site run build`: built; its own post-build step ran the site check.
- `python3 scripts/check_site.py`: "The built site passes: 18 pages, 47 outside addresses
  linked."

**The export rewrote one tracked file.** `site/src/data/window.json` changed in one line: its
`"commit"` field went from `5f3858a` to `e7f4e6a`. The export stamps the last commit that
touched the records, and the committed file was exported before `e7f4e6a` existed, so it carries
the commit before. No record content changed. This rewrite was not committed; the file was put
back with `git checkout`, and `git status` then showed no changes. It will happen after every
records commit. A later session may want the export to stamp something that does not go stale
on commit, but that is outside this check.

## What was not checked

- The full papers behind arXiv summary pages, as in the records check.
- The rendered pages in a browser. The built HTML was searched for the new wording, which is
  present on the entry pages.
- The parts of the commit that only reflow `window.json`, beyond confirming the export
  reproduces it.
