# Ruling: the ceiling for the Google run of the sealed capture is $10

Ruled by John on 2026-11-20, in conversation with the master planning session. **Decided by:
mixed** (a session proposed and recommended, John approved). Written by Claude (Fable 5.2), an
AI model.

## How it came up

The capture plan (`capture/plan.toml`) carries a proposed ceiling of $10.00 for the Google run
(`google-2026-12-01` in the plan), the one that asks Gemini 2.5 Pro and Gemini 2.5 Flash before
Google withdraws them on 2026-12-01. A ceiling is the most the run may cost before the script
stops itself. This was the second of five decisions put to John before that run.

## What the session told him

- *Expected cost:* $3.79 for both models, 100 exchanges in all
  (`docs/capture/cost-and-terms.md`, Part 2).
- *Where the money comes from:* John's own pocket. The monthly Anthropic credits do not cover
  Google.
- *The choice:* set the ceiling at $10.
- *Confidence:* moderate to high. The script counts a call whose cost the service does not
  report at the most it could have cost, so a ceiling close to the estimate lets a few broken
  connections stop the run, and these models cannot be asked again after the last safe day,
  2026-11-29. John ruled $10 for the Anthropic run on the same reasoning
  (`docs/rulings/2026-11-18-anthropic-ceiling.md`), and that run cost $0.2667.
- *Standard practice or judgment call:* judgment call. It matches the Anthropic ceiling.
- *Strongest alternative:* $5, which caps what he could lose lower and leaves a real chance of
  a stopped run with nine days left to start it again.

The question put to him was "Set the spending limit for the Google run at $10?" John: "Yes,
$10". **Decided by: mixed.**

## What is ruled

**The ceiling for the Google run (`google-2026-12-01` in the plan) is $10.00.** The plan
already holds that figure, so no figure in it changes. Its comment that calls the Google
ceiling "still PROPOSED" is now out of date, and is for the session that wrote the script to
bring up to date.

## Not covered by this ruling

- **This is not the go to spend.** The script starts only when the spending record
  (`docs/spending-record.md`) holds John's own words naming the developer and one figure with a
  dollar sign. "Yes, $10" answers a question about the ceiling and names no developer, so it is
  not recorded as the go. The go is still his to give.
- **The two OpenAI ceilings** ($15 and $10) stay proposed.
- Billing on the new Google project, the logging switch, the key, and whether Google will serve
  these models to the project at all.

No Google model has been asked anything, no Google key exists, and nothing has been spent on
this run.
