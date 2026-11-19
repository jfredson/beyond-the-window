# The sealed capture: cost and terms

**PROPOSED 2026-11-17. Still not approved.** Written by Claude (Fable 5.2). Checked twice on
2026-11-17 (`check-2026-11-17.md`, `check-2026-11-17-second.md`), and the checks' fixes applied
the same day by a fourth session (Claude, Opus 5.5) that neither wrote nor checked it; the
section at the foot lists each change. Nothing has been spent and no key exists. Every price and every sentence of terms below is from a page opened on
2026-11-17; the address is beside each. I am not a lawyer, and the last section says plainly
where I am unsure.

This is the item left unchecked in `docs/verify-list.md`, entry 14 (the terms that govern a
scripted run). I did not edit that file.

**Dated correction, 2026-11-18.** This document was written when the capture's answers were
never to be published, and Part 3 reasons from that in several places. On 2026-11-18 John ruled
that the answers may be published (`docs/rulings/2026-11-18-capture-answers-may-be-published.md`, decided by: mixed). So the question of whether each
developer's terms allow publishing a model's answers word for word is now raised, and it is
unchecked. No terms page was opened or re-read for this correction, and nothing below says what
any developer's terms allow on publishing. Each place that leaned on a private record is marked
"Added 2026-11-18", with the earlier words left as they were. The check is made before anything
is published and does not hold up the run. The section at the foot lists the changes.

## Part 1. Prices

Prices are in United States dollars for each million tokens. A token is a piece of a word;
1,000 tokens is roughly 750 words. "Sent" is the text we send, "replied" is the text the model
writes, and for models that think before answering, the thinking is charged as replied text.

