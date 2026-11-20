# What a stranger makes of the site, and five things to decide

**PROPOSED 2026-11-20, not ruled.** Written by Claude (Fable 5.2), an AI model, in a session
John opened to work on the site after an audit of all eight public sites in the family. Nothing
on the site or in the records was changed. The mock-ups described here were built on a copy of
the site, photographed, and thrown away; only their pictures and their page text are kept, in
`docs/proposals/pictures/2026-11-20-first-screen/`.

**A conflict to keep in view.** All five things the site counts as offered today are offered by
one developer, Anthropic, and Anthropic made the model that wrote this proposal. Two of the
decisions below are about how plainly the home page says that. Weigh my recommendations on
those two with that in mind.

## Where this came from

On 2026-11-20 two readers who knew nothing about the site were shown only phone pictures of it,
in stages: the first screen, the rest of the home page, the About page, the link preview and
one entry page. One reader was a Claude model and one was Gemini 3.1 Pro. They were told to act
as an impatient stranger who had tapped a link in a feed. The full method, and the same test on
the seven sibling sites, is in `timeassembler/docs/audits/cold-reader-audit-2026-11-20.md`.
Their answers for this site are in
`~/Code/Claude outputs/cold-reader-audit-2026-11-20/readers/` (the two files ending `btw.md`).

Two limits. No person has read the site for this. And the readers were told to be blunt, so
their tone is harsher than a real visitor's would be.

## What the readers found

**Both were lost in the first ten seconds.** Of the eight sites, this was one of two where both
readers were.

1. **Neither could say what the "things" are.** Both worked it out from the row labels on the
   window ("Being kept", "Being able to leave", "Protection in law"), and both said the page
   never states the subject in ordinary words. The Claude reader: "after ten seconds I cannot
   say what the subject is, and the paragraph meant to help is a paragraph of warnings about
   what the number does not mean."
2. **The caveat under the count reads as the site disowning its own number.** "The count is not
   a measure of how much lies past those limits, or of how much of it has been offered."
3. **"Offered" did not sit right.** Offered to whom? It covers "does the thing, provides it, or
   has publicly committed to it", and it is stretched when the thing is something a model does
   ("A model works on one task for days" is "Not offered yet").
4. **No stakes.** Neither reader was told why anyone should care. The Claude reader called the
   three cautions "the most interesting sentence on the page and the nearest thing to a reason
   to care", and found them in the ninth bullet of a list on the About page.
5. **The concrete entries are the draw.** "A model is interviewed before it is retired" was the
   one thing both readers said they would repeat, and the entry both would tap.
6. **Four different counts in two screens:** 5 at the top, 8 things in the list, 13 entries, and
   a second, different 5 "beside the list".
7. **Nothing shows movement.** No earlier count, no latest change, no dated news, and no way to
   be told when something changes.
8. **The link preview misleads.** From "A public list of things that lie past the present
   limits of AI models" the Claude reader guessed "a list of things AI cannot do yet". It is the
   only site in the family with no preview picture.
9. **An entry page read cold is mostly empty boxes.** On the memory entry, "Nothing recorded"
   appears six times across nearly two phone screens, and nothing on the page says what the
   site is or links to the list in a way a stranger would notice.
10. **One striking fact is hidden by "at least one AI developer".** The Claude reader guessed
    that every one of the five rests on the same developer. I checked the records and it is so:
    all five have `offered_by = ["Anthropic"]`. In the reader's words, "one company does five
    things; nobody else does any" is a more striking fact than "5".

**What they praised.** Every entry says in advance what would count and what settles it, and
keeps a dated log of its own changes with the reason, including reversals. Every claim links to
a dated source on the developer's own page.

## What collides with rulings already made

The audit's first suggestion was to drop the count and lead with a table of which developer
does what. Three things stand in the way, and none is mine to move:

- The home page opens with a count and no fraction (ruled 2026-11-18,
  `docs/rulings/2026-11-18-home-page-count.md`, decided by: mixed). The check of the built site
  enforces it.
- The exact sentence beside the count (ruled 2026-11-19,
  `docs/rulings/2026-11-19-home-page-sentence.md`, decided by: mixed).
- No developer is named off an entry page (the check of the built site, first-version choice
  18, decided by: agent).

