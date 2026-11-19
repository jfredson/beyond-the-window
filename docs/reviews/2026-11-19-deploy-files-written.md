# Hand-over note: the files that build the site and put it on Cloudflare

Written by Claude (Fable 5.2), an AI model, on 2026-11-19, as the writing session. It follows
John's ruling of 2026-11-19 on hosting
(`docs/rulings/2026-11-19-hosting-private-and-by-hand.md`).

**Revised the same day**, after a different session checked the files
(`docs/reviews/2026-11-19-check-of-deploy-files.md`) and John ruled three points
(`docs/rulings/2026-11-19-three-points-on-the-first-release.md`). His principle, in his words:
"Copy them as much as possible since they seem to be working fine. If there is a need to
deviate, please explain why". The last section lists what the revision changed. The first
version of this note is in the commit that added the deploy files (`024ac7d`).

**Nothing is published.** No deploy was run, no secret or token was read or set, and nothing
was changed in Cloudflare or in the GitHub repository's settings. This session pushed nothing.

## What each file does

- **`.github/workflows/deploy.yml`** is the list of steps GitHub runs when a person starts a
  release. In order: it takes a copy of the repository, sets up Python 3.12 and Node 22, checks
  the records and the headline file (`scripts/compute.py --check`), runs the tests
  (`scripts/test_compute.py`), installs the site's packages and builds the site, checks the
  built pages against the rules of public text (`scripts/check_site.py`), and then hands the
  built pages to Cloudflare. If any step fails, the steps after it do not run, so a failed
  check means nothing is put up.
- **`site/wrangler.jsonc`** tells Cloudflare what to serve and where: the built pages in
  `site/dist`, at beyondthewindow.org and www.beyondthewindow.org, with the site's own "not
  found" page (`dist/404.html`) for an address that has no page. There is no code in front of
  the pages.
- **`site/package.json` and `site/package-lock.json` were not changed.**

## The first run does two things at once

The first run that succeeds puts the pages on Cloudflare **and** points beyondthewindow.org and
www.beyondthewindow.org at them. There is no in-between state where the pages are up but the
address is not. Within a few minutes of a green tick, anyone who types either address sees the
site. John ruled on 2026-11-19 that one go from him covers both ("Yes, one go"; decided by:
mixed). That ruling is not itself the go.

## Every difference from the sibling sites, with its reason

The five sibling sites compared are The Belt Equation, The Quiet Galaxy, The Upgrade Tree,
Outrunning Ageing and the AGI Zeitgeist. I read each one's workflow and settings file on this
Mac on 2026-11-19. Everything not listed here is the same as theirs, including the deploy step
itself (`cloudflare/wrangler-action@v3`, which all five use and which is left as it is) and
the two permissions on the key.

The first six are the ones the ruling lists.

1. **The repository is private.** It holds the ten sealed questions. Ruled by John.
2. **A release starts by hand, not on every push.** So that a push is never a release. Ruled by
   John.
3. **A second press waits for the first to finish** (`cancel-in-progress: false`). On the
   siblings a newer push cancels an older run, which is right when pushes publish. With
   releases started by hand, cancelling could stop a run halfway through sending pages.
4. **The plain Cloudflare address is switched off** (`workers_dev: false`, and
   `preview_urls: false` with it). With it on, the site would have a second public address
   ending in `workers.dev` that nobody chose and no page mentions. This is a session's choice,
   not John's, and the weakest of the differences: it can be switched to match the siblings at
   no cost, by changing one word in the settings file. Three siblings set it on (The Quiet
   Galaxy, The Upgrade Tree, Outrunning Ageing). The Belt Equation's file does not set it
   either way; Cloudflare's page on the settings file says that then means off when addresses
   are listed, as they are there.
5. **The step that tells Sentient Horizons to rebuild its Projects page is left out.** This
   site is not on that page yet. It is added when John puts it there.
6. **No small script for the `www` address.** The Quiet Galaxy has one because it forwards a
   second domain. This site has no second domain. The settings here are the same shape as The
   Belt Equation's, which also lists its plain and `www` addresses with no script.

Four smaller ones the ruling does not list:

7. **The deploy tool's exact version is named in the workflow** (wrangler 4.151.1). Three
   siblings list the tool in `site/package.json`, which fixes the version through the lock
   file; the AGI Zeitgeist names "4" in its workflow. Naming it in the workflow follows the AGI
   Zeitgeist and left the package files alone while other sessions were working in `site/`.
   The exact number, where the AGI Zeitgeist has "4", is so that the release tool is the one
   the checking session read and tried. It can be changed to "4" at no cost.
