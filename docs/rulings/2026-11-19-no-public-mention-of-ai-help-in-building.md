# Ruling: the site does not say that an AI model helped build it

Ruled by John on 2026-11-19, in conversation with the master planning session. **Decided by:
John** (he stated it himself, unprompted). Written by Claude (Fable 5.2), an AI model.

This ruling replaces `docs/rulings/2026-11-18-how-the-site-declares-ai-authorship.md`, which is
left as it was. It settles the part of open question 7 in `docs/open-questions.md` about where
the public site declares who drafted it, and it changes guideline 3 in the project's
instruction file.

## His words

> "What is this obsession with disclosure about what has been discussed with AI? When it comes
> to our collaboration on building the project, we don't need to mention that publicly. The
> only place where disclosure of discussion with any AI Is relevant is when it is in actually
> asking the questions that make up the data of this project. Can you review the whole site and
> make sure it aligns with this?"

## Where the earlier practice came from

It did not come from John. The project's kickoff proposed that machine authorship be declared.
On 2026-11-18 a session showed him three placements for a notice and recommended keeping all
three, and he answered "As recommended". Sessions then added to it: a paragraph naming the
developer of the drafting model, a sentence on every entry page, and, on 2026-11-19, the master
session's own remarks that a further tie "belongs to the authorship notice". The weight of it on
the pages is the sessions' doing.

## What is ruled

1. **Public pages do not mention that an AI model took part in building the project:** the
   drafting of text, records or code, the checking, or anything discussed with a model along
   the way.
2. **Public pages do say when an AI model has been asked the questions that make up the
   project's data,** and say it plainly. That covers Still Asking, and the sealed capture once
   it has run.

This brings the project into line with the workspace rule that tools are not advertised.

## What the master session found on the pages, the same day

Read in the working copy while another session's changes were in progress.

*To remove:*

- **The notice "Who wrote this"** (`site/src/components/Notice.astro`), shown on the home page
  and the Still Asking page: "An AI model drafted much of the text, and that model is one of
  the kind of thing the site is about."
- **Every entry page** (`site/src/pages/list/[id].astro`): "It was drafted by an AI model from
  the sources above."
- **The About page, "Who Does What"** (`site/src/pages/about.astro`):
  - "and where and in whose voice the site says an AI model drafted much of it";
  - the paragraph beginning "Much of the text, the records and the code were drafted by an AI
    model, under my direction";
  - in the next paragraph, "The conflict is sharper than that. The model that drafted the text
    is made by Anthropic.";
  - "by a session that had not drafted them" and "by a session that had made none of them";
  - in the list of what is not known yet, "Who should check a site on this subject, when many
    of the available checkers are AI models."

*To keep, because it is about sources or about the data and not about how the site was built:*

- That several entries count things one developer does, and how many of the things counted
  rest on that developer's own pages.
- Where most of the first and second cautions come from (ruled the same day,
  `docs/rulings/2026-11-19-ties-between-sources-told-in-both-places.md`).
- That each entry is a first pass, when it was checked against its sources, and when it was
  corrected. The pages say what was checked and when, and not by what.
- John's name, that he decides what stands, and what he has and has not yet ruled.
- Everything on the Still Asking page about asking AI models, and the sentence on the About
  page that says whether any model has been asked anything.

## What does not change

- **Asked directly, John says so, and no page ever denies it.** That is the workspace rule, and
  this ruling does not touch it. A session making the removals writes nothing that says or
  implies that no AI model took part.
- **Documents inside the repository still say which were written by a model.** They are not
  public pages. If the repository is ever made public, that is put to John first.
- **Who decided is still recorded** in rulings and the worklog: John, mixed, or agent.

## One thing the master session said to him, once (decided by: agent)

With the drafting no longer mentioned, a reader is not told that the entries counting one
developer's commitments were drafted with that developer's model. The page still says how many
of the things counted rest on that developer's own pages, which lets a reader weigh the count.
The session flagged it and did not ask him to rule on it.

## What follows

- A session makes the removals after the session now editing those files has finished, and a
  different session checks the built pages.
- The part of the 2026-11-19 ruling on ties between sources that pointed to "the authorship
  notice" has nothing to point to and is moot.

Nothing is published.
