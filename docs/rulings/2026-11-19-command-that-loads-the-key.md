# Ruling: the command that loads the Anthropic key into the Terminal window

Ruled by John on 2026-11-19, in conversation with the master planning session. **Decided by:
mixed** (a session proposed and recommended, John approved). Written by Claude (Fable 5.2), an
AI model.

## How it came up

John ruled on 2026-11-18 that the capture script takes its key from a setting in the Terminal
window and opens no key file itself (`docs/rulings/2026-11-18-capture-script-four-points.md`,
point 3). That leaves one command for him to type on the day of the run, which copies the key
from its file into the window. The step list (`docs/capture/what-john-needs-to-do.md`, "The
Anthropic run, step by step", step 2) carried it as proposed and not ruled. This was the fourth
of six decisions put to him before the run that asks Claude Sonnet 4.5.

## The command

```bash
export BTW_CAPTURE_ANTHROPIC_API_KEY="$(sed -n 's/^BTW_CAPTURE_ANTHROPIC_API_KEY=//p' ~/.config/sentient-horizons/beyond-the-window.env)"
```

## What the session told him

- It finds the one line in the key file that begins with this project's Anthropic name, takes
  what follows the equals sign, and holds it in that Terminal window until the window is
  closed. It prints nothing.
- If it picks up nothing, because the file or the line is missing, the capture script stops at
  its first check with a plain message and makes no call.

The recommendation, with its four things. *The choice:* approve the command as written.
*Confidence:* moderate to high. It has been tried only on a constructed file holding no real
key, because the real file does not exist yet; the session changing the key-saving script was
asked to confirm it again on a constructed file written by the changed script. *Standard
practice or judgment call:* judgment call. *Strongest alternative:* the workspace's usual
command, which loads every line of a key file at once. It is shorter and familiar, and once the
file also holds the Google and OpenAI keys it would put all three in the window during a run
that needs one.

The question put to him was "Approve the proposed command that loads only the Anthropic key
into the Terminal window?" John: "Approve it". **Decided by: mixed.**

## What is ruled

The command above is the one John types to load the key for the Anthropic run.

## A condition the session attaches, which is the session's and not John's

The command depends on the key file's line being written as `BTW_CAPTURE_ANTHROPIC_API_KEY=`
followed by the key, with no quotation marks. If the check of the changed key-saving script
finds that it writes the line any other way, the command or the script is corrected and the
difference is put to John before the run. Decided by: agent.

## Not covered by this ruling

- The matching commands for the Google and OpenAI runs.
- Who types it. The step list says John does, in the Mac's own Terminal, and that a session
  doing so would be handling the key. That is unchanged.
- The key itself and the go to spend.

No model has been asked anything, no key has been handled, and nothing has been spent.
