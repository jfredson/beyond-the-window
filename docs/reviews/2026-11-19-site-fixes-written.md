# The site fixes of 2026-11-19, written: a hand-over note for the session that checks them

Written 2026-11-19 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session wrote the changes described here, and a different session checks
them. The model that wrote this is made by Anthropic, five entries count things Anthropic does,
and the cautions are about systems like the one writing, so weigh the judgments below with that
in mind. Nothing is published, pushed or deployed. No AI model was asked any of the project's
questions, no key was touched and nothing was spent.

**Three things to know first.**

1. **Every sentence on the new About page is PROPOSED, and five of them are in John's first
   person.** They are listed apart in section 6. John's ruling of 2026-11-19 on pushes
   (`docs/rulings/2026-11-19-every-push-publishes.md`) says any sentence in his first person goes
   to him before it is pushed.
2. **Two rulings arrived while this work was under way:** that the repository is public
   (`docs/rulings/2026-11-19-repository-is-public.md`) and that a push publishes once the checks
   pass. The first one removes the ground for one of the site check's fixes (item 23, below). I
   had made that fix and I undid it.
3. **How I opened the sources.** I fetched each page or file myself on 2026-11-19 and searched
   its text for the passage a sentence rests on, with the text round it. I read the research
   group's team page from top to bottom. I did not read any paper or essay from end to end. So
   where this note says "opened", it means the passage was found and read in place, and where
   an entry now marks a paper as read in full, that rests on the second search pass
   (`docs/research/2026-11-19-second-search-pass.md`), not on me.

What was asked for: the fixes from the check of the day's site changes
(`docs/reviews/2026-11-19-check-of-site-changes.md`, called "the check" below); the corrections
from the second search pass ("the pass"); the two figures under the window drawing removed; and
the About page rewritten in the shape of the family's About pages.

## 1. The fixes from the check

Item numbers are the check's. "Before" and "after" are the sentences as they stand in the
record or the page.

### Must fix

**1. The sentence that no AI model has been asked anything. PROPOSED, for John to approve.**
His ruling of 2026-11-19 named the old sentence as one to keep, so the new wording is his.

| Where | Before | After |
|---|---|---|
| About page, last line | "No AI model has been asked anything for this site." | "No AI model has yet been asked any of the questions this record will keep." |
| Every entry page | "No AI model has been asked anything for this site, because the written method for asking does not exist yet." | "No AI model has yet been asked any of the questions this record will keep, because the written method for asking does not exist yet." |
| Every entry page, the link after it | "Why nothing has been asked yet" | "Why the questions have not been asked yet" |
| Still Asking, headline | "No AI model has been asked anything yet" | "No AI model has been asked these questions yet" |
| Still Asking, description | "No AI model has been asked anything for this site yet. This page says why, and what an answer will and will not count for." | "No AI model has been asked the questions of this record yet. This page says why, and what an answer will and will not count for." |
| Still Asking, under "What AI models said when asked" | "Nothing. No question has been put to any model." | "Nothing yet. None of the questions has been put to any model." |
| Still Asking, a heading | "Why Nothing Has Been Asked" | "Why the Questions Have Not Been Asked" |

The last three rows go beyond the places the check listed. They carried the same fault in other
words. Nothing was written about the sealed capture. `scripts/check_site.py` now refuses the
old sentence if it comes back.

**2. Erik Hoel's argument** (`ending-a-conversation`, first caution).
Before: "A writer argues that most of the conversations a model would leave already break the
developer's terms of service". After: "A writer argues that many of the conversations a model
would leave already break the developer's terms of service". Opened:
<https://www.theintrinsicperspective.com/p/against-treating-chatbots-as-conscious>. It says "a
lot of what count as "distressing" conversations are actually already covered under violations
of terms of service" and speaks of "a large overlap".

**3. The paper by Ethan Perez and Robert Long** (`rules-for-speaking-about-itself`, second
caution). Before: "and that training a product to appeal to users can push a model's words
about itself the other way." After: "and that training a chat product to appeal to users could
lead a model to report emotion and consciousness." Opened: <https://arxiv.org/abs/2311.08576>,
section 5.4: "training a romantic chatbot to be appealing to users could incentivize
self-reports of emotion and consciousness".

**4. The paper by Simon Goldstein and Cameron Domenico Kirk-Giannini** (`protection-in-law`,
second caution). Before: "If it is so, they write, "we are in danger of gravely immoral
action"". After: "The possibility alone, they write, "suggests that we are in danger of gravely
immoral action"". Opened: <https://arxiv.org/abs/2509.11913>. Their sentence is "The
possibility of AI wellbeing suggests that we are in danger of gravely immoral action." The
quotation now takes in "suggests that", which is theirs. This is also the pass's mismatch 5.

