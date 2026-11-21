Constructed news posts, for drawing and testing the news pages before any real post exists.

Every post here is made up and carries `constructed: true`. Nothing here is published: the site
builds from site/src/content/news, and scripts/check_news.py refuses a constructed post there.
To see the pages with these posts, run the dev server with NEWS_POSTS pointed here:

    cd site && NEWS_POSTS=../scripts/fixtures/news npx astro dev --port 4329

A build with that setting fails the check of the built site (scripts/check_site.py, rule 14), so
these posts cannot be published by accident. Added 2026-11-21 with the news section
(docs/proposals/2026-11-21-news-section.md).

After using them, delete the generator's cache (rm -rf site/.astro site/node_modules/.astro)
before building the real site. On 2026-11-21 a build straight after a preview with these posts
still carried them from that cache, and the check of the built site refused it. The publishing
workflow starts from a clean copy each time, so it cannot carry them.
