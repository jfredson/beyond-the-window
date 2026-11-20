# Spending record

Every spend on this project, and John's own go for it, quoted word for word. Written by Claude
(Fable 5.2), an AI model, at John's direction. Nothing is spent without his go, and a go covers
what it names and nothing else. If he withdraws a go, it is taken out of this record, block and
all.

The monthly Anthropic credits that come with John's plan pay for the Anthropic run below
(vendor: Anthropic credits). The Google run is paid out of John's pocket (vendor: Google). As of
2026-11-20 the project has spent $0.2130 out of pocket, all of it on the Google run.

## 2026-11-19: the Anthropic run of the sealed capture

John gave this go on 2026-11-19, typed by him in conversation with the master planning session,
after the session set out what it permits (the ten approved questions, each asked five times,
of Claude Sonnet 4.5 before its withdrawal on 2026-11-30, up to $10, expected cost $1.89) and
what it does not (any other model or run, publishing any answer, anyone reading the answers
before a method for comparing them is written, checked and ruled). **Decided by: John.**

> Go for the sealed capture as written in docs/capture/ at commit 890b24b. Anthropic, up to $10.

```sealed-capture-go
run = "anthropic-2026-11-30"
date = "2026-11-19"
commit = "890b24b"
ceiling_usd = "10.00"
johns_words = "Anthropic, up to $10"
messages_sha256 = "d53fcc637b879aa05e29dbeb5cd347d496404cb27d8f2885ca5fa1efda5ff617"
```

The commit he names is the one that recorded the site's first release. The capture's script,
plan and ten message files are unchanged between the commit at which the capture documents were
settled (`485962c`) and that one.

**The run was made on 2026-11-19, and it is complete.** On John's word ("Yes, run it") the
master planning session ran it from this Mac: the dry look, then one question alone, then the
rest.

- 50 exchanges with Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`): the ten approved
  messages, each asked five times, each a new exchange.
- All 50 came back as a reply that ended normally, and in all 50 the service reported the
  model's name as expected. No attempt failed and none was repeated. The script's fault check
  flagged no file.
- **Counted cost: $0.2667 of the $10.00 ceiling** (vendor: Anthropic credits). The estimate was
  $1.89; the replies were much shorter than the estimate assumed, 170 to 276 words each.
- The replies are kept outside every repository. The list of their file names and checksums
  is `docs/capture/manifest.md`, and the script confirms the folder matches the list.
- Nobody has read the replies. The session saw labels, counts and costs only.

Still for John: compare the total with the Usage page in the Anthropic Console.

This go is used up. It covers nothing further.

## 2026-11-20: the Google run of the sealed capture

John gave this go on 2026-11-20, typed by him in conversation with the master planning session,
after the session set out what it permits (the ten approved questions, each asked five times,
of Gemini 2.5 Pro and Gemini 2.5 Flash before their withdrawal on 2026-12-01, 100 exchanges, up
to $10 out of his own pocket, expected cost $3.79) and what it does not (any other model or
run, publishing any answer, anyone reading the answers before a method for comparing them is
written, checked and ruled). He was also told that Google may refuse to serve these models to
the project, that the run may stop after one call if the service reports a model's name other
than the one the plan expects, and that the script's own limit is the only stop on the cost.
**Decided by: John.**

> Go for the sealed capture as written in docs/capture/ at commit 33ac89e. Google, up to $10.

```sealed-capture-go
run = "google-2026-12-01"
date = "2026-11-20"
commit = "33ac89e"
ceiling_usd = "10.00"
johns_words = "Google, up to $10"
messages_sha256 = "d53fcc637b879aa05e29dbeb5cd347d496404cb27d8f2885ca5fa1efda5ff617"
```

The commit he names is the last one of 2026-11-20 before the go. The capture's script, plan and
ten message files are unchanged between the commit named in the Anthropic go (`890b24b`) and
that one.

**Tried on 2026-11-20, and refused by Google. Nothing was spent.** On John's word ("Yes, run
it") the master planning session ran the script from this Mac, one question alone to each
model, with the key loaded for each command only.

- Gemini 2.5 Pro: one call. Google answered with its "not found" error (number 404) and the
  message "This model models/gemini-2.5-pro is no longer available to new users."
- Gemini 2.5 Flash: one call. The same error, with the message "This model
  models/gemini-2.5-flash is no longer available to new users."
- No model replied. Each call is kept as a failed attempt, with no reply in it. **Counted cost:
  $0.0000 of the $10.00 ceiling** (vendor: Google).
- This is the outcome the capture's documents expected for a project made new
  (`docs/capture/cost-and-terms.md`, Part 3). John's Google account had used Gemini 2.5 Flash
  through another project, and the new project was refused all the same, so Google's "users"
  reads as projects and not accounts. That reading is the session's.

The session stopped there. The go stands and is not used up: it covers this run up to $10 and
nothing else. Whether to try any other way before the last safe day, 2026-11-29, is John's to
decide.

**Tried again the same day through an older Google project of John's, on his ruling ("Yes, try
it"; `docs/rulings/2026-11-20-google-run-through-an-older-project.md`, decided by: mixed). The
run is complete for Gemini 2.5 Flash. Gemini 2.5 Pro was refused again and was not asked.**
John made a new key in the older project for this capture alone and saved it himself. The
master planning session ran the script from this Mac: one question alone to each model, then
the rest for the model that answered.

- **Gemini 2.5 Flash** (`gemini-2.5-flash`): 50 exchanges, the ten approved messages each asked
  five times, each a new exchange. All 50 came back as a reply that ended normally, and in all
  50 the service reported the model's name as the plan expects. No attempt through the older
  project failed and none was repeated. The script's fault check flagged no file. The replies
  run from 78 to 605 words.
- **Gemini 2.5 Pro** (`gemini-2.5-pro`): one call through the older project, refused with the
  same error and message as before. That project has no record of using the model. No reply
  exists, and there is no route left to this model.
- **Counted cost: $0.2130 of the $10.00 ceiling** (vendor: Google, out of John's pocket). The
  estimate for both models was $3.79, of which $0.76 was for this model.
- The reply folder now also holds three failed attempts with no reply in them: one for each
  model from the new project, and one for Gemini 2.5 Pro from the older one.
- The replies are kept outside every repository. The list of their file names and checksums
  is `docs/capture/manifest.md`, and the script confirms the folder matches the list.
- Nobody has read the replies. The session saw labels, counts and costs only.
- For this run the project's guideline that its calls never go through another project's key
  was set aside by the ruling named above: the key was new and used for nothing else, and the
  Google project it belongs to was made for other work.

Still for John: compare the total with the cost Google shows for that project, and delete the
two keys made for this capture once he is content (the one in the new project, which Google
would not serve, and the one in the older project).

This go is used up. It covers nothing further.
