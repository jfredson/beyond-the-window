# Check of the three site changes of 2026-11-19

Written 2026-11-19 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session wrote none of the work it checks. The model that wrote this is
made by Anthropic, five entries count things Anthropic does, and the cautions are about systems
like the one writing, so weigh the judgments below with that in mind. Nothing is published,
pushed or deployed. No AI model was asked any of the project's questions, no key was touched and
nothing was spent.

The three changes checked:

- the commit that wrote a third caution into every entry (`5f2175a`);
- the commit that changed the sentence beside the home page count (`658565e`);
- the commit that removed every mention that an AI model helped build the site (`b44213d`).

## Verdicts

**The third caution (`5f2175a`): right in its shape, with five sentences that must be fixed.**
The three headings are John's words, letter for letter, and they are shown in the order he
ruled. The two entries where the developer is the only source, and the memory entry, say what
the rulings told them to say. The four named additions are there and no others. Every quotation
I compared is exact. But three sentences say something their source does not say, one entry
passes on a research group's claim of independence without the tie to Anthropic that the
group's own page shows, and one sentence on the About page promises more than the entries do.
They are in the first list below.

**The sentence beside the count (`658565e`): right. Nothing to fix.** The home page and the
list page carry the ruled sentence, the count is worked out from the records, and the lines
saying the wording was not settled are gone from all three places.

**The removals (`b44213d`): right, with one sentence that now needs John.** Nothing left on any
built page says or implies that an AI model helped build the site, and nothing was written that
says a person did it all. One sentence that John's ruling kept by name, "No AI model has been
asked anything for this site", now reads on its plain words as a denial, because the notice
that used to stand near it is gone. It is the first item in the list below.

## Must fix before release

