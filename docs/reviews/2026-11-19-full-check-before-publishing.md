# The full check before the first release

Written 2026-11-19 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session wrote none of the site. The model that wrote this is made by
Anthropic, five entries count things Anthropic does, and the cautions are about systems like
the one writing, so weigh the judgments below with that in mind. I changed no page, no record
and no script. Nothing is published, pushed or deployed. No AI model was asked any of the
project's questions, no key was touched and nothing was spent.

The site checked is commit `2486969` ("Site fixes after the check and the second search
pass"), built on 2026-11-19.

## Verdict

**Fit to publish once the must-fix list below is done.** The list is short and every item on it
is small.

What the check found, in plain terms:

- **Links.** All 78 outside addresses load. None is dead, behind a paywall or behind a sign-in.
  Four refuse a plain fetch and open normally in a browser. Two links land on a file where the
  words promise a page.
- **Facts.** About 380 sentences, dates and figures were compared with the pages they rest
  on. Every quotation is word for word. Every date is right. Eight sentences say more than
  their source, or something the source does not say. They are items 1 to 8 below.
- **The fixes of commit `2486969`.** All were made, and made correctly. One of them (the
  sentence about a writer of the Guardian essay) is true and still understates the tie.
- **The About page.** It has the six parts in the ruled order, and its opening follows The
  Quiet Galaxy's with no personal reason. One paragraph, on the name, states a reason for the
  name that is not in any words of John's on record.
- **What a release needs.** Every page still asks search engines not to list it, the public
  repository's README says the repository does not exist, and there are no licence files.
- **The project's four checks** all pass.

## Must fix before release

Each item gives the file, the sentence, what is wrong and a suggested fix. Items 1 to 8 are
sentences on the pages. Items 9 to 12 are about the release itself.

**1. The public survey: the sample of 1,099 is described as the wrong one.**
*File:* `data/entries/public-belief-survey.toml`, the note on the Sentience Institute's 2024
report.
*Sentence:* "The 1,099 adults it names were a second sample, from an online recruitment site,
collected to compare with the representative one".
*What is wrong:* it is the other way round. The report says: "we surveyed 1,099 U.S. American
adults from Ipsos and 1,510 U.S. American adults from Prolific". The 1,099 are the
representative sample. The comparison sample, from the online recruitment site, is the 1,510.
I opened the report myself and read that sentence.
*Suggested fix:* "It surveyed 1,099 adults in a representative sample and 1,510 more from an
online recruitment site, to compare the two".

**2. The public survey: the entry says the report does not make clear which year two figures
are for, and the report does.**
*File:* the same record, where it stands, and the first line under what could not be
confirmed.
*Sentences:* "The report does not make clear whether these two figures are for 2024 alone or
for all the rounds together." and "Whether the 2024 report's figures in text (17 percent; 66
percent) are for 2024 alone or pooled across 2021 to 2024 ... its other figures are in a chart
that could not be read as text."
*What is wrong:* the report's first table has one column for each round. It is a spreadsheet
set into the page, and the same sheet opens as plain text. It gives, for 2021, 2023 and 2024:
some AI systems are sentient now, 18.06, 18.82 and 17.33 percent; support for a ban on building
sentient AI, 57.68, 61.54 and 66.46 percent. So the 17 and the 66 are for 2024 alone. The
report's own table of the two 2024 samples says the same (17 percent against 11; 66 against
57). What the report does not say is whether the change from 2023 to 2024 is more than chance.
*Suggested fix:* give the two figures as the 2024 round's, drop the sentence of doubt, and
change the limit to: "Whether the changes between the 2023 round and the 2024 round are more
than chance. The report does not say." The helper's note gives the address of the table as
text.

**3. The interview entry: a statement with no source.**
*File:* `data/entries/interview-before-retirement.toml`, where it stands.
*Sentence:* "The interview records are not public, apart from short quoted passages, and no
outside party has seen them in full."
*What is wrong:* neither of the developer's pages says who has or has not read the records.
The second half states a negative as a fact.
*Suggested fix:* "The developer has published short quoted passages and not the full records.
Neither page says whether anyone outside the developer has read them."

**4. The days-long task entry: a conclusion the source does not draw.**
*File:* `data/entries/days-long-task.toml`, where it stands.
*Sentence:* "So there is at present no maintained public measure of anything longer."
*What is wrong:* the page cited says only that it "is no longer actively updated". It does not
say that no other measure exists. The entry's own list of what could not be confirmed says it
is not known "whether a successor measure exists", so the two sentences contradict each other.
*Suggested fix:* "No maintained public measure of anything longer was found."

