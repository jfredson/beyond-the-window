# Hand-over note: the files that build the site and put it on Cloudflare

Written by Claude (Fable 5.2), an AI model, on 2026-11-19, as the writing session.

**This is the third version, all of the same day.** The first followed John's hosting ruling as
it then stood (the commit that added the deploy files, `024ac7d`). The second followed a
check by a different session (`docs/reviews/2026-11-19-check-of-deploy-files.md`) and John's
ruling on three points about the first release (the commit that revised the deploy files,
`136197f`). This one follows two more rulings by John:

- `docs/rulings/2026-11-19-repository-is-public.md`. John: "I see no reason to make any of
  this private. Let's follow the standard we have already set on the other sites". Decided by:
  John.
- `docs/rulings/2026-11-19-every-push-publishes.md`. Asked "Does every push publish the site,
  as on the sibling sites?", John: "Yes, like the siblings". Decided by: mixed.

His principle from the earlier ruling stands: "Copy them as much as possible since they seem to
be working fine. If there is a need to deviate, please explain why". The last section lists
what this version changed.

**Nothing is published.** No deploy was run, no secret or token was read or set, and nothing
was changed in Cloudflare or in the GitHub repository's settings. This session pushed nothing.

## What each file does

- **`.github/workflows/deploy.yml`** is the list of steps GitHub runs. It runs on every push to
  `main` that changes the records (`data/`), the scripts (`scripts/`), the site (`site/`) or
  the file itself, and it can also be started by hand. In order: it takes a copy of the
  repository, sets up Python 3.12 and Node 22, checks the records and the headline file
  (`scripts/compute.py --check`), runs the tests (`scripts/test_compute.py`), installs the
  site's packages and builds the site, checks the built pages against the rules of public text
  (`scripts/check_site.py`), hands the built pages to Cloudflare, and last tells the Sentient
  Horizons site to rebuild its Projects page. If a step fails, the steps after it do not run,
  so a push that fails a check publishes nothing.
- **`site/wrangler.jsonc`** tells Cloudflare what to serve and where: the built pages in
  `site/dist`, at beyondthewindow.org and www.beyondthewindow.org, with the site's own "not
  found" page (`dist/404.html`) for an address that has no page. There is no code in front of
  the pages.
- **`site/package.json` and `site/package-lock.json` were not changed.**

## When the site first goes public

A push publishes only once the two secret values are on the repository. Until they exist, a run
goes through every check and then fails at the deploy step, and nothing is published. So **the
first release is John setting the two values and giving his go.** The ruling records how the
master planning session applies that: once the values are set, it pushes nothing until John
has said go.

