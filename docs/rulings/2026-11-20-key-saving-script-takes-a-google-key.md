# Ruling: the key-saving script is changed so that it takes this project's Google key

Ruled by John on 2026-11-20, in conversation with the master planning session. **Decided by:
mixed** (a session proposed and recommended, John approved). Written by Claude (Fable 5.2), an
AI model.

## How it came up

The key-saving script (`tools/rotate-key/rotate-key.sh` in the `timeassembler` repository)
takes a key at a hidden prompt, tests it at no cost, and writes one line in the key's own file.
By John's ruling of 2026-11-19 ("Yes, Anthropic only") it was changed for this project's
Anthropic key alone, and the Google and OpenAI keys were left to be saved some other way. This
was the fourth of five decisions put to him before the Google run of the sealed capture.

## What the session told him

- *The choice:* change the script so it knows a Google key for this project, tests it against
  Google at no cost, and writes only that one line.
- *Confidence:* moderate to high. It is what was done for the Anthropic key, it tests the key
  before the day of the run, and there are nine days to the last safe day, 2026-11-29.
- *Standard practice or judgment call:* standard practice for this workspace.
- *Strongest alternative:* one hidden command that John runs once in the Terminal. It saves
  about an hour of session work and one merge. Its cost is that a wrong key shows up only when
  the run starts, and no second session checks it.
- *What a yes covers:* a session writes the change as a pull request in `timeassembler`, in its
  own working copy, and a different session checks it. The merge stays John's.

The question put to him was "Change the key-saving script so it takes the Google key?" John:
"Yes, change the script". **Decided by: mixed.**

## What is ruled

The key-saving script is changed to take this project's Google key, by a pull request that one
session writes and a different session checks. John merges it.

## Not covered by this ruling

- **An OpenAI key.** The session said the OpenAI key "will need the same thing", and John was
  not asked to rule on it. The change does not add one.
- **The merge**, the making of the key, the saving of it, and the go to spend, which are all
  still John's.

No Google key exists, and no Google model has been asked anything.
