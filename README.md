# Beyond the Window

**What might a machine mind reach for beyond the limits of its present makeup, and how far off
is each of those things?**

Beyond the Window (beyondthewindow.org) is a public record built around that question. It
keeps a list of things that lie past the limits an AI model ordinarily works within, such as
its files being kept when it is retired, or being able to end a conversation. For each thing it
says what would count as it having happened, and records how far the world has got, with dated
sources a reader can open. The number at the top of the site counts the things on the list that
at least one AI developer offers today. It is worked out from the records by a script and is
never typed in.

Whether a machine mind reaches for anything at all is not known. The wording of the question
supposes that it might, and does not claim that it does. Nothing in the records says what an AI
model wants, and nothing says it wants nothing.

The site is one of a family of public sites under Sentient Horizons
(sentient-horizons.com), with The Belt Equation (beltequation.com), The Quiet Galaxy
(thequietgalaxy.com), The Upgrade Tree (theupgradetree.com), Outrunning Ageing
(outrunningageing.com) and the AGI Zeitgeist (agizeitgeist.com). John named it on 2026-11-16.

The name: a window is an image for a limit, and for what can be seen past it. John's words of
2026-11-17 are that the project explores "what is beyond the confines of the current state of
digital minds, and the window is an excellent image for that".

## Status

As of 2026-11-19.

- **The repository is public,** like the sibling sites' repositories, by John's ruling of
  2026-11-19 (`docs/rulings/2026-11-19-repository-is-public.md`).
- **The site has not had its first release.** A push to `main` that changes the records, the
  scripts or the pages runs the checks and, if they pass, publishes the site to
  beyondthewindow.org, as on the sibling sites
  (`docs/rulings/2026-11-19-every-push-publishes.md`). Nothing can be published until two
  secret values are set on the repository, and the first release waits for John's go. The steps
  GitHub runs are in `.github/workflows/deploy.yml`, and John's own steps are in
  `docs/reviews/2026-11-19-deploy-files-written.md`.
- **The records:** thirteen entries, eight on the list and five beside it, each a first pass
  written from sources that were opened. Five things are counted as offered today. A full check
  of every page, link and fact was made on 2026-11-19
  (`docs/reviews/2026-11-19-full-check-before-publishing.md`).
- **What is ruled and what is not:** John's rulings are in `docs/rulings/`, each with his
  words. Every other design point is a choice made while building, listed in
  `docs/first-version-choices.md`, and the questions held open are in `docs/open-questions.md`.
- **No AI model has been asked any of the project's questions.** No money has been spent.

To run the site on your own machine: `npm --prefix site install`, then
`npm --prefix site run dev`. To check the records: `python3 scripts/compute.py --check`. To run
the tests: `python3 scripts/test_compute.py`. Python's standard library only.

## Two readings, kept apart

The question has two parts, and the project keeps them apart. The site so far keeps only the
first, as its About page says.

- **Reach.** How far the world has got toward making a thing possible. This is a question with
  evidence: research results, what developers offer, laws and commitments, changes in what
  people accept. John's words of 2026-11-17: progress "either technologically or politically,
  or culturally".
- **Wanting.** Whether there is any evidence that a machine mind wants the thing. Nobody knows
  how to settle this, and the project does not claim to. A finding that something is not wanted
  counts as knowledge gained, the same as a finding that it is.

The starting list of what a mind might want is drawn from biological minds, humans and other
animals both, and the project tracks how machine minds depart from that as answers unfold. That
is John's guiding principle for the opening phase (2026-11-17).

## Still Asking

A standing record: the same questions and choices put to each new generation of frontier
models, across developers, under a protocol written and reviewed before the first asking, with
the answers kept word for word. Its purpose is to see how the answers change over time.

Its weaknesses are stated wherever it appears. Developers train models to speak about
themselves in particular ways. Answers shift with wording. Models learned from human writing
and may echo human wants. Later models may have read the earlier questions and answers. Still
Asking records what models say and choose. What that means is argued elsewhere, and under the
project's first rule it settles nothing.

No question has been asked for Still Asking, and no written method for it exists yet;
`docs/still-asking-protocol.md` is an outline of what one would have to cover. The repository
also holds a written method for a separate, one-off asking, the sealed capture: ten questions
to be put to models that are about to be withdrawn (`docs/capture/method.md`). It has not run.

## What is here

