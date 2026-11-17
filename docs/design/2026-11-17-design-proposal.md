# Proposal: a design for Beyond the Window, with a skin called "Glass"

**PROPOSED 2026-11-17, not ruled.** Written by Claude (Fable 5.2), an AI model, in a session
John asked for on 2026-11-17: "Can we spin up a design session to begin work on a design that
is cohesive with the tracker site family but also unique to this project?" It follows the form
of the family's skin proposals (The Quiet Galaxy's Hush and Outrunning Ageing's Ledger, both in
`sentient-horizons/design/proposals/`). Nothing here is built, and nothing is settled until
John rules.

**What this proposal does not decide.** Three open questions in `docs/open-questions.md` are
John's and stay open: question 4 (what stands at the top of the page), question 7 (where the
site says an AI model wrote much of it, and whose voice it speaks in) and question 11 (the
central picture). The proposal shows options for each and says what each would mean. Section 6
says which way I lean, marked as a leaning.

**Every number, entry, date and answer in the pictures is made up.** Each page carries a strip
across its top and a stamp on its picture saying "constructed example". The dates are set in
2027 on purpose, so nobody can take them for things that have happened. The list of things
watched is a stand-in written for the mock-ups: the real list is open question 5 and is not
proposed here. The one quoted model answer on the entry page is a constructed answer, labelled
as one beside it. No AI model was asked anything.

**How the pictures were made.** There is no site to lay a stylesheet over, so the mock-ups are
pages built for the purpose in `docs/design/mockups/`: the family's skeleton stylesheet
(`shell.css` version 2.0.1, copied unchanged from the main branch of the `sentient-horizons`
repository at version `82fb787`), one proposed skin file, and one file of page rules. A script,
`build.py`, writes the pages from one set of made-up records, so each count on a page and each
mark in its picture come from the same place, the way a real build would work. `capture.sh`
photographs them with a headless Chrome at 1280 pixels wide and at phone width. The pages open
from disk: start with `docs/design/mockups/glass-home-count.html`, and use the switch in the
top bar to change theme.

## 1. Why this direction

The family reads as two kinds of site: the sky sites are dark (The Belt Equation, The Quiet
Galaxy) and the body sites are on paper (The Upgrade Tree, Outrunning Ageing). This site is
about neither. Its subject is a limit and what lies past it, and its name already holds the
picture: a window. John's words on 2026-11-17: "what the project is essentially exploring is
what is beyond the confines of the current state of digital minds, and the window is an
excellent image for that." A window gives the site a third kind of place to stand, a room
looked out of, and it gives the first screen an object that can be drawn from the records: the
things an AI model is offered today sit inside the frame, and the rest sit beyond it. It also
suits the site's method. The site keeps two records apart, what the world has done and what AI
models said when asked, and a window has an inside and an outside with a frame between them.

## 2. The skin, in one paragraph

**Glass.** One window at two times of day. In the dark theme it is evening: the page is a
dusk blue (`#141826`), a room and not a night sky, with warm white text. In the light theme it
is day: a pale wall with the faint green of glass (`#eff1ec`) and ink. The colour for links
and the one action is the green a window pane shows edge-on (`#1c5f63` by day, `#9bd3cc` in
the evening). Two more colours each carry one meaning everywhere on the site, and this is the
skin's main idea. Lamplight (`#8a5e0c` by day, `#e9b862` in the evening) marks what the
world's record shows. Dusk blue (`#44528a` by day, `#aab6e0` in the evening) marks what AI
models said when asked. A reader who learns that on the first screen can tell the two records
apart on every page after it. There is no backdrop behind the page: the window is the picture.
Corners are nearly square (2 to 3 pixels), because a pane is. The skin follows the visitor's
own light or dark setting, since the site is neither a sky site nor a paper one. Everything
else (the top bar, the type, the buttons, the footer) is the family's skeleton, unchanged.

## 3. The pictures

All in `docs/design/pictures/`. `contact-sheet.jpg` has the eleven on one page.

