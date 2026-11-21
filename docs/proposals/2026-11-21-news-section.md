# A news section for Beyond the Window

**PROPOSED 2026-11-21, not ruled.** Written by Claude (Opus 5.5) in a Claude Code session, on
branch `claude/news-section-79b5f4`, from John's request of 2026-11-21: "we need to create a news
section on the Beyond the Window site that mirrors the functionality of the other tracker
websites."

What is built on the branch: the post format, the News page, one page per post, the news feed,
the sitemap lines, the news check and its tests, and a guard that keeps made-up posts off the
site. What is not built, because it needs John's ruling: News in the top bar, the latest-news
panel on the home page, and the picture each post shows in a link preview. No real post is
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

## 2. The choices for John, in order

Each choice gives what is proposed, how confident the session is and why, whether it is the
family's standard or a judgment, and the strongest alternative with its cost.

### Choice 1. Copy Outrunning Ageing's news section

**Proposed and built.** Copy Outrunning Ageing's files (its main branch of 2026-11-21) and adapt
them: the post format, the helpers, the News page, the post page, the "Recent news" list, the
feed, the sitemap lines, the stylesheet's news part, and the check.

*Confidence:* high. The other three Astro sites copied it, so its files are the family's
standard in fact; it is built on the same generator as this site; and its "story" kind (a post
about the field that changes nothing on the site) suits a subject where most news will not move
the count.
*Standard practice* (guideline 1, inherit by default).
*Strongest alternative:* copy The Quiet Galaxy, the newest copy. It differs only in an "essay"
kind, which this site has no use for yet. Cost: none to speak of; the choice matters little.

### Choice 2. Six kinds of post, mapped onto what this site has

**Proposed and built.** This site has no rungs, estimates, flagged items or claims, so five of
the pattern's seven kinds have nothing to point at. The kinds built are:

| Kind in the file | Shown as | What it is for | The sibling's kind it replaces |
|---|---|---|---|
| `start-here` | start here | The one opening post | the same |
| `count-moved` | the count moved | The home page's count went up or down | the headline moved |
| `state-changed` | where a thing stands changed | One thing on the list changed state | a rung reached |
| `entry-added` | an entry added | A new thing joined the record | (none) |
| `method-changed` | the method changed | A dated change to how the record is kept | the same |
| `story` | a story from the field | News a reader would care about that changes nothing here | Outrunning Ageing's story |

*Confidence:* moderate. The mapping follows what the record holds, but no real post has been
written, and the first few may show a kind is missing (for example, a post about what a model
said when Still Asking was run, which would need John's ruling on how such answers may be
reported at all, under guideline 2).
*Judgment call.*
*Strongest alternative:* the pattern's seven unchanged. Cost: four kinds with nothing on this
site to refer to, and none for an entry added.

### Choice 3. News sits beside "Everything, by date", and does not replace it

**Proposed and built.** The site already lists every dated act at `/acts/` and in a feed of
acts (`/acts.xml`). That list is the record itself: one line per act, written by the export,
with no explanation. A news post is different: it is written by hand, only when something a
reader would want explained has changed, and it says why. So the two stay apart, each with its
own feed. The News page's foot points at "Everything, by date", as the siblings' foot points at
their story so far, and every page's head names both feeds.

*Confidence:* high that they should stay apart: the family keeps what was done and what was
said in separate records, and a feed that mixed generated lines with written posts would bury
the posts. Moderate on two feeds: a reader has to choose.
*Standard in form* (rule 4.15); the relation to a list of acts is this site's own.
*Strongest alternative:* one feed carrying both. Cost: a feed reader would show each act and its
post as two items about the same thing, and the acts would far outnumber the posts.

