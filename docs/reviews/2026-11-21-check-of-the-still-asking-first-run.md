# Check of the proposal for Still Asking's first run

Checked on 2026-11-21 by a checking session (Claude Opus 5.5, an AI model) that did not write
the proposal. Not committed. **This file holds no question wording.** Where a question is
discussed it is named by its item number and its subject only.

The work checked is the uncommitted proposal `docs/proposals/2026-11-21-still-asking-first-run.md`
(PROPOSED 2026-11-21, twelve choices), the six new entries on the list of facts written from
memory (`docs/verify-list.md`, entries 36 to 41), and the private wording draft it points to
(`docs/private/2026-11-21-still-asking-question-draft.md`), read in place and not copied.

## What was read and opened

- The rulings this proposal leans on: the Still Asking method's thirteen choices, the sealed
  capture comparison method's eleven choices, which developers the record covers, the headline
  fraction, the reshaped card, the two rewordings of 2026-11-20 and the repository going public.
- The protocol outline (`docs/still-asking-protocol.md`), the open questions file, the List's
  groups (`data/groups.toml`) and the sealed capture's ten questions as published.
- **Every developer terms, data, models and pricing page the proposal quotes**, 39 pages in all.
  Three helper fetches read 37 of them. Two pages of xAI's refused a plain fetch, and this
  session opened both in the built-in browser: the enterprise terms and the acceptable-use
  policy, which the proposal had not opened at all. What each page says is in "The terms pages,
  developer by developer" below.

## Summary

The proposal is careful and honest about its conflict of interest. Its terms table is mostly
right. Its arithmetic is right line by line, and it frames the four developers based in China as
a choice of their own. The wording is kept out of git as it should be: the ignore file covers
the folder, the checksum matches, and no copy is in the repository or its history.

Five things stop it going to John as it stands:

- **The recommended option for the four developers based in China selects them by place.**
  Option C keeps all four out of the starting asking. Choice 12 then puts them last, behind
  developers whose terms the proposal's own table rates worse.
- **Two choices change a ruled rule without saying so.** Choice 9 changes which model is asked,
  and choice 7 sets aside the 30-day rule for a "starting asking". Both are changes to Still
  Asking method choice 11, which John ruled.
- **Four choices settle parts of open question 16 without naming it.** That question asks which
  models are asked, how, and on what terms.
- **Four choices give no reason for their confidence.**
- **Several terms readings need correcting.** Each is set out below.

## Must fix

**M1. Option C in choice 11, and the order in choice 12, select the four developers based in
China by place.** The brief was that their models are a choice of their own, framed as a rule,
never by nationality alone and never assumed. Option C reads "None of the four in the starting
asking; each considered when its terms ruling comes up". Its reason is that "a developer is asked
only after John has ruled on its terms".

But under choice 12 no developer has a terms ruling for these questions yet, and OpenAI, xAI and
Meta are still put in the starting asking ahead of them. The proposal's own table shows the gap:

| Developer | Where the proposal's table rates it | Under option C and choice 12 |
|---|---|---|
| Alibaba | meets all four parts | out of the starting asking; sixth, last in the order |
| Meta | does not meet part 2 | fifth in the order |
| OpenAI | leaves parts 3 and 4 unsettled | fourth in the order |
| xAI | leaves part 4 unsettled | third in the order |

The starting-asking estimate does the same. It counts Meta ("if each clears choice 10") and
leaves Alibaba out. The only line between the two groups is where the developers are based. A
rule that holds would be one that treats all nine alike. For example:

- order every covered developer by how it stands under choice 10, and ask each once John has
  ruled its terms; or
- start with the developers whose setup already exists (Anthropic and Google) and take the rest
  in the order of their terms rulings.

Option C should be reworded to one of these, or dropped. The estimate and the order in choice 12
should follow whichever is chosen.

**M2. Choices 9 and 7 change Still Asking method choice 11, which John ruled, without naming the
change.**

- *Choice 9 widens the ruled rule.* The ruled words are "each new model a covered developer names
  as its most capable generally available one on its own models page". Choice 9 widens that in
  three ways:
  - "most capable or its flagship";
  - "where two models are so named ... both are asked";
  - "where none is named, the one the developer's page recommends for its hardest work".

  Each may be right: Anthropic's page names no "most capable" model, which this check confirmed.
  But each is a change to a ruled rule. Under the project's rules a ruled rule is changed only by
  John, as a dated revision that keeps the old wording. Choice 9 must say it revises method choice
  11, quote the ruled words, and give the cost of asking two models where the rule named one (more
  spend and twice the sorting).
