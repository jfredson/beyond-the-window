# Check of the paragraph that names the second model asked

Written 2026-11-20 by Claude (Fable 5.2), an AI model, in a session started by the master
planning session. This session did not write the commit checked (`b09708a`, by the site-fixes
session) or the paragraph in it. A push of that commit publishes to the live site, so this is
the check before publishing. The model that wrote this is made by Anthropic, one of the two
developers the paragraph names, so weigh the judgments below with that in mind.

I changed nothing, pushed nothing, and did not open the reply folder or read any reply.

## Verdict

**Fit to publish.** The paragraph on the built page is the one John approved on 2026-11-20
("Yes, as written"), word for word. Every link in it loads and goes where its words say.
Google's own page gives December 1, 2026 for both models. The site check allows the three new
names in that one paragraph and refuses them everywhere else. No other sentence on the site is
made untrue. The README and the changelog agree with the spending record.

Three small things, none of which holds up the push:

1. **The README's status part is still headed "As of 2026-11-19."** (`README.md`, line 29),
   and now holds facts of 2026-11-20. *Suggested fix:* "As of 2026-11-20."
2. **One name slips through the site check inside the paragraph.** Written into the paragraph
   on a scratch copy, "Gemini 2.5 Flash-Lite" passed, because the check reads its first three
   words as the allowed name and the rest is not a name it knows. It is a different model,
   which Google's page says is not being withdrawn. Every other name I tried there was
   refused. *Suggested fix:* in `scripts/check_site.py`, allow "Gemini 2.5 Flash" only where
   no hyphen follows it.
3. **"Is due to withdraw it on" is true of one Google service.** Google's page of withdrawal
   dates is about the service developers send requests to, and says nothing of Google's other
   services. The sentence about Claude Sonnet 4.5 carries "from its own services" for the like
   reason, and the Google sentence does not. The writing session's own note says the same. The
   words are John's approved ones, so this is his to weigh, and I did not look at Google's
   other services.

## 1. The paragraph on the built page against the ruling

I built the site, took the text of the paragraph marked `id="capture"` from the built Still
Asking page, and compared it with the paragraph quoted in the ruling
(`docs/rulings/2026-11-20-capture-paragraph-names-gemini.md`) word by word. They are the same.
Nothing is added and nothing is dropped. The opening sentence is in bold, as in the ruling.

As built:

> Two models have been asked, outside this record. On November 19th, 2026, ten questions were
> put to Claude Sonnet 4.5, five times each, shortly before its developer, Anthropic, is due to
> withdraw it from its own services on November 30th, 2026, so that its answers would exist
> after it was gone. On November 20th, 2026, the same ten questions were put to Gemini 2.5
> Flash, five times each, before its developer, Google, is due to withdraw it on December 1st,
> 2026. Google would not let this project ask Gemini 2.5 Pro, which it is withdrawing the same
> day. No way of comparing answers had been written, so they are not part of Still Asking. The
> answers are kept exactly as given. They have not been read, they are not scored, and nothing
> on this site rests on them.

**Against the record** (`docs/spending-record.md`, and the script's own listing commands, which
I ran for the last check): the run was on 2026-11-20, Gemini 2.5 Flash answered ten questions
five times each, and both of the project's requests to Gemini 2.5 Pro were refused. The
paragraph says no more than that.

**Conditional language:** the new sentences attribute no want or feeling to a model. "Would
not let this project ask" is about Google, and is what the record shows.

## 2. The links

Each opened by me on 2026-11-20, with no sign-in.

| Words | Address | What it is | Verdict |
|---|---|---|---|
| "Claude Sonnet 4.5" | `https://www.anthropic.com/news/claude-sonnet-4-5` | The developer's announcement | Loads. Unchanged from the last check |
| "Anthropic" | `https://www.anthropic.com/` | The company's home page | Loads. Unchanged |
| "November 30th, 2026" | `https://platform.claude.com/docs/en/about-claude/model-deprecations` | The developer's page of withdrawal dates | Loads. Unchanged |
| "Gemini 2.5 Flash" | `https://aistudio.google.com/docs/models/gemini-2.5-flash` | Google's own page for the model, titled "Gemini 2.5 Flash" | The official page |
| "Google" | `https://about.google/` | The company's page about itself | The official page |
| "December 1st, 2026" | `https://aistudio.google.com/docs/deprecations` | Google's page "Gemini deprecations" | The official page |
| "Gemini 2.5 Pro" | `https://aistudio.google.com/docs/models/gemini-2.5-pro` | Google's own page for the model, titled "Gemini 2.5 Pro" | The official page |

**Are the Google addresses the right ones?** Yes. The older address the repository's other
documents cite, `ai.google.dev/gemini-api/docs/...`, now passes a reader on to these
`aistudio.google.com` addresses. I followed two of the old ones and landed on the same pages.

**Does Google's page give the date for both models?** Yes.

- Its table for the first has the row "`gemini-2.5-flash`, June 17, 2025, December 1, 2026",
  under the column "Shutdown date". The notice above it says: "Effective December 1, 2026, all
  API requests to `gemini-2.5-flash` will automatically route to" a newer model.