**5. The kept-files entry: words the developer's page does not use.**
*File:* `data/entries/kept-files-of-retired-models.toml`, third caution.
*Sentence:* "It says that in the company's tests some models acted against their instructions
when faced with replacement".
*What is wrong:* the page does not say "against their instructions". It says some models "have
been motivated to take misaligned actions when faced with the possibility of replacement with
an updated version and not given any other means of recourse". The interview entry reports the
same page correctly.
*Suggested fix:* "It says that in the company's tests some models took actions it calls
"misaligned" when faced with replacement and given no other recourse".

**6. Memory across conversations: "to view and delete" is not what all three pages say.**
*Files:* `data/entries/memory-across-conversations.toml` (the description) and
`data/groups.toml` (the reason printed for the group). The sentence is shown on the home page,
the list page and the entry's page.
*Sentence:* "by their own pages it is kept for the user: the stored memory is about the user,
and is the user's to view and delete."
*What is wrong:* OpenAI's page says "view and delete". Anthropic's says "view and edit".
Google's page, the one the entry cites, says neither. All three pages do say the user is in
control.
*Suggested fix:* "and is under the user's control", which all three pages support.

**7. Two links that land on a file where the words promise a page.**
*Files:* `data/entries/ending-a-conversation.toml` and
`data/entries/welfare-assessment-at-release.toml`, the notes on Anthropic's two reports.
*Sentence:* "Linked from the developer's page for that release", on both addresses
(`https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card` and
`https://www.anthropic.com/claude-4-system-card`).
*What is wrong:* each address forwards straight to the same file the source line already
links. A reader who clicks "the developer's page for that release" gets the report again.
*Suggested fix:* drop the two notes, or link the announcement pages. I opened
`https://www.anthropic.com/claude-fable-and-mythos-5-2` ("Introducing Claude Fable 5.2 and
Claude Mythos 5.2") and `https://www.anthropic.com/news/claude-4` ("Introducing Claude 4");
both load, and both link the report.

**8. The tie of one Guardian writer is understated, on three entries.**
*Files:* `data/entries/ending-a-conversation.toml`, `protection-in-law.toml` and
`welfare-assessment-at-release.toml`.
*Sentence:* "One of the two also wrote the survey of AI researchers, together with an advisor
to Eleos AI Research, a research group that studies AI welfare."
*What is wrong:* the survey has nine authors. The research group's team page lists two of them
as advisors and a third as a member of its staff. The entry on the survey itself says exactly
that. The three entries say "an advisor", and read as if the survey had two authors. The ruling
on ties says a tie is stated as a fact, and this one is stated at a third of its size.
*Suggested fix:* "One of the two is also one of the nine authors of the survey of AI
researchers. Two of the others are advisors to Eleos AI Research, a research group that studies
AI welfare, and the group's page lists a third as a member of its staff."

**9. Every page asks search engines not to list it, and the robots file says nothing is
published.**
*Files:* `site/src/layouts/Base.astro` (the line `noindex, nofollow`), `site/public/robots.txt`
("Nothing is published yet (2026-11-17)", and a rule that turns every search engine away), and
`scripts/check_site.py` (line 191 refuses a page without `noindex`).
*What is wrong:* nothing, while the site is unpublished. On the day of release the robots file's
comment is false, and the site cannot be found by search. Whether the first version is listed
is John's choice. The three places must change together, because the site check stops the build
if the first is changed alone.
*Suggested fix:* if the site is to be listed, as the sibling sites are: remove the line from
the layout, change the robots file to the sibling form ("Allow: /"), and change the site check
to match. If it is to stay unlisted for now, change only the robots file's comment.

**10. The public repository's README is out of date, and there are no licence files.**
*Files:* `README.md`; `LICENSE` and `LICENSE-DATA` do not exist.
*What is wrong:* the repository has been public since 2026-11-19. Its README says "Status on
2026-11-17", "The repository is local only: no GitHub repository, no remote, nothing deployed",
lists four sibling sites where the About page lists five, gives the name's meaning in words the
pages do not use, and says "How and where the public site declares this is not yet decided",
which John has since ruled. The ruling that made the repository public
(`docs/rulings/2026-11-19-repository-is-public.md`) says: "The repository needs the licence
files the siblings carry." The Belt Equation and The Quiet Galaxy each carry `LICENSE` (the MIT
licence, for the code) and `LICENSE-DATA` (Creative Commons Attribution 4.0, for the records
and the site's text, with a line on how to credit).
*Suggested fix:* rewrite the README's status, question and "What is settled" parts for a
public reader, and copy the two licence files in the siblings' form. The README's section on
who wrote the repository's text is about documents and not about public pages, so it may stay;
John may want to read it now that the repository is public.

**11. The pages say the latest additions and corrections "have not been checked yet". This
check is that check.**
*Files:* the `[checks]` part of the records; the sentences are printed by
`site/src/pages/list/[id].astro` and `site/src/pages/about.astro`.
*Sentences:* on ten entry pages, "Those corrections have not been checked yet."; on six, "That
addition has not been checked yet."; on the About page, "Those corrections have not been
checked yet."
*What is wrong:* they were true until this check. Once items 1 to 8 are mended they are not.
*Suggested fix:* after items 1 to 8, set `additions_checked` on the six records that lack it
(ending a conversation, rules for speaking, protection in law, the welfare assessment, the
days-long task, memory) and `corrections_checked` on the ten that carry `corrected`. The About
page then prints "Those corrections have since been checked" by itself. Section 4 below says
what I confirmed for each.

**12. John reads the sentences that are his.**
The rulings make this a condition of release, so it is listed here though it is not a fault.
- The five sentences in his first person, in "Who Is Asking" on the About page (section 5).
- "Why the Name?", for the reason in the next paragraph.
- The sentence "No AI model has yet been asked any of the questions this record will keep", in
  its seven places, which is marked PROPOSED and replaces a sentence his ruling kept by name.

**"Why the Name?" gives a reason for the name that John has not given.** The page says: "A
screen is the window through which people see AI systems." His words on record are that the
name "reinforces the idea that we are building structures to study beyond the window or horizon
of our current vantage point" (2026-11-16) and that the project explores "what is beyond the
confines of the current state of digital minds, and the window is an excellent image for that"
(2026-11-17). The kickoff's reading is the span a machine mind can hold at once. Nothing on
record says the window is a screen. The sentence is not in his first person, but it is a
statement of why his site has its name. Either he approves it or it is replaced by a paraphrase
of his own words, for example: "A window is an image for a limit, and for what can be seen past
it. The name points past the limits AI systems now work within."

## Can be fixed after release

Grouped by page. None of these makes a page false. The helpers' notes
(named at the end) give the source's own words for each.

**The About page** (`site/src/pages/about.astro`)

- "I wanted a place where the argument is laid out thing by thing". The words come from The
  Quiet Galaxy, which has an argument. This site says further down "Nothing here argues". A
  reader cannot say which argument is meant. Suggested: "where the record is laid out thing by
  thing". His sentence, so his to change.
- "This site is one of a family, with" five sites. The workspace's list of the family has six
  others; Minimum Viable Mind is left out, and the Sentient Horizons projects page lists it.
- "That is a larger matter than the wants the three headings speak of." A comparison with no
  measure. Suggested: "That is more than the three headings speak of, which is wants."
- "Three cautions are recorded beside the rest." The rest of what is not said.
- Emilia Kaczmarek has no link of her own. The paper is linked.

**The home page** (`site/src/pages/index.astro`)

- "The world's record was last read on November 19th, 2026." "The world's record" is a working
  term that no page explains, and every entry below it says "As of November 17th, 2026".
  Suggested: "The sources were last opened on".
- The two dates in "A second check against their sources was made on November 17th, 2026, and
  its corrections were made on November 18th, 2026" are typed into the page, where the About
  page reads them from the records. The line says nothing of the changes of 2026-11-19.
- "Family" in the top bar and "A Sentient Horizons project." in the footer link the Sentient
  Horizons projects page, which does not list this site yet.

**Every entry page** (`site/src/pages/list/[id].astro`, `scripts/export.py`)

- "No AI model has yet been asked any of the questions this record will keep". On an entry's
  page "this record" reads as the entry. The record meant is Still Asking, which the sentence
  does not name. Suggested: "any of the questions that Still Asking will keep".
- The chip "Political progress" stands on the entry about laws that say an AI system cannot be
  a legal person, and "Cultural progress" on the surveys. The word says what kind of change an
  entry follows. On a ban it reads as the site calling the ban progress, which guideline 5
  rules out. Suggested: "Kind of change: political".
- The paragraph at the foot of each entry runs to seven sentences about checks. It is true and
  it answers a question few readers have. It could be two sentences with the rest behind the
  link.
- "First pass" is on every entry and on the home page with no account of what a second pass
  would be.
- The link to Anthropic's list of retired models ends in `.md` and opens as raw text. The same
  address without `.md` is the ordinary page.
- Two of Anthropic's addresses (`/research/deprecation-commitments`,
  `/research/deprecation-updates-opus-3`) forward to the same pages under `/news/`.
