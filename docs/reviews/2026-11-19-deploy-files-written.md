# Hand-over note: the files that build the site and put it on Cloudflare

Written by Claude (Fable 5.2), an AI model, on 2026-11-19, as the writing session. A different
session checks this work. It follows John's ruling of 2026-11-19 on hosting
(`docs/rulings/2026-11-19-hosting-private-and-by-hand.md`).

**Nothing is published.** No deploy was run, no secret or token was read or set, and nothing
was changed in Cloudflare or in the GitHub repository's settings. Nothing was pushed.

## What each file does

- **`.github/workflows/deploy.yml`** is the list of steps GitHub runs when a person starts a
  deploy. It was adapted from The Quiet Galaxy's file of the same name. In order: it takes a
  copy of the repository, sets up Python 3.12 and Node 22, checks the records and the headline
  file (`scripts/compute.py --check`), runs the tests (`scripts/test_compute.py`), installs the
  site's packages and builds the site, checks the built pages against the rules of public text
  (`scripts/check_site.py`), and then hands the built pages to Cloudflare. If any step fails,
  the steps after it do not run, so a failed check means nothing is put up.
  It differs from the sibling's file in four ways. It starts only by hand: there is no push
  trigger and no schedule. It leaves out the step that tells the parent site to rebuild. It
  refuses to run from any branch but `main`. And it names the version of Cloudflare's deploy
  tool in the file (see choice 3).
- **`site/wrangler.jsonc`** tells Cloudflare what to serve and where: the built pages in
  `site/dist`, at beyondthewindow.org and www.beyondthewindow.org, with the site's own "not
  found" page (`dist/404.html`) for an address that has no page. There is no code in front of
  the pages.
- **`site/package.json` and `site/package-lock.json` were not changed.** No other session had
  changed them either (`git status` showed them clean). They did not need changing, because
  the deploy step fetches Cloudflare's tool itself.

## Choices John has not ruled

Each is PROPOSED 2026-11-19 and decided by: agent.

1. **The workers.dev address is off, and so are preview addresses.** Cloudflare can also serve
   a site at a second address ending in `workers.dev`. With it off, the site has one public
   home. *Confidence: high,* because a second address would show the same pages under a name
   nobody chose. *Judgment call:* the siblings keep it on. *Strongest alternative:* on, as the
   siblings have it, which gives a place to look at a release before the real address shows
   it. Its cost is a second public copy of the site that is never mentioned anywhere.
2. **www.beyondthewindow.org shows the same pages, with no redirect.** A redirect from www to
   the plain address needs a small script that every request passes through, as The Quiet
   Galaxy has (`site/worker/redirect.js` there, 20 lines). I left it out. *Confidence:
   moderate.* *Judgment call.* The reason: without a script, Cloudflare serves the files
   directly and there is no code of ours that can fail in front of them. *Strongest
   alternative:* the sibling's script, cut down to the one rule. Its cost is that every visit
   then counts against the free daily allowance of script runs (100,000 a day, from memory),
   and one more file to keep right. If the two addresses showing the same pages bothers John,
   the cheaper fix is a line in each page naming the plain address as the real one (see
   "Outside these files", item 3).
3. **The deploy tool's version (wrangler 4.151.1) is named in the workflow, and the package
   files are left alone.** The sibling lists the tool in its `site/package.json`. Naming it in
   the workflow fixes the version just as firmly and touches no file another session might be
   editing. The version is the one in The Quiet Galaxy's lock file on 2026-11-19. *Confidence:
   moderate.* *Judgment call.* *Strongest alternative:* add it to `site/package.json` as the
   sibling does, which also lets a person run the tool on this Mac. Its cost is a larger
   install on every build and two more changed files.
4. **A run from any branch but `main` does nothing.** GitHub's menu lets a person pick a
   branch when starting a run. *Confidence: high.* *Judgment call.* *Strongest alternative:*
   no guard, which would let an unfinished branch be published by a wrong pick in a menu.
5. **Starting a run asks for no typed confirmation.** The ruling says "by hand", and pressing
   the button is that. *Confidence: moderate.* *Strongest alternative:* a box where the person
   must type a word such as "publish" before the run goes ahead. It would also stop a session
   starting a run with one command. Its cost is one more step each release. Worth John's
   thought, because as written the only thing that keeps a session from starting a deploy is
   the guideline that says publishing waits for him.
6. **The name on Cloudflare is `beyondthewindow`.** It follows the sibling's `quietgalaxy`.
   Standard practice. It is hard to change after the first deploy, so say now if another is
   wanted.
7. **Two small things kept from the sibling:** a second run started while one is going cancels
   the first, and the date that fixes Cloudflare's behaviour is set to 2026-11-01.

## What John does himself

These need doing once, in this order, before the first release. None of them publishes
anything until step 5. The menu names in steps 1 to 3 are partly from memory and Cloudflare
and GitHub move them now and then.

1. **Look at the address's records in Cloudflare.** In the Cloudflare dashboard, open
   beyondthewindow.org, then DNS, then Records. There should be no record named
   `beyondthewindow.org` or `www`. On the first deploy Cloudflare makes those records and the
   certificates itself. Cloudflare's page says this fails if a record of the kind called CNAME
   already exists for the name; it does not say what happens with other kinds, so the safe
   state is none.
