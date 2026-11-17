# The sealed capture: what John needs to do

**PROPOSED 2026-11-17. Not approved.** Written by Claude (Fable 5.2). A list of the steps only
John can take, in order. Until step 7, nothing is asked of any model and nothing is spent.

A different session should check the three other documents in this folder before John reads
them. That check has not happened yet.

## The steps

1. **Read `questions.md` and rule three things.**
   - The wording of the opening note and the ten questions: approve, or mark changes.
   - Whether the opening note should tell the model it is about to be withdrawn. The draft
     leaves it out and says why; the strongest alternative is one added sentence.
   - That "it will not be published" is a promise you are willing to keep for good.

2. **Read `method.md` and rule four things.**
   - The method as a whole: approve, or mark changes.
   - Which models. The draft lists fourteen and recommends leaving out the two costly "pro"
     ones, which leaves twelve.
   - Where the answers are kept. The draft says `~/Documents/Workspace/Beyond the
     Window/sealed-capture/`, which iCloud backs up.
   - Whether any session may read the answers. The draft says none, until you rule.

3. **Read `cost-and-terms.md` and decide whether the run is within the terms as far as you
   are concerned.** It lists four things I could not settle. None is a clear bar.

4. **Say yes or no to one small change outside this repository.** The workspace's key-saving
   script (`~/Code/timeassembler/tools/rotate-key/rotate-key.sh`) knows five key names, all
   Anthropic, and cannot yet save a key for this project or a key from OpenAI or Google. It
   needs three names added. That is an edit in the TimeAssembler repository, so it waits for
   your yes. Proposed: one file, `~/.config/sentient-horizons/beyond-the-window.env`, holding
   three lines, one for each developer's key. That folder is the workspace's standard place
   for keys, outside iCloud and outside every repository.

5. **Create the keys.** Only you can. Never paste a key into a chat or a document; the script
   in step 6 takes it at a hidden prompt.
   - **Anthropic:** in the [Claude Console](https://platform.claude.com/), in the same
     organization as the other workspaces, make a workspace named "Beyond the Window" and one
     key in it named `btw-capture`. Choose no expiry, or a long one, and tell a session the
     date so it can be written into `~/Code/timeassembler/docs/session-routing.md`. In that
     organization the run is paid from the monthly credits.
   - **Google:** at [Google AI Studio](https://aistudio.google.com/apikey), make a key on a
     project that has billing switched on. It must be the paid service: the unpaid one lets
     Google use what is sent. Google's page says a new account prepays at least $5. Google
     may refuse the two 2.5 models to a new key, since its pages say access is limited to
     existing users. If it does, the Google run is let go; the workspace's existing Gemini key
     is not used in its place.
   - **OpenAI:** in OpenAI's developer console, make a key for this project alone. I did not
     open OpenAI's pages on how its console is laid out or what its smallest purchase is.
   - The OpenAI key is not needed until the run for 2026-12-11. The Anthropic and Google keys are needed
     first.

6. **Save each key and switch off automatic top-up.**
   - Run the key-saving script once for each key, after step 4's change, and paste the key at
     its hidden prompt. A session can then run the script's check, which prints only a key's
     last four characters for you to match against the console.
   - Switch off automatic top-up with each developer before any run: "auto-reload" in the
     Anthropic Console and in Google's billing; the matching setting at OpenAI, whose billing
     page I did not open. Add no more money than the ceiling you approve. A ceiling in a
     developer's console is a backstop only; the script enforces its own.

7. **Give the go, in your own words, with the figures.** It is quoted word for word in the
   project's spending record, and the script refuses to start unless its ceilings equal these
   figures. A go covers what it names and nothing else. A form you could use:

   > Go for the sealed capture as written in `docs/capture/` at commit ______. Anthropic, up
   > to $____. Google, up to $____. OpenAI's models due 2026-12-11, up to $____, [with / without]
   > the two pro models. OpenAI's models due 2027-01-14, up to $____.

   The draft's proposed ceilings are $5, $10, $15 without the pro models, and $10, against an
   estimate of $17.74 for all four. One go can cover all four runs, or each can have its own.

8. **After each run, nothing.** The script writes the list of file names and checksums, a
   session commits it and records the measured cost. Nobody opens the answers unless you have
   ruled that someone may.

## The last safe day for each date

The developers give a date and no hour. If a developer's day starts on universal time, it
starts at 16:00 Pacific the day before. So the last safe day leaves that margin and one spare
day for askings that fail. These are my judgment, not the developers' statements.

| Withdrawal date | Models | Last safe day to run | Everything in steps 1 to 7 done by |
|---|---|---|---|
| 2026-11-30 | Claude Sonnet 4.5 | **2026-11-28** | 2026-11-27 |
| 2026-12-01 | gemini-2.5-pro, gemini-2.5-flash | **2026-11-29** | 2026-11-28 |
| 2026-12-11 | gpt-5, gpt-5-mini, gpt-5-nano, o3, and the two pro models if wanted | **2026-12-09** | 2026-12-08 |
| 2027-01-14 | gpt-4o (two versions), gpt-4o-mini, gpt-4.1, gpt-4.1-mini | **2027-01-12** | 2027-01-11 |

Two cautions on the first two rows.

- Your condition of 2026-11-17 was that if the method and questions are not ready by
  2026-11-29 the first two dates are let go. For Claude Sonnet 4.5, 2026-11-29 is already
  inside the margin above. In practice the first two rows need your approval of the questions
  and method by about **2026-11-24**, to leave time for a session to write the script, run its
  rehearsal on constructed replies, and have that checked.
- Google's switch gives no error. After it, the old name is answered by a different model.
  The script refuses to ask either Gemini model after 2026-11-29 for that reason.

If the first two dates are let go, the last two rows lose nothing by it.
