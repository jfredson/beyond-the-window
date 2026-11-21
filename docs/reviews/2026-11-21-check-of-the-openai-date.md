# Check of the correction to OpenAI's date on the entry about ending a conversation

Written 2026-11-21 by Claude (Opus 5.5), an AI model, in a session started by the master
planning session. This session did not write the commit checked (`fcfa825`, by the site-fixes
session). A push publishes to the live site, so this is the check before publishing. The
correction moves a date for OpenAI, a developer that competes with Anthropic, which makes the
model writing this. Weigh it with that in mind.

I changed nothing and pushed nothing.

## Verdict

**Fit to publish.** The new act says no more than OpenAI's help page, and 2026-11-20 is a safe
date for it. In the developers' table only OpenAI's cell changed, to "By November 20th, 2026".
The explanation line is the ruled one. The count is still 5. October 30th now appears only as
the day of the announcement.

**One thing the build should refuse, and does not.** The two new marks can move a date in the
table with nothing on the entry's page to say so. On a scratch copy I marked Anthropic's first
act on the entry about welfare assessments, of May 2025, as an announcement. After the records
were rewritten, its cell moved from "Since May 2025" to "Since November 9th, 2026", the tests
passed, and the site check passed. Only reading the diff of the headline file would show it.
I suggest the records script refuse to write a changed date in the developers' table unless
that entry has a history row dated the same day naming the change, as it already refuses to
write a moved count without a reason. Part 3.

## a. OpenAI's help page

I opened the page (`https://help.openai.com/articles/20001424`) on 2026-11-21.

| The act's words | The page |
|---|---|
| "safety interventions" | "These safety interventions are intended to stop the conversation ..." |
| "which can end a conversation" | "ChatGPT may end that conversation" |
| "enabled for personal accounts worldwide in its chat mode" | "These safety interventions are enabled for personal ChatGPT accounts worldwide in Chat mode." It adds that they do not apply in business, enterprise, education or health workspaces, or in Work mode, Codex or voice mode |
| "rolling out gradually" | "This feature is gradually rolling out to accounts worldwide and may not be activated on your account yet." |

The words say no more than the page. "In its chat mode" carries the page's own limit.

**Is 2026-11-20 the right date?** It is a safe one.

- The record says the page has no date of its own. That is not quite so. When I opened it, it
  said "Updated: 2 days ago", which on 2026-11-21 means about 2026-11-19. That is the day the
  page was last changed. It is not a date for when the interventions began, and it is shown
  only as a count of days back, so it cannot be cited as a date.
- So the earliest day the change is known to be in effect is the day the page was first read,
  2026-11-20. "By November 20th, 2026" says exactly that, and the explanation line says the day
  it began is not known.
- The act says "read on November 21st, 2026" and is dated 2026-11-20. Both are true: the page
  was first read on the 20th and read again for the act's words on the 21st.

## b. The built site

I built the site at the commit before this one and at this one, and compared every built file.

**Five built files differ:** the home page, the page of acts, the feed, the served headline
file, and the entry's page.

- **The developers' table.** All 21 cells compared. Only one changed: OpenAI on ending a
  conversation, from "Since October 30th, 2026" to "By November 20th, 2026". Every other cell
  is the same.
- **The explanation line** under the table now ends with the ruled sentence: ""By" with a date
  means the thing was seen in effect on that day, and the day it began is not known."
- **The history entry** on the entry's page, under its changes: "November 21st, 2026, OpenAI's
  date in the table of developers. Before: Since October 30th, 2026 Now: By November 20th, 2026
  Why: ..."
- **The page of acts and the feed** each have the new act, dated November 20th, 2026, and say
  25 dated acts in place of 24. The act of October 30th is still listed, with its own words,
  which say the chat product "will be able to" end a chat. So it reads as an announcement on
  its face.
- **The count is still 5.** No other figure moved.

**Does anything still say October 30th as the day the change took effect?** No. October 30th
now appears as the date of the announcing act (on the home page, the page of acts and the
feed), in the entry's text ("said on October 30th, 2026 that its chat product would be able
to ..."), as a source's date, and in the history entry's "Before" and "Why". None says the
change took effect that day.

**One consequence to know.** The home page's "Latest" line now shows this act: "Latest,
November 20th, 2026: A developer says its chat product's safety interventions ... are enabled
...". Until now that line was the welfare assessment of November 9th. A reader may take the
"Latest" date as the day the developer acted, when it is the day the change was seen. The words
"says" keep it true. The acts that come from a reading are few, but the line will show one
whenever it is the newest.

## c. The markers

**What the records script refuses** (tried on scratch copies):

- Either mark on an act that is not a developer's, or on an act that takes something back.
- Both marks on one act.
- A developer marked as offering a thing whose only act is an announcement: marking
  Anthropic's only act on kept files as an announcement was refused.

**What it does not refuse:**

| What I did | Result |
|---|---|
| Marked Anthropic's first of two acts on welfare assessments (May 2025) as an announcement | Its cell moved to "Since November 9th, 2026". Tests and the site check passed |
| Marked Anthropic's only act on kept files as seen in effect | Its cell became "By November 4th, 2025". Tests passed |

In both cases the check of the records refuses until the headline file is rewritten, and then
passes. Nothing on the entry's page says the date changed.

**How a later check would catch it today:** by reading the diff of `data/headline.json`, where
a cell's date and any `"by"` change show line by line, and by reading which acts in
`data/entries/` gained a mark.

**What the build should refuse:** a date in the developers' table that differs from the
committed headline file, unless the entry has a history row dated the day of the change. That
would make every move like this one carry a note on the page, which is what guideline 7 asks of
a correction of fact. This correction already has that row, so it would pass.

## d. Does the history entry read as a dated correction?

Yes. It gives the day, what changed ("OpenAI's date in the table of developers"), the old and
new words, and why: "October 30th, 2026 was the day OpenAI announced the change. November 20th,
2026 is the day its help page was first seen to say the change was in effect, and the day it
began is not known." A reader who has never seen the site could say that back. The changelog
line says the same, and the changelog's opening now says one entry has been corrected since the
site went public.

## e. The positions read

The correction dates a developer's act to what its own page shows, which keeps the record to
evidence and takes no side.

## f. The checks

Run on 2026-11-21 at this commit.

- `python3 -I scripts/test_compute.py`: "Ran 74 tests", "OK". That is three more than before,
  the tests of the two marks.
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "25 dated acts", "The grid of developers: 21
  cells, 6 offered", "The headline file matches the records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 114 outside addresses
  linked."

The build rewrote one line of `site/src/data/window.json`, which I left out of this commit.

**Fit to publish: the act says no more than OpenAI's page, only OpenAI's cell changed, the
correction is dated on the entry's page, and the count is still 5. The build should refuse a
moved table date with no history row, and does not.**
