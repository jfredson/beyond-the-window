# Check of the headline wording

Written 2026-11-21 by Claude (Opus 5.5), an AI model, in a session started by the master
planning session. This session did not write the two commits checked (`c5454ad` and `da3c9b2`,
by the site-fixes session). It did raise, in its check of the restored headline, the point the
first commit answers. A push publishes to the live site, so this is the check before
publishing. Anthropic, which makes the model writing this, does all five counted things.

I changed nothing and pushed nothing.

## Verdict

**Fit to publish.** The three lines are the ruled ones word for word, "seven" and "three" are
worked out from the records, and the page otherwise looks as John saw it. The new sentence
beside the count is true of all five counted things.

One small thing, for whoever next touches the page: the sentence under "Developers" says "three
developers" and the sentence after it says it again. As built: "This record follows seven
things, and where each of three developers stands on each. It covers three developers so far."
The ruling sets the first sentence and does not mention the second. Ending the paragraph with
"Other developers are not covered yet." would keep what the second sentence adds.

## a. The built home page

I built the site at the commit before the first of the two and at the second, and compared
every built file.

**The three lines, word for word:**

- Beside the count: "things a developer can do in how it treats the AI models it builds are
  done, or publicly committed to, by at least one developer today."
- Under "Developers": "This record follows seven things, and where each of three developers
  stands on each."
- The heading of "Who does what": "seven things, three developers".

Each matches answers four, five and seven of
`docs/rulings/2026-11-20-home-page-opens-with-a-headline-again.md`.

**Worked out from the records.** "Seven" and "three" are marked figures, written from the served
headline file, which lists seven things in the developers' table (ending a conversation, a
retired model staying open, kept files, the interview before retirement, a welfare assessment,
the days-long task, a checked self-report) and three covered developers. The site check
confirms each marked figure against that file.

**Against the pictures.** I looked at phone width (375 points) and at 1,440 points wide, in
light and in dark. The layout is the one John chose. At phone width the longer sentence takes
four lines where it took four before, and the "Among them" line and the breakdown sit where
they did. Neither width scrolls sideways.

## b. Is "in how it treats" true of each of the five?

| Counted thing | Is it something a developer does in how it treats its models? |
|---|---|
| Keeping a retired model's files | Yes: what it does with a model it retires |
| Interviewing a model before retiring it | Yes |
| A retired model staying open to the public | Yes: what it does with a model after retirement |
| A welfare assessment published at release | Yes: how it assesses a model before release |
| Ending a conversation | Yes, as Anthropic does it: it lets its model end one |

**The second developer's chat ending.** OpenAI's pages describe it as a safety step for people,
in which the chat product, and not the model, ends the conversation. "How it treats the AI
models it builds" is a looser fit for that than for Anthropic's version. But the sentence makes
a claim about each kind of thing and says each is done "by at least one developer". Every one
of the five is done by Anthropic, as the sentence describes. So the sentence is true of what
the count counts. OpenAI's one thing is counted in the breakdown below, "1, by a second: one of
the same 5", which makes no claim about whom the thing is for. John ruled that it is counted.

The change from "for" to "in how it treats" removes the claim about whom each thing is for,
which was the point raised.

## c. Other sentences that describe the same things

| Where | Sentence | Disagrees? |
|---|---|---|
| The list page, and the served headline file | "5 things past an AI model's ordinary limits are offered today by at least one AI developer" | No. It describes the same five by a different property: that they lie past a model's ordinary limits. Both are true |
| The About page | "4 of the 5 things counted as offered rest on pages published by the one developer that offers them, Anthropic" | No. It names no kind of thing |
| The About page | The beside-the-list entries "are about the setting in which the things on the list happen, and none of them is itself a thing that lies past the limits an AI model ordinarily works within" | No. It is about the entries that are not counted |
| The home page, below | "The List: 8 things, and how far the world has got on each" | No. It is the whole list, of which five are counted |

**Does any of it mislead?** Not in substance. A reader moving between the home page and the list
page meets two descriptions of the same five, and on the home page three counts (5, 7 and 8),
which my last check noted. Each is labelled with what it counts. None now says whom the things
are for, so the earlier gap is closed everywhere the words appear.

## d. The positions read

The new wording counts what is done without saying it is done for a model's sake, which keeps
open, as John's positions do, whether any model has interests.

## e. Pages, counts and the checks

- **One built page differs:** the home page. No count moved: the count is 5, with 24 dated
  acts. No changelog line was added by either commit, and none is owed for wording.
- `python3 -I scripts/test_compute.py`: "Ran 71 tests", "OK".
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "24 dated acts", "The headline file matches the
  records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 114 outside addresses
  linked."

To view the scratch build I added a temporary entry to the local preview settings and put them
back as they were. That file is not in the repository. The build rewrote one line of
`site/src/data/window.json`, which I left out of this commit.

**Fit to publish: the three lines are the ruled ones word for word, their figures come from the
records, and the sentence beside the count is true of all five counted things.**