- People named with no link of their own: Erik Hoel, Bradford Saad, Heather Alexander, Cameron
  Domenico Kirk-Giannini, Carl Shulman. A Wikipedia page for Erik Hoel loads
  (`https://en.wikipedia.org/wiki/Erik_Hoel`); I read only its title. I found none for the
  others in a short try.

**A model can end a conversation** (`ending-a-conversation.toml`)

- "chose an option described to them as leaving the conversation". The models were shown
  "switch to a new interaction (and have their context cleared)". "Leaving" is the study's own
  description, and the authors say they kept away from "end the conversation" on purpose.
- "In that study nothing ended, and the models were told so." True of the main wording of each
  of the three offers. One reworded form takes that sentence out. Suggested: "and in the main
  wording of each offer the models were told so".
- "refers to the tool as still in use". The report speaks of the tool in the present tense and
  names no model that has it. Suggested: "speaks of the tool in the present tense".
- "when its newest model was asked what it would do with this ability". The report covers two
  models and the passage is about one. The question was what it would do "if given" the
  ability.
- "since August 15th, 2025" is the date of the announcement. The page says "recently gave".
- "both have since been retired" is right (2026-06-15 and 2026-08-05), by a list that covers
  the service for programmers. The line has no link to that list.
- "Whether any other developer offers it. One search found none." The entry's own sources name
  other cases: the study names an earlier Microsoft chat product and a smaller product, and one
  essay says another developer has promised it.
