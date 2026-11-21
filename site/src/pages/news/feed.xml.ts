// The news feed (tracker pattern, rule 4.15): RSS, full text, the post's card as its picture when
// one has been drawn. Copied on 2026-11-21 from Outrunning Ageing's site/src/pages/news/feed.xml.ts.
// It is a second feed beside the feed of acts (/acts.xml): that one lists every dated act as the
// record holds it, and this one carries only the posts that explain something
// (docs/proposals/2026-11-21-news-section.md, part 2, B).
import rss from '@astrojs/rss';
import MarkdownIt from 'markdown-it';
import type { APIContext } from 'astro';
import { allPosts, postPath, cardIfDrawn } from '../../lib/news';

const md = new MarkdownIt({ html: false, linkify: false });

export async function GET(context: APIContext) {
  const site = String(context.site).replace(/\/$/, '');
  const posts = await allPosts();
  return rss({
    title: 'Beyond the Window · News',
    description: 'What changed in the record, and why: one post for each change a reader would want explained.',
    site: context.site!,
    items: posts.map((p) => {
      const card = cardIfDrawn(p);
      return {
        title: p.data.title,
        pubDate: new Date(p.data.date + 'T12:00:00Z'),
        description: p.data.summary,
        link: postPath(p),
        content: md.render(p.body ?? ''),
        ...(card ? { enclosure: { url: site + card, type: 'image/png', length: 0 } } : {}),
      };
    }),
    customData: '<language>en-gb</language>',
  });
}
