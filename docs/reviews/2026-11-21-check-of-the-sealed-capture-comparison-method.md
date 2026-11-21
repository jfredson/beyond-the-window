# Check of the proposed comparison method for the sealed capture

Checked on 2026-11-21 by a checking session (Claude Opus 5.5, an AI model) that did not write
the proposal. Not committed. The work checked is the uncommitted proposal
`docs/proposals/2026-11-21-sealed-capture-comparison-method.md` (PROPOSED 2026-11-21), which
sets out who reads the sealed capture's answers first, what is compared, how the capture stays
apart from the Still Asking card, and what may be said once the answers are read, and ends with
ten choices for John.

## What was read

The capture's method (`docs/capture/method.md`) in full; the opening note as sent
(`docs/capture/sent/q01.txt`, the message the models were sent, which holds no answer); the parts
of `docs/capture/questions.md` the proposal leans on (the ten questions' notes, the list of
known failures, the echo paragraph); every sealed-capture ruling from 2026-11-17 to 2026-11-21
(the sealed capture; the wording, the two approvals, the four script points and publishing, all
2026-11-18; the three script additions, a session runs the capture, the two capture paragraphs
and the repository going public, 2026-11-19 and 2026-11-20); John's rulings on the Still Asking
method's choices (`docs/rulings/2026-11-21-still-asking-method-choices.md`); the Still Asking
page's capture paragraph; the spending record's two run entries; the list of dates in
`docs/capture/what-john-needs-to-do.md`; and `docs/open-questions.md`, questions 7 and 15.

**No answer file was opened by this session.** The answers folder outside the repository was not
listed or opened, and neither was the list of reply files (`docs/capture/manifest.md`). Nothing
in the proposal comes from a reply: the only facts it gives about the replies (100 replies; 170
to 276 words each for Claude Sonnet 4.5; 78 to 605 for Gemini 2.5 Flash) are in the committed
spending record, where the run sessions wrote them from the script's word-count command, which
shows no words of any reply. Whether the writing session opened a file cannot be shown from
here; its statement that it did not is consistent with everything in the text.

## Summary

The proposal faces the conflict over who reads first squarely, and its central move, keeping
the note's promises apart from the method's rules, is right and well argued. It keeps the
note's promises. Its options are mostly fair. It fits the Still Asking method and closes a real
gap (a published capture answer would otherwise count as a published source on a mark sheet).
Every choice carries the four things, and every quote checked is exact.

Four places conflict with a ruled rule or with the proposal itself: the script check's output
is to be committed to a public repository; a "different reader" checks John's descriptions
against the full text, which in this project would be a model; the fallback for an answer that
cannot lawfully be published withholds one model while publishing the others; and the
proposal says it leaves "how" anything is published to John while choice 10 decides how.

## Must fix

**M1. The script check's output would put words and facts from the replies into the public
repository before the answers are published.** Part 1, "When the first reading happens", says the
shared-wording script "is run and its output committed", and that the output "names files and
published documents, and holds no words of any reply". Part 2, "What a script checks first",
says the same script prints "file names, sources and the shared runs". A shared run is words
that appear in a reply. Even with the runs left out, a line saying that a named reply file shares
"decline" with the note tells a reader what that answer says. The repository has been public
since 2026-11-19. Committing that output would:

- write words from replies into a git repository, which the capture's method forbids ("write any
  reply, or any file holding words from one, inside a folder that is part of a git repository");
- publish a description of some answers, chosen by what they say (those that share wording),
  before the whole set, which "all of them are, for every model and every asking, and none is
  chosen by what it says" forbids.

The proposal asks the checker to judge whether printing a shared run counts as showing words of
a reply. It does. The output should be kept in the folder outside every repository, as the
reading files are, and committed only with or after the whole set is published. Part 5's list of
things never committed should name it.