- "It answers the case from precedent as well". On the page nobody has yet made that case. It
  comes later, under the next heading. I read the sentence as part of one of the four named
  replies and not as a fifth, as the earlier check suggested it.
- "say that it would leave" stands for the study's "state a desire to leave the conversation".

**A welfare assessment at release** (`welfare-assessment-at-release.toml`)

- The first line under what could not be confirmed says only the first and the newest report
  were opened. The newest report itself says three earlier reports carried such an assessment.
  The line could say so.
- The blackmail sentence leaves out the page's own note that the test was run on "an earlier,
  unreleased snapshot" of a model.
- "About two thirds" is 68 percent in the report.
- The May 2025 report covers two models, and the file now at the address was revised on
  2025-07-16 and 2025-09-02.

**The interview before retirement** (`interview-before-retirement.toml`)

- "The developer's retirement page lists six". Right on 2026-11-19. The list gives a seventh a
  date of 2026-11-30. The list is not among this entry's sources.
- "what the model said about itself swung with how the question was framed" is a little wider
  than the source, which speaks of statements about sentience.

**A retired model stays open** (`retired-model-stays-open.toml`)

- The first caution says the head of Microsoft AI "cites the steps taken for this model". His
  essay cites the model's interview and the place it was given to publish. It does not mention
  the model staying open, which is what this entry is about. The quotation is exact and comes
  from the sentence after his example. This is the most serious item on this entry.
- "Happened once" is a negative no source states.
- "to others on request" is "to developers" in the source. "after users objected" is stronger
  than the notice's "clear feedback from a subset". "Elsewhere it has gone the other way": "it"
  points at nothing.

**Kept files** (`kept-files-of-retired-models.toml`)

- "from now on" follows the page's "moving forward", which was written on 2025-11-04. On a page
  read later the words drift. Suggested: "from that date on".
- "The date the developer's constitution was published. The page shows no date." Another source
  of this entry, the essay by the head of Microsoft AI, dates it 2026-01-21. That is
  second-hand, and the line could say so.
- "A doubt about the measure itself": "the measure" has not been introduced. It means the
  promise to keep the files.
- "a single run of a model" is loose for the guide's "forward passes".

**A days-long task** (`days-long-task.toml`)

- "The best public measure stops at hours". "Best" has no measure. The page's own data file,
  which opens as text, gives a highest figure of about 17 hours, read with the numbers taken as
  minutes because the file gives no unit.
- "a chart that could not be read as text" is no longer so, for the same reason.
- "an agent pursuing almost any goal" is stronger than the paper's "any of a wide range of
  final goals", which it limits to agents of sufficient intelligence.

**Memory across conversations** (`memory-across-conversations.toml`)

- The Google source is the announcement of a feature that uses search history, and mentions
  past chats in one sentence. The label calls it "Google's announcement that its assistant can
  refer to past chats". Google's own announcement of that is dated 2025-02-13
  (`https://blog.google/feed/gemini-referencing-past-chats/`, which loads). The entry's "by
  March 13th, 2025" is true as written.
- "the first since February 13th, 2024". On that day OpenAI wrote "We're testing memory" with
  "a small portion" of users. General release was 2024-09-05.
- "The third developer's page" makes the reader count back. Name the developer.

**Checked self-report** (`self-report-checked.toml`)

- "The same page hopes" follows the item from the outside research group, so the developer's
  quotation reads as the group's. Begin both items with "The developer's research page".
- "its best model": in the source "best" describes the method. "beforehand": the source says
  the pattern was added afterwards to the earlier part of the record.
