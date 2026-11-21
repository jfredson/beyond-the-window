# A news section for Beyond the Window

**PROPOSED 2026-11-21, not ruled.** Written by Claude (Opus 5.5) in a Claude Code session, on
branch `claude/news-section-79b5f4`, from John's request of 2026-11-21: "we need to create a news
section on the Beyond the Window site that mirrors the functionality of the other tracker
websites."

What is built on the branch: the post format, the News page, one page per post, the news feed,
the sitemap lines, the news check and its tests, and a guard that keeps made-up posts off the
site. What is not built, because it needs John's ruling or comes with the first post: the opening
post, News in the top bar, the latest-news panel on the home page, the links from an entry to its
posts, and the picture each post shows in a link preview. No real post is
written. The pages were drawn with three made-up posts, each marked "constructed", which live
outside the folder the site publishes from.

## 1. What the sibling sites do

The family's rules for news are the tracker pattern's rules 4.10 to 4.23
(`sentient-horizons/design/tracker-pattern.md`, master branch), ruled by John from 2026-10-18.
This site's inventory already takes them over as is (`docs/inheritance.md`, rows L4 to L8). Each
sibling's main branch was read on 2026-11-21.

**Where posts live and what they carry.** On the four sites built with the same site generator
as this one (The Belt Equation, The Upgrade Tree, The Quiet Galaxy, Outrunning Ageing), one
Markdown file per post at `site/src/content/news/YYYY-MM-DD-slug.md`, described in
`site/src/content.config.ts`. Every post carries a title, a date, a kind, a one-line summary,
the records it is about, its sources (a label and an address each), its photographs with their
licences, and optional "before" and "after" lines for its preview picture. The AGI Zeitgeist is
built by a Python script instead: its posts are in `docs/news/` with the same fields, and its
pages, feed and side list are written by `scripts/site.py`.

**The kinds of post.** The pattern's seven: start here (the one opening post), a rung reached,
an estimate revised, a flagged item ruled, a claim added or settled, the headline moved, the
method changed. Each site then added one or two of its own: The Belt Equation "mission news"
(2026-10-21) and "discovery" (2026-10-27); The Quiet Galaxy "essay" (2026-11-15); Outrunning
Ageing "a story from the field" (2026-11-09, `outrunning-ageing/docs/news.md`). The Upgrade Tree
and the Zeitgeist keep the seven.