The first run that succeeds puts the pages on Cloudflare **and** points beyondthewindow.org and
www.beyondthewindow.org at them, in one step. Within a few minutes of a green tick, anyone who
types either address sees the site. John ruled on 2026-11-19 that one go covers both ("Yes, one
go"; `docs/rulings/2026-11-19-three-points-on-the-first-release.md`).

After that, every push to `main` that touches the records, the scripts or the site and passes
the checks goes live without anyone pressing anything.

## What is still different from the sibling sites

The five sibling sites compared are The Belt Equation, The Quiet Galaxy, The Upgrade Tree,
Outrunning Ageing and the AGI Zeitgeist. I read each one's workflow and settings file on this
Mac on 2026-11-19. The workflow here was fitted from The Quiet Galaxy's. The triggers, the
cancelling of an older run by a newer one, the deploy step (`cloudflare/wrangler-action@v3`,
left as all five have it), the two permissions on the key, the plain Cloudflare address being
on, and the step that tells Sentient Horizons to rebuild are now the same as theirs.

One difference is of substance:

1. **No small script in front of the pages.** The Quiet Galaxy, The Upgrade Tree and
   Outrunning Ageing each have one because each forwards a second domain. This site has no
   second domain. The settings here are the same shape as The Belt Equation's, which also
   lists its plain and `www` addresses with no script. One effect to know: on the three sites
   with a script, `www` is sent on to the plain address; here, as on The Belt Equation, `www`
   shows the same pages with no redirect.

Four are small, and each is here because this repository differs, not because the setup does:

2. **The deploy tool's version is named in the workflow** (wrangler 4.151.1). Three siblings
   list the tool in `site/package.json`, where the lock file fixes its version; the AGI
   Zeitgeist names "4" in its workflow, as this one names its version. I was asked to touch
   three files only, and another session is working in `site/`, so the package files are
   unchanged. The number is the one in The Quiet Galaxy's lock file, so both sites deploy with
   the same tool. To match the three siblings exactly, a later session adds the tool to
   `site/package.json` and removes this line.
3. **`CHANGELOG.md` is not among the paths that start a run.** It is on The Quiet Galaxy's
   list because that site's pages read it. Nothing in this site's build reads this
   repository's changelog, so a push that changes only the changelog would rebuild the same
   pages.
4. **There is no check of news posts.** The Quiet Galaxy has one. This project has no news
   posts and no such script. The other checks are this project's own scripts under their own
   names.
5. **The job is told it may only read the repository** (`permissions: contents: read`). No
   sibling's workflow says this. It changes nothing the steps do. The reason to keep it is
   that the repository is now public and one step is another party's code; the line means that
   step cannot write to the repository. It can be removed at no cost if John would rather the
   file matched line for line.

**Removed in this version** because the ruling leaves no reason for them: the rule that a run
does nothing from any branch but `main`, the second run waiting for the first, the plain
Cloudflare address being off, and `preview_urls` (no sibling sets it).

**A note on the plain Cloudflare address.** With `workers_dev` on, the site also answers at an
address ending in `workers.dev`, which Cloudflare forms from the name `beyondthewindow` and the
account's own name. It shows the same pages. The Belt Equation's settings file does not set
this either way; the others set it on, and this file follows them.

## What John does himself

Once, in this order. Nothing is published until both values are set and a run succeeds.

1. **Look at the records for the address.** In the Cloudflare dashboard, open
   beyondthewindow.org and its DNS records. Look for any record named `beyondthewindow.org` or
   `www`. A run on GitHub does not stop and does not ask: it **replaces** a clashing record for
   either of those two names, and takes the name away from any other Cloudflare site that
   holds it. So look first, to be sure nothing wanted is replaced without warning. Records for
   other names, mail records included, are not touched. (How this is known: the checking
   session read the deploy tool's own code at the version the workflow names. Cloudflare's
   page does not say.)
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
   **From the moment both are set, the next push that touches the records, the scripts or the
   site publishes the site.** So set them when the first release is wanted, not before.
5. **Give the go.** The first release is then either the next push, or a run started by hand:
   on github.com open the repository, the Actions tab, "Deploy site" in the list at the left,
   the "Run workflow" button at the right, leave the branch as `main`, and press the green "Run
   workflow". Started by hand, the run uses whichever branch is chosen there, so leave it as
   `main`. A run takes a minute or two.
6. **Look at both addresses in a browser afterwards.** The certificates can take a few minutes,
   so a warning in the first minutes is not a failure.

**Optional, later: the third value.** The last step tells the Sentient Horizons site to rebuild
its Projects page. It needs a repository secret named `CLOUDFLARE_DEPLOY_HOOK`, the same value
the sibling repositories hold. Without it the step prints a warning and the release is not
held up. This site is not on that page yet, so the value does nothing useful until John puts
it there.

**One thing never to do: do not connect this repository to the site inside Cloudflare.**
Cloudflare has its own way to build a site straight from a GitHub repository. Its page says a
connected repository will "automatically deploy your code every time you push a change". That
would publish every push **without running this project's checks**, which are what keep a
broken record or a rule-breaking page off the site. The connection is made in the dashboard
under Workers & Pages, the site's name, Settings, Builds, Connect, and only if a person presses
that. If it is ever found on, the same place has Disconnect.

## What the tick and the cross mean

A run now appears in the repository's Actions tab after every push that touches the records,
the scripts or the site.

- **A green tick:** every check passed and Cloudflare accepted the pages. The site shows the
  pushed version.
- **A red cross on an early step** (the record check, the tests, the build, the check of the
  built pages): nothing was sent to Cloudflare and the public site is exactly as it was before
  the push. The name of the failed step says which check stopped it.
- **A red cross on the step "Deploy to Cloudflare Workers":** this does **not** always mean
  nothing changed. If the key is missing or refused outright, nothing changed; that is what
  every run shows until the two values are set. But this step does several things in turn
  (sends the pages, then attaches the addresses), and if it fails partway, the new pages can be
  live under a red cross. After a red cross on this step, look at the site in a browser before
  assuming either way.
- **A yellow warning with a green tick:** the last step found no `CLOUDFLARE_DEPLOY_HOOK`
  value. The site was published; only the Sentient Horizons page was not told.
- **"Cancelled":** a newer push arrived while this run was going, and the newer run took over.
  The newer run publishes the newer pages, so look at that one.

## How to take the site down

Written from Cloudflare's own pages, opened on 2026-11-19 through a reading session that
reported what each page says. Where a page does not give a step, this says so. Cloudflare
calls the site a "Worker"; this one is named `beyondthewindow`.

**First, stop pushes putting it back.** Any later push that touches the records, the scripts or
the site would publish again and attach both addresses again. So before taking the site down,
delete the `CLOUDFLARE_API_TOKEN` value from the repository (the same place as step 4 above),
after which every run fails at the deploy step and publishes nothing. (From memory, not from
an opened page: GitHub also lets a workflow be switched off from the Actions tab.)

**To take the site off its addresses, keeping everything else.** The addresses are listed in
the dashboard under Workers & Pages, then `beyondthewindow`, then Settings, then Domains &
Routes. Cloudflare's page on custom domains gives that place for adding an address and for
deleting a route. It does **not** give click-by-click steps for removing an address, so the
exact button is not something I can quote: expect a remove or delete choice beside each of the
two addresses there. Remove both. The plain Cloudflare address is listed in the same place;
Cloudflare's page on it says to press "Disable" beside `workers.dev` there and confirm, and
that a later deploy turns it back on while the settings file says `workers_dev` is on. With
all three gone, nobody can reach the site. Two things the pages say or leave unsaid:

- The certificate is left behind: "When you delete a Custom Domain, the associated Advanced
  Certificate is not automatically deleted." It can be removed under SSL/TLS, then Edge
  Certificates. Leaving it does no harm.
- The page does not say whether the DNS record Cloudflare made for an address is removed with
  it. After removing the addresses, look at the DNS records for beyondthewindow.org and delete
  any left for the two names.

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
at the site afterwards. The next push replaces whatever a rollback put back. The surer way to
put back earlier pages is a push to `main` that undoes the fault.

## The trial run

Run again on 2026-11-19 for this version, on a fresh copy of the repository at the last commit
(`00d8ae4`, the ruling that every push publishes) with the two changed files added. The deploy
step and the step after it were not run.

| Step | Result |
|---|---|
| Check the records and the headline file | Passed: 13 records, the headline file matches |
| Tests | Passed: 28 tests |
| Install the site's packages (`npm ci`) | Passed |
| Build, with its own checks before and after | Passed: 18 pages |
| Check of the built site | Passed: 18 pages, 67 outside addresses linked |

The Python steps were run under Python 3.12, the workflow's version. Both files still read as
valid files of their kind. Read back by a program, the workflow starts on a push to `main`
touching `data/`, `scripts/`, `site/` or the workflow file, and by hand; a newer run cancels an
older one; and the step that tells Sentient Horizons to rebuild appears once and is the same,
character for character, as the first copy in The Quiet Galaxy's file.

What this trial did not cover:

- **The deploy step and the step after it.** Neither can be tried without the secret values.
- **The deploy tool's trial mode and Node 22.** I ran neither (this Mac has Node 26, and I was
  told to deploy nothing, which I read as covering `wrangler deploy` in any form). The
  checking session ran both on the first version and both passed. **Since then the settings
  file has changed in substance:** `workers_dev` is now on and `preview_urls` is gone. The
  trial mode is worth running again on this version.

