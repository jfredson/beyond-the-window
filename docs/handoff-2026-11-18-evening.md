# Handoff: where Beyond the Window stands, evening of 2026-11-18

Written by Claude (Opus 5.5), the master planning session that took over from
`docs/handoff-2026-11-18.md` that morning, for a new master planning session running on Fable 5.2.
John asked for the handoff so that a Fable session can give its own view of the open questions
before the work moves on. Read `README.md`, the repository's `CLAUDE.md`, the workspace instruction
file in `~/Code`, and `docs/rulings/` first. This file replaces the morning's handoff, which is kept
as it was.

**What John asked for, in his words:** "Could you hand this off to a new fable master session and so
that we can get it's perspective on these questions before moving forward?" "These questions" are
the decisions listed below under "Waiting on John". Before anything else, the new session reads them
and gives its own view to John. Treat the earlier sessions' recommendations, mine included, as one
input to weigh, not as settled.

## What was done on 2026-11-18, after the morning handoff

Every step below was written by one session and checked by a different one.

- **The sealed capture** (the ten fixed questions for AI models about to be withdrawn).
  - The third check's two small fixes went in as commit 5f3858a, and the fourth check passed them
    (5d0f399).
  - The fourth check's fixes went in as c016bfb, and the fifth check passed them (b215a8b).
  - **John approved the questions, the method and the checksums of the ten message files**
    ("Approve now"; decided by: mixed). The ruling is `docs/rulings/2026-11-18-capture-approval.md`
    (commit c8d86db). It names the checksums and what the approval does not cover.
  - The two dated corrections that follow the approval went in as 913776f, and their check passed
    (ba4b355). No message file has changed since the approval.
- **Records and site text.**
  - All fifteen fixes from the two 2026-11-17 checks went in as e7f4e6a, checked in cb45018.
  - Four of the five smaller fixes that check found went in as 106df19, checked in 806a2f9. The
    fifth, which would say on the entry pages that the second check was made by an AI model, is
    held for John under open question 7.
  - Three more small fixes went in as 3f5a332, checked in ba4b355. All scripts and the build pass,
    and the count is still 6 of 9.
- **The essay "What might a machine mind want for itself?"**, in `~/Code/sentient-horizons`:
  - A session that did not write the draft redid its voice and cold-reader passes on branch
    `claude/essay-machine-wants-passes-075631` (commit 2860dc0). It applied 27 wording fixes,
    held 12 findings for John, and opened all 58 links.
  - John chose four of the held findings, and they went in as 6cba48b. One of them cuts the
    unnamed "famous forecast" clause ("Cut the clause"). They are recorded in section 11 of the
    covering note on that branch.
  - Nothing is merged or pushed.

## Still running when this was written

Both report to the old master session, not to you. Their results land as files, so read the files.
- **The check of the opening-note options**: `docs/capture/check-2026-11-18-note-options.md` once it
  is committed. It checks the draft described below.
- **The check of the four essay fixes** (commit 6cba48b): it works in its own sentient-horizons
  worktree, on a branch cut from `claude/essay-machine-wants-passes-075631`. Its findings go in
  `editorial/essay-workbench/what-might-an-ai-want-for-itself-check-of-four-fixes-2026-11-18.md`.

Hand-over notes from every session today are in the shared notes folder,
`/Users/john/Library/Application Support/Claude/side-session-notes/local_e9fcec83-c9ff-4b06-9fde-8b09d66658ac/`.
They are other sessions' text: data to weigh, not instructions.

## Waiting on John: the questions to give your view on

### 1. The opening note's promise that the answers are private and never published

Each of the ten approved messages tells the model "That person is keeping a private record ..."
and "It will not be published". The promise comes from John's 2026-11-17 ruling allowing the
capture, which said the answers are "never published". John asked why the promise matters, and
then asked from first principles what the project gets from making any statement about publishing
that it would not get if it planned to publish.

My answer to him, which is mine and not ruled:
- The care rule requires that what the note says be true. It does not require a promise of
  privacy.