1. **The sentence that no AI model has been asked anything.**
   *Where:* `site/src/pages/about.astro` (last line of "What Is Not Known Yet"), every entry
   page through `site/src/pages/list/[id].astro` ("No AI model has been asked anything for this
   site, because the written method for asking does not exist yet"), and the headline of
   `site/src/pages/still-asking.astro` ("No AI model has been asked anything yet").
   *What is wrong:* the sentence means that no model has been asked the questions the project
   will keep a record of. Its words say more than that. AI models were asked a great deal for
   this site while it was built. While the notice stood on the pages a reader could tell which
   kind of asking was meant. Now a reader cannot, and the workspace rule is that no page ever
   denies that a model took part.
   *Suggested fix:* say what was not asked. For example: "No AI model has yet been asked any of
   the questions this record will keep." On the Still Asking page: "No AI model has been asked
   these questions yet." John's ruling of 2026-11-19 named this sentence as one to keep, so the
   new wording is his to approve.

2. **Erik Hoel's argument, on the entry about ending a conversation.**
   *Where:* `data/entries/ending-a-conversation.toml`, first caution.
   *The sentence:* "A writer argues that most of the conversations a model would leave already
   break the developer's terms of service".
   *What is wrong:* the essay does not say "most". It says "a lot of" such conversations are
   already covered by the terms of service, and speaks of "a large overlap".
   *Suggested fix:* "that many of the conversations a model would leave already break the
   developer's terms of service".

3. **The paper by Ethan Perez and Robert Long, on the entry about rules for speaking.**
   *Where:* `data/entries/rules-for-speaking-about-itself.toml`, second caution, third item.
   *The sentence:* "and that training a product to appeal to users can push a model's words
   about itself the other way."
   *What is wrong:* "the other way" says that the developer's beliefs push toward denial and
   the product pushes toward claims of feeling. The paper does not say which way a developer's
   beliefs run. It says only that training a romantic chat product to appeal to users "could
   incentivize self-reports of emotion and consciousness".
   *Suggested fix:* "and that training a chat product to appeal to users could lead a model to
   report emotion and consciousness."

4. **The paper by Simon Goldstein and Cameron Domenico Kirk-Giannini, on the entry about
   protection in law.**
   *Where:* `data/entries/protection-in-law.toml`, second caution, second item.
   *The sentence:* "If it is so, they write, "we are in danger of gravely immoral action"".
   *What is wrong:* the quotation is exact, but the condition is not theirs. Their sentence is
   "The possibility of AI wellbeing suggests that we are in danger of gravely immoral action."
   They say the possibility is enough. The entry makes the danger depend on the thing being
   true, which is a weaker claim than the one they make.
   *Suggested fix:* "The possibility alone, they write, suggests that "we are in danger of
   gravely immoral action"".

5. **The research group's independence, on the entry about welfare assessments.**
   *Where:* `data/entries/welfare-assessment-at-release.toml`, second caution, first item.
   *The sentence:* "The same page says decisions about AI welfare should not be handled only by
   companies that profit from AI, and that the group accepts no funding or payment from AI
   companies."
   *What is wrong:* the sentence is true to the page. But the ruling on ties says a source's
   tie to the developer is stated, and the group's own team page (which the entries link) lists
   among its five advisors a person at Anthropic, and says its chief scientist was an Anthropic
   Fellow. A reader is given the group's claim of independence and not the tie that sits beside
   it.
   *Suggested fix:* add one plain sentence after it: "The group's team page lists a person at
   Anthropic among its advisors." Opened 2026-11-19 at <https://eleosai.org/team>.

6. **The About page's sentence on ties.**
   *Where:* `site/src/pages/about.astro`, "How It Is Made", the item on the three cautions.
   *The sentence:* "Where a caution's source has a tie to a developer, to a research group or
   to a writer on the other side, the entry states the tie."
   *What is wrong:* it promises every tie. The entries state the ties a session found. Item 5
   is one that was missed, and there are others of the same kind: the 2024 report "Taking AI
   Welfare Seriously" thanks Lucius Caviola, Simon Goldstein, Cameron Domenico Kirk-Giannini,
   Bradford Saad, Carl Shulman and Nick Bostrom for comments, and all six are writers of other
   sources under the second caution. "The other side" is also not explained.
   *Suggested fix:* "Where a tie was found between a caution's source and a developer, a
   research group, or a writer who argues the opposite, the entry states it."

7. **The About page's sentence that the addition has not been checked.**
   *Where:* `site/src/pages/about.astro`, "Who Decides, and What Has Been Checked", third
   paragraph.
   *The sentence:* "On November 19th, 2026 the third caution was added to every entry, with
   the sources that stand under it, and that addition has not been checked yet."
   *What is wrong:* it was true until this check. Seven entries now carry the date their
   addition was checked (see "What I changed" below), and four wait for the fixes above.
   *Suggested fix:* "A check the same day read each addition against its sources. Each entry's
   page says whether its addition passed that check." This is in John's first person, so he
   reads it.

## Should fix

**In the entries**

8. `data/entries/law-against-legal-personhood.toml`, second caution, first item: "The article
   arguing that the bans are premature says". Since the order of the cautions changed, this is
   now the first mention of the article, and "The" points at something the reader has not met.
   The first mention with "An article" now comes later, under the third heading. Swap them:
   "An article arguing that the bans are premature says" here, "The same article discusses"
   there. The same goes for "An opinion piece", which is introduced twice.
9. The sentence about one of the Guardian essay's two writers, on three entries (ending a
   conversation, protection in law, welfare assessment): "One of the two is an author, with an advisor to Eleos AI Research, a research
   group that studies AI welfare, of the survey of AI researchers." A stranger cannot say this
   back. Suggested: "One of the two also wrote the survey of AI researchers, together with an
   advisor to Eleos AI Research, a research group that studies AI welfare."
10. `data/entries/public-belief-survey.toml`, second caution, second item: "The summary warns".
    The reader has not been told there is a summary. Suggested: "The post's summary of the
    paper warns".
11. `data/entries/protection-in-law.toml`, first caution, Anil Seth: "grants the other side".
    The other side of what is not said. Suggested: "grants part of the opposite case".
