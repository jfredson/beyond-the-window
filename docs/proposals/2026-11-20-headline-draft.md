# The home page opens with a headline number again: two drafts of the top

**PROPOSED 2026-11-20.** Written by Claude (Opus 5.5), an AI model, in a working session started
by the master planning session. Nothing here is ruled beyond what the rulings named below say,
and nothing is published. The drafts are on the branch `claude/headline-draft-df7958` only.

It follows John's ruling of 2026-11-20 that the home page opens with a headline number, as the
sibling sites do (`docs/rulings/2026-11-20-home-page-opens-with-a-headline-again.md`, decided
by: mixed). That ruling leaves three things open: the exact number and sentence, the layout,
and the fraction. This document draws two versions of the top for John to choose between.

## The pictures

All in `docs/proposals/pictures/2026-11-20-headline-draft/`. Phone pictures are 375 points wide,
desktop pictures 1280. "First" is the first screen (812 points on a phone, 800 on a desktop);
"full" is the whole page.

| | Version A, the ruled words | Version B, a plainer sentence |
|---|---|---|
| Phone, light, first screen | `version-A-phone-light-first.jpg` | `version-B-phone-light-first.jpg` |
| Phone, dark, first screen | `version-A-phone-dark-first.jpg` | `version-B-phone-dark-first.jpg` |
| Desktop, light, first screen | `version-A-desktop-light-first.jpg` | `version-B-desktop-light-first.jpg` |
| Desktop, dark, first screen | `version-A-desktop-dark-first.jpg` | `version-B-desktop-dark-first.jpg` |
| Phone, light and dark, whole page | `version-A-phone-light-full.jpg`, `version-A-phone-dark-full.jpg` | `version-B-phone-light-full.jpg`, `version-B-phone-dark-full.jpg` |
| Desktop, light and dark, whole page | `version-A-desktop-light-full.jpg`, `version-A-desktop-dark-full.jpg` | `version-B-desktop-light-full.jpg`, `version-B-desktop-dark-full.jpg` |

One switch picks the version when the site is built: `HEADLINE_VERSION=B npm run build` draws B,
and anything else draws A. The site check passes for both.

## Version A: the ruled words

As shown, from the top:

> A DATED RECORD OF HOW THE WORLD IS TREATING AI MODELS
>
> **5**
>
> things past an AI model's ordinary limits are offered today by at least one AI developer.
>
> **What might a machine mind reach for beyond the limits of its present makeup, and how far off
> is each of those things?**
>
> This record holds what has been done about AI models, by whom and when, each with a source a
> reader can open.
>
> (the two lines saying when the record was last read and checked)
>
> [Read the list] [What AI models have been asked]

| Piece | Follows |
|---|---|
| The number, with no total beside it | `docs/rulings/2026-11-18-home-page-count.md` |
| The sentence, word for word, read from the headline file | `docs/rulings/2026-11-19-home-page-sentence.md` |
| The founding question as the page title | the founding question, ruled 2026-11-17 |
| The order: a short line, the number, the sentence, the question | `docs/rulings/2026-11-20-home-page-opens-with-a-headline-again.md` |
| The short line at the top, and the sentence under the question | the rebuild's own words, kept; a session's, not ruled |
| The layout | not ruled; John sees these pictures first |

## Version B: a plainer sentence for the same count

As shown, from the top:

> A DATED RECORD OF HOW THE WORLD IS TREATING AI MODELS
>
> **5**
>
> things a developer can do for the AI models it builds are done, or publicly committed to, by
> at least one developer today.
>
> Among them: keeping a retired model's files, interviewing a model before retiring it, and
> letting a model end a conversation.
>
> **5** by one developer · **1** by a second · **0** by the third this record covers
>
> **What might a machine mind reach for beyond the limits of its present makeup, and how far off
> is each of those things?**
>
> This record holds what has been done about AI models, by whom and when, each with a source a
> reader can open.
>
> (the two lines saying when the record was last read and checked)
>
> [Read the list] [What AI models have been asked]

What each piece is for, and what it rests on:

