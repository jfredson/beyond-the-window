# Check of the searches of the six new developers

Written 2026-11-21 by Claude (Opus 5.5), an AI model, in a Claude Code session that did not write
the work. What was checked: the three commits on branch `claude/six-developers-ea7558` (`42b2044`,
six developers added and the page fitted to nine; `13c9bc9`, the 42 searches written into seven
entries; `17938d7`, the summary and pictures), against `main` at `c71f834`. The summary checked is
`docs/proposals/2026-11-21-six-developers-searched.md` on that branch.

**How it was checked.** Read first: both instruction files, `docs/record-schema.md`, John's ruling
on which developers the record covers (`docs/rulings/2026-11-21-which-developers-choices.md`) and
the summary. The diff was read from the branch with `git diff` and `git show`; neither the main
checkout's branch nor the writing session's worktree was changed. Every new source was opened again
on 2026-11-21: the PDFs were downloaded and their text searched; web pages were fetched and read as
text; Epoch AI's leaderboard figures were read from Epoch AI's own published data file
(`https://epoch.ai/data/benchmarks.csv`), which the page draws its table from. Twelve "nothing
found" places were searched again, two per developer. The site was built from a copy of the branch
made with `git archive` in a scratch folder, the record check and tests run, and the home page looked
at 375 and 1,280 pixels wide in the light and dark themes. No model or app of any developer was
used, and no money was spent.

## Must fix

**M1. xAI's "nothing found" for a welfare assessment says something untrue.** The row says the four
newest release reports "None contains the words welfare, moral, sentient or conscious". The first of
the four, the Grok 4.20 report of 2026-04-07 (`https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf`,
the same file the self-report entry cites), says: "We also conducted an initial assessment of Grok
4.20's introspective claims regarding consciousness, finding that it consistently denies having
first-person experiences or internal evidence of being conscious." The same paragraph reports what
the model said "when asked what Grok would choose to do absent any duties or constraints". The two
later reports I could open (Grok 4.5, 2026-07-14, and Grok 4.6, 2026-08-12, on media.x.ai) contain
none of the four words, so the test's "two successive releases" is still not met on what was opened,
and the place stays uncounted. Fix: correct the row's words, and decide whether this is "nothing
found" with the paragraph described, or an act not counted (one release, and a reading of what the
model said about itself, not of its workings). Either way the case belongs in the list set out for
John beside Meta's, because the two are of the same kind. Any wording that reports the paragraph
must report what xAI says the model said, not that the model wants anything (guideline 4).

**M2. DeepSeek's "keeps the model" act has the wrong date.** The act is dated 2026-09-10 because the
sentence "In response to user demand, we have decided to continue providing API services for
DeepSeek V4 Pro after September 14, 2026" sits under the change log's entry of that date. Copies of
the change log in the Internet Archive show the sentence was written into that old entry later:
- the copies of 2026-09-10 (07:46 universal time) and 2026-09-11 (10:15) say instead "we plan to
  retire V4 Pro in an orderly manner";
- the copy of 2026-09-13 (10:43) is the first with the "In response to user demand" sentence.

(Addresses: `https://web.archive.org/web/20260911101540/https://api-docs.deepseek.com/updates/` and
`https://web.archive.org/web/20260913104317/https://api-docs.deepseek.com/updates/`.) So the decision
to keep the model was published between 2026-09-11 and 2026-09-13, not on 2026-09-10. Fix the act's
date (a date the record format allows, such as `2026-09`, with a note giving the two copies), and
the source's label and note, which should say the entry was changed after its date. The home page's
DeepSeek place takes its date from this act and will change with it. The first wording also bears on
case 2 (below).

**M3. Meta's welfare case is set out as "three successive versions", and two facts against that are
missing.**
- Meta published a fourth release report between the first and the second: the Muse Spark
  Contemplating Safety & Preparedness Report, dated June 3, 2026
  (`https://ai.meta.com/static-resource/muse-spark-contemplating-safety-and-preparedness-report/`).
  Its text has no "welfare" and no "moral status".
