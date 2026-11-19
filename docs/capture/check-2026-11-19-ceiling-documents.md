# Check of the documents' change after the ruling on the Anthropic ceiling

Written on 2026-11-19 by Claude (Fable 5.2), an AI model, in a session that wrote none of the
work checked. It checks one commit, bb559ce ("Capture step list and cost table: the Anthropic
ceiling is 10 dollars as John ruled, and the ruling is not his go"), which changed
`what-john-needs-to-do.md` and `cost-and-terms.md`. This session fixed nothing. No model was
asked anything, no key was handled, nothing was spent, and `docs/spending-record.md`, which
does not exist yet, was not read or written.

## Verdict

**The commit does what the ruling asked. Nothing must be fixed.** Every place that states the
Anthropic ceiling now says $10, as ruled, with the ruling file named, and none says or implies
that the ruling is John's go to spend. The other three ceilings are still shown as proposed.
The sums hold. The example go is the form the script accepts.

Counts: 0 must fix, 3 should fix, 6 notes.

The ruling is `docs/rulings/2026-11-18-anthropic-ceiling.md` ("Yes, $10"; decided by: mixed).
A ceiling is the most a run may cost before the script stops itself.

## The six things asked

### 1. Every place says $10, ruled, with the ruling named, and none says it is the go

Passes. The places, by line in the files as committed:

| File | Lines | What it says now |
|---|---|---|
| The step list (`what-john-needs-to-do.md`) | 23 to 31 | A status paragraph at the top: ruled at $10, the ruling named, "It is not your go to spend" |
| The step list | 233 to 239 | Under step 7's sentence on the proposed ceilings: ruled at $10, the ruling named, not the go |
| The step list | 244 to 246 | The example go, see item 4 |
| The step list | 266 to 271 | The figure in the script's plan: $10.00 in place of $5 |
| The step list | 285 to 293 | The sums for $10, the ruling named, not the go |
| The step list | 420 to 422, 427 to 429 | "While it runs": the lid and Ctrl-C, both at "the ruled ceiling of $10" |
| The step list | 464 to 469, 603 to 616 | The earlier words kept, and the table of what changed |
| The cost document (`cost-and-terms.md`) | 90 | The Anthropic row: $5 struck through, "$10, ruled 2026-11-18" |
| The cost document | 97 to 103, 346 to 353 | A note under the table and a table of what changed, the ruling named, not the go |

Two sentences still give $5 for the Anthropic run as the present figure, at lines 230 and 280
of the step list. Both are earlier words left in place, and each has its dated correction
directly beneath it, which is the document's habit.

The statement that the ruling is not the go appears six times across the two files. Each agrees
with the ruling's own section "Not covered by this ruling". One phrase beside it could be read
loosely, should-fix 3 below.

### 2. The other three ceilings and the Google prepayment lines

Passes. Google $10, OpenAI $15 and OpenAI $10 are called proposed in every place that names
them (the step list, lines 29 and 238 to 239; the cost document, lines 91 to 93 and 102).
The lines on Google's $5 prepayment (the step list, lines 185 and 188; the cost document, line
129) are not in the commit's difference, and read as before.

### 3. The sums

Passes, with one refinement, should-fix 1. Worked by this session from `capture/plan.toml`, the
ten message files' sizes, and the two formulas in `capture/capture.py` (the most a call could
cost; the first round times five).

| Figure | The documents say | This session's sum |
|---|---|---|
| The plan's ceilings | $10, $10, $15, $10 | 10.00, 10.00, 15.00, 10.00 |
| Their total | $45 | $45.00 |
| The estimate, and with one fifth added | $1.58, $1.89 | $1.575, $1.89 |
| The most one uncounted call is counted at | $0.48 | $0.4825 to $0.4829 for questions 1 to 9, $0.4886 for question 10 |
| One reply of the expected size | "about three cents" in the README; the sums use two and a half | $0.0315 |
| Two breaks in the first round, times five | $5.80 | $6.08 to $6.12 |
| Three breaks | $8.10, goes on at $10 | $8.34 to $8.37, goes on |
| Four breaks | $10.35, stops at $10 | $10.60 to $10.63, stops |
| Room needed before a first asking (the README only) | about $1.44 | $1.457 for question 10 |

The documents' figures are the README's, copied correctly, and the README's are rounded: $0.48
flat for an uncounted call, and about two and a half cents for a reply. With the plan's own
figures each total is about 25 cents higher. The conclusions do not change: at $10 the run
goes on after three broken connections in the first round and stops at four, and at $5 two
were enough.

### 4. The example go

Passes. The check of the go in `capture/capture.py` (the function `check_go`) asks that the
words sit word for word in the quotation directly above their block, name the developer, and
carry exactly one figure with a dollar sign, equal to the block's figure, which must equal the
plan's. For a developer with one run it asks for no date.