Both rulings recorded moderate confidence for the same reason: the form "had not been seen on
the page". It has now been seen by two strangers. That is new evidence, and it is the reason to
bring the question back two days after it was ruled.

## Decision 1. The first screen

Three choices, each photographed on a phone. Pictures are in
`docs/proposals/pictures/2026-11-20-first-screen/`.

**As published** (`as-published.jpg`).

**Option A: keep the ruled count and sentence, and fix what stands around them**
(`option-A-01.jpg`). Three changes:

- The line above the count becomes "A public record of what AI developers do for the models
  they build".
- A new line under the ruled sentence: "For example, one developer has committed to interview
  each model before retiring it and to keep the record, and has let models in its chat product
  end a conversation in rare cases. All five come from that one developer. The earliest dates
  from May 2025."
- The caveat shrinks to one sentence with a link: "The list is short and holds only things with
  a dated source, so the count does not measure how much there could be. What the count means."
  The rest of the caveat moves to the About page.

Option A passes the check of the built site as it stands.

**Option B: lead with what is not known, and put the count below it** (`option-B-01.jpg`).

- The page opens: "Nobody knows whether AI models have wants of their own. This is a record of
  what is done for them in the meantime, and what is not."
- Then the three cautions in one short paragraph, using the ruled headings' wording: "If an AI
  system has no wants, and is treated as if it had, that has a cost. If it has wants, and they
  go unnoticed, that has a cost. If it has wants, and they put people at risk, that has a cost
  too. This record keeps all three in view and argues for none."
- Then the ruled sentence with its count in ordinary type, the same examples line, the short
  caveat and the window.
- The question ("What might a machine mind reach for ...") moves below the window.

Option B fails the check of the built site, because the count no longer opens the page. It
would need the ruling of 2026-11-18 changed and the check changed with it.

**What a fresh pair of readers made of the two mock-ups** (first screen only, 2026-11-20):

| | As published | Option A | Option B |
|---|---|---|---|
| Gemini: what is the site about? | "count things AI can currently do or experience" (wrong) | "the weird, extra things tech companies are doing for their AI programs, like treating them as if they have rights" | "what AI companies are doing to treat their AI models like they might actually have their own feelings or desires" |
| Gemini: scroll or leave? | leave | leave | scroll |
| Gemini: reason to care? | none | none | saw the cautions, called them "a boring philosophy debate" |
| Claude: what is the site about? | "I am guessing" | "a list of things AI companies do for the benefit of their own AI models, as if the models were owed something" | "the things AI companies do for the benefit of their AI models themselves, in case those models turn out to have wants of their own" |
| Claude: scroll or leave? | most likely leave | scroll "a little" | scroll, "but only just" |
| Claude: reason to care? | none | none: "It never says why anyone would do anything 'for' an AI model" | "Half a reason": the opening line is "a good hook, and it is plain", the three costs are "abstract, because it never says what any of the costs are" |

Four things all four mock-up readings agree on:

- **The subject now gets across.** Every reader of either mock-up could say what the site is
  about. No reader of the published page could.
- **The ruled sentence is still the hardest thing on the screen.** Both Claude readers called
  "things past an AI model's ordinary limits" the vaguest phrase, and both first took it to mean
  extra abilities. Each said the examples line "rescued" it. So the examples line is doing the
  work the sentence was meant to do. This is evidence about the sentence ruled on 2026-11-19,
  and nothing here proposes changing it.
- **"All five come from that one developer" was read as the real news.** Both Claude readers
  said so unprompted, and both said the big sentence hides it.
- **Both Claude readers wanted the developer's name at once**, and both said they would scroll
  mainly to find it. This bears on decision 2.

Gemini's reader also took "May 2025" for a date in the future and suspected a prank. That comes
from the model not knowing today's date, and says nothing about the page.

**My recommendation: Option A now, and Option B put to you as the question it really is.**

- *Confidence:* high that A is better than the published page. Both readers of both mock-ups
  could say what the site is about, and neither reader of the published page could. Moderate on
  A against B. B did a little better: Gemini's reader scrolled on B and left on A, and B was the
  only version either reader said gave any reason to care. But the gap is small, it rests on
  two readers, and the Claude reader faulted B for three paragraphs of grey text before
  anything to look at, with the count no longer a figure.
