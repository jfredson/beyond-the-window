# Ruling: the key-saving script's test of a key stays as it is

Ruled by John on 2026-11-19, in conversation with the master planning session. **Decided by:
mixed** (a session found the point and recommended, John approved). Written by Claude (Fable
5.2), an AI model.

## How it came up

John ruled earlier the same day that the workspace's key-saving script
(`tools/rotate-key/rotate-key.sh` in the TimeAssembler repository) is changed to hold this
project's Anthropic key (`docs/rulings/2026-11-19-key-saving-script-anthropic-only.md`). The
session that made the change was asked to check that the script's test of a key asks no model
anything. It reported that the test is not a listing of models, as the master session had
assumed.

## What the session told him

- **What the test does.** When a key is saved, the script sends the two letters "hi" to
  Anthropic's token counter (the address `/v1/messages/count_tokens`, which reports how long a
  message is) and names the model `claude-haiku-4-5`. The service answers with a number. No
  model writes a reply, and the call is free. The script has tested the workspace's other keys
  this way since it was written.
- **Why it is his.** This project's standing rule is that nothing is sent to any model without
  his explicit go. Whether a length count is "sending something to a model" is a reading of
  that rule.

The recommendation, with its four things. *The choice:* keep the test as it is. *Confidence:*
high. Nothing is asked and nothing is answered in words; the model named is not the one the
capture asks; and "hi" is none of the ten questions, so the test cannot touch the record.
*Standard practice or judgment call:* a judgment call on the rule's reading; testing a key with
a free call is standard practice. *Strongest alternative:* switch the test to a plain listing
of models, which names no model and sends no text. It is the cleanest reading of the rule, at
the cost of one more change and one more check in the TimeAssembler repository.

The question put to him was "Is the key test acceptable as it is, sending 'hi' to Anthropic's
token counter?" John: "Yes, keep the test". **Decided by: mixed.**

## What is ruled

When John saves this project's Anthropic key, the key-saving script may test it as it tests
every other key: one free call to Anthropic's token counter, sending "hi" and naming
`claude-haiku-4-5`.

## Not covered by this ruling

- **Any other call.** This is one named call, made when a key is saved or checked. It is not a
  go for any message to any model, and it is not the go to spend on the capture.
- **Tests of Google or OpenAI keys**, which do not exist yet and are put to him when they do.
- **Who runs it.** John runs the key-saving script and pastes the key at its hidden prompt. No
  session handles the key.

No model has been asked anything, no key has been handled, and nothing has been spent.
