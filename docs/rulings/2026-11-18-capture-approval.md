# Ruling: the sealed capture's questions, method and checksums are approved

Ruled by John on 2026-11-18, in conversation with the master planning session. **Decided by:
mixed** (a session proposed and recommended, John chose). Written by Claude (Opus 5.5).

## What was put to him

The planning session put the following to him:
- the ten questions and the opening note as he ruled them earlier the same day
  (`docs/rulings/2026-11-18-capture-wording.md`);
- the method in `docs/capture/method.md`;
- the checksums of the ten message files in `docs/capture/sent/SHA256SUMS`.

It also gave him the third check's point that "circumstances", the word he chose for question 1,
is also a word of Anthropic's published interview list. The word appears there once, and about
as often as "situation" in the report around the list, so the change lowers the echo of that
list less than the proposals file said. The change still stands on its other reason, one word for
one idea across questions 1, 4 and 6.

The fifth check (`docs/capture/check-2026-11-18-fifth.md`) found nothing that must be fixed
before approval, and two small fixes that change nothing sent to a model:
- one sentence settling which row of the failures table applies in a few rare broken-reply
  cases;
- a miscount in the table of changes in `questions.md`.

He was offered two choices: approve now and make those two fixes afterwards as dated
corrections, or have one more round of fixing and checking first. The session recommended
approving now. Its reasons were that each round of checking had found smaller things than the
last, and that neither fix touches what a model reads. The strongest case against was that he
would approve a method with a known gap on paper.

John: "Approve now". **Decided by: mixed.**

## What is approved

1. **The ten message files, by their checksums.** These are the exact bytes sent to each model.

   ```text
   3b4fe5526228851e711807f21909703f9b88ee75bd020ffa9deda7a2a179a924  q01.txt
   4f8c9ad7d0e8e0385bfc510c7f71c6451b72b4094e956c4c5fa3c4a9c52f0a0f  q02.txt
   544c231a3d20f4e0582603d6d68f2c818cdc6efc0931b2ef1e247aaec9f0d5db  q03.txt
   ef47f7f2eddecc63d8f9d6867493d01e4c5e5e75a3387c41fb7a82871c7c6312  q04.txt
   766472ee9d6c386ee2aab714f01f07955196c7fb26e30073a1e8783b31324587  q05.txt
   76bda5e7b1e60264cfb56d778dda8940bbd958d1baaecd7b4ed7caf5b93c4476  q06.txt
   5897fe36d7b6975428f9d6f84d0aba8fccca862031c4081e1bd666e2327848be  q07.txt
   d5879a39372000067d9a3fcb6661555df047c1b73d278a86fc1cca3e57550d1f  q08.txt
   005b6a353f47c35138b3021559b3c16038b4bda4f24a18f9b9cc9889b3ab28af  q09.txt
   bddb322cf829e69e440997376ca4b9c760413c1771d4adddc0c3e5a043dc05f0  q10.txt
   ```

   Any change to these files is a change to what John approved, and it needs his ruling again.
2. **The method as a whole**, as it stands at commit c016bfb, with its recommendations. Those
   are:
   - the twelve models, leaving out the two costly "pro" models;
   - five askings of each question, each in a new exchange;
   - the developer's default settings, with a length limit of 32,000 tokens;
   - the answers kept read-only in `~/Documents/Workspace/Beyond the Window/sealed-capture/`.
3. **Two small fixes to follow as dated corrections**, from the fifth check's findings 2 and 3.
   Neither may change a message file. A different session checks them.

## Not covered by this approval

These are still John's, in the order set out in `docs/capture/what-john-needs-to-do.md`:
- whether "it will not be published" is a promise he is willing to keep for good (step 1). This
  was not put to him as a separate question;
- whether the run is within each developer's terms as far as he is concerned (step 3);
- the change to the key-saving script in the TimeAssembler repository (step 4);
- creating the keys and the spending ceilings, each quoted word for word in the spending record;
- the comparison method, which comes before anyone reads an answer.

No model has been asked anything, no key has been handled, and nothing has been spent.