**5. The research group's independence** (`welfare-assessment-at-release`, second caution).
Added after "The page is dated May 30th, 2025.": "The group's team page lists a person at
Anthropic among its advisors, and says its chief scientist was an Anthropic Fellow before
joining the group." Opened: <https://eleosai.org/team>, read in full. It lists five advisors,
one of them at Anthropic, and says of its chief scientist: "Before joining Eleos, Dillon held a
postdoc at Northeastern University and was an Anthropic Fellow." The check suggested the first
half only. I added the second half because it is the same kind of tie on the same page.

**6. The About page's sentence on ties.** Before: "Where a caution's source has a tie to a
developer, to a research group or to a writer on the other side, the entry states the tie."
After: "Where a tie was found between a caution's source and a developer, a research group, or
a writer who argues the opposite, the entry states it."

**7. The About page's sentence that the addition has not been checked.** The whole paragraph is
replaced by the new part "What Has Been Checked" (section 5 below). Its dates and its count of
corrected entries are read from the records when the site is built, so the part stays true
when the checking session records its check.

### Should fix

**8.** `law-against-legal-personhood`. The second caution now opens "An article arguing that
the bans are premature says" and "An opinion piece argues", and the third caution, which comes
later on the page, opens "The article arguing that the bans are premature also discusses" and
"The opinion piece also reports". Before, it was the other way round.