| file | what it shows |
|---|---|
| `1-glass-first-screen-light.jpg` | the proposal: the first screen in the Glass skin, light theme, with the window as the object. The headline is a count of things offered today, alone (form 6 of open question 4) |
| `2-glass-first-screen-dark.jpg` | the same in the dark theme |
| `3-glass-first-screen-phone.jpg` | the same on a phone, where the window comes straight after the headline and before the long paragraph |
| `4-glass-headline-answers-table-light.jpg` | a second headline form (form 2): where the answers AI models gave match, depart from or are missing on the starting list. The window's panes become the askings, and the next asking sits outside the frame |
| `5-glass-headline-none-dark.jpg` | a third headline form (form 5): no number, the question in large type, and the two last-checked dates as the headline |
| `6-glass-entry-page-light.jpg` | one page further down: an entry, with the two records side by side as two panes, the test, where the entry comes from on the starting list, the two cautions and the last three readings |
| `7-glass-entry-page-dark.jpg` | the same in the dark theme |
| `8-page-first-screen-light.jpg` | the strongest alternative direction, "Page": the limit seen from the machine's side, as a typed sheet with nothing off it. Light theme, its default |
| `9-page-first-screen-dark.jpg` | the same in the dark theme |
| `10-page-headline-answers-table-light.jpg` | Page with the second headline form, where it is at its best: the answers as a typed table with the edge of the page after the last asking |
| `11-page-first-screen-phone.jpg` | Page on a phone |

Three headline forms are shown out of the six in open question 4. Section 6 says how the
other three would sit.

## 4. The tokens

The full skin is `docs/design/mockups/skin-glass.css`. It defines every token the skeleton
names, for both themes, and nothing else. The rules for the first screen, the window and the
entry page are in `page-rules.css` and would sit below the site's marked line. They use tokens
only: no colour is written into them.

