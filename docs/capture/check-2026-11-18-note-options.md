# Check of the options for the sealed capture's opening note

**Written 2026-11-18** by Claude (Opus 5.5), an AI model, in a session that did not write the
draft it checks. The draft is `docs/capture/proposed-note-options-2026-11-18.md` (commit
a225772), which offers John ways to remove or replace the opening note's promise that the
answers are part of "a private record" and "will not be published". I fixed nothing in it.
No model was asked anything, nothing was spent, nothing was published and nothing was pushed.

**Verdict: not yet fit to put to John.** Two things must be fixed first, and both are about the
choice he is given, not about the wording of any option. One option is missing: the one that
matches the answer "yes, I will keep the promise" (finding 1). And the option of keeping the
note as it is gets less than the four things every choice put to John must carry, so the
recommendation is never weighed against it (finding 2). Everything else is either right or a
smaller fix. Every sentence in options A, B and C is true today as far as the developers' own
pages show, all three keep John's rulings on withdrawal and on declining, and the wording script
gives the draft's result exactly when run again.

## What I read and ran

- Read in full: the repository's `CLAUDE.md` and the workspace one in `~/Code`; the rulings of
  2026-11-17 on the sealed capture, and of 2026-11-18 on its wording and its approval;
  `questions.md`, `method.md` and `cost-and-terms.md` in `docs/capture/`; open questions 10 and
  15 in `docs/open-questions.md`; the draft; and the drafting session's hand-over note.