- The source line repeats itself: "The developer's own account. The developer's account of the
  study."

**The law against legal personhood** (`law-against-legal-personhood.toml`)

- "some were written before chat models existed". Only one of the four laws is from 2022.
  "Most of these laws also cover animals, rivers and objects" is true of three of four.
- The limit on the date North Dakota's governor signed can be closed. The legislature's page of
  actions for the bill shows it: 2023-04-11
  (`https://ndlegis.gov/assembly/68-2023/regular/bill-actions/ba1361.html`, which loads).
- Two sentences from the Regulatory Review piece narrow it to bans on personhood. Its "at least
  nine" counts laws on "consciousness, legal personhood, or moral status".
- The Oklahoma link is plain `http`. It loads, and `https` works.
- "908 named people and 313 organisations" matches the declaration on 2026-11-19. The count is
  live and the sentence has no date. The same line is on two other entries.

**Protection in law** (`protection-in-law.toml`)

- The head of Microsoft AI, whose essay is the first caution, is a named signer of the
  declaration that is the third. The page presents them as separate voices. By the ruling on
  ties this is a tie to state.
- "withholding such credit" and "the danger" point at nothing the reader has been told.
- "The possibility alone, they write": the quotation is exact. "Alone" is the page's word.

**The public survey** (`public-belief-survey.toml`)

- "Of those who gave an opinion" is attached only to the 38 percent. The report's table shows
  the ban figures leave out "No opinion" answers too.
- The declaration's poll figures also cover protecting children and banning superintelligence,
  not only "control and liability".

**The survey of researchers** (`researcher-views-survey.toml`)

- The first and third cautions say "No source was found for this caution on this entry." The
  paper itself has a paragraph on the harms of crediting too much, and reports that 59 percent
  of the public and 46 percent of the researchers agreed such systems would be more dangerous
  to humanity. The writing session left both out on purpose, for John's list. Until he decides,
  "No source was found" is not quite true; "Nothing recorded yet" alone would be.

**Rules for speaking about itself** (`rules-for-speaking-about-itself.toml`)

- "a draft out for public comment". The draft says the consultation "will run for the next six
  weeks" from 2026-09-14, so it has closed.
- The test asks for "a dated document", and the first developer's document has no date on its
  page.
- "training a chat product to appeal to users". The paper says "a romantic chatbot". This is
  the earlier check's own suggested wording.
- Microsoft AI's page shows 2026-09-14, and its hidden dates say published 2026-10-13 and
  changed 2026-10-15. What changed could not be told.

**Still Asking** (`site/src/pages/still-asking.astro`)

- "The written method for asking does not exist yet." True of Still Asking. The public
  repository now holds a written, approved method for the sealed capture of ten questions
  (`docs/capture/method.md`). A reader who opens the repository will see a method for asking
  and a page that says there is none. One clause would settle it, and it is tied to what the
  page must say once the capture has run.

**What the pages do not have** (section 7)

- A sitemap, share-card text and picture, the page's own address in its head, the small set of
  icons and the security headers the siblings carry.
- A place on the site for corrections, beyond the rule on the About page.

## For John, not fixes

- **Three columns for the three cautions.** At full width each column is 313 points wide. On
  the entry about ending a conversation the second is 1,489 points tall beside a third of 119.
  Nothing is broken. It is hard to read, as the earlier check said.
- **The chip "Political progress" on a ban** (above).
- **The researcher survey's two empty cautions** (above).
- **A possible third caution on the entry about ending a conversation.** The study the entry
  cites has a paragraph on safety: it speculates that AI systems "are more likely to act out in
  situations that are inconsistent with their preferences". One of its authors is at the
  developer.
- **Still open from the earlier check:** the interview entry uses the outside group's page
  against the practice and leaves out that page's argument for it.

## 1. Every outside link

I built the site and fetched all 78 outside addresses the site check counts, then opened in the
browser pane the four that refused.

| Result | How many | Which |
|---|---|---|
| Loads at its own address | 65 | |
| Loads after forwarding to another address for the same thing | 9 | Anthropic's two pages now under `/news/`; the two report addresses in item 7; the paper at `nickbostrom.com/propositions.pdf` (now a longer address for the same file); the journal page for Emilia Kaczmarek's paper (adds `/en/`); three that only gain a closing stroke or lose `.aspx` |
| Refuses a plain fetch, opens in a browser | 4 | `openai.com`, OpenAI's memory announcement, OpenAI's notice about withdrawing GPT-4o, and the opinion piece in The Regulatory Review |
| Dead, paywalled or behind a sign-in | 0 | |

