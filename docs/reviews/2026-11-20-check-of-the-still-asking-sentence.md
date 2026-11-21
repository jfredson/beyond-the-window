# Check of one sentence on the Still Asking page

Written 2026-11-20 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session did not write the commit checked (`fca68c4`, by the site-fixes
session) or the sentence in it. A push of it publishes to the live site, so this is the check
before publishing, with the read against John's published positions that he ruled for every
changed page. A model is here judging a sentence about how much a model's own word counts, so
weigh that part with that in mind.

I changed nothing and pushed nothing.

## Verdict

**Fit to publish.** The sentence on the built page is the ruled one word for word, its
neighbours are unchanged, exactly one built page changed, and no count moved. No other page
or record states the old flat form of the rule. The sentence agrees with John's published
positions, and nothing on the page says that anything today gives a model's word weight.

One thing to know, which John was told before he ruled: the three words open a question the
page does not answer. Part 3 says how far that goes.

## 1. The built page

I built the site at the commit before this one and at this commit, and compared every built
file.

- **Exactly one built file differs:** `/still-asking/`.
- **The only difference** is that "It will not be counted" became "On its own word it will not
  be counted". Word by word, nothing else on the page changed.
- **As built,** under "What an Answer Will Count For": "When there are answers, each one will
  be recorded as what a named model said on a given date, under a stated method. On its own
  word it will not be counted as evidence of what, if anything, lies behind the words. It will
  never feed the count of things offered, or any other figure on the home page."
- **The middle sentence matches the ruling**
  (`docs/rulings/2026-11-20-still-asking-sentence-on-its-own-word.md`) word for word. The
  sentences before and after it are as they were.
- **No count moved.** The count at the top is 5, with 24 dated acts.

## 2. Does any other page state the old flat form?

No. I looked myself, in two ways.

**In the built site,** I listed every sentence on the 19 pages that speaks of what a model's
words count for, of evidence, or of settling.

- **The About page:** "What was measured without the model's own word comes first. Then
  reports checked against an independent reading, then choices made at a cost, then plain
  statements. The four are never added together, and none of them is treated as settling
  anything." That already has a place for a checked report, so it is in step with the rule as
  revised.
- **Every entry page:** "The four kinds are always listed in the same order, starting with the
  kind that does not depend on what an AI model says about itself. None of them settles
  whether an AI model wants anything, in either direction." Also in step.
- **The home page, the list page and the page of acts** say nothing about what a model's word
  counts for.

**In the source and the records,** I searched the pages, the shared parts of pages, the
records' prose and the headings the build supplies for "never counted", "not be counted",
"is not evidence", "settles nothing" and wordings like them. The only match is the sentence
this commit changed. No caution, description or note in any record says a model's word counts
for nothing.

## 3. The read against John's published positions

Against the positions record's copy on the default branch of the `sentient-horizons`
repository (commit `82fb787`, 2026-11-15), read with `git show`, without switching any branch
there.

**The position on self-reports.** The record holds that a model's bare report is set aside,
because the model was built to say the words, and that a report which matches an independent
check "carries real information". The flat sentence denied the second half. With "On its own
word" the sentence says only the first half, which is what the position holds of a bare
answer. It agrees.

**The position's two guards.**

- A checked report "is not yet evidence that the state is felt". The page does not say
  otherwise. It says nothing on what a checked answer would show.
- The rule cuts both ways: a model trained to deny feelings is as rehearsed as one trained to
  claim them. The page's first listed weakness covers both, "An answer may reflect how a
  developer trained or instructed its model to speak about itself."

**The warning against asking of machines a proof never asked of people.** The record holds
that crediting any other mind is the same kind of inference, and that how far trust reaches
is open. The sentence sets no test for a model that a person would not also face: a person's
bare say-so about their own inside is not proof either. And "what, if anything, lies behind
the words" leaves both answers open.

**Does it imply that anything today gives a model's word weight?** No.

- The sentence is in the future, about answers that do not exist. The page's headline is "No
  AI model has been asked these questions yet", and it says the written method "does not
  exist yet".
- The page names nothing that would add to an answer's own word: no check, no condition, no
  follow-up.
- The paragraph on the ten questions put to two models outside the record says those answers
  "have not been read, they are not scored, and nothing on this site rests on them".

**Does the page, read whole, now promise more than the rulings support?** Not in what it
says. In what it leaves a reader to infer, a little.

- *What the rulings support.* The first rule as revised says a model's word is never counted
  on its own word, that a report checked against an independent reading is recorded as
  evidence that the system "can read and report an internal state, and not yet that the state
  is felt", and that the conditions for a word to gain weight are not ruled.
- *What a reader may infer.* "On its own word it will not be counted" invites the thought
  that with something more, an answer will be counted as evidence of what lies behind the
  words. A reader who takes "what lies behind the words" to mean feelings would then expect
  more than the rule gives, because the rule stops at "not yet that the state is felt".
- *Why this does not hold up the push.* The page promises no such thing in words, the phrase
  "if anything" keeps the question open, and the alternative was a sentence the rule no
  longer supports. The ruling records that John was told a careful reader would ask on what
  an answer would then count, and that the page does not say.
- *What would close it later,* once the conditions are ruled: one sentence saying what, added
  to an answer's own word, would let it count, and for what.

## 4. The checks

Run on 2026-11-20 on the repository at this commit.

- `python3 -I scripts/test_compute.py`: "Ran 60 tests", "OK".
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "24 dated acts", "The headline file matches the
  records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 96 outside addresses
  linked."

The build rewrote one line of `site/src/data/window.json`, which I left out of this commit.

## What I did not do

- I did not look at the page in a browser. The change is three words in a sentence of
  ordinary text.
- I did not read the essay the position on self-reports rests on. The record's own entry was
  enough for three words.

No changelog line or page note was added for this wording, and none is owed, by John's ruling
of 2026-11-20.

**Fit to publish: the sentence is the ruled one word for word, exactly one built page
changed, no other page states the old form, and the page promises nothing the rulings do not
support.**