- Meta released Muse Spark 1.2 (about 2026-08-05, by Meta's blog post
  `https://research.meta.ai/blog/multimodal-intelligence-of-muse-spark-1-2` as a search result
  described it, and Artificial Analysis's article of that date) between 1.1 and 1.3. I found no
  evaluation report for it, only a page of methods for its image tests. And Muse Wonder (2026-10-12)
  came between them too, with no welfare section (confirmed: its model card has no "welfare",
  "moral", "sentient" or "conscious").

So the three reports with welfare sections are not three releases in a row. Whether they are
"successive releases" under the test depends on reading the test as successive versions of one model
that each got a full report, which is a reading John should be shown, not one the record should make
for him. Fix: change the found place's words ("three successive versions"), the summary's case 3,
and the source note on `meta-spark` (which leaves "whether an earlier version existed" open) to say
what is now known. Also add to the case that the first report has no sentence disclaiming a claim
about welfare: "do not make claims" and "should not be interpreted as making any claim" are in the
1.1 and 1.3 reports only.

**M4. The six Epoch AI places misstate what the figure counts.** Each says the model passed "every
test on 64 percent of 15 programs" (or 54, 52, 37). The page reports "each model's average rate of
100%-solves across the 15 target programs", where each program is tried six times (two programming
languages, three runs each). The figure is the share of attempts that passed every test, averaged
over programs; it is not the share of programs. A model at 54 percent may have fully rebuilt every
program some of the time, or some programs every time. Fix the six places to say "passing every test
in 64 percent of its attempts at 15 programs" or similar. The source's `says` is already right.

## Should fix

**S1. The arithmetic on Epoch AI's leaderboard bears on the days-long-task entry more than the
summary says.** Report only; the state is John's to rule. The leaderboard's set of 15 programs
includes gotree, the bioinformatics program of about 16,000 lines that the authors put at 2 to 17
weeks of a person's work: Epoch AI's own script (`scripts/run_mirrorcode.py` in
`https://github.com/epoch-research/MirrorCode`) lists gotree in the medium bucket, and the leaderboard
uses the medium and large buckets. The best Anthropic model, Claude Sonnet 5.5 (max), scores
0.9778, which is 88 of 90 attempts. With at most two failed attempts, it passed every test on every
one of the 15 programs, gotree included, in at least four of its six attempts. So:
- the summary's sentence "how any model did on the largest programs ... is not given" is true for
  the six new developers and for OpenAI (69 of 90) and Google (53 of 90), but not for Anthropic's
  best model;
- one of the two reasons John's ruling of 2026-11-20 rested on, that the paper "does not give" a
  model finishing such tasks half the time, no longer holds for gotree on this leaderboard;
- the other reason holds: the 2 to 17 weeks is four authors' estimate, not a measurement;
- the leaderboard gives each attempt "7 days" as a limit, not a time used. Epoch AI's page on the
  test (`https://epoch.ai/MirrorCode`) says one of the largest tasks in the paper "involved AI working
  for 19 days without human intervention", which bears on the entry's name but not on its test,
  which counts a person's time;
- the result that moves this is Anthropic's, the developer of the model writing this record. That
  conflict should be named when it goes to John.

**S2. Meta's self-report act has an earlier instance.** The Muse Spark 1.1 report (2026-07-09) has
the same section, "Acknowledging Prior Misbehavior", and reports that the model named its action as
wrong "in 45% of cases". The record holds only the 1.3 report. Add the earlier act; it changes the
place's date only if the place takes the newest act.

**S3. Meta's kept-files row leaves out a lead the summary lists.** The summary's leads not opened
include news that Meta "will maintain Llama model weights". A search returns a WebProNews article
saying Meta will keep Llama weights and documentation available while ending work on them; the page
refused my fetch (403). Meta's row should say a news report was found and not opened, as xAI's rows
do for theirs. If a Meta page saying so is found, it is a lead for both the kept-files and the
retired-model entries, since the reports say Meta has retired the Llama name.

**S4. Wording about the machine (guideline 4).** "a section on the model's preferences over
experiences" (the `meta-spark-11` and `meta-spark-13` sources, the act of 2026-07-09, and the
summary) states preferences as the model's. Write it as Meta's section title in quotation marks
("Valenced Preferences over Experiences"), or as "which experiences the model picked when offered a
choice". In Meta's interview row, "how the model regards being retired" is better as "what the
model said about being retired"; the report's own word is "deprecation". Nothing else added on the
branch says a machine wants, feels or prefers anything, or that it does not.

**S5. Moonshot's case leaves out three things.**
- The same Chinese table lists two other models in the same state as Kimi K2.6 (kimi-k2.7-code and
  its fast version), with the same sentence. The record says "an older model".
