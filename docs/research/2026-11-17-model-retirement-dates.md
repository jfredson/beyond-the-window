# When current models are due to be withdrawn

Written 2026-11-17 by Claude (Fable 5.2). **Facts only.** Whether anything should be captured
before a model is withdrawn is John's decision, and this document does not recommend either
way. Every page below was opened on 2026-11-17. This clears entry 13 of `docs/verify-list.md`.

## What the words mean

Developers use different words for the same steps. In this document:

- **Withdrawn** means the developer has stopped serving the model to outside users through its
  programming interface. Anthropic calls this "retired", OpenAI and Google call it "shut down".
- **Notice given** means the developer has announced a withdrawal date. Anthropic and Google
  call a model in this state "deprecated".

Three limits apply to everything below.

- These are dates for the developers' programming interfaces. A chat product can drop a model
  on a different date. OpenAI withdrew GPT-4o from its chat product on 2026-02-13 (its page of
  2026-01-29, https://openai.com/index/retiring-gpt-4o-and-older-models/) while the same model
  stays available to developers until 2027-01-14.
- Withdrawn does not always mean gone. Anthropic says it keeps every released model's files,
  and kept one withdrawn model open to paying users (entries 1 and 3 of
  `docs/research/2026-11-17-first-entries.md`).
- Other companies that resell a model set their own dates. Anthropic's page says so for two
  cloud providers.

## Anthropic

**Page:** https://platform.claude.com/docs/en/about-claude/model-deprecations.md (opened
2026-11-17; no date on the page; its newest notice is dated 2026-09-30). The page promises at
least 60 days' notice before a publicly released model is withdrawn.

| Model, as the page names it | State | Notice given | Withdrawal date |
|---|---|---|---|
| claude-fable-5-2 | Active | none | Not sooner than 2027-11-09 |
| claude-mythos-5-2 | Active | none | Not sooner than 2027-11-09 |
| claude-fable-5-1 | Active | none | Not sooner than 2027-09-01 |
| claude-mythos-5-1 | Active | none | Not sooner than 2027-09-01 |
| claude-fable-5 | Active | none | Not sooner than 2027-06-09 |
| claude-mythos-5 | Active | none | Not sooner than 2027-06-09 |
| claude-mythos-preview | Notice given | 2026-06-09 | To be announced |
| claude-opus-5-5 | Active | none | Not sooner than 2027-09-22 |
| claude-opus-5 | Active | none | Not sooner than 2027-07-24 |
| claude-opus-4-8 | Active | none | Not sooner than 2027-05-28 |
| claude-opus-4-7 | Active | none | Not sooner than 2027-04-16 |
| claude-opus-4-6 | Active | none | Not sooner than 2027-02-05 |
| claude-opus-4-5-20251101 | Active | none | Not sooner than 2026-11-24 |
| claude-sonnet-5-5 | Active | none | Not sooner than 2027-09-28 |
| claude-sonnet-5 | Active | none | Not sooner than 2027-06-30 |
| claude-sonnet-4-6 | Active | none | Not sooner than 2027-02-17 |
| **claude-sonnet-4-5-20250929** | **Notice given** | **2026-09-30** | **2026-11-30** |
| claude-haiku-5-5 | Active | none | Not sooner than 2027-10-07 |
| claude-haiku-4-5-20251001 | Active | none | Not sooner than 2026-10-15 (already passed) |

Already withdrawn, for the record: Claude Opus 3 (2026-01-05), Claude Sonnet 3.7 and Claude
Haiku 3.5 (2026-02-19), Claude Haiku 3 (2026-04-20), Claude Opus 4 and Claude Sonnet 4
(2026-06-15), Claude Opus 4.1 (2026-08-05).

## OpenAI

**Page:** https://developers.openai.com/api/docs/deprecations.md (opened 2026-11-17; no date
on the page; its newest notice is dated 2026-11-10). The page lists only models that have a
withdrawal date. It gives no date for models with no notice, which include the current GPT-6
family named on the page as replacements. Its stated minimum notice is six months for
generally available models, three months for specialised variants, and as little as two weeks
for models with "preview" in the name.

Text models with a withdrawal date announced (image, speech and transcription models are left
out here; the page lists them):

| Model, as the page names it | Notice given | Withdrawal date |
|---|---|---|
| gpt-5, gpt-5-mini, gpt-5-nano | 2026-06-11 | 2026-12-11 |
| gpt-5-pro | 2026-06-11 | 2026-12-11 |
| o3, o3-pro | 2026-06-11 | 2026-12-11 |
| GPT-4o (two dated versions), GPT-4o mini | 2026-10-14 | 2027-01-14 |
| GPT-4.1, GPT-4.1 mini | 2026-10-14 | 2027-01-14 |
| gpt-5.5-cyber-preview | 2026-11-05 | 2027-02-01 |
| gpt-5.1 | 2026-10-01 | 2027-04-01 |
| gpt-5.3-codex | 2026-10-01 | 2027-04-01 |
| gpt-5.4-nano | 2026-10-01 | 2027-04-01 |

