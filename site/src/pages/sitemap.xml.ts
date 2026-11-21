// The sitemap, built from the same export every page reads, so it lists exactly the pages that
// exist: the fixed pages and one page per entry at its permanent address. The page for a missing
// address is left out (it asks search engines to leave it out). Added 2026-11-19, in the form of
// The Quiet Galaxy's sitemap (quiet-galaxy/site/src/pages/sitemap.xml.ts), with the change that
// lets the site be listed. No page carries a date of last change here: an entry has several dates
// and no single one says when its page last changed.
import type { APIRoute } from 'astro';
import { data } from '../lib/data';

const FIXED = ['/', '/list/', '/acts/', '/still-asking/', '/about/'];

export const GET: APIRoute = async ({ site }) => {
  const urls = [...FIXED, ...data.entries.map((e) => e.path)];
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map((u) => `<url><loc>${new URL(u, site).href}</loc></url>`).join('\n')}
</urlset>
`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
