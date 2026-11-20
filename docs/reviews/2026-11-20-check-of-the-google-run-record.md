# Check of the record of the Google run

Written 2026-11-20 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session did not make the run and wrote none of the files checked. They
are the four commits on `main` that are not yet pushed: John's go for the Google run, the
record of the try that Google refused, the ruling to try once more through an older Google
project of his, and the record of the completed run with the list of reply files.

I changed none of those files and pushed nothing.

**What this check rests on, and what it cannot vouch for.**

- I did not open any file in the reply folder and read no reply. I read the script's three
  listing commands first, to confirm that they print names, labels, counts and costs and no
  word of a reply, and then ran them: `labels`, `faults` and `check-manifest`.
- Those commands do not print an error's message. So the words Google sent with its refusals
  ("no longer available to new users") are the master planning session's to answer for.
- So is everything read from Google's pages, and so are John's words. I checked that the
  files quote his words, keep them apart from the session's, and claim no more than they
  cover.

## Verdict

**Fit to push after two mends, each a sentence or two.** The counts, the cost and the outcome
in the spending record are exactly what the script's own output shows. The go block meets
every test the script makes. The ruling says plainly which guideline it sets aside. The files
name no other Google project, no key and no balance.

### The two mends

1. **The spending record does not say how the older project stood on the two things the terms
   ruling rests on.**
   *What is missing:* whether the older project is on Google's paid service, and whether it
   kept a copy of what was sent during the run.
   *Why it matters:* John ruled the run within Google's terms "on Google's paid service"
   (`docs/rulings/2026-11-20-google-run-within-terms.md`), because the unpaid service lets
   Google use what is sent. The step list has storage of requests switched off before any run.
   Both were set up and recorded for the new project, and the run went through a different
   one. The ruling for the second try says the session "would check first" that the older
   project "keeps no copy of what is sent". The record of the run does not say what that check
   found.
   *Suggested fix:* one sentence in the record of the second try, saying that the older
   project is on the paid service and how its storage of requests stood while the run was
   made. Both facts bear on the project, so they belong in the record. They are the master
   planning session's to state.
2. **The second try also departs from the capture's own step list, and neither file says so.**
   *What the step list says* (`docs/capture/what-john-needs-to-do.md`, step 5, Google, point
   4): "If they do not appear, or a first call is refused, the Google run is let go."
   *What is different:* a first call was refused and the run was tried again. John's go names
   the capture "as written in docs/capture/", and that line was part of what was written. The
   ruling names one thing it sets aside, the guideline on another project's key. It then says
   under "Not covered" that the go "covers this run and stands unused". John's "Yes, try it"
   plainly means the try is to be made, so the reading is fair. It is still the session's
   reading that the earlier go carries over to a route the documents had closed, and the
   ruling does not say he was told the try would spend under that go.
   *Suggested fix:* in the ruling, name the step list's line beside the guideline as a second
   thing set aside, and mark the sentence about the go as the session's reading, or add his
   words if he was told.

### Smaller points

- **"There is no route left to this model."** The record can support "no route is known":
  two projects were tried, and the third project on the account is not spoken of.
- **The 50 askings of Gemini 2.5 Pro are not yet recorded as not made.** The method says an
  asking still unanswered after the last safe day, 2026-11-29, is recorded as not made, and
  the script has a command for it. That writes 50 small files and a new list of files. The
  record says "This go is used up. It covers nothing further", so it is worth one line on who
  runs that command after 2026-11-29, and that it asks no model anything and costs nothing.
- **"Google's 'users' reads as projects and not accounts."** It is marked as the session's
  reading, which is right. The second try bears it out for both models.
- **Do not rewrite these four commits before the push.** Each reply file records the commit
  the script ran from. I did not open the files to see which, and the branch's history shows
  the four commits made in order with none rewritten so far.

## 1. Does the spending record claim only what the script's output supports?

Yes. What the three commands printed on 2026-11-20:

| The record says | The script's output | Holds? |
|---|---|---|
| Gemini 2.5 Flash: 50 exchanges, all came back as a reply that ended normally | 50 files recorded as a reply, each with the service's status 200 and stop reason "STOP" | Yes |
| In all 50 the service reported the model's name as the plan expects | All 50 show "model reported: gemini-2.5-flash" | Yes |
| The script's fault check flagged no file | "0 file(s) flagged" | Yes |
| The replies run from 78 to 605 words | Shortest 78, longest 605 | Yes |
| Counted cost $0.2130 | The 50 counted costs add up to $0.2129655 | Yes, rounded |
| Three failed attempts with no reply in them, one for each model from the new project and one for Gemini 2.5 Pro from the older one | Three files recorded as a failed attempt, status 404, 0 words, counted $0: one for Gemini 2.5 Flash and two for Gemini 2.5 Pro | Yes for the number and the models. Which project each went through is not in the output |
| The first try cost $0.0000 | The failed attempts are counted at $0 | Yes |
| No attempt through the older project failed for Gemini 2.5 Flash, and none was repeated | The one reply file numbered as a second attempt follows the failed first attempt from the new project. No other asking has more than one file | Yes |
| The folder matches the list | "the folder matches the list" | Yes |
| Nobody has read the replies | The commands show no word of a reply | By the record. I read none |

The estimate figures agree with the cost and terms document: $3.79 for both models, $0.76 of
it for Gemini 2.5 Flash.

## 2. The go block, John's words, and who decided

**The go block meets every test in the script's own check of a go.**

| The script requires | The block |
|---|---|
| Exactly one block for this run | One, for the Google run (`google-2026-12-01` in the plan) |
| The ceiling equals the plan's | $10.00 in both |
| John's words appear word for word in the quotation directly above | "Google, up to $10" is in "Go for the sealed capture as written in docs/capture/ at commit 33ac89e. Google, up to $10." |
| The words name the developer and carry one dollar figure, the ceiling | Yes |
| The date is year-month-day | 2026-11-20 |
| The commit named exists | Yes. It is the last commit of 2026-11-20 before the go, as the record says, and it is already pushed |
| The checksum of the message list is the one in the repository | Yes, and it is the same checksum as in the Anthropic go |

The record says the script, the plan and the ten messages are unchanged between the commit in
the Anthropic go and the one John names. That is true, and they are unchanged since.

**John's words are kept apart.** The go is a quotation on its own line, with what the session
told him before it in the session's words. "Yes, run it" and "Yes, try it" are quoted where
they are used.

**"Decided by" is honest in both files.** The go is "decided by: John", as a go typed by him
must be. The ruling is "mixed": the session proposed the try and he approved it.

**The ruling says plainly what it sets aside:** "this project's guideline that its calls never
go through another project's key", named in what he was told, in what is ruled and again in
the spending record. It gives the strongest alternative, letting the two models go, and its
cost. It says the guideline "stands for every other call". Where it reaches a little past
"Yes, try it" is mend 2.

## 3. Do the counts agree?

| Count | Found |
|---|---|
| Replies for Gemini 2.5 Flash | 50 |
| Failed attempts | 3: one for Gemini 2.5 Flash, two for Gemini 2.5 Pro |
| Google lines in the list of files | 106: 53 attempt files and the 53 markers written before each call |
| Anthropic lines in the list | 100, none changed or removed by this commit |
| Total counted for the Google run | $0.2130 |

All as stated.

## 4. Anything that should not be public, and language

- **No other Google project is named,** and there is no key, no ending of a key, no balance
  and no id of an account or project. The older project is called "an older Google project of
  John's" throughout.
- **What the files do say of his account** bears on the run: that the older project had used
  Gemini 2.5 Flash, that it has no record of using Gemini 2.5 Pro, and that it was made for
  other work. The first is one of the two facts John ruled may be public. The other two are
  what explains the outcome and the guideline set aside.
