# Ruling: four points on how the capture script applies the method

Ruled by John on 2026-11-18, in conversation with the master planning session. **Decided by:
mixed** (sessions proposed, the planning session recommended, John approved). Written by Claude
(Fable 5.2), an AI model.

## What was put to him

A session wrote the capture script the method specifies (`capture/`), and a different session
checked it (`docs/capture/check-2026-11-18-capture-script.md`, commit 04cad04). The check found
two faults that must be fixed before any real run. The first: a few failed tries shut a model
out for the rest of the day even after the cause is fixed, so a key pasted wrongly on
2026-11-28 would end the capture for Claude Sonnet 4.5 with nothing asked. Its fix narrows how
a rule in the approved method is applied, so it needed John. The check also listed places where
the script departs from the method's words or settles what the method left to it.

The planning session put four points to him, each with its recommendation:

1. **A failure that retrying cannot cure stops the run without using up the day.** A wrong
   key, no credit or a wrong address stops the script with a line saying what to fix, and it
   can be run again the same day. Timeouts and an overloaded service keep the rule as the
   method has it. Built so that it can be switched off in one line. *Confidence:* high.
2. **The first Anthropic run happens by 2026-11-26, not on the last safe day.** Anthropic's
   own page says models close to withdrawal are likely to be less reliable, and two spare days
   cost nothing. *Confidence:* high.
3. **The key is read from a setting in John's shell, not from a file the script opens.** The
   method's words say "from its own file". The key still lives in its own file outside the
   repository, and the script never opens that file. The method needs a dated correction to
   match. *Confidence:* high.
4. **Two settings the method left to the script:** a reply of fewer than 20 words is listed as
   very short, and a second asking after a broken connection uses the same length limit. The
   check would approve both.

*Standard practice or judgment call:* judgment calls, all four. *Strongest alternative to all
four:* leave the method's words as approved and rely on running early, which needs no
correction to an approved document and leaves a mistyped key able to cost a whole day.

John: "Approve all four". **Decided by: mixed.**

## What is ruled

1. **The first row of the method's failures table is applied with one exception,** in the
   words the script's author wrote out for him to approve or refuse:

   > The first row of the failures table reads: "No reply: an error, a timeout, a rate limit
   > ... Tried again up to three times, a minute apart, then left for the next day." It is
   > applied with one exception. **An error that trying again cannot cure is not tried again
   > and is not one of the day's tries.** For Anthropic these are the service's statuses 400,
   > 401, 402, 403 and 404: a problem with the request, the key, billing, permission, or the
   > address. For OpenAI, 401 and 403. For Google, none, until a page confirms them for the
   > interface used. The attempt is kept as a failed attempt, with the error. The run stops
   > and says what to fix, and may be run again the same day. Every other failed attempt (a
   > timeout, a rate limit, a server error, an overloaded service, a connection that fails) is
   > tried again up to three times as before. The reason: four tries at an error of this kind
   > would use up the day, and on the last safe day that would end the capture for the model
   > with nothing asked. It can be turned off by one line in `capture/plan.toml`.

2. **The first Anthropic run is made no later than 2026-11-26.** The last safe day stays
   2026-11-28, as a limit the script enforces and not as the day to aim for.
3. **The key reaches the script through a setting in the shell, set from the key's own file
   outside the repository.** The script never opens a credentials file. The method's first
   script rule is corrected to say so.
4. **A reply of fewer than 20 words is listed as very short,** and **the one further asking
   after a reply cut off without the service's signal that it was complete uses the same
   length limit.**

The method takes each of these as a dated correction that keeps its earlier words. No message
file changes.

## Not covered by this ruling

- **Whether the script is fit to run.** Its fixes (commits 05b4516 and f23c238) are with a
  different session for a second check, and nothing runs before that check and John's go.
- The other places where the script took the stricter reading of the method, which the check
  judged need no ruling.
- Whether the run is within each developer's terms, the keys, and the spending go with its
  ceiling, quoted word for word in the spending record.
- Anything about the Google and OpenAI runs, which the check says are not ready.

No model has been asked anything, no key has been handled, and nothing has been spent.
