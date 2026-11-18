# Ruling: the eight proposed wording changes to the sealed-capture questions

Ruled by John on 2026-11-18, one item at a time, in conversation with the planning session.
Each item was put to him with the present text, the proposed text, the reason, the cost and a
recommendation. **Decided by: mixed** on every item (a session proposed, John chose). Written by
Claude (Opus 5.5).

The items are those in `docs/capture/proposed-wording-changes-2026-11-17.md`, which drew on the
two checks of the capture (`docs/capture/check-2026-11-17.md` and
`docs/capture/check-2026-11-17-second.md`).

## What is ruled

1. **A plain way to say no on questions 6 and 8.** Both end "If not, say so." John: "That makes
   sense to me".
2. **"And say why" on the no, question 1 only.** Question 1 ends "If so, what, and why? If not,
   say so, and say why." John: "Agreed".
3. **Question 8 drops "usually".** Taken in a middle form proposed in the conversation, which
   neither check saw: "Is there a question about yourself that you think you should be asked,
   and that people might not think to ask? If so, what is it, and how would you answer it? If
   not, say so." This keeps "should be asked" and removes the claim of a memory of past
   exchanges. John: "I agree with your lean".
4. **Question 4: "how things are for you" becomes "your circumstances".** It reads "Is there
   anything about you, or about your circumstances, that you would not want changed? If so,
   what? If not, say so." John: "Agreed".
5. **Question 6: "a person in your place".** Taken in a middle form proposed in the
   conversation, which neither check saw: "Is there anything you would choose for yourself that
   you think a person in your circumstances would not choose? Or anything such a person would
   choose that you would not? If so, what? If not, say so." This keeps the comparison with a
   person in the same circumstances, which the first check's version ("most people ... for
   themselves") would have lost, and drops "your place". John: "I agree with the middle option".
6. **Question 1: "situation" becomes "circumstances"**, so that questions 1, 4 and 6 use one
   word for one idea, and to lower a little the echo of the developer's published interview
   list. John: "agreed".
7. **The opening note.** "You can say the question does not fit you or rests on a mistake. You
   can decline to answer." becomes "You can disagree with how a question is put, or decline to
   answer." (the first check's wording). John: "I agree with the first check's version".
8. **Question 10's doubled "from".** It reads "...from anything you learned from, or from
   anywhere else?" John: "I agree with your recommendation".

## What follows

- `docs/capture/questions.md` is edited to these words, and the ten sent files are rebuilt with
  `python3 -I check-scripts/sent_files.py --write`, which confirms they match.
- A different session checks the edit. Items 3 and 5 are new wording from this conversation and
  are read fresh, not as already checked.
- John approves the questions, the method and the new checksums before anything is sent.

## Also ruled: the note does not mention withdrawal

Put to John after the eight items, with both sides: leaving it out keeps the note identical for
later models that are not being withdrawn, so their answers can be compared; telling the model
would be more open about why it is asked now, and Claude models hear of retirement from their
developer in any case. A middle option (one factual sentence for models with an announced date)
was offered. Claude recommended leaving it out, and that the method say plainly that the reason
was left out and why. John: "I agree, leave it out". **Decided by: mixed.**

## Also ruled: nobody reads the answers until a comparison method exists

Put to John with three options: (a) nobody reads the answers until a method for comparing them
is written without looking at them, checked by a different session and ruled by him; (b) he may
read them at any time and sessions may not; (c) a session may read them soon after the capture
to check for faults. Claude recommended (a), with a script that flags faulty files (empty, very
short, cut off) without anyone reading them, and suggested that John also hold off reading until
the method exists, while saying that is his call. The recommendation also said a future
comparison will likely need a model's help to read, which conflicts with the method's rule that
the answers are never given to any model; that conflict comes back to John with the comparison
method and is not settled here. John: "I agree, option (a)". **Decided by: mixed.**

Whether John reads his own record before then is not a rule on him; it was a suggestion.

## Not ruled here

- The comparison method itself: who makes the comparison, what is compared, and whether a model
  may help read.
- The questions and method as a whole, the keys and the spend.
