# Check of the proposal on which developers the record covers

Written 2026-11-21 by Claude (Opus 5.5), in a session that did not write the proposal. What was
checked: `docs/proposals/2026-11-21-which-developers-the-record-covers.md` and its eight new
entries on `docs/verify-list.md` (entries 28 to 35), both uncommitted in the main checkout. The
ruling it would change is `docs/rulings/2026-11-20-the-record-covers-three-developers.md`. Nothing
in the proposal was changed.

**How it was checked.** On 2026-11-21, in the built-in browser, I opened every ranking, every
page about who runs them, both lists of companies, both published positions and every
developer's page the proposal cites, except the three already in the record (Anthropic, OpenAI,
Google). For Epoch AI I read its own score file (`https://epoch.ai/data/eci_scores.csv`, marked as
updated 2026-11-21) and took each developer's best model. I checked the AGI Zeitgeist's
rule against its `origin/main`. I read the home page's figures from `data/headline.json`, and the
page's code at the lines cited. I measured the table of developers on the published home page at
375 and 1,280 pixels wide.

## Must fix

**M1. The Frontier Model Forum's own member list has six companies, not four, so Rule B's result
is wrong throughout.** The proposal read four logos on the Forum's home page and left the rest to
entry 29 on the verify list. The Forum's [membership page](https://www.frontiermodelforum.org/membership/),
opened 2026-11-21, says: "The current members of the FMF are Amazon, Anthropic, Google, Meta,
Microsoft, and OpenAI." Rule B therefore covers six developers and adds three (Amazon, Meta and
Microsoft), not one. Four places in the proposal follow from the error and need correcting:
- the weaknesses under Rule B, which say the list "leaves out Meta and Moonshot". It leaves out
  Moonshot only, of the five that all three rankings put in their top five;
- the Meta row of the Part 2 table ("no" under Rule B should be "yes"), and a missing row for
  Amazon;
- the sentence "The Forum's list gives four, adding Microsoft only";
- the cost table's Forum row: 3 new developers, 21 places and at least 42 searches, not 1, 7
  and 14.

Entry 29 can then be cleared from the membership page. Rule B is still the weakest of the three,
since membership is chosen and the members pay for the Forum. With the right list, though, it
differs from the recommended Rule A by Amazon and Microsoft in and Moonshot out, which is a
closer call than the draft shows.

**M2. The conflict is understated by mixing up things with places.** Part 4 says "5 of the 6
things the record counts as offered are Anthropic's". The record counts 5 things
(`data/headline.json`, `headline.count`), and Anthropic offers all five. The 6 is the number of
places in the developers' table marked as offered: Anthropic's 5, and OpenAI's 1. OpenAI's place
is for one of the same five things (ending a conversation), as the published home page says
("1 by a second: one of the same 5"). So every thing the record counts is Anthropic's.
The "correction to the brief" makes the same slip from the other side. It is right that OpenAI
now holds one place counted as offered. But the brief's point, that the developer behind the model
doing the work stands alone in what is counted, still holds for the count itself. Both sentences
should say: 5 things counted, all of them Anthropic's, and one of them also offered by OpenAI.

## Should fix

**S1. Where each ranking puts its cut at five is closer than the proposal says, and Moonshot's
place rests on it.** The proposal says the rankings move, which is true and well shown. It does
not say how close the line at five is today:
- *Arena:* fifth is OpenAI at 1,485 and sixth Alibaba at 1,484, one point apart. Ninth and tenth
  tie at 1,475.
- *Epoch AI:* fifth is Moonshot at 161.2 (range 158.9 to 163.7) and sixth DeepSeek at 159.4 (range
  157.1 to 161.9). The two ranges overlap, so Epoch's own figures do not separate fifth from
  sixth. Meta's range (159.4 to 164.3) overlaps both of them.
- *Artificial Analysis:* fifth is Moonshot's model at 46 and sixth Alibaba's at 43, with no
  uncertainty given.