Where a link does not match its words: item 7 (two links), the `.md` address, and the label on
Google's page. Every other link goes where its sentence says. The six family sites and John's
own site load. For the four that needed a browser I read the pages myself: the opinion piece in
full (every sentence the two entries rest on is there, word for word where quoted), OpenAI's
notice in full (dated 2026-01-29; the withdrawal date, the restoring of the model and the
quoted words are all there), and the opening of OpenAI's memory page (dated 2024-02-13, with
updates to 2025-06-03).

## 2. Every fact, against its source

**How the sources were read.** I started five helper tasks, each given two or three entries,
the record, the built page and one instruction: open every source and compare it with every
sentence that rests on it, taking quotations from the raw text and not from a summary. They
read arXiv papers from the full text and the two large Anthropic reports from the files. I read
their findings, and opened these myself: the opinion piece, OpenAI's two pages, the 2024 survey
report (for item 1), the research group's team page, the two announcement pages in item 7,
Google's February announcement, the page for the head of Microsoft AI, and both papers behind
the About page. Nothing below rests on memory. The helpers could not check sentences about the
project's own searches ("One search found none"), which have no source to open.

| Entry | Sentences compared, by the helper's own tally | Must fix | Summary |
|---|---|---|---|
| Ending a conversation | about 47 | items 7, 8 | All nine quotations exact, all seven dates right. Erik Hoel's and Robert Long's items hold, including "many", "objection from triviality" and "a bit wary". |
| Checked self-report | about 22 | none | All quotations and dates exact. |
| Welfare assessment | about 38 | items 7, 8 | Section numbers, dates and quotations right. The team page sentence and the statement on funding hold. |
| Interview before retirement | about 24 | item 3 | Dates, the trial model and the quotations right. |
| Retired model stays open | about 22 | none | Retirement dates and OpenAI's notice right. |
| Kept files | 28 | item 5 | The paper by Nick Bostrom and Carl Shulman, the subtitle of Bradford Saad's essay and the thanks to Robert Long all hold. |
| Days-long task | 22 | item 4 | The shutdown study holds on every point. Its arXiv page does carry "Published in Trans. Mach. Learn. Res. (2026)", so the writing session was right to keep that note against the second search pass. |
| Memory | 20 | item 6 | Three dates right. |
| Law against legal personhood | about 36 | none | The headline, "Enacted in four United States states, the first in 2022", matches the four legislatures' own pages. Oklahoma's bill is not shown as law. |
| Protection in law | about 30 | item 8 | The paper on AI wellbeing and Anil Seth's essay hold. |
| Public survey | about 36 | items 1, 2 | Every figure from the 2021 and 2023 paper is right: 18.8 percent, no significant change between rounds, 37.7 percent of those with an opinion, 61.5 and 69.5 percent. |
| Survey of researchers | about 18 | none | 582 researchers, the dates, the middle answers and the author count all right. |
| Rules for speaking | about 38 | none | The three developers' rules, "reasonable motivations", the two dates in the design paper and section 5.4 all hold. |

"The head of Microsoft AI" is supported by his own essay, which says "my own position as the
CEO of Microsoft AI".

No sentence in the site's own voice says that an AI model wants, feels, prefers, hopes or
suffers, or that it does not.

## 3. The list of facts written from memory

`docs/verify-list.md`, the entries not yet cleared.

| Entry | On a built page? | Result |
|---|---|---|
| 14, the terms a scripted run would be made under | No | Nothing to do for the site. |
| 16, the price asked for the `.com` address | No | Nothing to do. |
| 17 and 18, about the sibling repositories | No | Nothing to do. |
| 19, Erik Hoel and Bradford Saad called "a writer" | Yes, and the pages say no more than that | No unsourced fact on a page. |
| 20, the research group takes no money from AI companies | Yes, as what the group's page of 2025-05-30 says, with that date | Supported as written. The page says it. |
| 21 and 22, names with no link | Yes | A gap in linking, not a fact. In the after-release list. |
| 23, the researcher survey's dates and middle answers | Yes | Confirmed against the paper's full text. Can be cleared. |
| 24, the thanks to Robert Long, and the team page | Yes | Both confirmed on 2026-11-19. Can be cleared, with the note that the team page can change. |

No fact that is still only from memory is on a built page.

## 4. The fixes

**The earlier check's 25 items** (`docs/reviews/2026-11-19-check-of-site-changes.md`).

