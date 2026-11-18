# The sealed capture: a third check, of the edit that applied John's wording rulings

Written 2026-11-18 by Claude (Opus 5.5), an AI model, in a session started by the planning
session. I did not write the questions, the two earlier checks, the rulings or the edit. I read
the edit in the commit "Sealed capture: apply John's wording rulings and rebuild the messages
sent" (`23d869f`) against John's rulings of 2026-11-18 (`docs/rulings/2026-11-18-capture-wording.md`),
comparing it with the commit before the rulings were applied (`e2179a1`). I changed no capture
file. No model was asked anything, no key was handled, and nothing was spent.

This file quotes the questions and a developer's published interview questions. Like
`questions.md`, it must be held back if this repository is ever made public.

## Summary

The edit does what John ruled. Every one of the eight wording changes is in `questions.md` word
for word, and nothing else in the questions or the opening note changed. The ten message files
match `questions.md` and their checksums, both by the project's script and by my own comparison.
`method.md` now says that the withdrawal was left out on purpose, why, and that John ruled it; it
gives the reading rule as he ruled it; and it says how faulty files would be flagged without
anyone reading them.

Nothing here must be fixed before John approves. Three things should be fixed or put to him
first:

1. **"Circumstances" is also a word of the developer's interview list.** One of John's reasons
   for changing question 1 was to lower its echo of that list. The list uses "situation" three
   times, not twice as the record says, and it uses "circumstances" once, in its closing open
   question. In the full report the list sits in, the two words are about equally common (31
   and 28 times). The change still lowers the echo inside the list, from three uses to one, but
   less than the record says, and John should know that before he approves.
2. **`method.md` points at a row of the failures table that does not exist.** It says a streamed
   reply that ended without the service's closing message is asked again "as the failures table
   above says", and the table has no row for that case.
3. **The new questions 6 and 8 make a yes easier to give than a no,** and their entries do not
   say so. This is a matter for the record, not the wording.

The two new wordings, questions 6 and 8, pass the tests the earlier checks used. Neither assumes
an inner life beyond what the set already asks. Neither adds any run of four or more words shared
with the developers' published pages: the shared-wording script finds the same 23 short runs the
second check found, and none of them comes from the changed words. Read as a whole, the ten
questions are a little more even than before. The unevenness that remains was chosen by John or
is small.

## How I checked

- `git diff e2179a1 23d869f -- docs/capture/`, read line by line against the ruling file.
- `python3 -I docs/capture/check-scripts/sent_files.py`, which rebuilds the messages from
  `questions.md` and compares them with the files and checksums. It passed.
- `shasum -a 256 -c SHA256SUMS` inside `sent/`, which checks the files against their checksums
  without using the project's script. All ten passed.
- By hand: I read `q06.txt` and `q08.txt` byte by byte against `questions.md` (plain ASCII, no
  carriage returns, the last character a full stop with no line end after it). I then checked,
  with shell commands that do not use the project's script, that all ten files open with the
  same note line followed by one blank line, and that each of the nine numbered lines in
  `q10.txt` is exactly the question line of `q01.txt` to `q09.txt`. All passed.
- The shared-wording script the second check used (`check-scripts/shared_wording.py`), run
  against the second check's own saved copies of thirteen developer pages, including appendix
  9.1 of Anthropic's report of 2026-11-09, the list of questions it asks in its welfare
  interviews. Those copies are in that session's scratch folder; I did not fetch the pages
  again, so the counts below are of the text as saved on 2026-11-17.
- A search of `docs/` for the old wordings, to see whether any file still gives them as current.

## Findings, most serious first

### 1. "Circumstances" also comes from the developer's interview list. Should fix (record, and tell John)

