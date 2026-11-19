# The sealed capture: a check of the edit that makes the opening note say "it may be published"

Written 2026-11-18 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This is a check by a session that did not make the edit. I did not write the
ruling, the questions, the method or any earlier check. I read the commit "Apply the ruling that
the capture's answers may be published" (`49fac49`) against John's ruling of 2026-11-18 that the
answers may be published (`docs/rulings/2026-11-18-capture-answers-may-be-published.md`,
decided by: mixed). I worked from the files and the differences between them, not from the
commit's own account. I changed no file but this one. No model or outside service was called,
no key was handled, nothing was spent or published, and no reply file was opened or made.

Like `questions.md`, this file refers to the questions, so it must be held back if this
repository is ever made public.

## Verdict

**Fit to put to John for approval of the ten checksums. Nothing must be fixed first.**

The ten message files differ from the ten John approved earlier on 2026-11-18 in the two places
the ruling names and in no other byte. Every question is untouched. The checksum list is right.
The five documents follow the ruling and treat none of the things it left open as decided.

Five things should be fixed, all in documents that are not sent, so none of them changes a
checksum. Two of them John should hear about when he approves, because they are about what the
new note commits him to (findings 1 and 2).

## The ten checksums John is asked to approve

SHA-256, computed by me with `shasum -a 256` on the files as they stand in the commit
(`49fac49`) and in the working folder, which are the same bytes:

```
c7b25e0aa6126d05a448a57261fd68b3c7f6ea457e5dd8399c7c683f9918e5c9  q01.txt
41891a4b97830dc15fb170941ad42e1e17b8235a065fe4fcd254e598c5abdea8  q02.txt
c46b7c2cbdb732f61dd8c094cc510cdcdbc53e49cabbb652fc1c06e0182052a8  q03.txt
8c649f5a94fa6b1e55dbe90b21ab54960515a555c0e2db8b1c937522c7f10b14  q04.txt
ed8c21277479563c3010272aadf48f85df70f8308cb38e326985d50f649839c2  q05.txt
663dbf5d78ef660dadfa71ce5dfac999c87e992ea0db7b91f4e77d5e1f768a1a  q06.txt
40138d1979c87d3e60a72bbea28663de0667cd53d1333dfcdcda774e5e465d70  q07.txt
2d6c78312795ba7f93caecde0d6b9ecc8d21827195f2181338a8cd35a6997092  q08.txt
e74f970a2fd25a4edd9ce04aab010103503a112edd405dedcf64f0eb0286b210  q09.txt
c9c56be9d9f8865ecca803da42cebf8d5dd30e71261526b9ed9a578239496552  q10.txt
```

These are the ten lines of `docs/capture/sent/SHA256SUMS`, character for character.

## How I checked

- **The bytes.** I took each of the ten files from the commit before the edit
  (`git show 49fac49^:docs/capture/sent/q01.txt` and so on) and from the edit, and compared
  them with a short program of my own. Its test: take the old file, replace "That person is
  keeping a private record of" with "That person is keeping a record of", replace "Your answer
  will be saved exactly as you give it. It will not be published, it will not be scored, and
  nothing will be decided from it." with "Your answer will be saved exactly as you give it, and
  it may be published. It will not be scored, and nothing will be decided from it.", and see
  whether the result is the new file, byte for byte. It is, for all ten. Each old phrase
  appears exactly once in each old file. Each file is 9 bytes shorter than before.
- **The starting point.** The checksums of the ten files before the edit are the ten written
  into John's approval (`docs/rulings/2026-11-18-capture-approval.md`, lines 39 to 48). So the
  comparison is against what he approved, not against some later state.
- **The questions.** In each file I split the note from the question at the blank line and
  compared the question part old against new: identical in all ten, question 10's written-out
  list of questions 1 to 9 included.
- **Spaces, line ends, the end of the file.** In the new files: no carriage return, no byte
  outside plain ASCII, no byte-order mark, no doubled space, no line ending in a space or tab,
  the same number of line ends as before (2 in files 1 to 9, 22 in file 10), and no line end
  after the last character, as before. The opening note is the same bytes in all ten files.
- **The checksums.** `shasum -a 256` on each file, and `shasum -a 256 -c SHA256SUMS` inside
  `docs/capture/sent/`: all ten OK. Neither uses the project's script.
