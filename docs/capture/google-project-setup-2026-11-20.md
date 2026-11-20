# The Google project made ready for the run: billing on, storage of requests off

Done on 2026-11-20 by the master planning session, in Google AI Studio, on John's word. Written
by Claude (Fable 5.2), an AI model. No key was made, no model was asked anything, and no payment
was made. Not yet checked by a different session, which cannot see Google's pages; the facts
read from them are the master session's to answer for.

## John's word

The session asked "Join the new Google project to your existing billing account?", and said a
yes would cover three things: joining the project to that account, switching logging off on the
project, and looking at how automatic top-up is set without changing it. John: "Yes, existing
account". **Decided by: mixed** (the session recommended it; the strongest alternative put to
him was a separate billing account, at a minimum of $5 up front). The ruling has its own file,
`docs/rulings/2026-11-20-google-project-joins-existing-billing-account.md`.

One part of the recommendation was the session's own reading and is marked as such: the rule
that calls never go through another project's key is about keys, the new project gets a key of
its own, and so sharing a billing account is within the rule.

## What was done, and what the pages showed afterwards

1. **The project "Beyond the Window" was joined to an existing billing account of John's.**
   AI Studio's own notice said: "Your Google Cloud billing account and Gemini API project are
   now linked", and "Gemini API Paid Tier activated". No screen asked for a payment.
2. **Storage of requests is off for the project, on both switches** in the project's log
   settings.
   - "GenerateContent API": **was already off** when the session opened the page. The capture
     script calls this interface. Google's logging page, as read on 2026-11-17
     (`cost-and-terms.md`, Part 3), said logging is on by default for new projects, so either
     that page has changed, or it describes something other than this switch. Not looked into.
   - "Interactions API": was on. The session switched it off and confirmed Google's question
     "Disable storage?". The capture script does not call this interface, so this is a
     precaution.
   - The project's log list showed "No logs found".
3. **The session read the billing page and changed nothing on it.** A run within the $10
   ceiling needs no new payment to Google. That does not mean no cost: whatever the run costs
   is John's money, already with Google. The step list (`what-john-needs-to-do.md`, step 6)
   had in mind an account holding no more than the ceiling, as a second stop behind the
   script. That is not the case here, so the script's own limit of $10 is the only thing that
   stops the run.

## What the project's list of limits shows now

On the paid service the project's row for "Gemini 2.5 Pro" has limits above zero (1,000
requests a minute), where on the unpaid service it had zero. "Gemini 2.5 Flash" has 2,000
requests a minute. This bears out the reading in the note on the free check
(`google-free-check-2026-11-19.md`) that the zero meant the paid service was needed.

It still does not show that Google will answer a call. Its page says access to the 2.5 models
"is limited to users who have actively used them in the past", and the earlier reading, that a
new project will very likely be refused, stands until a first call is made.

## What is still John's before any run

A key for the project, which he makes and saves himself; the change that lets the key-saving
script take a Google key; and his go naming Google and one dollar figure. The ceiling is ruled
at $10 (`docs/rulings/2026-11-20-google-ceiling.md`) and the terms are ruled
(`docs/rulings/2026-11-20-google-run-within-terms.md`). The last safe day is 2026-11-29.