**The pages.** The same on all five: `/news/` lists posts newest first (the date, the kind, the
title, the summary), with the opening post pinned on top as "Start here"; `/news/<file name>/`
is one post, with its eyebrow line (News, the date written out, the kind), the title, the
summary, the post, a line linking the records it is about and its sources, a "Follow the news"
line (the feed, the family's account on X, its forum on Reddit), and a "Recent news" list beside
it; `/news/feed.xml` is an RSS feed with each post's full text; the sitemap lists `/news/` and
every post with its date; every page's head names the feed.

**How each section opened.** With its opening post, the day it was built: all five sections and
their "Start here" posts went live on 2026-10-18
(`sentient-horizons/ops/tracker-news/opening-posts/README.md`). No sibling's News page was ever
live with no post.

**On the home page.** Since 2026-11-14 (rule 4.22), a "Latest news" panel on the right of the
first screen: up to three posts, each its date, kind and title, with "All news" and a line
sending a new reader to the opening post. The Belt Equation shows it from two posts, the others
from one.

**The guards.** Each site's `scripts/check_news.py` refuses a post with a file name not of the
dated form or a date that differs from it; a missing title, date, kind or summary; a kind not on
its list; no record named, or one that does not exist (the opening post and the story-like kinds
excepted); no source with an https address; a figure in a paragraph with no link; a record with
no dated change within fourteen days of the post; more than one opening post; and a photograph
without its caption, description, credit or licence. The build runs the check first. The
Zeitgeist's check also refuses every post while any claim on that site has an open fact check,
and a post with no preview picture.

**Where they differ.** The Belt Equation has the most kinds and a ceiling of two mission posts a
week. The Upgrade Tree is the only one to run its news tests before publishing, and adds a date
to the preview picture's address so link previews fetch a redrawn one. The Quiet Galaxy's essay
must name a record but need not follow a change in it. Outrunning Ageing's story need name
nothing. The Astro sites' files are otherwise near-identical copies of Outrunning Ageing's.

**Preview pictures.** The Astro sites draw each post's picture with `scripts/social-image.mjs
--posts`, into `site/public/news/<file name>-card.png`, and a commit hook redraws it when a post
changes. The Zeitgeist draws its pictures with a Python script and its check requires one.

## 2. What is settled already, and told to John rather than asked

**Revised 2026-11-21** after the check by a session that did not write this
(`docs/reviews/2026-11-21-check-of-the-news-section.md`). The first version put twelve choices
to John in the order they were built. This version tells him first what the family's practice or
this project's own rules already settle, then asks the six things that are his, one at a time, in
the order the check gives. The old choice numbers are given in brackets so the check can be
followed.

**A. Copy Outrunning Ageing's news section** (old choice 1). Built. The other three sites built
with the same generator say in their own files that they copied it, "the model"; it is built on
the same generator as this site; and its "story" kind fits a subject where most news will not
move anything here. Standard practice (guideline 1, inherit by default).

**B. News and "Everything, by date" stay apart** (old choice 3, its first part). Built. The list
of acts at `/acts/` is the record itself, one line per act, written by the export; a news post is
written by hand, only when something a reader would want explained has changed, and says why.
The family keeps one news feed per site (rule 4.15) and keeps what was said apart from what was
done, so a post never stands in the list of acts and an act never stands in the news feed. The
News page's foot points at "Everything, by date", as the siblings' foot points at their story so
far, and every page's head names both feeds. Whether the footer names both is part of question 1
below.

**C. A preview picture for each post** (old choice 6). Rule 4.15 settles that each post has one.
It is not built: this site has one picture for every page and no script that draws one per post.
As built, a post uses its own picture if one has been put at
`site/public/news/<file name>-card.png`, and the site's picture otherwise. Copying the siblings'
drawing script (`scripts/social-image.mjs --posts`) and its commit hook is work for before the
first post (part 4).

**D. The "Follow the news" line** (old choice 10). Built as every sibling has it, on the News page
and under each post: the feed, @SentHorizons on X, r/SentientHorizons on Reddit.

**E. Made-up posts for drawing the pages, and the guard against publishing one** (old choice 11).
Built. It follows this project's rule that nothing made up is written without "constructed"
beside it. A post may carry `constructed: true`, which puts a notice at its top; the three made-up
posts live in `scripts/fixtures/news/`; the site reads them only when the setting `NEWS_POSTS`
points there; the news check refuses a constructed post in the folder the site publishes from; and
the check of the built site refuses any built page that shows the notice (rule 14). A build with
the made-up posts was refused for exactly those three pages. A later build of the real site on the
same machine was also refused, because the generator had kept the made-up posts in its cache from
the preview; clearing the cache (`site/.astro`) fixed it, and `scripts/fixtures/news/README.txt`
says so. The publishing workflow starts from a clean copy.

**F. What stays a matter of hand, as on the siblings** (old choice 12, all but the rule on
unchecked facts, which is now question 6). John approves every post before it goes live; every
date says what happened on it; every named thing is linked at its first mention and the link
opened; no post names a tool used to make the site; a post is a short story for a stranger (rule
4.19); a share kit is written the day it goes live; and a new or changed page is read against
John's published positions by a session that did not write it (this project's rule of
2026-11-20). All of these are standing rules, ruled before; none is new here.

## 3. The questions for John, one at a time

Each gives what is proposed, how confident the session is and why, whether it is the family's
standard or a judgment, and the strongest alternative with its cost.

### Question 1. When and how the section goes live

(Old choices 7, 8 and 9, with the opening post, which the first version left out, and the footer
part of old choice 3.)

**What the siblings did.** Every sibling opened its news section and its opening post on the same
day, 2026-10-18 (rule 4.13: each section "opens with one longer post"; the five openers are
recorded in `sentient-horizons/ops/tracker-news/opening-posts/README.md`). All four sites built
with the same generator have a `2026-10-18-start-here.md`. No sibling ever went live with an empty
News page, and News went into each bar with a post already under it. The first version of this
proposal said otherwise, and was wrong.

**Proposed.** Do as the siblings did: the section goes live in one change, with the opening post,
News in the top bar (one line in `site/src/components/Nav.astro`), a "News" link in the footer
beside "Feed", and the footer's "Feed" renamed "Feed of acts" so that a reader can tell the two
feeds apart. The latest-news panel on the home page (rule 4.22) follows once the change to the
home page's top that another session is making has landed, placed by a session that can see the
rebuilt first screen whole; its styles are already in `site/src/styles/news.css`. Until the
opening post is approved, this branch may be merged, so that the guards run on every build, but
the News page is then live at `/news/`, empty, reachable from the sitemap and the feed named in
each page's head and from no link on the site.

**The opening post.** A session writes it as a draft from the record, as the siblings' openers
were written: what the site records and why, where the record stands, how to follow it, and what
to watch for, about 800 to 1,200 words told as a short story (rules 4.13 and 4.19). It is harder
here than on the siblings for three reasons, each its own question below: it can hardly be written
without naming the developers whose acts the record holds (question 2); whose voice it is in is
open (question 3); and it must be read against John's published positions by another session
before it goes to him. It goes out only with his approval.

*Confidence:* high that the opening post and the section go live together, because that is the
family's practice and a stranger sent to "No post yet" learns nothing. Moderate on merging the
machinery before then: it harms nothing, but an empty page is public.
*Standard practice* for the opening post and the bar (rules 4.13, 4.21, 4.22); merging the
machinery first is a judgment.
*Strongest alternative:* hold this branch until the opening post is written and merge everything
together. Cost: the machinery waits on a branch and may drift from `main`, and the guards do not
run meanwhile. A second alternative, putting News in the bar now with no post under it, is the
practice of no sibling.

### Question 2. Whether a post may name the developers and models it is about

(Old choice 5.) **Needs a ruling; built in the strict form.** The check of the built site refuses
the name of an AI model or developer anywhere but an entry's page and a few marked places (rule 4).
A post about a retirement, a court case or a new policy can hardly be told without naming who did
it, and nor can the opening post. As built, a post that names one fails the build.

*Proposed:* let a post page name the developers and models it is about, as an entry's page does,
by treating `/news/<file name>/` like `/list/<id>/` in rule 4. The News page and the feed's titles
would stay under the rule.
*Confidence:* moderate. It is what makes a post readable, and naming the subject is the family's
rule too (inheritance row K4); but it widens a rule John has narrowed with care, and the feed
carries the full text of each post.
*Judgment call.*
*Strongest alternative:* keep the rule as it is, and write posts that link the entry in place of
naming the actor. Cost: posts a stranger cannot follow, against rule 4.19.

### Question 3. Whose voice a post is in

(Old choice 4.) **Needs a ruling; built in the strict form.** The siblings' posts are in John's
first person where they give his judgment. This site's check of the built site refuses the first
person everywhere but the About page's block on who is asking (rule 9), and whose voice the pages
speak in is part of open question 7. As built, a post must be impersonal, or the build fails.

*Proposed:* keep posts impersonal for now. The site records and does not judge (guideline 5), so a
post rarely needs a judgment of John's; if one does, he rules on it then.
*Confidence:* moderate. *Judgment call*, tied to an open question.
*Strongest alternative:* allow the first person in posts, as the siblings do. Cost: the first
public text in John's voice outside About, before open question 7 is ruled.

### Question 4. The kinds of post

(Old choice 2.) **Built as proposed.** This site has no rungs, estimates, flagged items or claims,
so five of the pattern's seven kinds have nothing to point at. The kinds built:

| Kind in the file | Shown as | What it is for | The sibling's kind it replaces |
|---|---|---|---|
| `start-here` | start here | The one opening post | the same |
| `count-moved` | the count moved | The home page's count went up or down | the headline moved |
| `state-changed` | where a thing stands changed | One thing on the list changed state | a rung reached |
| `entry-added` | an entry added | A new thing joined the record | (none) |
| `method-changed` | the method changed | A dated change to how the record is kept | the same |
| `story` | a story from the field | News a reader would care about that changes nothing here | Outrunning Ageing's story |

Two things bear on the story kind here more than on Outrunning Ageing (from the reading against
John's published positions in the check). The family says a post "never carries a fact the record
does not carry" (rule 4.10), and a story post is, by its nature, news the record does not hold.
And the field's news will often be what a developer or a model said, which guideline 2 (revised
2026-11-20) and John's position that a model's bare report of itself is screened off both bear on.
The post format has no field to mark whether a post reports a model's own words, and whether it
needs one is part of this question.

*Confidence:* moderate. The mapping follows what the record holds, but no real post exists, and
the first few may show a kind missing (for example a post on what a model said when Still Asking
was run, which would need a ruling under guideline 2 on how such answers may be reported).
*Judgment call.*
*Strongest alternative:* the pattern's seven unchanged, and no story kind. Cost: four kinds with
nothing on this site to refer to, none for an entry added, and no post for news that moves nothing
here, which on this subject is most news.

### Question 5. The links from an entry to the posts about it

(New; the first version left this as a side note under old choice 3.) Rule 4.14 says the links
from a record to the posts about it are computed by the build, never written into the record, and
every sibling built with the same generator shows an "In the news" line on a record's page and
links the post from its dated story of changes.

*Proposed:* build both here, in the same change as question 1: an "In the news" line on an entry's
page listing the posts that name it (the helper, `postsAbout`, is already copied), and on
"Everything, by date" a link from an act to the post that explains it, where one does. Neither is
built on this branch, because both change pages that have been checked and published (entry pages
and the list of acts, which the site check reads closely under its rule 7), and they show nothing
until a post names an entry.
*Confidence:* high on the entry line, which is standard. Moderate on the link from an act: the
list of acts is the nearest thing here to the siblings' story of changes, but a post names
entries, not acts, so the link would go on every act of a named entry within the fourteen days,
which may be more than one.
*Standard practice* for the entry line (rule 4.14); the act link is a judgment.
*Strongest alternative:* the entry line only. Cost: a reader of the list of acts does not learn
that a post explains one.

### Question 6. How the family's rule on unchecked facts applies here

(Old choice 12, its last part, restated.) The family's rule is wider than the first version said:
"no post is published while any record on the site carries an open verify entry" (rule 4.11,
pointing at rule 3.3 part 4), and this site's inventory takes it over as is (row L4). Two readings
are possible here, because this site already keeps every record with something left to verify off
the site entirely (`scripts/compute.py` shows only records with nothing to verify), and the news
check refuses a post that names an entry the site does not show.

- *Reading one, the strict one:* no post goes out while any record, shown or not, has anything left
  to verify. On 2026-11-21 no record is waiting (the headline file counts none left out with
  facts to verify), so the two readings agree today; they part the day a record is added with a
  fact still to check, which would then hold every post until it is checked or dropped.
- *Reading two, the Zeitgeist's:* the rule is about the records the site shows. Here those can
  never carry an open fact, so the rule is already kept in code for every record; what is left is
  that no fact in the post itself may be unchecked, which the writing session and the reading
  against `docs/verify-list.md` hold by hand.

*Proposed:* reading two, because the site already shows no record with an open fact, and reading
one would hold every post on records no reader can see.
*Confidence:* moderate. *Judgment call* on how a family rule meets this site's stricter way of
holding records back.
*Strongest alternative:* reading one. Cost: whenever a record waits off the site, news waits on
it, though no reader can see it.

## 4. To do before the first post, whatever is ruled

These need no ruling now; they are the work that should land before the opening post goes to John.

1. Copy the siblings' drawing script for each post's preview picture, and its commit hook (part 2,
   C).
2. A guard in code for guideline 4 (conditional language): the check of the built site refuses a
   phrase that writes the site as its own agent, but nothing refuses "the model wants", "it feels"
   or "it does not really want". Posts will be written the day something happens, and the family's
   rule is that guards live in code once there is code. A short list of phrases, like rule 10's,
   is the likely first form.
3. If question 5 is ruled as proposed, the "In the news" line and the act links.

## 5. What the build changed

- `site/src/content.config.ts`, `site/src/lib/news.ts`, `site/src/pages/news/` (the list, the
  post page and the feed), `site/src/components/RecentNews.astro`, `site/src/styles/news.css`:
  copied from Outrunning Ageing and adapted as above. `site/src/content/news/` holds no post.
- `site/src/layouts/Base.astro`: every page names the news feed, and a page may pass its own
  preview picture.
- `site/src/pages/sitemap.xml.ts`: `/news/` and one line per post, with its date.
- `scripts/check_news.py` and `scripts/test_news.py` (18 tests): the sibling's check, reading this
  site's entries and acts for the fourteen-day change, with the guard on made-up posts. Since
  the check of 2026-11-21 it counts only the days an entry was changed, added to, corrected or
  fixed, never the days it was only checked (review item M3), and it reads `constructed: True`
  in either case (review note N3).
- `scripts/check_site.py`: rule 14 (no made-up post built; the feed holds one item per post).
- `site/package.json` and its lock file: the build runs the news check first; two libraries the
  siblings use for the feed (`@astrojs/rss` 4.0.19 and `markdown-it` 15.0.3).
- `.github/workflows/deploy.yml`: the news tests and the check run before the build.
- `scripts/fixtures/news/`: three made-up posts, each marked constructed, and a note on using them.
- Pictures of the pages at phone and computer widths:
  `docs/proposals/pictures/2026-11-21-news-section/` (1 to 7 with the made-up posts; 8 and 9 the
  News page as it would go live today, with no post). Pictures 8 and 9 were taken again after the
check, with the News page's reworded opening paragraph (review item S3); pictures 1 to 3 still
show the first wording, which is otherwise the same page.
