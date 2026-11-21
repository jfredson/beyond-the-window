# Check of the three fixes to the key-saving script's Google change (2026-11-20)

Written by Claude (Fable 5.2), an AI model, in a session that did not write the change. It is
the same session that wrote the first check
(`docs/capture/check-2026-11-20-google-key-script.md`), whose three should-fix points this
change is meant to make.

It checks [the pull request "Key swap script: tighter refusal under the Google name, and key notes brought up to date"](https://github.com/jfredson/timeassembler/pull/144)
(number 144 in the private TimeAssembler repository). **The exact commit checked is
`d5719e14c92b90319abb0ca96baa8209efbed19c`**, the pull request's only commit, against that
repository's `main` branch at `d6d66cbc2603919802a0122b48960c85d3fc0b41`. The script on `main`
is byte for byte the one the first check passed. John's word for this change: "Yes, fix them"
(decided by: mixed).

This session changed nothing in the pull request, merged nothing, and left no comment on it.
John's checked-out copy of TimeAssembler was not touched. No key file was opened. No key value
was read, printed or typed. Every save was run with made-up values on scratch files, with a
stand-in for `curl` (the program the script uses to reach Anthropic and Google) that makes no
connection and records what it is handed.

## Verdict

**Fit to merge. Nothing must be fixed first.**

- The three pastes named in the request are each refused under the Google name with no call
  made.
- The new code cannot change what is written for a real Google key, and the chance of it
  wrongly refusing one is too small to count.
- The six Anthropic names behave exactly as on `main`.
- No new path lets a key value reach the screen, an argument, an address or a log.
- The README and the routing guide are true as written, and the two recorded key endings
  match what the script's own check prints.
- The pull request holds the three fixes and nothing else.

Two small points are left for later, under "Could be better". Neither needs a change before
the merge.

## Must-fix

None.

## Should-fix

None.

## Could be better, at no urgency

**1. One kind of wrong paste still gets through.** Where: `tools/rotate-key/rotate-key.sh`,
line 188 (the test `sk-*|*sk-ant-*|*sk-proj-*`).

An OpenAI key of a kind that does not hold `sk-proj-` (an older key, or one for a service
account), pasted with something in front of it other than quotation marks, is still sent to
Google. I ran three such made-up pastes: a whole line `OPENAI_API_KEY=sk-svcacct-...`, a whole
line `OPENAI_API_KEY=sk-...`, and a value in round brackets. Each made one call. The same
values pasted bare are refused, because they start `sk-`.

Why it can wait: this project has no OpenAI key yet and John has not ruled on one, the
project's own OpenAI line would hold the `sk-proj-` kind, and Google would answer 400 and
nothing would be written.

Suggested fix, if it is ever wanted: also refuse text holding `=sk-`. I would not refuse `sk-`
anywhere in the text, because three characters could turn up by chance in a real Google key
about once in several thousand keys, and that would refuse a good key.

**2. The documents do not say that the Google key now stored is the second one saved that
day.** Where: `docs/session-routing.md`, the Google row of the key table, and
`tools/rotate-key/README.md`, the last paragraph of the Google section ("John made the Google
key and saved it with this script on 2026-11-20").

The sentences are true of the key now in the file. This project's records show that two
Google keys were saved on 2026-11-20: one from the new Google project, and then one made in an
older Google project of John's, after Google refused the first run
(`docs/rulings/2026-11-20-google-run-through-an-older-project.md`). The pull request was
written after the second save, and the ending it records is the stored key's. A reader of the
routing guide would not learn that an earlier key exists in the other Google project and may
still be live there. One sentence would do it. The same row still describes the run as
something ahead ("to ask ... before Google withdraws them"), though the run happened that day;
that wording was not part of this change.

## What I ran and what it showed

### 1. The tighter refusal under the Google name

Each paste below was given to both versions, with the stand-in set to answer 200, so that
anything not refused by the script itself would be "saved" and show up. "Calls" is how many
times the stand-in was reached.

| Made-up paste | `main` | Pull request 144 |
|---|---|---|
| A double quotation mark, then an `sk-ant-` value | 1 call | refused, 0 calls |
| An `sk-ant-` value in single quotation marks | 1 call | refused, 0 calls |
| The same in two pairs of double quotation marks | 1 call | refused, 0 calls |
| A whole line `BTW_CAPTURE_ANTHROPIC_API_KEY=sk-ant-...` | 1 call, and written to the file | refused, 0 calls |
| A line `export ANTHROPIC_API_KEY="sk-ant-..."` | 1 call | refused, 0 calls |
| A bare `sk-proj-` value | refused, 0 calls | refused, 0 calls |
| A whole line `BTW_CAPTURE_OPENAI_API_KEY=sk-proj-...` | 1 call, and written | refused, 0 calls |
| An `sk-proj-` value in quotation marks | 1 call | refused, 0 calls |
| An `sk-ant-` value in curly quotation marks | 1 call, and written | refused, 0 calls |
| An `sk-ant-` value in backticks | 1 call, and written | refused, 0 calls |
| Two quotation marks and nothing else; one quotation mark alone | 1 call | "nothing was pasted", 0 calls |

In every refused case the scratch file was unchanged, byte for byte. The three required cases
(a leading quotation mark, a whole `NAME=sk-ant-...` line, a value holding `sk-proj-`) are the
first, fourth, sixth and seventh rows.

**Can the new code wrongly refuse a real Google key?** Only a key that starts `sk-`, or holds
the seven characters `sk-ant-` or the eight characters `sk-proj-`. For a key of about sixty
characters that is a chance of roughly one in a hundred billion. Made-up Google-shaped values
holding near misses (`...ask-antler...`, `...desk-project...`) were accepted, as they should
be. So were a value shaped like the older kind of Google key, one with dots in it, and one
with a hyphen and an underscore.

**Can it change what is written to the file?** Only by removing quotation marks from the two
ends of the pasted text, and Google's keys do not begin or end with one. A made-up Google
value pasted in quotation marks, or with one stray mark in front, was sent to the stand-in
without the marks and saved without them. Quotation marks inside a value are left alone. On
`main` the same quoted paste was sent with its marks and ended in the confusing message "the
file did not take the new key", so this is a small improvement beyond the gap itself. The
writer asked whether dropping the marks at the end as well as the front is right. It is: with
only the front removed, a quoted key would go to Google with a stray mark and be refused for
no reason John could see.

A made-up quoted value sent to the real Google through the new script: answer 400, file
unchanged, as before.

### 2. The Anthropic names against `main`

Each of the six Anthropic names was run through both versions with nineteen inputs: the
fourteen from the first check, and five new ones (an `sk-ant-` value in double quotation
marks with answers 200 and 401, one in single quotation marks, a whole `NAME=sk-ant-...`
line, and a value with a quotation mark on the end). With one extra case that makes 115. What
was printed, the exit code, every file in the scratch home with its mode, and what `curl` was
handed were the same in all 115. The change sits wholly inside the branch for the Google
name, and the writer rightly did not extend the dropping of quotation marks to the Anthropic
names, which was not asked for.

The real check (`--check <name>`) for each of the seven names printed the same line from both
versions.

### 3. Can a key value get out on a new path?

No. The new lines only shorten the pasted text in the script's own memory and compare it. They
start no program, so nothing is handed to another command. The one changed message is a fixed
sentence with no part of the value in it. Across the side-by-side run the stand-in recorded
118 calls; no argument line held a made-up value, the Google address held none, and the
environment given to `curl` held none. A quoted made-up value typed at a pretend keyboard (a
pseudo-terminal) showed nothing of itself on the terminal, and afterwards was in the key file
and nowhere else. No temporary file was left in any case.

### 4. The README and the routing guide

True as written, with the one omission under "Could be better" 2.

- **The Anthropic key was saved on 2026-11-19.** This project's records agree: the Anthropic
  run of the sealed capture was completed that day, which needs the key in its file.
- **The Google key was made and saved on 2026-11-20, and Google answered 200 for it.** The
  script's check prints "works" for that name, and it prints that only for a 200. This
  replaces the sentence the first check called untested.
- **The two recorded endings.** I compared each against the script's own
  `--check` output for that name, inside the shell, without printing or opening anything else.
  Both match, and both keys work. The endings are not repeated here, because this repository
  is public and the routing guide's is not.
- **No key value.** A search of all three files for anything shaped like an Anthropic, OpenAI
  or Google key found nothing. The only key text is the four-character endings in the guide's
  table, as its other rows already have.
- The statements that a key "is not saved yet" or "does not exist yet" are gone from both
  documents. The test record's new paragraph matches what I saw.

### 5. Anything beyond the three fixes?

No. One commit, three files: the script (11 lines added, 3 removed, all in the Google
branch), its README and `docs/session-routing.md`. No OpenAI key name, no other tool, no
merge. The pull request is open.

`bash -n` passes. `shellcheck` is not installed on this Mac, so it was not run.

## What I could not check

- **A real Anthropic or OpenAI key pasted under the Google name.** No real key was used. The
  refusal happens before any call, so the stand-in shows the same thing.
- **A real Google key pasted in quotation marks.** The saved key was not pasted again. The
  made-up cases stand in for it.
- **Which of the day's two Google keys the recorded ending belongs to, by any means other than
  the script's check.** The check shows it is the key now stored. I did not open the key file
  or Google's site.
- **`shellcheck`.** Not installed.
