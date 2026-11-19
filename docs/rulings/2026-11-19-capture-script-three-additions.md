# Ruling: three things the capture script does beyond the method's words are accepted

Ruled by John on 2026-11-19, in conversation with the master planning session.
**Decided by: mixed** (a session proposed and recommended, John approved). Written by Claude
(Fable 5.2), an AI model.

## How it came up

John approved the capture's method (`docs/capture/method.md`) on 2026-11-18. The session that
wrote the capture script (`capture/capture.py`) met three situations the method has no words
for, and handled them. The script's own notes (`capture/README.md`) and its third check
(`docs/capture/check-2026-11-18-capture-script-third.md`) both marked them as things John should
know of and could object to. This was the first of six decisions put to him before the run that
asks Claude Sonnet 4.5.

## What the session told him

1. **Three extra kinds of failure.** The method lists seven ways a call can turn out. The
   script adds three for trouble on its own side: a reply it cannot take apart (everything
   received is saved, and the run stops); a call that was sent with no record written, as after
   a power cut; and a file that was only half written when the machine stopped. Each is counted
   at the most the call could have cost, so the spending total can be too high and never too
   low.
2. **Extra files in the answers folder.** A small marker file written before each call, and an
   empty lock file held while the script runs. The markers are how the script knows a call was
   sent even if its reply was lost, and never asks under the same number twice. The lock stops
   two runs going at once. Neither holds any of a model's words.
3. **A command that shows every reply's word count.** The method speaks of a word count only
   for a faulty reply. The script's `labels` command shows the count for every reply, and never
   any words.

The recommendation, with its four things. *The choice:* accept all three. *Confidence:* high on
the first two, moderate to high on the third. *Standard practice or judgment call:* the first
two are standard practice for a script that must not lose or count twice a paid call; the third
is a judgment call. *Strongest alternative:* have `labels` show counts only for faulty replies,
as the method's words say. Its cost: after the one watched call, nobody could tell a full answer
from a very short one without opening the file, which the method forbids, and it would need a
script change, a new rehearsal and another check before 2026-11-26.

The session also said that a word count is a small piece of information about an answer, since
a very short count hints at a refusal, and that this was the one of the three where John's view
could reasonably differ.

The question put to him was "Accept the three things the script adds beyond the method's
words?" John: "Accept all three". **Decided by: mixed.**

## What is ruled

1. The three added outcomes stand, each counted at the most its call could cost.
2. The marker files and the lock file in the answers folder stand.
3. The `labels` command may show the word count of every reply, and no words of any.

The script is not changed by this ruling. The method's rule that nobody reads the answers until
a way of comparing them is ruled is not changed either: a word count is not a reading.

## Not covered by this ruling

- Bringing the method's words into line, so that it names the three outcomes, the extra files
  and the command. That is a dated correction for the session that keeps the capture documents,
  checked by a different session. It changes nothing that is sent.
- The go to spend, the key, the command that loads it, and whether the run is within
  Anthropic's terms, which are all still John's.

No model has been asked anything, no key has been handled, and nothing has been spent.