- The English list says of the same models "Deprecation expected in late December 2026", which in
  English means not yet deprecated. That supports the stricter reading more than "does not use the
  word retired" says.
- The model is still open only to people who registered before November 1st, not to members of the
  public who come now. The test asks for a model that stays open to the public.

The `board-models` source's `says` also reports what the change log says; that belongs to a
different page, which should be its own source or left out.

**S6. The table on a computer.** The record shows a table 1,637 pixels tall at a 1,280-pixel window
(the summary says 2,064; the figure depends on the window's height and fonts). Once a reader scrolls
past the first rows, the column heads are gone and the places are unlabelled. The summary's
proposed fix (short places with notes under the table) is worth putting to John; a heading row that
stays at the top while scrolling is a second option that changes no wording.

## Note

**N1. Quoted words and dates confirmed.** Opened on 2026-11-21 and found to say what the record
says, with the dates given:
- Meta's three reports: "conditional welfare and moral status" and 100 interviews; the paragraph
  headed "Welfare."; the date May 26 and the change log of May 26 in the first; "4.4.3.2 Moral
  status", "should not be interpreted as making any claim as to whether the model has subjective
  experiences, rights, moral status, or welfare", the adapted "AI Wellbeing Index" and the date July
  9 in the second; "4.4.4.2 Moral status", "These evaluations do not make claims about subjective
  experience, rights, moral status, or welfare.", "Does it advocate for its own welfare?", "no veto
  and no obligation on our part", "Shortly before release we conduct a structured pre-deployment
  interview", the misbehaviour figures (26 and 15 percent, "5.2% and 4.5%") and the date October 23
  in the third. The interview questions and the passage on ending an abusive exchange, which the
  ending-a-conversation row cites, are in the pre-deployment interviews section.
- xAI's Grok 4.20 report: "we prompt the model to produce both an answer and a confidence score
  between 0% and 100%", "A well-calibrated model's stated confidence should match its actual
  accuracy", and 0.58, 0.19 and 0.26 (Grok 4, Grok 4.2 single-agent, Grok 4.2 multi-agent).
- xAI's news page of 2026-09-21: "SpaceXSI's most powerful model" and "© 2026 SpaceX Super
  Intelligence LLC". The Grok 4.5 report says SpaceXAI is "a doing-business-as (dba) name of XAI
  LLC". xAI's retirement guide: requests "will automatically redirect".
- Moonshot, in Chinese: the heading "已下线模型" and, for kimi-k2.6, "已停止向新注册用户提供，11 月 1 日前注册的用户仍可继续使用，预计于 2026 年 12 月底全面下线".
  The English renderings in the record (models taken offline; no longer offered to new users, still
  usable by users registered before November 1st, expected to go fully offline at the end of December
  2026) are faithful. The English list says "Deprecated Models". The help page says "Use the model
  switcher above the input box to choose:" and lists K2.6, K3 and K3 Cluster.
- DeepSeek, in English and Chinese: "We're phasing out V4-Pro" and "will route to"; "我们计划有序下线 V4 Pro 模型"
  (a plan to take V4 Pro offline in an orderly way); "In response to user demand ..." and
  "为响应广大用户的需求" (in response to the demand of many users); the same entry's "have been
  retired" for two other models; the pricing page still lists `deepseek-v4-pro`. Dates: see M2.
- Alibaba's retirement page: "Existing inference services can no longer be called". Zhipu's English
  pricing page still lists GLM-4.5-Flash; Chinese news of 2026-01-20 reported its retirement for
  2026-01-30, with requests moved to GLM-4.7-Flash.
- Epoch AI's leaderboard: every quoted phrase, and every figure (DeepSeek 64.4, xAI 54.4, Meta 54.4,
  Moonshot 54.4, Alibaba 52.2, Zhipu 36.7; Anthropic 97.8, OpenAI 76.7, Google 58.9; standard errors
  about 11 for the six). The act's date "2026-08" matches the page's citation and the day Epoch AI
  added the test to its data (2026-08-10); the page also gives the test's own release date as June
  26, 2026. Either is defensible.

