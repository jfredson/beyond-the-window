// The sitemap, built from the same export every page reads, so it lists exactly the pages that
// exist: the fixed pages and one page per entry at its permanent address. The page for a missing
// address is left out (it asks search engines to leave it out). Added 2026-11-19, in the form of
// The Quiet Galaxy's sitemap (quiet-galaxy/site/src/pages/sitemap.xml.ts), with the change that
// lets the site be listed. No page carries a date of last change here: an entry has several dates
// and no single one says when its page last changed. On 2026-11-21 the news page and one page per
// news post were added, as on Outrunning Ageing; a post does carry its date as its last change.
import type { APIRoute } from 'astro';
import { data } from '../lib/data';
import { allPosts, postPath } from '../lib/news';

const FIXED = ['/', '/list/', '/acts/', '/still-asking/', '/about/', '/news/'];

export const GET: APIRoute = async ({ site }) => {
  const posts = await allPosts();
  const urls: { loc: string; lastmod?: string }[] = [
    ...FIXED.map((loc) => ({ loc })),
    ...data.entries.map((e) => ({ loc: e.path })),
    ...posts.map((p) => ({ loc: postPath(p), lastmod: p.data.date })),
  ];
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls
  .map((u) => `<url><loc>${new URL(u.loc, site).href}</loc>${u.lastmod ? `<lastmod>${u.lastmod}</lastmod>` : ''}</url>`)
  .join('\n')}
</urlset>
`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
