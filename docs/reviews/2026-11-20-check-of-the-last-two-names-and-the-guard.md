# Check of the last two group names, the guard on the placement note, and everything not yet pushed

Written 2026-11-20 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session did not write the two commits checked (`701c5a4` and `a02d01c`,
by the site-fixes session). It is the last look before everything not yet pushed goes out
together, and a push publishes to the live site.

I changed nothing and pushed nothing.

## Verdict

**Fit to publish.** All six ruled names are shown wherever a group's name is shown, the two
names that were wrong are gone, and each of the two new names is true of both entries in its
group. No address, anchor or count changed. The guard refuses what it should and lets the
memory entry through. Nothing in the unpushed commits should be held back, and no two of the
changes disagree on the built site.

One thing to know about the guard, which is not a reason to hold the push: the records script
alone can be got round in five ways I tried, and a test that runs before every release
catches all five. One small gap is left, and it is described in part 2.

## 1. The two names on the built site

I built the site as it stood before these two commits and as it stands now, and compared
every built file.

- **Six built pages differ:** the home page, the list page, and the pages of the four entries
  in the two groups.
- **"Kept after retirement"** is on the home page twice (the window drawing and the list), on
  the list page once, and on its two entries' pages.
- **"Asked and assessed"** is in the same places for its two entries.
- **"Being kept" and "Asked and assessed by the developer" are gone** from every built file.
- **All six ruled names** are now the only names for those groups anywhere a group's name is
  shown. "Memory" is shown nowhere, because no entry on the list is in that group. The one
  old name left is "Remembering" in the memory entry's dated history, which is a record of
  where that entry stood.
- **No address, link or anchor changed,** and no count moved.

**Is each new name true of both entries in its group?**

| Name | Entry | True? |
|---|---|---|
| Kept after retirement | A developer promises in public to keep the files of every model it retires | Yes: the files are kept after the model is retired |
| Kept after retirement | A retired model stays open to the public after its retirement date | Yes: the model is kept in use after it is retired |
| Asked and assessed | A model is interviewed before it is retired, and the record is kept | Yes: the model is asked |
| Asked and assessed | A welfare assessment is published when a model is released | Yes: the model is asked and assessed, and the name no longer says by whom, which is what was wrong |

## 2. The guard on the placement note

The records script now refuses the note unless the record names a ruling file, that file is
in `docs/rulings/`, and the note stands in it word for word. I tried it on scratch copies. The
repository was not touched.

**What it refuses, and what it lets through.**

| What I tried | Result |
|---|---|
| The memory entry as committed | Passes |
| A made-up sentence on another entry beside the list, with no ruling named | Refused: no ruling named |
| The same made-up sentence, naming the memory entry's real ruling | Refused: "is not found word for word in the ruling it names" |
| A ruling file that does not exist | Refused: "docs/rulings/ holds no such file" |
| A file outside the rulings folder, named by a path | Refused |
| The memory entry's sentence with one word changed ("little" for "nothing") | Refused |
| A ruling named with no note | Refused |

**Can it be got round?** The records script alone, yes. Each of these built without complaint
when I put it on another entry beside the list:

1. A sentence that a ruling quotes as the wording John later replaced.
2. A sentence of the session's own from inside a ruling, which John never approved for a
   page.
3. A two-word fragment found in a ruling ("Yes, add it").
4. The memory entry's ruled sentence itself, on an entry it was not ruled for.
5. A made-up sentence, together with a new ruling file made up to hold it.

**What catches those.** A test added in the same commit holds that the memory entry is the
only record carrying a note. With any of the five in place, the tests fail, naming the extra
entry. The release runs the tests before it builds and publishes
(`.github/workflows/deploy.yml`), so none of the five could reach the live site without
someone also changing that test. The ordinary build on this Mac does not run the tests, so a
session building here would not be stopped until the release.

