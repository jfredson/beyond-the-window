# Hand-over note: the files that build the site and put it on Cloudflare

Written by Claude (Fable 5.2), an AI model, on 2026-11-19, as the writing session. Fourth
version; the last section says what each version changed.

**In three lines.** The files that publish the site are written and twice checked by a
different session. Nothing is published, and nothing can be until John does the four steps
below. After that, every change pushed to GitHub that passes the project's checks goes live at
beyondthewindow.org, as on the sibling sites.

## What John does himself

Four steps, in this order. Steps 1 to 3 publish nothing. The site goes public at step 4.

1. **Look at the records for beyondthewindow.org.** In the Cloudflare dashboard, open
   beyondthewindow.org and its DNS records (the list of where each name under the address
   points). Look for any record named `beyondthewindow.org` or `www`. The first release
   **replaces** a record for either of those two names without asking, and takes the name away
   from any other Cloudflare site that holds it. So look first, to be sure nothing wanted is
   replaced. If there is no such record, there is nothing to do. Records for other names, mail
   records included, are not touched.

2. **Make the key.** Cloudflare calls it an API token; it is made in the dashboard under your
   profile. Cloudflare's screens for this have changed more than once, so here is what to end
   up with, whatever the screen looks like. Start from a custom or blank token ("from
   scratch"), not from the ready-made template "Edit Cloudflare Workers", which allows eight
   things where the site needs two. The finished key has:
   - **exactly two permissions:** "Workers Scripts: Edit", which is an account permission, and
     "Workers Routes: Edit", which is a zone permission. The screen may say "Write" where this
     says "Edit"; Cloudflare's own list uses both words for the same thing;
   - **one account:** yours, and no other;
   - **one zone:** beyondthewindow.org, and no other.

   These are the same two permissions the five sibling sites' workflows describe for their own
   keys. Cloudflare shows the key once. Copy it straight into step 3 and nowhere else.

3. **Add two secret values to the repository.** On github.com, open
   `jfredson/beyond-the-window`, then Settings, then Secrets and variables, then Actions, then
   "New repository secret", and after filling it in, "Add secret". Do this twice:
   - one named exactly `CLOUDFLARE_API_TOKEN`, holding the key from step 2;
   - one named exactly `CLOUDFLARE_ACCOUNT_ID`, holding your Cloudflare account id. The id is
     in the Cloudflare dashboard under Workers & Pages, in the "Account Details" section, with
     a copy button. It is the same value the sibling repositories hold.

   **From the moment both are set, the next push that touches the records, the scripts or the
   site publishes the site.** So do this step when the first release is wanted, not before.
   The master planning session pushes nothing between this step and your go.

4. **Tell the master session to go.** It then pushes, and the push starts the release. Nothing
   more is needed from you. (The release can also be started by hand: on github.com open the
   repository, the Actions tab, "Deploy site" in the list at the left, the "Run workflow"
   button at the right, leave the branch as `main`, press the green "Run workflow".)

### What you will see when it works

- On github.com, in the repository's Actions tab, a run named "Deploy site" goes from a
  yellow dot to a **green tick** in a minute or two.
- The run carries one **yellow warning**, saying the Sentient Horizons site was not told to
  rebuild its Projects page. That is expected and harmless: this site is not on that page yet.
- Within a few minutes, beyondthewindow.org and www.beyondthewindow.org both show the site.
  The certificates can take a few minutes, so a security warning in the browser during the
  first minutes is not a failure. Look at both addresses.
- From then on, a new run appears after every push that touches the records, the scripts or
  the site, and each green tick means the public site shows that push.

### What to do if it does not work

- **A red cross on an early step** (the record check, the tests, the build, or the check of
  the built pages). Nothing was sent to Cloudflare and nothing is public. The failed step's
  name says which check stopped it. Tell the master session; a session corrects the fault and
  pushes again.
- **A red cross on the step "Deploy to Cloudflare Workers", with a message about the key or
  about not being allowed.** The likeliest causes are a secret's name not typed exactly, the
  key pasted with something missing, or the key made for the wrong account or zone. Check the
  two names in step 3, and if they are right, make a new key (step 2) and replace the value.
  Then tell the master session to go again.
- **A red cross on that step, with a message about a domain or a route.** This is the one
  case where the site can already be public under a red cross. The deploy sends the pages and
  turns on the plain Cloudflare address (the one ending in `workers.dev`) at the same time as
  it attaches the two addresses, so if only the attaching fails, the pages are up at the plain
  Cloudflare address and not at beyondthewindow.org. It may mean the two permissions are not
  enough to attach an address for the first time. Nobody has been able to confirm that they
  are: on the sibling sites the addresses were first attached by hand in the dashboard, and
  the deploys since have only kept them in place. The way out is the siblings' own way. Attach
  the two addresses by hand, as Cloudflare's page on custom domains gives it: in the Cloudflare
  dashboard go to Workers & Pages; in Overview, select `beyondthewindow`; go to Settings, then
  Domains & Routes, then Add, then Custom Domain; enter `beyondthewindow.org`; select "Add
  Custom Domain". Do the same again for `www.beyondthewindow.org`. Later runs then only keep
  them in place, as on the siblings.
- **A red cross and you are not sure what is public.** Look at beyondthewindow.org in a
  browser. If the site should not be up, the take-down steps are further down this note.

### Three standing cautions

- **Do not connect this repository to the site inside Cloudflare.** Cloudflare has its own way
  to build a site straight from a GitHub repository. Its page says a connected repository will
  "automatically deploy your code every time you push a change". That would publish every push
  **without running this project's checks**, which are what keep a broken record or a
  rule-breaking page off the site. The connection is made in the dashboard under Workers &
  Pages, the site's name, Settings, Builds, Connect, and only if a person presses that. If it
  is ever found on, the same place has Disconnect.
- **Read a stranger's proposed change before accepting it.** The repository is public, so
  anyone can propose a change (GitHub calls it a pull request). A proposed change cannot
  publish anything and cannot reach the key. But once you accept one, it is a push to `main`:
  the checks run, and the result is published with the key. So before accepting a stranger's
  change that touches `.github/`, `scripts/` or the site's package files
  (`site/package.json`, `site/package-lock.json`), read it, because a change there could
  weaken a check or misuse the key at that moment.
- **The key can change the sibling sites too.** "Workers Scripts: Edit" covers every
  Cloudflare site of this kind on the account. That is the same for each sibling's key.

### Optional, later: the third value

The last step of each run tells the Sentient Horizons site to rebuild its Projects page. It
needs a repository secret named `CLOUDFLARE_DEPLOY_HOOK`, the same value the sibling
repositories hold. Without it the step prints the yellow warning and the release is not held
up. The value does nothing useful until this site is on that page.

## How to take the site down

Written from Cloudflare's and GitHub's own pages, opened on 2026-11-19 through reading sessions
that reported what each page says. Where a page does not give a step, this says so. Cloudflare
calls the site a "Worker"; this one is named `beyondthewindow`.

**How many addresses the site has.** Not only two. Once released, the same pages answer at:

- beyondthewindow.org and www.beyondthewindow.org;
- the plain Cloudflare address, which Cloudflare's page gives as the Worker's name, then the
  account's own name, then `.workers.dev`;
- **one more address for every release.** Cloudflare gives each uploaded version of the site
  its own address (it calls these Version URLs): a short code, then `-beyondthewindow.`, then
  the account's name, then `.workers.dev`. Cloudflare's page says: "If Version URLs are
  enabled, the URL is public and available after version creation." They are hard to guess but
  they are public, and an old one goes on showing the old version of the pages. The sibling
  sites have these too.

Taking the site down means closing all of these. In order:

1. **Stop pushes putting it back.** Any later push that touches the records, the scripts or
   the site would publish again. Switch the workflow off: on github.com open the repository,
   the Actions tab, "Deploy site" at the left, the button "Show workflow options", then
   "Disable workflow". GitHub's page says this does not stop a run already going, so let any
   such run finish first, or cancel it from its own page. (Deleting the
   `CLOUDFLARE_API_TOKEN` value from the repository has the same effect, since every run then
   fails at the deploy step. GitHub's pages do not give steps for deleting a secret; the
   choice is beside the secret's name where it was added.)
2. **Remove the two addresses.** In the Cloudflare dashboard: Workers & Pages, then
   `beyondthewindow`, then Settings, then Domains & Routes. Cloudflare's page on custom
   domains gives that place for adding an address and for deleting a route. It does **not**
   give click-by-click steps for removing an address, so the exact button is not something I
   can quote: expect a remove or delete choice beside each of the two addresses. Remove both.
3. **Switch off the plain Cloudflare address.** In the same place, Cloudflare's page says to
   click "Disable" on `workers.dev` and confirm.
4. **Switch off the addresses of the uploaded versions.** In the same place, Cloudflare's page
   says to find "Version URLs" and select "Disable". Its page on the plain address says in so
   many words that step 3 does not do this: "Disabling your `workers.dev` route does not
   disable Version URLs, Preview URLs, or Deployment URLs." And its page on version addresses
   says: "Disabling Version URLs disables routing to Version URLs and aliased Version URLs."
   It does not say in so many words that addresses already given out stop working, so try one
   afterwards if one is known.

With all four done, nobody can reach the site. Three things to know:

- **Steps 3 and 4 do not survive the next release.** The settings file says the plain
  Cloudflare address is on, and Cloudflare's page says a later deploy then turns it back on.
  For the version addresses the page says only that, where the settings file does not mention
  them, a deploy "does not change an existing Version URL setting", which suggests they would
  stay off; it is not certain. This is why step 1 comes first. If the site is to stay down
  while releases go on to some other end, a session changes the settings file to say both are
  off.
- **The certificate is left behind.** Cloudflare's page: "When you delete a Custom Domain, the
  associated Advanced Certificate is not automatically deleted." It can be removed under
  SSL/TLS, then Edge Certificates. Leaving it does no harm.
- **The DNS records may be left behind.** The page does not say whether the record Cloudflare
  made for an address is removed with it. Afterwards, look at the DNS records for
  beyondthewindow.org and delete any left for the two names.

**To remove the site from Cloudflare altogether.** Cloudflare's pages document this as a
command, not as dashboard steps: `wrangler delete`, which its page describes as "Delete your
Worker and all associated Cloudflare developer platform resources." The page does not say
whether that also removes the addresses and their DNS records, so check both afterwards. The
command needs a person signed in to Cloudflare at a keyboard. No session runs it. The dashboard
very likely has a delete choice in the site's Settings as well, but no page that was opened
says so. Do step 1 first here too.

**To go back to the release before, without taking the site down.** Cloudflare's page on
rollbacks gives the steps: Workers & Pages, then `beyondthewindow`, then Deployments, then the
three-dot menu on the earlier version, then Rollback. The page says a rollback "applies to your
Worker's routes and domains", and that only the 100 most recent versions can be gone back to.
It does not plainly say that the older set of pages comes back with the older version, so look
at the site afterwards. The next push replaces whatever a rollback put back. The surer way to
put back earlier pages is a push to `main` that undoes the fault.

## What the tick and the cross mean, in full

A run appears in the repository's Actions tab after every push that touches the records, the
scripts or the site. Because the repository is public, anyone can read the record of each run.
Nothing in it is secret.

- **A green tick:** every check passed and Cloudflare accepted the pages. The site shows the
  pushed version.
- **A red cross on an early step:** nothing was sent to Cloudflare and the public site is
  exactly as it was before the push.
- **A red cross on the step "Deploy to Cloudflare Workers":** this does **not** always mean
  nothing changed. If the key is missing or refused outright, nothing changed; that is what
  every run shows until the two values are set. But this step does several things in turn, and
  if it fails partway, new pages can be live under a red cross. Look at the site in a browser
  before assuming either way.
- **A yellow warning with a green tick:** the last step found no `CLOUDFLARE_DEPLOY_HOOK`
  value. The site was published; only the Sentient Horizons page was not told.
- **"Cancelled":** a newer push arrived while this run was going, and the newer run took over.
  The newer run publishes the newer pages, so look at that one.

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

The first run that succeeds puts the pages on Cloudflare **and** points the two addresses at
them, in one step. John ruled on 2026-11-19 that one go covers both ("Yes, one go";
`docs/rulings/2026-11-19-three-points-on-the-first-release.md`).

## What is still different from the sibling sites

John's principle: "Copy them as much as possible since they seem to be working fine. If there
is a need to deviate, please explain why". The five sibling sites compared are The Belt
Equation, The Quiet Galaxy, The Upgrade Tree, Outrunning Ageing and the AGI Zeitgeist. I read
each one's workflow and settings file on this Mac on 2026-11-19. The workflow here was fitted
from The Quiet Galaxy's, and the second check compared the two line by line by program and
found each difference below to hold. The triggers, the cancelling of an older run by a newer
one, the deploy step (`cloudflare/wrangler-action@v3`, left as all five have it), the two
permissions on the key, the plain Cloudflare address being on, and the step that tells
Sentient Horizons to rebuild are the same as theirs.

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
   Zeitgeist names "4" in its workflow, as this one names its version. The package files were
   outside what I was asked to touch. The number is the one in The Quiet Galaxy's lock file,
   so both sites deploy with the same tool. To match the three siblings exactly, a later
   session adds the tool to `site/package.json` and removes this line.
3. **`CHANGELOG.md` is not among the paths that start a run.** It is on The Quiet Galaxy's
   list because that site's pages read it. Nothing in this site's build reads this
   repository's changelog.
4. **There is no check of news posts.** The Quiet Galaxy has one. This project has no news
   posts and no such script. The other checks are this project's own scripts under their own
   names.
5. **The job is told it may only read the repository** (`permissions: contents: read`). No
   sibling's workflow says this. The second check found that GitHub's setting for this
   repository already gives read-only access, so the line changes nothing now and keeps it so
   if the setting changes. It can be removed at no cost if John would rather the file matched
   line for line.

The Belt Equation's settings file does not set the plain Cloudflare address either way; the
others set it on, and this file follows them.

## The build and checks, run locally

**By this session,** on 2026-11-19 for the third version, on a fresh copy of the repository at
the commit then last (`00d8ae4`, the ruling that every push publishes) with the two changed
files added: the record check, 28 tests, the install, the build of 18 pages and the check of
the built site all passed, the Python steps under Python 3.12. The deploy step and the step
after it were not run.

**By the checking session,** on the same day, on a fresh copy at a later commit (`2486969`,
the site fixes after the check and the second search pass), under Python 3.12 and Node 22: the
same steps passed (29 tests by then, 78 outside addresses linked), and so did the deploy
tool's trial mode on the settings file as it now stands, which reads the file and the built
pages and sends nothing.

This fourth version changes only this note, so nothing was run again for it.

Not covered by either: the real deploy step and the step after it, which cannot be tried
without the secret values.

## Outside these files, before a first release

As the second check found them on 2026-11-19. Another session is working on these files, so
they may have changed since. I changed none of them.

1. **Search engines are told to stay away, in three places.**
   - `site/src/layouts/Base.astro`, line 53, puts `<meta name="robots" content="noindex,
     nofollow" />` on every page: do not list this page and do not follow its links.
   - `site/public/robots.txt` says: "Nothing is published yet (2026-11-17). Until John rules
     that the site goes public, no page is offered to search engines." followed by `User-agent:
     *` and `Disallow: /`, which asks every search engine to read no page.
   - `scripts/check_site.py` (rule 5 in its opening text) refuses any built page that lacks the
     `noindex` line.

   Whether the first release is listed by search engines is John's to rule. Listing it means
   changing all three, or the check will stop every push from publishing. Two more things,
   from the first check's section 7 and more pressing now that a release is one step away:
   the comment in `robots.txt` will be a public file on the site saying "Nothing is published
   yet"; and its `Disallow` line stops Google reading the "do not list" line on each page, so
   the two work against each other.
2. **`README.md` is out of date and is public now.** Its status paragraph (lines 10 to 13 when
   the second check read it) says there is no GitHub repository and nothing deployed.
3. **Licence files.** The ruling that made the repository public says the repository needs the
   licence files the siblings carry. The second check found none there yet.
4. **No page names its one real address.** The same pages answer at several addresses (see the
   take-down section). A line in the head of `Base.astro` naming the page's address at
   beyondthewindow.org would tell search engines the others are copies. It only matters once
   the site is listed.
5. **The public copy of the headline file** is served at `/data/headline.json`. That is by
   design (`scripts/export.py` writes it).

## For John's other repository, not this one

The Quiet Galaxy's `.github/workflows/deploy.yml` has its last step, the one that tells
Sentient Horizons to rebuild, written twice. It is harmless (the parent is told twice on every
release). I copied it here once and changed nothing there.

## Facts here that no opened page backs

- That the two permissions are enough to attach the two addresses on a first release. The
  siblings' workflows say their keys have those two, but their addresses were first attached
  by hand. What to do if they are not enough is above, under "What to do if it does not work".
- Where a secret is deleted on GitHub. GitHub's pages do not give steps for it.
- The exact button for removing an address from the site, and whether the dashboard can delete
  the site. Cloudflare's pages give neither.
- That Cloudflare's building from GitHub is off unless someone connects a repository. Its pages
  describe connecting as a step a person takes and do not say "off by default" in those words.
- Whether version addresses stay off after a later release, and whether one already given out
  stops working once they are switched off. Cloudflare's page stops short of saying either.
- How a clashing record is treated, and what happens with an empty key, are known from the
  checking session's reading of the deploy tool's code at version 4.151.1, not from a page.

Now backed by GitHub's pages, which the checking session opened: the path for adding a secret,
and that a workflow can be switched off and where.

## Sources

Opened on 2026-11-19, through reading sessions that reported what each page says. Cloudflare:
[custom domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/),
[the workers.dev address](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/),
[addresses for uploaded versions](https://developers.cloudflare.com/workers/versions-and-deployments/version-urls/),
[the settings file](https://developers.cloudflare.com/workers/wrangler/configuration/),
[the deploy tool's commands](https://developers.cloudflare.com/workers/wrangler/commands/workers/),
[rollbacks](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/rollbacks/),
[building from a GitHub repository](https://developers.cloudflare.com/workers/ci-cd/builds/)
and [connecting one](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/),
[deploying from GitHub](https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/),
[what each key template allows](https://developers.cloudflare.com/fundamentals/api/reference/template/),
and [the deploy step's own page](https://github.com/cloudflare/wrangler-action).

Opened by the checking session and relied on here through its note
(`docs/reviews/2026-11-19-second-check-of-deploy-files.md`), not opened by me: GitHub's pages
on [secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets),
on [switching a workflow off](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows)
and on [approving runs from a stranger's copy](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/approve-runs-from-forks),
and Cloudflare's [list of what each permission allows](https://developers.cloudflare.com/fundamentals/api/reference/permissions/).

Read directly on this Mac: the workflow and settings file of each of the five sibling sites,
the two checks of the deploy files, and the rulings named in the next section.

## The four versions of this note

All of 2026-11-19.

1. **First** (the commit that added the deploy files, `024ac7d`), after John's hosting ruling
   as it then stood (`docs/rulings/2026-11-19-hosting-private-and-by-hand.md`): a private
   repository and releases only by hand.
2. **Second** (the commit that revised them, `136197f`), after the first check
   (`docs/reviews/2026-11-19-check-of-deploy-files.md`) and John's ruling on three points
   about the first release: the correction that a clashing record is replaced without asking,
   the two-permission key, the take-down steps, what a tick and a cross mean.
3. **Third** (the commit that brought them into line with the siblings, `730ddb7`), after two
   more rulings. `docs/rulings/2026-11-19-repository-is-public.md`: John, "I see no reason to
   make any of this private. Let's follow the standard we have already set on the other sites"
   (decided by: John). `docs/rulings/2026-11-19-every-push-publishes.md`: asked "Does every
   push publish the site, as on the sibling sites?", John, "Yes, like the siblings" (decided
   by: mixed). A push now publishes, a newer run cancels an older one, the plain Cloudflare
   address is on, and the Sentient Horizons step is copied in.
4. **Fourth,** this one, after the second check. It changes this note only; the two deploy
   files are as the third version left them, because no point of the check needed them
   changed.
   - *Must fix 1:* the take-down steps now switch off the addresses Cloudflare gives each
     uploaded version, written from Cloudflare's page, and the count of addresses is
     corrected. The third version said that with three addresses closed "nobody can reach the
     site", which was wrong.
   - *Should fix 1:* what to do if the key is refused when the addresses are first attached,
     and that the site can then already be public at the plain Cloudflare address.
   - *Should fix 2:* the caution about accepting a stranger's proposed change.
   - *Should fix 3:* three items moved out of the list of facts no page backs.
   - *Should fix 4:* the screen may say "Write" where the note says "Edit".
   - *Should fix 5:* the list of things outside these files brought up to date, with the
     licence files added.
   - "What John does himself" moved to the top as four steps, followed by what he will see
     when it works and what to do if it does not.

Decided by: agent, and not ruled by John: differences 2 to 5 from the sibling sites, and the
name `beyondthewindow` on Cloudflare, which follows the siblings' way of naming and is hard to
change after the first release.