This session also ran that function on records it made up in its scratch folder, each marked
"constructed", with made-up quotations. The real spending record was not involved.

| Constructed words | Result |
|---|---|
| "Anthropic, up to $10" | passes |
| "Anthropic, up to $10.00" | passes |
| "Anthropic, up to $5", block at 5.00 | refused: the plan's ceiling and the go must be equal |
| "Anthropic, up to $5", block at 10.00 | refused: the words do not carry the figure |
| "Anthropic, up to 10 dollars" | refused: no figure with a dollar sign |
| "Anthropic, up to $10, not $5" | refused: two figures |
| "Yes, $10" | refused: the words do not name the developer |

So the step list's three statements are right: "Anthropic, up to $10" passes, "Anthropic, up to
$5" is now refused because the figure must equal the plan's, and "Anthropic, up to 5 dollars"
is refused. The last row confirms by program what the ruling says in words: the answer "Yes,
$10" cannot serve as the go.

### 5. Form, and what else changed

Passes. Each change is a dated correction beside the earlier words, or strikes them through
(the example go, the plan's figure, the table's cell). The two points under "While it runs"
were rewritten in place, and their earlier words are quoted in full under "Earlier wording of
the run's step list", which is how that list has been kept since it was written out clean.

The commit touches the two documents and nothing else. The ten message files match the ten
checksums in `sent/SHA256SUMS` (checked with `shasum`), and neither they nor `method.md` have
changed since before this commit. The two checks the script makes against these documents (each
last safe day against the step list's table, each price against the cost document's table)
were run by calling them directly, and both still pass.

### 6. Plain language

Passes. The added lines hold no long dash, no month name, no slash date and no relative date.
The one commit id (a57a212) carries a plain phrase, "the script's plan was changed to $10.00
and its rehearsal run again". One added line is 102 characters, two over the file's usual
width.

## Should fix

1. **"Goes on after three, and four end it" is true for replies of the expected size, and the
   run's list says it without that condition** (the step list, lines 420 to 422 and 427 to 429;
   also line 281). The second half of the sum is what the replies that did arrive cost, and
   that is not known until the day. By the plan's figures:
   - after three breaks the run goes on only if the seven replies that arrived average under
     about $0.079 each, which is about 5,000 tokens of reply, two and a half times the estimate
     of 2,000;
   - four breaks alone come to 5 x $1.93 = $9.65, which is under $10. They stop the run only
     if the six replies that arrived cost more than about 7 cents together, and at the expected
     size they cost about 19.

   So long replies can make three breaks enough to stop the run, and very short ones can let it
   go on after four. The first of those is the one that matters to John on the day. Suggested:
   add "if the replies are about the size expected" to the two points under "While it runs",
   and one sentence under step 7's sums saying that longer replies leave less room.

2. **The cost table's row "All four" still shows $40 in bold** (the cost document, line 94).
   The note under the table says the four now come to $45, but a reader of the table alone
   sees $40. The row above was corrected in its cell. Suggested: the same here, $40 struck
   through and $45 beside it, with a word that $45 is one ruled figure and three proposed.

3. **"Naming that figure is done"** (the step list, lines 26 to 27, and again at 235 to 236).
   The figure is chosen, but John's go must still carry it: "Yes, $10" is refused by the
   script, and "Anthropic, up to $10" is what passes. Lines 236 to 238 say so. The status
   paragraph at the top does not, and a reader who stops there could take it that he need not
   say the figure again. Suggested: "choosing that figure is done; your go must still say it".

## Notes

1. **The date on the corrections.** They are dated 2026-11-18, the day of the ruling, and so
   is the commit's title. The commit was made on 2026-11-19 at 06:35 Pacific time. This session
   cannot tell on which day the words were written. If it was the 19th, the corrections' date
   should say so.
2. **The script's own notes still show the old example.** The explanation above `check_go` in
   `capture/capture.py` gives "Anthropic, up to $5" and a block at 5.00 as its example of the
   form. It is an example and changes nothing the script does. It is outside this commit, and
   is the script session's to change.
3. **The step list adds a reading of its own, and says so.** Lines 269 to 271 say a figure
   other than $10 for Anthropic would need a new ruling first, "this session's reading of the
   ruling, which does not say so itself". That is labelled honestly. It is John's to confirm.
4. **An earlier view still says $5.** The master session's first view
   (`docs/reviews/2026-11-18-fable-view-on-the-waiting-questions.md`, line 132) agrees with
   $5. It is a record of what was thought before the ruling, and the ruling cites it as such.
5. **The table's column is still headed "Proposed ceiling"** while one cell in it is ruled.
   The cell says so itself.
6. **What was not done.** The script's command that shows a run before it happens was not
   run, because it reads the spending record. Its two checks that read only these documents
   were run directly, as said under item 5.