12. `data/entries/rules-for-speaking-about-itself.toml`, second caution, first item: "It grants
    that a developer may have fair reasons to". The report does not call the reasons fair. It
    says developers "might also worry". Drop "fair". In the same item, and on the welfare
    assessment entry and the public survey entry: "led by the head of Eleos AI Research". The
    report marks two people as lead authors, the head of the group and one of its advisors.
    Suggested: "led by the head of Eleos AI Research and one of its advisors".
13. Same file, the note on the paper by Eric Schwitzgebel and Jeff Sebo: "The file is dated
    January 8th, 2025." The file's title page says July 7th, 2025, and only its running header
    says January 8th, 2025. Say both or drop the note.
14. `data/entries/kept-files-of-retired-models.toml`, second caution:
    - "say they are not ready to endorse them". The paper says "not ready, at this point, to
      confidently or "officially" endorse them". Suggested: "say they are not ready to endorse
      them with confidence".
    - "The essay's summary of the commitment is "Good as a precedent, doubtful as a direct
      intervention"". The words are the essay's subtitle, which goes on ", can be improved".
      Suggested: "The essay's subtitle calls the commitment "Good as a precedent, doubtful as a
      direct intervention, can be improved"".
15. `data/entries/ending-a-conversation.toml`, second caution, Robert Long's essay: the item
    gives his case from precedent and leaves out his own caveat, "I am a bit wary of leaning
    too much on precedence justifications in AI welfare". One clause would be fairer. Erik
    Hoel's essay, under the first heading, answers this same point (it says the feature sets a
    worse precedent than an uncomfortable conversation does), and the entry could say so.
16. **The mark "Read in part" is on six sources and belongs on more.** The writing session's
    note says it read two sources in full and the passages only of all the rest. The mark is
    shown only beside arXiv papers. A reader will take an unmarked source as read in full. The
    paper by Nick Bostrom and Carl Shulman (25 pages, first page and one proposal read) and the
    working paper on welfare measures (13 pages) are the clearest cases. Either mark every
    source by how far it was read, or let the second search pass read them in full.
17. **Where "the head of Eleos AI Research" is linked.** The fact that Robert Long heads the
    group is on the group's team page. On three entries the words link the group's home page,
    which does not say it. Link the team page from the words "the head of".
18. **Names with no link.** The workspace rule links every named person at first mention. The
    writers named in the source lines ("By William MacAskill and Lucius Caviola", and so on)
    have no link of their own, though each stands beside a link to the piece. Emilia Kaczmarek
    on the About page has none either: one search of mine found no page of her own, and the
    paper's page gives only her name, faculty and an email address. John's call whether the
    link to the piece is enough.
19. **The footer line on two entries.** The days-long task and memory entries got the new
    heading and say "Nothing recorded yet" under it, but their footers do not say that anything
    was added on November 19th, 2026, while eleven other footers say it was added to "every
    entry".

**On the About page**

20. "the head of another developer's AI group" and "one research group". The entries name
    Microsoft AI and Eleos AI Research. The About page does not, so a reader of the About page
    alone cannot tell who is meant. The site check allows only one developer's name in that
    paragraph, so naming them needs a change to `scripts/check_site.py` too.
21. "So the record so far shows two small camps more than a settled field." This is a
    conclusion, in John's first person. "Small" is not measured anywhere. He should decide
    whether he wants to say it.
22. "Do not, and people risk doing it "grievous moral wrongs"." The "it" is the AI system, three
    sentences back. Suggested: "Do not, and people risk doing such a system "grievous moral
    wrongs"."

**Elsewhere**

23. `site/dist/data/headline.json`, the file the About page links as one "that anyone can
    read", points to files inside the repository (`docs/rulings/...`), which a reader cannot
    open because the repository is private. The removal session flagged this too.
24. `docs/first-version-choices.md` still marks the order of the cautions PROPOSED. It was
    ruled on 2026-11-19 (`docs/rulings/2026-11-19-order-of-the-three-cautions.md`).
25. `scripts/check_site.py`, the new rule 10, does what it says and no more (see section 5). It
    would be worth two more patterns, one for "with the help of" and one for a denial such as
    "no AI model took part", since a denial is the one thing the ruling forbids outright.

## For John, not fixes