The page also says that after a model's shutdown date a customer may in some cases arrange
dedicated capacity to keep using it, through the sales team.

## Google

**Page:** https://ai.google.dev/gemini-api/docs/deprecations (opened 2026-11-17 in its plain
text form at https://aistudio.google.com/docs/deprecations.md; no date on the page). The page
says the dates shown are the earliest possible, and that exact dates are given with notice.

| Model, as the page names it | Released | Withdrawal date |
|---|---|---|
| gemini-4-hydrogen | 2026-11-12 | None announced |
| gemini-4-carbon | 2026-11-10 | None announced |
| gemini-4-argon | 2026-10-13 | None announced |
| gemini-3.8-flash | 2026-09-02 | None announced |
| gemini-3.6-flash | 2026-07-21 | None announced |
| gemini-3.5-flash-lite | 2026-07-21 | None announced |
| gemini-3.7-flash | 2026-08-13 | Not shut down; requests are now answered by gemini-3.8-flash |
| gemini-3.5-flash | 2026-05-19 | Not shut down; requests are now answered by gemini-3.6-flash |
| gemini-3.1-flash-lite | 2026-05-07 | 2027-05-07 |
| gemini-3.1-pro-preview | 2026-02-19 | None announced |
| gemini-3-flash-preview | 2025-12-17 | None announced |
| **gemini-2.5-pro** | 2025-06-17 | **2026-12-01**; requests will then be answered by gemini-3.8-flash. Already limited to existing users. |
| **gemini-2.5-flash** | 2025-06-17 | **2026-12-01**; requests will then be answered by gemini-3.5-flash-lite |
| gemini-2.5-flash-lite | 2025-07-22 | None announced |

Two rows show a practice the other developers' pages do not: the model's name keeps working,
and a different model answers. For a record of what a named model said, that is the same as
withdrawal, with no error to show that it happened.

## xAI

**No schedule page found.** The models page (https://docs.x.ai/developers/models, opened
2026-11-17) lists current models with no withdrawal dates. Withdrawals are announced in
separate notices, of which I opened one:
https://docs.x.ai/developers/migration/may-15-retirement (opened 2026-11-17). It says eight
models, among them grok-4-0709 and grok-3, were withdrawn on 2026-05-15, and that requests to
their names are now answered by grok-4.3. A second notice, for an image model on 2026-11-02,
is listed and was not opened. I found no announced withdrawal date for any current text model.

## Mistral

**Page:** https://docs.mistral.ai/models (opened 2026-11-17; no date on the page). It has a
section listing models with a notice date and a withdrawal date. Rows I read:

| Model | Notice given | Withdrawal date |
|---|---|---|
| Mistral Large 3 | 2026-10-31 | 2027-04-30 |
| Mistral Medium 3.5 | 2026-10-31 | 2027-04-30 |
| Mistral Medium 3.1 | 2026-05-22 | 2026-08-31 (passed) |
| Mistral Small 3.2 | 2026-04-30 | 2026-07-31 (passed) |

The page gives dates as month/day/year; they are converted here. I did not read every row, and
did not read the list of current models for dates.

## Not looked up

Meta, DeepSeek, Cohere, Amazon and others. Models whose files are published openly can be run
by anyone who holds a copy, so a developer's withdrawal date means less for them; I did not
check which current models that covers.

## Is anything current due to be withdrawn within about three months?

Yes. Counting from 2026-11-17 to about 2027-02-17, these have announced dates: Anthropic's
Claude Sonnet 4.5 on 2026-11-30, which is thirteen days away; Google's gemini-2.5-pro and
gemini-2.5-flash on 2026-12-01, after which their names will be answered by other models;
OpenAI's gpt-5, gpt-5-mini, gpt-5-nano, gpt-5-pro, o3 and o3-pro on 2026-12-11; OpenAI's
GPT-4o, GPT-4o mini, GPT-4.1 and GPT-4.1 mini on 2027-01-14; and OpenAI's
gpt-5.5-cyber-preview on 2027-02-01. Four Anthropic models have "not sooner than" dates that
have passed or fall inside the window (Claude Haiku 4.5, Claude Opus 4.5, Claude Opus 4.6,
and Claude Sonnet 4.6 on the window's last day), but none of them has been given notice, and
the page promises at least 60 days' notice, so none of those can be withdrawn before the
middle of January 2027 at the earliest, and only if notice were given today. Claude Mythos
Preview has been given notice with no date. None of the newest models from any of the five
developers has an announced date.

## Not confirmed

- That each page is complete and current. Each was read once, on one day.
- The dates on which chat products drop models, apart from the one OpenAI page cited.
- Whether Anthropic's commitment to interview a model before withdrawal has been carried out
  for Claude Sonnet 4.5, or will be before 2026-11-30.