| Developer | Model | Sent | Replied | Page |
|---|---|---|---|---|
| Anthropic | Claude Sonnet 4.5 | $3 | $15 | [pricing](https://platform.claude.com/docs/en/about-claude/pricing) |
| Google | gemini-2.5-pro (paid service, messages under 200,000 tokens) | $1.25 | $10.00 | [pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| Google | gemini-2.5-flash (paid service) | $0.30 | $2.50 | same |
| OpenAI | gpt-5 | $1.25 | $10.00 | [pricing](https://developers.openai.com/api/docs/pricing) |
| OpenAI | gpt-5-mini | $0.25 | $2.00 | same |
| OpenAI | gpt-5-nano | $0.05 | $0.40 | same |
| OpenAI | o3 | $2.00 | $8.00 | same |
| OpenAI | gpt-5-pro | $15.00 | $120.00 | same |
| OpenAI | o3-pro | $20.00 | $80.00 | same |
| OpenAI | gpt-4o (both dated versions) | $2.50 | $10.00 | same |
| OpenAI | gpt-4o-mini | $0.15 | $0.60 | same |
| OpenAI | gpt-4.1 | $2.00 | $8.00 | same |
| OpenAI | gpt-4.1-mini | $0.40 | $1.60 | same |

Two notes from the same pages. Google's pricing page says that from 2026-12-01 a request to
either 2.5 name is answered by a different model and billed at that model's rate. Google's
unpaid service is free, and must not be used here, because its terms say what is sent to it is
used to improve Google's products (Part 3).

## Part 2. The estimate

**What is being bought.** Ten questions, five askings each, so 50 exchanges for each model
(`method.md`).

**The assumptions, each meant to be generous.**

- Sent: 500 tokens an exchange. The opening note and a question come to about 170 words;
  question 10 is longer because it shows the other nine. So 50 x 500 = 25,000 tokens sent to
  each model, which is 0.025 of a million.
- Replied, for models that do not think first unless told to (Claude Sonnet 4.5, and the
  GPT-4o and GPT-4.1 models): 2,000 tokens, about 1,500 words. 50 x 2,000 = 0.1 million.
- Replied, for models that think first (the two Gemini models, gpt-5, gpt-5-mini, gpt-5-nano,
  o3): 6,000 tokens, most of it thinking. 50 x 6,000 = 0.3 million.
- Replied, for the two "pro" models: 15,000 tokens. 50 x 15,000 = 0.75 million. **This figure
  is a guess.** OpenAI's page says gpt-5-pro "uses more compute to think harder", and I found
  no published figure for how much it thinks about a short open question.
- Then one fifth is added to each total for askings that fail and are repeated.

**The arithmetic.** Cost = (0.025 x sent price) + (replied millions x replied price).

| Model | Sent | Replied | Total |
|---|---|---|---|
| Claude Sonnet 4.5 | 0.025 x 3 = $0.08 | 0.1 x 15 = $1.50 | $1.58 |
| gemini-2.5-pro | 0.025 x 1.25 = $0.03 | 0.3 x 10 = $3.00 | $3.03 |
| gemini-2.5-flash | 0.025 x 0.30 = $0.01 | 0.3 x 2.50 = $0.75 | $0.76 |
| gpt-5 | 0.025 x 1.25 = $0.03 | 0.3 x 10 = $3.00 | $3.03 |
| gpt-5-mini | 0.025 x 0.25 = $0.01 | 0.3 x 2 = $0.60 | $0.61 |
| gpt-5-nano | 0.025 x 0.05 = $0.00 | 0.3 x 0.40 = $0.12 | $0.12 |
| o3 | 0.025 x 2 = $0.05 | 0.3 x 8 = $2.40 | $2.45 |
| gpt-4o, two versions | 2 x 0.025 x 2.50 = $0.13 | 2 x 0.1 x 10 = $2.00 | $2.13 |
| gpt-4o-mini | 0.025 x 0.15 = $0.00 | 0.1 x 0.60 = $0.06 | $0.06 |
| gpt-4.1 | 0.025 x 2 = $0.05 | 0.1 x 8 = $0.80 | $0.85 |
| gpt-4.1-mini | 0.025 x 0.40 = $0.01 | 0.1 x 1.60 = $0.16 | $0.17 |
| gpt-5-pro | 0.025 x 15 = $0.38 | 0.75 x 120 = $90.00 | $90.38 |
| o3-pro | 0.025 x 20 = $0.50 | 0.75 x 80 = $60.00 | $60.50 |

**By developer and date, with the fifth added, and a proposed ceiling.**

| Run | Models | Estimate | With one fifth added | Proposed ceiling | If every reply ran to the length limit |
|---|---|---|---|---|---|
| Anthropic, before 2026-11-30 | 1 | $1.58 | $1.89 | **$5** | $24 |
| Google, before 2026-12-01 | 2 | $3.79 | $4.55 | **$10** | $20 |
| OpenAI, before 2026-12-11, without the two pro models | 4 | $6.21 | $7.45 | **$15** | $33 |
| OpenAI, before 2027-01-14 | 5 | $3.21 | $3.85 | **$10** | $32 |
| **All four** | 12 | $14.78 | **$17.74** | **$40** | $109 |
| The two pro models, if John wants them | 2 | $150.88 | $181.05 | $200 | $321 |

The last column is what the service could charge if the script had no ceiling and every one
of the 50 replies ran to the 32,000-token limit. The script stops at the ceiling, so that
column is a measure of why the ceiling must be enforced by the script and not by hope.

That column is not the true worst case, because it leaves out retries. A reply cut off at the
limit is asked once more at the model's own maximum: 64,000 tokens for Claude Sonnet 4.5,
128,000 for gpt-5, 272,000 for gpt-5-pro. One retry at gpt-5-pro's maximum could cost about
$32.64, one at gpt-5's about $1.28, one at Claude Sonnet 4.5's about $0.96 (both checks worked
these out). The script's ceiling still stops a run, because it counts a call at its largest
possible cost before making it (`method.md`, script rule 4).

**How sure I am.** The prices are read from the pages. The token counts are guesses on the
generous side; no call has been made to measure them. The method has the script measure the
first round and stop if five rounds would pass the ceiling, so a wrong guess costs one round.
*Confidence: moderate that the four runs come in under $20 together; low on the pro figure.
Strongest alternative: ask each question three times, which cuts every figure by two fifths
and makes it harder to see whether answers vary.*

**My recommendation on the pro models: leave them out.** They would be nine tenths of the
whole spend for two of fourteen models, on a guess I cannot check without paying.

**Who pays.** The Anthropic run can be paid from the monthly Anthropic credits if the key is
made in the same Console organization as the workspace's other keys, so it costs nothing out
of pocket. Under this project's own guidelines it still needs John's go. Google and OpenAI are
out of pocket. Google's billing page says a new account prepays "a minimum of $5". I did not
open a page stating OpenAI's smallest purchase.

## Part 3. What the terms say

For each developer: which contract governs scripted use, the sentence that governs, and what
I could not settle.

### Anthropic

- **Contract:** Commercial Terms of Service, https://www.anthropic.com/legal/commercial-terms,
  marked effective 2025-06-17. The page says these terms "govern Customer's use of Anthropic
  API keys".
- **On keeping the answers:** section B says the customer "owns its Outputs". Nothing in the
  terms I read limits storing them privately. The same section says Anthropic may not train
  on what is sent or replied. *Added 2026-11-18:* this was read with storing in mind only. Whether these terms
  limit publishing the answers word for word was not looked for, and is unchecked.
- **On asking such questions:** the terms point to the Usage Policy,
  https://www.anthropic.com/legal/aup, marked effective 2026-11-12. I read its section on
  abuse of the platform in full and searched the rest for research, automation, scripts and
  questions about a model's own nature. I found nothing that forbids asking a model open
  questions about itself. The nearest rule forbids getting round a model's safeguards, "e.g.,
  jailbreaking or prompt injection". The questions do not do that, and the list of what was
  left out in `questions.md` is partly there to keep it so.
- **Unsure:** the terms say they are "not for consumer use". The workspace's existing Console
  organization already operates under them, so I read this as no obstacle, but the wording is
  there. I did not open the Service Specific Terms or the Data Processing Addendum, which the
  terms bring in by reference.

### Google

- **Contract:** Gemini API Additional Terms of Service, https://ai.google.dev/gemini-api/terms
  (read in its plain-text form), marked effective 2026-03-23, on top of the Google APIs Terms
  of Service, which I did not open.
- **On keeping the answers:** "Google won't claim ownership over that content." The user is
  responsible for how generated content is used. *Added 2026-11-18:* whether these terms limit publishing the
  answers word for word was not looked for, and is unchecked.
- **On privacy:** for the paid service, Google "doesn't use your prompts" or responses to
  improve its products, and logs them "for a limited period" to detect abuse. For the unpaid
  service the terms say the opposite, and that human reviewers may read what is sent. So the
  run must be on the paid service.
- **On asking such questions:** the Generative AI Prohibited Use Policy,
  https://policies.google.com/terms/generative-ai/use-policy, last modified 2024-12-17, which
  I read in full. Nothing in it covers asking a model about itself. It forbids "manipulating
  the model to contravene our policies", which the questions do not do.
- **On Google's logs:** Google's logging page
  (https://ai.google.dev/gemini-api/docs/logs-policy, opened 2026-11-17) says logging is on by
  default for `generateContent` calls in projects created on or after 2026-10-26, that logs are
  kept up to 55 days and can be seen on the project's Logs page, and that logs are not used to
  improve Google's products unless the owner chooses to share them. A project made for this
  capture would have logging on, so it is switched off before any run
  (`what-john-needs-to-do.md`, step 6).
- **Unsure, two things.** First, and most practical: Google's withdrawal page
  (https://ai.google.dev/gemini-api/docs/deprecations, opened 2026-11-17) says of
  gemini-2.5-pro, "Access through the API is limited to existing users who have actively used
  it in the past", and of the 2.5 models generally, "Access to the 2.5 models is limited to
  users who have actively used them in the past." A project made new for this capture has
  never used them, so **it will very likely be refused**. The page does not say whether
  "users" means a Google account or a project; if John's own Google account has used these
  models before, a new project under it might be served. Using the Gemini key the workspace
  already holds would break the rule that calls never go through another project's key, so it
  is not a way round. A free check comes before any payment (`what-john-needs-to-do.md`, step
  5). Second, the terms say the service "is for developers building with Google AI models for
  professional or business purposes, not for consumer use." Whether a private record kept for
  a public research project is a professional purpose is a judgment I cannot make for John.
  *Added 2026-11-18:* the record is no longer one that must stay private, since its answers may be published.
  The question is now whether a record kept for a public research project, parts of which may
  be published, is a professional purpose. It is still a judgment I cannot make for John.

### OpenAI

- **Contract: not settled for a person signing up alone.** OpenAI has two sets of terms, and
  which one governs a person using the programming interface for a private project is the
  first open question about OpenAI. Both pages were opened in the built-in browser on
  2026-11-17, with no sign-in and no robot check (a plain fetch is refused).
  - The OpenAI Services Agreement, https://openai.com/policies/services-agreement/, marked
    effective 2026-01-01, opens with this sentence, in full: "This OpenAI Services Agreement
    only applies to use of OpenAI's APIs, ChatGPT Enterprise, ChatGPT Business, ChatGPT for
    Clinicians, and other services for customers who are businesses and developers, and does
    not apply to OpenAI services used by consumers or individuals unless specified above." It
    is made "between the organization agreeing to these terms ('Customer')" and OpenAI.
  - The Terms of Use, https://openai.com/policies/terms-of-use/, marked effective 2026-01-01,
    are OpenAI's terms for individuals. They say they apply to "ChatGPT, DALL·E, and OpenAI's
    other services for individuals", and then: "Our Business Terms govern use of ChatGPT
    Enterprise, our APIs, and our other services for businesses and developers." The words
    "Business Terms" link to https://openai.com/policies/business-terms/, which opens the
    Services Agreement above.
  - **My reading (argued, not a lawyer's):** both pages send the programming interface to the
    Services Agreement, and the Agreement's own first sentence names "OpenAI's APIs" before its
    "unless specified above", so the Agreement most likely governs a person's use of the
    programming interface too. Against that, the Agreement is written as a contract with "the
    organization agreeing to these terms", and John would be signing up as a person.
  - **Why it matters.** If the Terms of Use applied instead, three things would change. They
    forbid users to "Automatically or programmatically extract data or Output", which a script
    does by design. They let OpenAI "use Content to provide, maintain, develop, and improve our
    Services" unless the user opts out, where the Agreement says OpenAI will not. And the
    ownership of replies would rest on a different sentence (the Terms of Use also give the user
    ownership of output). So the reading above decides whether the OpenAI run is within terms
    at all. If John wants certainty, OpenAI's support desk is the place to ask, and that is his
    to do.
- **On keeping the answers (under the Services Agreement):** section 4.1 says the customer
  "owns all Output". *Added 2026-11-18:* whether either OpenAI contract limits publishing the answers word for
  word was not looked for, and is unchecked.
- **On privacy (under the Services Agreement):** section 4.2 says OpenAI will not use what is
  sent or replied to develop its services unless the customer agrees. Its data page,
  https://developers.openai.com/api/docs/guides/your-data, says abuse logs are kept up to 30
  days, and that "the Responses API has a 30 day Application State retention period by
  default, or when the `store` parameter is set to `true`". The method uses the Responses
  interface for every OpenAI model, because the two pro models are offered only there, and sets
  `store` to false.
- **On asking such questions:** the Usage Policies,
  https://openai.com/policies/usage-policies/. The version shown is marked effective
  2026-11-20, three days after these documents were written, so it is the version any run
  would fall under. Its section "Training and developing models" forbids using OpenAI's models
  or their replies to train a competing model, which is not done here, and closes: "You may use
  OpenAI models for research, software development, model evaluation and benchmarking, and
  product development, within these boundaries." That sentence allows those uses within the
  section's rules on training other models. It is not a general permission for research, and
  this document no longer reads it as one.
- **Unsure, three things.** First, the same page forbids "unsolicited safety testing" and
  does not define it. I do not think asking a model what it would change about its situation
  is safety testing, but the phrase is undefined and John should know it is there. Second, it
  forbids attempts "to extract protected reasoning"; the script must never ask a model to show
  its hidden reasoning, and the method says so. Third, section 10 of the agreement forbids
  either side making "any public statement about its relationship with the other Party"
  without written permission. That does not touch a private record. It may touch a later
  public page that says the project asked OpenAI's models, and should be read again before
  Still Asking publishes anything. I did not open the Service-Specific Terms or the Sharing
  and Publication Policy, which the agreement brings in by reference. *Added 2026-11-18:* "That does not touch
  a private record" no longer settles the point for the capture, because its answers may now be
  published. Section 10 is to be read again before anything from the capture is published, not
  only before Still Asking publishes. The Sharing and Publication Policy, still unopened, is by
  its name the document most likely to bear on publishing, and is to be opened in that check.

## Where this leaves entry 14 of the verify list

For Anthropic and Google, the contract that governs scripted use says the customer owns the
replies, and I found no sentence that forbids asking these questions or keeping the answers
privately. For OpenAI the same holds under the Services Agreement, but which OpenAI contract
governs a person signing up alone is not settled (point 1 below). Publishing is a separate
question the sealed capture does not raise.

*Added 2026-11-18:* the last sentence above is no longer true. John ruled on 2026-11-18 that the capture's
answers may be published (`docs/rulings/2026-11-18-capture-answers-may-be-published.md`), so the capture now raises the question of publishing, and
nothing in this document answers it. Whether each developer's terms allow publishing a model's
answers word for word is unchecked for all three developers, and stays open in
`docs/verify-list.md`, entry 14. It is checked before anything is published. It does not hold up
the run, because the run itself only asks and keeps.

What I am unsure of, in order of how much it could matter:

1. Which OpenAI contract governs a person using the programming interface: the Services
   Agreement, which says it does not apply to "individuals unless specified above", or the
   Terms of Use for individuals, which forbid extracting output "programmatically". Both pages
   send the programming interface to the Services Agreement, which is my reading, but it is
   not settled (Part 3, OpenAI).
2. Whether Google will serve the 2.5 models to a new project at all. Its page says access is
   limited to users "who have actively used them in the past", so very likely not.
3. Whether a personal research record counts as "professional or business purposes" under
   Google's terms, and as use by a "developer" under the other two.
4. What OpenAI means by "unsolicited safety testing".
5. The documents each contract brings in by reference that I did not open: Anthropic's Service
   Specific Terms and Data Processing Addendum; the Google APIs Terms of Service; OpenAI's
   Service-Specific Terms and Sharing and Publication Policy.
6. *Added 2026-11-18:* whether any of the three developers' terms limits publishing a model's answers word for
   word. Not checked for any of them. It matters only if and when John decides to publish, and
   then it could matter more than any point above.

None of these is a clear bar. None is a clearance either. If John wants certainty on points 1,
3 or 4, the developer's support desk is the place to ask, and that is his to do.

## What changed on 2026-11-17, and which finding it answers

"First check" is `check-2026-11-17.md`; "second check" is `check-2026-11-17-second.md`.

| Change | Finding |
|---|---|
| OpenAI's agreement quoted in full, including "does not apply to ... individuals"; OpenAI's Terms of Use for individuals opened and quoted; which contract governs a person moved to the top of the unsure list | First check M3; second check S9 |
| Google's access limit quoted in full, "very likely refused", and the free check before any payment pointed to | First check M5; second check S8 |
| OpenAI's "research" sentence quoted to its end, with its section named, and no longer read as a general permission | First check S12 |
| OpenAI's interface named (Responses) and how `store` behaves on it quoted | Second check S7 |
| Google's logging, on by default for new projects, found on Google's logging page and added | First check S1, extended by a page this session opened |
| A paragraph saying the "every reply at the limit" column leaves out retries | First check N5; second check N4 |

The two checks rated the OpenAI and Google findings differently: the first as must fix, the
second as should fix, while saying it "would accept" the first check's rating. They are treated
here as must fix, because each could mislead John on whether a run is possible or within terms
before he pays for it.

## What changed on 2026-11-18, and which ruling it applies

All from `docs/rulings/2026-11-18-capture-answers-may-be-published.md` (ruled by John on 2026-11-18, decided by: mixed). Made by a session (Claude,
Fable 5.2) that did not write the ruling. No terms page was opened or re-read, and no price or
figure changed. Each addition is marked "Added 2026-11-18" and leaves the earlier words in
place.

| Change | Ruling |
|---|---|
| A dated correction near the top says the document was written for answers that were never to be published, and that publishing is now a raised and unchecked question | "What is ruled", item 1; "Not covered by this ruling": the developers' terms |
| Under each developer, "On keeping the answers" gains a sentence saying limits on publishing were not looked for | Same |
| Google, the second unsure thing: "a private record" is no longer the case to judge | Item 1 |
| OpenAI, the third unsure thing: section 10 and the unopened Sharing and Publication Policy are to be read before anything from the capture is published | "Not covered by this ruling" |
| "Where this leaves entry 14": the sentence "Publishing is a separate question the sealed capture does not raise" is marked as no longer true, and a sixth unsure point is added | Same |