When I started this version, the only uncommitted changes in the working copy were my own.

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
   changing all three, or the check will stop every push from publishing. The checking session
   found two more things here, set out in section 7 of its note: the two instructions work
   against each other, and the comment in `robots.txt` becomes a public file that says "Nothing
   is published yet".
2. **`README.md` is out of date.** Its status paragraph says there is no GitHub repository and
   no remote. The repository is now public, so that paragraph is public too.
3. **No page names its one real address.** The same pages will answer at three addresses (the
   plain one, `www`, and the one ending in `workers.dev`). A line in the head of `Base.astro`
   naming the page's address at beyondthewindow.org would tell search engines the other two
   are copies. It only matters once the site is listed.
4. **The public copy of the headline file** is served at `/data/headline.json`. That is by
   design (`scripts/export.py` writes it).

## For John's other repository, not this one

The Quiet Galaxy's `.github/workflows/deploy.yml` has its last step, the one that tells
Sentient Horizons to rebuild, written twice. It is harmless (the parent is told twice on every
release). I copied it here once and changed nothing there.

## Facts here that no opened page backs

- The path through GitHub's settings for adding or deleting a secret, and that a workflow can
  be switched off from the Actions tab.
- That the two permissions are enough to attach the two addresses on a first release. The
  siblings' workflows say their keys have those two.
- The exact button for removing an address from the site, and whether the dashboard can delete
  the site. Cloudflare's pages give neither.
- That Cloudflare's building from GitHub is off unless someone connects a repository. Its pages
  describe connecting as a step a person takes and do not say "off by default" in those words.
- The exact form of the address ending in `workers.dev`.

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
the check of the deploy files, and the rulings named above.

## What this version changed

1. **A run starts on every push to `main`** that touches the records, the scripts, the site or
   the workflow file, and can still be started by hand. Before, by hand only.
2. **A newer run cancels an older one** again, as on the siblings, since pushes now publish.
3. **The plain Cloudflare address is on,** with the sibling's comment, and `preview_urls` is
   removed because no sibling sets it.
4. **The step that tells Sentient Horizons to rebuild is copied in,** once, with its comment.
5. **The rule that only `main` is published from the button is removed,** as no sibling has it.
6. **The workflow is named "Deploy site"** again, as on the siblings.
7. **Everything that said a push never publishes, or that the repository is private, is
   gone** from the two files and from this note.
8. **Kept from the second version:** the correction that a clashing record is replaced without
   asking, the two-permission key, the take-down steps, what a tick and a cross mean, and the
   warning not to connect the repository inside Cloudflare. The take-down steps gained a first
   step (stop pushes putting the site back) and the plain Cloudflare address; the warning's
   reason changed, since a push now publishes anyway: the danger is publishing without the
   checks.

Decided by: agent, and not ruled by John: differences 2 to 5 above, and the name
`beyondthewindow` on Cloudflare, which follows the siblings' way of naming and is hard to
change after the first release.