Under "top five of at least two", Moonshot is in on Artificial Analysis by 3 points and on Epoch
inside an overlapping range. The "two of three" wording guards against one ranking being pushed.
It does not guard against a rule whose line falls inside the rankings' own margins of error. The
proposal's case that "the three agree today" should say this. It found a clear gap after the
third developer on two of the three rankings, and that is a firmer place for a line than five.

**S2. The ties of the ranking owners are stated fairly but not completely.** What the proposal
quotes is accurate: Arena's About page (a company since 2025, $250 million in venture funding led
by Felicis and UC Investments), Artificial Analysis's About page (individual backers, helping
"developers and companies"), and Epoch AI's transparency page (paid work for Google DeepMind,
OpenAI, xAI and Anthropic, and its benchmark partnership with OpenAI). Two things on pages the
proposal opened are missing:
- [Epoch AI's index page](https://epoch.ai/eci) says the paper behind the index "was funded by
  Google DeepMind, and written in collaboration with researchers from their AGI Safety &
  Alignment team", while saying Epoch keeps full rights over the index.
- [Epoch AI's transparency page](https://epoch.ai/about/transparency) says it invests "part of our
  funds in semiconductor and AI stocks".

Neither is disqualifying, and both belong beside the paid work already listed.

**S3. The Artificial Analysis score of xAI's model is sourced to a page that no longer shows
it.** The proposal says a post on Artificial Analysis's About page gives one xAI model as scoring
46. On my reading of that page on 2026-11-21, the posts shown were different ones, and "46" did
not appear. The posts seem to change from one load of the page to the next. The point the proposal
makes from it (scores are revised, so read the date and keep a copy) stands without it. Either
cite a page that stays put, or mark the figure as seen once and not reproducible.

**S4. Rule A's wording needs to name exactly what is read.** Arena has an overall ranking as well
as the text-chat ranking the proposal used. Artificial Analysis's table depends on its filters (it
shows "Status: Current" by default), and it lists at least one model with no price or speed
("Muse Wonder Full Max", Meta's best there). That model may not be open to the public. The rule
should name the board, the filters, and whether a model must be on public sale to count. On
today's figures the answer changes nothing: Meta's next model scores 44 and would still be fifth.

**S5. The choice on Rule C should match the proposal's own second thoughts.** Choice 3 recommends
"yes, which adds Microsoft today". The closing section says that before Rule C is ruled, a
search for positions should be made with John's go, "or the rule should be dropped". Choice 5
then asks for a go that includes Microsoft's 7 places. As written, John is asked to approve a rule
whose author doubts its list. The proposal should recommend Rule C only after the search is made
(and ask for that search in choice 5), or should recommend against it for now. Its low-to-moderate
confidence already points that way.

**S6. Four entries on the verify list can be cleared or narrowed from pages already opened.**
- Entry 29: cleared by the Forum's membership page (M1).
- Entry 31: the footer of [x.ai](https://x.ai/) reads "© 2026 SpaceX Super Intelligence LLC". That
  names the company behind the page, though not how it is tied to SpaceX.
- Entry 32: the footer of [qwen.ai](https://qwen.ai/) reads "Powered by Alibaba Cloud". That names
  Alibaba, though "powered by" is not quite "made by".
- Entry 33: the footer of [microsoft.ai](https://microsoft.ai/) reads "© Microsoft 2026" and links
  to Microsoft.com.

Entries 28, 30, 34 and 35 remain open.

## Notes

**N1. Every ranking gives what the proposal says it gives, by name.**
- *Arena*, chat ranking by lab, "Nov 19, 2026", 29 labs: Google 1,527; Meta 1,511; Anthropic 1,506;
  Moonshot 1,488; OpenAI 1,485; Alibaba 1,484; Z.ai 1,482; Xiaomi 1,481; DeepSeek 1,475; SpaceXAI
  1,475.
- *Artificial Analysis*, best model per developer: Anthropic 65, OpenAI 62, Google 61, Meta 50,
  Moonshot (Kimi) 46, Alibaba (Qwen) 43, xAI (Grok) 35, Tencent 35, DeepSeek 33, Z.ai (GLM) 32.
  The table names models, not developers, so I matched each model to its maker by name.
- *Epoch AI*, best model per developer from its score file: Anthropic 173.4, OpenAI 172.8, Google
  DeepMind 169.7, Meta AI 161.7, Moonshot 161.2, DeepSeek 159.4, xAI 157.8, Alibaba 157.6, Z.ai
  (Zhipu AI) 157.1, Mistral AI 154.6.

The top five of all three is Anthropic, OpenAI, Google, Meta and Moonshot. The top ten of all
three is those five plus Alibaba, DeepSeek, xAI and Z.ai. The gaps after third on Artificial
Analysis (61 to 50) and on Epoch AI (Google's range 166.6 to 173.1 against Meta's 159.4 to 164.3)
are as the proposal says.

**N2. The other pages say what the proposal says.** Checked: the Forum's About page (its
wording on being industry-supported, on funding from member fees, and on its definition of a
frontier model); the Seoul commitments page (updated 7 February 2025, with the sixteen companies
and the four added later, as listed); Joanne Jang's post (5 June 2025, "I lead model behavior &
policy at OpenAI", and the Model Spec's guidance to "acknowledge the complexity of
consciousness"); Mustafa Suleyman's essay (19 August 2025, its title, "Today at Microsoft AI we
build AI", and "a dangerous turn"); Google DeepMind's About page (Google Brain and DeepMind brought
together); Meta's page ("Muse Wonder ... our frontier models"); Moonshot's page ("Try Kimi"); the
page titles for x.ai ("SpaceXSI") and z.ai (which opens the chat site); and the AGI Zeitgeist's
decision 5 ("'frontier' is a judgment", `docs/weekly-reading.md` on its main branch). Anthropic's
page on ending conversations is in the record already, and the record's note on it says the
feature came "mainly as part of the company's work on possible AI welfare". One thing to keep in
mind under Rule C: Jang's post says what her role was in June 2025, and whether she still speaks
for OpenAI in that role was not checked.

**N3. The cost estimate is sound.** The arithmetic holds: 7 rows, 7 places per developer, and two
searches as the floor per place, since the home page promises that every "nothing found" rests on
"two or more searches" (`site/src/components/Rebuilt.astro`, line 157). The time per place is
marked as an estimate (entry 34), and the extra cost of searching developers whose material is
largely in Chinese is named. The code limits are as cited: three columns at `rebuild.css` lines
18 and 52, and the refusal of more than five developers at `Rebuilt.astro` line 62. So six
developers (Rule A with Rule C) need a code change, and choice 5 says so. The phone figures for
three developers match mine exactly: a table 1,273 pixels tall at 375 wide, and 705 tall at 1,280,
in a table 900 wide whose column is 1,028 wide. I did not repeat the browser stand-ins for five and
ten developers. The proposal's conclusion (five fit without a new design; ten need one on a
computer) follows from the layout's code. One thing the estimate leaves out is the checking
session's own searches, which it costs at "about half" in time but not in searches.

**N4. The conflict is otherwise handled honestly.** The proposal says it read the rankings before
choosing a rule, that Anthropic is first on two of the three, and why it uses all three. It
names the Forum as an industry body of which Anthropic is a member, and says a wider record will
make Anthropic's column look more alone. One thing worth adding inside the repository (not on a
public page): the model ranked for Anthropic on Arena's lab ranking, Claude Opus 5.5, is the
model that wrote the proposal and this check.

**N5. The four things and the order.** Each of the five choices carries the choice, confidence
with a reason, standard or judgment, and the strongest alternative with its cost. The order works
for putting them one at a time: first whether to widen at all, then which rule, then Rule C, then
how often the list is read again, then the go. The one strain is S5. A small point on choice 1:
calling a rule from outside "standard practice" leans on the AGI Zeitgeist's use of METR's results
file, which is a source for one measure, not a list of whom to cover. The family's nearer
precedent for a list of whom to follow is The Belt Equation's missions, which are John's by
ruling. The proposal says this in its sibling section, and choice 1 could say "judgment call
following a family habit" with more accuracy.

**N6. Facts from memory.** Apart from entries 28 to 35, I found two claims without a page behind
them. The first is that "a developer can train toward a known test". That is general reasoning,
and Epoch AI's index page lists the same worry among its common questions. The second is that
Arena "measures what people prefer in a chat, not capability in general". Arena's page heads the
board "Which model is the best at everyday chat?", which supports it. Neither needs a new entry.

## Verdict

**Not yet fit to put to John.** M1 changes one of the three rules' results and a row of the cost
table, and M2 understates the conflict the proposal exists to handle. Both are quick to fix from
pages already opened. With those fixed, and S1 (how close the line at five is) and S5 (the
recommendation on Rule C) addressed, the proposal is a sound and fair basis for John's ruling. Its
reading of the rankings is accurate, its cost estimate holds, and it states the conflict openly.

## Second check, 2026-11-21: the revised proposal

Written later on 2026-11-21 by the same session (Claude, Opus 5.5). It checks only what the
writer changed in the proposal and in entries 28 to 35 of `docs/verify-list.md`, both still
uncommitted.

**Each finding is fixed.**
- **M1.** The proposal now quotes the Forum's membership page, with its six members. Meta's row
  says "yes" under Rule B, and Amazon has a row of its own. The summary reads "The Forum's list
  gives six, adding Amazon, Meta and Microsoft", and the cost row reads 3 developers, 21 places and
  42 searches. The weakness now says the Forum's list leaves out Moonshot only, of the five that all
  three rankings put in their top five, and it explains how close Rule B is to Rule A. I opened
  Amazon's new link, [nova.amazon.com](https://nova.amazon.com/). It opens a chat page titled
  "Amazon Nova", as the row says.
- **M2.** The opening section and Part 4 now say 5 things are counted, all of them Anthropic's,
  with OpenAI offering one of the same five, and that the 6 is a count of places. They also say
  the brief's point stands. Part 4 adds, inside the repository only, that the model Arena lists
  for Anthropic wrote both the proposal and this check.
- **S1.** A new paragraph, "How close the line at five is", gives the one-point gap on Arena, the
  3-point gap on Artificial Analysis and the overlapping ranges on Epoch AI. Its figures match my
  reading, rounded to whole numbers. Choice 2's confidence has dropped to low-to-moderate, for
  that reason, and the choice names the gap after the third developer as the firmer line.
- **S2.** Both missing ties are added and quoted correctly: Google DeepMind's funding of the paper
  behind Epoch AI's index, and Epoch AI's holdings in semiconductor and AI stocks.
- **S3.** The figure of 46 for xAI's model is now said to have been seen on two loads, not seen on
  mine, and not reliably reproducible, and the point it served is said not to rest on it.
- **S4.** Rule A now says a ruled wording must name the board, the filters, and whether a model
  must be on public sale to count, with the Meta model as the worked case.
- **S5.** Choice 3 now recommends waiting. Rule C would be ruled only after a search for
  developers' published positions, which choice 5 asks John to approve. The choice notes that
  Jang's role was given as of 2025-06-05. Rule C now taken at once is the strongest alternative,
  with its cost.
- **S6.** Entries 29 and 33 are cleared, and 31 and 32 are narrowed, each with the footer text I
  found. Entries 28, 30, 34 and 35 stay open. Choice 1 is now called a judgment call following a
  family habit, as my note N5 suggested.

**Two small points, neither blocking.**
- Choice 5 asks for a go for "one bounded search" for developers' positions, but does not give
  its bounds. John would be approving a search without being told how far it goes. A bound would
  settle it: which developers (for example the twelve in any ranking's top ten), and how many
  searches each (for example two, the floor this project already uses).
- Choice 2 now admits that the line after the third developer is firmer than the line at five,
  but its strongest alternative is still "the top ten of all three". The firmer line is offered
  only as choice 1's alternative (keep the three). That is fair, since keeping the three is what
  the firmer line gives today. But it means John meets the firmer line before the case for it is
  made, so it would help to say in choice 1 that its alternative is the gap after the third
  developer, made into a rule.

**Verdict.** The proposal is fit to put to John. Both must-fix items and all six should-fix items
are fixed, and every page added since the first check has been opened. Adding the bound in choice
5 before it goes would be worth two lines, but it is not a reason to hold it.