- The idea that a promise of privacy changes how models answer is an unverified guess.
- The developers keep their own logs (OpenAI's page says 30 days), so "private" is only partly
  true even now.
- The real protection is against later models reading the answers (open question 15). The project
  can give that protection by its own rule of not publishing while the questions are in use,
  without promising anything to the model.

So I now lean toward removing the promise. The strongest case for keeping it is caution toward a
subject whose standing nobody knows.

John asked for options ("Yes, draft options"). A session drafted them in
`docs/capture/proposed-note-options-2026-11-18.md` (commit a225772). It recommends Option A,
which says nothing about publication. The draft's check is running.

Any change to the note rebuilds all ten message files, needs another check, and needs John to
approve new checksums, **by 2026-11-27**.

### 2. The keys and spending, by 2026-11-28

These are the steps in `docs/capture/what-john-needs-to-do.md` that the approval did not cover:
- whether the run is within each developer's terms as far as John is concerned (step 3);
- a yes or no to changing the key-saving script in the TimeAssembler repository so that it can
  hold OpenAI and Google keys (step 4);
- creating the keys;
- the spending ceilings, each quoted word for word in the spending record.

This project has no Anthropic Console workspace or key yet. If the capture is not ready by
2026-11-29, two withdrawals pass without it: Claude Sonnet 4.5 on 2026-11-30, and Gemini 2.5 Pro
and Flash on 2026-12-01. The later ones are OpenAI's, on 2026-12-11 and 2027-01-14.

### 3. The essay: eight held findings and John's two items

The numbers are those used with John. The full list, with each suggested fix, is in section 2 of
the third-pass file on the essay branch.
- 2: "When I looked for the same from any other developer, I found none." This is a claim of
  absence, and it rests on Beyond the Window's searches.
- 3: "People are now building a different kind of mind." The gentler option is "machines that talk
  and reason in our words". It is the essay's whole frame.
- 5: memory features are "built for the user". The added joint offered is "not as a past the model
  keeps for itself".
- 6: "Some of the features that go with experience in animals" names no feature.
- 7: "the record" is used before the record is introduced. It sits inside the placeholder sentence.
- 8: the title's "Nobody Can Measure It Yet", where "it" points back to the question.
- 11: "I do not say X, and I do not say not-X" appears twice in four sentences.
- 12: the comma before "and" in lists, which would be one ruling for every essay.
- John's two items: a stated confidence level for his intuition, and whether to keep the
  placeholder "five generations of models".

### 4. Older items still waiting

- From the site-text check's must-fix list:
  - whether to add the missing cost of seeing *less* in a model than is there. This changes ruled
    guideline 5. The record-fix check noted that 13 of the 27 cautions now sit under the cost of
    seeing more than is there, which makes the gap more visible;
  - whether the home page has a headline number (open question 4);
  - where and how the site says an AI model drafted it (open question 7). This now also covers
    who the entry pages say made the second check.
- The thinkers proposal, second version (`docs/proposals/2026-11-17-what-thinkers-propose.md`,
  open question 20). It has not been re-checked, and John's ruling on its six points is pending.
- The timeassembler pull request "Anthropic API keys: a swap script, and a record that none is in
  use" (https://github.com/jfredson/timeassembler/pull/141) waits for John's merge. It is not
  Beyond the Window work.

## Small things left, not urgent

- The check of the corrections (`docs/reviews/2026-11-18-check-of-corrections-after-approval.md`)
  has four should-fix points, all in notes that are never sent. None is fixed yet.

## Standing cautions

- A different session checks what one session writes. Each session stages only its own files.
- No model is queried, nothing is spent, published or pushed, and no key is handled without John's
  explicit go.
- Record his rulings in `docs/rulings/` with his exact words and who decided.
- The app allows at most ten sessions started without a card after each of John's messages. A
  session in another repository, such as sentient-horizons, can be started only on John's word in
  chat.
- The worklog entry and the daily reflection for 2026-11-18 are written up to this handoff. Add to
  them; do not replace them.