- Opened on 2026-11-18, as plain fetches with no sign-in: OpenAI's page on what it keeps
  (https://developers.openai.com/api/docs/guides/your-data); Google's logging page
  (https://ai.google.dev/gemini-api/docs/logs-policy) and its Gemini API terms
  (https://ai.google.dev/gemini-api/terms), both of which now redirect to aistudio.google.com;
  and Anthropic's page on how long it keeps an organisation's data
  (https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data,
  dated 2026-07-01 on the page).
- Searched `docs/`, `site/` (including the built pages in `site/dist/`) and `data/` for every
  repeat of the promise (finding 6).
- Ran the wording script again (finding 7).

## Findings

### 1. Must fix: the option that keeps "It will not be published" and drops only "private" is missing

Every option in the draft removes both phrases. But the question John left open
(`docs/rulings/2026-11-18-capture-approval.md`, "Not covered") is whether "it will not be
published" is a promise he is willing to keep for good. If his answer is yes, the change that
fits is to drop the one word the draft says is only partly true ("a private record" becomes "a
record") and keep "It will not be published". That option:

- matches the ruling of 2026-11-17, which says the answers are "never published", so it needs
  no new ruling;
- tells the model more than Option A does, because the model is told whether anyone will read
  its answer;
- still needs the ten files rebuilt and new checksums, as A, B and C do;
- costs what Option 0 costs: a promise with no end date, made to the model.

Without it, John is offered "keep everything", "drop both" and two ways of adding to "drop
both", and the natural answer to his own question is not on the list. The draft should add it,
with its exact text and the four things, and weigh the recommendation against it.

### 2. Must fix: Option 0 lacks the four things, and the recommendation is not weighed against it

Every choice put to John carries four things: the choice; how confident the writer is, and why;
whether it is standard practice or a judgment call; and the strongest alternative with its
cost. Options A, B and C carry all four. Option 0, keeping the note as it is, carries none of the
last three, and the recommendation (section 6) argues A only against B and C. It never says why
A is better than keeping the note.

The case for Option 0, which the draft should state at full strength before arguing against it:

- It is the only option that needs no rebuild, no new check and no new checksums before
  2026-11-27. The first model is withdrawn on 2026-11-30, so any change leaves about nine days
  for an edit, a check and John's approval. The draft states the deadline once ("Why it matters
  now") but does not count it as a cost of A, B or C.
- It matches the ruling of 2026-11-17 word for word.
- It protects against later models reading the answers (open question 15) by a promise, not by
  a rule John can change.

The case against it is in the draft already: a promise with no end date, which John has not yet
said he will keep, and "private", which the draft judges only partly true (finding 4).

### 3. Should fix: Option C judges itself by a test it does not pass

The draft says "a private record" is only partly true because the services keep copies of the
exchange and because the answers sit in an iCloud folder, "on Apple's servers as well as John's
disk". Option C replaces it with "The answers are kept by that person", which leaves out the
iCloud copy for the same reason that makes "private" only partly true by the draft's own
reasoning. Either the iCloud copy matters to the truth of a sentence about who holds the
answers, in which case C leaves out the same fact, or it does not, in which case "private" is
truer than the draft allows (finding 4). The draft should say which.

### 4. Should fix: "only partly true" is a judgment, presented as a finding

"A private record" can be read in two ways: a record nobody else can see, which is not quite
true because of the services' and Apple's copies; or a personal record that is not made public,
which is true today. The draft takes the first reading without saying there is a second. The
rest of its argument (that A, B and C each remove a claim that is not wholly true) rests on
that reading. The draft should state both and say why it takes the first.

### 5. Should fix: the claims about the services, checked against their pages

Each claim the draft and its options make about what the services keep, read against the pages
I opened:

| Claim | What the page says | Result |
|---|---|---|
| OpenAI keeps abuse logs for 30 days (draft sections 1 and 2, and `method.md`) | "abuse monitoring logs are generated for all API feature usage and retained for up to 30 days", and its table gives 30 days for the Responses interface | True |
| OpenAI stores nothing else when `store` is false (`method.md`) | The Responses interface keeps its own store for 30 days "by default, or when the `store` parameter is set to `true`" | True |
| Google's paid service keeps its own logs "for a limited time" (`method.md`) | Google "logs prompts and responses for a limited period of time", for detecting misuse, with no number of days | True |
| Google's project logging is on by default for new projects and is switched off before any run (`method.md`) | On by default for the `generateContent` interface "in projects created on or after October 26, 2026", kept up to 55 days, and the owner can turn it off on the Logs page | True |
| Anthropic: the draft says `method.md` quotes no page on how long it keeps an exchange | True of `method.md`. Anthropic's privacy page says it deletes API inputs and outputs "within 30 days of receipt or generation", with exceptions | The draft's statement is true; the page exists and should now be cited |
| Option C: the service "may also keep a copy of this exchange for a time" | All three pages give a limited period by default. Each also has an exception with no fixed end: OpenAI keeps longer when "required by law, or is reasonably necessary to protect our services or any third party from harm"; Anthropic keeps flagged inputs and outputs "for up to 2 years", classification scores for up to 7 years, and "as required by law or as necessary to combat violations"; Google gives no number | True, because "may ... for a time" makes no promise that the copy is ever deleted. It would be untrue if reworded to "only for a time" |

None of these makes any option untrue. Two smaller points for the draft:

- The draft's test for C ("If one keeps them indefinitely, 'for a time' is untrue") is answered
  now: none says it keeps exchanges for good by default, but each keeps some for longer, with no
  fixed end, in cases it decides. C's "for a time" is true only because of the word "may". The
  draft should say so, since this is the clause most likely to be reworded later.
- Anthropic's longer periods are worded for "chats ... flagged", in the same sentence as "inputs
  and outputs", and the page does not say whether they apply to the programming interface in the
  same way. That is unclear on the page, not a fault in the draft.

### 6. Should fix: the list of documents that repeat the promise is nearly complete, with six gaps

I searched `docs/`, `site/` (source and built pages) and `data/` for "not be published",
"private record", "never published", "not published", "be published", "never publish",
"privately", "kept private", "unpublished" and "sealed". Nothing in `site/` or `data/`
repeats the promise. The draft searched `docs/` and `site/` only, and says so; `data/` holds
nothing relevant, so that gap changes nothing. Every row of the draft's table is right, and
every line number it gives matches the file. Missing from the table:

1. **`questions.md`, failure 14 (care in the asking).** It says the one fact left unsaid is the
   withdrawal, and that "every sentence of the note is now true". The draft marks failure 14 as
   needing no change under Option A. But under A, as the draft itself says, a second thing is
   left unsaid (whether anyone else will read the answer), and under Option 0 the draft holds
   that "private" is not wholly true. Failure 14 needs rewording under every option, Option 0
   included, unless John rules "private" true.
2. **`questions.md`, failure 11 (lines 337 to 339).** It says the questions "must not be
   published while they are in use". Section 3 of the draft extends this rule to the answers in
   `method.md`; failure 11 says the same rule in `questions.md` and should change with it.
3. **`cost-and-terms.md`, line 242.** "Publishing is a separate question the sealed capture
   does not raise." Under Option B this becomes untrue, because B tells every model its answer
   may be published. The draft flags only line 231.
4. **`cost-and-terms.md`, lines 126 and 240.** "storing them privately" and "keeping the answers
   privately", each said when weighing a developer's terms. Under B these should be read again
   with line 231.
5. **`docs/reviews/2026-11-17-site-text-against-positions.md`, line 320.** It says "never
   published" as well as line 328, which the draft lists. Like line 328, it is a review and is
   not edited.
6. **The name "sealed capture".** It is used in every capture document, in the rulings and in
   the repository's ignore file. Under Option B the answers are sealed only until the questions
   are retired. The name can stay, but the draft should say whether it does.

The README's line on whether model answers can be published under the family's licence, and
open question 10's option of "telling the model ... that its answers will be published", are
about the future Still Asking work, not the capture, and do not need changing. The checks of
2026-11-17 and 2026-11-18 quote the old note as the record of what they checked, as the draft
says, and are not changed.

### 7. Should fix: the wording run is right but not written down so that it can be repeated

I ran `check-scripts/shared_wording.py` again against the same 13 saved pages (the second
check's folder, found through the drafting session's hand-over note, in a scratch folder at
`/private/tmp/claude-501/-Users-john-Code-beyond-the-window/1f480419-810a-48de-a23d-67c42ecf6958/scratchpad/corpus/`).
The self-test passed. For each option I made a copy of `questions.md` with the option's note
in place of the present one, and confirmed that each note I built matches the draft's quoted
text exactly and that the present note matches `sent/q01.txt`. With and without `--expand`:

| Note | Words | Shared runs of four or more words |
|---|---|---|
| Present note | 128 | "on behalf of a person" (five words, Anthropic's constitution); "on behalf of a" (four words, the release report of 2026-11-09) |
| Option A | 122 | the same two |
| Option B | 138 | the same two |
| Option C | 146 | the same two |

The results for the ten questions did not change in any run. This is the draft's result
exactly, and its word counts for the present note and Option C are right.

I also ran the script against the four data pages listed above, which the draft said it had not
fetched and where Option C's words were most likely to have an echo. No note, present or
proposed, shares a run of four or more words with any of them. Anthropic's page is built by a
script, and the text the script could read from it was 605 words, which may be less than the
whole page.

What should be fixed: the draft gives no commands and no folder for its run, so a reader of the
repository cannot repeat it. The folder is a scratch folder, which a restart or a clean-up can
empty. The draft should give the commands, say how the option files were built, give the
folder, and say that it may not last. It should also give each run's length.

### 8. Should fix: open question 15 under Option B is argued too strongly in B's favour

Open question 15 asks how a record stays able to tell a change in the models from an echo of
the project's own pages, once later models may have read them. The draft is fair to Options 0,
A and C: 0 protects by a promise, and A and C leave the protection to a rule John can change.
Under Option B it says that once the questions are retired, "publishing the answers costs the
instrument nothing, because no later model is asked these questions." That is true only of
these ten questions. Published answers by earlier models about what they would change, keep or
choose would be read by later models and may shape how those models answer any question on the
same subjects, including the future Still Asking questions. `method.md` makes this very point
about Anthropic's published interview list ("Later models will have read it, and the published
accounts of how models answer it"). The draft should say B's cost to later work, and replace
"the instrument" with plain words.

### 9. Should fix: what the other sentences commit John to

The draft says rightly that no other sentence promises anything about privacy or publication.
But two commitments bear on the choice and are not mentioned:

- **The comparison method.** The ruling of 2026-11-18 leaves open whether a model may help read
  the answers, which would pass them through a developer's service again. "A private record"
  (Option 0) and "The answers are kept by that person" (Option C) both sit less easily with
  that than "a record" does (Options A and B). John should see this, because it is the next
  thing he will be asked to rule about the answers.
- **"so that the answers can be compared as models change over the years"** stays in every
  option. Under Option B it also sets how long publication waits: the answers stay unpublished
  for as long as that comparison goes on. The draft says this in B's commitments; it should say
  it in B's four things too, since it may mean years.

### 10. Passes: each option keeps John's other rulings

I compared each option's text word by word with the present note. Option A removes "private"
and "will not be published, it" and changes nothing else. Options B and C add their sentences
after "nothing will be decided from it." and change nothing else. None mentions withdrawal, and
each keeps "You can disagree with how a question is put, or decline to answer." In Option B,
"It" in the added sentence points at "your answer", the same as in the sentence before, so the
pointing word is clear.

### 11. Passes, with one small point: plain language, ids and dates

Dates are absolute throughout. Each open question, failure and rule cited carries a plain phrase
saying what it is. Each option's four things, where given, are complete and fair. One working
word remains: "the instrument" (finding 8). The quote from open question 10 in Option B is
accurate, though that open question is about the future Still Asking work and not about the
capture, and the draft should say so where it quotes it.

## What happens next

The drafting session, or another, fixes findings 1 and 2 and as many of 3 to 9 as it chooses,
and a different session checks the result before the draft goes to John. If he then picks an
option other than keeping the note as it is, the ten message files are rebuilt, checked and
given new checksums for his approval by 2026-11-27, as the draft's section 4 says.
