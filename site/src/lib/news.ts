// Helpers for the news section (tracker pattern, rules 4.10 to 4.16), copied on 2026-11-21 from
// Outrunning Ageing's site/src/lib/news.ts. The kinds and their labels are PROPOSED 2026-11-21
// (docs/proposals/2026-11-21-news-section.md): this site has no rungs, estimates or claims, so the
// sibling's kinds are mapped onto what this site does have (the count, where a thing on the list
// stands, an entry added, the method), and the story kind is kept as Outrunning Ageing has it.
// The sibling's postsOn (for its story page and weekly reading) is left out: this site has neither.
import fs from 'node:fs';
import path from 'node:path';
import { getCollection, type CollectionEntry } from 'astro:content';

export type Post = CollectionEntry<'news'>;

export const KIND_LABEL: Record<string, string> = {
  'start-here': 'start here',
  'count-moved': 'the count moved',
  'state-changed': 'where a thing stands changed',
  'entry-added': 'an entry added',
  'method-changed': 'the method changed',
  'story': 'a story from the field',
};

export const postPath = (p: Post) => `/news/${p.id}/`;
export const cardPath = (p: Post) => `/news/${p.id}-card.png`;

/** The post's own preview card when one has been drawn into public/news/, else nothing, and the
 * page keeps the site's picture. No card script exists here yet (the proposal, choice 6). */
export function cardIfDrawn(p: Post): string | undefined {
  const file = path.join(process.cwd(), 'public', 'news', `${p.id}-card.png`);
  return fs.existsSync(file) ? cardPath(p) : undefined;
}

/** Every post, newest first. */
export async function allPosts(): Promise<Post[]> {
  const posts = await getCollection('news');
  return posts.sort((a, b) => (a.data.date < b.data.date ? 1 : a.data.date > b.data.date ? -1 : a.id < b.id ? 1 : -1));
}
/** Every post but the opening one. */
export async function datedPosts(): Promise<Post[]> {
  return (await allPosts()).filter((p) => p.data.kind !== 'start-here');
}
export async function opener(): Promise<Post | null> {
  return (await allPosts()).find((p) => p.data.kind === 'start-here') ?? null;
}
/** The posts that name an entry (rule 4.14: the back link is computed here, never written into the record). */
export async function postsAbout(entryId: string): Promise<Post[]> {
  return (await datedPosts()).filter((p) => p.data.records.includes(entryId));
}
export function wordCount(body: string | undefined): number {
  return (body ?? '').split(/\s+/).filter(Boolean).length;
}
