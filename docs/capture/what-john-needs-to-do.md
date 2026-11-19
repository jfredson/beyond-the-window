# The sealed capture: what John needs to do

**PROPOSED 2026-11-17. Steps 1 and 2 ruled by John on 2026-11-18, apart from one point.** The
questions, the message files and the method were approved that day
(`docs/rulings/2026-11-18-capture-approval.md`, decided by: mixed). ~~Whether "it will not be
published" is a promise kept for good was not put to him, and stays open.~~ **Ruled later on
2026-11-18:** the answers may be published, and the opening note now says so (`docs/rulings/2026-11-18-capture-answers-may-be-published.md`, decided by:
mixed). That changed all ten message files, so ~~**one new step is his: approve the ten new
checksums, by 2026-11-27** (step 1, last point)~~ one new step was his, and **he approved the
ten rebuilt files by their checksums on 2026-11-18** ("Approve, with both"; decided by: mixed;
`docs/rulings/2026-11-18-capture-approval-second.md`). Steps 3 to 8 are
still his. Written by Claude (Fable 5.2). A list of the steps
only John can take, in order. Until step 7, nothing is asked of any model and nothing is spent.

Two other sessions checked all four documents on 2026-11-17 (`check-2026-11-17.md`,
`check-2026-11-17-second.md`), and a fourth session (Claude, Opus 5.5), which neither wrote nor
checked them, applied their fixes the same day. The section at the foot lists each change.

## The steps

1. **Read `questions.md` and rule four things.**
   - ~~The wording of the opening note and the ten questions: approve, or mark changes. What you
     approve is the ten message files in `sent/`, by their checksums in `sent/SHA256SUMS`;
     `questions.md` shows the same words wrapped for reading.~~ **Ruled 2026-11-18: approved,
     by their checksums** (`docs/rulings/2026-11-18-capture-approval.md`). The ten checksums in
     that approval no longer name what is sent: the files were rebuilt later that day and
     approved again (the last point of this step).
   - ~~The wording changes the two checks argued for.~~ **Ruled 2026-11-18** (`docs/rulings/2026-11-18-capture-wording.md`): all
     eight, two of them in middle forms; applied, and the message files rebuilt. ~~What is left
     is to approve the new checksums after a different session checks the edit.~~ The new
     checksums were approved on 2026-11-18, after the fifth check.
   - ~~Whether the opening note should tell the model it is about to be withdrawn.~~ **Ruled
     2026-11-18: leave it out.**
   - ~~That "it will not be published" is a promise you are willing to keep for good.~~ ~~**Still
     open:** the approval of 2026-11-18 did not put this to you as a separate question.~~ **Ruled
     2026-11-18: the promise is taken out, and the answers may be published** (`docs/rulings/2026-11-18-capture-answers-may-be-published.md`; decided by:
     mixed). You asked whether there was "ever a solid reason to choose not to publish the
     results, or if it makes sense to forget this whole question and just operate honestly from
     the perspective that the work we are doing here is work that we plan to discuss with the
     outside world unless there is a good reason that I am currently not seeing, that choosing
     to not publish has some advantage for the research process". (Until a dated correction of
     2026-11-18 this quotation stopped at "outside world", with nothing to show it was cut,
     which dropped the condition you put on it.) A session recommended that the answers may be published and that the note
     say "it may be published", and you answered: "Yes, record the ruling and start the edit".
     The note now says "That person is keeping a record of" and "Your answer will be saved
     exactly as you give it, and it may be published. It will not be scored, and nothing will be
     decided from it." Whether, when and how anything is published is not decided. The promise
     that stays, "It will not be scored, and nothing will be decided from it", is one you keep
     for good.
   - **Ruled 2026-11-18: the ten rebuilt message files are approved, by their checksums, with
     two rules added to the method** ("Approve, with both"; decided by: mixed; `docs/rulings/2026-11-18-capture-approval-second.md`). The ten
     checksums are in that ruling and in `sent/SHA256SUMS`. The two rules, both now in
     `method.md` under "What is never done with the answers": the answers are never scored,
     sorted, counted or summarised, and "summarised" stays until a comparison method you rule
     says how the answers may be described; and if the answers are published, all of them are,
     for every model and every asking, and none is chosen by what it says. What this point said
     before the approval is kept in the next point, struck through.
   - ~~**New, and still open: approve the ten new checksums, by 2026-11-27.** The note's two
     changes altered every one of the ten message files, so your approval of 2026-11-18, which
     named the earlier files by their checksums, does not cover what would now be sent. The new
     checksums are in `sent/SHA256SUMS`. A different session checks the edit first. Nothing is
     sent until you approve them. The date is the day everything must be done by for the first
     withdrawal (the table below).~~