- **The sentence** answers the two things the strangers in the reading test of 2026-11-20 could
  not follow (`docs/proposals/2026-11-20-what-a-stranger-makes-of-the-site.md`, findings 1
  and 3). "Things past an AI model's ordinary limits" did not tell them what the things were.
  B says what kind of thing is counted: something a developer can do for the models it builds,
  the same words the rebuilt page already uses for its developers' reading. "Offered" left them
  asking "offered to whom?". B uses the ruled meaning of the word in place of the word: John
  ruled on 2026-11-18 that a thing is counted when a developer "does the thing, provides it, or
  has publicly committed to it" (`docs/rulings/2026-11-18-what-offered-today-means.md`). "Done"
  covers doing it and providing it. The sentence keeps "at least one developer" and "today", so
  it says no more than A.
- **The line under it** names three of the five things counted, each linked to its page. The
  build stops if any of the three stops being counted. The Upgrade Tree has nothing quite like
  it, so this is a departure (see below). It is there because both strangers worked out what the
  things were only from the labels on the window drawing, and the one thing both said they would
  repeat was the interview before retirement.
- **The breakdown** is how many of the five each developer the record covers does, most first.
  It is read from the developers' reading the build already serves (Anthropic 5, OpenAI 1,
  Google 0) and checked by the site check figure by figure. It does not name the developers: the
  site check allows a developer's name on the home page only inside the developers' reading
  (its rule 12), and the names stand just below (on a phone) or beside (on a desktop). It shows
  the fact the strangers found most striking (finding 10): one developer does all five. That is
  still true, but one thing has changed since the reading test: OpenAI is now counted for one
  thing, ending a conversation, so the test's other half, "nobody else does any", is no longer
  so. The breakdown therefore says "1 by a second", not "all five come from one developer"
  alone.

| Piece | Follows, or would need |
|---|---|
| The number, with no total beside it | `docs/rulings/2026-11-18-home-page-count.md` |
| The sentence | **Would need John's ruling**, replacing the sentence ruled on 2026-11-19. It is also written in the headline file by `scripts/compute.py` and printed at the top of the list page; if John chose B, those would change too, with the test that holds the ruled sentence |
| The line naming three things | would need John's ruling; a session's |
| The breakdown by developer | would need John's ruling; a session's |
| The founding question, the order, the layout | as for A |

Conditional language: neither sentence says what a model wants or does not want. B says what a
developer does, and "for the AI models it builds" is the rebuilt page's own phrase.

## Where the number comes from

`scripts/compute.py` reads the records in `data/entries/` and counts each entry on the list whose
state names at least one developer that offers it (`offered_by`), under the meaning ruled on
2026-11-18. It writes the count, the entries counted and the ruled sentence to
`data/headline.json`, and the build serves that file at `/data/headline.json`. The page reads the
count from it and never types it. Today the count is **5**: ending a conversation, an interview
before retirement, keeping the files of retired models, a retired model staying open to the
public, and a welfare assessment published at release.

**Do the count and the rebuilt page's figures agree?** Yes, and neither could be taken for the
other's headline, so I built without stopping. The rebuilt page's developers' reading counts
places in its table, one for each pair of a thing and a developer: 6 are "in place or promised"
(Anthropic 5, OpenAI 1). The count is of things, and 5 things are done by at least one
developer. Both come from the same `offered_by` lists, so the 6 is the 5 Anthropic does plus
OpenAI's one, ending a conversation, which Anthropic also does. Two smaller points, set out for
the checker and not mended here:

1. The rebuilt page calls a counted place "in place or promised", and explains it as "the
   developer does the thing or has publicly committed to it". The ruled meaning also says that "a
   promise that has not yet taken effect is not counted". "Promised" on its own reads wider than
   the ruling. Version B's "done, or publicly committed to" is nearer the ruling, which leaves two
   wordings for one idea on the same screen. A wording change, so only the box labels would move.
2. OpenAI's counted act for ending a conversation (dated 2026-10-30) says its chat product "will
   be able to end a chat automatically", "with the change to begin in the following weeks". That
   may be a promise not yet in effect. It does not change the count, because Anthropic does the
   thing, but it would change the breakdown in B from "1 by a second" to "0". A check of the
   record against its source should settle it.

The home page also still shows other counts close together, which the reading test called
confusing (finding 6): 5 at the top, the seven things in the developers' reading, the 8 things on
the list, and 13 entries in the "last read" line. Neither version fixes that.

## Departures from the sibling sites

I read the live home pages of The Upgrade Tree, Outrunning Ageing and the AGI Zeitgeist at phone
and desktop width on 2026-11-20, and the top block of the first two in their repositories
(`upgrade-tree/site/src/pages/index.astro` and its `global.css`; `outrunning-ageing/site/src/pages/index.astro`). The sizes and spacing of the number, the sentence, the breakdown row and the
question are copied from The Upgrade Tree's styles and fitted to this site's colours. Where the
drafts differ:

1. **No total beside the number.** The Upgrade Tree shows "28 of 35". John ruled on 2026-11-18
   that this site's count stands alone, and the ruling of 2026-11-20 keeps that unless he changes
   it.
2. **Version A has no breakdown under the number.** The Upgrade Tree and Outrunning Ageing both
   have a row of small figures there. A is kept to the ruled words so that the two versions can
   be compared on the sentence; B has the row.
3. **B's breakdown does not add up to the number.** The Upgrade Tree's five stages add up to its
   35. Here a thing two developers do is counted under both, so 5 and 1 make 6, not 5. Each label
   says "by" a developer so that it reads as who does them, not as parts of the 5. A reader may
   still try to add them up; the checker should look at that.
4. **B's line naming examples has no exact match** on the siblings. The nearest is The Upgrade
   Tree's paragraph under the question, which gives examples ("an implant that gives back some
   sight..."). The line is here because the reading test showed this site's "things" are
   unclear without examples, and the siblings' things (ways of changing a person, the year
   ageing is outrun) are clear at once.
5. **The right-hand column on a desktop holds the readings, not a picture.** The Upgrade Tree puts
   its figure there and Outrunning Ageing its chart. This site's picture, the window drawing, was
   moved below the readings by the rebuild (`docs/proposals/2026-11-20-rebuild-design.md`,
   decision 5), and the ruling of 2026-11-20 lets the readings stay beneath the number. On a
   desktop "beneath" left half the first screen empty, so the readings stand where the siblings'
   picture stands. On a phone they follow below the buttons, as the siblings' picture does.
6. **The "last checked" lines are the site's own two lines, not the siblings' one strip.** The
   siblings' strip says "Last checked (date): 33 upgrades read, none moved. See the week's
   reading." This site has no weekly reading yet, so there is nothing to say about what moved. The
   two lines were kept word for word and moved to where the siblings put the strip.
7. **The short line at the top is the rebuild's**, "A dated record of how the world is treating
   AI models", and not a line like The Upgrade Tree's "A public count, kept in the open". The
   reading test showed that saying the subject in plain words was what made the rebuild readable
   (settled point 1), and this line does that.
8. **The sentence under the question is one sentence**, where the siblings have a paragraph. It is
   the rebuild's, kept.

## Changes to the rebuilt page's content

Everything else on the page is as the rebuild left it.

1. **Removed:** the opening sentence, "One AI developer has committed to interview each of its
   models before retiring it, and to keep the record.", with the check in the build that it holds
   for exactly one developer. In B the interview is still named, in the line under the number.
2. **Added:** the eyebrow, number, sentence and question block above; in B also the line of
   examples and the breakdown.
3. **Moved:** the founding question, from the end of "Why keep this record" ("The question behind
   the record: ...") to the page title. It is no longer printed in that section, where it would
   have repeated itself.
4. **Moved:** the two lines on when the record was last read and checked, and the two buttons,
   from below the readings to below the sentence under the question.
5. **Moved, desktop only:** the readings (researchers, developers, law, the public, the latest
   act) into a right-hand column beside the top block. On a phone they follow it, as before.
6. **Trimmed, B only:** the developers' reading no longer says "such as keeping a retired model's
   files or letting a model end a conversation", because the line under the number now gives
   those examples a few lines above.

The developers' table, the dated list, "Why keep this record" (less the question), the window
drawing, the list and the entries beside it are unchanged.

## The guard in code

The site check (`scripts/check_site.py`, rule 7, new part d) refuses a home page whose first
figure is not the computed count. The page must hold one number in the large type, marked as the
count, reading exactly the count in the served headline file with nothing beside it, and no other
figure and no reading may come before it. Rule 8 still refuses the count written as a share of
the list anywhere. Six tests in `scripts/test_compute.py` (the class `HomeHeadline`) cover it,
and a built page with "of 8" put beside the 5 was refused three ways when tried. All 71 tests
pass, and the build and the site check pass for both versions.

## Before anything is published

- John chooses A, B or neither, from the pictures.
- If B: John rules the new sentence, and `scripts/compute.py`, its test and the list page's
  heading follow it.
- A session that did not write the page checks it, including against John's published positions
  (the rule of 2026-11-20), and checks the two points under "Where the number comes from".
- The switch is removed once a version is chosen, so the site has one home page.