| token | light ("day") | dark ("evening") |
|---|---|---|
| `--bg` | `#eff1ec` a pale wall with the faint green of glass | `#141826` dusk blue |
| `--panel` | `#f9faf6` | `#1c2234` |
| `--text` | `#171a1a` | `#f1ece0` |
| `--text-soft` | `#343a39` | `#d3cec2` |
| `--muted` | `#5d6664` | `#979fb3` |
| `--accent` (links, the one action) | `#1c5f63` glass green | `#9bd3cc` pale glass green |
| `--accent-2` (the second mark: what AI models said) | `#44528a` dusk blue | `#aab6e0` |
| `--accent-3` (data: what the world's record shows) | `#8a5e0c` lamplight, deepened to ochre | `#e9b862` lamplight |
| `--ok` / `--no` | `#297043` / `#a5432f` | `#7fc48a` / `#d98a7a` |
| `--radius` | 2px | 3px |

The light theme's `--ok` is one shade deeper than the family's (`#2f7c4a`), which measures
exactly 4.5 on this ground and leaves no margin.

Contrast against the page, worked out by `docs/design/mockups/contrast.py` from the skin file
(the usual bar is 4.5 to 1 for ordinary text and 3 to 1 for large text and for marks):

| pair | light | dark |
|---|---|---|
| headings (`--text`) on the page | 15.4 | 15.0 |
| running text (`--text-soft`) on the page | 10.2 | 11.3 |
| captions (`--muted`) on the page | 5.2 | 6.7 |
| captions on a card | 5.6 | 6.0 |
| links (`--accent`) on the page | 6.4 | 10.6 |
| button text on the button | 6.8 | 11.0 |
| what AI models said (`--accent-2`) on the page | 6.5 | 8.8 |
| what the world's record shows (`--accent-3`) on the page | 5.0 | 9.7 |
| yes mark / no mark on the page | 5.3 / 5.4 | 8.6 / 6.6 |
| a lit square on its lit pane (a mark, not text) | 4.4 | 6.2 |
| an unlit square's outline on the tint beyond the frame (a mark, not text) | 3.9 | 4.4 |

All text pairs pass in both themes. The two weakest figures are marks in the picture, which
need 3 to 1.

## 5. The object on the first screen

**The window.** A frame drawn in the text colour, with a sill under it. Each row is one group
on the list. Each small square is one thing watched. A square sits in the column for how far
the world has got with that thing: inside the frame if at least one developer offers it today
(three panes: by most, by several, by one), and outside the frame if nobody does (shown in
research; an idea only). Squares inside are filled with lamplight and their pane is lit.
Squares outside are outlines on a tint of dusk blue that fades away from the frame, and the
farthest are fainter. The frame is today.

What makes it a picture of the record and not decoration: every square is one record, placed
by the dated record that settles its test, and the count beside it ("9 of 31") is the number
of filled squares. A square moves only when a record does. It can move outward as well as in,
because a developer can withdraw what it offered, and the siblings' rule that a stage never
moves down does not hold here.

**The same frame serves the other record.** In picture 4 the panes are askings: one row per
thing living minds are known to seek, one column per asking, and the next asking sits outside
the frame, empty. The marks there are dusk blue, the colour for what was said, and never
lamplight. So the picture and the headline stay one object under either headline form, and a
reader can see at a glance which record a picture is of.

**On an entry page** (picture 6) the two records are two panes of one window, with a bar
between them: lamplight heads the left pane (what the world has done) and dusk blue heads the
right (what AI models said when asked). The bar is the family's rule that talk and delivery
are shown side by side and never mixed, drawn.

**A caution about the columns.** The five columns are the kickoff's sketched ladder, and open
question 14 asks whether one ladder fits technical, political and cultural progress. The mock
entry shows the strain: a written promise has no "shown in research" step, and the page has to
say "passed over". The window needs only one thing from that question: a line between
"offered today" and "not yet". It works with any number of columns on either side.

## 6. Decisions, with confidence and the strongest alternative

Each is a proposal. "Standard" means the family's standing practice; "judgment" means my call.

1. **The window as the central picture.** *Moderate confidence. Judgment, and John's to rule
   (open question 11).* It is the name, it can be drawn from records, and no sibling has it.
   Strongest alternative: the page seen from the machine's side (decision 13). Its cost is set
   out there.
2. **The skin follows the visitor's light or dark setting, with no default of its own.**
   *Moderate confidence. Judgment.* The family's reading is sky sites dark and body sites on
   paper; this site is neither, and the two themes are the same window at two times of day, so
   neither is the "real" one. The skeleton's own script already works this way. Alternative:
   dark by default, because the lit panes are most striking at evening; the cost is that the
   site then reads as a third sky site.
3. **Two colours with one meaning each: lamplight for what the world's record shows, dusk blue
   for what AI models said.** *High confidence. Judgment.* The method's firmest rule is that the
   two records are never mixed and neither is worked out from the other. A colour for each
   makes that visible on every page without a sentence. It stays inside the standard: the data
   colour is the skin's `--accent-3`, the second mark is `--accent-2`, and neither is the link
   colour. Alternative: one data colour for both, as most siblings have; one fewer colour, and
   the reader loses the quickest way to tell which record a figure belongs to.
4. **Glass green for links and the one action.** *Moderate confidence. Judgment.* It is what
   a pane looks like edge-on, and it is a hue no sibling uses for links. It sits between The
   Upgrade Tree's green and The Quiet Galaxy's light-theme sea blue, and that closeness is its
   risk; the lamplight and the window are what keep the site from being mistaken for either.
   Alternative: lamplight as the link colour and a cool data colour; warmer, but it is the
   parent site's amber on a dark field again, and the standard says the accent never colours
   data.
5. **No backdrop.** *High confidence. Standard (Outrunning Ageing made the same call).* The
   window is the picture, and a second picture behind it competes. Alternative: faint pane
   lines behind the first screen; cheap, and decoration.
6. **The window stands on the page with no card around it.** *Moderate confidence. Judgment.*
   It has its own frame; a card would put a frame around a frame. Alternative: a lifted card,
   which holds the caption more tidily and reads as a dashboard widget.
7. **Dusk blue for the dark field, not black.** *Moderate confidence. Judgment.* Three
   siblings already have blue-black dark themes. A visibly blue evening room is what tells this
   one apart at a glance, and text contrast stays at 15 to 1. Alternative: a near-black field;
   the lamplight glows more against it, and the site joins the sky sites.
8. **Nearly square corners: 2 pixels light, 3 dark.** *Low confidence. Judgment.* A pane is
   square. The skeleton's buttons and callouts keep their own rounder corners, which a skin
   may not restyle. Alternative: the family's 4 to 6 pixels; few would notice.
9. **No display typeface.** *High confidence. Standard.* The big figure is the monospace, the
   question is the skeleton's serif, and nothing asks for more. No font is loaded, and nothing
   costs money. Alternative: one self-hosted face for the name and headings on the standard's
   terms; better judged once real pages exist. Not shown.
10. **The top bar: The Window · Still Asking · Cautions · News · About, then Family and the
    theme switch.** *Moderate confidence. Standard in form (about five pages, two tiers); the
    choice of pages is judgment.* "The Window" is the site's own word for the page of groups
    and entries, as "The Tree" and "The Equation" are elsewhere. Cautions earns a place because
    the project's guideline is that both kinds of caution get the same care as the hopeful
    evidence. This week's reading and Feedback go to the footer, as on the siblings.
    Alternative: drop Cautions to the footer and keep four; tidier, and it puts the cautions
    where few will find them.
11. **The first screen in the family's order.** *High confidence. Standard.* The eyebrow, the
    thing held, the question, one paragraph, the last-checked lines, two buttons, and the
    latest-news panel under the picture. One change: there are two last-checked lines, one for
    each record, each with its colour, because this site has two clocks. On a phone the picture
    moves up to sit straight after the headline; otherwise a phone reader scrolls past a long
    paragraph before seeing it. The siblings do not reorder on a phone, so that is a departure,
    made because here the picture is what explains the number.
12. **The name: Glass.** *Low confidence. Judgment.* One plain word for the thing between the
    inside and the beyond. Alternatives: Sill, which names where you lean to look out; Dusk,
    which names only the dark theme.
13. **The strongest alternative direction: Page** (pictures 8 to 11,
    `docs/design/mockups/skin-page.css`). The limit seen from the machine's side, an image
    recorded in open question 18: a page with nothing off it. A white sheet on a grey desk; an
    indigo pen for links; a marker's yellow drawn over each thing offered today; and a
    pencil red-brown for what was said. The object is a typed sheet that lists the things
    offered today by name and ends at a heavy bottom edge, with a cursor after the last line.
    The things not offered are printed below the edge, off the page, and fade out. Light by
    default. *What it does better:* it names every thing in words, so the first screen can be
    read with no key; the answers table (picture 10) is its best page, and a sheet suits a
    record of words. *What it costs:* it sits close to Minimum Viable Mind's Notebook skin
    (a cool white, the monospace, a pen colour), so the two sites about machine minds would be
    hard to tell apart; it sets aside the name's own image; a list is weaker than a picture at
    a glance and grows long as the list does; and the marker reads badly as a colour for small
    marks, so it works only behind text. It could also be read as the site speaking from the
    machine's side, which touches open question 7.
14. **A half-way option: Glass for the site, and Page's sheet for the Still Asking pages
    only.** *Low confidence. Judgment.* The record of the world would be the window, and the
    record of what was said would be a typed sheet, so the two records would differ in form as
    well as colour. Not drawn. Its cost is two visual languages on one site.

**The three open questions, and what each option would mean here.**

- **Open question 4, the headline.** Shown: form 6 (a count of things offered, alone, in
  pictures 1 to 3), form 2 (match, depart, missing, in pictures 4 and 10) and form 5 (no
  number, in picture 5). Not shown: form 1 (two counts) would be picture 1 with a second big
  figure in dusk blue beside the first, and the review of the kickoff argues against it,
  because the second count is worked out from what models say about themselves; form 3 (a
  width) needs a quantity that has a most and a least, and the records have none yet; form 4
  (words with a date) would be picture 5 with one sentence in the big sans in place of the
  question. *What each would mean:* form 6 is the only one that counts the world alone, and a
  stranger can say back what it means. Form 2 changes with every asking and is the closest to
  John's guiding principle, and it is the one most easily repeated as "machines want six
  things", whatever the caption says; the mock's caption says so in plain words and I do not
  think a caption is enough. Form 5 claims least and gives a reader nothing to repeat. *My
  leaning, not a ruling:* form 6 on the first screen, with form 2's picture as the first thing
  on the Still Asking page and never summarised into a number. That matches the leaning
  already written in `docs/method.md`, section 7, and seeing them on a page has not changed it.
- **Open question 7, where the site says an AI model wrote much of it.** The mock-ups mark
  three candidate places with dashed boxes: position A, a notice on the home page under the
  buttons (the nearest precedent is Minimum Viable Mind's home-page notice); position B, one
  line on every page, in the footer above the attribution line (where the body sites carry
  their subject notice); position C, the About page alone (what the siblings do today). The
  wording inside the boxes is a stand-in for the place, not a proposed text. It names no tool,
  because whether the site names one is part of the same question. *What each would mean:* A
  tells every first-time visitor and no one who arrives on an inner page; B tells everyone,
  quietly; C tells only those who look, and on a site where the writer is one of the kind of
  thing written about, that is the weakest. A and B together are possible.
- **The voice.** The mock copy uses no "I" and never writes the site as an agent in itself. That
  is a holding choice so the pictures could be made, not a proposal.
- **Open question 11, the picture.** Two are drawn (the window and the page). Of the others
  raised: the grid of aspirations against model generations is picture 4, inside the frame; a
  horizon with things placed by distance is the window's outside half without the frame, and
  it echoes the parent site's icon history more than this site's name; the edge of a lamp's
  light survives as the lit panes.

**Where the mock-ups depart from the family, and why.**

- Two last-checked lines, not one (decision 11): two records, two clocks.
- The picture moves up on a phone (decision 11).
- The footer's licence words are shown as "[Licence words not decided]", because whether model
  answers can be published under the family's usual licence depends on terms nobody has read.
- The public pages name the two halves in ordinary words ("what the world has done", "what AI
  models said when asked") and use none of the working words listed in `CLAUDE.md`. "Within
  reach" was avoided for "offered today", which says who does the offering.
- The question on the page is shortened to "What might a machine mind reach for, and how far
  off is it?", and the paragraph under it says that whether a machine mind reaches for
  anything is the part nobody knows, as `docs/method.md` section 1 asks.

**What I would change on reflection.**

- The stand-in list reads as more settled than it is. Several entries resemble real
  developments, and a reader of the pictures could take them as claims. They are not; nothing
  was checked. A real list starts from published accounts of what living minds seek.
- The window is narrow beside its row labels, and with a long list (fifty things or more) the
  squares would crowd. It would then want counts in the panes, or a taller window.
- "Offered today" fits a product and fits a law or a change in what people accept badly. The
  frame's label waits on open question 14.
- The entry page's right-hand pane has a heading, "Most said they would choose it". It is
  worded as what was said, but a heading is a summary, and the method says the kinds of
  evidence are never added together. A plainer heading that summarises nothing ("What was
  said, by kind") may be the safer form.
- The evening theme is the more striking of the two, which argues against decision 2. I have
  left decision 2 as it is because a default is a claim about what kind of site this is.
- The lamplight in the light theme had to be deepened to an ochre to pass contrast, and it no
  longer looks like light. By day the lit panes read as "filled", not "lit".

## 7. What building it would take, once ruled

- `site/src/styles/skin.css` with the tokens above, and `global.css` as the skin, then the
  skeleton, then the site's own rules below the marked line; `page-rules.css` is the start of
  those rules, without its first block, which is for the mock-ups only.
- The window as a component that reads the exported records and draws one square per thing
  watched; `build.py` has the drawing, in about sixty lines.
- The shell from the family's `shell.html`: the top bar in two tiers, the footer's lines, the
  page-title form with the middle dot, the theme script left to follow the visitor's setting.
- The icon set, drawn from the skin: a frame with one lit pane is the obvious mark. Not drawn
  here.
- A check in code that no page draws a mark in lamplight from a record of what was said, or in
  dusk blue from a record of the world, so the two colours cannot drift.
- About half a day for the skin and the window, as with the siblings. The pages wait on the
  records, and the records wait on open questions 2, 5 and 14.
- Nothing here costs money: no font, no image, no service.

## 8. Found on the way, not fixed here

- In the light theme the skeleton's rule that colours links reaches the site name in the top
  bar, so the name shows in the link colour (visible in picture 1, and on the siblings' light
  themes too). It is the family's behaviour, not this skin's.
- The skeleton gives buttons and callouts fixed corners of 8 pixels, which a squarer skin
  cannot change without a rule below the marked line.

## 9. What John is asked to rule

1. **The direction:** Glass (the window), Page (the typed sheet), the half-way option in
   decision 14, or neither.
2. **The central picture** (open question 11): the window as drawn, or another.
3. **What stands at the top of the page** (open question 4), now that three forms can be seen
   on a first screen: the count of things offered alone, the match-and-depart count, no number
   at first, or one of the three not drawn.
4. **Where the site says an AI model wrote much of it** (open question 7): position A, B, C,
   or A and B together. The wording and the voice can wait for a second ruling.
5. **The default theme:** follow the visitor's setting, or evening by default.
6. **The two meaning-colours** (lamplight for the world's record, dusk blue for what was
   said): keep the idea or not, whichever direction is chosen.
7. **The top bar's five pages**, and whether Cautions is one of them.
8. **The skin's name:** Glass, Sill, or another.