**The one gap left.** On the memory entry itself, the note could be swapped for another
sentence that stands in its own ruling file, such as a sentence of the session's from "How it
came up". The script would pass it, and the test would pass it too, because the entry is the
allowed one. It is one entry and one file, and the swap would show in any reading of the
diff.

**What the guard protects against, and what it does not.**

- *It protects against* prose reaching a page by accident or by habit: a sentence nobody
  ruled, a ruled sentence that has drifted by a word, or a note added to a second entry
  without a deliberate change to the test.
- *It does not protect against* a session that sets out to get round it, since the same hand
  can write a ruling file and change a test. No code can check that John said the words. The
  guard on the spending record says the same of itself, and the answer there is the same: a
  different session reads the change.

## 3. The read against John's published positions

Against the positions record's copy on the default branch of the `sentient-horizons`
repository (commit `82fb787`, 2026-11-15), read with `git show`.

- **"Kept after retirement":** it says what is done and no longer names the model as the one
  who is kept, and it says nothing on whether anyone is there.
- **"Asked and assessed":** it says what is done, claims nothing about who answers, and no
  longer says who does the asking, which is the more accurate of the two.

There is nothing else to find. With these two, no group's name is left that names the model
as the one something happens to.

## 4. Everything not yet pushed, taken together

I compared the site as last pushed (commit `8122de8`) with the site as it stands now.

**Eleven built pages differ, and every difference is one John has ruled.**

| Page | What changes |
|---|---|
| About | One sentence added: "Nor does the word "mind" claim that anyone is there." |
| Home page | Five group names, each shown twice |
| List page | The same five names |
| The memory entry | The two sentences on what its placement rests on |
| The entry on ending a conversation | Its group's name, and its opening sentence |
| Six other entry pages | The group's name on each |

- **The set of built files is the same,** and no address, link or anchor differs. The count
  at the top is 5, with 24 dated acts.
- **No two changes disagree.** Each group's name reads the same on the home page, the list
  page and the entry pages. The page of acts and the feed carry no group names. No sentence on
  any page still uses a name that was replaced, apart from the dated history noted above.

**Is there anything that should not go out?** Not that I found.

- *Keys, addresses, account matter:* I scanned every added line in the unpushed commits and
  found none.
- *Private material:* the unpushed note of proposed sources for the first caution
  (`docs/proposals/2026-11-20-sources-for-the-first-caution.md`) is marked "PROPOSED
  2026-11-20. Nothing here is applied", says a model wrote it and that it deserves a second
  look, draws on published sources only, and its longest quotation is 16 words. I did not
  check its sources. It changes no record and no page.
- *The rulings:* five ruling files are in the push, each with John's words quoted.

**Three things from my earlier checks still stand as written, and none holds up the push:**

- The About page's new sentence disclaims in one direction only, so a quick reader could take
  it as leaning toward "nobody is there". John's approved words.
- On the entry on ending a conversation, "close the conversation" stands in two sentences
  running with two meanings. Loose, and not misleading in substance.
- The comment at the head of `data/groups.toml` still says the names sort the entries "by
  what is done to or for a model", and `docs/first-version-choices.md` still lists the old
  names. Neither is on a page.

## 5. The checks

Run on 2026-11-20 on the repository at the second commit.

- `python3 -I scripts/test_compute.py`: "Ran 60 tests", "OK". That is two more than before,
  the tests of the guard.
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "24 dated acts", "The headline file matches the
  records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 96 outside addresses
  linked."

The build rewrote one line of `site/src/data/window.json`, which I left out of this commit.

## What I did not do

- I did not look at the pages in a browser this time. Both new names are shorter than the
  ones I measured at phone width in the last check.
- I did not check the sources in the note of proposed sources, which is another session's
  work and applies nothing.

**Fit to publish: all six ruled names are in place and true of their entries, no address or
count changed, the guard refuses what it should, and nothing in the unpushed commits disagrees
with anything else or should be held back.**
