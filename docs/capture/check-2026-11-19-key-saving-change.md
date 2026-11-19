# Check of the change to the key-saving script (2026-11-19)

Written by Claude (Fable 5.2), an AI model, in a session that did not write the change. It
checks [the pull request that adds this project's key name to the key-saving script](https://github.com/jfredson/timeassembler/pull/142)
(number 142 in the TimeAssembler repository), at its newest commit (`f5528f1`, "Key swap script
documents: Beyond the Window workspace and key now exist"). That pull request is open against
the branch of [the older pull request that adds the key-saving script itself](https://github.com/jfredson/timeassembler/pull/141)
(number 141), which is also not merged.

This session fixed nothing, merged nothing, and left no comment on either pull request. Every
test used made-up values, in a scratch folder, with the home folder pointed at the scratch
folder and a stand-in for `curl` (the program the script uses to reach Anthropic) that makes no
connection. No real key file was read, listed or copied. No service was called, no key was
handled, and nothing was spent.

## Verdict

**Yes. John may merge the pull request and save his key with the changed script.** Nothing in
the pull request must be fixed first. The script does what the ruling asked: it writes one
line, `BTW_CAPTURE_ANTHROPIC_API_KEY=` followed by the key with no quotation marks, into
`~/.config/sentient-horizons/beyond-the-window.env`, in a file only its owner can read, and the
approved load command gives back exactly that value. The five older key names behave exactly
as before.

Three things outside the pull request need care before John acts. They are in this
repository's step list (`docs/capture/what-john-needs-to-do.md`) or on the Mac, not in the
changed script:

1. **The order of the two merges.** The step list says the older pull request first. Done that
   way, the change can end up on a branch that is never merged. The newer one goes first. See
   must-fix 1.
2. **The copy of the script on the Mac is the old one** until it is brought up to date after
   the merge. See must-fix 2.
3. **Whether a session may run the script's check** now touches this project's key, and the
   TimeAssembler guide says a session may. See should-fix 1.

## Must-fix

None of these is in the pull request. Both are in what John is told to do.

**1. The merge order in the step list would strand the change.** Where:
`docs/capture/what-john-needs-to-do.md`, "What is left before the Anthropic run, in order",
point 2: "The older pull request ... first, then the new one, which is open against the older
one's branch."

Why: the newer pull request (142) does not go into `main`. It goes into the older one's branch
(`claude/rotate-key-2026-11-16`). If the older one (141) is merged into `main` first, its
branch stays where it is, because the TimeAssembler repository does not delete a branch when
its pull request is merged (the repository's setting `delete_branch_on_merge` is `false`; read
with `gh api repos/jfredson/timeassembler`). Merging the newer one afterwards then puts the
change on that leftover branch, and `main` never receives it. It would reach `main` only if
John deleted the older branch by hand between the two merges, which makes GitHub point the
newer pull request at `main`.

The order that needs no such step: **merge the newer pull request (142) first**, which adds its
two commits to the older one's branch, **then merge the older one (141) into `main`**. The
newer pull request's own description says the same: "Merging this one adds the change to that
pull request; nothing reaches `main` until John merges that one."

What I ran: `git merge-tree --write-tree` for each merge, which works out the result without
touching any branch. The newer into the older: no conflict. The result into `main`: no
conflict, and the files come out identical to the newer branch's own files, because `main` has
not moved since the older branch was cut (`git merge-base` gives `main`'s newest commit,
`3a56aa6`, and GitHub's `main` is at the same commit). No other pull request is open in that
repository.

**2. After the merge, the Mac still holds the old script.** Where: the same step list, step 6,
which will name the path `~/Code/timeassembler/tools/rotate-key/rotate-key.sh`.

Why: a merge on GitHub changes nothing on the Mac. The folder `~/Code/timeassembler` is at
present on the older pull request's branch (`claude/rotate-key-2026-11-16`, commit `29ba695`),
with no uncommitted changes, and the script at that path is the old one. Run with this
project's key name it answers `Stopped: unknown key name "beyond-the-window-capture"` and
saves nothing. So the step list needs one step between the merges and the save, which brings
that folder up to date, and one command that proves it. This command is the proof, and it
makes no call to any service while no key is saved:

```bash
~/Code/timeassembler/tools/rotate-key/rotate-key.sh --check beyond-the-window-capture
```

The changed script answers `beyond-the-window-capture no file at` followed by the file's path.
The old script answers `Stopped: unknown key name`. Which git commands bring the folder up to
date depends on how John merges, and other sessions share that folder, so I leave them to the
session that writes the step.

## Should-fix

**1. The TimeAssembler guide tells sessions they may run the check, and the check now reaches
this project's key.** Where: `docs/session-routing.md` in the TimeAssembler repository,
"Standing rules", rule 1: "`tools/rotate-key/rotate-key.sh --check` tests every stored key and
prints only its last 4 characters ... A session can run this." The pull request did not change
that sentence, and its README says the same ("A Claude session can run this safely").

Why: with the sixth name added, `--check` with no name reads this project's key file and sends
the key to Anthropic's token counter, once John has saved it. The script never shows the value
to the session that runs it, only the last four characters. But this project's step list
(step 6, "Who runs it") says that whether a session may run the check is not settled, and that
until John says, the check is his. A session in another project that follows the TimeAssembler
guide would not know that. Either John rules that a session may run the check for this key, or
the guide and the README say that for this one key the check is his. This is his to rule, and
it is better settled before the key is saved.

**2. The check and the save should always name the key.** Where: the commands still to be
written into step 6 of the step list.

Why: `--check` with no name tests all six names. It sends each of the five other projects'
stored keys to Anthropic as well, four of which the guide says expired on 2026-11-17, so it
makes up to six calls where this project's ruling allowed "one named call". The command above,
with the name on the end, tests this key alone.

**3. The name to type is `beyond-the-window-capture`, not `btw-capture`.** Where: step 5 of the
step list asks for the Console key to be named `btw-capture`. The script knows the key only as
`beyond-the-window-capture`. Typing `btw-capture` gives `Stopped: unknown key name`. The step
list already reports the script's name as "as reported"; this check confirms it. The README and
the guide both say plainly that the two names may differ, which is true and harmless, since
the script's name only picks the file and the line.

**4. The pull request's description is out of date in one sentence.** Where: the description
of pull request 142, "Both say the Console workspace and the key do not exist yet and are
John's to create." Why: the second commit (`f5528f1`) changed both documents to say that John
created them on 2026-11-19. The documents are right and the description is not.

**5. The guide's new row gives a spend limit of "none" that nobody recorded.** Where:
`docs/session-routing.md`, the new "Beyond the Window" row, last column. Why: no session saw
the Console, and I found no record in this repository of John saying what limit, if any, the
new workspace has. "Not known" would be the true entry until he says.

**6. The README's instruction for adding a key is now one line short.** Where:
`tools/rotate-key/README.md`, "A new key gets one more line in the `key_file` list at the top
of the script." Why: a new name also has to be added to the `ALL_KEYS` list, or `--check`
skips it, and to `key_var` if its line has its own name. The first part was already true
before this change.

## The eight questions, with what I ran

The two versions of the script were copied out of git into a scratch folder with
`git show <branch>:tools/rotate-key/rotate-key.sh`. Nothing in `~/Code/timeassembler` was
edited and no branch was switched. The stand-in for `curl` wrote down the arguments and the
input it was given and printed a fixed answer code.

**1. Does saving write exactly one line, readable by its owner only, and replace only its own
line?** Yes.

- Into a folder with no file: the file holds the 58 bytes
  `BTW_CAPTURE_ANTHROPIC_API_KEY=sk-ant-api03-MADEUPaaaa1111` and a line end, nothing else,
  read byte by byte with `od -c`. Its mode is `-rw-------`, owner only.
- Into a file made readable by everyone, holding a comment, a `BTW_CAPTURE_GOOGLE_API_KEY=`
  line, an older `BTW_CAPTURE_ANTHROPIC_API_KEY=` line, a `BTW_CAPTURE_OPENAI_API_KEY=` line
  and a plain `ANTHROPIC_API_KEY=` line: `diff` of before and after shows the one line changed
  and no other. The file's mode became owner only. No other file was left in the folder.
- Into a file with the comment and the two other companies' lines and no line of its own, and
  no line end after the last line: the new line is added at the end and the other three are
  unchanged.

**2. Does the approved load command give back exactly what the script wrote?** Yes, for
everything the script can write.

- Values holding `=`, `&`, `/`, `\`, `$`, a percent sign, backticks, `$(id)`, both kinds of
  quotation mark, and the two characters backslash and "n": each came back from the load
  command character for character (compared with Python's `repr`), and nothing in them was
  run or expanded.
- **A trailing space or carriage return cannot be written by the script.** It removes every
  space, tab and line-end character from what is pasted before it tests or saves it. A paste
  of the value followed by a space and a carriage return was saved clean.
- Files the script did not write, made by hand to see what the load command does:

  | The file's line | The Terminal window then holds | The capture script receives |
  |---|---|---|
  | the value, then a space | the value and the space | the value alone; it trims spaces at both ends (`capture.py`, `read_key`) |
  | the value, then a carriage return | the value and the carriage return | the value alone, for the same reason |
  | the line twice, with different values | both values, with a line break between | both values with the line break; see the note below |
  | the value inside quotation marks | the value with the quotation marks | the value with the quotation marks, which Anthropic would refuse |
  | the line with `export ` in front | nothing | nothing; it stops with "the environment variable ... is not set" |

- **The script and the load command disagree about three of those hand-made files.** For the
  doubled line, the quoted value and the `export` line, the script's check reads the file its
  own way (the last such line, quotation marks removed, `export` allowed) and would report the
  key as working, while the load command hands the capture script something else. This cannot
  arise from the script's own saving: saving over each of those files left exactly one plain
  line, and the load command then gave back the value. It matters only if the file is edited
  by hand.

**3. Do the five existing key names behave exactly as before?** Yes. Forty-six cases, each run
through the old script and the new one in separate fresh scratch folders: for each of the five
names, a good save of an awkward value, a save with spaces around the value, a key the service
rejects, an empty paste, text that is not a key, an admin key, a check that is accepted, a
check that is rejected, and a save to another file with `--file`; plus a save of the key
already stored. The starting files included a file with no key line, a line with `export` and
quotation marks, a line that appears twice, a line ending in a carriage return, a neighbouring
`ANTHROPIC_API_KEY_OLD=` line, a `BTW_CAPTURE_ANTHROPIC_API_KEY=` line in another project's
file, and a missing file. What was printed, the exit code, every file's contents and mode, and
what was handed to `curl` were identical in all forty-six. A save under `ta-voice` left the
`BTW_CAPTURE_ANTHROPIC_API_KEY=` line in that file alone.

Three differences, all expected: `--check` with no name prints a sixth row for the new name;
and the list of known names, shown for an unknown name or for no arguments, has the new name
on the end.

**4. Is the value ever printed, logged, left in a temporary file, put on a command line, or
written anywhere else? Is the hidden prompt hidden?**

- **Printed:** only its last four characters, and the last four of the key it replaced. That
  is the script's design and is unchanged. The whole value never appeared in anything printed.
- **The hidden prompt:** yes. I ran the changed script at a pretend keyboard (a
  pseudo-terminal, made with Python's `pty`), typed a made-up value at the prompt, and
  searched everything the terminal showed. Neither the value nor any eight characters in a row
  of it appeared. The pull request's author had not tested this.
- **Command lines:** the value is never an argument to any program. `curl` receives it on its
  input, and the stand-in's record of its arguments held no value in any case.
- **One thing short of that, unchanged by this pull request:** when the file already exists,
  the script hands the new value to `awk` (the program that rewrites the file) as a setting in
  that one program's environment, for the instant it runs (line 93). Another program running
  as John, or as the Mac's administrator, could read it in that instant. A program running as
  any other user could not. The value is not handed to `curl` that way, which the stand-in
  confirmed.
- **Temporary file:** the script writes the new file beside the old one under a random name,
  readable by its owner only, and moves it into place. After every successful save and every
  refusal, no such file was left. If the script were interrupted or the disk filled in the
  moment between writing and moving, that file would stay in the same folder holding the key,
  still owner only. Unchanged by this pull request.
- **Logged or written elsewhere:** no. The script has no log. After the pretend-keyboard run,
  the only file under the scratch home holding the value was the key file.
- **A small point:** if the folder `~/.config/sentient-horizons` did not exist, the script
  would create it open to other users to list (mode 755), though the file inside is owner
  only. The workspace's instruction file says that folder already holds keys, so it exists. I
  did not look at the real folder.

**5. The key test.** Read from the code only (lines 51 to 58, the function `http_status`); no
call was made. It sends one request to `https://api.anthropic.com/v1/messages/count_tokens`,
with the body `{"model":"claude-haiku-4-5","messages":[{"role":"user","content":"hi"}]}`, the
key in an `x-api-key` header given to `curl` on its input, and a 20-second limit. It keeps only
the answer's status number and throws the body away. `diff` of that function between the old
branch and the new one shows no difference, and it is the only place in the script that names
an address or runs `curl`. The new name reaches it through the same two paths as every other
name: the save (line 144) and the check (line 77). This matches the ruling
(`docs/rulings/2026-11-19-key-test-stays.md`) word for word: the token counter, "hi",
`claude-haiku-4-5`.

**6. Do the README and the guide's keys table say true things?**

| The claim | True? |
|---|---|
| The name `beyond-the-window-capture`, the file `~/.config/sentient-horizons/beyond-the-window.env`, the line `BTW_CAPTURE_ANTHROPIC_API_KEY=` | Yes, all three match the script and the capture script's own setting name |
| John created the workspace and key on 2026-11-19 with no expiry, in his words "Done, no expiry" | Matches this repository's record of his words (`what-john-needs-to-do.md`, step 5). No session saw the Console, and both documents rest on his word, as they say |
| John has not confirmed the Console name; the step list asked for `btw-capture` | Matches the step list |
| The key is not yet saved | Matches the step list. I did not look at the real folder to confirm it, on purpose |
| Only that one line is replaced; Anthropic keys only, with John's words "Yes, Anthropic only" | Yes, tested, and the quotation matches the ruling |
| `--check` reports "no file" for this name until the key is saved | Yes, tested |
| The README's account of what was tested on 2026-11-19 | Consistent with the pull request's description; I repeated each of those tests and they hold |
| No key value anywhere | Yes. A search of the three changed files on the branch for anything shaped like an Anthropic key found none |
| Spend limit "none" | Not recorded anywhere I could find. See should-fix 5 |

"The first five keys were created 2026-10-18" replaces "All five keys were created
2026-10-18" and is the same claim as before.

**7. What happens at the two merges?** No conflict at either, and after both, `main` holds
exactly the files of the newer branch. Nothing in the repository points at the wrong place
afterwards: the only other mentions of the script are the two rules in the guide, which name
its path correctly. The danger is the order, which is must-fix 1, and the Mac's own copy, which
is must-fix 2. One small thing: once the newer pull request is merged into the older one, the
older one's title, "Anthropic API keys: a swap script, and a record that none is in use", no
longer covers everything in it.

**8. Do the step list's steps match the script, command for command?** The step list was
changed by another session while this check ran (the commit `e786dba`, "Capture step list: the
key-loading command is ruled, the key is made, and what is left before the Anthropic run, in
order"). I read it as it stands after that commit. It now says on purpose that the commands
for saving this key are not written yet and will be added when this check lands. So there is
no save command to compare. What is there, against the script:

- **The merge order is the wrong way round** ("What is left", point 2). Must-fix 1.
- **Nothing says the Mac's copy must be brought up to date after the merge.** Must-fix 2.
- **Step 6 says "Run the key-saving script once for each key".** The script can save only the
  Anthropic key. It refuses anything that does not begin `sk-ant-`. Step 4 says so; step 6's
  first sentence does not.
- **Step 5's key name `btw-capture` is not a name the script knows.** Should-fix 3.
- **Step 6's older sentence, "A session can then run the script's check",** is already marked
  in the step list as written before the ruling and not settled. The script's check does read
  the key file and make the same call, as that note says. Should-fix 1.
- **Step 6 says the check "prints only a key's last four characters".** True. It also prints
  the key's name and `works` or `REJECTED (answer ...)` with the status number.
- **The load command (step 2 of "The Anthropic run, step by step")** matches the file the
  script writes. The condition attached to the ruling of that command, that the line is
  written with no quotation marks, is met.
- **Step 2's kept record says the real file "does not exist until step 4's change is made".**
  More exactly, it does not exist until John saves the key with the changed script.
- **The script's last line** after a save is "Done. Tell Claude the new ending so the routing
  guide's key table is updated." The step list does not mention telling a session the key's
  last four characters. Whether they are written into the guide, as they are for two other
  keys, is John's choice.

The commands the step list will need, each tested here on made-up values:

```bash
~/Code/timeassembler/tools/rotate-key/rotate-key.sh beyond-the-window-capture
```

It prints `Paste the new "beyond-the-window-capture" key and press Return (nothing will
show):`, and after a good key, `"beyond-the-window-capture": new key saved, ends` with the
last four characters, `and it works.`, then the file's path, then the closing line quoted
above. The check afterwards is the command under must-fix 2, which then answers
`beyond-the-window-capture ends` with the last four characters and `works`.

## Notes

- **A doubled key line would make the capture script fail in a way that may show the key.**
  This is about `capture/capture.py`, not the pull request, and it is read from the code, not
  run. If the key file ever held the line twice, the load command would hand the capture
  script two values with a line break between them. Python's own web library refuses such a
  value with an error whose text contains the value (I confirmed that much with a made-up
  value and no connection). The capture script does not catch that kind of error before any
  answer has arrived (`capture.py`, lines 1070 to 1074), so the error's text, with both keys in
  it, may be printed in the Terminal window. The key-saving script cannot produce such a file,
  and saving over one repairs it. A follow-up for the capture script: refuse a key that holds
  a line break, in `read_key`, with a message that does not repeat the value.
- **The check's columns.** The name `beyond-the-window-capture` is 25 characters and the
  script lines its rows up at 20, so this one row sits five characters to the right of the
  others. Nothing is lost.
- **Two older weaknesses the change did not make and did not touch.** When a key line had
  `export` in front, saving rewrites it without `export`. And when a hand-made line ends in a
  space or a carriage return with no quotation marks, the script's check counts that stray
  character as part of the key, so it would show three characters of the ending and send a
  key Anthropic would reject. Neither can come from the script's own saving.
- **What this check did not cover.** A real key against Anthropic's real service; the real
  folder and file on the Mac; and the Console. All three are John's.
- **Where the test programs are.** The two I wrote (the old-against-new comparison and the
  pretend-keyboard run) are in the sessions' shared notes folder, outside this repository,
  under the name `key-saving-check-2026-11-19`. They hold made-up values only.
