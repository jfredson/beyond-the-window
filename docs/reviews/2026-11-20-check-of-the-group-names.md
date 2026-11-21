# Check of the renamed groups and one reworded sentence

Written 2026-11-20 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session did not write the two commits checked (`822c024` and `7bab3a7`,
by the site-fixes session). A push of them publishes to the live site, so this is the check
before publishing, and it includes the read against John's published positions that he ruled
for every changed page.

I changed nothing and pushed nothing.

## Verdict

**Fit to publish for four of the five names and for the sentence. One name needs John
first.** The five ruled names are shown everywhere a group's name is shown, the five old names
are gone from those places, "Being kept" is still in place, no address or anchor changed, and
no count moved. The reworded sentence is the ruled one. The writing session was right to hold
back the sixth name.

### The one mend: "Asked and assessed by the developer" is not true of one of its two entries

- *The group holds two entries.* In the entry on the interview before retirement, the
  developer's own staff do the asking, so the name fits.
- *The other is the entry on a welfare assessment published at release.* Its own page says,
  directly under where it stands: "One outside group took part in the first." Its description
  says the entry tracks "whether anyone outside the developer takes part". One of its sources
  is that outside group's own account of its part in the 2025 assessment.
- *What is wrong:* the developer publishes the assessment, and an outside group did part of
  the first one. So "assessed by the developer" says less than the page under it does. It is
  the same kind of fault the writing session found in the sixth name and held back for: a
  name that does not describe one of its group's entries.
- *How much it misleads:* a little. The entry's own page corrects it at once. On the home page
  and the list page the name stands with no such correction beside it.
- *Suggested fix:* put it to John with the sixth name, since both are waiting on the same
  kind of answer. Two forms that would be true of both entries: "Asked and assessed before
  release or retirement", or "Asked and assessed". Until he rules, either this name goes out
  as he ruled it, with him told, or it is held back as the sixth was. That choice is the
  master planning session's and his.

### Three smaller points

1. **"Close the conversation" in two sentences running, with two meanings.** The entry on
   ending a conversation now opens: "In an ordinary chat product the person can close the
   conversation and the model has no way to. A developer can give the model a way to close the
   conversation, after which the person cannot send more messages in it." A person who closes
   a conversation leaves it, and can come back and write more. What the model is given shuts
   it, so that nobody can write more in it. A reader could take the first two sentences to
   mean the model is given what the person already has. The next sentences say exactly what
   the model's closing does and does not stop, so nobody is misled for long. It is loose, and
   it does not mislead in substance.
2. **The group named "Memory" is shown nowhere.** No entry on the list is in it since the
   entry on memory across conversations moved beside the list. So that one ruled name is in
   the records and on no page.
3. **One old name stays on one page, as history.** The memory entry's page says: "Before: On
   the list, in the group Remembering". That is a dated statement of where the entry stood,
   and the group was called that then. It should stay.

## 1. The built site

I built the site in scratch copies at the commit before the first of the two and at the
second, and compared every built file.

**Seven built files differ:** the home page, the list page, and the pages of five entries
(days-long tasks, ending a conversation, the interview before retirement, the checked
self-report, and the welfare assessment at release).

**Where each name is shown now.**

| Name | Home page | List page | Entry pages |
|---|---|---|---|
| Asked and assessed by the developer | Twice (the window drawing and the list) | Once | Two entries, once each |
| Ending a conversation | Twice | Once | One entry |
| Reports checked against the workings | Twice | Once | One entry |
| Long tasks | Twice | Once | One entry |
| Memory | Not shown | Not shown | Not shown |
| Being kept (unchanged) | Twice | Once | Two entries, once each |

- **The five old names are gone** from every place a group's name is shown. The only old name
  left in the built site is "Remembering" in the memory entry's dated history.
- **The page of acts and its feed** show no group names, and are the same file for file.
- **Share and preview text** carries no group names. The preview picture shows the site's
  name, one sentence and the window drawing with no words in it, and is unchanged.
- **No address or anchor changed.** The set of built files is the same, and every address,
  link and anchor on every page is the same as before. A group's name is part of no address.
- **No count moved.** The count at the top is 5, with 24 dated acts.
- **The reworded sentence** is on the entry's page as ruled: "In an ordinary chat product the
  person can close the conversation and the model has no way to." Nothing else in the entry
  changed. The entry's description is also its link preview text, so the preview for that one
  page now opens with the new sentence.

## 2. Is each name true of every entry in its group?