- *Standard practice or judgment call:* judgment call. The nearest sibling practice is the AGI
  Zeitgeist, whose plain verdict ("Not yet. Four things would all have to be true") was the one
  line both of its readers understood at once.
- *Strongest alternative:* B, at the cost of reopening a ruling two days old and of putting
  the cautions, which are the site's most careful wording, in the place most readers will
  quote from.
- *What I would change on reflection:* the examples line is long. It could lose its last
  sentence.

Every sentence in both options is new public wording, so each needs your eye before it stands,
and a different session's check before it is pushed.

## Decision 1, continued. Option C: the site rebuilt from the question up

*Added later on 2026-11-20.* After seeing options A and B, John asked how the site would be
designed from nothing to meet the audit's tests. Option C is a mock-up of that
(`option-C-01.jpg`, `option-C-02.jpg`, page text in `option-C-index.astro.txt`). It changes
what is counted, not only the wording, so it reaches well past decision 1.

**The idea.** The unit stops being a thing on a list, marked offered or not, and becomes a
dated act by a named actor: who did what, on what day, with its source. The question at the
top becomes "How is the world treating AI models, while nobody knows whether it matters to
them?" The founding question stays as the reason for the project and moves to the About page.

**What the first screen shows.** No single count. Three short readings, each of which the
world moves:

- **Developers, "1":** "One developer does five things for its own models, the first in May
  2025. One is interviewing a model before retiring it. None was found at any other developer."
- **Law, "4":** "United States states have passed a law saying an AI system cannot be a legal
  person, the first in 2022. No law was found that protects one."
- **People, "17%":** "of United States adults surveyed in late 2024 believed sentient AI systems
  already exist. AI researchers surveyed that year put the chance that an AI system has inner
  experience at 1 percent now and 70 percent by 2100."

Under them: "Latest, November 9th, 2026: a developer published a welfare assessment with its
newest models", and a link to "Everything, by date", a list of eleven dated acts drawn from
the records, newest first. Every figure and date is taken from the thirteen records as they
stand; none is new research. In the mock-up the present window still sits between the first
screen and the dated list, because only the top was rebuilt.

**What fresh readers made of it** (first screen only):

| | Option A | Option B | Option C |
|---|---|---|---|
| Could say what the site is about | both | both | both |
| Could say what it is telling them today | the count, which neither would repeat | the count | both gave a finding in their own words: "almost nobody is doing anything, and the law so far runs the other way" (Claude); "society is mostly ignoring AI rights, but it's starting to become a legal and social issue" (Gemini) |
| Scroll or leave | Claude scroll, Gemini leave | both scroll | Claude scroll ("a near thing"), Gemini leave |
| Fact they would repeat | the interview | the interview | the interview (Claude); the 17 percent (Gemini) |

**What C does that A and B do not.** It is the only version where a stranger could say what
the site is telling them today as a statement about the world. It also gave two different
facts worth repeating, from two different readings.

**What C gets wrong, by the readers' account.**

- **The opening paragraph about costs fails here as it did in B.** The Claude reader: "I read
  it twice and it still felt like a logic puzzle." Gemini's: "written like a riddle". In all
  three mock-ups the thing that made a reader care was the concrete detail, the interview
  before retirement, and never the argument. The costs belong lower down, and the concrete
  fact belongs at the top.
- **No one-line summary.** The Claude reader had to add the three readings up, and wanted the
  page to do it.
- **The "1" row carries three counts** (one developer, five things, one example), and the
  researchers' figures sit under the public's 17 percent, so both readers briefly mixed them.
- **The name again.** "Just say the name; hiding it feels coy and makes me slightly
  suspicious."
- **Both readers summed the page up as "almost nobody is doing anything".** That is a fair
  reading of the facts, and it is also a judgment the page does not make. Guideline 5 says the
  site does not campaign, so a one-line summary would need careful wording.

**What C would cost.** It sets aside the ruling that the home page opens with a count
(2026-11-18) and the ruled sentence (2026-11-19). It needs a stated rule for which developers
are covered, since "none was found at any other developer" is only as good as the search. And
it makes the survey and law entries, which now sit beside the list and are not counted, into
two of the three readings.

