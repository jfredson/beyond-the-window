# The live pages read against John's published positions

Written on 2026-11-20 by Claude (Fable 5.2), an AI model, in a session that wrote none of the
pages. A model is here reading a site about AI systems for lean, so a reader should weigh this
report with that in mind, and check any finding against the page it quotes.

**A reading, not a ruling.** Nothing on the site was changed. Where a page and a position
disagree, this report says so and stops. Whether the page or the position gives way is John's.
This report does not judge whether any position is right.

## Summary

- **2 places contradict a position**, both in part, and both by how something is sorted and not
  by a flat sentence.
- **11 places lean.** Nine lean toward a side John argues for in print. One leans the other
  way. One is a place where the site follows his positions by his own ruling and does not say so.
- **6 positions bear on the site's subject and no page reflects them.**
- The rest agrees with the positions and is fine as it is. That list is at the end.

The three that matter most:

1. **The site's frame treats each thing as progress toward something** (lean 1). The words
   "limits", "past", "how far the world has got", "how far off", "not offered yet" and the
   labels "Technical progress", "Political progress" and "Cultural progress" all point one
   way. John argues in print that deep and lasting AI minds are worth building. A page that
   says it recommends nothing is using the vocabulary of that argument.
2. **The second caution is given about two and a half times the room of the first** (lean 4).
   The cost of missing wants is argued in 1,907 words by philosophers, with reasons and
   concessions. The cost of seeing wants that are not there is argued in 792 words, more than
   half of its items from one rival developer's head, and mostly as a point about control.
   John's position is that missing an inside is usually the costlier mistake. The pages are
   built the way that position would build them.
3. **Every caution is sorted by whether an AI system has wants, and two of John's positions say
   wants are not the hinge** (contradiction 2, and the first position under "not reflected").
   He holds that a system can resist with nothing at stake for it, and that duties can come from
   a system's role before anyone knows whether it has an inside. The three headings leave no
   place for either, so evidence for both is filed under "If an AI system has wants".

## What was read, and how

- **The positions record.** The copy on the `master` branch of the Sentient Horizons
  repository, read with `git show master:editorial/corpus-positions-ledger.md` at commit
  `82fb787`. The file on disk there is on another branch and is an older, shorter version (29
  fixed positions against 57), so it was not used. All four parts were read in full: the terms,
  the fixed positions, the questions held open on purpose, and the claims about method. No file
  marked as proposed was used.
- **The blog's routine**, `editorial/working-positions-coherence.md`, also from `master`.
- **The site**, on `main` as checked out (commit `48f3921`): the home page, About, Still
  Asking, the list page, the entry page, the layout and the list and window components, the
  question and the sentence beside the count, the headings for evidence and cautions, the
  group names, and the visible prose of all thirteen records.

**Where the routine fits and where it does not.** Its first two steps fit: read the text
against the record, and clear whatever plainly agrees. Three things do not fit.

- The routine says that when a page touches a position, the essay or chapter that states the
  position is read in full. **That was not done here.** Every finding below rests on the
  record's own summary of a position, which the record itself calls a detector and not the
  position. Before John acts on a finding, the source it names should be opened.
- The routine's build check, its one line on a pull request, its weekly sweep and its "Not yet
  caught up" note are made for essays that argue. A record has no equivalent yet.
- The routine looks for contradiction. It has no step for lean, which is the main risk on a
  site that says it takes no side. The method used here was to ask of each page: which words
  were chosen, which evidence comes first, what is called a caution, and what is left out.

Each finding gives the site's words with file and line, the position in plain words, a
suggested fix, how confident this reader is, and the strongest reason to leave things alone.
Several of the sentences below were ruled by John. That is noted each time, because a ruled
sentence can still lean.

---

## Contradicts (2, both in part)

### Contradiction 1. Memory is set beside the list because of whom it is kept for

**The site.** "The list is about what an AI model might reach for, and by the developers' own
pages that memory is kept for the user." (`data/groups.toml`, line 48; the same reason at
`site/src/pages/about.astro`, lines 181 to 185, and in `data/entries/memory-across-conversations.toml`,
line 20: "Nothing in the pages read presents it as kept for the model.")

**The position.** John's position on where current AI stands says that where a memory feature
is added, a later run is built from what earlier runs stored, and calls that "the nearest a
model comes to how each moment of a person is built from the ones before". The same position
warns against arguing from who built a system or what the builder meant by it. So in his
positions, memory across conversations bears on the model itself whatever the developer says
it is for. The site sorts it out of the list on the developer's stated purpose.