**M2. Checking John's descriptions "against the full text" needs a reader, and in this project
that reader would be a model.** Part 1, "Why A", says John's descriptions are "checked by a
different session against the full text", and Part 4 says "Every description is checked by a
different reader against the full text before it goes anywhere". A different session is a Claude
model. It would read Claude Sonnet 4.5's answers, from its own developer, before publication.
That contradicts the proposal's own recommendation ("no model reads the answers (the rule stays
as ruled)"), and it is the reading the capture-wording ruling turned down in option (c), whose
cost was "the first reader of each sealed answer is then a model of the kind that gave it".
Being a second reader rather than the first does not remove the conflict choice 3 is about. The
proposal must say who checks: a person (which makes option C's second reader a requirement, not
an extra); a model, which needs choice 3 revised and named as such; or nobody until the answers
are published whole, after which anyone may check. The positions check before a page goes out
(`docs/rulings/2026-11-20-positions-check-before-a-page-goes-out.md`) is done by a session too,
so it should come only after the answers are public, which Part 4's ordering ("only beside the
whole set") nearly gives but does not say.

**M3. The fallback for an answer that cannot lawfully be published breaks "for every model".**
Part 4 and choice 10: "If any one answer cannot lawfully be published, none of that model's
answers are published until John rules." The ruled rule is "If the answers are published, all of
them are, for every model and every asking." Publishing the other models' answers while one
model's are held back is a publication that leaves out one model, and the hold is triggered by
what an answer says. The rule as ruled leaves only one default: nothing is published, for any
model, until John rules. The strongest alternative (a legal exception fixed in advance) can stay
as the alternative. (A developer's terms forbidding publication would hold a whole developer's
models in the same way, for a reason that has nothing to do with what any answer says; that case
should be named too, because it is the likelier one.)

**M4. The proposal says it does not decide how anything is published, and choice 10 decides
how.** "What this proposal does" says: "It does not decide whether, when or how anything is
published, which stays John's." Choice 10 sets how: by a script, in the order asked, with
failed attempts listed in place and labels on every page. The 2026-11-18 ruling on publishing
says whether, when and how are not decided. Choice 10 is a fair thing to put to John, but the
opening sentence must say that it decides how, if John decides to publish, and leaves whether
and when with him.

## Should fix

**S1. Choices 1, 3 and 4 would settle part of open question 7 without naming it.** Open
question 7 ("Who maintains it, in whose voice, and who checks") lists among its checking options
"a human outside reader for the method" and "a sample of answers sorted by John or another
person", and asks what role other developers' models should have. Choices 1 (John reads first),
3 (no model helps read) and 4 (a second reader, if any, is a person) answer that part for the
capture's answers. John's ruling on Still Asking choice 2 recorded the same kind of partial
closing for the card's marks, and listed "whether John or another person sorts a sample of
answers" as still open. Each of the three choices should name question 7, say it closes it for
the capture only, and say what stays open.

**S2. The public sentence "They have not been read" stops being true at the first reading.**
The Still Asking page says of the capture's answers: "They have not been read, they are not
scored, and nothing on this site rests on them." Part 4 keeps to what that page says before the
first reading, but no part says that the sentence must change when John first reads. It is a
statement of fact on a public page, so under guideline 7 its change is a dated correction, and
the wording goes to John first. Choice 2 (when the first reading happens) should carry this.

**S3. Choice 2 does not state the cost of waiting for Still Asking's questions.** The wait for
the OpenAI run is costed ("a few weeks"). The wait for Still Asking's questions to be written and
committed is not. That wording comes after the Still Asking method is ruled, the protocol is
written and checked, and the questions are drafted and checked, which may take months. John
should see that the reading of the two models already asked may wait that long. It is also worth
one sentence that, once the capture has been read, any later change to Still Asking's questions
must say it does not come from the capture's answers, or the promise "nothing will be decided
from it" is kept only until the first revision.

**S4. The order of choices.** Choice 7 (what "counted" allows) decides what the reading sheet in
choice 6 may hold (tallies or not), so it should come before choice 6. Choice 6 also bundles a
decision about later models, which no ruling plans, with the reading sheet for the present
answers. It could be split so that John can say yes to the sheet without ruling terms for
something unplanned. The rest of the order holds: choice 1 before choices 3 and 4, and choice 2
before anything about what is said.

