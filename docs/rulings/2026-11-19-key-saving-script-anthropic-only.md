# Ruling: the key-saving script is changed for this project's Anthropic key only, for now

Ruled by John on 2026-11-19, in conversation with the master planning session. **Decided by:
mixed** (a session proposed and recommended, John approved). Written by Claude (Fable 5.2), an
AI model.

## How it came up

The capture script reads its key only from a setting named `BTW_CAPTURE_ANTHROPIC_API_KEY`, and
never opens a key file. The key therefore has to be saved first, in
`~/.config/sentient-horizons/beyond-the-window.env`, the workspace's usual place for keys. The
workspace's key-saving script (`tools/rotate-key/rotate-key.sh` in the TimeAssembler repository)
takes a key at a hidden prompt, checks its form, tests it against the service and writes the
file. Step 4 of the step list (`docs/capture/what-john-needs-to-do.md`) left to John a yes or no
to changing that script, because the change is outside this repository. This was the third of
six decisions put to him before the run that asks Claude Sonnet 4.5.

## What the session told him

- The script exists only on the branch of the open pull request "Anthropic API keys: a swap
  script, and a record that none is in use" (https://github.com/jfredson/timeassembler/pull/141),
  which waits for his merge.
- It knows five key names, none of them this project's, and stores every key under the one
  name `ANTHROPIC_API_KEY`, which the capture script will not read.
- The change comes in two sizes. Small: one new name and file for this project's Anthropic
  key. Whole: also OpenAI and Google keys, each with its own form check and its own test
  against that developer's service, needed only when those runs come near.

The recommendation, with its four things. *The choice:* the small change now, the rest later.
*Confidence:* high on splitting, moderate on using the script at all for one key. *Standard
practice or judgment call:* using the key-saving script is the workspace's standard practice;
splitting the change is a judgment call. *Strongest alternative:* make no change and save this
one key by hand with a single checked command, which needs no merge and no work in another
repository, at the cost that nothing tests the key before the day of the run.

The session also said that a yes would be his word to start a session in the TimeAssembler
repository, that the session would work on its own branch and open a pull request, that a
different session would check it, and that both pull requests are his to merge.

The question put to him was "Make the small Anthropic-only change to the key-saving script in
TimeAssembler?" John: "Yes, Anthropic only". **Decided by: mixed.**

## What is ruled

1. The key-saving script is changed so that it can save this project's Anthropic key, as the
   line `BTW_CAPTURE_ANTHROPIC_API_KEY=` followed by the key, in
   `~/.config/sentient-horizons/beyond-the-window.env`.
2. A session may be started in the TimeAssembler repository to make that change on its own
   branch, and a different session checks it.

## Not covered by this ruling

- **The merges.** John did not say to merge the open pull request, and nobody merges it or the
  new one for him.
- **OpenAI and Google keys.** That larger change waits for those runs.
- **The key itself.** No key exists for this project yet. Creating it and saving it are his.
- The command that loads the key into a Terminal window, and the go to spend.

No model has been asked anything, no key has been handled, and nothing has been spent.