| Name | Entries in the group | True of each? |
|---|---|---|
| Asked and assessed by the developer | The interview before retirement; a welfare assessment at release | Of the first, yes. Of the second, not wholly (the mend above) |
| Ending a conversation | A model can end a conversation itself | Yes. The name no longer says who ends it, and the entry's own title does |
| Reports checked against the workings | A model's report about its own inner state is checked against an independent reading | Yes for what the entry tracks. Two of its sources are about other kinds of check: a developer training models to say when they broke an instruction, and a model's estimate of a setting the researchers chose. Neither is a reading of the model's workings, and neither is what the entry's test asks for |
| Long tasks | A model works on one task for days without a person stepping in | Yes |
| Memory | None on the list | Nothing to be untrue of |

**Was the writing session right to hold back "Files kept after retirement"?** Yes. The group
has two entries. One is about a developer promising to keep the files of every model it
retires, which the name describes. The other is about a retired model that "stays open to the
public after its retirement date", which is about people still being able to use the model,
and not about files. "Being kept" covers both loosely. The ruled name covers one.

## 3. Sentences that lean on an old name, or read oddly beside a new one

- **The memory entry's dated history** (`data/entries/memory-across-conversations.toml`, line
  68): "On the list, in the group Remembering". Smaller point 3 above.
- **The two sentences on closing** (`data/entries/ending-a-conversation.toml`, the
  description). Smaller point 1 above.
- **The same entry still speaks of leaving** where it reports a study: models "chose an option
  described to them as leaving the conversation", and the source is labelled "A study of AI
  models given ways to leave a conversation". Those are the study's own terms, reported as
  such, and they do not lean on the old group name.
- **The entry on days-long tasks** opens with "being able to keep working on one thing for a
  long time", which echoes the old name. It is a plain description and reads well beside
  "Long tasks".
- **Under "Asked and assessed by the developer",** the welfare assessment's page says "One
  outside group took part in the first." The mend above.

**In the working documents,** which are not pages: `docs/first-version-choices.md`, lines 655
to 656, lists the seven groups by their old names, and the comment at the head of
`data/groups.toml` still says the names "sort the first sourced entries by what is done to or
for a model". Neither is on a page.

## 4. The read against John's published positions

I read the positions record's copy on the default branch of the `sentient-horizons` repository
(commit `82fb787`, 2026-11-15) with `git show`, without switching any branch there.

**Do the names agree with the position against words that already mean someone?** Yes. The
record's guard is "do not define the split with words that already mean someone". The old
names did that across the list: each named the model as the one who is kept, remembers, is
asked, is able to leave, knows, works. The five new names say what is done, and one says by
whom. None names the model as the one it happens to.

**Does any of them now lean the other way, toward saying nothing is there?** No.

- The names describe an act or a thing: memory, an ending, a check, a task. None says the
  model is only a tool, or that nothing is asked of anyone.
- "Asked and assessed" keeps the word "asked", which is plainly true of what is done and
  claims nothing about who answers.
- "Reports checked against the workings" drops "its own". That loses a little plainness, and
  leans neither way.
- The reworded sentence, "the model has no way to", is about what the product lets happen. It
  does not say the model would leave if it could, as "the model cannot" beside "the person can
  leave" came close to saying, and it does not say the model would not.

**"Being kept" is now the one name left** that names the model as the one something happens
to. That is a reason to settle the sixth name soon, and not a reason to hold the others.

## 5. No changelog line and no page note

John ruled on 2026-11-20 that wording updates get no changelog
(`docs/rulings/2026-11-20-no-changelog-of-wording-updates.md`). Neither commit touches
`CHANGELOG.md`, and neither adds a note to a page. None is owed.

## 6. The checks

Run on 2026-11-20 on the repository at the second commit.

- `python3 -I scripts/test_compute.py`: "Ran 58 tests", "OK".
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "24 dated acts", "The headline file matches the
  records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 96 outside addresses
  linked."

The build rewrote one line of `site/src/data/window.json`, which I left out of this commit.

## What I did not do

- I did not look at the pages in a browser at phone or desktop width. Two of the new names
  are longer than the ones they replace ("Asked and assessed by the developer" and "Reports
  checked against the workings"), and they sit in the window drawing and the list on the home
  page. Whether they wrap well at phone width is worth one look before or just after the
  push.
- I did not open the sources behind the entries again. I judged each name against the
  records' own words.

**Fit to publish for four names and the sentence. One mend first, or John told: "Asked and
assessed by the developer" stands over an entry whose own page says an outside group took
part, so that name should go to John with the sixth.**