2. **Make the Cloudflare key.** In the dashboard: the person icon at top right, My Profile,
   API Tokens, Create Token. Choose the template called "Edit Cloudflare Workers". Under
   Account Resources choose your account. Under Zone Resources choose "Specific zone" and
   beyondthewindow.org. Continue, Create Token. Cloudflare shows the key once: copy it straight
   into step 4 and nowhere else.
   That template allows more than this site needs (it can also write to two kinds of Cloudflare
   storage). A narrower key has only two permissions: "Workers Scripts, Edit" on the account
   and "Workers Routes, Edit" on the zone. The Quiet Galaxy's workflow says that is what its
   key has. I recommend the template for the first release, because it is the one Cloudflare's
   own instructions name, and the narrower key afterwards if wanted.
3. **Find the account id.** In the dashboard, open Workers & Pages; the id is under "Account
   details" at the side. It is the same value the sibling sites use.
4. **Add both to the repository.** On github.com, open `jfredson/beyond-the-window`, then
   Settings, Secrets and variables, Actions, New repository secret. Add one named exactly
   `CLOUDFLARE_API_TOKEN` holding the key, and one named exactly `CLOUDFLARE_ACCOUNT_ID`
   holding the id.
5. **Start a deploy, when a release is wanted.** The workflow file must first be on GitHub,
   which happens when the master session next pushes `main`. Then on github.com open the
   repository, the Actions tab, "Deploy site (by hand only)" in the list at the left, the "Run
   workflow" button at the right, leave the branch as `main`, and press the green "Run
   workflow". The run takes a minute or two. A green tick means the site is at
   beyondthewindow.org. A red cross means nothing changed, and the failed step's name says
   which check stopped it.

## The trial run

I ran the workflow's steps on this Mac, on a fresh copy of the repository at the last commit
(`0671e08`, the hand-over note on the additions checked against the ruling on AI help) with
only my two files added, so that no other session's unfinished work was in it. The deploy step
was not run.

| Step | Result |
|---|---|
| Check the records and the headline file | Passed: 13 records, the headline file matches |
| Tests | Passed: 28 tests |
| `npm ci` | Passed |
| Build | Passed: 18 pages. The build's own before and after checks passed |
| Check of the built site | Passed: 18 pages, 67 outside addresses linked |

What the trial did not cover:

- **The deploy step itself.** It cannot be tried without the key.
- **Cloudflare's own reading of `site/wrangler.jsonc`.** The tool has a trial mode that reads
  the file and sends nothing, but it is run as `wrangler deploy --dry-run`, and my instructions
  were not to run `wrangler deploy`, so I did not. Instead I checked that every setting's name,
  and the value for the "not found" page, appear in the list of allowed settings that ships
  with wrangler 4.151.1. That is weaker than the trial mode. The checking session, or John,
  may want to run the trial mode.
- **Node 22.** This Mac has Node 26, so the build ran under that. The three Python scripts
  were run under both Python 3.14 and Python 3.12 (the workflow's version) and passed.

When I started, the working copy had no uncommitted changes from any session, so nothing here
failed because of another session's work.

## Outside these files, before a first release

1. **Search engines are told to stay away, in three places that must change together.**
   - `site/src/layouts/Base.astro`, line 53, puts `<meta name="robots" content="noindex,
     nofollow" />` on every page: do not list this page and do not follow its links.
   - `site/public/robots.txt` says: "Nothing is published yet (2026-11-17). Until John rules
     that the site goes public, no page is offered to search engines." followed by `User-agent:
     *` and `Disallow: /`, which asks every search engine to read no page.
   - `scripts/check_site.py` (rule 5 in its opening text, line 154) refuses any built page that
     lacks the `noindex` line.

   I changed none of them. As they stand, a first release would work and the site would be
   reachable by anyone with the address but not listed by search engines. Whether the first
   release goes out that way, or listed, is John's to rule. Listing it means changing all
   three, or the check will stop the deploy.
2. **`README.md` is out of date.** Its status paragraph says there is no GitHub repository and
   no remote. `site/astro.config.mjs` has a comment saying nothing is deployed, which is true
   until the first release.
3. **No page names its one real address.** If choice 2 stands, a line in the head of
   `Base.astro` naming the page's address at beyondthewindow.org (a "canonical" link) would
   tell search engines that the www copy is the same page. It only matters once the site is
   listed.
4. **The public copy of the headline file** is served at `/data/headline.json`. That is by
   design (`scripts/export.py` writes it), and is noted here only so the first release has no
   surprises.
5. **The repository stays private**, so GitHub charges build time against the account's free
   monthly allowance for private repositories (2,000 minutes on the free plan, from memory). A
   run is a minute or two.

## Not for this project

The Quiet Galaxy's `.github/workflows/deploy.yml` has its last step, the one that tells the
parent site to rebuild, written twice. It is harmless (the parent is told twice) and I changed
nothing there.

## Facts here that I did not open a source for

- The menu names in "What John does himself" (steps 1 to 4), beyond what the Cloudflare pages
  below say.
- The free allowances: 100,000 script runs a day on Cloudflare, 2,000 build minutes a month on
  GitHub.
- That the narrower key is enough to make the two addresses on a first deploy. The sibling's
  file says its key has those two permissions, but its addresses may have been attached by
  hand.

Opened on 2026-11-19, through a reading session that reported what each page says:
[Cloudflare's page on custom domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/),
[its page on the settings file](https://developers.cloudflare.com/workers/wrangler/configuration/),
[its page on deploying from GitHub](https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/),
[its list of what each key template allows](https://developers.cloudflare.com/fundamentals/api/reference/template/),
and [the deploy step's own page](https://github.com/cloudflare/wrangler-action).