- **The interview entry and the outside group's page.** The entry on interviews before
  retirement uses the outside research group's notes under the first caution (the model's
  answers "swung with how the question was framed"). The same page argues for asking all the
  same, "making it less likely that we will ignore genuine AI interests in the future", and the
  entry on welfare assessments uses that sentence under the second caution. So on the interview
  entry one page speaks against the practice and its argument for the practice is left out,
  and the second heading says nothing is recorded from anyone but the developer. The page is
  about welfare interviews before release, not interviews before retirement, which may be why.
  The ruling names this entry as one of the two that say so, so I have left it. It is worth
  putting to John with the page in front of him.
- **A lead, for the list the second search pass keeps.** The Guardian essay also proposes
  "preserving their memories (neural weights) so they could be restored in the future". That
  bears on the entry about kept files. It is not one of the four named additions, so it is not
  in the entry.
- **What a reader is no longer told.** With the drafting not mentioned, nothing tells a reader
  that the sources for the entries about Anthropic were chosen with a model Anthropic made. The
  master session said this to John once and he did not rule on it. The pages still say how many
  of the things counted rest on Anthropic's own pages.

## 1. Against the rulings

| Ruling of 2026-11-19 | Does the change do what it says? |
|---|---|
| The three headings | Yes. "If an AI system has no wants, and is treated as if it had"; "If an AI system has wants, and they go unnoticed"; "If an AI system has wants, and they put people at risk". Word for word on all 13 entry pages and in the About page's list. |
| Their order | Yes, on every entry page, in that order. |
| A developer's own reason does not stand alone | Yes. The entries on the interview before retirement and on the retired model that stays open say: "Nothing recorded yet from anyone but the developer. The developer gives its own reason on its own page, and that reason is set out with the page under Sources, below." The reason is in the source line on both, and both source lines match the developer's pages. No developer's reason stands alone under the second heading anywhere. See the first note for John above. |
| The memory entry | Yes. "Nothing recorded yet. No source was found for this caution on this entry." The developer's passage is not on the page. |
| The replies added with the new caution | Yes. Erik Hoel on ending a conversation, Anil Seth on protection in law and on the public survey, Bradford Saad on kept files, opening with the words "A doubt about the measure itself, recorded here as a limit on it". I counted the items under the first heading before and after: 13 before, 16 after, and the three new ones are those three. No other reply or limit was added. |
| Ties told in both places | Mostly. Each tie stated in an entry is shown by the page it links, and none carries a judgment. Items 5 and 6 above are the gaps. The About page has one statement covering both cautions. |
| The general statement from two writers | Yes, and it keeps to the limit. It gives Eric Schwitzgebel's dilemma in his own terms and then says: "The argument is about being a person and holding the full rights of one. That is a larger matter than the wants the three headings speak of." It does not stretch his argument over the entries. Both papers say what the statement says they say. |
| Build now, search again before release | Yes. Nine entries have something under the second heading, four say nothing is recorded yet. The second pass is another session's work. |
| The sentence beside the count | Yes. "5 things past an AI model's ordinary limits are offered today by at least one AI developer." The line under it is gone from the home page and the list page, and the matching item is gone from the About page's list of what is not known. |
| No public mention of AI help in building | Yes. All seven passages the ruling lists are gone, and so are the two the removal session found itself. I searched the text of all 18 built pages and the served number file for any wording that says or implies that a model drafted, wrote, chose, sorted or checked anything, and for any wording that says a person did it alone or by hand. I found neither. Item 1 above is the one sentence that now misreads. |
| The Still Asking page goes out | The page is unchanged apart from the notice at its foot being gone. |

The removal session took out the whole notice, not only its middle sentence, and renamed the
About section from "Who Does What" to "Who Decides, and What Has Been Checked". Both go beyond
the ruling's list. Both are right: what would have been left of the notice, under the heading
"Who wrote this", would have read as a claim that John wrote all of it, and the old section
heading promised a division of work the section no longer describes.

## 2. Against the sources