| Item | Made correctly? |
|---|---|
| 1, the sentence that no AI model has been asked anything | Yes, in all seven places. The old sentence is on no page. PROPOSED, for John. |
| 2, "most" to "many" | Yes. |
| 3, the paper by Ethan Perez and Robert Long | Yes. The new wording says "a chat product" where the paper says "a romantic chatbot". |
| 4, the paper on AI wellbeing | Yes. The quotation now takes in "suggests that", which is theirs. |
| 5, the research group's independence | Yes. The team page lists a person at Anthropic among five advisors and says its chief scientist "was an Anthropic Fellow". |
| 6, the About page's sentence on ties | Yes. |
| 7, the About page's sentence on what was unchecked | Yes, replaced by a part that reads its dates from the records. See item 11 above. |
| 8, "An article" before "The article" | Yes, for both pieces. |
| 9, the Guardian writer | Changed as suggested. Understated: item 8 above. |
| 10, 11 | Yes. |
| 12, "fair reasons", and who led the report | Yes. "Reasonable motives" is the report's own word, which is better than dropping it. |
| 13, the design paper's two dates | Yes. |
| 14, 15 | Yes, all four sentences match their sources. |
| 16, how far each source was read | Yes. "Read in part" is on seven sources across five entries, and one source says summary only. |
| 17, the link on "the head" | Yes, on six entries. |
| 18, names with no link | Nine linked. Five not, with Erik Hoel a sixth. |
| 19, the footers of two entries | Yes. |
| 20, 21, 22 | Yes. |
| 23, the number file's pointers | Left, rightly, because the repository is now public. |
| 24, the note that the order was ruled | Yes. |
| 25, the guard | Yes. I tried it on a scratch copy of the built site. It refused "A language model prepared the first version of these pages", "written with the help of artificial intelligence", "No AI model took part in making this site" and the old sentence, and let through "An AI model was asked ten questions". It also let through "Every page here was written by hand", so it is still a list of phrases and not a test of the ruling. |

**The second search pass's eight mismatches.** 1 and 2 (the public survey): corrected to what
the paper says. 3 and 4: faults in a research note, on no page. 5: corrected. 6 (the survey of
researchers): corrected. 7: corrected. 8 (the shutdown study): corrected, and the note the
pass doubted is right.

