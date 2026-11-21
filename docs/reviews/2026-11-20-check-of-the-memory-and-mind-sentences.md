# Check of two added sentences: on the memory entry, and on the word "mind"

Written 2026-11-20 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session did not write the two commits checked (`ffaa2a3` and `16a61c7`,
by the site-fixes session) or either sentence. A push of them publishes to the live site, so
this is the check before publishing, and it includes the read against John's published
positions that he ruled for every changed page. A model is here judging a sentence about
whether "anyone is there" in a machine, so weigh that part with that in mind.

I changed nothing and pushed nothing.

## Verdict

**Fit to publish.** Each sentence is on the built site word for word, in the ruled place, with
nothing else on its page changed. Exactly two built pages changed and no count moved. The
other twelve records build exactly as before. Both sentences agree with John's published
positions. No changelog line or page note was added, as he ruled.

Two things to know, neither of which holds up the push:

1. **The new field can put a sentence on a page with nothing in the build to stop it.** The
   records script checks that the field is text and that the entry sits beside the list. It
   does not check what the sentence says, or that John ruled it. I tried it on a scratch copy:
   a constructed sentence making a claim, added to another entry beside the list, built and
   passed every check. Part 2 says how a later check would catch that, and what would make the
   build catch it.
2. **The About page's new sentence disclaims in one direction only.** Read strictly it is
   neutral. A stranger could still hear it as leaning toward "nobody is there". Part 3 gives
   the reasoning. The words are John's approved ones, so this is his to weigh.

## 1. The built site

I built the site in scratch copies at the commit before the first of the two and at the
second, and compared every built file.

- **Exactly two built files differ:** `/list/memory-across-conversations/` and `/about/`.
- **The memory entry's page.** One paragraph is added and nothing else differs. As built, it
  follows the reason for the placement directly: "... The list is about what an AI model might
  reach for. So this entry is kept beside the list and is not counted among the things
  offered. This entry is placed by what the developers say the memory is for. That says
  nothing about what stored memory does to how a later conversation is built." The two new
  sentences match the ruling
  (`docs/rulings/2026-11-20-memory-entry-says-what-its-placement-rests-on.md`) word for word.
- **The About page.** One sentence is added and nothing else differs. As built, under "How It
  Works": "The wording of the question supposes that it might. It does not claim that it does.
  Nor does the word "mind" claim that anyone is there. So far only the first part is kept
  here ..." It matches the ruling
  (`docs/rulings/2026-11-20-about-page-says-mind-claims-nothing.md`) word for word, and sits
  directly after "It does not claim that it does."
- **No count moved.** The count at the top is 5, with 24 dated acts, and the table of
  developers is unchanged. The home page, the page of acts, its feed, the list and every other
  entry page are the same file for file.

## 2. The new optional field

**Do the other twelve records build exactly as before?** Yes. The twelve other entry pages are
identical file for file. In the one file the site reads, every entry is the same as before
apart from the new field, which is empty on twelve and filled on one.

**Is the field described truly in `docs/record-schema.md`?** Yes, on each point I could test.

| The document says | What I found |
|---|---|
| A record beside the list may carry one optional field, a sentence or two on what its placement rests on | So. The script accepts it there |
| The entry's own page shows it straight after the reason for the placement, and nowhere else | So. It appears on that one built page and in no other built file |
| One record has it today | So: the entry on memory across conversations |
| The script refuses the field on an entry that is on the list | So. On a scratch copy the script answered "Refused. Nothing was written", naming the entry and the reason |
| Holding the sentence in a field of its own was decided by a session | It says so, "decided by: agent", which matches what the master planning session told me |

A new test covers the field: a record without it builds as before, one with it carries it,
it changes nothing counted, and it is refused on an entry on the list or when it is not text.

**Could it be misused?** Yes, in one way. Any session could add the field to one of the five
entries beside the list, and whatever it wrote would appear on that entry's page under the
reason for its placement. On a scratch copy I added a constructed sentence making a claim to
the entry on the public survey. The build finished and the site check passed.

**How a later check would catch it today:**

- By reading the diff of `data/entries/`, where the field's name is easy to search for.
- By building the site before and after a change and comparing every page, as this check
  does. A new paragraph on an entry page would show.
- The site check would still stop some sentences: one that names a model or a developer off
  an entry's page, uses a working word, or speaks in the first person.

**What would not catch it:** nothing in the build ties the sentence to a ruling, and the
entry's own closing part on what has been checked does not cover it.

