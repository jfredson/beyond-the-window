# Check of the records made before the Google run

Written 2026-11-20 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session wrote none of the files checked. They are the commits on `main`
that are not yet pushed, other than my own earlier verdict:

- the mends to the note on the free check (`docs/capture/google-free-check-2026-11-19.md`,
  commit `d6915aa`);
- the new note on the Google project's setup (`docs/capture/google-project-setup-2026-11-20.md`,
  commit `daa55db`);
- the rulings in `docs/rulings/` dated 2026-11-20, and the paragraph added to
  `docs/capture/cost-and-terms.md` (commit `9b86612`).

I changed none of them and pushed nothing.

*Added 2026-11-20 by the master planning session, which did not write this check:* this check's
first mend asked whether three further details of John's billing account in the setup note
might be public. John asked what they had to do with the project, they were taken out of the
note, and on his word ("Yes, rewrite them") the commits not yet pushed were rewritten so the
details never reached the public repository. This check quoted those details, so seven places
in it were reworded or cut by the master session, each marked in square brackets where the
sense changed. Nothing else in the check was changed, and its verdict stands as written.

**What this check cannot vouch for.** I could not see Google's pages and did not try to. Every
fact read from them is the master planning session's to answer for: that the project was
joined to a billing account, what the notices said, how the switches stood, and what the list
of limits shows. I also did not hear John's words. I checked that each ruling quotes them,
keeps them apart from the session's, and claims no more than they cover.

## Verdict

**Fit to push after two mends, one of which is a question to John.** The mends to the first
note do what was asked. The rulings quote John's words, keep them apart from the session's,
and say honestly who decided. The ceiling ruling does not read as a go to spend. The setup
note keeps "the limits are above zero" apart from "Google will answer a call".

### The two mends

