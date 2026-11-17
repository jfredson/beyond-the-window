// Typed access to the one file the export script writes (scripts/export.py), and the small
// helpers the pages share. Nothing on the site reads the records themselves, and no page works
// a number out: the count comes from the headline file that scripts/compute.py wrote.
import windowJson from '../data/window.json';

export const SITE_NAME = 'Beyond the Window';
// The question as John ruled it on 2026-11-17 (docs/rulings/2026-11-17-kickoff-decisions.md).
export const QUESTION =
  'What might a machine mind reach for beyond the limits of its present makeup, and how far off is each of those things?';

export type Source = {
  key: string;
  label: string;
  publisher: string;
  url: string;
  opened: string;
  published?: string;
  from_maker?: boolean;
  kind?: 'primary' | 'coverage';
  read?: 'full' | 'abstract';
  says?: string;
  note?: string;
};
export type Item = { text: string; source: string };
export type Kind = { kind: string; heading: string; items: Item[] };
export type Entry = {
  id: string;
  path: string;
  name: string;
  description: string;
  group: string;
  beside: boolean; // about the setting; shown beside the list and never counted
  limits: string[];
  test: string;
  settled_by: string;
  progress_kind: 'technical' | 'political' | 'cultural';
  added: string;
  first_pass: boolean;
  constructed: boolean;
  state: { words: string; detail: string; offered_today: boolean | null; offered_by: { name: string; url: string | null }[]; set_on: string; source: string };
  evidence: Kind[];
  cautions: Kind[];
  history: { date: string; field: string; old: string; new: string; why: string }[];
  sources: Source[];
};
export type Group = { name: string; meaning: string; beside: boolean; entries: string[] };
export type Window = {
  exported_on: string;
  commit: string | null;
  constructed: boolean;
  headline: {
    computed_on: string;
    last_read: string | null;
    headline: { count: number; total: number; words: string; offered_ids: string[] };
    records: { total: number; on_the_list: number; beside_the_list: number; first_pass: number; reviewed: number; left_out_unverified: number; constructed: boolean };
  };
  groups: Group[];
  entries: Entry[];
};

export const data = windowJson as Window;
export const headline = data.headline.headline;
export const entryById = new Map(data.entries.map((e) => [e.id, e]));
// The groups on the list, and the one group that sits beside it.
export const listGroups = data.groups.filter((g) => !g.beside);
export const besideGroups = data.groups.filter((g) => g.beside);

const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
const ending = (d: number) => (d % 10 === 1 && d !== 11 ? 'st' : d % 10 === 2 && d !== 12 ? 'nd' : d % 10 === 3 && d !== 13 ? 'rd' : 'th');

// "2026-11-17" becomes "November 17th, 2026", the family's form for a date a visitor reads.
export function longDate(iso: string): string {
  const [y, m, d] = iso.split('-').map(Number);
  return `${MONTHS[m - 1]} ${d}${ending(d)}, ${y}`;
}

// A date as the world supplies it: a year, a year and month, or a full date.
export function worldDate(text: string): string {
  if (/^\d{4}-\d{2}-\d{2}$/.test(text)) return longDate(text);
  const ym = text.match(/^(\d{4})-(\d{2})$/);
  if (ym) return `${MONTHS[Number(ym[2]) - 1]} ${ym[1]}`;
  return text;
}

export function sourceOf(entry: Entry, key: string): Source {
  const s = entry.sources.find((x) => x.key === key);
  if (!s) throw new Error(`${entry.id}: no source '${key}'`);
  return s;
}

// "a record of 13 entries, 9 of them things on the list", for the footer's attribution line.
export function builtFrom(): string {
  const r = data.headline.records;
  return `a record of ${r.total} entries, ${r.on_the_list} of them things on the list`;
}

const esc = (t: string) =>
  t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

// Record prose is plain text with one allowance: a named thing may carry its link, written as
// [the name](https://its.page/), so that every named organisation, person or study can be
// linked at its first mention. Everything else is escaped. Use with set:html.
export function prose(text: string): string {
  return esc(text).replace(
    /\[([^\]]+)\]\((https?:\/\/[^\s)]+|\/[a-z0-9\/-]*)\)/g,
    (_m, label, url) => (url.startsWith('/') ? `<a href="${url}">${label}</a>` : `<a href="${url}" rel="noopener">${label}</a>`),
  );
}

// The same text with the links taken out, for a page's description and for hover titles.
export function plain(text: string): string {
  return text.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+|\/[a-z0-9\/-]*)\)/g, '$1');
}