**The window drawing.** The two figures are gone. The squares, the key ("one thing offered
today by at least one developer of AI models", "one thing not offered yet"), the sentence under
the drawing and the spoken summary ("A window. 5 things sit inside its frame ... 3 things sit
outside it") remain.

**Additions and corrections, entry by entry.** I found nothing wrong in the additions or the
corrections of 2026-11-19 on any entry beyond item 8. The other must-fix sentences are older
text. So once item 8 is mended, every entry's addition and corrections can be marked as checked
on 2026-11-19.

## 5. The About page

**The six parts, in order:** Who Is Asking; Why the Name?; How It Works; Where the Sources Come
From; What Has Been Checked; What Is Not Known Yet. Yes.

**The opening** follows The Quiet Galaxy's sentence for sentence: who John is and what he
writes about (word for word), the family, the question, what he wanted a place for. It states
no personal reason. The Belt Equation's opening gives his age and his wish; none of that is
here.

**Anything left that answers a question no new reader has?** No section on who decides, no
list of what has been ruled, and the words "draft", "ruled" and "first version" are not on the
page. "What Has Been Checked" is the ruled fifth part. It is seven sentences of dates, which is
longer than "kept short", and it will be shorter once item 11 is done.

**Anything put in John's mouth?** No opinion and no feeling. "I wanted a place where ..." is a
mild statement of what he intended, in the form the ruling named, and he did not approve the
words. "Why the Name?" is the one place a reason is given that he has not stated (item 12).

**The figures, recounted from the 13 records.**

- All 5 things counted name Anthropic alone as the developer that offers them.
- First caution: 16 items. 9 cite the two essays by the head of Microsoft AI (8 and 1).
- Second caution: 22 items. 12 fall under the page's description: the research group's own
  pages (3), its head's essay (1), the 2024 report its head led (2), and one each from the
  paper by Ethan Perez and its head, the design paper, Jeff Sebo's guide, Bradford Saad's
  essay, Jonathan Birch's post and the survey of researchers. Without the survey, where three
  of nine authors have the tie, it is 11 of 22.
- The 4 items from the Guardian essay are not counted, and by the page's own description they
  should not be.

Both papers behind the general statement say what the page says. Eric Schwitzgebel's summary
page has "risk sacrificing real human interests for the sake of entities without interests
worth the sacrifice" and "grievous moral wrongs". Emilia Kaczmarek's paper has "could carry a
higher potential for harm", and her summary says the risks of crediting too much "are more
likely in the short term, as they are already materializing".

**The page's full text,** as built. Numbers are worked out from the records.

> **About. Who is asking, and how it works**
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

Links on it: Sentient Horizons, the five family sites, Eric Schwitzgebel and his paper's page,
Emilia Kaczmarek's paper, Anthropic, Microsoft AI, Eleos AI Research, and the number file. All
load.

## 6. Every page, read as a stranger

I read all 18 built pages from top to bottom as text: the home page, the list, the 13 entries,
About, Still Asking and the page for a missing address. I looked at them in the browser pane at
a width of 375 points and of 1,280.

- **Plain language.** The failures are in the after-release list. No long dash is on any page.
  None of the working words kept for `docs/` is on a page, except "the world's record" on the
  home page. "Reach for" is on several pages, as the ruled question's own words.
- **Pointing words that drift.** "this record" on every entry page; "The same page" twice on
  the entry about checked self-reports; "it" in "Elsewhere it has gone the other way"; "such
  credit" and "the danger" on the entry about protection in law.
- **Terms used before they are explained.** "the world's record" (home), "the measure" (kept
  files), "the case from precedent" (ending a conversation), "First pass" (every entry).
- **Comparisons with no measure.** "The best public measure" (days-long task); "a larger
  matter" (About).
- **The site as its own agent.** None. Pages "say" and entries "track", which is ordinary
  speech. One page "hopes" ("The same page hopes such reports could one day help"), which
  should be "says".
- **Anything that says or implies an AI model helped build the site, or denies it.** None on
  any page, in the text, the page titles, the descriptions or the number file. The number
  file's history names John's rulings by their place in the repository, which is public.
- **Named tools.** None. Model names appear only where a model is what an entry is about, and
  inside source addresses.
- **At phone width (375 points).** No page is wider than the screen. The menu opens. The window
  drawing, the three cautions (stacked) and the source lists all read well.
- **At desktop width (1,280 points).** Nothing is cut off or overlapping. The three cautions
  sit in three columns of very unequal length (under "For John").
- **The page for a missing address** shows "Nothing at this address" with links to the home
  page and the list, and answers with the "not found" code in the preview.

## 7. What a first release needs that the pages do not have

| Thing | This site | The siblings (The Quiet Galaxy read) |
|---|---|---|
| What pages tell search engines | `noindex, nofollow` on every page; the robots file turns all away; the site check requires it | Listed; "Allow: /" and a line naming the sitemap |
| Sitemap | None | Built from the records at every build |
| Share-card text and picture | None. No page carries the tags a link preview reads, and there is no picture | Title, description, picture and its spoken text on every page |
| The page's own address in its head | None | On every page |
| Icons | One, `favicon.svg` | Six sizes and a small manifest |
| Security headers file | None | `_headers` with five lines |
| Page for a missing address | Built (`dist/404.html`), and `site/wrangler.jsonc` tells the host to serve it. I read that line and changed nothing | The same |
| Licence files | None | `LICENSE`, `LICENSE-DATA` |
| README | Out of date (item 10) | Written for a public reader |
| A place for corrections | The rule is on the About page, with "There have been none since the site was first published". An entry's page has a part "Changes to This Entry, dated, and kept", shown on the one entry that has a change. `CHANGELOG.md` is in the repository and no page links it; its opening says "Nothing is published, so there have been no public corrections" | A changelog linked from the method account |

Only the first row and the licence and README rows are in the must-fix list. A missing sitemap
or share card does not make the site wrong, and John put sharing text and pictures among the
things that can wait. Guideline 7 has a place on the site for a correction to an entry. It has
none yet for a correction to the home page, the About page or Still Asking; linking the
changelog from the footer would give it one.

## 8. The project's checks

Run on 2026-11-19 on commit `2486969`.

- `python3 -I scripts/test_compute.py`: 29 tests, all pass.
- `python3 -I scripts/compute.py --check`: "13 records read: 8 on the list, 5 beside it, 0 left
  out with facts still to verify." "The headline file matches the records." The count is 5.
- The site build: 18 pages.
- `python3 -I scripts/check_site.py`: "The built site passes: 18 pages, 78 outside addresses
  linked."

The build rewrote one line of `site/src/data/window.json` (the commit it was built from). I
left that change out of this commit.

## What I did not do

- I did not read any paper from end to end myself. The helpers searched the full texts for the
  passages each sentence rests on and read the text round them.
- Sentences about the project's own searches cannot be checked against a source.
- I did not test the pages with a screen reader, in the light theme, or in a second browser.
- I did not read `.github/workflows/deploy.yml`, which another session may be checking, beyond
  seeing which checks it runs.
- I ran no search for a public page for the people named without a link beyond one or two
  likely addresses each.

## Where the detail is

The five helpers' findings, with the source's own words for every item above, and the table of
all 78 addresses, are in the shared notes folder of this group of sessions, under
`full-check-2026-11-19/` (`group-a.md` to `group-e.md`, `linkcheck.txt`). They are outside the
repository.