A side effect to know: a post about an act does not appear on "Everything, by date", and the act
does not link its post. The siblings compute such back links (rule 4.14, an "In the news" line on
a record's page). The helper for it (`postsAbout`) is copied; the line on entry pages is not
built, so as not to touch the entry pages before John has seen the section.

### Choice 4. Whose voice a post is in

**Needs a ruling; built in the strict form.** The sibling sites' posts are in John's first person
where they give his judgment ("my model puts the chance at 58 percent"). This site's check of the
built site refuses the first person everywhere but the About page's block on who is asking (rule
9 of `scripts/check_site.py`), and whose voice the pages speak in is part of open question 7. So
as built, a post must be written impersonally, or the build fails.

*Recommendation:* keep posts impersonal for now, because the site records and does not judge
(guideline 5), so a post rarely needs a judgment of John's. If a post does, John rules on it then.
*Confidence:* moderate. *Judgment call*, tied to an open question.
*Strongest alternative:* allow the first person in posts, as the siblings do. Cost: the first
public text in John's voice outside About, before open question 7 is ruled.

### Choice 5. Whether a post may name the developers and models it is about

**Needs a ruling; built in the strict form.** The check of the built site refuses the name of an
AI model or developer anywhere but an entry's page and a few marked places (rule 4). A post about
a retirement, a court case or a new policy can hardly be told without naming who did it. As
built, a post that names one fails the build.

*Recommendation:* let a post page name the developers and models it is about, as an entry's page
does, by treating `/news/<file name>/` like `/list/<id>/` in rule 4. The News page and the feed's
titles would stay under the rule.
*Confidence:* moderate. It is what makes a post readable, and naming the subject is the family's
rule too (inheritance row K4); but it widens a rule John has narrowed with care, and the feed
carries the full text of each post.
*Judgment call.*
*Strongest alternative:* keep the rule as it is and write posts that link the entry instead of
naming the actor. Cost: posts a stranger cannot follow, against rule 4.19's short story for a
reader who has never seen the site.

### Choice 6. A preview picture for each post

**Not built.** The siblings draw a picture per post for link previews. This site has one
picture, drawn by `scripts/preview_picture.sh`, and no drawing script for posts. As built, a post
page uses its own picture if one has been put at `site/public/news/<file name>-card.png`, and
the site's picture otherwise; the feed carries a picture only when one exists.

*Recommendation:* copy the siblings' drawing script and its commit hook before the first post
goes out, as its own piece of work.
*Confidence:* high that a post needs one: a shared link is how most readers meet a post.
*Standard practice* (rule 4.15).
*Strongest alternative:* the site's one picture for every post. Cost: every shared post looks
the same in a preview.

### Choice 7. News in the top bar and the footer

**Not built.** Rule 4.21 puts News in the bar, and this site's bar was set before there were any
news pages (`docs/first-version-choices.md`, choice 14). The change is one line in
`site/src/components/Nav.astro`, and a "News" link in the footer beside "Feed".

*Recommendation:* add both the day the first post (the opening post) is approved, not before,
so that a stranger is not sent to an empty page from every page of the site.
*Confidence:* moderate. *Standard in form; the timing is a judgment.*
*Strongest alternative:* add them now, as the siblings did on their first day. Cost: a link on
every page to "No post yet".

### Choice 8. The latest news on the home page

**Not built.** Rule 4.22 puts a "Latest news" panel on the right of the home page's first
screen, from the first dated post. This site's home page was rebuilt on 2026-11-20 and another
session is changing its top on 2026-11-21 (the founding question above the count), so this
session did not touch it.

*Recommendation:* add the panel once the first dated post is approved and the change to the
home page's top has landed, placed by a session that can see the rebuilt first screen whole.
The panel is copied from the siblings' home pages; its styles are already in
`site/src/styles/news.css`.
*Confidence:* moderate. The rebuilt first screen may have no right-hand column with room for it.
*Standard practice* (rule 4.22), with placement left open.
*Strongest alternative:* a short "Latest news" block below the first screen. Cost: a returning
reader sees nothing new without scrolling.

### Choice 9. Whether the empty News page may go live

**Needs a ruling.** If this branch is merged and pushed as it is, `/news/` is published with "No
post yet", reachable from the sitemap and the feed named in every page's head, and from no link
on the site.