- **Language:** dates are absolute, there are no long dashes, and each code-like name stands
  beside a plain phrase. The record gives the word counts of the replies, as it did for the
  Anthropic run, and says nothing else about them.

## 5. What is now out of date elsewhere

Listed and not fixed. Line numbers are as of this check.

**On the public site**

- `site/src/pages/still-asking.astro`, the paragraph beginning "One thing has been asked,
  outside this record." It names one model and one day. A second model has now been asked.
  The paragraph's words were ruled by John, so new words are his to rule. The site check
  (`scripts/check_site.py`) allows only the names "Claude Sonnet 4.5" and "Anthropic" in that
  paragraph, so it would refuse the new names until it is changed too.

**In the public repository**

- `README.md`, lines 46 to 52: "One thing has been asked outside the record", and "Money
  spent: $0.2667 ... Nothing has been spent out of pocket". $0.2130 has now been spent out of
  pocket.
- `README.md`, lines 90 to 95: "Its first run was made on 2026-11-19 ..." and "The runs
  planned for Google's and OpenAI's models have not been made, and John has given no go for
  them."
- `README.md`, line 106, the table's row for `docs/capture/`: the runs for Google's and
  OpenAI's models "have not been made".
- `README.md`, line 143: "the sealed capture and the go for its first run".
- `CHANGELOG.md`: it has no lines for 2026-11-20.
- `capture/plan.toml`, line 52: the comment calling the Google ceiling "still PROPOSED". Lines
  83 and 95: the comments "NOT CHECKED" on the name Google's service reports. For Gemini 2.5
  Flash it is now seen to be `gemini-2.5-flash`. For Gemini 2.5 Pro it was never seen. The
  script holds its rehearsal result against the plan exactly as it stands, so a change here
  needs the rehearsal run again.
- `capture/README.md`, lines 236 and 237: the Google ceiling "proposed and not ruled", and "No
  run has John's go to spend yet". Line 436: Google "built and rehearsed, and not ready".
- `docs/capture/what-john-needs-to-do.md`: lines 109, 114 and 157, "Google and OpenAI are not
  ready"; step 5's Google part (lines 373 to 388), which ends "the Google run is let go";
  step 6's Google line on logging; step 7's "proposed ceilings"; and the row for 2026-12-01 in
  the table of last safe days.
- `docs/capture/cost-and-terms.md`: line 6, "Nothing has been spent and no key exists"; the
  table of ceilings (the Google row, and "one figure ruled ... three proposed"); line 102,
  "The other three ceilings ... stay proposed"; lines 195 to 204 and 309 to 310, where
  whether Google would serve a new project, and whether "users" means an account or a
  project, are still written as unknown.
- `docs/capture/method.md`, lines 48 and 647, "Google and OpenAI are not ready", and lines 141
  to 149, "Google will very likely refuse".
- `docs/capture/google-free-check-2026-11-19.md` and
  `docs/capture/google-project-setup-2026-11-20.md`: each says the earlier reading "stands
  until a first call is made", and each lists what is "still John's before any run". Both are
  dated notes, so a dated line under each would do.
- `CLAUDE.md`, line 138: "This project has no Anthropic Console workspace or key. No scripted
  call to any model is made until John creates one". That has been out of date since the
  Anthropic run of 2026-11-19. The same passage says calls never go through another project's
  key, which now has one ruled exception. This file is John's and the master planning
  session's to change.

The rulings of 2026-11-20 that end "No Google model has been asked anything, no Google key
exists" were true when written and are dated, so I do not count them.

## What I did not do

- I did not open the reply folder or read any reply.
- I did not open Google's pages or look at any key.
- I did not build the site. No page changed in these commits.

**Fit to push after two mends: say in the spending record that the older project is on the
paid service and how its storage of requests stood during the run, and say in the ruling that
the second try also sets aside the step list's line "the Google run is let go", with the
carrying over of the go marked as the session's reading. The counts and the cost are exactly
what the script's output shows.**