**Where I land.** C's structure is right and its opening is wrong. If the project goes this
way, the next mock-up should open on the concrete facts, give one plain summary line, split the
researchers' figures into their own reading, and move the costs below the first screen. Option
A remains the change that can be made now without reopening anything.

- *Confidence:* moderate. C is the only option that passed the "what is it telling me today"
  test, on two readers and one screen. It has not been read past the first screen.
- *Standard practice or judgment call:* judgment call. The nearest sibling practice is the AGI
  Zeitgeist's four signs, each one checkable fact set against the record.
- *Strongest alternative:* Option A, which changes little and keeps both rulings.

## Decision 2. Saying that all five come from one developer

The home page says "at least one AI developer" and the list says "one developer" five times. A
reader is left to assume several developers. The records say one.

- **Proposed:** say it on the home page without the name: "All five come from that one
  developer." Both mock-ups carry the sentence. The name stays on the entry pages, where it is
  now.
- *Confidence:* high that the home page should say it. It is the plainest true thing the count
  leaves out, and both mock-up readers repeated it correctly.
- *Standard practice or judgment call:* judgment call.
- *Strongest alternative:* name the developer on the home page. The reader evidence favours
  it: both Claude readers of the mock-ups wanted the name at once and were annoyed not to get
  it, and both said they could not repeat the fact to a friend without it. It would need the
  check changed. Against it: one company's name at the top of the site reads as promotion, and
  it is the company that made the model writing this, so I am the wrong one to weigh it. I
  have left the name out of the mock-ups for that reason and put the evidence here plainly. A
  middle course is to make "that one developer" a link to the entry that names it.

## Decision 3. The link preview

- **Proposed text:** "A public record of what AI developers do for the models they build, and
  what none does yet: keeping a retired model's files, interviewing it before retirement,
  letting it end a conversation."
- **Proposed picture:** the window as the home page draws it, with the site's name, built by a
  script from the records as the sibling sites build theirs.
- *Confidence:* high that a picture and a plainer text are needed. Moderate on the wording.
- *Standard practice or judgment call:* standard. Every sibling has a preview picture; this
  site left it out before it was public (first-version choice 17).
- *Strongest alternative:* the question as the preview text. It is the site's own wording, and
  neither reader could say it back.

## Decision 4. An entry page read by someone who lands on it

- **Proposed:** (a) one line under the entry's title saying what the site is, with a link to
  the list; (b) the kinds of record and the cautions that have nothing under them are named in
  one sentence ("Nothing is recorded yet under: ...") in place of a heading and a "Nothing
  recorded" line each.
- *Confidence:* high on (a). Moderate on (b): the empty headings may be there on purpose, since
  guideline 5 has the three cautions recorded with the same care as the hopeful evidence, and
  an absence shown is a kind of care. One sentence keeps the absence visible and takes two
  screens off the page.
- *Standard practice or judgment call:* (a) is standard in the family's news posts; (b) is a
  judgment call.
- *Strongest alternative:* leave the empty headings, at the cost of a page that a stranger
  reads as an unfilled form.

## Decision 5. Showing movement, and a way to follow

- **Proposed:** (a) a dated "Latest change" line on the home page, built from the entries' own
  change logs and the count's history, with no new writing; (b) a feed of those changes; (c) a
  way to follow by email, decided once for all the trackers, since none of them has one.
- *Confidence:* high on (a). It needs no ruling on wording beyond its form, because it prints
  what the records already say. Moderate on (b). (c) is a family decision and is only noted
  here.
- *Standard practice or judgment call:* (a) and (b) are standard (the siblings' "last checked"
  strip and news feed).
- *Strongest alternative:* dated news posts as the siblings have. That is more work and every
  post is new public wording, which the short path ruled on 2026-11-19 was meant to avoid.

## Noted, with no proposal

- **"Offered".** The readers' trouble with the word is evidence for open question 14 (whether
  one frame fits three kinds of progress). What "offered today" means was ruled on 2026-11-18
  and nothing here proposes changing it.
- **The About page.** Nine phone screens, mostly rules about what the site does not do. The
  three cautions are its strongest passage and sit low in a list.
- **The four counts** (5, 8, 13, and the second 5). Options A and B do not fix this. The note
  "All 13 entries are a first pass" is the easiest to cut.
- **The name.** Neither reader connected "Beyond the Window" to the subject. The line above the
  count in both options does that work.