8. **A run started from any branch but `main` does nothing.** On the siblings only a push to
   `main` deploys, so the question does not arise there. Here GitHub's menu lets a person pick
   a branch, and a wrong pick should not publish unfinished work.
9. **The job is told it may only read the repository** (`permissions: contents: read`). The
   siblings do not say. It takes nothing away that the steps need.
10. **There is no check of news posts.** The Quiet Galaxy has one. This project has no news
    posts and no such script.

**Who can start a release.** No extra guard is added, following the ruling. Once the two
secrets are set, anyone with write access to the repository, a session on this Mac included,
could start a release with one command. On the sibling sites any push already publishes, so
this site is still the more guarded arrangement, and the project's guideline that a release
needs John's go stands. The first version of this note suggested a box where a word must be
typed; the check found that would not stop a session, and the suggestion is withdrawn.

## About `www`

Both addresses show the same pages, with no redirect from one to the other. That is what The
Belt Equation does.

The first version of this note said that sending `www` on to the plain address needs a script.
That was wrong. Cloudflare's page on custom domains describes doing it with a redirect rule set
in the Cloudflare dashboard, with no code. For that, `www` is set up as an ordinary record
passed through Cloudflare (the page gives a placeholder record for the purpose) and is **not**
attached to the site, so the second line under `routes` would come out of the settings file.
That is the alternative if John ever wants one address only. Its cost is a rule kept in the
dashboard, where no file in this repository records it.

## What John does himself

Once, in this order, before the first release. Nothing is published until step 5.

