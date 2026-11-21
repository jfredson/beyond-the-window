// The news posts, copied on 2026-11-21 from Outrunning Ageing's (outrunning-ageing,
// site/src/content.config.ts, main branch), the model the other sibling sites copied: one Markdown
// file per event of note in site/src/content/news/YYYY-MM-DD-slug.md (the family's tracker pattern,
// rules 4.10 to 4.16, ruled by John 2026-10-18). Everything else the site shows comes from the
// records through scripts/export.py; a post explains a change the records already carry, or tells
// a story from the field (kind "story"), and scripts/check_news.py refuses a post that cannot be
// trusted. The kinds below are PROPOSED 2026-11-21 (docs/proposals/2026-11-21-news-section.md).
//
// Two things differ from the sibling. A post may carry `constructed: true`, for a made-up example
// used to draw the pages before any real post exists; scripts/check_news.py refuses such a post in
// the folder the site publishes from, and scripts/check_site.py refuses a built page that shows one.
// And the folder can be pointed elsewhere with NEWS_POSTS (for example scripts/fixtures/news), so
// that the pages can be photographed with made-up posts without any of them entering the site.
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

export const NEWS_KINDS = ['start-here', 'count-moved', 'state-changed', 'entry-added', 'method-changed', 'story'] as const;

// YAML reads a bare 2026-10-18 as a date; the site keeps dates as YYYY-MM-DD strings.
const isoDate = z.union([z.string().regex(/^\d{4}-\d{2}-\d{2}$/), z.date().transform((d) => d.toISOString().slice(0, 10))]);

const news = defineCollection({
  loader: glob({ pattern: '**/*.md', base: process.env.NEWS_POSTS || './src/content/news' }),
  schema: z.object({
    title: z.string(),
    date: isoDate,
    kind: z.enum(NEWS_KINDS),
    summary: z.string(),
    records: z.array(z.string()).default([]),
    sources: z.array(z.object({ label: z.string(), url: z.string().url() })).default([]),
    // The pictures the post shows (tracker pattern, rule 4.23): for each, its file in public/news/,
    // the page it came from, the credit, the licence with its link, and the day the licence was read
    // on that page. scripts/check_news.py refuses a picture in the body with no entry here.
    photos: z.array(z.object({ file: z.string(), source: z.string().url(), credit: z.string(), licence: z.string(), licence_url: z.string().url(), read_on: isoDate })).default([]),
    before: z.string().optional(),
    after: z.string().optional(),
    constructed: z.boolean().default(false),
  }),
});

export const collections = { news };