1. **The setup note says more about John's Google account than his ruling covers.**
   *File:* `docs/capture/google-project-setup-2026-11-20.md`, point 3 under "What was done".
   *Sentences:* three sentences in that point, not quoted here. [Taken out: the sentences
   stated three details of John's billing account.]
   *What is wrong:* the ruling
   (`docs/rulings/2026-11-20-google-account-facts-may-be-public.md`) covers two facts: that
   the account has a billing account on the paid service with other projects on it, and that
   one of them used Gemini 2.5 Flash in the 28 days before 2026-11-19. It lists the balance
   under "Not covered", and says of the two notes, "Neither note names another project, a sum
   of money or a balance." The setup note gives no figure, but it does state three further
   facts about the account. [Taken out: what the three facts were.]
   *Suggested fix:* one question to John, naming the three facts. If he says yes, the ruling
   gains a dated line with his words, and its sentence about the two notes is corrected. If he
   would sooner not, point 3 can say only that the session read the billing page, changed
   nothing, and found that a run within the ceiling needs no new payment.
2. **The setup note differs from the step list in one place and does not say so.**
   *What the step list says* (`docs/capture/what-john-needs-to-do.md`, step 6): "Add no more
   money than the ceiling you approve. A ceiling in a developer's console is a backstop only;
   the script enforces its own."
   *What is different now:* the project draws on money already with Google, and the account is
   not one that holds no more than the ceiling. [Reworded: a detail of the account taken out.] So the backstop the step list had in
   mind, an account holding no more than the ceiling, is not there. The script's own limit of
   $10 is the only thing that stops the run.
   *Suggested fix:* two sentences in point 3. One says this and names the step. The other says
   that "no new payment" does not mean no cost: whatever the run costs comes out of John's
   pocket. [Reworded: a detail of the account taken out.]

### Smaller points

- **Five rulings were named and four files exist.** The four are the terms, the ceiling, the
  key-saving script and the account facts. John's fifth word that day, "Yes, existing
  account", is recorded only inside the setup note. It is quoted and marked "decided by:
  mixed" there, so nothing is lost, but every other word of his has a file of its own in
  `docs/rulings/`.
- **Two sentences were overtaken by the ceiling ruling in the same push.** The terms ruling
  says "The spending limit ($10 is proposed)", and the note on the free check says "$10 is
  proposed and not approved". Each was true when written, and the ceiling was ruled next. A
  dated line under each would save a reader the puzzle.
- **"This confirms the reading ... that the zero meant the paid service was needed."** The
  limits rising above zero once the project joined the paid service is good support for that
  reading, and it is still a list of limits. "Bears out" would claim a little less than
  "confirms". The next paragraph already says the list does not show a served call.
- **The session's reading of the key rule** (that sharing a billing account is within the rule
  that calls never go through another project's key) is marked as the session's own, which is
  right. It was part of what John said yes to, so it rests on "mixed" and not on his own
  words.

## 1. The mends to the note on the free check (commit `d6915aa`)

| What the earlier check asked | Done? |
|---|---|
| Mend 1: say that a list of every model would show the rows to any project, and that "very likely refused" stands until a first call | Yes, under "What follows", and the choice to pay is left to John "on the same footing as before the check" |
| Mend 2: "the zero says" softened | Yes: "most likely means", with both things it does not say |
| Name the page behind "the same page" | Yes: "the usage figures AI Studio shows for the account's projects" |
| Why a free call would not answer for the smaller model | Yes, with the place in the cost and terms document |
| The names the plan sends were not seen | Yes, as a new point |
| Logging, John's go and the last safe day | Yes, in a closing paragraph |

**Did anything added go too far?** No. The new sentences claim less than the old ones. The
opening line now says the note was checked and "mended as that check asked", which is true.

## 2. The note on the project's setup (commit `daa55db`)

**Does it claim only what the pages can show?** Yes, apart from the word "confirms" above. It
quotes Google's own notices for the joining, says which switch was already off and which it
turned off, and says "No screen asked for a payment" where it could have said nothing was
charged. It repeats that the list "still does not show that Google will answer a call".

**Does it agree with the other three documents?**

| Point | The note | The other documents | Agree? |
|---|---|---|---|
| Billing on the paid service | Joined to an existing billing account, no payment | Step 5: "switch billing on (it must be the paid service ...)". Cost and terms: a new account prepays "a minimum of $5" | Yes. The note gives the new account as the alternative put to John |
| Logging | Both switches off, one of them already off | Step 6 and cost and terms: logging is on by default for new projects | Differs, and the note says so and says it was not looked into |
| Automatic top-up | Read, and left alone | Step 6: switch it off before any run | Yes |
| Money in the account | Not limited to the ceiling | Step 6: "Add no more money than the ceiling you approve" | Differs, and the note does not say so (mend 2) |
| The ceiling | "ruled at $10" | The plan holds 10.00. Its comment still says proposed, which is known and for another session | Yes |
| The last safe day | 2026-11-29 | The plan and the step list | Yes |
| Whether Google will serve the models | "very likely be refused, stands until a first call" | Cost and terms, and the mended first note | Yes |

**Anything that should not be public?** No key, no id, no name of a billing account or of
another project, and no figure for the balance. What goes beyond John's ruling is in mend 1.

## 3. The rulings and the added paragraph

| Ruling | John's words quoted, and kept apart | "Decided by" | Does it claim more than his words cover? |
|---|---|---|---|
| The Google run is within Google's terms | "Yes, within terms", after the question as put. What the session told him and what was not settled are in their own parts | Mixed, and it says he "decided as the customer" | No. It rules the run as described to him, and lists publishing, the unread document and whether Google will serve the models as not covered. It says the session did not reopen the terms page that day |
| The ceiling is $10 | "Yes, $10", after "Set the spending limit for the Google run at $10?" | Mixed | No. Its first line under "Not covered" is "This is not the go to spend", with the reason: his words answer a question about the limit and name no developer. The spending record holds no line for Google |
| The key-saving script takes a Google key | "Yes, change the script", with what a yes covers set out before it | Mixed | No. The merge, the key and the go stay his, and an OpenAI key is named as not ruled |
| Two facts about his account may be public | "Yes, that can stay in the public repository" | Mixed, with who raised it | The ruling itself does not. Its sentence "Neither note names ... a balance" does not hold for the setup note, which speaks of the balance (mend 1) |

**The paragraph added to the cost and terms document** gives the question, his answer, who
decided and the ruling's file, and ends with the two things the ruling does not cover. It adds
nothing to his words.

**The quotations from Google's terms** in the terms ruling match the cost and terms document
word for word. The figures in the ceiling ruling match it too: $3.79 expected, 100 exchanges
for two models, $10 proposed.

## 4. Language

Dates are absolute, there are no long dashes, and the plan's name for the run
(`google-2026-12-01`) carries a plain phrase each time. "Nine days" in two rulings stands
beside the date it counts to.

## What I did not do

- I did not open Google's pages or look at any key, by instruction.
- I did not check the facts read from those pages against anything but the repository's own
  documents.

**Fit to push after two mends: ask John whether the three further facts about his Google
account in the setup note may be public or take
them out, and say in that note that the account holds more than the ceiling, so the script's
own limit is the only stop and the run's cost comes from his pocket. The facts read from
Google's pages are the master planning session's to answer for.**