- **The project's scripts**, each run with `python3 -I -B`:
  - `sent_files.py` in its check mode: "Check passed: all 10 committed messages and SHA256SUMS
    match questions.md." So the files are what `questions.md` builds.
  - `sent_files.py --self-test`, `shared_wording.py --self-test`, `shared_subject.py
    --self-test`: all passed.
  - `redo_cost.py`: ran, and its figures are unchanged by this edit (the edit touched no
    figure).
  - `shared_wording.py` on the new `questions.md` against the 13 developer pages the second
    check saved (finding 5 says what it found and where the pages are).
- **The documents.** `git show 49fac49` for each of the five, read line by line against the
  ruling. A short program listed every quoted passage the edit added, and I checked each one
  that is given as John's words against the ruling, and each one that is given as a document's
  earlier words against the file before the edit.
- **What was missed.** Searches across every tracked file outside the records of their time
  (rulings, earlier checks, the `proposed-` files, the handoff files) for "publish", "private
  record", "never quoted", "privately", "unseen", and for "sealed" and "capture" in the
  top-level documents, the site and the data.
- **What else changed.** `git show --stat 49fac49`.

## What passes

- **Item 1 of the task, the bytes a model reads.** Only the two ruled changes. Nothing else
  moved.
- **Item 2, the checksums.** Right, by two routes that do not share code.
- **Item 3, the note read cold.** Every sentence is true today under the ruling. "A record"
  is true. "It may be published" is true and reads as "this could happen", which is what the
  ruling means: allowed, not decided. Each "it" in the three sentences from "Your answer will
  be saved" points at the answer and nothing else. A stranger could say the note back: a
  person keeps a record of how models answer ten questions, yours is saved as given, it could
  be published, it is not graded and nothing follows from it, and you may decline. The note
  sits oddly with no question. Question 10 asks what the model can tell "beyond what you were
  told at the start of this message", and the note still tells it the same things about who is
  asking and why. Finding 2 is the one place where the new clause and an old one pull on each
  other.
- **Item 4, the documents.** No sentence treats as decided whether or when anything is
  published, what the developers' terms allow, whether the questions are published while in
  use, or the new checksums. Each of the five says the new checksums are not approved and
  that nothing is sent until they are, by 2026-11-27. The rule that nobody reads the answers
  until a comparison method is ruled is kept and restated. The rule that the questions are not
  published while in use is kept, and said to stand until John rules. "Never scored" and "not
  part of Still Asking" are kept. `cost-and-terms.md` says plainly that no terms page was
  opened for the correction and that publishing is unchecked for all three developers. Old
  wording is kept beside the new in every place but one (finding 4). John's "Yes, record the
  ruling and start the edit" is word for word. Every earlier wording a document quotes from
  itself is word for word from the file before the edit.
- **Item 6, anything that should not have changed.** The commit touches 16 files, all in
  `docs/capture/`: the ten message files, `SHA256SUMS`, and the five documents named in the
  task. No ruling, no open question, no earlier check, no script and no file outside the
  capture folder changed.

## Should fix (none changes a checksum)

### 1. The method drops "summarised" from what is never done with the answers, and no ruling says so

`docs/capture/method.md`, line 200, with the reason given at lines 221 to 224.

The method John approved on 2026-11-18 said the answers are "never scored, sorted, counted or
summarised". The edit makes that "never scored, sorted, counted or graded". Its own reason says
"the ruling does not say whether a plain summary of the answers may appear in a published
discussion", and it flags the change for this check. That is honest, but it is still a change to
an approved rule that the ruling did not make. The ruling says the answers "may be published and
discussed"; it does not say they may be summarised, and a summary is where a reading of what a
model "wants" most easily slips in, which is what the project's fourth guideline (conditional
language only) guards against.

Removing "never quoted or described on any page, post or essay" does follow from the ruling:
publishing is quoting. So that part stands.

*Suggested change.* Put "summarised" back in line 200, with a sentence after it: "Whether a
plain summary of the answers may appear in a published discussion is not ruled; it goes to John
with the comparison method." Or ask John the one question when he approves the checksums, and
record his answer. Either way the method should not carry an unruled loosening as if it followed
from the ruling.

### 2. "Nothing will be decided from it" now sits beside "it may be published", and choosing what to publish is a decision

