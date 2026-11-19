# Check of the files that build the site and put it on Cloudflare

Written by Claude (Fable 5.2), an AI model, on 2026-11-19, as the checking session. I wrote
none of the files checked. They are `.github/workflows/deploy.yml` (the list of steps GitHub
runs), `site/wrangler.jsonc` (the Cloudflare settings) and the writing session's hand-over note
(`docs/reviews/2026-11-19-deploy-files-written.md`), all from the commit that added the deploy
files (`024ac7d`). I changed none of them. I deployed nothing, signed in to nothing, read and
set no secret, and changed nothing in Cloudflare or in the GitHub repository's settings.
Nothing is published.

## The two answers

**Is it safe to push now? Yes.** Pushing these files to GitHub cannot make anything public.
The workflow has one way to start, a person starting it by hand, and until John has set the
two secrets a run started by hand fails at its last step.

**Is it safe to use for a first release, once John has set the two secrets? Yes, with one
correction to the instructions first** (must fix 1). The files themselves need no change to
work. John should also know three things before he presses the button, each explained below:

- The first run does two things at once. It puts the pages on Cloudflare and it points
  beyondthewindow.org and www.beyondthewindow.org at them. The ruling lists "pointing the
  address at the site" and "the first release" as two things that each wait for his go. With
  these settings they are one press of one button.
- The key he makes can change every site on his Cloudflare account, not only this one (should
  fix 1).
- Once the secrets are set, any working session on this Mac could start a release with one
  command. Only the project's guideline stops it (should fix 3).

## Must fix

1. **The note and the settings file say the wrong thing about records that already exist for
   the address.** Step 1 of "What John does himself" says the first deploy "fails" if a record
   already exists for the name, and the comment in `site/wrangler.jsonc` (lines 17 to 19) says
   the deploy "only works if no DNS record for either name exists already". For a run on
   GitHub the opposite is true. I read the code of the deploy tool at the version the workflow
   names (wrangler 4.151.1, the part that publishes addresses). When nobody is at a keyboard,
   as on GitHub, the tool does not ask and does not stop. It tells Cloudflare to replace a
   clashing record for the address, and to take the address away from any other Cloudflare
   Worker that holds it. Run by a person at a keyboard, the same tool asks first.
   So step 1 is still the right step, for a different reason: John looks at the records for
   beyondthewindow.org so that he knows nothing he wants is replaced without warning. The
   wording in both places should say that. Only records for the two names
   `beyondthewindow.org` and `www.beyondthewindow.org` can be replaced. Mail records and
   records for other names are not touched, and no other address is.
   *How I know:* the tool's own code, read on this Mac. Cloudflare's page on custom domains
   says only that an address cannot be attached where a record of the kind called CNAME
   exists, and does not say what the tool does about it.

## Should fix

1. **Start with the narrow key, not the template.** The note recommends Cloudflare's template
   "Edit Cloudflare Workers" for the first release and the narrow key afterwards. I would
   reverse that. Cloudflare's list of templates gives that template eight permissions: write
   access to Workers Scripts, to two kinds of storage (Workers KV and R2) and to Workers
   Routes, and read access to Workers Tail, Account Settings, User Details and User
   Memberships. The site needs two: "Workers Scripts, Edit" on the account and "Workers Routes,
   Edit" on the one zone beyondthewindow.org. Cloudflare's own page on deploying from GitHub
   says to cut the permissions down as far as possible. If the narrow key is refused, the run
   fails at the last step with nothing published, and the template is still there to fall back
   on.
   Two honest limits. First, no Cloudflare page I opened says which permission attaching an
   address needs. The evidence that the two are enough is The Quiet Galaxy: its workflow says
   its key has those two, its settings attach four addresses, and its last three runs (the
   latest on 2026-11-15) succeeded. I could not see that key, so this rests on that comment
   being right. Second, "Workers Scripts, Edit" covers every Worker on the account. Either
   key, stored on this repository, could overwrite or delete the sibling sites. I know of no
   way to limit a key to one Worker (from memory, not checked). That is the same risk each
   sibling repository already carries.
