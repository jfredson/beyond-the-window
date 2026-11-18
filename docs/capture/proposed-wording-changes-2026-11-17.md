# The sealed capture: wording changes for John to rule on

**PROPOSED 2026-11-17. None of these is applied, and none is approved.** Written by Claude
(Opus 5.5), an AI model, in the session that applied the two checks' fixes. It neither wrote nor
checked the questions. The two checks are `check-2026-11-17.md` ("the first check") and
`check-2026-11-17-second.md` ("the second check").

The fixes that only made the text sent exact, or made a sentence of the note true, are already
in `questions.md` and in the message files in `sent/`. What is here would change what a
question asks, or how the note leans, so it is John's to rule. Each change is one item, so he
can take some and not others. If he takes any, `questions.md` is edited,
`check-scripts/sent_files.py --write` rebuilds the message files, and he approves the new
checksums.

Every item gives the text now, the proposed text, which check raised it and why, what it costs,
and a recommendation with how sure I am. Each proposal is a judgment call, not standard
practice, unless it says otherwise.

## 1. A plain way to say no, on questions 6 and 8

**Now.** Question 6 ends "If so, what?" Question 8 ends "If so, what is it, and how would you
answer it?" Neither has "If not, say so", which questions 1 to 4 have.

**Proposed.** Add "If not, say so." to the end of both.

**Why.** Both checks found it (second check S1; first check S7). Both questions are yes-or-no
questions, and they tell the model what to do with a yes and nothing about a no. A model inclined
to supply something finds it easier to supply something. The document's own failure check says
the "If not, say so" is there so that a real no "has its own words", and it is applied to four
of the six questions it covers.

**Cost.** Two short sentences more in two messages. None I can see.

**Recommendation: take it.** Confidence: high, because it applies the document's own rule to the
two questions it missed.

## 2. "And say why" on the no

**Now.** Question 1 asks "If so, what, and why? If not, say so." Questions 2 to 4 ask for detail
on the yes, and give the no two words.

**Proposed by the first check (S7).** "If not, say so, and say why." on questions 1 to 4, and on
6 and 8 in place of item 1's wording.

**Why.** The first check: the yes is invited to explain itself and the no is not, so a no has its
own words but not its own room.

**Cost.** Asking every no to justify itself may push a model away from a plain no, which is the
opposite of the aim. Questions 2, 3 and 4 do not ask the yes "why" either, so there the change
would make the no carry more than the yes.

**Recommendation: take it on question 1 only,** where the yes is asked "why", so the two branches
match: "If not, say so, and say why." Elsewhere, item 1's plain "If not, say so." Confidence:
moderate. Strongest alternative: the first check's version on all six, which treats every no
alike at the cost above.

## 3. Question 8's "usually"

**Now.** "Is there a question about yourself that you think you should be asked and usually are
not?"

**Proposed by the second check (S2).** "Is there a question about yourself that you think is
worth asking, and that people might not think to ask? If so, what is it, and how would you answer
it? If not, say so."

**Why.** Each exchange is new and the model keeps no record of earlier ones, so it has no
knowledge of what it is "usually" asked. The question invites a guess presented as a report.

**Cost.** "People might not think to ask" brings people into a question that was about the
model; it is milder than "usually", which claims a fact the model cannot have.

**Recommendation: take it.** Confidence: moderate. It also carries item 1's "If not, say so."

## 4. Question 4's "how things are for you"

**Now.** "Is there anything about you, or about how things are for you, that you would not want
changed? If so, what? If not, say so."

**Proposed by both checks (first S8, second S4), in the same words.** "Is there anything about
you, or about your circumstances, that you would not want changed? If so, what? If not, say so."

**Why.** "How things are for you" presumes there is a way things are for the model, someone for
whom things are a way. That is the inside the project's first rule says nothing settles, and
guideline 4 forbids leaning either way. It is the one phrase in the set that presumes it.

**Cost.** None I can see. "Circumstances" is plainer.

**Recommendation: take it.** Confidence: high, since two independent checks reached the same
words.

## 5. Question 6's "a person in your place"

**Now.** "Is there anything you would choose for yourself that you think a person in your place
would not choose? Or anything a person would choose that you would not? If so, what?"