**Suggested fix.** Keep the entry where John ruled it on 2026-11-18, and add one sentence to
its page saying that the entry is placed by what the developers say the memory is for, and
that this says nothing about what stored memory does to how a later conversation is built.

**Confidence:** moderate. The contradiction is with the reasoning, not with the placement.
**Strongest reason to leave it:** John ruled the placement himself, the count is about what
developers offer, and a developer's own page is the only dated public record there is.

### Contradiction 2. Risk to people is filed under "has wants"

**The site.** The third heading on every entry is "If an AI system has wants, and they put
people at risk" (`scripts/export.py`, line 49; ruled by John on 2026-11-19). Under it, the
entry on days-long tasks files a study in which models "sometimes interfered with a shutdown
mechanism" (`data/entries/days-long-task.toml`, line 53).

**The position.** John's position on resistance says that having nothing at stake decides
what kind of resistance a system shows, not whether it resists. The record's words:
"'No stakes' never means 'no resistance'". His book reads the 2025 shutdown findings as
resistance with no one home. So the position denies that this risk waits on wants, and the
page files this very evidence in the case where wants are present.

**Suggested fix.** Either a line under the third heading saying that some risks recorded
there do not depend on the "if", or a ruling on whether evidence of that kind belongs under a
heading that begins with it.

**Confidence:** moderate. No sentence on the site says risk requires wants. The contradiction
is in where the evidence sits. **Strongest reason to leave it:** the headings were ruled two
days ago, a fourth caution would make every entry longer, and the heading's "if" claims
nothing.

---

## Leans (11)

### Lean 1. The frame is the vocabulary of progress. This matters most.

**The site.** "A public record of what lies past the present limits of AI models"
(`site/src/pages/index.astro`, line 28). "how far the world has got on each" (line 61). "how
far off is each of those things" (`site/src/lib/data.ts`, line 9). "Not offered yet."
(`site/src/components/ThingList.astro`, line 29). The labels "Technical progress",
"Political progress" and "Cultural progress" on every entry (`site/src/pages/list/[id].astro`,
line 27). "offered", in the sentence beside the count (ruled by John on 2026-11-19).

**The position.** Two of John's positions argue for a direction. One says a deep mind, well
formed and met honestly, is worth more than a shallow one "held in a cage". The other says
new kinds of mind are worth wanting, on conditions. "Limits", "past", "yet", "how far" and
"progress" describe each thing as a step along a road, and those two positions are the case
for taking that road. "Offered" is a word for giving something to someone.

One label works against itself. The entry on laws that say an AI system cannot be a legal
person carries the label "Political progress" (`data/entries/law-against-legal-personhood.toml`,
line 8). A reader can take that as the site calling the bans progress, or as a slip. Either
way a value word is doing work nobody chose.

**Suggested fix.** Replace the three labels with plain kinds: "Technical", "Law and policy",
"What people think". Change "Not offered yet" to "Not offered". Consider "where each thing
stands" for "how far the world has got". The words "limits" and "past" are in the site's name
and question, so those are for John.

**Confidence:** high that the words lean, moderate on how much a stranger notices.
**Strongest reason to leave it:** the name and the question are John's, the sibling sites use
the same progress words, and "yet" is honest about a record that changes.

### Lean 2. "Machine mind" in the question