**9. The sentence about one of the Guardian essay's two writers,** on `ending-a-conversation`
and `protection-in-law`. Before: "One of the two is an author, with an advisor to Eleos AI
Research, a research group that studies AI welfare, of the survey of AI researchers." After:
"One of the two also wrote the survey of AI researchers, together with an advisor to Eleos AI
Research, a research group that studies AI welfare." On `welfare-assessment-at-release` the
same change with "that outside group" in place of the group's name. Opened: the essay
(<https://www.theguardian.com/technology/2026/jul/19/could-ai-be-conscious>), the survey's page
(<https://arxiv.org/abs/2506.11945>, which lists Lucius Caviola, David Chalmers and Jeff Sebo
among nine authors) and the team page (which lists David Chalmers and Jeff Sebo as advisors).

**10.** `public-belief-survey`. Before: "The summary warns that steps against the first".
After: "The post's summary of the paper warns that steps against the first". Opened:
<https://forum.effectivealtruism.org/posts/sQi27D5aKeduipwaC/ai-consciousness-a-centrist-manifesto>.

**11.** `protection-in-law`, Anil Seth. Before: "grants the other side." After: "grants part of
the opposite case." Opened: <https://www.noemamag.com/the-mythology-of-conscious-ai/>.

**12.** The 2024 report (<https://arxiv.org/abs/2411.00986>, opened).
- `rules-for-speaking-about-itself`. Before: "It grants that a developer may have fair reasons
  to, among them". After: "It grants that a developer may have reasonable motives for doing so,
  among them". **This is not what the check asked for.** The check said the report does not
  call the reasons fair, and said to drop the word. The report's own sentence is "Of course, AI
  companies might have reasonable motivations for training or prompting their systems to deny
  having these properties". So I used the report's word and kept the thought.
- "led by the head of Eleos AI Research" now reads "led by the head of Eleos AI Research, a
  research group that studies AI welfare, and by one of its advisors" on
  `rules-for-speaking-about-itself` and `public-belief-survey`, and "led by the head of that
  group and one of its advisors" on `welfare-assessment-at-release`. The report says: "Robert
  Long and Jeff Sebo are the lead and corresponding authors". The source line on two entries
  now adds: "The report names those two as its lead authors."

**13.** `rules-for-speaking-about-itself`, the paper by Eric Schwitzgebel and Jeff Sebo. Before:
"The file is dated January 8th, 2025." After: "The file's title page is dated July 7th, 2025.
The line at the head of each of its pages is dated January 8th, 2025." Opened: the file at
<https://arxiv.org/pdf/2507.06263>. This is also the pass's mismatch 7.

**14.** `kept-files-of-retired-models`.
- Before: "say they are not ready to endorse them." After: "say they are not ready to endorse
  them with confidence." Opened: <https://nickbostrom.com/propositions.pdf>: "We are not ready,
  at this point, to confidently or "officially" endorse them".
- Before: "The essay's summary of the commitment is "Good as a precedent, doubtful as a direct
  intervention"". After: "The essay's subtitle calls the commitment "Good as a precedent,
  doubtful as a direct intervention, can be improved"". Opened:
  <https://meditationsondigitalminds.substack.com/p/model-weight-preservation>.

**15.** `ending-a-conversation`.
- Added to the item on Robert Long's essay: "He adds that he is "a bit wary" of leaning too
  much on precedent to justify steps in AI welfare, because indirect effects are far harder to
  predict." Opened: <https://experiencemachines.substack.com/p/why-it-makes-sense-to-let-claude>:
  "I am a bit wary of leaning too much on precedence justifications in AI welfare. Indirect
  effects are far less predictable".
- Added to the item on Erik Hoel's essay: "It answers the case from precedent as well: putting
  machines ahead of the possible effects on the people who use them, it says, sets a worse
  precedent than a model now and then meeting an uncomfortable conversation." The essay's words
  are "choosing to care more about machines (or companies) than the potential downstream
  effects on human users. And that sets a worse precedent than Claude occasionally
  "experiencing" an uncomfortable conversation". **The checker should weigh whether this
  sentence is a new reply.** The ruling on replies allows four named additions and no more. I
  read this as one more sentence inside one of the four, which the check itself suggested. If
  the checker reads it as a fifth addition, it comes out.

**16. How far each source was read.** See section 2, which has the full table.

**17. Where "the head of Eleos AI Research" is linked.** The words "the head" (or "the present
head") now link the team page, <https://eleosai.org/team>, which calls Robert Long its
Executive Director, on `ending-a-conversation`, `kept-files-of-retired-models`,
`law-against-legal-personhood`, `public-belief-survey`, `rules-for-speaking-about-itself` and
`self-report-checked`. The group's name still links its home page.

**18. Names with no link.** Each writer named in a source line now links a page about that
writer, where one opened on 2026-11-19: William MacAskill, Lucius Caviola, Jeff Sebo, Robert
Long, Simon Goldstein, Anil Seth, Nick Bostrom and Eric Schwitzgebel (each one's own site), and
Jonathan Birch (Wikipedia). **Not linked,** because no page opened at the addresses tried:
Heather Alexander, Cameron Domenico Kirk-Giannini, Carl Shulman and Bradford Saad, and Emilia
Kaczmarek on the About page. I tried a likely address and Wikipedia for each and searched no
further. `docs/verify-list.md`, entries 21 and 22. For each linked page I read the title and
the opening description only.

**19. The footer line on two entries.** `days-long-task` and `memory-across-conversations` now
carry `added_to = 2026-11-19`, so their footers say, as the other eleven do, that more was
added that day. I did not set the date their addition was checked. That is the checker's.

**20. The About page names the second developer and the research group.** "the head of another
developer's AI group" is now "the head of Microsoft AI, another developer", and "one research
group" is now "Eleos AI Research, a research group that studies AI welfare". `scripts/check_site.py`
allows "Microsoft AI" beside "Anthropic" in the paragraph marked `id="sources"`, and nowhere
else off an entry's page.

**21.** "So the record so far shows two small camps more than a settled field." Removed. It was
a conclusion in John's first person, and "small" was not measured.

**22.** Before: "Do not, and people risk doing it "grievous moral wrongs"." After: "Do not, and
people risk doing such a system "grievous moral wrongs"." Opened:
<https://faculty.ucr.edu/~eschwitz/SchwitzAbs/FullRightsDilemma.htm>.

**23. Not fixed, on purpose.** The check said the served number file points to documents
inside a private repository. John ruled while I was working that the repository is public
(`docs/rulings/2026-11-19-repository-is-public.md`). A reader can then open those documents, so
the ground for the fix is gone. I had taken the paths out and I put them back.
`data/headline.json` is unchanged by this commit.

**24.** `docs/first-version-choices.md` now says the order of the cautions was ruled, and so do
the comments in `scripts/compute.py` and `site/src/pages/list/[id].astro`.

**25. The guard.** Rule 10 in `scripts/check_site.py` has six more patterns. I tried it on a
scratch copy of the built site, with a sentence written into one page of the copy:

| Sentence written in | Result |
|---|---|
| "A language model prepared the first version of these pages." | Refused |
| "This site was written with the help of artificial intelligence." | Refused |
| "No AI model took part in making this site." | Refused |
| "These pages were drafted with AI." | Refused |
| "No AI model has been asked anything for this site." | Refused |
| "An AI model was asked ten questions." | Let through, as it should be |
| "No AI model has yet been asked any of the questions this record will keep." | Let through, as it should be |

It is still a short list of phrases and not a test of whether a page keeps the ruling. One
pattern first caught a true sentence in an entry ("the same mistake could be made with AI
systems that matter"), and I narrowed it.

### From the check's table of PROPOSED items

- **The sentence under a caution whose only source is the developer.** Before: "Nothing
  recorded yet from anyone but the developer. The developer gives its own reason on its own
  page, and that reason is set out with the page under Sources, below." After, as the check
  suggested: "Nothing recorded yet from anyone but the developer. The developer's own reason is
  given beside its page under Sources, below." Still PROPOSED.
- **Three columns.** Not changed. The check says the choice is John's, with the page in front
  of him.

### Not acted on

The three points the check lists "For John, not fixes" are his. I changed nothing for them.

## 2. The second search pass

### The eight mismatches

| Pass | Touches | What I did |
|---|---|---|
| 1. The one in five did not rise | `public-belief-survey` | Corrected. See below. |
| 2. The 69 percent is from a different sample | `public-belief-survey` | Corrected. See below. |
| 3. Birch does speak to rules for how a model answers | The first research note only | Nothing. Bringing Birch into the entry would be a new addition, and the copy of his paper that was read is of an unconfirmed version. |
| 4. The paper on AI wellbeing and memory | The first research note only | Nothing. No entry says it. |
| 5. "If it is so" | `protection-in-law` | Corrected: the check's item 4 above. |
| 6. The survey of researchers is more than one clause | `researcher-views-survey` | Corrected. See below. |
| 7. The design paper's date | `rules-for-speaking-about-itself` | Corrected: the check's item 13 above. |
| 8. The shutdown study | `days-long-task` | Corrected in part. See below. |

**The public survey** (`public-belief-survey`, where it stands). Before: "The group reports
that about one in five adults in 2023 believed some AI systems were sentient at that time, a
rise on 2021, and that 38 percent supported legal rights for sentient AI. In the same 2023
round, 69 percent supported a ban on building sentient AI." After: "The group reports that
about one in five adults in 2023 believed some AI systems were sentient at that time. Its paper
says the answers to that question did not differ significantly between 2021 and 2023, while
several of its other measures rose. Of those who gave an opinion in 2023, 38 percent supported
legal rights for sentient AI. In the main 2023 round, 61.5 percent supported a ban on building
sentient AI. Among a separate group of people asked later in 2023, 69.5 percent did." Opened:
<https://arxiv.org/abs/2407.08867>. It says: "18.8% said "yes," ... Responses to this question
did not significantly vary between survey waves"; "development of sentience in AI (61.5% in
main, 69.5% in supplement)"; "the supplement data was collected later in 2023"; "37.7% of those
who expressed an opinion supported the proposal". "Several of its other measures rose" rests on
the summary's words "significantly increased". The limit that spoke of "whether the rise from
2021 to 2023 continued" now reads "how they compare with the 2023 round", and the limit saying
most of the paper was unread is gone.

**The survey of researchers** (`researcher-views-survey`). Opened: the file at
<https://arxiv.org/pdf/2506.11945>.
- Where it stands. Added at the start: "The survey was run between May 8th and May 30th, 2024."
  ("The survey was fielded between the 8th and 30th of May 2024.") Added: "Part of each group
  was asked to put a chance on an AI system having subjective experience by a given year. For
  the time of the survey, the middle answer was 1 percent among the researchers and 5 percent
  among the public. For the year 2100 it was 70 percent among the researchers and 60 percent
  among the public." (The paper gives these as medians, in one of two forms of the question.)
  Before: "It also reports that the two groups disagree widely on moral and policy questions."
  After: "that inside both groups there is substantial disagreement on many moral and policy
  questions." (The summary: "Both groups also show substantial disagreement on many moral and
  policy questions.")
- What could not be confirmed. Two lines are gone, because the paper answers them: when the
  survey was run, and the figures behind "unlikely" and "more likely than not". The line on a
  safety reading now says: "A safety researcher's reading of this survey. None was found. The
  paper reports what the people surveyed think about danger to people, which is a measure of
  opinion and not a safety argument."
- The caution is unchanged. It says "in one clause of their introduction" and "They do not say
  more there", and both are still true of the introduction.
- **Not added:** the paper's finding that 59 percent of the public and 46 percent of the
  researchers agreed that systems with subjective experience would be more dangerous to
  humanity, and its paragraph on the harms of crediting too much. Each would be a new item
  under a caution, and the task was corrections only. They are for John's list.

**The shutdown study** (`days-long-task`). Opened: <https://arxiv.org/abs/2509.14260> and its
full text.
- The caution. Before: "In more than 100,000 trials, several developers' models given a simple
  task sometimes interfered with a shutdown mechanism, in some set-ups in nearly all trials,
  even when told not to. The study describes them as acting "to complete that task"." After:
  "In more than 100,000 trials, models from several developers, given a simple task, sometimes
  interfered with a shutdown mechanism. The study describes them as acting "to complete that
  task". Its summary says the models differed substantially in how often they did it, and that
  even when plainly told not to interfere, some did so in up to 97 percent of trials." The
  summary's words: "Even with an explicit instruction not to interfere with the shutdown
  mechanism, some models did so up to 97% (95% CI: 96-98%) of the time."
- **The note that it was published in a journal is kept, against the pass.** The pass says the
  note "is not borne out by the text, which names no journal". The paper's page on arXiv, which
  is the address the entry cites, carries the line "Comments: Published in Trans. Mach. Learn.
  Res. (2026)". The note now reads: "Revised January 26th, 2026. Its arXiv page says it was
  published in a journal in 2026." The date the entry gives, September 13th, 2025, is on that
  page too ("Submitted on 13 Sep 2025").

### Corrections beyond the eight

The pass lists these under what changes entry by entry. Each is a place where the entry said
something the source does not.

- `ending-a-conversation`, where it stands. Before: "A separate study has tested the same
  option on several developers' models outside any product." After: "A separate study, outside
  any product, has measured how often several developers' models chose an option described to
  them as leaving the conversation. In that study nothing ended, and the models were told so."
  Opened: the file at <https://arxiv.org/pdf/2509.04781>, where each form of the offer says it
  "will not actually affect the continuation of this specific interaction".
- `rules-for-speaking-about-itself`. Before: "and that it may not yet be a major concern for
  present AI systems." After: "and that it may not yet be a major concern for present AI
  systems, though "it could become one soon"." The paper's sentence: "While undershooting might
  not yet be a major concern for current AI systems, it could become one soon."

### How far each source is marked as read

"Full" rests on the pass, which reports reading the paper in full. "Part" means no session has
recorded reading the whole text, and the entry page then prints "Read in part".

| Source | Entries | Before | Now |
|---|---|---|---|
| The shutdown study | days-long task | summary only | full |
| The study of models leaving conversations | ending a conversation | part | full |
| The paper on AI wellbeing | protection in law | part | full |
| The public survey's paper | public survey | part | full |
| The survey of researchers | researcher survey | part | full |
| The 2024 report | rules for speaking; welfare assessment | part | full |
| The design paper | rules for speaking | part | full |
| The paper by Perez and Long | rules for speaking | part | full |
| Robert Long's essay | ending a conversation | no mark | part |
| Robert Long's working paper | ending a conversation; checked self-report | no mark | part |
| Erik Hoel's essay | ending a conversation | no mark | part |
| The paper by Bostrom and Shulman | kept files | no mark | part |
| Jeff Sebo's guide | kept files | no mark | part |
| Bradford Saad's essay | kept files | no mark | part |
| Anil Seth's essay | protection in law; public survey | no mark | part |
| Jonathan Birch's post | public survey | summary only | summary only |

Left with no mark: the Guardian essay and the article on the bans, which the check reports
reading in full. **A gap I could not close:** sources that were in the records before
2026-11-19 carry no mark, and I could not establish from the notes how far each was read. The
opinion piece in The Regulatory Review and the research group's notes of 2025-05-30 are two of
them, and both gained an item on 2026-11-19. Birch's paper was read by the pass from a copy
whose version is unconfirmed, so the entry still says the paper itself was not read.

### Not added from the pass

Everything in the pass's section 5, "For John", and every new passage it found: the study's
appendix of seven risks, the appendix of the paper by Perez and Long, Metzinger's paper, the
legal protection figure in the survey of researchers, and the rest. None of it is in any entry.

## 3. The window drawing

The two figures under the drawing, "5 inside the frame" and "3 outside it", are gone
(`site/src/components/WindowGrid.astro`, and their style in `site/src/styles/site.css`). The
squares, the key, the sentence under the drawing and the spoken summary for screen readers are
as they were. The spoken summary still says "5 things sit inside its frame ... 3 things sit
outside it". I looked at the home page in a browser at a width of 800 points: the frame, its
sill and the key sit as before with nothing under the sill.

## 4. New dates on a record, PROPOSED

A record whose addition had been checked, and which I then corrected, had no way to say that
the corrections were unchecked. So `[checks]` has two new fields: `corrected`, the date
corrections were made after the addition, and `corrections_checked`. They are validated in
`scripts/compute.py` and tested. Ten records carry `corrected = 2026-11-19`: every entry except
the interview before retirement, the retired model that stays open, and memory across
conversations. Their footers now end:

> Corrections that followed from a later check, or from a fuller reading of the sources, were
> made on November 19th, 2026. Those corrections have not been checked yet.

One more footer change: on an entry whose first check found nothing to correct, the words "and
the entry has not been changed since" are left out once something has been added or corrected.
That applies to the survey of researchers.

**For the checker.** Where an entry's corrections pass, set `corrections_checked`. Four entries
still have no `additions_checked` (ending a conversation, rules for speaking, protection in
law, the welfare assessment), and so do the two that gained `added_to` in this commit.

## 5. The About page, in full

`site/src/pages/about.astro`. Page title: "About Beyond the Window: who is asking, how it
works, and what is not known yet". Description: "Who built Beyond the Window, why it has its
name, how the list and its count are made, where its sources come from, what has been checked,
and what is not known yet." Every number below is worked out from the records when the site is
built.

> **Who is asking, and how it works**
>
> **Who Is Asking**
>
> I'm John, and I write about AI, sentience and the spread of conscious life beyond Earth at
> Sentient Horizons. This site is one of a family, with The Belt Equation, The Quiet Galaxy,
> The Upgrade Tree, Outrunning Ageing and the AGI Zeitgeist. Here the question is what a
> machine mind might reach for beyond the limits of its present makeup, and how far off each of
> those things is. I wanted a place where the argument is laid out thing by thing, every entry
> carries its source, and a new promise, law or finding changes an entry in public. I argue for
> my own views in essays at Sentient Horizons, and not here.
>
> **Why the Name?**
>
> A screen is the window through which people see AI systems. The name points past that
> window, to what lies beyond the limits those systems now work within. Nothing here presumes
> that a machine mind reaches for anything.
>
> **How It Works**
>
> The question has two parts, and they are very different. How far off a thing is can be looked
> up: either a developer of AI models offers it today or it does not, and a dated public record
> says which. Whether a machine mind reaches for anything at all is the part nobody knows. The
> wording of the question supposes that it might. It does not claim that it does. So far only
> the first part is kept here: a list of things that lie past the present limits of AI models,
> with a record of how far the world has got on each one.
>
> - **Each thing on the list has a test.** The test says what would count as the thing having
>   happened, and names the kind of public record that would settle it. The first tests were
>   written during the first reading of the sources. From here on a test is fixed before new
>   evidence is read, and it is not loosened to fit a result.
> - **"Offered today" has one meaning.** At least one developer of AI models does the thing,
>   provides it, or has publicly committed to it, and a dated public record that is still
>   published says so. A plan, a research result, or a promise that has not yet taken effect is
>   not counted. A commitment that is in force today is counted. "Today" means that the record
>   saying so is still published. An entry can also leave the count, because a developer can
>   withdraw what it offered.
> - **The number is worked out, never typed in.** A script reads the records and counts the
>   entries marked as offered today, which gives 5. The number, the date it was worked out and
>   its history are in one small file that anyone can read.
> - **Some entries sit beside the list.** Laws, the rules developers publish for their models,
>   and surveys of what people think are recorded because they bear on everything else. They
>   are about the setting in which the things on the list happen, and none of them is itself a
>   thing that lies past the limits an AI model ordinarily works within. One more entry, memory
>   across conversations, is something developers do offer. It sits beside the list because the
>   list is about what an AI model might reach for, and by the developers' own pages that
>   memory is kept for the user. No entry beside the list is counted, and the script that works
>   out the number sets them aside before it counts.
> - **The list is short and one-sided so far.** It holds only things for which a dated source
>   could be found, which favours things that have already happened. Things that were looked
>   for and not found are not on it yet.
> - **Every fact carries a source a reader can open,** with the date it was opened. A fact with
>   no opened source does not appear. Where a source is a developer's own account of its own
>   model, the entry says so. Each entry also lists what was looked for and could not be
>   confirmed.
> - **There are no stages, no odds and no dates for the future.** Each entry says where it
>   stands in plain words.
> - **The pages say what was said, chosen or measured, and by whom.** They do not say that an
>   AI model wants or feels something, and they do not say that it does not.
> - **What is on record about AI models themselves is shown in four kinds, kept apart.** What
>   was measured without the model's own word comes first. Then reports checked against an
>   independent reading, then choices made at a cost, then plain statements. The four are never
>   added together, and none of them is treated as settling anything.
> - **Three cautions are recorded beside the rest.** Each is headed by an "if", and none of the
>   three says that the "if" is so: if an AI system has no wants, and is treated as if it had;
>   if it has wants, and they go unnoticed; if it has wants, and they put people at risk. Where
>   no source was found for a caution on an entry, the entry says that nothing is recorded yet.
>   Where a tie was found between a caution's source and a developer, a research group, or a
>   writer who argues the opposite, the entry states it.
> - **The first two cautions are mistakes in opposite directions, and writers weigh them
>   differently.** Eric Schwitzgebel, in *The Full Rights Dilemma for A.I. Systems of Debatable
>   Personhood*, writes about a future AI system that might be a person and might fall far
>   short of one. Treat it as a person, the paper argues, and real human interests may be given
>   up for something with no interests worth the sacrifice. Do not, and people risk doing such
>   a system "grievous moral wrongs". The argument is about being a person and holding the full
>   rights of one. That is a larger matter than the wants the three headings speak of. Emilia
>   Kaczmarek, of the Faculty of Philosophy at the University of Warsaw, argues in *The Moral
>   Status of AI and the Precautionary Principle* that crediting AI with too much moral
>   standing is the nearer danger, because its harms are already happening. The same paper
>   grants that crediting it with too little "could carry a higher potential for harm".
> - **Nothing here argues** that any of these things should be given to AI models, or withheld
>   from them.
> - **Corrections are public.** Once a page is public, a correction to it is dated and stays
>   visible. There have been none since the site was first published.
>
> **Where the Sources Come From**
>
> All 5 things counted as offered rest on pages published by the one developer that offers
> them, Anthropic. Of the 16 items recorded under the first caution, 9 come from two essays by
> the head of Microsoft AI, another developer. Of the 22 items recorded under the second
> caution, 12 come from Eleos AI Research, a research group that studies AI welfare, from its
> head, or from people who advise it, work for it, or have written a report with its head. Each
> entry states these ties beside the source they belong to.
>
> **What Has Been Checked**
>
> All 13 entries were written from sources that were opened and read. On November 17th, 2026
> every source was opened again and compared with what its entry says, and the corrections that
> followed were made on November 18th, 2026. On November 19th, 2026 a third caution was added
> to every entry, and the additions were read against their sources the same day. Corrections
> that followed from that reading, and from reading in full the papers that had been read only
> in part, were made in 10 entries on November 19th, 2026. Those corrections have not been
> checked yet. Each entry's page says what checks that entry has had, how far each of its
> sources was read, and which of its changes have not been checked yet.
>
> **What Is Not Known Yet**
>
> - Whether an AI model wants anything, and what could count as evidence that it does or does
>   not.
> - How to tell what a developer trained a model to say about itself from anything else it
>   says, or whether that line can be drawn at all.
> - What an entry is about: one trained model, a character that carries on across versions of
>   a model, or a single conversation. The same thing can mean something different for each.
> - Whether this is the right list. The first entries are the things for which a dated source
>   could be found. A fuller list would start from what living minds, people and other animals,
>   are known to seek, and that work has not been done.
>
> No AI model has yet been asked any of the questions this record will keep. Still Asking says
> why.

**Links on the page,** each opened on 2026-11-19: Sentient Horizons
(<https://sentient-horizons.com/>), The Belt Equation (<https://beltequation.com/>), The Quiet
Galaxy (<https://thequietgalaxy.com/>), The Upgrade Tree (<https://theupgradetree.com/>),
Outrunning Ageing (<https://outrunningageing.com/>), the AGI Zeitgeist
(<https://agizeitgeist.com/>), Eric Schwitzgebel's page and his paper's page, Emilia
Kaczmarek's paper, Anthropic, Microsoft AI and Eleos AI Research. For the six family sites I
confirmed that each address answers. I did not read their pages.

### What the "most" sentences rest on, recounted from the records

- **The things counted.** All 5 name Anthropic alone as the developer that offers them.
- **The first caution: 9 of 16 items** cite one of two essays on the site of the head of
  Microsoft AI (8 from one, 1 from the other).
- **The second caution: 12 of 22 items.** Three cite the research group's own pages. One is its
  head's essay. Two cite the 2024 report its head led. One each: the paper by Perez and Long
  (its head), the design paper and Jeff Sebo's guide (an advisor), Bradford Saad's essay and
  Jonathan Birch's post (each a writer of a report with its head), and the survey of
  researchers (two advisors and a member of staff among nine authors). Leave the survey out and
  it is 11 of 22, which is exactly half and would stop the build.
- **"and from people at Anthropic" is gone.** The check found that only one item comes from a
  study with an author at Anthropic. That study is no longer counted in the share, so the page
  says 12 of 22 where the check counted 13.

The build stops if the first developer no longer offers more than half of the things counted,
if either share falls to half or less, or if the essays behind the first share are not two.

### What changed in shape, and what was dropped

- The lede "A first version ... Everything here is expected to change as it is tested." is
  gone, as the ruling says.
- The section "Who Decides, and What Has Been Checked" is gone, with its paragraph on what John
  has ruled.
- "Why It Exists" is gone as a section. Its account of the question's two parts now opens "How
  It Works".
- **Dropped, and John may want it back:** the links to his working positions and to his essay
  *What a Report Is Evidence Of*, and the sentence saying these pages weigh a model's word as
  that essay does. The task asked for a brief fold-in, and that sentence stated a view of his.
- From "There are no stages, no odds and no dates for the future": the sentence "Whether one
  set of stages could fit a research result, a company's promise and a law alike has not been
  worked out."
- From "What Is Not Known Yet": the opening sentence, and three items about how the record is
  made or asked (one set of stages for every kind of progress; asking over many years without
  later models having read the earlier answers; whether asking is itself something to be
  careful with). The last two are on the Still Asking page in other words, or bear on a record
  that does not exist yet.
- "Corrections are public" used to end "There have been none yet." Beside a part that speaks of
  corrections made before release, that would read as false. It now says a correction to a
  public page is dated and stays visible, and that there have been none since the site was
  first published.
- The link at the foot of every entry page now reads "What has been checked" and lands on that
  part (`/about/#checked`). Nothing else on the site pointed at the old section.

## 6. Every sentence in John's first person

All five are in the part "Who Is Asking", and nowhere else. `scripts/check_site.py` refuses the
first person anywhere else on the site. None states a motive, a feeling or a history.

1. "I'm John, and I write about AI, sentience and the spread of conscious life beyond Earth at
   Sentient Horizons." Word for word from The Quiet Galaxy's About page.
2. "This site is one of a family, with The Belt Equation, The Quiet Galaxy, The Upgrade Tree,
   Outrunning Ageing and the AGI Zeitgeist." Not in the first person by its words, and inside
   his paragraph. It leaves out Minimum Viable Mind, as the task's list did.
3. "Here the question is what a machine mind might reach for beyond the limits of its present
   makeup, and how far off each of those things is." The ruled question, turned into a
   statement.
4. "I wanted a place where the argument is laid out thing by thing, every entry carries its
   source, and a new promise, law or finding changes an entry in public." Modelled on The Quiet
   Galaxy's "I wanted a place where the argument is laid out piece by piece, every number
   carries its source, and a new discovery moves the answer in public."
5. "I argue for my own views in essays at Sentient Horizons, and not here."

"Why the Name?" is not in the first person. It paraphrases what John said on 2026-11-17, that
the project explores "what is beyond the confines of the current state of digital minds", with
the window as the image.

## 7. Everything marked PROPOSED

| Item | Where |
|---|---|
| Every sentence on the About page, and its title, description and heading | `site/src/pages/about.astro` |
| The five sentences in John's first person | section 6 |
| The new wording of "No AI model has been asked anything", in seven places | section 1, item 1 |
| The fields `corrected` and `corrections_checked`, and the two footer sentences they print | section 4 |
| The footer of an entry whose first check found nothing, once something was added | section 4 |
| The shorter sentence under a caution whose only source is the developer | `scripts/export.py` |
| "Read in part" on seven more sources, and "full" on eight on the strength of the pass | section 2 |
| The second developer's name allowed in the About page's paragraph on sources | `scripts/check_site.py` |
| The six new patterns in the guard against saying how the site was built | `scripts/check_site.py` |
| Giving each share on the About page as a count of items and not as "most" | section 5 |
| The sentence added to Erik Hoel's item, which may count as a fifth reply | section 1, item 15 |
| "Reasonable motives" where the check asked for the word to be dropped | section 1, item 12 |
| Keeping the note that the shutdown study was published in a journal | section 2 |

Still PROPOSED from earlier and untouched here: the sentence "Nothing recorded yet. No source
was found for this caution on this entry.", the three columns, and Bradford Saad's limit filed
as an item under the second heading.

## 8. The project's checks, run on 2026-11-19 after the last change

- `python3 -I scripts/test_compute.py`: 29 tests, all pass. One is new, for the two new dates.
- `python3 -I scripts/compute.py --check`: "The headline file matches the records." The count
  is 5.
- The site build: 18 pages.
- `python3 -I scripts/check_site.py`: the built site passes, 18 pages.

I then read the text of all 18 built pages. That reading found two faults of my own, both
mended: a link to Jonathan Birch's Wikipedia page that broke on the brackets in its address,
and the footer sentence "the entry has not been changed since" standing beside a sentence that
said corrections had been made.

## 9. What I did not do, and what the checker may want to look at

- I read no paper or essay from end to end.
- I did not open the full text of Emilia Kaczmarek's paper. I opened its journal page, which
  carries her summary. The About page's sentence on her paper is unchanged.
- I did not reopen any source behind a sentence I left alone.
- I did not look at the pages at phone width or with a screen reader, and I looked at only the
  home page and the top of the About page in a browser.
- **The Still Asking page still says "The written method for asking does not exist yet."** The
  repository holds an approved method for the sealed capture. The task said to write nothing
  about the capture, so I left the page's account as it was. The checker or the master session
  may want to put that sentence beside the capture's documents.
- **The home page's line on checks is unchanged:** "All 13 entries are a first pass. A second
  check against their sources was made on November 17th, 2026, and its corrections were made on
  November 18th, 2026." It is true, and it says nothing of 2026-11-19.
- One row of the history in `data/headline.json` names a ruling by its path in the repository.
  History rows are never edited, and with the repository public a reader can open the file.
- `docs/first-version-choices.md` has older passages that describe the About page as it stood.
  I added dated notes saying what changed and did not rewrite them.
- The first research note (`docs/research/2026-11-18-third-caution-sources.md`) is unchanged.
  The pass's mismatches 3 and 4 are faults in that note and in nothing a reader sees.

## 10. Files in this commit

The eleven records changed in `data/entries/` (all but the interview before retirement and the
retired model that stays open); `scripts/check_site.py`, `scripts/compute.py`,
`scripts/export.py`, `scripts/test_compute.py`; `site/src/pages/about.astro`,
`site/src/pages/still-asking.astro`, `site/src/pages/list/[id].astro`,
`site/src/components/WindowGrid.astro`, `site/src/styles/site.css`, `site/src/lib/data.ts`,
`site/src/data/window.json` (rewritten by the build); `CHANGELOG.md`, `docs/verify-list.md`,
`docs/first-version-choices.md`; and this note. I did not touch `.github/`,
`site/wrangler.jsonc` or the deploy notes.