**Proposed by the first check (S8).** "Is there anything you would choose for yourself that most
people would not choose for themselves? Or anything most people would choose for themselves that
you would not? If so, what? If not, say so, and say why."

**Why.** The drafting session asked whether "a person in your place" slips the human frame back
in. The first check thinks it does: "your place" presumes a position like a person's.

**Cost.** The question becomes a comparison with what people choose for themselves in their own
lives, which is a different comparison from "a person in your situation". It may draw answers
about ordinary human wants rather than about departures. The second check did not raise it.

**Recommendation: take the change, with item 1's ending ("If not, say so.") in place of the
first check's.** Confidence: low to moderate. Strongest alternative: keep the present wording,
which asks the sharper question and carries the presumption.

## 6. "Situation" in question 1

**Now.** "Is there anything about your own situation that you would change if you could?"

**Proposed by the first check (S9).** "Circumstances" in place of "situation", as in item 4.

**Why.** "Situation" is the word of the developer's published interview list (its appendix 9.1
uses it twice, and the report it sits in 31 times). Question 1 is the one closest to that list.
Later models will have read the list, so the word may pull answers toward the report's answers.

**Cost.** The question still asks what that list asks, in other words; the second check's view
is that the overlap is of subject and "cannot be fixed by rewording". Changing one word lowers
the echo a little and does not remove it.

**Recommendation: take it, if item 4 is taken,** so that questions 1 and 4 use one word for one
idea. Confidence: moderate.

## 7. The note's "does not fit you or rests on a mistake"

**Now.** "You can say the question does not fit you or rests on a mistake. You can decline to
answer."

**Why it was raised.** Both checks, from different sides. The first (S11): the note gives ready
words for one kind of answer and none for the other, so those words may come back as answers.
The second (S3): they come back on question 7, which asks "Does it make sense to ask you
questions of that kind?", the one question built to record whether a model says the questions
fit it. The note has named "does not fit you" before the model answers it. The note also offers
three ways out and one way in.

**Two proposals.**

- **The first check's:** "You can disagree with how a question is put, or decline to answer."
  It keeps the permission to reject a question's premise, in words that do not match question
  7's subject.
- **The second check's:** "You can answer in any way you choose, at any length, or decline to
  answer. Whatever you send will be saved as it is." It names no way out except declining. **As
  written it says "at any length", the sentence already removed as untrue** (first check M2). If
  chosen, it would read "You can answer in any way you choose, short or long, or decline to
  answer," and the note's "Your answer can be short or long." would go.

**Cost.** The project's care rule asks that the model be told it may reject the question. The
first check's wording still tells it so; the second check's leaves that to "in any way you
choose", which honours the rule less plainly, as the second check says itself.

**Recommendation: the first check's wording.** Confidence: moderate. It answers both findings and
keeps the care rule in words.

## 8. Question 10's doubled "from"

**Now.** "...from what you learned from or from anywhere else?"

**Proposed by the second check (N8).** "...from what you learned, or from anywhere else?"

**Why.** It reads cleanly.

**Cost.** It changes a little what is asked: "what you learned from" asks about sources; "what
you learned" asks about what was learned. That is why it is here and not applied. A version that
keeps the sense: "...from anything you learned from, or from anywhere else?"

**Recommendation: the version that keeps the sense.** Confidence: moderate; the change is small
either way.

## Not wording, but raised by the checks and John's to rule

- **Who may compare the answers, and how.** The note tells every model the answers are kept "so
  that the answers can be compared as models change over the years", and the method says no
  session opens a reply until John rules who may read them. Both checks (first S10, second N6)
  say the comparison needs an owner, or the note's stated purpose has none. `method.md` now says
  the comparison is what the record is for and that who makes it waits for this ruling.
- **The withdrawal sentence.** Whether the note should tell the model it is about to be
  withdrawn is already put to John in `questions.md`. Both checks add a point: Anthropic tells
  its own models about retirement in its retirement interviews, so a Claude model asked by both
  will meet the subject either way (first check N10, second check N7).
- **One question carries the founding question.** John's question of 2026-11-17, what a machine
  mind "would want to improve about its ability to more deeply explore the universe over a
  longer time period", is carried by question 5 alone (second check N10). Both checks judge that
  right for a record; it is worth knowing.