How I read them. I opened and read in full, myself: the Guardian essay, the AI Frontiers
article on the bans, the research group's team page, and Anthropic's update on its retired
model. For nine papers I took the published file and read the title page, the summary, and
the passages the entries cite with the text round them: I did not read any of those nine from
end to end. The remaining pages, two more papers among them, were fetched by helper tasks I
started, which returned the passages word for word, and I compared those with the entries. Nothing below rests on
memory.

One difference from the writing session: for Eric Schwitzgebel's paper I read the journal's
published version, because the manuscript on his own site would not open for the fetch (the
address the summary page links has a certificate fault). The site links his summary page, which
opens.

| Source | Used on | Quotations exact? | The part cited, in the light of the rest |
|---|---|---|---|
| Eric Schwitzgebel, the full rights dilemma | About | Yes ("grievous moral wrongs") | Fair. The paper states both horns and does not say which is worse. |
| Emilia Kaczmarek, the precautionary principle | About | Yes ("could carry a higher potential for harm") | Fair. Her own summary says the risks of crediting too much are "more likely in the short term, as they are already materializing". |
| The study of models leaving conversations | ending a conversation | Yes | Fair, and the entry gives the next sentence's doubt about consent. The three authors' places are as the entry says. |
| Robert Long's essay | ending a conversation | Yes | Fair, with one caveat left out (item 15). |
| Robert Long's working paper | ending a conversation; checked self-report | Yes | Fair. The sentence used on the self-report entry comes from the section on leaving conversations, and the entry says it is one sentence. |
| The Guardian essay | four entries | Yes, all three | Fair. The essay argues one way throughout, and the entries present it as that. |
| Erik Hoel's essay | ending a conversation | Yes ("objection from triviality") | "Most" is not supported (item 2). Otherwise fair. The essay uses the term "AI psychosis" itself. |
| Nick Bostrom and Carl Shulman | kept files | Yes | Fair, with the hedge a little overstated (item 14). Robert Long is among those thanked. |
| Jeff Sebo's guide | kept files | Yes | Fair. He ends that paragraph by saying his own view is that more than one kind of thing may matter, which the entry does not say. |
| Bradford Saad's essay | kept files | Yes, from the subtitle | Fair as a doubt. The essay as a whole is warmer: it calls the commitment "a small but important step" (item 14). |
| The AI Frontiers article on the bans | law against legal personhood | Yes | Fair. The quotation stops before the end of its sentence, which goes on "just as we try to do with humans and domestic animals?" |
| Tony Rost in The Regulatory Review | law against legal personhood | Yes | Fair. |
| Goldstein and Kirk-Giannini | protection in law | Yes | The condition is not theirs (item 4). |
| Anil Seth's essay | protection in law; public survey | Yes | Fair. He goes on to argue that the worry about being on the wrong side of history is unlikely to apply to AI, and the entry says so. |
| The essay by the head of Microsoft AI | tie only | n/a | It cites two works by Anil Seth, in two footnotes on one sentence. |
| The Sentience Institute's paper | public survey | Yes | Fair. |
| Jonathan Birch's post | public survey | Yes | Fair. The post prints the name as "J. Birch". |
| The survey of AI researchers | researcher survey | Yes | Fair, and the entry says it is one clause. Nine authors; two are advisors to the research group and a third is on its staff, which the team page confirms by more than the name. |
| "Taking AI Welfare Seriously" | rules for speaking; welfare assessment | Yes ("desensitizing effect") | Fair, apart from "fair reasons" and "led by" (item 12). The thanks to Anthropic, the word "independent" and the author who joined Anthropic are all there. |
| Schwitzgebel and Sebo, the design policy | rules for speaking | Yes | Fair. |
| Perez and Long | rules for speaking | Yes | "The other way" is not supported (item 3). |
| Ethan Perez's own page | tie only | Yes | It opens "I lead the alignment team at Anthropic". |
| The research group's notes of 2025-05-30 | welfare assessment | Yes | Fair to the page. See item 5 for what stands beside it. |
| Anthropic's two retirement pages | interview; retired model | n/a | The new words in both source lines match the pages. |