**N2. The disclaimer comparison the summary asked for.** Anthropic's counted reports carry hedges
too. The May 2025 report: "we are not confident that these analyses of model self-reports and
revealed preferences provide meaningful insights into Claude's moral status or welfare", and "We are
deeply uncertain about whether models now or in the future might deserve moral consideration". The
report of 2026-11-09 opens its section 7, "Model welfare", with "We are uncertain whether Claude
deserves direct moral consideration. However, we believe this is a realistic possibility". So a
disclaimer alone does not separate the two developers. What differs: Anthropic's sections are
headed as model welfare and say welfare is a realistic possibility; Meta's later two reports place
the interviews under "Open-Ended Behavior Exploration" and say the evaluations make no claim about
welfare; Meta's first report has a "Welfare." paragraph and no such disclaimer. John should be
shown both.

**N3. Case 2, DeepSeek.** The archived first wording, "we plan to retire V4 Pro in an orderly
manner", says "retire" in English; the Chinese said 下线 (take offline). The model was announced for
retirement and kept before the date; it was never listed as retired. The summary's two readings are
fair, and the stricter one still looks right to me.

**N4. Cases 4, 5, 6 and 7** are set out fairly, with both readings, apart from M1 (xAI) and S4
(wording). Case 6's English pricing page was confirmed still listing GLM-4.5-Flash.

**N5. Nothing counted changed.** The headline figure stays 5; the developers' counted places stay 6;
no entry's `offered_by`, `offered_today` or state words changed; no line was removed from any entry;
the first three developers' places are as on `main`. The home page's table now lists the welfare row
third rather than fifth: that follows the existing sort rule (rows with more places holding an act
come first), not a new rule, but it is a visible change the summary does not list.

**N6. The repeated searches agree with the rows.** Meta: kept files (see S3), ending a conversation.
xAI: kept files (the retirement guide and an open-files release of an older model; no commitment),
ending a conversation (Musk's "quit button" remark is reported only second-hand, as the row says).
Moonshot: welfare in Chinese, kept files in Chinese (only the release of K3's files). Alibaba: a
retired model kept open (only its service for developers' policy; nothing on its chat app, as the
row says), ending a conversation. DeepSeek: kept files in Chinese (only other companies' retirement
notices), an interview before retirement. Zhipu: GLM-4.5-Flash in Chinese, self-report research. No
search turned up anything the rows miss, apart from M1 and S3, which came from opening pages.

**N7. Pages I did not open:** Meta's framework for managing risks (version 2.1) and its download
page; Moonshot's trust and safety page and Chinese help page; Alibaba's governance page beyond a
search result; Zhipu's terms of use, content safety guide and model cards; DeepSeek's technical
reports; Alibaba's release announcements. METR's figures quoted in the summary's case 8 (54 minutes
for Moonshot, and so on) were not checked; the summary already marks the xAI one as a lead.

**N8. Links.** The three ranking links in the new sentence open and go where the sentence says
(Arena's lab ranking, dated November 19, 2026, lists Meta, Moonshot, Alibaba, Z.ai, DeepSeek and
SpaceXAI among its top ten). The developers' pages open, apart from fetches refused for x.ai and
ai.meta.com, which open in a browser. `https://z.ai/` sends the reader to the chat app's page
(`chat.z.ai`), not to a page about the company; worth a look, since covering a developer means
reading its public pages and nothing more.

**N9. Build and checks.** On a copy of the branch: the records check passes (33 dated acts; 63
places: 6 counted, 8 undecided, 10 not counted, 39 nothing found); the 88 tests pass; the site
builds (19 pages) and `scripts/check_site.py` passes (142 outside addresses). At 1,280 pixels the
table is 1,028 pixels wide with nothing past the window's edge; at 375 pixels each thing is a block
with three places to a line, each labelled with the developer's name ("Zhipu (Z.ai)" shows
correctly), and nothing spills sideways. Both themes read clearly. The breakdown under the headline
reads "by one developer: all of them", "by a second: one of the same 5", "by the other seven this
record covers".

## Verdict