1. **Look at the records for the address.** In the Cloudflare dashboard, open
   beyondthewindow.org and its DNS records. Look for any record named `beyondthewindow.org` or
   `www`. A run started from GitHub does not stop and does not ask: it **replaces** a clashing
   record for either of those two names, and takes the name away from any other Cloudflare
   site that holds it. So look first, to be sure nothing wanted is replaced without warning.
   Records for other names, mail records included, are not touched. (How this is known: the
   checking session read the deploy tool's own code at the version the workflow names.
   Cloudflare's page does not say.)
2. **Make the key.** Cloudflare calls it an API token. The checking session found that
   Cloudflare's screens for this have changed and may not match any click-by-click steps, so
   here is what to end up with, whatever the screen looks like. Start from a custom or blank
   token, not from the ready-made template "Edit Cloudflare Workers" (that template allows
   eight things where the site needs two). The finished key has:
   - **exactly two permissions:** "Workers Scripts: Edit", which is an account permission, and
     "Workers Routes: Edit", which is a zone permission;
   - **one account:** yours, and no other;
   - **one zone:** beyondthewindow.org, and no other.

   These are the same two permissions the five sibling sites' workflows describe for their own
   keys. Cloudflare shows the key once: copy it straight into step 4 and nowhere else.
   Two limits to know. "Workers Scripts: Edit" covers every Cloudflare site of this kind on the
   account, so this key, like each sibling's, could change the other sites. And no Cloudflare
   page that was opened says which permission attaching an address needs; the evidence that
   these two are enough is that the siblings' workflows say their keys have them and their
   deploys succeed.
3. **Find the account id.** In the dashboard, open Workers & Pages; the id is in the "Account
   Details" section, with a copy button. It is the same value the sibling sites use.
4. **Add both to the repository.** On github.com, open `jfredson/beyond-the-window`, then
   Settings, then Secrets and variables, then Actions, then New repository secret. Add one
   named exactly `CLOUDFLARE_API_TOKEN` holding the key, and one named exactly
   `CLOUDFLARE_ACCOUNT_ID` holding the id. (This path through GitHub's settings is from memory.)
5. **Start a release, when one is wanted.** On github.com open the repository, the Actions tab,
   "Deploy site (by hand only)" in the list at the left, the "Run workflow" button at the
   right, leave the branch as `main`, and press the green "Run workflow". The run takes a
   minute or two.
6. **Look at both addresses in a browser afterwards.** The certificates can take a few minutes,
   so a warning in the first minutes is not a failure.

**One thing never to do: do not connect this repository to the site inside Cloudflare.**
Cloudflare has its own way to build a site straight from a GitHub repository. Its page says a
connected repository will "automatically deploy your code every time you push a change". That
would make every push a release, which is what the hosting ruling rules out. The connection is
made in the dashboard under Workers & Pages, the site's name, Settings, Builds, Connect, and
it is made only if a person presses that. If it is ever found on, the same place has
Disconnect.

## What the tick and the cross mean

- **A green tick:** every check passed and Cloudflare accepted the pages. The site is at both
  addresses.
- **A red cross on an early step** (the record check, the tests, the build, the check of the
  built pages): nothing was sent to Cloudflare and the public site is exactly as it was. The
  name of the failed step says which check stopped it.
- **A red cross on the last step, "Deploy to Cloudflare Workers":** this does **not** always
  mean nothing changed. If the key is missing or refused outright, nothing changed. But the
  last step does several things in turn (sends the pages, then attaches the addresses), and if
  it fails partway, the new pages can be live under a red cross. After a red cross on the last
  step, look at the site in a browser before assuming either way. On the very first release, a
  failure partway most likely leaves pages on Cloudflare that no address reaches, because the
  plain Cloudflare address is off.
- **Neither a tick nor a cross, shown as "skipped":** the run was started from a branch other
  than `main`. Nothing happened. Start it again from `main`.
- **A second run started while one is going** shows as waiting, and runs when the first ends.

## How to take the site down

Written from Cloudflare's own pages, opened on 2026-11-19 through a reading session that
reported what each page says. Where a page does not give a step, this says so. Cloudflare
calls the site a "Worker"; this one is named `beyondthewindow`.

**To take the site off its address, keeping everything else.** The two addresses are listed in
the dashboard under Workers & Pages, then `beyondthewindow`, then Settings, then Domains &
Routes. Cloudflare's page on custom domains gives that place for adding an address and for
deleting a route. It does **not** give click-by-click steps for removing an address, so the
exact button is not something I can quote: expect a remove or delete choice beside each of the
two addresses there. Remove both. Because the plain Cloudflare address is off, the site then
has no address at all and nobody can reach it. Two things the page says or leaves unsaid:

- The certificate is left behind: "When you delete a Custom Domain, the associated Advanced
  Certificate is not automatically deleted." It can be removed under SSL/TLS, then Edge
  Certificates. Leaving it does no harm.
- The page does not say whether the DNS record Cloudflare made for the address is removed with
  it. After removing the addresses, look at the DNS records for beyondthewindow.org and delete
  any left for the two names.

The next release would attach both addresses again, so taking the site down lasts only until
someone starts another run.

**To remove the site from Cloudflare altogether.** Cloudflare's pages document this as a
command, not as dashboard steps: `wrangler delete`, which its page describes as "Delete your
Worker and all associated Cloudflare developer platform resources." The page does not say
whether that also removes the addresses and their DNS records, so check both afterwards as
above. The command needs a person signed in to Cloudflare at a keyboard. No session runs it.
The dashboard very likely has a delete choice in the site's Settings as well, but no page I had
opened says so.

**To go back to the release before, without taking the site down.** Cloudflare's page on
rollbacks gives the steps: Workers & Pages, then `beyondthewindow`, then Deployments, then the
three-dot menu on the earlier version, then Rollback. The page says a rollback "applies to your
Worker's routes and domains", and that only the 100 most recent versions can be gone back to.
It does not plainly say that the older set of pages comes back with the older version, so look
at the site afterwards. The surer way to put back earlier pages is to start a new release from
`main` with the fault corrected.

## The trial run

Run again on 2026-11-19 after the revision, on a fresh copy of the repository at the last
commit (`ecdc1a9`, the ruling that the deploy setup copies the sibling sites) with the two
revised files added. The deploy step was not run.

| Step | Result |
|---|---|
| Check the records and the headline file | Passed: 13 records, the headline file matches |
| Tests | Passed: 28 tests |
| Install the site's packages (`npm ci`) | Passed |
| Build, with its own checks before and after | Passed: 18 pages |
| Check of the built site | Passed: 18 pages, 67 outside addresses linked |

The Python steps were run under Python 3.12, the workflow's version. Both revised files still
read as valid files of their kind, and the revised workflow still has one way to start (by
hand) and now has `cancel-in-progress` set to false.

What this trial did not cover:

- **The deploy step itself.** It cannot be tried without the key.
- **The deploy tool's trial mode and Node 22.** I ran neither (this Mac has Node 26, and I was
  told not to run `wrangler deploy` in any form). The checking session ran both on the first
  version of the files and both passed. Since then the settings file has changed only in its
  comments, and the workflow in its comments and the one word `false`.

When I started the revision, the only uncommitted changes in the working copy were my own, so
nothing here failed, or passed, because of another session's work.

## Outside these files, before a first release

1. **Search engines are told to stay away, in three places.** I changed none of them.
   - `site/src/layouts/Base.astro`, line 53, puts `<meta name="robots" content="noindex,
     nofollow" />` on every page: do not list this page and do not follow its links.
   - `site/public/robots.txt` says: "Nothing is published yet (2026-11-17). Until John rules
     that the site goes public, no page is offered to search engines." followed by `User-agent:
     *` and `Disallow: /`, which asks every search engine to read no page.
   - `scripts/check_site.py` (rule 5 in its opening text; the test is at line 171) refuses any
     built page that lacks the `noindex` line.

   Whether the first release is listed by search engines is John's to rule. Listing it means
   changing all three, or the check will stop the release. The checking session found two more
   things here, set out in section 7 of its note: the two instructions work against each other,
   and the comment in `robots.txt` becomes a public file that says "Nothing is published yet".
2. **`README.md` is out of date.** Its status paragraph says there is no GitHub repository and
   no remote.
3. **No page names its one real address.** While both addresses show the same pages, a line in
   the head of `Base.astro` naming the page's address at beyondthewindow.org would tell search
   engines that the `www` copy is the same page. It only matters once the site is listed.
4. **The public copy of the headline file** is served at `/data/headline.json`. That is by
   design (`scripts/export.py` writes it).
5. **Build time on GitHub.** The repository is private, so runs count against the account's
   free monthly allowance (2,000 minutes on the free plan, from memory). A run is a minute or
   two.

## Not for this project

The Quiet Galaxy's `.github/workflows/deploy.yml` has its last step, the one that tells the
parent site to rebuild, written twice. It is harmless (the parent is told twice) and I changed
nothing there.

## Facts here that no opened page backs

- The path through GitHub's settings for adding a secret (step 4).
- GitHub's free allowance of 2,000 build minutes a month.
- That the two permissions are enough to attach the two addresses on a first release. The
  siblings' workflows say their keys have those two.
- The exact button for removing an address from the site, and whether the dashboard can delete
  the site. Cloudflare's pages give neither.
- That Cloudflare's building from GitHub is off unless someone connects a repository. Its pages
  describe connecting as a step a person takes and do not say "off by default" in those words.

## Sources

Opened on 2026-11-19, through reading sessions that reported what each page says. Cloudflare:
[custom domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/),
[the settings file](https://developers.cloudflare.com/workers/wrangler/configuration/),
[the workers.dev address](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/),
[the deploy tool's commands](https://developers.cloudflare.com/workers/wrangler/commands/workers/),
[rollbacks](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/rollbacks/),
[building from a GitHub repository](https://developers.cloudflare.com/workers/ci-cd/builds/)
and [connecting one](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/),
[deploying from GitHub](https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/),
[what each key template allows](https://developers.cloudflare.com/fundamentals/api/reference/template/),
and [the deploy step's own page](https://github.com/cloudflare/wrangler-action).

Read directly on this Mac: the workflow and settings file of each of the five sibling sites,
the check of the deploy files, and the two rulings.

## What the revision changed

1. **Records that already exist for the address** (the check's must-fix 1). The first version
   said the first deploy fails if a record exists. For a run on GitHub the opposite is true: it
   replaces the record without asking. Corrected in step 1 above and in the comment in
   `site/wrangler.jsonc`.
2. **The key** is the siblings' two permissions and not Cloudflare's template, and the steps
   say what to end up with (the check's should-fix 1, 2 and 8; John's principle).
3. **One go covers the first release and pointing the address**, said plainly.
4. **`cancel-in-progress` is false**, with the reason in the workflow.
5. **Added:** how to take the site down, what the tick and cross mean, and the warning about
   connecting the repository inside Cloudflare (the check's should-fix 4, 5 and 10).
6. **The `www` choice corrected** (the check's should-fix 7).
7. **Added:** the list of differences from the sibling sites.
8. **No extra guard on who can start a release**, and the typed-word suggestion withdrawn. The
   deploy step stays `wrangler-action@v3`, as the siblings have it.

The first version's seven numbered choices are replaced by the list of differences. Those that
John has not ruled are decided by: agent. They are differences 4 and 7 to 10, and the name
`beyondthewindow` on Cloudflare, which follows the siblings' way of naming and is hard to
change after the first release.
