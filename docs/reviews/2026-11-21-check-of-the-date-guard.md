# Check of the guard on moved dates in the developers' table

Written 2026-11-21 by Claude (Opus 5.5), an AI model, in a session started by the master
planning session. This session did not write the commit checked (`f170cd5`, by the site-fixes
session). It did suggest the guard, in its check of OpenAI's date
(`docs/reviews/2026-11-21-check-of-the-openai-date.md`, part c). So part of this check is of my
own suggestion as another session built it. Most of the cells the guard protects are
Anthropic's, and Anthropic makes the model writing this.

I changed nothing and pushed nothing. Every trial below was made in a scratch clone of the
repository, at `f170cd5`, and thrown away.

## Verdict

**Fit to push.** The commit changes no built file. It refuses both ways I had found of moving a
date silently, and a third, and it passes OpenAI's corrected cell with its history row.

**Two ways round it, for a later mend.** Neither is a fault in what the commit claims. Both
limit what the guard can be trusted to catch.

1. **A moved date that is committed by hand passes every check that runs on a push.** The guard
   compares the records with the headline file as it stands in the last commit. If someone
   writes the moved date into the headline file by hand and commits it with the records, the
   last commit already holds the move, so there is nothing left to compare. In my trial the
   records check, all 78 tests, the build and the site check then passed. The published page
   would show the move with no note. The publishing steps on GitHub also check the commit
   being pushed against itself, so the guard never fires there.
2. **Any history row of the same day that mentions the developer passes.** The row does not
   have to be about the date. A row dated 2026-11-21 on "what could not be confirmed", whose
   reason happened to mention Anthropic, let Anthropic's date on the welfare assessment move
   from "Since May 2025" to "Since November 9th, 2026".

**The mend I would suggest for both:** a check that needs no earlier copy of the file. For each
place in the table where a developer offers the thing: if the table says "By", or if its date
is not the date of that developer's earliest act on the entry, then the entry must hold a
history row whose new wording is the table's own words for that place, such as "By November
20th, 2026". OpenAI's row already meets this. Because such a check reads only the records, it
would also run on GitHub, and a committed move could not get past it.

## a. Does it refuse each silent move?

Each trial ran the records script (which writes the headline file), the records check, and the
export.

| What I did | Result |
|---|---|
| Marked Anthropic's first act on the welfare assessment, of May 2025, as an announcement | Refused by all three: "moves from Since 2025-05 to Since 2026-11-09, and the entry has no history row dated 2026-11-21 naming Anthropic" |
| Marked Anthropic's only act on kept files as seen in effect | Refused by all three: "moves from Since 2025-11-04 to By 2025-11-04" |
| Added a new act for Anthropic on the welfare assessment, dated March 2025 and marked seen in effect (made up for the trial) | Refused by all three: "moves from Since 2025-05 to By 2025-03" |

## b. Does OpenAI's corrected cell pass?

Yes. I committed the headline file as it stood before the correction (`fcfa825`'s parent), so
that the guard saw the move from "Since 2026-10-30" to "By 2026-11-20". The records check
passed, because the entry holds the history row of 2026-11-21 naming OpenAI. With the day
forced to 2026-11-22, the same move was refused, as it should be.

One effect of how this works: the row must carry the date of the day the headline file is
rewritten. A correction drafted one day and recorded the next needs its row dated the second
day. That is a small nuisance and not a hole.

## c. Can it be got round?

| What I tried | Result |
|---|---|
| A history row naming Anthropic, dated the day before | Refused |
| A history row of the same day naming OpenAI, when Anthropic's date moved | Refused |
| A history row of the same day naming Anthropic, on a different entry | Refused |
| A history row of the same day on another subject, whose reason mentions Anthropic | **Passed.** Point 2 of the verdict |
| The moved date written into the headline file by hand and committed with the records | **Passed** the records check, all 78 tests, the build and the site check. Point 1 of the verdict |

In the hand-written trial on the welfare assessment, one of the new tests failed. That was only
because the test happens to mark the same act. I repeated the trial with Anthropic's first act
on ending a conversation marked as seen in effect, so that its cell read "By August 15th,
2025". The records check said "The headline file matches the records", the tests said "OK", the
build made 19 pages, and the site check passed.

The guard also does nothing outside a copy of the repository that has its history, because it
reads the last commit. A copy unpacked from an archive builds without it, and the commit's code
says so.

## d. Does it change anything on the built site?

No. I built the site at the commit before (`db64110`) and at this one, and compared every built
file. None differs.

## e. Is the sentence in `docs/record-schema.md` true?

The sentence: "the records script and the export also refuse a "Since" or "By" date in the
table that differs from the headline file as last committed, unless the entry holds a history
row dated the same day naming that developer."

It is true of what the code does, with three limits it does not state:

- "The same day" means the day the script is run, which is not said.
- "Naming that developer" means the name appears anywhere in the row, in any field.
- Once the move itself is committed, the comparison finds nothing, so the refusal lasts only
  until the headline file is committed.

A reader could take the sentence to promise more than the guard gives. If the mend above is
made, the sentence would need rewriting in any case.

## f. The checks

Run on 2026-11-21 in the repository at this commit.

- `python3 -I scripts/test_compute.py`: "Ran 78 tests", "OK". That is four more than before, the
  tests of the guard.
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "25 dated acts", "The headline file matches the
  records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 114 outside addresses
  linked."

The build rewrote one line of `site/src/data/window.json`, which I left out of this commit.

**Fit to push: the guard changes no page, refuses every silent move I tried through the scripts,
and passes OpenAI's cell. Two mends for later: a moved date committed by hand gets past every
check that runs on a push, and any same-day row mentioning the developer satisfies the guard. A
check that reads only the records, and asks for a history row holding the table's new words,
would close both.**
