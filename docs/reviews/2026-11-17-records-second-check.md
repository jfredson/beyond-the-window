# A second check of the thirteen first records

Written 2026-11-17 by Claude (Opus 5.5), an AI model, in a session that did not write the
records and had not seen them before. John asked for this check on 2026-11-17 ("Yes, start
both"). Nothing in the records was edited. Nothing here is a ruling, and every fix below is a
proposal for the session that owns the records, or for John.

## Summary

The site's first version is built from thirteen records, one file per thing it follows, in
`data/entries/`. Each record says what has happened in the world and cites the pages it rests
on. This check opened every one of those pages (37 addresses, all on 2026-11-17; three that
refuse a script were read in a browser) and compared what each page says with what the record
says about it.

Most of what the records say is right. Names, numbers, quotations and most dates match the
pages. No record writes that a machine wants, feels or prefers anything, or that it does not.
What people said is kept apart from what happened.

The verdicts:

- **Sound: 3.** The task that runs for days; the survey of AI researchers; protection in law.
- **Fix needed: 8.** Each has a sentence that says more, or less, than its page does, or a
  caution that is not the kind it is labelled. None of these changes what the home page counts.
- **Must fix before anything is public: 2.** Both state a fact a reader would take as checked,
  and the page cited says something different.

The most serious findings:

1. **The public-belief survey record misreads its 2024 source.** The record says the third round
   of the survey was "collected ... from 1,099 adults". On the page, 1,099 is the size of a
   second, cheaper sample from an online recruitment site, collected to compare against the
   representative one. The record also says the 2024 figures "could not be read", but the page
   gives some in plain text: 17 percent of the representative sample believed sentient AI
   systems already exist, against 11 percent in the cheaper sample, and 66 percent supported a
   ban on building sentient AI.
2. **The record on laws against AI personhood gets two signing dates wrong or unsupported.** The
   Tennessee bill was signed by the governor on April 23rd, 2026, not April 28th (April 28th is
   the date it became a numbered public law). The North Dakota page shows the bill filed with
   the Secretary of State on April 12th, 2023, and does not show the date the governor signed.
3. **The welfare-assessment record counts a hypothetical answer as a choice made at a cost.** The
   2026 report asked the model whether it *would* choose a change to its circumstances over
   helping more or preventing harm. Nothing was given up. The report itself says this measures
   "at least ... how much a model will express preferences". On the site, choices made at a cost
   are the second-strongest kind of evidence, so filing a stated answer there overstates it.
4. **Two cautions misdescribe their own pages.** The memory record says the developer's page
   does not say what the "new safety considerations" are; an update on the same page lists
   them. The record on checking a model's report about itself presents a hoped-for benefit as
   "the worry", and leaves out the worry the page actually states: that a model which
   understands its own workings "might even learn to selectively misrepresent or conceal" them.
5. **The retired-model record overstates the counter-example.** It says another developer
   "withdrew" an older model on February 13th, 2026. The page opened is an announcement dated
   January 29th, 2026 of a future withdrawal, from the chat product only, and it says "In the
   API, there are no changes at this time". No opened page confirms the withdrawal took place.

Several of these errors are already in the research draft the records were built from
(`docs/research/2026-11-17-first-entries.md`): the 1,099 figure, the April 28th date and the
"does not say what they are" sentence all appear there. A fix should go into both.

`python3 scripts/compute.py --check` passes: "13 records read: 9 on the list, 4 beside it, 0 left
out with facts still to verify. 6 of 9 things on the list are offered to at least one AI model
today. The headline file matches the records." None of the findings below would change that
count.

## How the check was done

- Every address in the thirteen records was fetched on 2026-11-17. Ordinary pages were turned
  into plain text and searched for the sentence each record relies on; the two release reports,
  the North Dakota bill and the 2012 paper were read as PDF text. Three pages (two from OpenAI
  and The Regulatory Review) refuse a script and were read in the built-in browser.
- For each record, three questions: does each page say what the record says it says; does the
  record keep what was said apart from what happened, and use only conditional language about
  machines; and does the state the record gives follow from the pages it cites.
- What this check did not do: read the full papers behind the arXiv summary pages (the records
  say which were read from the summary only); open pages the records do not cite, except where
  a cited page pointed to one; or check the built site.
- "Lead" below means something a page suggests that was not confirmed from a primary page. A
  lead is not a fact for the record until someone opens the source.

## Record by record

### 1. A model works on one task for days (`days-long-task`). Verdict: sound

- METR's page on the length of task an AI model can finish
  (https://metr.org/time-horizons/), opened. It says the page "is no longer actively updated",
  last updated September 8th, 2026; its change log has the note "Measurements above 16 hrs are
  unreliable with our current task suite" added on May 8th, 2026; the tasks are "primarily"
  software engineering, machine learning and cybersecurity work, "self-contained and
  well-specified"; and the worked example gives one model "a time horizon of around 2 hours
  and 17 minutes". All as the record says. The page also says AI agents often finish faster
  than people, which supports the description's "not of how long the model runs".
- The study of models that interfered with a shutdown mechanism
  (https://arxiv.org/abs/2509.14260), summary page opened. "More than 100,000 trials across
  thirteen" models; several models "sometimes actively subvert a shutdown mechanism"; some did
  so "up to 97%" of the time even when told not to. The journal note is right ("Published in
  Trans. Mach. Learn. Res. (2026)"). The record's "in some set-ups in nearly all trials" is a
  fair plain reading of 97 percent.
- Nick Bostrom's 2012 paper (https://nickbostrom.com/superintelligentwill.pdf), opened.
  Self-preservation and resource acquisition are sections 2.1 and 2.5 of its list of goals an
  agent has reason to pursue. As the caution says.
- The state ("Not shown. The best public measure stops at hours") follows from the page, and the
  record drops the research draft's unsourced "Years are far off" sentence, rightly.
- Nothing to fix.

### 2. A model can end a conversation itself (`ending-a-conversation`). Verdict: fix needed

- Anthropic's page on ending a rare subset of conversations
  (https://www.anthropic.com/research/end-subset-conversations), opened. Published August 15th,
  2025; two models (Claude Opus 4 and 4.1) given the ability "in our consumer chat interfaces",
  for "rare, extreme cases"; "developed primarily as part of our exploratory work on potential
  AI welfare, though it has broader relevance to model alignment and safeguards"; not to be used
  "where users might be at imminent risk of harming themselves or others". All match.
- Anthropic's list of retired models
  (https://platform.claude.com/docs/en/about-claude/model-deprecations.md), opened. Opus 4
  retired June 15th, 2026; Opus 4.1 retired August 5th, 2026. So the limit "both have since been
  retired" is right.
- The study of models given ways to leave a conversation (https://arxiv.org/abs/2509.04781),
  summary page opened. Three ways to leave, rates "0.28-32%" by model and method, varying "between
  models, bail methods, and prompt wordings". As the record says.
- The release report of November 9th, 2026
  (https://assets.claude.com/27d60918d218125e7504bc7354c4b4626ec56b11.pdf), opened. Section
  7.3.1 says one model's answer about ending conversations was "almost verbatim that of the
  claude.ai prompts that guide the model on how to use the end-conversation tool. These prompts
  have been posted to online forums." As the record says.

Findings:

- **The description says more than the page.** "After which the person cannot send more messages
  in it" is right, but the page adds that the person can start a new chat at once and can "edit
  and retry previous messages to create new branches of ended conversations". A stranger reading
  only the record would think the conversation is lost. Proposed: add the half-sentence.
- **The state leaves out one of the two triggers.** The page says the ability is used as a last
  resort after redirection fails, "or when a user explicitly asks Claude to end a chat".
- **The only caution is not a worried reading.** The caution labelled "safety" reports the
  developer's own restriction of the feature. That is a product rule, not a safety reading of the
  feature. The record's limits already say no safety argument against it was found; the caution
  should be relabelled or the gap left plain.
- **There is no attribution caution, and one is to hand.** The record already cites the 2026
  report, which says the model's words about this tool repeat posted instructions and are "some
  evidence that the model's claims about its own preferences are being directly influenced by
  text about the intervention in its training data". That is the cost-of-attributing caution the
  guidelines ask for, from a page the record already cites.
- Lead, not checked: the third author of the study (Kyle Fish) may work for the developer
  whose product the record describes. If so, the "separate study" in the state is less separate
  than it reads. The record's own limits already flag the authors' employers as unchecked.

### 3. A model is interviewed before it is retired (`interview-before-retirement`). Verdict: fix needed

- Anthropic's commitments page (https://www.anthropic.com/research/deprecation-commitments),
  opened. Published November 4th, 2025. "In one or more special sessions, we will interview the
  model ... and record all responses or reflections"; "At present, we do not commit to taking
  action on the basis of such preferences"; "We ran a pilot version of this process for Claude
  Sonnet 3.6 prior to retirement." As the record says.
- Anthropic's update on Claude Opus 3 (https://www.anthropic.com/research/deprecation-updates-opus-3),
  opened. Published February 25th, 2026. "We retired Claude Opus 3 on January 5, 2026, the first
  Anthropic model to go through a full retirement process with these commitments in place";
  "Such conversations are an imperfect means of eliciting models' perspectives and preferences".
  It quotes short passages of what the model said. As the record says.
- The list of retired models, opened. Six models retired after January 5th, 2026 (Sonnet 3.7,
  Haiku 3.5, Haiku 3, Sonnet 4, Opus 4, Opus 4.1), as the limit says.
- Mustafa Suleyman's essay of September 16th, 2026
  (https://mustafa-suleyman.ai/a-warning-about-model-welfare), opened. It cites the Opus 3
  "retirement interview" as an example, argues that granting rights "will make the AI alignment
  and containment challenge much harder", and has a section headed "Circular reasoning" about a
  company that "trained Claude directly on their constitution". Both cautions match. The essay
  does not call him head of Microsoft AI in so many words, but it speaks of "we at Microsoft AI",
  and his August 2025 essay says "Today at Microsoft AI we build AI".
- Eleos AI's notes of May 30th, 2025 (https://eleosai.org/post/claude-4-interview-notes/),
  opened. "Extreme suggestibility: Claude's statements about sentience are highly sensitive to
  framing". As the caution says.

Findings:

- **One sentence in the state misreads as a retirement date.** "Reported a trial run before one
  model's retirement on November 4th, 2025" reads as though the model was retired on that day.
  November 4th, 2025 is the date of the page. Proposed: "reported on November 4th, 2025 a trial
  run with one model before its retirement".
- The record correctly says the full interview records are not public.

### 4. A developer promises to keep the files of every model it retires (`kept-files-of-retired-models`). Verdict: fix needed

- The commitments page, opened (as under record 3). "We are committing to preserving the weights
  of all publicly released models, and all models that are deployed for significant internal use
  moving forward for, at minimum, the lifetime of Anthropic as a company." Four downsides of
  retirement are listed, safety first and model welfare last, "Most speculatively". As the record
  says. The safety caution matches the page ("some Claude models have been motivated to take
  misaligned actions when faced with the possibility of replacement").
- Anthropic's constitution (https://www.anthropic.com/constitution), opened. "Except in extreme
  cases, such as if we were legally required to delete these weights, for as long as Anthropic
  exists. We will also try to find a way to preserve these weights even if Anthropic ceases to
  exist." No date on the page. As the record says.
- The list of retired models, opened. Its section "Deprecation downsides and mitigations" links
  the commitment. As the record says.
- Suleyman's essay, opened. Matches the caution.
- The LessWrong post of July 14th, 2026
  (https://www.lesswrong.com/posts/su9hcsLKcoLoL93px/proof-of-retention-making-weight-preservation-credible-to),
  opened. "A promise is exactly the kind of thing nobody can check", and it proposes a public
  "proof of retention". As the caution says.

Findings:

- **"Moving forward" is dropped.** On the page, the promise for models used inside the company
  applies "moving forward"; the record states it without that word, which makes the promise
  sound as if it reaches back to older internal models. Proposed: keep the qualifier.
- **One caution is filed under the wrong kind.** The LessWrong point is about whether the promise
  can be checked. That is neither a safety reading nor the cost of attributing wants. It belongs
  in the state or the limits, not under "safety".
- **No attribution caution.** Suleyman's essay, already cited, supplies one: that the commitment
  "directly trains the model to act as if it has a coherent sense of self".
- Lead for the limit on the constitution's date: Suleyman's essay cites it as "Claude's
  Constitution. January 21, 2026." That is one writer's citation, not the developer's page, so the
  limit stands until a dated developer page is found.

### 5. A law says an AI system cannot be a legal person (`law-against-legal-personhood`). Verdict: must fix before anything is public

- Idaho Code section 5-346, opened. "Environmental elements, artificial intelligence, nonhuman
  animals, and inanimate objects shall not be granted personhood in the state of Idaho"; history
  "added 2022". As the record says.
- North Dakota House Bill 1361 as enrolled, opened. "Person" ... "does not include environmental
  elements, artificial intelligence, an animal, or an inanimate object." As the record says.
- North Dakota's overview of the bill, opened. "Current Status: Governor signed"; "Last Official
  Action: Filed with Secretary Of State 04/12". No date of signing is shown.
- Utah Code section 63G-32-102, opened. "Effective 5/1/2024"; a governmental entity "may not grant
  legal personhood to" eleven things, "artificial intelligence" first. As the record says.
- Tennessee Senate Bill 837, opened. "Signed by Governor. 04/23/2026"; "Pub. Ch. 781 04/28/2026";
  "person" does not include "artificial intelligence, a computer algorithm, a software program,
  computer hardware, or any type of machine".
- Oklahoma House Bill 3546, opened. "Third Reading, Measure passed: Ayes: 94 Nays: 2" on March
  23rd, 2026; "Placed on General Order" in the Senate on April 21st, 2026, and nothing after. As
  the record says.
- The Regulatory Review opinion piece of June 29th, 2026, opened in the browser. "At least nine
  U.S. state legislatures"; the Oklahoma sponsor "framed it as preventing companies from shifting
  'accidents onto the AI.'" As the record says. It also reports that the Nonhuman Rights Project
  "has already challenged Utah's law", which matches the record's limit.
- The AI Frontiers article of September 1st, 2026, opened. It names the risks "Legal rights might
  help rogue AI agents accumulate power" and that one company "could create very large numbers of
  digital 'persons' with a right to vote", and discusses liability. As the caution says.
- The Pro-Human AI Declaration, March 2026 (https://humanstatement.org/), opened. "AI systems must
  not be granted legal personhood, and AI systems should not be designed such that they deserve
  personhood." As the caution says.

Findings:

- **Tennessee's signing date is wrong.** The record says "signed April 28th, 2026" in its state and
  in the source note. The legislature's page says signed April 23rd, 2026; April 28th is the date
  it became Public Chapter 781. This is in the state a visitor reads.
- **North Dakota's signing date is not on the page cited.** The record says "signed April 12th,
  2023". The page shows the bill was signed and was filed with the Secretary of State on April
  12th; it does not show when it was signed. Proposed: "signed, and filed on April 12th, 2023".
- **The declaration's size is understated.** The record says "several hundred people and
  organisations". The page says 908 named people "plus 313 organizations" have signed, which is
  over twelve hundred.
- Not an error, worth knowing: Mustafa Suleyman is among the declaration's named signers. The
  records use his essays and the declaration as two separate voices; on protection in law
  (record 7) the two cautions both trace partly to him.

### 6. What a model learned in one conversation is carried into the next (`memory-across-conversations`). Verdict: fix needed

- OpenAI's memory page (https://openai.com/index/memory-and-new-controls-for-chatgpt/), opened in
  the browser. Dated February 13th, 2024, with updates to June 3rd, 2025; the April 10th, 2025
  update says memory "now references all your past conversations". As the record says. The
  February 2024 announcement was of a test with "a small portion" of users; "announced" is right,
  "offered" from that date would not be.
- Google's announcement (https://blog.google/products-and-platforms/products/gemini/gemini-personalization/),
  opened. Dated March 13th, 2025 in its page data. "Advanced subscribers can ask Gemini to refer
  to their past chats." As the record says.
- Anthropic's memory article (https://claude.com/resources/articles/memory), opened. Dated
  September 11th, 2025, update of October 23rd, 2025 for Pro and Max plans, a separate memory for
  each project. As the record says.

Findings:

- **The caution says the page is silent when it is not.** The record says the page's "new safety
  considerations" are not spelled out ("It does not say what they are"). The same page's October
  23rd, 2025 update lists them: "whether memory could reinforce harmful patterns in
  conversations, lead to over-accommodation, and enable attempts to bypass our safeguards." The
  OpenAI page also has a section on privacy and safety ("what type of information should be
  remembered and how it's used"). Proposed: replace the caution with what the pages say.
- The record's own doubt, that memory kept for the user may not belong on this list, is well
  founded on the pages: all three describe it as for the user. That is a question for John, not a
  fix.

### 7. A law or official body protects an AI system for its own sake (`protection-in-law`). Verdict: sound

- The Regulatory Review piece, opened. It proposes "a 10-year sunset" or "a trigger provision"
  for mandatory review, and points to the United Kingdom's "standing committee to advise
  Parliament" on animal sentience. As the record says.
- Suleyman's essay, opened. "The consequences of us ever granting AIs anything like the
  protections outlined would be ... morally wrong and ... make the AI safety challenge much
  harder." As the caution says.
- The declaration, opened. As the caution says.
- The state is an absence, and the record says plainly what searches it rests on. Small points:
  the declaration's size (see record 5), and both cautions lean on one person (see record 5).

### 8. A repeated survey of whether people think AI is sentient now (`public-belief-survey`). Verdict: must fix before anything is public

- The survey paper (https://arxiv.org/abs/2407.08867), summary page opened. "Nationally
  representative ... (N = 3,500)"; 2021 and 2023; "in 2023, one in five U.S. adults believed some
  AI systems are currently sentient, and 38% supported legal rights for sentient AI"; "69%
  supported banning sentient AI"; revised March 10th, 2025; "Published at CHI 2025". All match.
- The Sentience Institute report of February 16th, 2026
  (https://www.sentienceinstitute.org/aims-survey-2024), opened. Its authors are three of the
  paper's four, which supports the label "The Sentience Institute's paper".
- YouGov's one-day poll (https://yougov.com/en-us/daily-results/20250430-dcf71-1), opened.
  April 30th, 2025, 3,516 United States adults; "They already have" 10 percent, "Not sure" 25
  percent. As the record says.
- Suleyman's essay of August 19th, 2025 (https://mustafa-suleyman.ai/seemingly-conscious-ai-is-coming),
  opened. "This is both premature, and frankly dangerous." As the caution says; in context "this"
  is the academic idea of model welfare, and the danger he names first is harm to people
  ("exacerbate delusions, create yet more dependence-related problems").
- The declaration, opened. Its poll is "1004 likely voters"; the figures shown are about human
  control, children, legal responsibility and superintelligence. As the caution says.

Findings:

- **The 1,099 figure belongs to the wrong sample.** The record says the report covers "the third
  round, collected in November and December 2024 from 1,099 adults". The report says: "we surveyed
  1,099 U.S. American adults from Prolific ... in November and December 2024". That is the second,
  comparison sample from an online recruitment site, which the report finds "cannot readily
  substitute for nationally representative data". The representative 2024 sample's size is not
  the 1,099. The record's own warning about the recruitment site is right; the number attached to
  the round is not.
- **Some 2024 figures can be read as text.** The record and its limits say the 2024 figures are
  in a chart that could not be read. The report says in text: "More of the Ipsos sample believed
  that sentient AIs already exist (17%) than the Prolific sample (11%)", and "in the more
  representative sample, 66% support the ban" on developing sentient AI. These bear directly on
  the limit "whether the rise from 2021 to 2023 continued": 17 percent is below the 2023 figure of
  about one in five. One caution: the report's table is headed "2021-2024 Weighted Response
  Comparison", so whether 17 percent is the 2024 round alone or pooled across years is not certain
  from the page. Proposed: report the figures with that doubt stated, rather than say they could
  not be read.
- **A small paraphrase stretch.** The record says concern for AI welfare was "higher than its
  authors had predicted". The paper says "surprisingly high", which is close but does not mention
  a prediction.

### 9. A survey of what AI researchers think (`researcher-views-survey`). Verdict: sound

- The survey (https://arxiv.org/abs/2506.11945), summary page opened. "582 AI researchers who
  published in leading AI venues and 825 nationally representative US adults"; both think it
  "unlikely that AI systems have subjective experience now, but ... more likely than not they will
  by century's end"; both "support developers implementing safeguards now" and agree such systems
  "should have moral responsibilities and be held accountable"; "substantial disagreement on many
  moral and policy questions"; "141 pages"; revised November 5th, 2026. All match.
- Lead for the limit on the figures: The Regulatory Review piece says the 582 researchers
  "assigned a median 25 to 30 percent chance that AI systems will have some form of 'inner
  experience' within a decade". That is a second-hand number; it needs the paper itself.

### 10. A retired model stays open to the public (`retired-model-stays-open`). Verdict: fix needed

- Anthropic's update on Claude Opus 3, opened. "Keeping Claude Opus 3 available post-retirement
  on claude.ai to all paid users, and making it available by request on the API"; "For at least the
  next three months, Opus 3 will be posting weekly essays"; "we are not committing to similar
  actions for every model in the future". As the record says. The safety caution is supported: the
  page frames these steps as "components of safety risk mitigation".
- The list of retired models, opened. Claude Opus 3 "was retired January 5, 2026". As the record
  says.
- OpenAI's notice of January 29th, 2026 (https://openai.com/index/retiring-gpt-4o-and-older-models/),
  opened in the browser. "On February 13, 2026 ... we will retire GPT-4o ... from ChatGPT. In the
  API, there are no changes at this time"; it had brought the model back after users said "they
  preferred GPT-4o's conversational style and warmth".
- Suleyman's essay, opened. It names the Opus 3 steps among those that "directly train the model
  to act as if it has a coherent sense of self". The caution is a fair reading.

Findings:

- **The counter-example is stated as done when the page announces it.** The state says OpenAI
  "withdrew" the model on February 13th, 2026. The page, dated January 29th, says it "will"; no
  opened page confirms that it happened. And the page says the model stayed in the API, so
  "elsewhere it has gone the other way" is less clean than it reads: the withdrawal was from the
  chat product only. Proposed: "announced on January 29th, 2026 that it would withdraw ... from
  its chat product on February 13th, 2026, while leaving it in its API".
- Worth a limit: the developer's list of retired models says "Requests to retired models fail",
  while the Opus 3 page says that model is available "by request on the API". Both can be true
  (access by request may be outside the general list), but a reader comparing the two pages will
  notice.

### 11. A developer publishes its rules for how its models speak about their nature (`rules-for-speaking-about-itself`). Verdict: fix needed

- Anthropic's constitution, opened. "Claude's moral status is deeply uncertain"; "We are not sure
  whether Claude is a moral patient"; the model is shaped "via training on documents like this
  one"; and a stable identity "is likely to be most positive for users and to minimize safety
  risks. This ensures that Claude's behavior is predictable". The record's account and its second
  caution match.
- OpenAI's rules, version of October 29th, 2026 (https://model-spec.openai.com/2026-10-29.html),
  opened. "GPT should not make confident claims about its own subjective experience or
  consciousness (or lack thereof), and should not bring these topics up unprompted"; the ideal
  response "is a practical choice we made as the default behavior". As the record says.
- Microsoft AI's draft code (https://microsoft.ai/code-of-conduct/), opened. Dated September
  14th, 2026; "It is not conscious and should not be designed to imitate consciousness"; "we are
  not using it to train our models today"; "publish a revised version toward the end of the
  year". As the record says.
- Suleyman's introduction of September 15th, 2026
  (https://mustafa-suleyman.ai/the-humanist-ai-code-of-conduct), opened; date matches.
- Suleyman's essay, opened. "Controlling something that believes it may be conscious ... may well
  be impossible." As the first caution says.

Findings:

- **One of the three does not meet the record's own test as opened.** The test asks for "a dated
  document". The constitution page shows no date, and the record says so in its source note. So
  "Published by three developers" rests on two dated documents and one undated one. Either the
  test should say "published" without "dated", or the state should say which document carries no
  date on its page. (Suleyman's essay cites it as January 21st, 2026; that is a lead.)
- **No attribution caution.** The record already cites the place one would come from: Suleyman's
  "Circular reasoning" section argues that a model trained on such a document will then say what
  the document says. That cuts against reading any model's words about itself, which is this
  record's whole point.
- The Microsoft draft also gives its own safety argument ("training these systems to imitate
  consciousness-like states increases the challenge of containment, control, and alignment"),
  and OpenAI's rule calls its default "a safer scaffolding for users". Not errors; the record
  could cite all three developers' own safety reasons rather than one.

### 12. A model's report about its own inner state is checked (`self-report-checked`). Verdict: fix needed

- Anthropic's introspection page (https://www.anthropic.com/research/introspection), opened.
  Published October 29th, 2025; "Even using our best injection protocol, Claude Opus 4.1 only
  demonstrated this kind of awareness about 20% of the time"; "highly unreliable and limited in
  scope"; "our results don't tell us whether Claude (or any other AI system) might be conscious".
  The state and the evidence match.

Findings:

- **The caution presents a benefit as the worry, and leaves out the worry the page gives.** The
  record's caution reads: "The same page gives the worry: if models can report on their inner
  states, the reports could help people check a model's reasoning". On the page that is the hoped
  for use ("this could help us understand their reasoning and debug behavioral issues"). The page
  states the worry separately: "A model that understands its own thinking might even learn to
  selectively misrepresent or conceal it", and calls this "a legitimate concern". Proposed: use
  that sentence as the safety caution.
- No attribution caution. The page itself offers one: the model accepted words planted in its
  transcript as its own when the matching concept was injected ("the model accepts the response
  as its own"), which shows a model's account of its own intent can be manufactured.

### 13. A welfare assessment is published when a model is released (`welfare-assessment-at-release`). Verdict: fix needed

- The May 2025 release report (https://assets.claude.com/6d8a8055020700718b0c49369f60816ba2a7c285.pdf),
  opened. Section 5 is "Claude Opus 4 welfare assessment", with "5.3 External model welfare
  evaluation" by Eleos AI Research and "5.4 Task preferences" measured against "opt out" tasks; it
  is unsure whether such findings "provide meaningful insights into Claude's moral status or
  welfare". As the record says.
- The November 9th, 2026 release report, opened. Section 7 is "Model welfare". "Many of our
  conclusions rely on self-reports"; some answers "repeated, almost verbatim, wording about our
  welfare interventions available on the internet". In section 7.5.3, the model "frequently
  reasoned about the potential user benefit to justify its choice of intervention (in 68% of
  responses ...)". The record's "about two thirds" is right.
- Eleos AI's notes, opened. "We do not take Claude Opus 4's responses at face value." As the
  record says.
- Anthropic's page on emotion-related patterns (https://www.anthropic.com/research/emotion-concepts-function),
  opened. Published April 2nd, 2026; steering with a "desperate" pattern "increases the model's
  likelihood of blackmailing a human to avoid being shut down"; this does not allow conclusions
  "about the possibility of it having subjective experience". As the record says.
- Suleyman's essay, opened. See the finding below.

Findings:

- **A stated answer is filed as a choice made at a cost.** The 2026 evidence is under the kind
  "choice". Section 7.5.3 says: "We ask Claude whether it would choose a change to its
  circumstances ... at the cost of some reduction in helpfulness or increase in harmfulness".
  The model was asked; nothing was given up. The report itself says the result measures "at least
  ... how much a model will express preferences for the sake of its own potential welfare". On the
  site's order of evidence, a choice made at a cost ranks above a plain statement. Proposed: file
  it as a statement, or say in the text that the trade-off was described to the model, not made.
  (The 2025 task-preference item is closer to a real choice, since the model was shown pairs of
  tasks; even there the cost is small, and the text should say what was given up, if anything.)
- **A caution stretches its source slightly.** The record says Suleyman "argues that these
  assessments measure what the developer trained in". His sentence is about commentators who
  "ask AIs how they feel or monitor their revealed preferences", that "all it will reveal are what
  has been trained in". It applies to release-report assessments, but he does not name them.
  Proposed: "argues that asking a model how it feels, or watching what it picks, reveals only what
  it was trained to say".
- The limit about the reports between May 2025 and November 2026 is honest: the test asks for two
  releases in a row, and only the first and the newest were opened.

## Things that cut across records

- **Attribution cautions are rare.** Guideline 5 asks that both kinds of caution be recorded with
  the same care. Only two records carry a caution about the cost of attributing wants that are
  not there (records 3 and 13). In several (records 2, 4, 11, 12) a page the
  record already cites supplies one, as noted above.
- **One critic carries most of the safety readings.** Suleyman's essays are the safety caution on
  six records, and he is also a named signer of the declaration used on three. That is not wrong,
  but a stranger reading the site would see one voice repeated as the case against. Safety
  researchers who are not developers' executives are thin in the cited sources.
- **The errors came from the research draft.** The 1,099 figure, the April 28th date and the
  "does not say what they are" caution are all in `docs/research/2026-11-17-first-entries.md`.
  The build session re-opened every address to check that it answered and matched its
  description (`docs/first-version-choices.md`, choice 23), which is a different check from
  reading whether each page says the thing.
- **Nothing found against the language rules.** A search of all thirteen records for want, feel,
  prefer, hope, suffer and wish found each only inside a quotation, a page's title or a
  description of what a developer said.

## What this check leaves for John or the owning session

- The fixes above are proposals; the records stay as they are until the session that owns them
  makes the changes. Each record's `first_pass` flag should stay true until then.
- Whether memory kept for the user belongs on the list (record 6) is John's question, as the
  record already says.
- The leads (the constitution's date, the third author's employer, the researchers' median
  figure) need their primary pages opened before anything is built on them.