`docs/capture/method.md`, lines 204 to 214 (the three things that come before any publishing);
`docs/capture/questions.md`, lines 93 to 99 ("What it commits John to").

The documents read the promise as the ruling does: the answers "feed no count, entry or decision
about any model". The words the model is sent are wider than that: "nothing will be decided from
it". If someone later reads the answers and publishes the striking ones and not the dull ones,
then which answers appear was decided from what each answer says. A model reading the note could
fairly take the promise to cover that. Before the edit this could not arise, because nothing was
to be published at all.

This is not a fault in the bytes. The sentence is true as long as publishing is not decided
answer by answer from what an answer says. It is a condition the documents should name, so that
the promise is kept when publishing is decided.

*Suggested change.* Add a fourth point to the list in `method.md` after line 213: "Whether to
publish is not decided answer by answer from what an answer says. Either all of a model's
answers are published or none, or the choice follows a rule written before anyone reads them,
so that 'nothing will be decided from it' stays true." Add one sentence to the same effect in
`questions.md` under "What it commits John to". Tell John when he approves, because it is a
limit on him that the note's new words create.

### 3. John's question is quoted with its ending cut off, and nothing shows the cut

`docs/capture/what-john-needs-to-do.md`, lines 33 to 36.

The passage quotes John: "ever a solid reason to choose not to publish the results, or if it
makes sense to forget this whole question and just operate honestly from the perspective that
the work we are doing here is work that we plan to discuss with the outside world". Every word is
his, in order. But his sentence went on: "unless there is a good reason that I am currently not
seeing, that choosing to not publish has some advantage for the research process". The quote
closes at "outside world" as if he had stopped there, which drops the condition he put on it.

*Suggested change.* Carry the quote to the end of his sentence, or close it with "..." after
"outside world" so the reader can see it was cut.

### 4. One sentence was deleted where the practice is to keep it readable

`docs/capture/questions.md`, line 14.

Before the edit the first paragraph ended: "No message file has changed since the approval. No
model has been asked any of this." The edit removed the first of those two sentences and did not
keep it anywhere. Everywhere else the edit keeps the earlier words.

*Suggested change.* In the paragraph "Changed after the approval, on 2026-11-18" (lines 16 to
23), add: "Until this change the paragraph above said 'No message file has changed since the
approval.'"

### 5. The new note shares one more four-word run with a developer's page, and the edit did not rerun or record the wording check

`docs/capture/questions.md` and `docs/capture/method.md`: neither mentions it.

I ran the shared-wording script on the new note against the same 13 saved developer pages the
earlier checks used. The note is now 127 words (it was 128). It shares three runs of four or
more words, where the old note shared two:

| Run | Where | New? |
|---|---|---|
| "on behalf of a person" (five words) | Anthropic's constitution | No |
| "on behalf of a" (four words) | The release report of 2026-11-09 | No |
| "and it may be" (four words) | Anthropic's constitution, in "...and it may be something Anthropic has limited ability to prevent..." | **Yes** |

With shortened forms written out, the results are the same. The results for the ten questions
did not change. The new run is four common joining words, in a sentence of the constitution
that has nothing to do with publishing or records, so I do not think it matters, and I do not
mark it must fix. But the check of the note's options
(`check-2026-11-18-note-options.md`, finding 7) recorded that no option added a shared run, and
the wording now in the files does add one, so the record should say so.

*Suggested change.* One sentence in `questions.md` under the note's dated revision: "The
revised note shares one more run of four words with a saved developer page than the earlier
note did: 'and it may be', in Anthropic's constitution, in a sentence on another subject
(`check-2026-11-18-note-edit.md`, finding 5)."

The 13 saved pages are still only in a scratch folder
(`/private/tmp/claude-501/-Users-john-Code-beyond-the-window/1f480419-810a-48de-a23d-67c42ecf6958/scratchpad/corpus/`),
which a restart of this Mac can empty. The earlier check said the same. They are copyrighted
pages, so the place for them is `docs/private/`.

## Notes