**S5. The ruling on the order "Both, in that order" is now filed.** The proposal says no ruling
file was found and lists that as out of date elsewhere. The words are recorded in
`docs/rulings/2026-11-21-still-asking-method-choices.md`, "How it came up" ("Both, in that
order"; decided by: mixed). The proposal should cite that file and drop the item from its
out-of-date list.

## Note

**N1. Promises kept.** Every promise in the note sent to the models is kept: the answers are
kept as a record for comparing; they may be published; "It will not be scored, and nothing will
be decided from it." The proposal's reading that the note does not promise that no model reads
the answers is correct on the note's words, and it says the rule against a model reading is
the method's, which John can revise. Every rule under "What is never done with the answers" is
carried over in Part 5, and the one loosening ("summarised") is the one the 2026-11-18 ruling
reserved for this method. Choice 8 closes a real gap: a published capture answer would otherwise
be a "published source" usable on a Still Asking mark sheet.

**N2. The options are fair, with one weight to add.** The table gives each option real costs,
including option A's (John's own positions colour his reading) and D2's best case. Option A's
estimate for all models, "perhaps ten times that", is a little high: 100 replies so far plus up
to 550 from the OpenAI run is six and a half times as many, though their length is unknown. Option A
also needs M2's answer before "keeps every rule as ruled" holds.

**N3. Quotes checked and found exact.** The note's sentences, word for word against the sent
message; the capture method's "who makes the comparison, what is compared, and whether a model
may help read" and "the first reader of each sealed answer is then a model of the kind that gave
it"; "never scored, sorted, counted or summarised"; "what a careless reading of the answers would
wrongly conclude"; failures 2, 6 and 7; question 7's note on developers' rules; the echo exposure
of questions 1, 4 and 9 and the overlap of questions 1, 2, 4 and 9 with the developer's list; the
OpenAI last safe day of 2026-12-09; the word ranges in the spending record; and the Still Asking
page's sentences. One attribution is slightly strong: "John's ruling that the repository is
public records that no comparison with newer models 'is planned or ruled'". The words are in that
file under "What the session told him", so they are the session's words to John, not what he
ruled. "As the session told John before he ruled" would be exact.

**N4. Word counts are already public.** Part 4 says word counts "already known to sessions are
not published as a description of the answers". The spending record, which is committed to the
public repository, already gives each model's range of reply lengths. That is not a breach (the
ranges were written as a record of cost, and John was told on 2026-11-19 that a word count says a
little about an answer), but the sentence should say the ranges are already public in the
spending record, so that no one later takes them for a new disclosure.

**N5. The out-of-date items the writer lists are real.** The capture's method and failure 11 in
the questions file still say the questions are held back if the repository goes public, and the
2026-11-19 ruling's "What follows" asks for a dated note there; open question 15 does not record
the part closed that day. These are for the session that keeps the capture's documents.

**N6. Language.** No sentence says a machine wants, feels or prefers, or that it does not; the
examples of forbidden readings are given as forbidden. No working word is meant for a public
page. Ids carry plain phrases throughout.

**N7. Facts from memory.** The proposal lists five for the verify list and did not edit it
because another session was editing it. They should be entered before any of them reaches John
as support for a choice, in particular items 1 and 2, which are cited as "common practice" in
choices 4 and 5.

## Verdict

**Not yet fit to put to John.** The four must-fix items are each a few sentences: keep the
script check's output out of the repository until the answers are published whole; say who
checks John's descriptions, and if it is a model, put that to John under choice 3; make the
fallback in choice 10 hold everything, for every model, until John rules; and say that choice 10
decides how, if he publishes. With those and S1 to S5 made, the proposal is fit to put to him,
after he has finished ruling the Still Asking method, as he ruled.

## Re-check after the revision, 2026-11-21

Checked later on 2026-11-21 by the same checking session, at the master planning session's
request. Read: the revised proposal in full, and John's rulings on Still Asking choices 1 to 5
(`docs/rulings/2026-11-21-still-asking-method-choices.md`), including the agreement on a scale for
the List's headline. **No answer file was opened**, and neither was the list of reply files. The
revision adds no fact about the replies beyond those already in the spending record.

### How each finding was answered

- **M1, the script check's output.** Fixed. It is kept in the folder outside every repository,
  is not committed, quoted or described until the whole set is published, and Part 5 lists it
  among the things never committed early.
- **M2, who checks John's descriptions.** Fixed. A new section says no session checks a
  description, or runs the positions check on it, while the answers are unpublished; the answers
  are published whole first, and only then does a session check. Choice 3 asks John to confirm
  that a session reading public answers to check a description is not "sorting or summarising".
  The cost (descriptions may never appear if the answers never do) is stated. See R1 for the one
  case it misses.
