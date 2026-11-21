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
  read?: 'full' | 'abstract' | 'part';
  says?: string;
  note?: string;
};
export type Item = { text: string; source: string };
// `none` is the sentence a caution prints when it holds nothing (scripts/export.py); the four
// kinds of evidence do not carry one.
export type Kind = { kind: string; heading: string; none?: string; items: Item[] };
export type Entry = {
  id: string;
  path: string;
  name: string;
  description: string;
  group: string;
  beside: boolean; // about the setting; shown beside the list and never counted
  placement_note: string | null; // what the placement rests on; shown after the reason for it
  limits: string[];
  test: string;
  settled_by: string;
  progress_kind: 'technical' | 'political' | 'cultural';
  added: string;
  first_pass: boolean;
  constructed: boolean;
  // What checks the record has had; null when it has had no second check.
  checks: { against_sources: string; changed?: string; changes_checked?: string; some_unchecked?: boolean; added_to?: string; additions_checked?: string; corrected?: string; corrections_checked?: string; fixed?: string; fixes_checked?: string } | null;
  state: { words: string; detail: string; offered_today: boolean | null; offered_by: { name: string; url: string | null }[]; set_on: string; source: string };
  evidence: Kind[];
  cautions: Kind[];
  history: { date: string; field: string; old: string; new: string; why: string }[];
  sources: Source[];
};
// The readings of the rebuilt home page, a draft (PROPOSED 2026-11-20,
// docs/proposals/2026-11-20-rebuild-design.md). Worked out by scripts/compute.py and read from
// the same headline file as the count. No published page reads them.
export type SourceRef = { key: string; label: string; publisher: string; url: string; opened: string };
export type Act = {
  id: string;
  entry: string;
  entry_name: string;
  date: string; // a day, a month or a year, as the source gives it
  actor: string;
  actor_kind: 'developer' | 'lawmaker' | 'court' | 'researchers';
  words: string;
  withdraws: boolean;
  about: string[]; // for an act by someone other than a developer: whose models it is about
  actor_url: string | null; // the public page of an actor that is not a developer
  source: SourceRef;
  read_on: string;
};
export type CellKind = 'offered' | 'unruled' | 'not_counted' | 'taken_back' | 'nothing_found' | 'not_searched';
export type Cell = { developer: string; kind: CellKind; date: string | null; words?: string };
export type MeasureReading = {
  entry: string;
  date: string;
  one_source: boolean;
  measures: { value: number; unit: string; words: string; entry: string; source: SourceRef; read_on: string }[];
};
export type Readings = {
  status: string;
  developers: {
    covered: string[];
    things: number;
    cells: number;
    offering: number;
    counts: Record<CellKind, number>;
    by_developer: ({ name: string; url: string | null } & Record<CellKind, number>)[];
    rows: { entry: string; name: string; cells: Cell[] }[];
  };
  law: {
    against: { entry: string; count: number; places: { name: string; date: string }[]; first: string | null; latest: string | null } | null;
    protecting: { entry: string; count: number; places: string[]; met: boolean; looked_on: string } | null;
  };
  public: MeasureReading | null;
  researchers: MeasureReading | null;
  latest: Act | null;
  acts: Act[];
};
export type Group = { name: string; meaning: string; beside: boolean; entries: string[] };
export type Window = {
  exported_on: string;
  commit: string | null;
  constructed: boolean;
  headline: {
    computed_on: string;
    last_read: string | null;
    // The count and its sentence. There is no total here: the count stands alone (ruled
    // 2026-11-18, docs/rulings/2026-11-18-home-page-count.md). How many things are on the list
    // is records.on_the_list, a plain fact about the records, never shown beside the count.
    headline: { count: number; words: string; offered_ids: string[] };
    records: { total: number; on_the_list: number; beside_the_list: number; first_pass: number; reviewed: number; left_out_unverified: number; constructed: boolean };
    readings?: Readings | null;
  };
  groups: Group[];
  entries: Entry[];
};

export const data = windowJson as Window;
export const headline = data.headline.headline;
export const readings = data.headline.readings ?? null;
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

// A count a reader meets in a sentence: a word up to twelve, a figure after that.
const COUNT_WORDS = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'];
export function countWord(n: number): string {
  return n >= 0 && n < COUNT_WORDS.length ? COUNT_WORDS[n] : String(n);
}

// A date placed at its first day, so that acts dated to a day, a month or a year can be put in
// order and given to a feed.
export function startOf(text: string): string {
  const [y, m = '01', d = '01'] = text.split('-');
  return `${y}-${m}-${d}`;
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