*Recommendation:* merge it once checked, because the empty page harms nothing, the guards then
run on every build, and the first post becomes a small change.
*Confidence:* moderate. *Judgment call.*
*Strongest alternative:* hold the merge until the opening post is written. Cost: the machinery
waits on the branch and may drift from `main`.

### Choice 10. The "Follow the news" line

**Built as the siblings have it:** the feed, @SentHorizons on X, r/SentientHorizons on Reddit, on
the News page and under each post. This site's footer has no X link, though rule 4.15 asks for
one on every tracker (on the siblings' main branches no footer carries it either).

*Confidence:* high. *Standard practice.*
*Strongest alternative:* the feed only. Cost: posts are shared from those accounts, and a reader
who found one there has no way back.

### Choice 11. Made-up posts for drawing the pages, and the guard against publishing one

**Built; this site's own.** The siblings show a "stand-in" notice on a real placeholder post.
This site's guideline is that nothing made up is written without "constructed" beside it. So:
a post may carry `constructed: true`, which puts a notice at its top; the three made-up posts
live in `scripts/fixtures/news/`; the site reads them only when the setting `NEWS_POSTS` points
there; the news check refuses a constructed post in the folder the site publishes from; and the
check of the built site refuses any built page that shows the notice (rule 14). A build with the
made-up posts was tried on 2026-11-21 and refused for exactly those three pages. A later build of the
real site on the same machine was also refused, because the site generator had kept the made-up
posts in its cache from the preview; clearing the cache (`site/.astro`) fixed it, and the note in
`scripts/fixtures/news/README.txt` says so. The publishing workflow starts from a clean copy, so it
cannot carry them, and the check would refuse it if it did.

*Confidence:* high. *Judgment call*, following the project's own rule on constructed examples.
*Strongest alternative:* no made-up posts, and pictures only once a real post exists. Cost: the
post page cannot be seen or checked before the first real post.

### Choice 12. What stays a matter of hand, as on the siblings

Not built as code, and kept from the pattern as rules for whoever writes a post: John approves
every post before it goes live; every date says what happened on it; every named thing is
linked at its first mention and the link opened; no post names a tool used to make the site; a
post is a short story for a stranger (rule 4.19); a share kit is written the day it goes live.
Two of this site's own rules apply too: a new page is read against John's published positions by
a session that did not write it, and no post goes out while a fact in it is on
`docs/verify-list.md`. The Zeitgeist enforces the last in code; here it would need the verify
list in a form a script can read, which is a later step and John's call.

## 3. What the build changed

- `site/src/content.config.ts`, `site/src/lib/news.ts`, `site/src/pages/news/` (the list, the
  post page and the feed), `site/src/components/RecentNews.astro`, `site/src/styles/news.css`:
  copied from Outrunning Ageing and adapted as above. `site/src/content/news/` holds no post.
- `site/src/layouts/Base.astro`: every page names the news feed, and a page may pass its own
  preview picture.
- `site/src/pages/sitemap.xml.ts`: `/news/` and one line per post, with its date.
- `scripts/check_news.py` and `scripts/test_news.py` (16 tests): the sibling's check, reading this
  site's entries and acts for the fourteen-day change, with the guard on made-up posts.
- `scripts/check_site.py`: rule 14 (no made-up post built; the feed holds one item per post).
- `site/package.json` and its lock file: the build runs the news check first; two libraries the
  siblings use for the feed (`@astrojs/rss` 4.0.19 and `markdown-it` 15.0.3).
- `.github/workflows/deploy.yml`: the news tests and the check run before the build.
- `scripts/fixtures/news/`: three made-up posts, each marked constructed, and a note on using them.
- Pictures of the pages at phone and computer widths:
  `docs/proposals/pictures/2026-11-21-news-section/` (1 to 7 with the made-up posts; 8 and 9 the
  News page as it would go live today, with no post).
