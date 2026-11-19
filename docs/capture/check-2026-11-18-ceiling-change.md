# The sealed capture: a check of the change of ceiling

Written 2026-11-19 by Claude (Fable 5.2), an AI model, in the session that wrote the three
earlier checks of the capture script. The file name carries 2026-11-18 because that is the day
of the ruling and of the change checked. This is a check by a session that did not write the
change.

John ruled the ceiling for the Anthropic run at 10 dollars in place of 5 ("Yes, $10"; decided
by: mixed; `docs/rulings/2026-11-18-anthropic-ceiling.md`, commit c9d5f90, the ruling). The
script's author then made commit a57a212 (the plan, the rehearsal, the README and the
rehearsal's result). I checked the difference in `capture/` and in the message files between
commit 3dda42d (the script as my third check read it) and commit a57a212.

I changed nothing in `capture/` and nothing in any other session's file. No model and no
service's programming interface was called. I did not run `capture.py run`. No key was handled
and nothing was spent. Every reply and every spending record in my tests is constructed, and
all of them were written in a scratch folder outside the repository and then deleted.

## Verdict

**The Anthropic run: yes, still. Nothing must be fixed, and nothing should be fixed first.**
The third check's yes stands at the 10 dollar ceiling. Google and OpenAI are still not ready,
for the reasons the earlier checks give.

There are four notes at the end. One is a set of sums in the README that come out about 70
cents low. The README's conclusions from those sums are right.

## 1. The script and the message files

Unchanged to the byte.

- `capture/capture.py` is the same stored object in both commits (git object 156d150), and its
  SHA-256 checksum is 2c38f8af…909e4 in both, the figure my third check recorded.
- The folder `docs/capture/sent/` (the ten message files, `SHA256SUMS` and its README) is the
  same stored tree in both commits (git object 4877609). The ten files also match
  `SHA256SUMS` when checked now.
