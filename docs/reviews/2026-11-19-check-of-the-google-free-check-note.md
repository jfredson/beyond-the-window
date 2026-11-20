# Check of the note on the free check before the Google run

Written 2026-11-19 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session did not write the note (`docs/capture/google-free-check-2026-11-19.md`,
added in commit `8aa4920`) and did not make the check it records. I read the note against the
capture's cost and terms document, its plan and its step list for John. I changed nothing and
pushed nothing.

**What this check cannot vouch for.** I could not see the Google page and did not try to open
it. Every fact the note reads from that page is the master planning session's to answer for:
that the project was made, that it has no key and no billing, the rows and limits listed, and
what was seen of the account's other projects.

## Verdict

**Fit to push after two small mends.** The note keeps "the model is listed" apart from "Google
will answer a call", and says so in its own section. It holds no key, no project id and no
name of any other project. Two sentences say a little more than a list can show, and both sit
where John will read them before deciding whether to pay.

### The two mends

1. **"They appear" reads as the step's condition being met, and the note's own words suggest
   the list is the same for every project.**
   *Sentences:* "switched on 'All models', which lists every model with the project's limits
   for it", and under "What follows": "only if the models appear, switch billing on. They
   appear."
   *What is wrong:* a list of every model shows a row to any project, new or old. So the two
   rows being there says little about whether this project will be served. The step list
   (`what-john-needs-to-do.md`, step 5) already warned of this: "the list may show nothing
   useful until then", and "you choose whether to prepay the $5 minimum to find out, knowing it
   will very likely be refused." The cost and terms document still says "very likely refused"
   (Part 3, Google). The note differs from both in tone and does not say so.
   *Suggested fix:* under "What follows", say that the rows appear, that a list of every model
   would show them to any project, so the check did not settle whether the project will be
   served, and that the earlier documents' "very likely refused" stands until a first call is
   made. Then the choice to pay is John's on the same footing as before.
2. **"So the zero says the model needs the paid service."**
   *What is wrong:* a list can show that the zero is shared with other larger models that are
   not being withdrawn. That makes "needs the paid service" the likely reading. It does not
   establish it, and it cannot rule out that this project is also refused.
   *Suggested fix:* "so the zero most likely means the model needs the paid service. By itself
   it does not say the project is refused, and it does not say the project will be served."

### Smaller points, for whoever next touches the note

- **"by the same page"** in the last bullet of "Two things seen in passing": no page is named
  in that part, so a reader cannot tell which page showed the 28 days of use. Name it.
- **"Only a first real call on the paid service answers it."** The list gives Gemini 2.5 Flash
  limits on the unpaid service, so a reader may wonder why a free call would not answer for
  that model. The reason is in the cost and terms document: the unpaid service lets Google use
  what is sent, so it "must not be used here". One clause would close the gap.
- **The names.** The list shows the names "Gemini 2.5 Flash" and "Gemini 2.5 Pro". The plan
  sends `gemini-2.5-flash` and `gemini-2.5-pro`, and marks the name the service reports back
  as not checked. The note could say that the list did not show those names, so that point is
  still not checked.
- **"What follows" leaves out three things the step list holds:** logging is switched off on
  the project before any run (step 6), John's go with the figure is still needed (step 7; the
  $10 limit for this run is proposed and not approved), and the last safe day for these two
  models is 2026-11-29.
- **No key was made, where the step list's first point says "make a new project and a key".**
  The note says plainly that no key was made and leaves the key to John, which is the more
  careful reading. It does not need to change.

## 1. Does it claim only what a list can show?

Mostly yes. Its section "What the list does not show" says the thing that matters: "A row in a
list of limits is not a served call." The two places it goes further are the two mends above.
The passing finding that the account, "though not the new project", has used Gemini 2.5 Flash
is worded with care, and it bears on a point the cost and terms document left open: whether
Google's word "users" means an account or a project. The note does not claim to settle that.

## 2. Does it agree with the other three documents?

| Point | The note | The other documents | Agree? |
|---|---|---|---|
| Google's sentence on access | "is limited to users who have actively used them in the past" | The same words, quoted in the cost and terms document and the step list | Yes |
| The paid service is the one to use | "Only a first real call on the paid service" | Cost and terms: the unpaid service "must not be used here" | Yes, without the reason |
| Which models | Gemini 2.5 Pro and Gemini 2.5 Flash | The plan's Google run holds those two | Yes |
| What comes after the list | "They appear", then John's steps | The step list: the list "may show nothing useful", and a new project "will very likely be refused" | Differs in tone, and does not say so (mend 1) |
| Whether billing needs a new payment | "was not looked at" | Cost and terms: a new account prepays "a minimum of $5" | No conflict. The note adds that a billing account already exists, which may change what has to be paid |
| Using another project's key | "Neither project's key was used or looked at" | The step list: "The workspace's existing Gemini key is not used in its place" | Yes |

## 3. Anything that should not be in a public repository?

- **No key, and no project id.** The message asking for this check said the note names a
  Google project id and two other projects by name. The note as committed does neither: it
  gives the new project's display name, "Beyond the Window", and speaks of "two other
  projects" with no names. Nothing needs to come out on that score.
- **What it does say of John's account:** that the account has a billing account on the paid
  service with two other projects, and that one of them used Gemini 2.5 Flash in the 28 days
  before 2026-11-19. Both facts bear on the run, and neither names a project, a sum or a
  person. The cost and terms document already says in public that the workspace holds a Gemini
  key. I would leave them in. Whether John is content to have that much of his account in a
  public file is his to say, and it is worth one question to him before the push.
- **No private matter** otherwise.

## 4. Language

- Dates are absolute. There are no long dashes and no bare ids.
- John's word is quoted ("Yes, start the free check"). It is recorded nowhere else in the
  repository, which is fine for a check that spent nothing, as long as the worklog holds it
  too.
- The page's own labels ("Free tier", "Rate Limit", "All models") are quoted with plain words
  beside them. "Tokens" is used without a plain meaning, as the other capture documents do.
- The one unclear pointer is "the same page", listed above.

## What I did not do

- I did not open Google's pages, by instruction, and did not look at any key.
- I did not check the note's facts against anything but the repository's own documents.

**Fit to push after two mends: say under "What follows" that a list of every model would show
these two rows to any project, so "very likely refused" still stands until a first call, and
soften "the zero says" to "the zero most likely means". The facts read from Google's page are
the master planning session's to answer for.**