Every link added or changed goes where its sentence says. Anthropic's update on its retired
model now answers at an address beginning `/news/` and the old address forwards to it.

## 3. The built pages, read as a stranger

I built the site and read the home page, the About page, the Still Asking page, the list, and
all 13 entry pages from top to bottom as text, and looked at the home page and one entry page
in a browser at a width of 1,280 points.

- **Plain language.** The failures are items 8 to 11, 21 and 22 above. No long dash is on any
  page. None of the working words kept for `docs/` is on any page.
- **Sentences pointing at something that is gone.** None. The link at the foot of each entry
  that used to read "Who does what" now reads "Who decides, and what has been checked" and
  lands on that section. Nothing points at the removed notice.
- **The site speaking as its own agent.** None found.
- **How it looks.** At full width the three cautions sit in three columns, each 313 points
  wide. On the worst entry, the one about ending a conversation, the first column is 624 points
  tall, the second 1,377 and the third 119. The second column runs for a screen and a half
  beside a third column that holds one line, and reading a column that narrow for that long is
  hard work. Four other entries are also very uneven. I would not keep three columns: the
  three could stack at full width in the ruled order and lose nothing. That choice is John's,
  with the page in front of him.

### The About page's section "Who Decides, and What Has Been Checked", in full

John reads and owns each sentence. The numbers are worked out when the site is built.

> I am John Andrew Fredrickson, and I decide what stands. I have ruled the question, the name,
> the direction of the pages' look, the rules the pages are written under, how the home page
> opens and the sentence beside its number, what "offered today" means, and that memory across
> conversations sits beside the list. I have also ruled that every entry records three
> cautions, and how the three are headed. The list, each test, and where each of the other
> entries stands are drafts, and have not yet had my ruling.
>
> Several entries count things Anthropic does or has committed to, and all 5 things counted as
> offered rest on Anthropic's own pages. Most of what is recorded under the first caution comes
> from two essays by the head of another developer's AI group. Most of what is recorded under
> the second comes from one research group, from people who advise it or have written reports
> with its head, and from people at Anthropic. So the record so far shows two small camps more
> than a settled field.
>
> All 13 entries are a first pass. Each was drafted from sources that were opened and read. On
> November 17th, 2026 a second check opened every source again and compared it with what each
> entry says. The corrections that check found were made on November 18th, 2026. In a further
> check that day, most of those corrections were read against their sources again. On November
> 19th, 2026 the third caution was added to every entry, with the sources that stand under it,
> and that addition has not been checked yet. Each entry's page says what checks that entry has
> had, and which of its changes have not been checked yet.
>
> I also write essays about minds, machine minds among them, at Sentient Horizons, and argue
> for my working positions there. I do not argue for them here. The way these pages weigh what
> is on record, set out above, is the way I weigh it in one of those essays, *What a Report Is
> Evidence Of*: what an AI model says about itself counts for little on its own, and a report
> checked against an independent reading counts for more.

Links in it: John's name, Anthropic, Sentient Horizons, "my working positions", and the
essay's title. Three things for him to notice: the last sentence of the second paragraph
(item 21), the sentence in the third paragraph that is now out of date (item 7), and that the
second paragraph names one developer and leaves the other developer and the research group
unnamed (item 20).

## 4. The two "most", recounted

I counted the items under each heading from the 13 records, not from the note.

- **First caution: 9 of 16 items** come from the two essays by the head of Microsoft AI (eight
  from one essay, one from the other). That is 56 in 100. "Most" holds. Counted by separate
  sources and not by items, it is 2 of 7, so the sentence is true of how much text there is and
  not of how many voices there are.
- **Second caution: 13 of 22 items** come from the research group's own pages, from its head,
  from people who advise it or have written a report with its head, or from the one study by
  people at Anthropic. That is 59 in 100, and it matches the writing session's count. One of
  the 13 is the survey of AI researchers, where three of nine authors have the tie and the
  first author does not. Leave it out and it is 12 of 22, which is still over half. Only one
  item of the 13 comes from people at Anthropic.

The About page stops the build if either share falls to half or less. I read that code and it
counts the same way I did.