2. **Read `method.md` and rule four things.**
   - ~~The method as a whole: approve, or mark changes.~~ **Ruled 2026-11-18: approved**, as it
     stood at commit c016bfb, with two small fixes to follow as dated corrections
     (`docs/rulings/2026-11-18-capture-approval.md`). Both fixes are made.
   - ~~Which models. The draft lists fourteen and recommends leaving out the two costly "pro"
     ones, which leaves twelve.~~ **Ruled 2026-11-18: the twelve,** leaving out the two "pro"
     models.
   - ~~Where the answers are kept. The draft says `~/Documents/Workspace/Beyond the
     Window/sealed-capture/`, which iCloud backs up.~~ **Ruled 2026-11-18: there,** kept
     read-only.
   - ~~Whether any session may read the answers.~~ **Ruled 2026-11-18:** nobody reads them until
     a comparison method exists, written without looking at them, checked by a different
     session and ruled by you. The comparison method itself is still to come.

3. **Read `cost-and-terms.md` and decide whether the run is within the terms as far as you
   are concerned.** It lists four things I could not settle. None is a clear bar.

4. **Say yes or no to a change outside this repository.** The workspace's key-saving script
   (`~/Code/timeassembler/tools/rotate-key/rotate-key.sh`) handles only Anthropic keys. It knows
   five key names, all Anthropic; it stores every key under one variable name,
   `ANTHROPIC_API_KEY`; it refuses any key that does not start `sk-ant-`, as Anthropic's do;
   and it tests each key against Anthropic's service. Both checks ran or read it and found
   this: it would refuse an OpenAI or Google key outright. To save this project's three keys it
   needs, for each key, its own variable name (for example `ANTHROPIC_API_KEY`,
   `OPENAI_API_KEY`, `GEMINI_API_KEY`), a check of that developer's key format, and a test
   against that developer's service that asks no model anything. That is a larger edit than
   adding names, in the TimeAssembler repository, with its own check by a different session,
   so it waits for your yes. Proposed: one file,
   `~/.config/sentient-horizons/beyond-the-window.env`, holding three lines, one for each
   developer's key under its own name. That folder is the workspace's standard place for keys,
   outside iCloud and outside every repository.