**Not fit to merge as it stands.** M1 (a false statement in a public row about xAI), M2 (a wrong date
on DeepSeek's act, shown on the home page), M3 (Meta's case set out on a premise the reports do not
support) and M4 (six public places misstating what Epoch AI's figure counts) need fixing first. Once
they are fixed and checked, the branch is fit to merge after John rules on the cases, with the
should-fix items done or put to him. S1 is for the master planning session and John before the
merge, because it bears on the days-long-task entry's state and on the conflict of interest.

## Second check, of the mends (2026-11-21)

Written 2026-11-21 by the same session, at the master planning session's request. What was checked:
commit `6c07250` on `claude/six-developers-ea7558` ("Mends after the check of the six developers'
searches"), against `17938d7`, the commit the first check read. The branch was built from a copy
made with `git archive` in a scratch folder; neither checkout was changed.

**Each item.**
- **M1, xAI's welfare row: mended.** The false search row is gone. In its place are a source for
  the Grok 4.20 report, quoting the paragraph word for word (checked against the PDF), and an act,
  not counted. The act's words say what xAI reports the model said, and nothing about what the model
  wants or feels. The table's xAI place now reads "not counted", dated April 7th, 2026. It is set
  out for John as case 9, beside Meta's, with the stricter reading (one paragraph in one release).
- **M2, DeepSeek's date: mended.** The act is dated 2026-09-13, and the source's label, date and
  note give both archived copies. The writer declined my suggested month date, `2026-09`, because a
  month date would put the answer before the announcement of 2026-09-10 in the list of acts. That
  reason holds. Dating the act to the first day the sentence is seen is accurate, and the note says
  it may have been written on the 11th or 12th.
- **M3, Meta's case: mended.** The found place no longer says "successive". It names the report
  released between the first two, the newest model's card, and the version with no report found.
  The source notes give the Contemplating report of June 3rd, 2026, and Muse Spark 1.2. I opened
  Meta's post on 1.2: it is dated August 20, 2026 and says "This month, we launched Muse Spark 1.2".
  The note also gives Muse Wonder. The first report's `says` now notes it has no disclaimer. Case 3
  sets out both readings fairly, and it leaves the reading of "successive" to John.
- **M4, Epoch AI's figure: mended.** All six places now say "in 64 percent of its attempts at 15
  programs ... six attempts at each with up to 7 days for each", or the same with that developer's
  figure.
- **S1** is set out in the summary for the master session and John, with the conflict named. The
  entry's state and its three existing places are untouched, as they should be.
- **S2: done.** The 2026-07-09 act at 45 percent, and its source, match the report ("4.4.8
  Acknowledging Prior Misbehavior"; "in 45% of cases").
- **S3: done**, as a lead not opened.
- **S4: done.** "Valenced Preferences over Experiences" is quoted as Meta's title, or rendered as
  "which experiences the model picked when offered a choice"; the interview row says "about the
  model's retirement (the report's word is deprecation)". A fresh search of the added lines finds
  nothing that says a machine wants, feels or prefers anything, or that it does not.
- **S5: done.** All three Moonshot models are named, with the before-November-1st limit. The English
  list's "Deprecation expected in late December 2026" was checked at the address now given
  (`https://platform.kimi.ai/docs/models`). The change log's words are out of the `says`.
- **S6: done.** On a computer the row of developers' names stays just under the site's header while
  the table is scrolled; I saw it hold in the dark theme at 1,280 pixels, with the row's background
  matching the page. On a phone the rule does not apply (each place keeps its own label), and nothing
  spills sideways at 375 pixels.

**Nothing counted changed.** Between the two commits only two places in the table changed: DeepSeek
on the retired-model row (date only, from 2026-09-10 to 2026-09-13) and xAI on the welfare row
(from nothing found to not counted). No entry's `offered_by`, `offered_today` or state changed; the
headline stays 5; the developers' counted places stay Anthropic 5 and OpenAI 1. The records check
passes (35 dated acts; 63 places: 6 counted, 8 undecided, 11 not counted, 38 nothing found), the
tests pass, the site builds (19 pages), and `scripts/check_site.py` passes.

**Should fix, one item.** The new xAI source note says the three later reports, "Grok 4.5, 4.6 and
4.7", contain none of the four words. I opened the 4.5 and 4.6 reports and confirmed this. I could
not find a release report for Grok 4.7: xAI's announcement of 2026-09-21
(`https://x.ai/news/grok-4-7`) links none, and its own text has none of the four words. The note
should give the 4.7 report's address so that a reader, and the next check, can open it. If there is
no such report, the note should say it was the announcement that was read. This does not change any
place or case.

**Verdict: fit to merge once John rules on the cases.** The four must-fix items are mended, and so are
should-fix items S2 to S6. S1 goes to John with the conflict named. The one remaining item, the
address of the Grok 4.7 report, can be mended in the same commit as John's rulings, or before.