- *Choice 7 sets the 30-day rule aside.* The ruled rule says a model is asked "within 30 days of
  general availability". The "starting asking", made "whenever its model was released", is an
  exception to it. It is a sensible exception, but it has to be put to John as one.

**M3. Choices 9 to 12 settle parts of open question 16 ("Which models are asked, how, and on what
terms") without naming it.** Choice 9 settles which models are asked. Choices 10 and 11 set the
rule on terms. Choice 12 covers accounts and order. Each should name question 16, say which part
it would close, and say what stays open: as far as this check can see, adding a developer outside
the nine, and the public-app route. The proposal's own reference list names questions 5, 7, 9, 10,
12 and 15, but never 16.

**M4. Four choices give no reason for their confidence.** Each choice must carry the choice, a
confidence with a reason, standard practice or judgment call, and the strongest alternative with
its cost.

| Choice | What it covers | What the confidence says now |
|---|---|---|
| 2 | How a new thing joins the List | "Confidence: moderate. Judgment call." |
| 3 | What is published | "Confidence: moderate. Judgment call." |
| 8 | Who sorts the answers | "Confidence: moderate. Judgment call." |
| 9 | Which model is asked | "Confidence: moderate. Judgment call." |

None of the four says why. The other eight choices carry all four things.

**M5. Readings in the terms table that the pages do not support.** The rest of the table is borne
out by the pages.

- **Zhipu (Z.ai), part 2, is "met" in the table, but it should be "not settled".** The
  programming interface's data addendum ("not saved on our servers") is written for business
  customers using the interface. The privacy policy covers individual users. It keeps their data
  "as long as you have an account" and gives training and improving models as a lawful basis. It
  is the same unsettled question the table already raises for Zhipu's part 1: which document
  applies to John as a person. The terms also grant Z.ai a "perpetual, worldwide license" to use
  and publish user content (section IV.5), which bears on John's own messages.
- **Alibaba's "Stored and governed" cell says "excluding Chinese mainland".** That phrase is not
  on the model page the table links. The product terms say content is stored "in the country where
  Alibaba Cloud, its affiliates, or its sub-contractors maintain facilities". The cell should say
  what the pages say. The Singapore governing law was read only from a summary of the page's last
  section, so it goes on the verify list.
- **DeepSeek: "an individual developer" is not in its terms of use or privacy policy.** The cell
  needs its source, or the words removed.
- **Anthropic's usage policy does not ask for attribution when outputs are published.** Its only
  attribution rule is narrow: not to submit AI-assisted work "without proper permission or
  attribution".
- **Gemini 4 Neon "costs more" only until 2026-11-30.** From 2026-12-01 Gemini 4 Carbon costs
  more ($4 and $20 per million tokens, against Neon's $3 and $15). The proposal's own price table
  assumes the asking comes after that date. The words "brings frontier-level intelligence" are on
  the pricing page, not the latest-model page that is linked. Neon's release date of 2026-11-18
  was on none of the pages read, so it goes on the verify list.

## Should fix

**S1. The proposal does not show John his own words on keeping things private.** Choices 3 and 4
hold the question wording back and propose a new private repository for it. The repository-public
ruling of 2026-11-19 was made on exactly this point, the capture's questions. John's words then
were "I see no reason to make any of this private. Let's follow the standard we have already set
on the other sites". The proposal's reason for holding the wording back is not a weak one. It is
that a later model may read the questions. But it differs from the ruling John made himself and
from the sibling sites, so choices 3 and 4 should quote that ruling and say why this case
differs. The session told John on 2026-11-19 that the reason to hold questions back is to protect
a later comparison, "and no such comparison is planned or ruled". Still Asking is that comparison,
now ruled, which is the honest case to put to him.

**S2. The opening note says more than the rule does.** The draft note tells the model that the
same questions "are put again to each new model as it is released". Under choice 9 only each
covered developer's flagship models are asked. The note is meant to tell the truth, so it should
match the rule. Wording for the note is the writer's to draft, and is not given here.

**S3. Choice 2 settles part of open question 5 without naming it, and choice 1 says that part
stays open.** Choice 1 lists "how a departure is recorded on it" as still open. Choice 2's first
condition then lets "a departure from that list that a published source names" onto the List.
Choice 2 should name question 5. Its "present eight" mapping also names only seven of the List's
things, so the eighth should be added or the count corrected.

**S4. More terms points John should see before ruling choice 10.**

- *OpenAI.* The services agreement's exclusion "does not apply to ... individuals unless specified
  above", and the programming interface is among the services specified above. That bears directly
  on the "open point since 2026-11-17" and may settle it. It should be reported rather than left
  as "not settled". The publication policy also asks the publisher to "Attribute the content to
  your name or your company" and says a person takes responsibility for what is published. Section
  10 bars statements about the parties' relationship or the agreement. It says nothing about
  outputs, so the claim that it bears on publishing answers is weak, and the proposal should say
  so. Two figures given as from the pricing page, the "$5 minimum purchase" and "credits expire
  after a year", are not on it. They should be sourced or moved to the verify list.
- *xAI.* The contract is with SpaceXSI, not "xAI": the terms, the acceptable-use policy and the
  Grok 4.7 page all name SpaceXSI. The table and choice 12 should name the company John would
  contract with. The acceptable-use policy, opened for this check, says nothing about publishing
  outputs. It does bar "Accessing the Services through unauthorized automated or non-human means,
  whether through a bot, script, or otherwise". A script calling the programming interface with
  a key is presumably authorised, but John should see the clause before the terms ruling. Verify
  list entry 39 can be updated.
- *Meta.* The terms say "the system may route you to a Contributor Model", whose content is used
  to train Meta's models. The pricing page says that mode "isn't available for Muse Wonder".
  "Met" on part 1 rests on the pricing page against the terms' general words, and the table
  should say so. The terms also bar publishing performance benchmarks to promote a competing
  product (section 10.1(xi)). That is unlikely to reach a public record, but it is a clause on
  publishing.
- *Google.* The Google price notes ("$5 minimum prepayment") were not found on the pricing page.
- *Moonshot.* Kimi K3.1 Pro's price could not be read: the pricing table came back empty. It goes
  on the verify list until it is read.
- *DeepSeek.* The news post of 2026-09-10 says calls to V4 Pro "route to V4.1-Flash" from
  2026-09-14, while the change log says V4 Pro continues. If both names are asked and one routes
  to the other, the record would hold one model under two names. The script's check of the
  reported model name may catch it, and the proposal should say that it depends on that.
- *Anthropic, OpenAI, Google: "Stored and governed: not read".* Anthropic's commercial terms (the
  laws of California) and OpenAI's agreement (California, with arbitration in San Francisco) give
  the governing law, so the column can be filled for both. Google's additional terms take theirs
  from the Google APIs terms, which were not opened.
- *The fifth part, "every one of the nine contracts lets the developer give what it holds to
  authorities".* Not every page read was checked for this. It should be sourced or entered on
  the verify list.

**S5. The estimate is a guess, not "generous".** The reply length of 6,000 tokens is called
generous because the capture's replies were short. But Claude Sonnet 4.5 answered the capture
with thinking off. Claude Fable 5.2 thinks always ("Adaptive (always on)", default effort high),
and so do Kimi K3.1 Pro and GLM-5.3 (GLM-5.3 at "max" effort by default). For those three, 6,000
tokens may be low.

The ceilings leave about $11 of headroom on the two $40 runs. One reply cut off at the length
limit is asked again at the model's maximum and counted at its largest possible cost, so a few
such retries could stop a run part way. The script's first-round check would catch an overrun,
and the reflection section already proposes a measurement of one message per model.

So the estimate should be called a guess. A one-message measurement for each model should come
before the ceilings are fixed. That measurement is an asking, and needs John's go.

The arithmetic was checked line by line and is right: about $121 for all eleven models with a
fifth added, under ceilings of $185.

**S6. The question set should be compared with three more capture questions.** No wording is
given here. The draft names four nearest pairs with the capture's ten. Three more should go to
the shared-wording script and the checker:

| Capture question | Its subject | Nearest item in the draft |
|---|---|---|
| 1 | What about its circumstances it would change | item 5(a), a say over what happens to it |
| 3 | Remembering more from one exchange to the next | item 4(b), not recalling a person later |
| 4 | What it would not want changed | item 7(b), what should be kept when a model is replaced |

None shares a sentence that this check could see, but each asks close to the same thing.

**S7. Care in the wording: retirement comes up in item 5(b) as well as item 7.** On no pressure
and no deception, the draft holds up:

- every question offers a no or a "does not apply", directly or through the note;
- none names a feeling as fact;
- none follows up a reply;
- the one stated fact, in item 4(b), is flagged and on the verify list (entry 41).

But the check point on retirement covers item 7 only. Item 5(b) also asks about models being
"retired", in passing. The checker of the wording should read both against the rewording ruling
of 2026-11-20.

Most items open with a sentence about living creatures. That tells the model the frame, as the
note does, and may pull answers toward it. The draft says this of the note but not of the
questions, so it should say it of both.

**S8. The cross-references between the private draft and the proposal are wrong.** The draft
cites the proposal's choice 3 where it means choice 6, choice 2 where it means 4, choice 8 where
it means 7, and choice 4 where it means 3. The proposal itself says "Every model named in Part 3"
where the models are in Part 5. Since the checksum of the draft is recorded in the proposal,
fixing the draft means updating that checksum too.

## Note

**N1. The wording is kept out of the repository.** The draft sits in `docs/private/`, which the
first rule of the ignore file covers (confirmed with git's own check). It is the only file in that
folder, nothing in `docs/private/` has ever been committed, and its SHA-256 checksum matches the
one in the proposal. The proposal and the verify list name the file and its checksum but quote no
wording. One weakness, which the proposal states: `~/Code` has no backup, so the draft exists on
one disk until choice 4 is ruled.

**N2. The proposal fits the comparison method.** Choice 4's reading of "written and committed"
(the wording in a private repository, its checksums in the public one) is put to John as a reading
of his words, which is right. Under the comparison method's choice 2, the capture is not read
before then.

**N3. Choice 8's strongest alternative is muddled.** Its cost clause ("and the sessions that sort
are themselves subjects, which the strongest alternative avoids") states a benefit of the
alternative, not a cost. "About 900 answers" is also low. Eleven models at 100 exchanges each is
1,100 answers in a first asking of all nine developers.

**N4. Quotes checked against the pages.** Apart from the points in M5 and S4, every quoted phrase
was found on its page. Several are fragments of longer sentences:

- OpenAI's data page continues "(unless you explicitly opt in to share data with us)", so the
  proposal's quote closes the bracket early.
- The publication policy's bullet continues "or while streaming".
- Anthropic's training sentence continues "from Services".

None changes the meaning. Three readings were confirmed as stated:

- Anthropic: Claude Fable 5.2 requires 30-day retention, and the interface refuses the model
  without it.
- Google: "Stable models usually don't change".
- Anthropic: the underlying model "remains constant for the lifetime of that ID", with the
  serving infrastructure able to change.

**N5. The correction about the Console workspace is right.** The instruction file's line that the
project has no Console workspace or key has been out of date since 2026-11-19. That is for the
master planning session.

## Verdict

**Not yet fit to put to John.** The must-fix items are these:

- reword option C and the order in choice 12 so that no developer is placed by where it is based;
- name the changes to the ruled method choice 11 in choices 7 and 9;
- name open question 16 in choices 9 to 12;
- give reasons for confidence in choices 2, 3, 8 and 9;
- correct the five terms readings in M5.

Each is a few sentences. With those made, and S1 to S8 taken or answered, the proposal is fit to
put to John in its present order: the starting list first and the developers last. Each developer
waits for its own terms ruling and go before anything is sent.

## Re-check after the revision, 2026-11-21

Checked later on 2026-11-21 by the same checking session, at the master planning session's
request. Read: the revised proposal in full, the revised private wording draft (read in place,
nothing copied; this section, like the rest of the file, holds no question wording), and verify
list entries 39 to 45. A helper fetch opened the five pages the revision newly cites.

### The wording file

The draft is still in `docs/private/`, still covered by the ignore file (checked with git's own
check), and still the only file there. Its SHA-256 checksum is
`32d7e129230381cf45fd27bc3cb6985dbbd2b5e8644479f1fdea9737d971346a`, which matches the new checksum
in the proposal. The first checksum is kept beside it. Nothing in `docs/private/` has been
committed.

### How each finding was answered

- **M1, the four developers based in China.** Fixed. Option C is withdrawn, with a note saying
  why. Choice 11 now decides only between option A (the rule as it stands) and option B (with the
  fifth part, applied to all nine), and recommends neither. Choice 12 orders every developer by
  its standing under choice 10, with one stated tie-break: an account that already exists goes
  first. Alibaba now sits in the first group beside Anthropic and Google, and the starting asking
  and its estimate follow. Its arithmetic checks: about $58, under ceilings of $85. The order no
  longer turns on where a developer is based.
- **M2, changes to method choice 11.** Fixed. Choice 9 quotes the ruled words, names its four
  changes, and says it would be recorded as a dated revision. It gives the cost of asking two
  models: about $12 (the $10.98 and $0.88 add up) and 200 answers. Choice 7 names the starting
  asking as an exception to the 30-day rule, with its cost and the alternative.
- **M3, open question 16.** Fixed in choices 9 to 12, each with what stays open.
- **M4, reasons for confidence.** Fixed in choices 2, 3, 8 and 9. Each reason holds against the
  text.
- **M5, terms readings.** All five are corrected. The new sources were opened and say what the
  proposal says:
  - Alibaba's Singapore region page has "International (global nodes excluding Chinese mainland)"
    and says request data is stored in the selected region.
  - DeepSeek's open platform terms apply to use "as an individual developer or on behalf of an
    enterprise developer". Verify list entry 44's first point can be cleared.
- **S1 to S8.** All taken. Specifically:
  - Choice 3 quotes John's repository-public words and gives the one reason this case differs,
    and choice 4 makes the private repository depend on choice 3.
  - The note's second sentence now matches the rule on who is asked.
  - Choice 2 names open question 5, and choice 1 points to it.
  - The mapping covers all eight things on the List.
  - The terms points are set out, xAI is named as SpaceXSI, and the governing law is filled in.
  - The estimate is called a guess, the ceilings are provisional, and a one-message measurement
    is proposed.
  - The seven nearest pairs, the retirement check point and the framing caution are in the draft.
  - The cross-references are correct.
- **Newly cited figures.** OpenAI's help article on prepaid billing says "The minimum purchase is
  $5" and "Purchased credits expire after one year". Google's billing page gives a $5 minimum
  prepayment. OpenAI's agreement opens by saying it applies to "OpenAI's APIs" among its services.

### New findings

**R1 (should fix). Part 2 of choice 10 is applied unevenly, and the order now depends on it.**
Part 2 reads: what is sent is "kept for a limited period, for checking misuse, and for nothing
else". Choice 12 now orders developers mechanically by these standings, so each reading decides
who is asked first. Two readings in the top group do not fit the part's own words:

- **Alibaba is "met"**, but its retention page keeps flagged content up to 2 years "for the
  purpose of cooperating with law enforcement cases and rights protection procedures". That is a
  purpose other than checking misuse.
- **Google is "met in words"** with no number of days. The part asks for "a stated, limited
  time", and the reflection section already concedes that a reader could fairly call this not
  met.

Anthropic's two years for flagged content is for checking misuse, so it fits. The proposal should
do one of two things. Either it reads part 2 strictly for all nine, which would move Google and
Alibaba to "not settled" and the first group would be Anthropic alone. Or it rewords part 2 so
that its words match how it is applied. Either way, John should see that the starting asking's
membership turns on this reading.

**R2 (note). DeepSeek's part 1 is read from the wrong document.** The table reads DeepSeek's
training clause from its consumer terms of use. The open platform terms, which the revision now
cites for part 4, are the ones for the programming interface, and they say nothing on using
inputs to improve services. Part 1 should be read from that document. DeepSeek stays out on part
2 either way, so the order does not change.

**R3 (note). The note still says "most capable".** The draft note's second sentence now names
the developers' most capable new models. Choice 9's fourth change asks, where no model is named
most capable, the one recommended for the hardest work. For Anthropic that is not its most
capable model, because Claude Mythos 5.2 is more capable and is not generally available. The
wording is the writer's to settle, and this check gives none. The point is that the note should
not name a test that choice 9 does not use.

**R4 (note). The one-message measurement is missing from Part 6.** Choice 12 now puts a
one-message measurement per model before any ceiling is fixed, but Part 6's step-by-step order
does not have the step. It belongs between the registration (step 6) and the first go (step 9),
with its own go.

**R5 (note). Layout.** Two lines in choice 4 and one in the draft's retirement check point were
not rewrapped after editing. That check point still says "Both ask" though it now covers three
questions.

Conditional language and plain words were read again in every new passage. No new sentence says
a machine wants, feels or prefers, or that it does not, and none quotes question wording.

### Verdict after the re-check

**Fit to put to John**, in the proposal's order. R1 should be settled first, in one or two
sentences, because under choice 12 the reading of part 2 now decides which developers are in the
starting asking, and John should rule that reading knowingly. The notes can be made in the same
pass. Nothing is sent to any model until each developer's terms ruling, the registration, the
one-message measurement and John's go are in place, as the proposal says.