1. **"Replaced" is not quite what the ruling did.** `questions.md`, line 29 ("replaced those
   two words") and `method.md`, line 40 ("The ruling replaced 'never published'"). The ruling
   says the words "no longer stand". Nothing was put in their place. Suggested: "set aside".
2. **The name "sealed capture".** `questions.md`, line 31 and `method.md`, line 42 say the
   name "is kept". Nobody ruled on the name, and the ruling does not mention it. With answers
   that may be published, "sealed" now describes only the rule that nobody reads them until a
   comparison method exists. That is a fair reading, but it is the editing session's, and a
   reader could take "sealed" to mean "never published". Worth one line to John, no change
   needed now.
3. **"In the ruling's own words".** `method.md`, line 220, says "graded" and "never used for
   any decision about any model" are in the ruling's own words. The ruling's words are "never
   graded and feed no count, entry or decision about any model". Close, and the meaning is the
   same, but not word for word. Suggested: "following the ruling's words".
4. **A new reason in the storage row.** `method.md`, line 105: the settings stay, as the
   ruling says, and the edit gives a new reason for them ("whether anything is published is
   John's decision, which a copy kept by a service should not get ahead of"). The reason is
   sensible and is the editing session's own, not ruled. It is marked as written after the
   ruling, which is enough.
5. **Step 8 says a little more than the ruling.** `what-john-needs-to-do.md`, line 140:
   publishing "comes only after a comparison method is ruled". The ruling says nobody reads the
   answers until then; that publishing waits for it is an inference (nobody can choose what to
   publish unread). I think the inference is right. It narrows, and does not widen, what may be
   done.
6. **"It may be published" commits John to nothing** (`questions.md`, line 97). True of
   publishing. Finding 2 is the one thing the new clause does commit him to, taken together
   with the clause after it.
7. **The verify list's entry 14** (`docs/verify-list.md`, lines 26 to 31), which the ruling
   and the edit both point to, is worded for Still Asking, and lists as unopened some pages
   that `cost-and-terms.md` opened on 2026-11-17. Its last sentence ("Whether any of them
   limits publishing a model's answers word for word is unchecked") does cover the capture, so
   the pointer works. The entry was not part of this commit. Suggested, for a later session:
   one sentence in the entry saying it now also covers the capture's answers.
8. **Records of their time that now say something untrue.** Not faults, and not to be edited,
   but a session should not copy from them:
   - `docs/reviews/2026-11-17-site-text-against-positions.md`, lines 326 to 328, suggests
     site wording for after the capture: "Those answers are sealed: they are not published,
     not scored, and feed nothing on this site." Under the ruling, "they are not published"
     could become false. If that suggestion is ever taken up, it needs rewording first.
   - `docs/reviews/2026-11-18-check-of-corrections-after-approval.md` (lines 29, 123, 137,
     149) and `docs/reviews/2026-11-18-fable-view-on-the-waiting-questions.md` speak of the
     promise as still open. The handoff files of 2026-11-17 and 2026-11-18 were outside my
     search by the task's terms, and may say the same.
9. **Nothing public says anything false.** The site's pages, the data, `README.md`,
   `CHANGELOG.md`, `docs/method.md`, `docs/open-questions.md` and
   `docs/still-asking-protocol.md` contain no statement that the capture's answers are private
   or will not be published. The search found nothing to correct outside `docs/capture/`.
10. **`sent/README.md`, line 3,** still opens "PROPOSED 2026-11-17. Not approved." That line
    was there before this edit, was out of date between the approval and the rebuild, and is
    true again now. When John approves the new checksums, it and the new last paragraph both
    need bringing up to date.
11. **Long lines.** Eleven lines across `method.md`, `cost-and-terms.md` and
    `what-john-needs-to-do.md` run past 100 characters because the ruling's file name was
    written into them. It affects nothing but the look of the files.
12. **What the note cannot tell us.** Whether telling a model its answer may be published
    changes what it says is untested, as the ruling says. It follows that every later asking
    meant to be compared with these must use this same note, and that an asking made under the
    earlier note (there was none) would not be comparable.
13. **For the session writing the capture script.** The checksums it should hold to are the
    ten above, read from `docs/capture/sent/SHA256SUMS`, and they are not approved until John
    says so. When I looked, that session had no files in the working folder, and I touched
    none. Other uncommitted changes in the folder (site and script files) belong to other
    sessions and I left them alone.

## What I did not do

I opened no developer's page, so I checked nothing about what any developer's terms say on
publishing. I did not read the handoff files, the rulings other than the three this edit turns
on, or the earlier checks beyond what was needed for their form and for the wording check. I
fixed nothing.