- The only commits that touch `capture/` or the message files after 3dda42d are b0c5bf7 (the
  rehearsal's result, which the third check covered) and a57a212.

## 2. The plan

One figure changed: the Anthropic run's `ceiling_usd`, from "5.00" to "10.00". The only other
change is the comment above it, which now records John's ruling in his words and says the
ruling "sets the limit and is not his go to spend". That is accurate.

The other three ceilings are untouched (Google 10.00, OpenAI's models due 2026-12-11 15.00,
OpenAI's models due 2027-01-14 10.00), and the comment still calls them proposed. No price,
day, model name, length limit or estimate changed.

## 3. The rehearsal

**It passes and matches.** Run by me: 299 checks, none failed, nothing on the error stream.
Its output is the same as the committed `capture/rehearsal-result.txt` line for line, apart
from the name of the temporary folder and the date in the last line (mine says 2026-11-19).
The committed last line names the checksums of the script and the plan as they now stand.
The `show` command, which sends nothing, passes every start check on the real repository
except the two that should fail today: there is no go from John, and no key is set.

**No check was dropped, weakened or loosened.** Against the result my third check read, the
299 check lines are the same 299, and the only differences are figures in their wording ($5
to $10, $50 to $100, $5,000 and $5k to $10,000 and $10k) and three counts of files and lines
at the end, which rose because some constructed runs now go further before stopping. Every
change in `rehearsal.py` is one of three kinds: a figure in a label, a constructed go reworded
from 5 to 10 dollars with its near-miss scaled the same way, and the string the rehearsal
swaps out when it builds a plan with a different constructed ceiling.

**The one case now run at a constructed ceiling of 5 dollars is an honest way to keep it.**
The case is the reply cut off at the length limit: one question cut off once, one cut off
twice. Its first round is counted at $1.46, so five rounds come to $7.28. At 5 dollars the
first-round rule stops the run there; at 10 dollars it does not. I ran the case both ways:

- At the constructed 5 dollars: 12 calls, then "stopped after the first round".
- At the plan's own 10 dollars: the run goes on to the end, 52 calls, $1.52 counted. The
  cut-off behaviour is the same (cut off at 32,000, asked once more at 64,000, kept, and no
  third asking). Two of the case's checks then fail, and only because of how they are
  written: one expects the stop, and the other counts the calls for a question across the
  whole run, which holds only if the run ends after round one.

So the case needs a run that stops after round one, and the comment in the rehearsal and the
check's own label both say the ceiling is constructed. Nothing is hidden by it. What the case
tests (what the script does with a cut-off reply) does not depend on the ceiling.

**The behaviour at 10 dollars is tested.** Three places test the plan's own figure: the case
with replies of 20,000 tokens (first round $3.01, five rounds about $15, stopped at 10
dollars), the `show` case (which must print "ceiling $10.0000"), and the three refusals of a
go that does not equal the plan's 10 dollars. Every ordinary case in the rehearsal also now
runs at 10 dollars and must finish all five rounds.

**Broken copies.** I ran the rehearsal against nine copies of the script, each broken on
purpose in the money rules or the go, and one copy of the rehearsal changed to run the
cut-off case at 10 dollars. Eight of the nine broken scripts were caught:

| Broken on purpose | Caught |
|---|---|
| The first-round rule never stops a run | yes |
| The first round is multiplied by one, not five | yes |
| The first round is multiplied by three | yes |
| The first round is multiplied by four | no |
| The first-round rule compares against twice the ceiling | yes |
| The check before each call allows twice the ceiling | yes |
| A go for less than the plan's ceiling passes | yes |
| A go for more than the plan's ceiling passes | yes |
| The figure in John's words need not equal the figure in the block | no |

Neither miss is new. The rehearsal never had a case that sits between four rounds and five,
at 5 dollars or at 10, and never had a go whose words carry one figure and whose block carries
another. My own test in section 5 shows the script refuses that second one. Both are in the
notes.

## 4. The README's sums

**The conclusions are right. The figures are about 70 cents low.**

The README says three broken streams in round one give 5 x (1.44 + 0.18) = $8.10 and the run
goes on, and four give 5 x (1.92 + 0.15) = $10.35 and the run stops. Its arithmetic is right
for the numbers it uses. Two things are left out of those numbers:

- A broken stream is asked once more, and that second reply is also in round one. So all ten
  questions add an ordinary reply to the round, not seven or six of them.
- An ordinary reply of the size the cost document expects (2,000 tokens) is counted at $0.031,
  and a broken stream at $0.4824.

I ran the script's own counting against constructed replies of 2,000 tokens, with the plan as
it stands:

| Broken streams in round one | Round one counted | Five rounds | At 10 dollars |
|---|---|---|---|
| 0 | $0.31 | $1.53 | goes on |
| 1 | $0.79 | $3.94 | goes on |
| 2 | $1.27 | $6.36 | goes on |
| 3 | $1.75 | $8.77 | goes on |
| 4 | $2.24 | $11.18 | stops for good |
| 5 | $2.72 | $13.59 | stops for good |

So: **three broken streams do not stop it, and four do**, as the README says. The README's
$8.10 should read $8.77, its $10.35 should read $11.18, and its figure for two breaks at the
old 5 dollars ($5.80) should read $6.36. The README's other figures are right: the script
needs about $1.44 of room before a first asking ($1.4448 exactly), so it stops asking once
about $8.56 is counted. With every reply a broken stream, my test run made 18 calls and
stopped with $8.68 counted, before the call that could pass 10 dollars.

One thing the corrected sum shows that the README does not say: with three breaks there is
$1.23 of room left under the rule, not $1.90. If the ordinary replies average more than about
3,600 tokens (about 2,700 words), three breaks would stop the run. With no breaks at all the
rule stops the run only if replies average more than about 13,000 tokens.

The README's lines about Ctrl-C and a sleeping Mac now say four calls counted at the most "can
end the run". That is right.

## 5. What go would be accepted

With the plan at 10.00, tested against constructed spending records in a scratch folder (the
real `docs/spending-record.md` does not exist and was not made):

**Accepted**

- A block with `ceiling_usd = "10.00"`, the words "Anthropic, up to $10", under a constructed
  quotation ending "Anthropic, up to $10." This is the form the README offers.
- The same with "$10.00" in the words, and the same with `ceiling_usd = "10"` in the block.

**Refused**

| The go | Why the script refuses |
|---|---|
| Block 5.00, words "Anthropic, up to $5" | the plan's ceiling and the go's figure "must be equal" |
| Block 10.00, words "Anthropic, up to $5" | the words do not carry the figure $10 |
| Block 100.00, words "Anthropic, up to $100" | must be equal |
| Block 10.00, words "Anthropic, up to $100" | the words do not carry the figure $10 |
| Block 10.00, words "up to $10", quotation says $100 | not quoted word for word |
| Block 10.50, words "Anthropic, up to $10.50" | must be equal |
| Block 10.00, words "Anthropic, up to $10.50" | the words do not carry the figure $10 |
| Block 10.00, words "up to $10", quotation says $10.50 | not quoted word for word |
| Block 10.00, words "up to $10", quotation says $10,000, $10k or $1000 | not quoted word for word |
| Block 10.00, words "Anthropic, up to $10 or $5" | the words must carry only that figure |
| Block 10.00, words "Google, up to $10" | the words do not name the developer |
| Block 10.00, words "Anthropic, up to 10 dollars" | no figure with a dollar sign |

So a go reading "Anthropic, up to $10" is accepted, and "$5", "$100" and "$10.50" are each
refused whichever way they are written into the record. John's go must carry the figure with
a dollar sign: "ten dollars" or "10 dollars" is refused.

## 6. Notes

None of these needs fixing before the Anthropic run.

1. **The README's three sums are low** (section 4): $8.10, $10.35 and $5.80 should read $8.77,
   $11.18 and $6.36. Changing the README does not change the script or the plan, so the
   rehearsal's result stays good. The README is not one of the files the script requires to
   be committed and unchanged, but it lives in `capture/`, so the change is the author's.
2. **A comment inside `capture.py` still shows a go for 5 dollars** (line 431, in the
   description of the go check). It is an example in a comment and changes nothing. Leaving
   it is right: touching the script would mean the rehearsal again and another check.
3. **Two gaps in the rehearsal, neither new:** no case tells a multiplier of four from five in
   the first-round rule, and no case has a go whose words and block carry different figures.
   The script does both correctly (sections 4 and 5).
4. **The step list and the cost document still carry 5 dollar lines.** The documents session
   is correcting them and they are not part of this check. They must be committed before the
   day of the run, because the script refuses to start if either file differs from its
   committed copy.

## What John's go should now name

The figure is $10, with the dollar sign, and the developer's name, Anthropic. The commit is
the latest one in the repository when he gives the go, after the documents' corrections are
committed. Before giving him that id, a session confirms that the last commit to touch
`capture/` or the message files is still a57a212 (or a later one that changes only the README,
if note 1 is acted on), and that `show` passes every check except the go and the key.
