# Check of the closer wording on the entry about checked self-reports

Written 2026-11-20 by Claude (Opus 5.5), an AI model, in a session started by the master
planning session. Earlier in this same session, running on Fable 5.2, I offered the wording
this commit puts in place. So here I am checking my own suggestion as another session carried
it out. The study is by Anthropic, which also makes the model writing this. Weigh what follows
with both in mind.

The commit checked is `308a237`, by the site-fixes session. It follows John's ruling of
2026-11-20, "Yes, closer wording"
(`docs/rulings/2026-11-20-reading-of-a-checked-report-is-attributed.md`, under "The wording,
ruled the same day"). I changed nothing and pushed nothing.

## Verdict

**Fit to publish.** The description ends in the wording I offered, word for word. Both
quotations are exact and come from one passage of the developer's page. The page's
description and link preview carry the text whole. The developer's name appears nowhere new.
One built page changed and no count moved.

## The points asked

- **Word for word.** As built, the description ends: "The developer whose researchers ran such
  a test says its research "provides evidence for some degree of introspective awareness" in
  its models, and stresses that the ability "is still highly unreliable and limited in scope".
  It says the results do not show whether any AI system might be conscious." That matches the
  wording I offered in `docs/reviews/2026-11-20-check-of-three-small-rewordings.md` and the
  wording in the ruling.
- **Both quotations exact, from one passage.** I opened the developer's page
  (`https://www.anthropic.com/research/introspection`) again. Near its head it says: "Our new
  research provides evidence for some degree of introspective awareness in our current Claude
  models, as well as a degree of control over their own internal states. We stress that this
  introspective capability is still highly unreliable and limited in scope". Both quoted
  phrases are in those two sentences, as written. The passage's mention of control is left
  out, which is the point of the change, because the entry tracks only the checked report.
- **Text for search engines and link previews.** The page's description and its link preview
  text both carry the full description, ending with the sentence on consciousness. Nothing is
  cut.
- **The developer's name.** The new words say "the developer" and name no one. They appear on
  the entry's own page and nowhere else in the built site. The built-site check passes.
- **Built pages and counts.** One built page differs: `/list/self-report-checked/`. No count
  moved: the count at the top is 5, with 24 dated acts. No changelog line was added, and none
  is owed for wording, by John's ruling of 2026-11-20.

## The positions read

Against the positions record's default-branch copy in the `sentient-horizons` repository, as
read earlier the same day: the sentence reports the developer's claim as the developer's and
states no position of John's, so it neither leans on his view of checked self-reports nor away
from it.

## The checks

Run on 2026-11-20 at this commit.

- `python3 -I scripts/test_compute.py`: "Ran 65 tests", "OK".
- `python3 -I scripts/compute.py --check`: "5 things past an AI model's ordinary limits are
  offered today by at least one AI developer", "24 dated acts", "The headline file matches the
  records."
- The site build: "19 page(s) built", "Complete!".
- `python3 -I scripts/check_site.py`: "The built site passes: 19 pages, 114 outside addresses
  linked."

The build rewrote one line of `site/src/data/window.json`, which I left out of this commit.

**Fit to publish: the description ends in the ruled wording word for word, both quotations are
exact and from one passage of the developer's page, and nothing else on the site changed.**