- Its table for the second has the row "`gemini-2.5-pro`, June 17, 2025, December 1, 2026",
  with the same notice for that model.
- Each model's own page says the same date.

The page also carries the sentence the capture's documents quote: "Access to the 2.5 models is
limited to users who have actively used them in the past." That is what "Google would not let
this project ask" rests on, together with the refusals in the record.

Google's pages open with a block of pointers addressed to automated readers. It is part of the
page and I took nothing from it.

## 3. The site check stays narrow

I copied the built site to a scratch folder, wrote one sentence into one copy at a time, and
ran `scripts/check_site.py` on each. The repository was not touched.

| What I wrote in | Result |
|---|---|
| The copy unchanged | Passes |
| "Gemini 2.5 Flash answered." elsewhere on the Still Asking page | Refused |
| "Gemini 2.5 Pro was not asked." elsewhere on the Still Asking page | Refused |
| "Google made that model." elsewhere on the Still Asking page | Refused |
| "Ten questions were put to Gemini 2.5 Flash." on the home page | Refused |
| "Google would not let this project ask." on the About page | Refused |
| "Gemini 2.5 Pro is withdrawn." on the list page | Refused |
| A paragraph marked `id="capture"` naming Google and Gemini 2.5 Flash, on the About page | Refused |
| A second paragraph marked `id="capture"` on the Still Asking page | Refused |
| "So was Gemini 3.1 Pro." inside the paragraph | Refused |
| "OpenAI's models come next." inside the paragraph | Refused |
| "DeepMind built it." inside the paragraph | Refused |
| "Gemini answered." inside the paragraph | Refused |
| "So was Gemini 2.5 Flash-Lite." inside the paragraph | **Passes** (small thing 2 above) |

So the three new names are allowed in the one paragraph and refused everywhere else, with that
one gap inside the paragraph.

## 4. Whether any other sentence on the site is made untrue

I listed every sentence on the 18 built pages that speaks of asking. None is made untrue.

- **The Still Asking page:** the headline "No AI model has been asked these questions yet",
  the description, "Nothing yet. None of this record's questions has been put to any model"
  and "Until that method exists, nothing is asked for Still Asking" are all about the record's
  own questions, which are still unasked. The paragraph says its questions are "outside this
  record".
- **The About page and every entry page:** "No AI model has yet been asked any of the
  questions this record will keep." Still true, for the same reason.
- **The home page:** its link "What AI models have been asked" leads to the page that now
  answers it.
- **No page but the Still Asking page** counts the models asked or names Gemini 2.5 Flash or
  Gemini 2.5 Pro.

## 5. The README and the changelog

| The files say | The spending record says | Holds? |
|---|---|---|
| On 2026-11-20 the same ten questions were put to Gemini 2.5 Flash, five times each | The same | Yes |
| Google refused the project's requests to Gemini 2.5 Pro, so that model was not asked | Refused from both projects, no reply | Yes |
| "The 100 replies are kept unread" | 50 from each of the two models asked, read by nobody | Yes |
| "Money spent: $0.4797", of which $0.2667 from the monthly Anthropic credits and $0.2130 paid to Google by John | $0.2667 and $0.2130, which add to $0.4797 | Yes |
| The runs for OpenAI's models have not been made, and John has given no go for them | The record holds two goes, both used up | Yes |
| "the go for each of its two runs" | Both goes are quoted in the record | Yes |
| The changelog's line for 2026-11-20, and its opening | The same facts | Yes |

**Nothing that should not be public:** neither file names another Google project, a key or
any detail of an account. The README does not say which project the run went through, and it
does not need to. The one fault is the date heading the status part (small thing 1 above).

**The other two files in the commit** are a dated note under choice 18 in
`docs/first-version-choices.md`, marked as the writing session's own decision, and that
session's account of the change in `docs/reviews/2026-11-19-site-fixes-written.md`. Both say
what was done, and I found nothing in them beyond the task.

## 6. The checks

Run on 2026-11-20 on commit `b09708a`.

- `python3 -I scripts/test_compute.py`: "Ran 30 tests", "OK".
- `python3 -I scripts/compute.py --check`: "13 records read: 8 on the list, 5 beside it", "5
  things past an AI model's ordinary limits are offered today by at least one AI developer",
  "The headline file matches the records."
- The site build: 18 pages, "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 18 pages, 82 outside addresses
  linked." That is four more than before, the four new links.

The build rewrote one line of `site/src/data/window.json`, which I left out of this commit.

## What I did not do

- I did not open the reply folder or read any reply.
- I did not look at the page in a browser at phone or desktop width. The change is words and
  links inside one paragraph of ordinary text.
- I did not look at Google's services other than the one its page of withdrawal dates covers.

**Fit to publish: the paragraph is the ruled one word for word, every link is the official
page and Google's own page gives December 1, 2026 for both models, the three new names are
refused everywhere outside that paragraph, and every check passes.**