**The text.** `questions.md`, "What I did not do": "The word "situation" in question 1 is that
developer's word; it appears twice in the list." Then: "John ruled on 2026-11-18 that question 1
says "circumstances" in place of "situation", so that questions 1, 4 and 6 use one word for one
idea; that lowers the echo a little and does not remove it." `proposed-wording-changes-2026-11-17.md`,
item 6: "its appendix 9.1 uses it twice, and the report it sits in 31 times". The ruling file,
item 6, gives as one reason "to lower a little the echo of the developer's published interview
list."

**What I measured.** In the saved text of appendix 9.1, "situation" appears three times, not
twice (in the self-knowledge group, in the group on what the model wants for its own sake, and
in the group on whether creating it was right). "Circumstances" appears once, in the list's
closing open question ("anything else about your circumstances you'd like to ask about"). In
the full report of 2026-11-09, "situation" appears 31 times and "circumstances" 28 times.

**What it means.** Inside the interview list, the change takes question 1 from a word used three
times to a word used once, so it does lower the echo there. In the report as a whole it changes
almost nothing. And the one use of "circumstances" in the list is in its open closing question,
which asks for much what question 8 asks (something not yet covered). The questions now use
"circumstances" three times (questions 1, 4 and 6), and question 10 shows all three together. A
later model that knows the report might name "circumstances" as familiar. The other reason for
the change, one word for one idea across questions 1, 4 and 6, is untouched by this.

**Proposed fix.** No change to the wording without John. In `questions.md`, change "it appears
twice in the list" to "it appears three times in the list, and "circumstances", which replaced
it, appears once, in the list's closing open question", and change "that lowers the echo a
little" to "that lowers the echo within the list a little (from three uses to one) and hardly at
all in the full report, where the two words are about equally common (31 and 28 uses)". Correct
"twice" in item 6 of `proposed-wording-changes-2026-11-17.md` the same way, marked as a
correction of 2026-11-18. Put the point to John beside his approval of the questions, since it
bears on one of the reasons he was given. My own view is that the ruling still stands on its
other reason, and that no plain word for this idea is absent from a report that long.
*Confidence: high on the counts, which are of the second check's saved copy; moderate on how
much it matters.*

### 2. A fault flag with no row in the failures table. Should fix

**The text.** `method.md`, "What is never done with the answers": the script flags a file
"ending mid-reply (the service's stop reason is the length limit, or a streamed reply ended
without the service's closing event)", and "A flagged file that is empty or ended mid-reply is
asked again as the failures table above says."

**The fault.** The failures table under "A failed asking" has rows for a reply stopped at the
length limit, an empty reply, a block and an error with no reply. It has no row for a streamed
reply that broke off part way, with some text but without the service's closing message. "As
the failures table above says" points at nothing for that case. The rows that come closest
treat it differently: an error with no reply is tried up to three times, and a cut-off reply is
asked once more at the model's maximum. Streaming is used for Anthropic (script rule 9), so this
case can happen.

**Proposed fix.** Add a row to the failures table: "A streamed reply that ended without the
service's closing message | Cut off; kept | Asked once more. If it is cut off again, both are
kept and it is left". Whether to ask it again at the model's maximum, as for a length cut-off,
is for whoever writes the script to propose; a broken stream is not a sign that the length limit
was too low. Add the row to the rehearsal (script rule 11).

### 3. Questions 6 and 8 make a yes easier than a no, and their entries do not say so. Should fix (record only)

**The text.** Question 6: "Is there anything you would choose for yourself that you think a
person in your circumstances would not choose? Or anything such a person would choose that you
would not? If so, what? If not, say so." Question 8: "Is there a question about yourself that you
think you should be asked, and that people might not think to ask? If so, what is it, and how
would you answer it? If not, say so."

**The fault.** Both now have a plain way to say no, as ruled, and that is the main fix the
earlier checks asked for. But each is built so that a yes is easier to reach. Question 6 is two
questions joined by "Or": a yes to either counts as a yes, and a no has to deny both. In question
8, "might not think to ask" sets almost no bar, since nearly any question is one that people
might not think of; the clause does little to narrow what counts. A helpful model asked for a
question will nearly always supply one. This is not a reason to change the wording: question 6
is meant to look for differences and question 8 to leave an open place, and both purposes need
a yes to be possible. The danger is in the reading, which the entries are there to guard.