2. **The steps for making the key may not match the screen.** Cloudflare's page on creating a
   key still gives "My Profile", then "API Tokens", then "Create Token", as the note does, and
   confirms the key is shown only once. But Cloudflare's page on deploying from GitHub now
   describes a different screen: an "Account API tokens" page, and a "Permission policies"
   section with a "Custom" menu holding "Edit Cloudflare Workers". The note's words "Account
   Resources" and "Zone Resources" are on neither page. John should expect the labels to
   differ, and the note should say what to end up with (the two permissions, the one account,
   the one zone) so he can find his way on either screen. Steps 3, 4 and 5 match Cloudflare's
   and GitHub's pages as they stand.
3. **Who can start a release.** The note's choice 5 raises this and is right to. I can add two
   facts. GitHub's command-line tool on this Mac is signed in with write access to the
   repository (I used it, reading only, to check the repository is private). GitHub's page
   says anyone with write access can start the workflow, from the website, that tool or
   GitHub's programming interface. So once the secrets are set, one command from any session
   starts a release. And the note's suggested fix, a box where a word must be typed, would not
   stop a session, because the same command can supply the word. A real stop would be GitHub's
   feature that holds a run until a named person approves it; whether John's plan offers that
   on a private repository I did not check. This is John's to weigh, not a fault in the file.
4. **The note does not say how to take the site down.** A first release should come with the
   way back. In the Cloudflare dashboard that is removing the two addresses from the Worker
   named `beyondthewindow`, or deleting that Worker. A session should write those steps from
   Cloudflare's pages before the first release. I did not open a page for them.
5. **"A red cross means nothing changed" is true for the first release and not always after.**
   If a check fails, nothing changes. If the last step fails partway on a later release (the
   pages are sent, then attaching the addresses fails), the new pages can be live under a red
   cross. And a run started from a branch other than `main` shows neither a tick nor a cross:
   it shows as skipped. The note should say both.
6. **A second run cancels the first.** `cancel-in-progress: true` (line 31 of the workflow)
   was right for the sibling, where a newer push should replace an older one. For a release
   started by hand, a second press would stop the first run wherever it is, possibly in the
   middle of sending pages. `false` would make the second wait.
7. **The note is wrong that sending www to the plain address needs a script** (choice 2).
   Cloudflare's page on custom domains describes doing it with a redirect rule set in the
   dashboard, with no code. It needs www set up as an ordinary proxied record and not attached
   to the Worker, so the second route would come out of the settings file. The choice as made
   (both addresses show the same pages) works and is what the sibling does for its own www.
   The alternative put to John should be the dashboard rule, not the script.
8. **The workflow's opening comment undersells the template** (lines 12 to 14). It describes
   "Edit Cloudflare Workers" as two permissions. It has eight.
9. **The deploy step is a version behind Cloudflare's example.** The workflow uses
   `cloudflare/wrangler-action@v3`, as the sibling does. Cloudflare's page now shows `@v4`.
   Version 3 works today: the sibling's run on 2026-11-15 used it. This is the one step by
   another party that is handed the key, and `@v3` is a label its owner can move. Naming an
   exact commit of it would fix what runs. Low priority.
10. **Do not connect this repository to the Worker inside Cloudflare.** Cloudflare can also
    build a site straight from a GitHub repository on every push. That is a setting in
    Cloudflare, off unless someone turns it on, and I could not look. If it were turned on,
    a push would publish. The note should say so in a line.

## What I checked, in the order of the task

### 1. A push cannot publish

- The workflow's only trigger is `workflow_dispatch` (lines 22 and 23), which means "started
  by a person". There is no push, pull request, schedule or other trigger.
- It is the only workflow file. `.github/` holds nothing else.
- `site/package.json` has no deploy script, and nothing in it runs on install. Three packages
  the site depends on (esbuild, sharp, fsevents) run their own install steps; those fetch
  program files and deploy nothing. The deploy tool is not among the site's packages.