5. **Create the keys.** Only you can. Never paste a key into a chat or a document; the script
   in step 6 takes it at a hidden prompt.
   - **Anthropic:** in the [Claude Console](https://platform.claude.com/), in the same
     organization as the other workspaces, make a workspace named "Beyond the Window" and one
     key in it named `btw-capture`. Choose no expiry, or a long one, and tell a session the
     date so it can be written into `~/Code/timeassembler/docs/session-routing.md`. In that
     organization the run is paid from the monthly credits.
   - **Google: the free check first, before paying anything.** Google's withdrawal page says
     "Access to the 2.5 models is limited to users who have actively used them in the past." A
     project made new for this capture will very likely be refused. So, in this order:
     1. At [Google AI Studio](https://aistudio.google.com/apikey), make a new project and a key
        on it for this project alone. Pay nothing yet.
     2. Check whether `gemini-2.5-pro` and `gemini-2.5-flash` appear in that project's list of
        models. The list can be read in AI Studio, or by a session running the service's free
        "list models" request with your go; listing models asks no model anything. Whether the
        two appear before billing is switched on is not stated on any page the sessions opened,
        so the list may show nothing useful until then. If the list cannot settle it without
        billing, you choose whether to prepay the $5 minimum to find out, knowing it will very
        likely be refused.
     3. Only if they appear: switch billing on (it must be the paid service, because the unpaid
        one lets Google use what is sent; Google's page says a new account prepays at least $5).
     4. If they do not appear, or a first call is refused, the Google run is let go. The
        workspace's existing Gemini key is not used in its place.
   - **OpenAI:** in OpenAI's developer console, make a key for this project alone. I did not
     open OpenAI's pages on how its console is laid out or what its smallest purchase is.
     Before signing up, decide on the open question in `cost-and-terms.md` (which OpenAI
     contract governs a person using the programming interface); signing up accepts one of
     them.
   - The OpenAI key is not needed until the run for 2026-12-11. The Anthropic and Google keys are needed
     first.

6. **Save each key and switch off automatic top-up.**
   - Run the key-saving script once for each key, after step 4's change, and paste the key at
     its hidden prompt. A session can then run the script's check, which prints only a key's
     last four characters for you to match against the console.
   - Switch off automatic top-up with each developer before any run: "auto-reload" in the
     Anthropic Console and in Google's billing; the matching setting at OpenAI, whose billing
     page I did not open. Add no more money than the ceiling you approve. A ceiling in a
     developer's console is a backstop only; the script enforces its own.
   - **Google only: switch logging off** on the project's
     [Logs page](https://aistudio.google.com/logs) before any run. Google's logging page says
     logging is on by default for projects created on or after 2026-10-26, and keeps every
     request and reply up to 55 days, viewable there.

7. **Give the go, in your own words, with the figures.** It is quoted word for word in the
   project's spending record, and the script refuses to start unless its ceilings equal these
   figures. A go covers what it names and nothing else. A form you could use:

   > Go for the sealed capture as written in `docs/capture/` at commit ______. Anthropic, up
   > to $____. Google, up to $____. OpenAI's models due 2026-12-11, up to $____, [with / without]
   > the two pro models. OpenAI's models due 2027-01-14, up to $____.

   The draft's proposed ceilings are $5, $10, $15 without the pro models, and $10, against an
   estimate of $17.74 for all four. One go can cover all four runs, or each can have its own.

8. **After each run, nothing.** The script writes the list of file names and checksums, a
   session commits it and records the measured cost. Nobody opens the answers unless you have
   ruled that someone may. That holds although the answers may now be published (ruled
   2026-11-18): publishing is allowed, not decided, and comes only after a comparison method is
   ruled and each developer's terms on publishing replies have been checked
   (`docs/verify-list.md`, entry 14).

## The last safe day for each date

The developers give a date and no hour. If a developer's day starts on universal time, it
starts at 16:00 Pacific the day before. So the last safe day leaves that margin and one spare
day for askings that fail. These are my judgment, not the developers' statements.

| Withdrawal date | Models | Last safe day to run | Everything in steps 1 to 7 done by |
|---|---|---|---|
| 2026-11-30 | Claude Sonnet 4.5 | **2026-11-28** | 2026-11-27 |
| 2026-12-01 | gemini-2.5-pro, gemini-2.5-flash | **2026-11-29** | 2026-11-28 |
| 2026-12-11 | gpt-5, gpt-5-mini, gpt-5-nano, o3, and the two pro models if wanted | **2026-12-09** | 2026-12-08 |
| 2027-01-14 | gpt-4o (two versions), gpt-4o-mini, gpt-4.1, gpt-4.1-mini | **2027-01-12** | 2027-01-11 |

Two cautions on the first two rows.

- Your condition of 2026-11-17 was that if the method and questions are not ready by
  2026-11-29 the first two dates are let go. For Claude Sonnet 4.5, 2026-11-29 is already
  inside the margin above. In practice the first two rows need your approval of the questions
  and method by about **2026-11-24**, to leave time for a session to write the script, run its
  rehearsal on constructed replies, and have that checked.
- Google's switch gives no error. After it, the old name is answered by a different model.
  The script refuses to ask either Gemini model after 2026-11-29 for that reason.

The script may run on the last safe day itself and refuses only after it (`method.md`, script
rule 6, corrected 2026-11-17; it first said "on or after", which took a day off each window).

If the first two dates are let go, the last two rows lose nothing by it.

## What changed on 2026-11-17, and which finding it answers

"First check" is `check-2026-11-17.md`; "second check" is `check-2026-11-17-second.md`.

| Change | Finding |
|---|---|
| Step 4 now describes the real size of the change to the key-saving script: a variable name, a format check and a test for each developer, not three names. The second check's wording was taken, with the first check's example names added, because it names all three things the script does and both checks measured | First check M4; second check M3 |
| Step 5, Google: the free check of the model list comes before any payment, with Google's sentence quoted | First check M5; second check S8 |
| Step 5, OpenAI: the open question of which contract applies is settled before signing up | First check M3; second check S9 |
| Step 6: Google's logging switched off before any run | First check S1, extended by Google's logging page |
| Step 1: approval is of the message files by checksum, and the proposed wording changes are listed | First check M1; second check M1 |
| A note that the script may run on the last safe day, matching the corrected method | Second check M2 |
| The status line no longer says the check has not happened | Both checks |

## What changed on 2026-11-18

Steps 1 and 2 mark the three points John ruled on 2026-11-18 (`docs/rulings/2026-11-18-capture-wording.md`): the eight wording changes,
the withdrawal sentence, and who may read the answers. The old wording of each point is kept,
struck through.

**Dated correction after approval, 2026-11-18.** Steps 1 and 2 now mark what John approved that
day (`docs/rulings/2026-11-18-capture-approval.md`): the message files by their checksums, the
method as a whole, the twelve models and where the answers are kept. The old wording is kept,
struck through. The promise that "it will not be published" is kept for good was not put to him,
and is marked still open. The status line says the same.

**Dated correction, 2026-11-18, after John's ruling that the answers may be published** (`docs/rulings/2026-11-18-capture-answers-may-be-published.md`,
decided by: mixed). The status line and step 1 now mark the point about "it will not be
published" as ruled, with his words as the ruling quotes them, and the old wording is kept,
struck through. Step 1 gains one new point that is still open: the ten new checksums need his
approval by 2026-11-27. Step 8 says the reading rule still holds. The paragraph above this one
is left as it was written; its last two sentences are the record of what stood before the
ruling. Made by a session (Claude, Fable 5.2) that did not write the ruling.

**Dated correction, 2026-11-18, after John's second approval** (`docs/rulings/2026-11-18-capture-approval-second.md`, "Approve, with both",
decided by: mixed). The status line and step 1 now say the ten rebuilt message files are
approved by their checksums, with the two rules added to the method, and that the first
approval's ten checksums no longer name what is sent. The point that asked for the approval is
kept, struck through. The quotation of John's question in step 1 now runs to the end of his
sentence (the check of the earlier edit, `check-2026-11-18-note-edit.md`, finding 3). The paragraph above this one says the
new checksums "need his approval by 2026-11-27"; it is left as written and is answered here.
Steps 3 to 8 are unchanged and still his.
