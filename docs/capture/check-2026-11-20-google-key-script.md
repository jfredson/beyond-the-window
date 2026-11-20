# Check of the change that lets the key-saving script take the Google key (2026-11-20)

Written by Claude (Fable 5.2), an AI model, in a session that did not write the change. It
checks [the pull request "Key swap script: save and test the Google key for Beyond the Window"](https://github.com/jfredson/timeassembler/pull/143)
(number 143 in the private TimeAssembler repository), at its one commit (`0a25b72`), against
that repository's `main` branch (`2ab1084`). The pull request follows John's ruling of
2026-11-20, "Yes, change the script"
(`docs/rulings/2026-11-20-key-saving-script-takes-a-google-key.md`, decided by: mixed).

This session changed nothing in the pull request, merged nothing, and left no comment on it.
John's checked-out copy of TimeAssembler was not touched: the two versions of each file were
read out of the repository's history into a scratch folder and run from there. No key file was
opened by this session. No key value was read, printed or typed. Every save was run with
made-up values on scratch files.

## Verdict

**Fit to merge. Nothing must be fixed first.** John may merge the pull request and save his
Google key with the changed script.

- The key value does not reach the screen, any command's arguments, the address, or any file
  other than its own line.
- The Anthropic line in the shared file comes through a Google save unchanged, and a Google
  line comes through an Anthropic save unchanged.
- The six older key names behave as they do on `main`.
- The Google test asks no model anything, and Google's pages give good reason to believe it
  costs nothing, though no page says so in those words.
- The pull request holds the script, its README and one guide, and nothing else. It adds no
  OpenAI key and it is not merged.

There are three should-fix points. None needs to hold the merge. The first is a small gap in
the refusal of a key pasted under the wrong name. The other two are sentences in the README
and the routing guide that are no longer true.

## Must-fix

None.

## Should-fix

**1. The refusal of a wrong company's key only catches text that starts exactly `sk-`.**
Where: `tools/rotate-key/rotate-key.sh`, lines 179 to 181 (the `sk-*` test inside the Google
branch).

What is wrong: if an Anthropic or OpenAI key is pasted under the Google name with anything in
front of it, the test does not see it, and the script sends that key to Google in the request
header. Two ways this could happen: the key is copied with a quotation mark in front, or a
whole line is copied out of a key file (`BTW_CAPTURE_ANTHROPIC_API_KEY=sk-ant-...`). I ran
both with made-up values and a stand-in for Google: one call was made in each case, where the
plain `sk-` paste made none. With the real Google the answer would be 400 and nothing would be
written, so the file is safe either way. The harm is only that a key belonging to one company
would have been shown to another, and would then need replacing.

How likely: low. John copies the Google key with the copy button in Google AI Studio, which
gives no quotation marks.

Suggested fix: before the test, strip any leading quotation marks from the pasted text, and
refuse the text if `sk-ant-` or `sk-proj-` appears anywhere in it, as well as when it starts
`sk-`. A real Google key will not hold either of those seven-character runs by chance.

**2. The README and the routing guide still say this project's Anthropic key is not saved.**
Where: `tools/rotate-key/README.md`, the paragraph beginning "John created the "Beyond the
Window" workspace" ("The key is not saved on this Mac yet. Until John runs the script ...
`--check` reports "no file" for this name"); and `docs/session-routing.md`, the paragraph under
the key table ("created by John on 2026-11-19 with no expiry and not yet saved to its file").

What is wrong: the key is saved and works. I ran the script's check for that name with both
versions on 2026-11-20 and both printed "works". The pull request's own description says the
same and says the sentences were left as they were. The routing guide's sentence is in a
paragraph the pull request edits, so the paragraph now carries today's date beside a statement
that is out of date.

Suggested fix: change both to say the key was saved and tested on the day it was, and drop
the sentence about "no file". This can be a later change. It does not affect the script.

**3. The README states as fact something nobody has seen.** Where:
`tools/rotate-key/README.md`, section "The Google key for Beyond the Window": "Google answers
200 for a working key".

What is wrong: no real Google key exists, so nobody has seen Google answer 200 to this call.
The sentence rests on Google's troubleshooting page, which speaks of "A 200 OK response from
models.list". That is good support, but it is not a test.

Suggested fix: "Google's pages say it answers 200 for a key that exists", until John's first
save shows it.

Two smaller points, neither worth a change on its own: one line in the README's section on
checking keys runs to about 160 characters where the rest are wrapped; and the alignment of the
check's printed columns is off for the two long Beyond the Window names, as it already was for
the first of them on `main`.

## What I ran and what it showed

Both versions of the script were copied to a scratch folder. A stand-in for `curl` (the
program the script uses to reach Anthropic and Google) was placed first in the search path. It
makes no connection, records the arguments and the standard input it is given, and prints
whichever answer code the test asks for. The home folder was pointed at the scratch folder, or
the script's own `--file <scratch path>` option was used.

### 1. Can the key value get out?

No way found.

- **Arguments and address.** The stand-in recorded 100 calls across the side-by-side run. No
  argument line held a made-up value. The Google call's arguments are exactly
  `-s -o /dev/null -w %{http_code} --max-time 20 https://generativelanguage.googleapis.com/v1beta/models?pageSize=1 -H @-`.
  The key arrives on standard input as one header line, `x-goog-api-key: <value>`. The address
  holds no key. Google's own example for this call puts the key in the address (`?key=`), and
  the script rightly does not.
- **Environment.** The script does not put the pasted key into the environment of `curl`. (The
  writing step hands the new key to `awk`, a text tool, through the environment for the moment
  it runs. That is how `main` already works for every key, and is unchanged.)
- **Screen.** I ran the Google name at a pretend keyboard (a pseudo-terminal) and typed a
  made-up value. Nothing of it showed: no run of eight characters of the value appeared in what
  the terminal displayed. The only part of a key ever printed is its last four characters.
- **Files.** After every save the made-up value was in the key file and nowhere else in the
  scratch home. No temporary file was left behind in any case. The saved file's mode is 600
  (owner only).
- **Error paths.** Each prints a fixed sentence with at most the answer code and the file's
  path: Google answering 400, Google answering 403, no network, `curl` itself failing, nothing
  pasted, a wrong company's key, a folder that cannot be written to (the message names the
  temporary file's path only, and the old file is left whole). None printed any part of a
  value. The script has no logging and never switches on command tracing.
- **Redirects.** The script does not tell `curl` to follow redirects, so the key cannot be
  carried to a second address. A real call with a made-up value showed no redirect.

### 2. Is the Anthropic line in the shared file safe?

Yes. Each case compares the file before and after, byte for byte, with made-up values.

| Scratch file before | Save | What changed |
|---|---|---|
| A comment, an Anthropic line, another line with a trailing note, a blank line, a commented-out Google line, a quoted OpenAI line | Google, no Google line yet | One line added at the end. Nothing else. |
| The same, now with a Google line | Google again | Only the Google line. |
| The same | Google, same value again | Nothing. The script says the key is the one already stored. |
| The same | Anthropic | Only the Anthropic line. The Google line untouched. |
| Both lines with `export` in front and quotation marks | Google | Only the Google line, rewritten without `export` or quotes. The Anthropic line kept its `export` and quotes. |
| The same | Anthropic | Only the Anthropic line. |
| No final newline, Anthropic line last, no Google line | Google | The Google line added. The Anthropic line gained the newline it lacked and is otherwise the same. |
| No final newline, Google line last | Anthropic | Only the Anthropic line. The Google line gained a newline and is otherwise the same. |
| Windows line endings, an empty Google line, a second Google line, and a line named `BTW_CAPTURE_GOOGLE_API_KEY_OLD` | Google, with a value full of awkward characters (`\`, `&`, `$`, `=`, `%s`) | The two Google lines became one, holding the value exactly as pasted. The Anthropic line and the look-alike `_OLD` line untouched. |
| No file | Google | A new file with the one line, mode 600. |

The two line names cannot be mistaken for each other or for plain `ANTHROPIC_API_KEY`, because
the script matches a name only at the start of a line and only when `=` follows it directly.

### 3. Do the six older names behave as on `main`?

Yes. Each of the six names was run through both versions with fourteen inputs: a good key
with awkward characters, a key with spaces round it, a refused key, no network, nothing, text
that is not a key, a Google-shaped value, an OpenAI-shaped value, an admin key, the check with
answers 200 and 401, a save to another file, and two malformed uses of the `--file` option.
With one extra case that makes 85. What was printed, the exit code, every file in the scratch
home with its mode, and what `curl` was handed were compared.

- 79 cases were the same in every respect.
- 6 differed in one line only: the usage text, shown when `--file` has no path after it, lists
  the key names, and the list now has the new name on the end. That is the change itself.

I also ran the real check (`--check <name>`) for each of the six names with both versions and
compared the printed lines. All six matched. Only the printed lines were read, and no key
ending is repeated here.

### 4. Does the Google test cost nothing and ask no model anything?

**It asks no model anything. That is certain.** The call is `models.list`: it returns
descriptions of models (names, limits, supported methods). Google's
[list-models reference page](https://aistudio.google.com/api-reference/models/list-models)
describes it as "Lists the Models available through the Gemini API", with the address
`GET https://generativelanguage.googleapis.com/v1beta/models` and the optional settings
`pageSize` and `pageToken`. No prompt is sent and no model produces anything.

**That it costs nothing is very likely, and Google does not say it in those words.** I opened
these pages on 2026-11-20 (the `ai.google.dev` addresses now redirect to `aistudio.google.com`):

- Google's [billing page](https://aistudio.google.com/docs/billing), under "What am I billed
  for?": "Gemini API pricing is based on the following: Input token count, Output token count,
  Cached token count, Cached token storage duration." Listing models reads and writes no
  tokens and stores nothing, so none of the four applies. The pull request does not cite this
  page, and it is the strongest support there is.
- Google's [troubleshooting page](https://aistudio.google.com/docs/troubleshooting):
  "Read-only metadata endpoints such as models.list (GET /v1beta/models) only validate that
  your API key exists and don't check project tier eligibility or billing status." A call that
  does not look at billing is hard to bill.
- Google's [pricing page](https://aistudio.google.com/docs/pricing) prices models per million
  tokens and some tools per thousand requests. I did not read all of that long page word for
  word. A reader working for this session read the first third and summarised the rest, and
  found no charge for listing models.
- Google's [API reference overview](https://aistudio.google.com/api-reference): "To
  authenticate, pass your API key in the x-goog-api-key header". The script does this.

The writer is right that no page says "listing models is free". Does that matter? Little. The
risk is that Google charges for a call it does not list a price for, on a page that lists what
it charges for. I put the chance that one check costs anything at well under one in a hundred,
and if it did, the amount would be a fraction of a cent. That one-in-a-hundred figure is my
judgment, not a measurement. The one way to be fully sure is to look at the project's billing
report the day after the first real save, which costs John a minute.

One real call was made to Google from the script with a made-up value: answer 400, "API key not
valid", file unchanged. The same call with no key at all gives 403. So Google reads the header
the script sends.

### 5. The refusal of `sk-`, and leaving the rest to Google

- A value starting `sk-ant-` and one starting `sk-proj-`, given to the Google name: refused
  with "that looks like an Anthropic or OpenAI key", no call made (the stand-in recorded none),
  file unchanged. The gap is should-fix 1 above.
- A Google-shaped value given to the Anthropic name is refused as before, with no call.
- **Leaving the rest to Google is sound, and it is the right choice.** Google's
  [page on API keys](https://aistudio.google.com/docs/api-key) states no prefix, length or
  character set for a key. It also says: "Starting May 28, 2026, all new API keys created in
  Google AI Studio are automatically created as auth keys", a newer kind tied to a service
  account. The key John makes will be of that kind, and Google does not say what it looks
  like. A script that demanded the older familiar shape could have refused a real key. This
  one cannot: the only texts it refuses are an empty paste and one starting `sk-`.
- A wrong paste that is not a key at all (a whole line, a value in quotation marks) goes to
  Google, is answered 400, and nothing is written.

### 6. Does the pull request hold anything beyond the ruling?

No. It is one commit changing three files: the script, its README and
`docs/session-routing.md`. No OpenAI key name is added, and both documents say John has not
ruled on one. No other tool is changed. The pull request is open, not merged, and its
description says the merge is John's. The new name is added to the list that the check walks
through when given no name, so a check of all keys will, once the Google key is saved, send it
to Google for the free test. That follows from the ruling ("tests it against Google at no
cost").

The README and the routing guide hold no key value and no key ending for the new key. I
searched both, and the script, for anything shaped like a key. What they say about the Google
key, its file, its line name, the two models and the last safe day (2026-11-29) matches this
repository's records. What is not true as written is in should-fix 2 and 3.

### 7. Syntax checks

`bash -n` passes for both versions. `shellcheck` is not installed on this Mac, so it was not
run, by the writer or by me.

## What I could not check

- **The path where Google says yes.** No real Google key exists, so nobody has seen the real
  Google answer 200 to this call. Every "saved, and it works" in the tests came from the
  stand-in. The first real run will be John's. If Google refuses a key he has just copied,
  the script stops with Google's answer code and writes nothing, so a failure there costs
  nothing and loses nothing.
- **The newer kind of key ("auth key") with this call.** Google's pages say a key is passed in
  the `x-goog-api-key` header and name both kinds of key in the same breath, but no page shows
  the newer kind used on `models.list`. Untested by anyone.
- **Whether a key that passes will be accepted when a model is asked.** Google's troubleshooting
  page says a pass here does not guarantee it. The README says this plainly. Only the run
  itself, or a first real question to a model, shows it.
- **That listing models is free, in Google's own words.** See section 4.
- **The whole pricing page, word for word.** Part was read through a summary.
- **`shellcheck`.** Not installed.
- **The real key file.** I did not open it, by rule. The shared-file tests were run on scratch
  files built to resemble it, so a layout in the real file that I did not think of is not
  covered. The cases above cover comments, blank lines, `export`, quotation marks, Windows
  line endings, duplicate lines, a look-alike name and a missing final newline.

## Noticed in passing, not part of this change

- When the network is down, both versions print "rejected the pasted key (answer 000000)":
  the code is doubled, and "rejected" is not what happened. It is the same on `main`.
- The pull request's description lists some older keys that the check now reports as refused.
  My run of the check agrees with it. That is for the TimeAssembler side to follow up, not
  this project.