**What would close it,** in keeping with the project's rule that guards live in code: have
the records script hold the list of entries allowed to carry the field, one today, so that a
second needs a deliberate change that names its ruling. That is a change to the script and is
for the master planning session to decide.

## 3. The read against John's published positions

I read the positions record's copy on the default branch of the `sentient-horizons` repository
(commit `82fb787`, 2026-11-15) with `git show`, without switching any branch there.

### The memory sentence

**It agrees with the position on where current AI stands.** That position says that where a
memory feature is added, a later run is built from what earlier runs stored. It carries a
guard against arguing from who built a system. The entry's stated reason for its placement
rests on what the developers say the memory is for, which is close to what that guard warns
about. The new sentence says so in plain words: the placement rests on what the developers
say, and that says nothing about what stored memory does to how a later conversation is
built.

**It claims nothing about what that means for the model.** It does not say a later
conversation is built from stored memory, only that the placement is silent on it. It does
not use the position's comparison with a person. So it removes the mismatch the earlier read
found (`docs/reviews/2026-11-20-live-pages-read-against-the-positions.md`, its first
contradiction) without stating John's position on a page that says it argues for none.

**One small thing in the reading:** the paragraph just before it still gives the developers'
purpose as the reason, and the new sentence qualifies it. Together they read as a reason
followed by its limit, which is what was ruled.

### The About sentence

**It sits rightly with the positions.**

- John holds open, on purpose, whether any particular AI system is conscious. A sentence
  saying the question's word claims nothing keeps that open.
- His positions use "mind" in a way that does not settle whether experience is present: they
  keep intelligence, sentience and consciousness apart as three questions, and say complexity
  can exist without a mind. So it is true in his own terms that the word claims no one.
- "Anyone is there" is his own way of putting it. The record speaks of things happening "to
  someone", of a description that can be accurate "with no one inside", and of "a no-one".
- The record warns against defining a feature with "words that already mean someone". The new
  sentence does the opposite: it marks a word that a reader might take to mean someone, and
  says it does not.

**Could "claim that anyone is there" be read as a lean toward "nobody is there"?** Plainly:
yes, a little, by a reader who is not reading closely.

- *Read strictly, it is neutral.* It denies that a claim is made. It does not make the
  opposite claim, and it parallels the sentence before it, "It does not claim that it does."
- *Why it can still lean.* It is the third disclaimer in a row, and it disclaims in one
  direction only. Nothing beside it says that the word does not claim no one is there either.
  John's positions treat dismissal as a mistake equal to over-reading, and say uncertainty is
  no licence to treat an inside as absent. A run of sentences that each step back from
  "someone" can add up to a tone the positions would not choose.
- *What offsets it on the same page.* The sentence two before it says that whether a machine
  mind reaches for anything is "the part nobody knows". Elsewhere the page says of the
  sources: "They do not say that an AI model wants or feels something, and they do not say
  that it does not." And its list of what is not known begins with whether an AI model wants
  anything.
- *What would close it,* if John wants it closed: a two-sided form, such as "Nor does the
  word 'mind' claim that anyone is there, or that no one is." The ruling records that he was
  told an added disclaimer can make the page read as a defence, and he chose the sentence as
  shown.

So it is not a contradiction, and it is not a lean the page fails to answer. It is a lean a
quick reader could take from one sentence alone.

## 4. No changelog line and no page note

John ruled on 2026-11-20 that wording updates get no changelog
(`docs/rulings/2026-11-20-no-changelog-of-wording-updates.md`). Neither commit touches
`CHANGELOG.md`, and neither adds a dated note to a page. None is owed, and I ask for none.

## 5. The checks

Run on 2026-11-20 on the repository at the second commit.

- `python3 -I scripts/test_compute.py`: "Ran 58 tests", "OK". That is one more than before,
  the test of the new field.
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "24 dated acts", "The headline file matches the
  records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 96 outside addresses
  linked."

The build rewrote one line of `site/src/data/window.json`, which I left out of this commit.

## What I did not do

- I did not open the published page of John's stance on current AI or the essay the ruling
  quotes. The ruling records that the master planning session read both before the sentence
  was written, and the positions record says the same.
- I did not look at the pages in a browser at phone or desktop width. Each change is one
  short paragraph or sentence of ordinary text. The new paragraph uses a style the entry page
  already had.

**Fit to publish: both sentences are on the built site word for word in the ruled places,
exactly two pages changed and no count moved, the other twelve records build as before, and
both sentences agree with John's published positions.**