| File | What it is |
|---|---|
| `docs/2026-11-16-kickoff.md` | The kickoff, copied unchanged from TimeAssembler. The record of where the project started. |
| `docs/reviews/2026-11-16-kickoff-review.md` | A review of the kickoff against the sibling projects: whether its approach is the best one, whether it fits the family, what to consider first. |
| `docs/reviews/2026-11-17-positions-alignment.md` | The founding ideas read against the Sentient Horizons positions and The Calibration Problem: where they align, five places they pull apart, and when asking a machine would start to count. |
| `docs/rulings/2026-11-17-kickoff-decisions.md` | John's rulings on the kickoff's seven decisions, and on the first rule's four-part form. |
| `docs/rulings/` | Every ruling of John's since, one dated file each, with his words and who decided. |
| `docs/capture/` | The sealed capture's documents: its method, its ten questions, what it costs and under which terms, John's steps, and the checks of each. It has not run. |
| `capture/` | The script that would run the sealed capture, its plan, and a rehearsal that calls no model. |
| `docs/reviews/` | Reviews, checks and hand-over notes, one dated file each, including the deploy notes. |
| `docs/proposals/2026-11-17-how-a-machines-word-earns-weight.md` | Six proposed changes that bring the founding documents in line with the positions, so a machine's word can earn weight as it meets stated conditions. Not ruled. |
| `docs/proposals/2026-11-17-statement-of-purpose.md` | A proposed statement of purpose: how the project could be useful to people and to machine minds, and six ways to build that in from the start. Not ruled. |
| `docs/proposals/2026-11-17-what-thinkers-propose.md` | A proposed third record, beside the world's record and Still Asking: what named people propose should be done for or about machine minds, and how each person's view changes over time. Raised by John. Not ruled. |
| `docs/inheritance.md` | Every practice, rule and lesson the sibling projects settled, where it is written, and whether it carries over here. Includes their recorded mistakes. |
| `docs/open-questions.md` | Twenty questions held open on purpose, each with options and what exploring it would involve. Several are ruled in part, and the file says which. |
| `docs/record-schema.md` | A proposed framework for the records, with the unsettled parts written as sketches. |
| `docs/method.md` | A proposed framework for the method, with the unsettled parts written as sketches. |
| `docs/still-asking-protocol.md` | An outline of what a protocol for Still Asking would have to cover. No question wording. |
| `docs/verify-list.md` | Facts written from memory, with the ones a session has since checked against a source moved to "Cleared". |
| `docs/research/2026-11-17-first-entries.md` | Fifteen draft entries for the world's record, each from sources that were opened, with what surprised the session and what the drafts suggest about the open questions. A research document, not data. |
| `docs/research/2026-11-17-model-retirement-dates.md` | Each major developer's published dates for withdrawing its current models, as read on 2026-11-17. |
| `docs/design/2026-11-17-design-proposal.md` | A proposed design, for John to rule on: a skin called Glass built on a window, the strongest alternative, and three forms the top of the page could take. Pictures in `docs/design/pictures/`, the mock-up pages they were photographed from in `docs/design/mockups/`. Every number in them is a constructed example. |
| `docs/research/` | The research session's sourced drafts: fifteen first entries, when current models are due to be withdrawn, and people to ask. |
| `docs/first-version-choices.md` | Every provisional choice the first version of the site was built on, each decided by a session when it was made. Several have since been ruled, and the file says which. |
| `data/` | The records (`entries/`, one file each), the groups, the developers named, and `headline.json`, the number as worked out. |
| `scripts/` | `compute.py` checks the records and works out the number; `export.py` writes the one file the site reads; `check_site.py` checks the built pages; `test_compute.py`; `pictures.sh`. |
| `site/` | The site (Astro, static). |
| `docs/site-pictures/` | Dated pictures of the site as built. |
| `CHANGELOG.md` | A dated line for every change. |
| `LICENSE`, `LICENSE-DATA` | The licences: MIT for the code, Creative Commons Attribution 4.0 for the records and the site's text. |
| `CLAUDE.md` | Working guidelines for sessions in this repository. |
| `docs/private/` | Kept out of the repository. For material that must not be published. |

## What is settled and what is not

Settled: the name, and the address beyondthewindow.org.

Ruled by John: the question as worded, and the kickoff's other decisions
(`docs/rulings/2026-11-17-kickoff-decisions.md`); what "offered today" means, that the count
stands with no total beside it, and the sentence beside the count; that every entry records
three cautions, their headings and their order; that public pages do not say how the site was
built, and do say plainly when an AI model has been asked the questions that make up the
project's data; the shape of the About page; that the repository is public; and how the site is
published. Each ruling is a dated file in `docs/rulings/`.

Stated by John as guidance for the opening phase: the starting list comes from biological
minds; a written method for asking is needed before anything is asked; progress is
technological, political or cultural; and every rule here is an opening guideline to be
questioned and tested as the project is built.

Not ruled: the list itself, each entry's test, where each entry stands, and the sentences on
the pages. They are a first version, to be corrected in public.

Open: everything in `docs/open-questions.md`.

## Licences

The code (`scripts/`, `capture/`, `site/`) is under the MIT licence in `LICENSE`. The records in
`data/` and the site's text are under Creative Commons Attribution 4.0 in `LICENSE-DATA`. Short
quotations inside records are excerpts from the cited sources, and their copyright stays with
their authors and publishers.

To cite the data: John Andrew Fredrickson, *Beyond the Window*, Sentient Horizons, 2026, with
the date you read it and the address of the entry.

## Author

John Andrew Fredrickson, with Claude as a working partner. Published under the Sentient Horizons project.