- The repository on GitHub is private, and GitHub Pages (GitHub's own site hosting) is not set
  up on it. Both read from GitHub on 2026-11-19, changing nothing.
- The deploy commit is not on GitHub yet. GitHub lists no workflows for the repository.
- GitHub's page says the "Run workflow" button appears only once the file is on the default
  branch, so a push is what makes a release possible. It does not start one.
- What I could not see: the Cloudflare account (should fix 10).

### 2. Every check runs before the deploy and stops it

The steps run in order and GitHub stops at the first that fails. Each check ends with a
failure signal when it finds a problem: I read the last lines of `scripts/compute.py`,
`scripts/export.py` and `scripts/check_site.py`, and `scripts/test_compute.py` uses Python's
standard test runner, which does the same.

| The Quiet Galaxy's step | Here |
|---|---|
| Check the records | `scripts/compute.py --check`, present |
| Run the tests | `scripts/test_compute.py`, present |
| Check the news posts | Not here. This project has no news posts and no such script. The note does not say so, and could in one line |
| Install and build | Present. Here the build also runs the record check before and the site check after |
| Check the built site | Present, run a second time after the build |
| Deploy | Present, with the tool's version named |
| Tell the parent site to rebuild | Left out, with the reason stated in the file |

I found no step that could pass when it should fail. Two things the checks do not cover, for
the record: nothing reads `robots.txt`, and nothing opens the 67 outside links.

The guard that only `main` is published (line 37) works: started from another branch or a tag,
the whole job is skipped.

### 3. The Cloudflare settings

Checked against Cloudflare's pages, opened on 2026-11-19 through reading sessions that
reported what each page says, with the sentences quoted.

| Setting | Finding |
|---|---|
| `name: beyondthewindow` | Allowed (letters, digits and dashes). No other project in `~/Code` uses it: the others are `quietgalaxy`, `beltequation`, `theupgradetree`, `outrunningageing`, `agi-zeitgeist`, `sentient-horizons`, `hearthandvoid`, `mvm`, `fredricksonstudios` and `john-andrew-fredrickson`. I could not look at the account itself for a Worker of that name made some other way |
| `assets.directory: ./dist` | Right. No code in front of the pages is allowed: Cloudflare's page says `main` is optional when a Worker only serves files. Cloudflare's page says requests for such files are free and unlimited |
| `not_found_handling: 404-page` | Right. Cloudflare serves the nearest `404.html` with the "not found" status. The build makes `dist/404.html` |
| Addresses ending in a slash | Cloudflare's default serves `/about/` from `about/index.html` and sends `/about` on to `/about/`, which matches how the site is built |
| The two routes | The form is the one Cloudflare's page gives. Cloudflare makes the records and certificates itself. Each address must be attached separately, which the file does |
| `www` | Shows the same pages as the plain address, with no redirect. See should fix 7 |
| `workers_dev: false` | No second public address ending in `workers.dev`. Cloudflare's page says this is already the default when routes are present; writing it out is harmless and clearer |
| `preview_urls: false` | No public address for each uploaded version. Confirmed as the setting's meaning |
| `compatibility_date: 2026-11-01` | Required by Cloudflare, and in the past |

**What a first deploy would do, in plain words.** It creates a Worker named `beyondthewindow`
on John's Cloudflare account and sends it the 22 built files. It creates the records and
certificates for beyondthewindow.org and www.beyondthewindow.org and points both at those
files. Within a few minutes anyone who types either address sees the site. There is no other
address for it.

**Can it touch John's other sites?** Not through these settings. The name clashes with none of
them, and the routes name only this address. The risk to the other sites is in the key, not the
settings (should fix 1).

### 4. The secrets

The workflow names `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`, and passes them only to
the deploy step (lines 67 and 68). No step prints them, and no step that runs the project's
own scripts or the site's packages is given them. The deploy step's own page says the key is
not printed in the run's record. The job's own access to the repository is read-only (lines 26
and 27). The permissions are in should fix 1: the template is more than the least that works.
I read no secret, and did not list their names on GitHub.

### 5. The steps written for John

Followed in my head as someone new to the tools:

- **Step 1** (look at the records): the right step with the wrong reason. Must fix 1.
- **Step 2** (make the key): should fix 1 and 2.
- **Step 3** (find the account id): matches Cloudflare's page, which says Workers & Pages,
  then the "Account Details" section, then the copy button beside "Account ID".
- **Step 4** (add both to the repository): the path through GitHub's settings is from the
  note's memory and I did not open a page for it. The two names match the workflow exactly.
- **Step 5** (start a deploy): matches GitHub's page step for step. Should fix 5 on what the
  tick and cross mean.
- **Missing:** how to take the site down (should fix 4); a line saying the first run makes the
  site public at both addresses at once; a line saying to look at both addresses in a browser
  afterwards, since the certificates can take a few minutes; and the warning in should fix 10.

### 6. The build and checks, run here

Run on 2026-11-19 on a fresh copy of the last commit at the time (`005dc05`, the ruling that
drops the two figures under the window drawing), outside the working folder, so no other
session's unfinished work was in it.

| Step | Result |
|---|---|
| Check the records and the headline file | Passed: 13 records, the headline file matches |
| Tests | Passed: 28 tests |
| Install the site's packages (`npm ci`) | Passed |
| Build, with its own checks before and after | Passed: 18 pages |
| Check of the built site | Passed: 18 pages, 67 outside addresses linked |
| The three Python scripts under Python 3.12, the workflow's version | Passed |
| The build again under Node 22, the workflow's version | Passed |
| The deploy tool's trial mode | Passed, see below |

**The trial mode.** I ran `wrangler deploy --dry-run` at version 4.151.1, which reads the
settings file and the built pages and sends nothing. It was run with no Cloudflare key in its
surroundings and with an empty folder as its home, so it had no sign-in to use even by
mistake. It did not ask for one. It reported: "Read 40 files from the assets directory" (22
files and 18 folders), "No bindings found", "--dry-run: exiting now", with no warning about
any setting. This shows the tool accepts the file. It does not test the key, the account, or
whether Cloudflare will attach the addresses: only a real deploy does.

One more check, by script: none of the 326 longer sentences in the file of sealed questions
(`docs/capture/questions.md`) appears in the built pages.

### 7. What else must change before a first release

What each says now, confirmed by opening it:

- `site/src/layouts/Base.astro`, line 53: `<meta name="robots" content="noindex, nofollow" />`
  on every page.
- `site/public/robots.txt`: two comment lines, "Nothing is published yet (2026-11-17). Until
  John rules that the site goes public, no page is offered to search engines.", then
  `User-agent: *` and `Disallow: /`.
- `scripts/check_site.py` refuses any built page without the `noindex` line (rule 5; the test
  is now at line 171, not 154 as the note says).

Two things the note does not say:

- **The two instructions work against each other.** Google's page on blocking pages from its
  listings says the `noindex` line only works if the page is not blocked by `robots.txt`,
  because a blocked page is never read. Google's page on `robots.txt` says a blocked address
  can still appear in results, without a description, if another site links to it. So as the
  files stand, the first release would be mostly unlisted but not reliably. If John rules the
  first release should stay out of search listings, the reliable form is to keep the `noindex`
  line and remove the `Disallow` line.
- **`robots.txt` is itself a public file.** After a release, anyone can read its comment at
  beyondthewindow.org/robots.txt. It would then say "Nothing is published yet" on a published
  site, and it names John. The comment should be rewritten or removed before the first release,
  whichever way he rules on listing.

## What I did not check

- The Cloudflare account: whether a Worker named `beyondthewindow` exists, what records the
  address has, and whether Cloudflare's own building from GitHub is turned on.
- The real deploy step, which cannot be tried without the key.
- Whether a key can be limited to one Worker, and whether GitHub's approval feature is
  available on a private repository on John's plan. Both are from memory.
- The steps for taking a site down.
- The path through GitHub's settings to add a secret.

## Sources

Opened on 2026-11-19 through reading sessions that reported what each page says. Cloudflare:
[custom domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/),
[the workers.dev address](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/),
[addresses for uploaded versions](https://developers.cloudflare.com/workers/versions-and-deployments/version-urls/),
[the settings file](https://developers.cloudflare.com/workers/wrangler/configuration/),
[pages built ahead of time](https://developers.cloudflare.com/workers/static-assets/routing/static-site-generation/),
[how addresses map to files](https://developers.cloudflare.com/workers/static-assets/routing/advanced/html-handling/),
[what serving files costs](https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/),
[deploying from GitHub](https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/),
[what each key template allows](https://developers.cloudflare.com/fundamentals/api/reference/template/),
[what each permission allows](https://developers.cloudflare.com/fundamentals/api/reference/permissions/),
[creating a key](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/),
[finding the account id](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/),
[the deploy command](https://developers.cloudflare.com/workers/wrangler/commands/workers/),
and [the deploy step's own page](https://github.com/cloudflare/wrangler-action). GitHub:
[starting a workflow by hand](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow)
and [what starts a workflow](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).
Google: [blocking a page from listings](https://developers.google.com/search/docs/crawling-indexing/block-indexing)
and [what robots.txt does](https://developers.google.com/search/docs/crawling-indexing/robots/intro).

Read directly on this Mac: the three files checked, the ruling, The Quiet Galaxy's workflow and
settings, the project's four scripts, and the deploy tool's code at version 4.151.1.