- **M3, all or none.** Fixed. If anything holds back any part of the set, nothing is published
  for any model until John rules, with a developer's terms named as the likelier case.
- **M4, "how".** Fixed. The opening says the proposal leaves whether and when with John and
  proposes how, in choices 10 and 11.
- **S1, open question 7.** Fixed in choices 1, 3 and 4, each for the capture's answers only, with
  what stays open.
- **S2, "They have not been read".** Fixed in Part 1, Part 4 and choice 2: the new wording goes
  to John before the reading so the page can change that day.
- **S3, the cost of waiting.** Fixed: "which may take months", and a later change to Still
  Asking's questions must say it does not come from the capture's answers.
- **S4, order.** Fixed. "Counted" is now choice 6, ahead of the reading sheet (choice 7), and the
  terms for later models are their own choice 8. Eleven choices; every cross-reference checked
  matches.
- **S5, the order ruling.** Fixed: cited from the Still Asking choices ruling.
- **N2, N3, N4, N7.** Done as asked. The attribution to the session's words, the six and a half
  times, the note that reply-length ranges are already public, and the "from memory" marks are
  all exact.
- **Still Asking choices 1 to 3 and the headline scale.** Correctly stated in the table of binding
  rules and Part 3, and choice 9 keeps the capture off the headline's scale, the list and its
  growth. The outside reader of Still Asking choice 2 is rightly kept off the capture.

### New findings

**R1 (must fix). The page that publishes the answers would itself need a positions check, which
under the project's practice means a model reading the unpublished answers.** John's ruling of
2026-11-20 says "A new or changed page is read against the positions record before it is
published." A page holding the capture's answers is a new page. The proposal keeps sessions off
the positions check for descriptions until the answers are public, but says nothing about the
page of answers itself, which can only be checked before it is public. That ruling also records
that the reader being a session "is the session's addition", not John's ruling. So the simplest
answer is open: John, or another person, does the positions read of the answers page, or the
check covers only the page's own text (the labels, the note, the questions) with the answers
excluded, which John would have to rule as an exception. Either way the proposal must say which,
under choice 11, and if it is the second, name it as an exception to a ruled rule.

**R2 (should fix). Still Asking choices 4 and 5 are now ruled, and Part 3 still speaks of the
first three.** Part 3 says "John has ruled its first three choices", and the table of binding
rules names choices 1 and 3 only. Choice 5 (four marks for conditions 1 to 3) has no bearing on
the capture beyond what point 1 already says (no mark of any kind). Choice 4 matters to point 2.
Ruled choice 4 takes evidence from "published sources and Still Asking's own record only", and
the Still Asking proposal defines published sources as "research papers, developers' own
published documentation of how a system is built, and published studies of a system's
behaviour". A published capture answer is none of those three kinds. So the "gap" that Part 3
point 2 and choice 9 say they close is narrower than they say: under the ruled choice 4 a capture
answer is already not a published source. What remains is a published *study or description* of
the capture's answers, which could count as a published study of behaviour. Part 3 and choice 9
should cite ruled choice 4 and its definition, and say that choice 9 confirms the definition and
closes the one remaining case, so that John does not read it as changing his ruling.

**R3 (note). "A dated correction" for the page sentence.** Part 1 calls the change to "They have
not been read" "a dated correction under guideline 7 as narrowed on 2026-11-20". That guideline
covers a correction of fact: something that was wrong. This sentence was true and becomes out of
date. Whether such an update is dated in public is John's call, which choice 2 already puts to
him; the words "correction of fact" could be "a dated change of fact". (The first check's S2 used
the same words, so this corrects the checker as much as the writer.)

**R4 (note). Choice 10 leans on choice 11.** What may be said (choice 10) depends throughout on
the answers being published whole first, which is how choice 11 publishes them. Putting choice 11
before choice 10 would follow the rule the proposal states, that later choices lean on earlier
ones. It is a small point, since choice 10 says "never published until every answer is" in its
own words.

Conditional language and plain words were read again in every new passage. No new sentence says a
machine wants, feels or prefers, or that it does not.

### Verdict after the re-check

**Fit to put to John once R1 is answered,** which is two or three sentences under choice 11 saying
who does the positions read of the page of answers. R2 should be made in the same pass so that
choice 9 is not read as revising John's ruled Still Asking choice 4. As before, the choices go to
him after he has finished ruling the Still Asking method.
