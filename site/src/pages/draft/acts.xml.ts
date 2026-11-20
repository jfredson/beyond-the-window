// A feed of acts, newest first, for a reader who wants to be told when something changes
// (PROPOSED 2026-11-20, a draft with the rebuilt home page; the published site has no feed).
// Built from the same readings every draft page reads. An act dated to a month or a year is
// given the first day of it, because a feed needs a full date.
import type { APIRoute } from 'astro';
import { readings, startOf, SITE_NAME } from '../../lib/data';

const esc = (t: string) => t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

export const GET: APIRoute = async ({ site }) => {
  const acts = readings?.acts ?? [];
  const page = new URL('/draft/acts/', site).href;
  const self = new URL('/draft/acts.xml', site).href;
  const updated = acts.length ? `${startOf(acts[0].date)}T00:00:00Z` : '1970-01-01T00:00:00Z';
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
<title>${esc(SITE_NAME)}: every act, by date</title>
<subtitle>A dated record of how the world is treating AI models.</subtitle>
<id>${self}</id>
<link rel="self" href="${self}"/>
<link href="${page}"/>
<updated>${updated}</updated>
<author><name>John Andrew Fredrickson</name></author>
${acts.map((a) => `<entry>
<id>${page}#${a.id}</id>
<title>${esc(`${a.actor} ${a.words}`)}</title>
<link href="${page}#${a.id}"/>
<updated>${startOf(a.date)}T00:00:00Z</updated>
<summary>${esc(`${a.actor} ${a.words}. Source: ${a.source.label}. Entry: ${a.entry_name}.`)}</summary>
</entry>`).join('\n')}
</feed>
`;
  return new Response(xml, { headers: { 'Content-Type': 'application/atom+xml; charset=utf-8' } });
};