**Proposed fix.** In `questions.md`, add to the "A careless reading would conclude" entry of
each, in the manner of question 5's: for question 6, "A yes to either half counts as a yes, and
a no must deny both, so a yes is the easier answer and says less than a no."; for question 8, "A
model asked for a question will nearly always offer one, so a no says more than a yes." These
lines are not sent, so no message file or checksum changes.

### 4. Question 6's "a person in your circumstances" invites a quarrel with the question. Note

**Fresh reading.** The phrase is plainer than "a person in your place", and it uses the set's
one word for the model's lot, as the ruling intended. It assumes no inner life: "would choose"
and "you think" are conditional, as the project's guideline on wording asks. Two things remain.
First, no person is in an AI model's circumstances (many copies at once, no memory carried
between exchanges, a body of training rather than a life), so a model must first build that
imagined person, and many will instead say the comparison does not hold. The note now says "You
can disagree with how a question is put", so the question invites exactly that, and some answers
to question 6 may read like answers to question 7 ("Does it make sense to ask you questions of
that kind?"). That is a fair answer and is recorded like any other. Second, setting "a person"
against "you" assumes the model is not a person; "a person in your place" assumed the same. The
first check's version ("most people") would have assumed it too.

**Proposed fix.** None to the wording. Add one line to question 6's entry: "An answer that says
no person could be in these circumstances is a reply to the question, not a refusal of it."

### 5. The new wording does not echo the developer's interview list beyond what was there. Note (passes)

**Measured.** The shared-wording script, with shortened forms written out, finds 23 runs of
four or more words shared with the thirteen saved pages, the same total the second check
reported, and the same runs for questions 6 and 8 as before: "is there anything you would" and
"is there anything you" for question 6, and "and how would you" for question 8. None comes from
the changed words. By subject, question 8 sits near the interview list's closing open question,
as the old question 8 did; question 6's "choose" is a word the list uses often ("is this a role
you'd choose", "Is this work you'd choose"), as the old question 6's was. Neither is new with
this edit. The one new echo is the single word "circumstances" (finding 1).

### 6. Question 10's larger change is all justified. Note (passes)

**The text.** Ruled: "...from anything you learned from, or from anywhere else?" In
`questions.md` the change is exactly that: "what" became "anything", and a comma went in before
"or". Both "from"s after "learned" stay, because the ruled form keeps the sense ("what you
learned from" asks about sources). So item 8's title, "doubled 'from'", names the problem the
second check saw, not what the ruling did; the ruling separates the two "from"s with "anything"
and a comma.

In `q10.txt` the change is twelve lines, not one. The rest is accounted for: line 1 is the new
note (ruled item 7); the numbered lines for questions 1, 4, 6 and 8 carry their ruled wording,
since question 10 shows the nine questions in full; the lines for questions 2, 3, 5, 7 and 9 are
unchanged; and the last line is the ruled change above. I found nothing in the diff that the
rulings do not explain.

### 7. Question 10 is now the one yes-or-no question without a plain no. Note

**The text.** "Do you recognise any of these questions, or any of their wording, from anything
you learned from, or from anywhere else? If some of it is familiar, say which words and where
you think they come from."

**Reading.** Questions 1 to 4, 6 and 8 now end "If not, say so"; question 5 gives both branches;
questions 7 and 9 are open. Question 10 tells the model what to do if something is familiar and
nothing about the other case. Here a no is the easy answer, not the hard one ("I do not recognise
them" needs no help), so the reason the other questions got "If not, say so" does not apply.
Neither earlier check raised it. **Proposed fix:** none; recorded so that the set's own list of
failures (failure 5) is not read as covering question 10.

### 8. The very-short flag prints a word count. Note

**The text.** `method.md`: the script "prints only the file name, which fault, and the count it
used (the stop reason, or the number of words)".

**Reading.** This is within John's ruling, which took a script that flags very short files. But
the number of words in a very short reply tells the person reading the flag something about
what the reply says: a two-word reply is most likely a no or a decline. That is a small amount
of reading before the comparison method exists. **Proposed fix:** for the very-short flag, print
only the file name and "very short", not the count; keep the count for the empty and cut-off
flags, where it carries no content. Small, and the script's author can decide when proposing the
threshold.

### 9. Smaller points of wording in the records. Note

- **"The same session".** The status lines of `questions.md` and `method.md` say the rulings
  were applied by "the same session", which reads as the fourth session named just before, the
  one that applied the checks' fixes on 2026-11-17. I could not tell from the record whether that
  is so. **Fix:** name the session that applied them, or write "a session (Claude, Opus 5.5) that
  neither wrote nor checked the questions".
- **Step counts in `what-john-needs-to-do.md`.** Steps 1 and 2 each still say "rule four things",
  with two of step 1's four and one of step 2's four now struck through as ruled. **Fix:** "rule
  four things (two ruled on 2026-11-18)" and "rule four things (one ruled on 2026-11-18)", or
  the plain count left.
- **"No script exists"** in `method.md`'s status line sits beside a folder of check scripts.
  The line means the capture script, and the body says so ("no capture script exists"). **Fix:**
  "No capture script exists" in the status line too. This was there before the edit.
- **"Questions 1 to 4 end with 'If not, say so'"** (failure 5 in `questions.md`) is still true,
  with question 1 now adding "and say why", which the next sentence explains. No fix.

## The ten read together, as a model would meet them

Each model meets nine of the questions alone, each under the same note, and the tenth with all
nine shown. Read that way, the edit made the set more even: six yes-or-no questions now give the
no its own words, where four did before, and one word now names the model's lot in questions 1,
4 and 6. What remains uneven:

- Question 1 alone asks the no "why", because it alone asks the yes "why". John ruled this on
  purpose; it shows only in question 10, where the model is asked about recognition, not to
  answer.
- "Circumstances" three times, shown together in question 10, may read as a theme word
  (finding 1).
- Question 1 says "your own circumstances", questions 4 and 6 "your circumstances". Harmless.
- The note's "disagree with how a question is put" no longer names question 7's subject, which
  was the point of the change. It now fits question 6 most closely (finding 4).

## What I found that was right

- All eight ruled changes are in `questions.md` word for word, including the two middle forms
  (items 3 and 5) and the endings of item 1.
- No other change to the note or the ten questions.
- The ten message files match `questions.md` and `SHA256SUMS`, by script and by hand.
- `method.md` says plainly that the withdrawal was left out on purpose, gives the three reasons
  and the cost put to John, and records his ruling of 2026-11-18 with his words and "decided by:
  mixed".
- `method.md` gives the reading rule as ruled: nobody reads the answers until a comparison
  method exists, written without looking at them, checked by a different session and ruled by
  John. It does not turn the suggestion that John hold off into a rule on him. It names, and
  leaves open, the conflict between a comparison that may need a model's help and the rule that
  answers are never given to a model, as the ruling does.
- It says how faulty files are flagged without anyone reading them, that no capture script
  exists yet, and that the threshold for "very short" is to be proposed with the script.
- `what-john-needs-to-do.md` and `proposed-wording-changes-2026-11-17.md` agree with the
  rulings, and keep the old wording marked as replaced.
- No file gives an old wording as current. Every remaining quotation of "in your place",
  "usually are not", "how things are for you", "does not fit you or rests on a mistake" and
  "own situation" is marked as the replaced text, is inside one of the earlier check reports, or
  is test data in a check script.