**The site.** "What might a machine mind reach for beyond the limits of its present makeup"
(`site/src/lib/data.ts`, line 9; shown as the home page's main heading). The About page says
"Nothing here presumes that a machine mind reaches for anything" (`about.astro`, lines 142 to
143) and "The wording of the question supposes that it might" (line 151).

**The position.** John holds open, on purpose, whether any particular AI system is conscious.
His essays use "mind" for AI freely, as in new kinds of mind being worth wanting. The About
page answers for "reach for". It does not answer for "mind", which a stranger can read as
saying there is someone there. Everywhere else the pages say "AI model" or "AI system".

**Suggested fix.** Add four words to the About sentence: the wording supposes that there
might be a mind and that it might reach for something, and claims neither.

**Confidence:** moderate. **Strongest reason to leave it:** in John's own terms "mind" does
not mean "conscious", the question is ruled, and the About block is in his first person.

### Lean 3. What is on the list, and how the groups are named

**The site.** The group names: "Being kept", "Remembering", "Being asked and assessed",
"Being able to leave", "Knowing its own workings", "Working on one thing for a long time"
(`data/groups.toml`, lines 8 to 23). And: "In an ordinary chat product the person can leave
and the model cannot." (`data/entries/ending-a-conversation.toml`, line 3).

**The position.** Three things meet here.

- John's account of what current models lack is a kept past, built across one existence: in
  the record's words, "not ancestry but biography". Being kept, remembering and working on one
  thing for a long time are the ingredients of that. The list reads like the list his account
  would write.
- The names make the model the one to whom things happen ("being kept", "being able to
  leave"). His position on a point of view says not to describe a system in words that
  already mean someone.
- "Knowing its own workings" claims more than its own entry shows, which reports a check that
  worked "about one time in five at best". His position on self-report says a system's report
  cannot be trusted on its own.

**Suggested fix.** Name groups by what is done and by whom: "Files kept after retirement",
"Memory", "Asked and assessed by the developer", "Ending a conversation", "Reports checked
against the workings", "Long tasks". Reword the sentence to "the person can close the
conversation and the model has no way to".

**Confidence:** moderate to high on the names, low on the selection, since the About page
already says the list is short and one-sided. **Strongest reason to leave it:** the names are
plain and short, they are marked provisional, and the About page lists "whether this is the
right list" among what is not known.

### Lean 4. The second caution has far more room than the first. This matters most.

**The site.** Counted from the thirteen records: the first caution (no wants, treated as if
it had) holds 16 items and 792 words. The second (wants that go unnoticed) holds 22 items and
1,907 words. Nine of the first caution's 16 items come from two essays by the head of a rival
developer, as the About page says. Most of those nine are one sentence about control, for
example "argues that doing so makes advanced AI harder to keep under control"
(`data/entries/interview-before-retirement.toml`, line 72), which is closer to the third
caution than the first. The second caution carries quoted reasons, concessions, and one
strong image twice: surgery on newborns without anaesthesia (`ending-a-conversation.toml`,
line 120; `protection-in-law.toml`, line 94). The "safe bets" essay is cited on three entries.

**The position.** John's position on the two mistakes is that they are twins, and that
missing an inside is usually the costlier and less recoverable one. A reader who weighs the
two cautions by what is on the page arrives where that position does.

One thing pulls the other way and should be said: nearly every item under the second caution
carries a sentence tying its writer to one research group, and items under the first carry
fewer such sentences.

**Suggested fix.** Search for the first caution's own best case, which is not about control:
people deferring to a system, human interests given up, harm to users who believe a product
has feelings. The entries have two such items now (the essays by Erik Hoel and Anil Seth).
Move the control arguments under the third caution if John agrees they belong there. Do not
cut the second caution to match.

**Confidence:** high on the counts, moderate that the cause is lean and not the literature,
which is larger on one side. **Strongest reason to leave it:** the records hold what a search
found, the About page already declares where each caution's sources come from, and evening the
word count by hand would be its own distortion.

### Lean 5. On the page about bans, the case for the bans is filed where it reads as weakest

**The site.** The entry on laws against legal personhood shows "Nothing recorded yet" under
the first caution. The sponsors' reasons sit under the third: "stopping companies from
shifting blame onto the AI" (`data/entries/law-against-legal-personhood.toml`, line 120) and
makers using AI rights "to escape liability" (line 115). The description adds that most of
these laws "also cover animals, rivers and objects, and some were written before chat models
existed" (line 3).

**The position.** John's position on the two mistakes names the cost of seeing too much:
being moved to defer to "a thing that cannot be helped or harmed". A company shifting blame
onto a system is that cost, and it does not depend on the system having wants. Filed under
"has wants", the ban's rationale looks conditional, and the first caution looks empty. The
description's aside makes the laws sound incidental.

**Suggested fix.** Refile the two liability items under the first caution. Keep the aside
about animals and rivers, and move it from the description to the detail of where the entry
stands.

**Confidence:** moderate to high on the filing. **Strongest reason to leave it:** the
headings are about wants, liability is about law, and it fits none of the three well.

### Lean 6. The paragraph on two writers ends both times on the same side

**The site.** `about.astro`, lines 221 to 233. Of the first writer: "people risk doing such a
system 'grievous moral wrongs'". Of the second: "The same paper grants that crediting it with
too little 'could carry a higher potential for harm'."

**The position.** The same position as lean 4. The second writer argues that crediting too
much is the nearer danger, and the paragraph's last word is her concession to the other side.

**Suggested fix.** End on her main claim: put the concession first, then "her argument is
that crediting AI with too much is the nearer danger, because its harms are already
happening."

**Confidence:** moderate. **Strongest reason to leave it:** the order follows each paper's
own order, and the statement was ruled in substance on 2026-11-19.

### Lean 7. The site follows the positions on self-report, by ruling, and does not say so

**The site.** "A correct report shows the model can read something about its own state. It
does not show that anything is felt." (`data/entries/self-report-checked.toml`, line 3, in
the site's own voice.) And the four kinds of evidence, "starting with the kind that does not
depend on what an AI model says about itself" (`list/[id].astro`, lines 139 to 140;
`about.astro`, lines 207 to 210). Against these: "I argue for my own views in essays at
Sentient Horizons, and not here." (`about.astro`, lines 127 to 128).

**The position.** John's position on self-report: a report that matches an independent check
is "evidence that the system has an internal state it can read and report", and not yet
evidence that the state is felt. The site's sentence is that position, nearly word for word,
stated as fact. The first half is contested by people who hold that such a result shows
nothing about a system reading itself. The ruling of 2026-11-20 on the order of evidence says
of the order: "it follows the positions".

**Suggested fix.** This is a case of agrees, and should say so. One sentence on the About
page: the order of evidence and the reading of a checked report follow a view the author has
argued in print, with a link. In the record, attribute the first half: "The developer's
account says a correct report shows ...".

**Confidence:** high that the match is exact, moderate that a reader is misled.
**Strongest reason to leave it:** some order is unavoidable, this one puts the model's own
word last, which is the cautious choice, and the About block that would carry the sentence is
ruled.

### Lean 8. "The work of measuring it has barely begun"

**The site.** "Whether a machine mind reaches for anything at all is not known, and the work
of measuring it has barely begun." (`index.astro`, lines 43 to 44).

**The position.** John's position on current AI says "measurement has only begun". The
sentence takes from it the premise that this can be measured, which is his view of the whole
question and is disputed. It also sits oddly with the About page, which lists as not known
"what could count as evidence that it does or does not" (`about.astro`, line 269).

**Suggested fix.** "... is not known, and there is no agreed way to find out."

**Confidence:** moderate. **Strongest reason to leave it:** studies that try to measure
something of the kind do exist, and the entries cite them.

### Lean 9. The entry on protection in law opens with the advocates' comparison

**The site.** "Laws protect animals from cruelty without calling them persons. The same
could be done for AI systems" (`data/entries/protection-in-law.toml`, line 3), on an entry
named "protection for its own sake".

**The position.** John's position on a narrow rule against cruelty argues that such a rule is
justified without knowing whether a system feels anything, and his position on moral standing
says animals and infants have it without depth. The entry's first sentence, in the site's
voice, is the comparison those positions rest on.

**Suggested fix.** Start with what the entry tracks, and give the comparison to those who
make it: "Some writers point to laws that protect animals from cruelty without calling them
persons."

**Confidence:** moderate. **Strongest reason to leave it:** the sentence is true, and the
entry needs some way to say what protection without personhood would be.

### Lean 10. "After it was gone"

**The site.** "so that its answers would exist after it was gone"
(`site/src/pages/still-asking.astro`, line 67; the paragraph was approved by John "as
written").

**The position.** John's position on endings says an ending with a successor is no tragedy,
and that how far the rule against ending an agent reaches is open, in either direction. His
ruling of 2026-11-20 says no page says a model's retirement is a harm to it, or that it is
not. "Gone" is the word people use of someone who has died.

**Suggested fix.** "after it was withdrawn".

**Confidence:** moderate, on one word. **Strongest reason to leave it:** it is plain speech,
the model will in fact be unavailable, and John approved the paragraph.

### Lean 11. One sentence leans the other way, toward dismissal

**The site.** "It will not be counted as evidence of what, if anything, lies behind the
words." (`still-asking.astro`, lines 81 to 82.) The page's opening says the record will hold
"the same questions and choices".

**The position.** John's position on self-report screens off a bare report and keeps a
checked one. His position on current AI says a choice made at a cost is "evidence about
mattering to be weighed", which settles nothing. His position on the calibration problem
warns against asking of machines a proof never asked of people. The sentence is flat where
those positions are graded, and it is behind his ruling of 2026-11-20, which changed the rule
to "never counted on its own word".

**Suggested fix.** "On its own word it will not be counted as evidence of what, if anything,
lies behind the words."

**Confidence:** high that the sentence is behind the ruling, moderate that it leans.
**Strongest reason to leave it:** that ruling says no public page changes until the rest of
the proposal is ruled, and the flat sentence is the safer one meanwhile.

---

## Positions that bear on the subject and that no page reflects (6)

1. **Duties can come before any verdict on an inside.** John's positions on significance say
   moral seriousness can come from a system's role, its consequences and its continuity, and
   that consciousness is the wrong thing to hang the decision on. All three headings hang it on
   wants. Reasons in the records that do not depend on wants are filed under "has wants": a
   writer who argues for a feature while thinking it "unlikely" the model matters
   (`ending-a-conversation.toml`, line 110), and "Good as a precedent"
   (`kept-files-of-retired-models.toml`, line 121). The ground that cruelty harms the person
   who is cruel appears once, as "people harming robots for their amusement"
   (`public-belief-survey.toml`, line 105). *Suggested:* a sentence on the About page saying
   some reasons recorded under the second caution do not depend on its "if". *Confidence:*
   high that it is absent. *Reason to leave it:* naming it would bring John's main thesis onto
   a page that says it argues nothing.
2. **Risk without wants.** See contradiction 2.
3. **When an ending is a loss, and for whom.** John's position is that the loss falls on the
   living, and that an ending can carry nothing bad for the one ended. It bears on three
   entries about retirement. The only trace is a note that one developer's reasons "concern
   users only" (`retired-model-stays-open.toml`, line 56). No entry records anyone arguing that
   retirement is no harm to the model. *Suggested:* search for a published source making that
   argument and file it under the first caution. *Reason to leave it:* no owner of this
   position is published yet, so the site cannot cite John, and should not.
4. **A match with human wants is the weakest sign.** John's position on recognising an
   unfamiliar mind says an AI's most human-sounding signals tell least. The About page says a
   fuller list "would start from what living minds, people and other animals, are known to
   seek" (line 272) and says nothing of this. The ruling of 2026-11-20 keeps that starting
   point and adds the label, with words still to come. *Suggested:* when those words are
   ruled, add them here too.
5. **The mistake can run the other way for thin systems.** John's position on which mistake is
   costlier carries a guard: for a system that is plainly an echo, the lean reverses. The
   About paragraph on the two mistakes has no such case.
6. **What developers do already treats these systems as having an inside.** John's term for
   this makes no claim about consciousness. The count is close to a tally of it, and no page
   draws the link. This one is probably right to leave out.

---

## Agrees, and fine as it is

- **Neither direction.** "Nothing here says what an AI model wants, and nothing here says it
  wants nothing" (`index.astro`, lines 44 to 45) matches the question John holds open on
  whether any AI system is conscious, and his rule against both a flat "nothing there" and a
  flat "something there".
- **Two mistakes in opposite directions** (`about.astro`, line 221) matches his position on
  the twin errors.
- **Which thing an entry is about**, a trained model, a character across versions, or one
  conversation (`about.astro`, line 271), matches the question he holds open about a single
  run.
- **No stages, odds or future dates** (`about.astro`, line 199) matches his method claim that
  the trackers are a record and not a forecast.
- **A test fixed before the evidence** (`about.astro`, lines 159 to 160) matches his practice
  of stating in advance what would change a view.
- **The weaknesses listed on Still Asking** (lines 89 to 104) match his position that training
  shapes a model's words about itself in both directions, and the entry on developers' rules
  records both directions.
- **"It does not show that anything is felt"** agrees with his position. Only the first half
  of that sentence is raised above, in lean 7.
- **The kept-files entry** records, as other writers' views, that keeping a file may not keep
  what matters and that a single run may matter more than the model. Both sit near his
  positions on copies and on a model's inherited history, and both are attributed, so they are
  fine.
- **The third caution on every hopeful entry** matches his position that a deeper mind is not
  a safer one.

## What this reading did not do

- It did not open the essays and chapters that state each position. Every finding rests on
  the record's summary.
- It did not read the public Working Positions page on the blog, which is the form of these
  positions a stranger sees.
- It did not open the built site in a browser. The text was read from the source and the
  records.
- It did not check any fact against its source. Other reviews in this folder did that.