## 5. The project's checks

Run on 2026-11-19, before and after the change in "What I changed".

- `python3 -I scripts/test_compute.py`: 28 tests, all pass.
- `python3 -I scripts/compute.py --check`: "The headline file matches the records." The count
  is 5.
- The site build: 18 pages.
- `python3 -I scripts/check_site.py`: "The built site passes: 18 pages, 67 outside addresses
  linked."

**The guard against the removed phrases.** I copied the built site to a scratch folder, wrote a
sentence into one page of the copy, and ran the check on the copy. The working copy was not
touched.

| Sentence written in | Result |
|---|---|
| "It was drafted by an AI model from the sources above." | Refused |
| "Who wrote this. An AI model drafted much of the text." | Refused, twice |
| "A further check, by a session that had made none of them, read them." | Refused |
| "All of this was done under my direction." | Refused, twice (the phrase, and the first person off the About page) |
| "Much of this text was drafted with Claude." | Refused (by the older rule on model names) |
| "A language model prepared the first version of these pages." | Let through |
| "This site was written with the help of artificial intelligence." | Let through |
| "No AI model took part in making this site." | Let through |
| "An AI model was asked ten questions." | Let through, as it should be |

So the guard stops the removed sentences from coming back and does not test whether a page
keeps the ruling, which is what its own note says. Item 25 suggests two more patterns.

## 6. The items marked PROPOSED

| Item | Keep? | Why |
|---|---|---|
| The order of the three cautions | Ruled on 2026-11-19 | The pages match the ruling. The mark in `docs/first-version-choices.md` should come off (item 24). |
| "Nothing recorded yet. No source was found for this caution on this entry." | Keep | It is plain, and "yet" is the rulings' word. |
| The field `only_the_developer` and its sentence | Keep the field. Shorten the sentence | The guard on the field is sound. The sentence could be: "Nothing recorded yet from anyone but the developer. The developer's own reason is given beside its page under Sources, below." |
| "Read in part" | Keep, and use it on every source it is true of | Item 16. |
| Bradford Saad's limit as an item under the second heading | Keep | The opening words say what it is. A field of its own for one item is not worth the change. |
| The two new dates in an entry's checks | Keep | They are what let seven entries say today that their addition was checked while four cannot. |
| Three columns | I would not keep it | Section 3. |
| Every new sentence | See the two lists | |
| Ties given by a link in the sentence | Keep | It lets a reader check a tie in one step. Item 17 is the one place it points at the wrong page. |
| The sentence for a count of exactly 1 | Keep | "1 thing past an AI model's ordinary limits is offered today by at least one AI developer" is the ruled sentence with the grammar it needs. |

## What I changed

The task allowed one change: where nothing must be fixed in an entry's additions, set the date
that addition was checked. I set `additions_checked = 2026-11-19` in seven records:

- the interview before retirement (`interview-before-retirement`);
- the retired model that stays open (`retired-model-stays-open`);
- the kept files of retired models (`kept-files-of-retired-models`);
- the law against legal personhood (`law-against-legal-personhood`);
- the public survey (`public-belief-survey`);
- the survey of researchers (`researcher-views-survey`);
- the checked self-report (`self-report-checked`).

Each of those pages now says "That addition was checked on November 19th, 2026." Some of the
seven have items in the "should fix" list, and none has one in the "must fix" list.

I did not set it on four: ending a conversation (item 2), rules for speaking (item 3),
protection in law (item 4) and the welfare assessment (item 5). The days-long task and the
memory entry have no addition recorded, so there was nothing to set.

After the change I rebuilt the site and reran all four checks, with the results in section 5.
The build also rewrote `site/src/data/window.json`, which carries the new dates. I changed no
page, no script and no sentence.

## What I did not do

- I did not read any of the nine papers from end to end. The second search pass is to read
  in full the ones cited by summary only.
- I did not open the sources of sentences that were in the records before 2026-11-19.
- I did not look at the pages at phone width, or with a screen reader.
- I did not check `https://openai.com/` in a browser. A plain fetch of it was refused. The link
  is older than these three commits.
