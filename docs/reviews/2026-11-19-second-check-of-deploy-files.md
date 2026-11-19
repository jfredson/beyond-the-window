# Second check of the files that build the site and put it on Cloudflare

Written by Claude (Fable 5.2), an AI model, on 2026-11-19, as the checking session. This is the
second check. The first is `docs/reviews/2026-11-19-check-of-deploy-files.md`. Since then the
writing session revised the files twice (the commits `136197f` and `730ddb7`) and John ruled
three more times: one go covers the first release and pointing the address at it, the
repository is public, and every push that passes the checks publishes, as on the sibling
sites.

I checked the files as they stand at the last commit (`2486969`, the site fixes after the
check and the second search pass): `.github/workflows/deploy.yml` (the list of steps GitHub
runs), `site/wrangler.jsonc` (the Cloudflare settings) and the writing session's note
(`docs/reviews/2026-11-19-deploy-files-written.md`, third version). I wrote none of them and
changed none of them. I deployed nothing, signed in to nothing, read and set no secret, did
not look at which secret values exist, pushed nothing, and changed nothing in Cloudflare or in
the GitHub repository's settings. Nothing is published.

## The two answers

**Is it safe to push now? Yes,** as long as the two secret values are still not set. I did not
look; the master planning session checks that before each push, as the ruling says. With the
values unset, the push starts one run on GitHub. The run passes every check, then fails at the
step "Deploy to Cloudflare Workers" because it has no key, and shows a red cross. Nothing
reaches Cloudflare. Every later push that touches the records, the scripts or the site does
the same until the values are set.

**Is it safe for the first release, once John has set the two values and given his go? Yes.**
The files need no change to work. One thing in the instructions should be corrected before
the release (must fix 1), because it is in the steps for taking the site down, and those are
the steps that have to be right on a bad day.

## Must fix

1. **The take-down steps leave the site reachable.** The note says that with the two addresses
   removed and the plain Cloudflare address disabled, "nobody can reach the site". That is not
   so. With `workers_dev` on, Cloudflare also gives each uploaded version of the site its own
   public address (Cloudflare calls these Version URLs; they look like a short code, then
   `-beyondthewindow.`, then the account's name, then `.workers.dev`). Cloudflare's page on the
   plain address says in so many words that disabling it does not disable those. They are
   switched off in the same place in the dashboard: Workers & Pages, then `beyondthewindow`,
   then Settings, then Domains & Routes, then "Disable" beside Version URLs. The take-down
   steps need that fourth thing, and the note's count of addresses ("three") should say that
   each release also has an address of its own. The sibling sites are the same, so this is no
   difference from them. The addresses are hard to guess but they are public.

## Should fix

1. **Say what to do if the key is refused when attaching the addresses.** On the sibling
   sites the addresses were first attached by hand in the dashboard (their settings files say
   so), and the deploys since have only kept them in place. Here the first run attaches them
   itself. So the siblings show a little less than the note says about whether the two
   permissions are enough for a first attaching. The note already states the doubt. What it
   lacks is the way out, which is the siblings' own way: in the dashboard, Workers & Pages,
   then `beyondthewindow`, then Settings, then Domains & Routes, then Add, then Custom Domain
   (Cloudflare's page gives these words). Also worth a line: the deploy tool turns on the plain
   Cloudflare address and attaches the two addresses side by side, so if only the attaching
   fails, the site can already be public at the plain Cloudflare address under a red cross. The
   note's section on the tick and the cross covers this in general terms.
2. **A pull request is safe to receive and not always safe to accept.** See section 4. The
   note should carry one line for John: before accepting a stranger's proposed change that
   touches `.github/`, `scripts/` or the site's package files, read it, because once accepted
   it runs with the key and publishes.
3. **Three of the note's "from memory" items are now backed by GitHub's pages** and can be
   moved out of its list of unbacked facts: the path for adding a secret (Settings, then
   Secrets and variables, then Actions, then "New repository secret", then "Add secret"); that
   a workflow can be switched off (Actions tab, the workflow's name at the left, the button
   "Show workflow options", then "Disable workflow"); and GitHub's page adds that switching a
   workflow off does not stop a run already going. GitHub's pages do not give steps for
   deleting a secret.
4. **The key's permissions may be worded "Write" on the screen.** Cloudflare's list of
   permissions gives both "Workers Scripts Edit" and "Workers Scripts Write" for the same
   thing, and the same for Workers Routes, without saying which wording is current. The note
   says "Edit" only.
5. **Outside these files, still as the first check found them,** and now more pressing because
   the repository is public and a release is one step away: `site/public/robots.txt` still
   opens with "Nothing is published yet (2026-11-17). Until John rules that the site goes
   public", and will be a public file on the site; its `Disallow` line still stops Google
   reading the "do not list" line on each page; and `README.md` (lines 10 to 13), which is
   public now, still says there is no GitHub repository and nothing deployed. The note lists
   all three. The ruling that made the repository public also says licence files are to be
   added; none is there yet.

## 1. Every difference from The Quiet Galaxy's files

Compared line by line by program, with the two files side by side.

**The workflow** (`.github/workflows/deploy.yml`):

| Difference | Stated reason | Does it hold? |
|---|---|---|
| The opening comment is this site's own, and adds that John sets the values and that the first release is his go | The rulings | Yes |
| `CHANGELOG.md` is not among the paths that start a run | Nothing in this site's build reads the changelog | Yes. I searched the site's pages and the scripts and found no use of it. The Quiet Galaxy's About page does read its own |
| A block saying the job may only read the repository | The repository is public and one step is another party's code | Yes. GitHub's setting for this repository already gives read-only access, so the block changes nothing now and keeps it so if the setting changes |
| The record check is `scripts/compute.py --check`, where the sibling has `scripts/export.py --check` | This project's own script | Yes |
| No check of news posts | No news posts and no such script | Yes |
| A comment that the build runs the record check before and the site check after | True of `site/package.json` | Yes |
| The check of the built site is called with `--dist site/dist`, and named for the rules of public text | That is how this project's script takes the folder | Yes |
| The deploy tool's version (4.151.1) is named in the workflow | The site's package files do not list the tool | Yes as an explanation. It is a real difference in how the tool arrives: GitHub fetches it at each run. The AGI Zeitgeist's workflow does the same and deploys. Adding the tool to the package files later would remove the difference |
| The step that tells Sentient Horizons to rebuild appears once, where the sibling has it twice | The sibling's second copy is a slip | Yes. The one copy here is the same as the sibling's, character for character |

Everything else is the same: the triggers (a push to `main` and the button), a newer run
cancelling an older one, the versions of Python and Node, the install and build, the deploy
step and its version, and the two secret names.

**The settings** (`site/wrangler.jsonc`):

| Difference | Stated reason | Does it hold? |
|---|---|---|
| The name `beyondthewindow` | Follows the siblings' naming | Yes. No other project in `~/Code` uses it |
| No script in front of the pages, so no `main`, `binding` or `run_worker_first` | No second domain to forward | Yes. The file has the same shape as The Belt Equation's, which I read |
| `compatibility_date` is 2026-11-01, where the sibling has 2026-10-01 | None stated | Harmless. Cloudflare's page says to set it near the day of writing |
| Two addresses, where the sibling has four | The sibling's other two are its second domain | Yes |
| A longer comment on the addresses | It carries the first check's correction | Yes, and it is now right |

The plain Cloudflare address is on, as on the sibling.

## 2. What a push does now, and after the values are set

**Now, with the two values unset.** GitHub has an older version of the workflow, the one
started only by hand, and has never run it. The three commits not yet pushed include the new
workflow and changes to the site, so the push starts one run. It checks the records, runs the
tests, builds the site and checks the built pages. Then the deploy step runs with an empty
key. GitHub's page says an unset secret is an empty string, the deploy step's own list of
inputs marks the key as optional, and the deploy tool's code (version 4.151.1) stops with the
message that a key is needed when nobody is at a keyboard. The step fails, the step after it
does not run, and the run shows a red cross. Nothing is sent to Cloudflare, so nothing can be
published before the values are set. I read this from the code and the pages; I did not run
the deploy step. The sibling's workflow describes the same behaviour for itself.

Two small things to expect: GitHub may send John a message about the failed run (from memory,
not from an opened page), and because the repository is public, the record of each run can be
read by anyone. Nothing in it is secret.

**The first push after both values are set,** or a press of the button. The same steps, and
then the deploy step succeeds. It creates a Worker named `beyondthewindow` on John's account,
sends it the 22 built files, turns on the plain Cloudflare address, and attaches
beyondthewindow.org and www.beyondthewindow.org, replacing without asking any record that
clashes with those two names. Within a few minutes the site is public at those addresses.
The last step then prints a warning, because the third value is not set, and the run shows a
green tick. From then on every push to `main` that touches the records, the scripts, the site
or the workflow, and passes the checks, replaces the public site. The ruling says the master
session pushes nothing between the values being set and John's go; nothing in the files
enforces that, and it is not meant to.

A push that touches none of those paths, such as one changing only documents, should start no
run. That is how I understand GitHub's path filter; the page was too long for the reading
session to quote that sentence.

## 3. The first check's points

| First check | Now |
|---|---|
| Must fix 1: a clashing record is replaced, not refused | Corrected, in the settings file's comment and in step 1 for John |
| Should fix 1: start with the narrow key | Done. Two permissions, one account, one zone, and both limits stated |
| Should fix 2: the screens for making a key have changed | Done well: the step says what to end up with. Cloudflare's page as it stands speaks of starting "from scratch" and choosing a policy type of Account or Zone, which fits. See should fix 4 above on "Edit" and "Write" |
| Should fix 3: any session could start a release | Moot. John ruled that every push publishes |
| Should fix 4: no steps for taking the site down | Written, and right against Cloudflare's pages on each point I could check (where the addresses are listed, the certificate left behind, the delete command, the rollback steps and their limit of 100 versions), with one gap: must fix 1 above |
| Should fix 5: what a tick and a cross mean | Done, and correct. The "skipped" case is gone with the rule that made it |
| Should fix 6: a second run cancels the first | Reversed on purpose by the ruling, to match the siblings. The note explains "Cancelled" |
| Should fix 7: a redirect for www needs no script | The wrong claim is gone. The note says plainly that www shows the same pages, as on The Belt Equation |
| Should fix 8: the comment undersold the template | Gone with the template |
| Should fix 9: the deploy step is a version behind | Kept at version 3 to match all five siblings, with the reason stated. Version 3 is not marked as retired on its own pages; version 4 is the current one |
| Should fix 10: do not connect the repository inside Cloudflare | Done, with the right new reason (it would publish without the checks) and the place to disconnect, which matches Cloudflare's page |
| Section 7: the search-engine files | Not changed, and not for these files. See should fix 5 above |

The other steps for John: finding the account id matches Cloudflare's page; adding the two
values matches GitHub's page; starting a run by hand matches GitHub's page.

## 4. A stranger's pull request, now that the repository is public

A pull request is a change a stranger proposes from their own copy of the repository.

- **It cannot start this workflow.** The workflow starts on a push to `main` of this
  repository or on the button. GitHub's page says the button needs write access. The
  repository has one person with any access, John (read from GitHub, changing nothing).
- **It cannot reach the secret values.** GitHub's page on secrets says that, apart from a
  read-only pass GitHub makes for each run, secrets are not handed to a run started from a
  stranger's copy. So even a proposed change that adds a workflow of its own gets no key.
  GitHub's pages did not say, in what the reading session could quote, which version of a
  changed workflow runs for a pull request; the point above holds either way.
- **A first-time stranger's run waits for approval.** The repository's setting is the default:
  runs from people who have never had a change accepted wait for John to approve them.
- **A stranger's own copy has no values.** Secrets are not copied with a repository. A run
  there fails at the deploy step as it does here now.
- **The real exposure is accepting a change.** Once John accepts a pull request, it is a push
  to `main`: the checks run and the result is published, with the key. A change to a script,
  to the workflow or to the site's packages could weaken a check or misuse the key at that
  moment. `main` has no protection rule, which is right for one maintainer. See should fix 2.

## 5. The build and checks, run here

Run on 2026-11-19 on a fresh copy of the last commit (`2486969`), outside the working folder,
under the workflow's own versions: Python 3.12 and Node 22.

| Step | Result |
|---|---|
| Check the records and the headline file | Passed: 13 records, the headline file matches |
| Tests | Passed: 29 tests |
| Install the site's packages (`npm ci`) | Passed |
| Build, with its own checks before and after | Passed: 18 pages |
| Check of the built site | Passed: 18 pages, 78 outside addresses linked |
| The deploy tool's trial mode on the changed settings | Passed |

**The trial mode.** `wrangler deploy --dry-run` at version 4.151.1, with no key in its
surroundings and an empty folder as its home, so it had no sign-in to use. It asked for none.
It reported "Read 40 files from the assets directory" (22 files and 18 folders), "No bindings
found" and "--dry-run: exiting now", with no warning about any setting. It also mentioned that
a newer version of the tool exists (4.165.0). This shows the tool accepts the file. It does
not test the key, the account, or whether Cloudflare will attach the addresses.

## What I did not check

- Whether the two secret values are set. The first answer depends on their being unset.
- The Cloudflare account: whether a Worker named `beyondthewindow` exists, what records the
  address has, and whether Cloudflare's own building from GitHub is connected.
- The real deploy step and the step after it.
- Whether the two permissions are enough to attach an address for the first time.
- GitHub's sentence on what a path filter does with a push that touches none of the paths, and
  whether GitHub sends a message about a failed run.

## Sources

Opened on 2026-11-19 through reading sessions that reported what each page says, with the
sentences quoted. Cloudflare:
[custom domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/),
[the workers.dev address](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/),
[addresses for uploaded versions](https://developers.cloudflare.com/workers/versions-and-deployments/version-urls/),
[rollbacks](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/rollbacks/),
[building from a GitHub repository](https://developers.cloudflare.com/workers/ci-cd/builds/)
and [connecting one](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/),
[the deploy tool's commands](https://developers.cloudflare.com/workers/wrangler/commands/workers/),
[the settings file](https://developers.cloudflare.com/workers/wrangler/configuration/),
[creating a key](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/),
[what each permission allows](https://developers.cloudflare.com/fundamentals/api/reference/permissions/),
[the deploy step's list of inputs](https://github.com/cloudflare/wrangler-action/blob/main/action.yml)
and [its releases](https://github.com/cloudflare/wrangler-action/releases). GitHub:
[what starts a workflow](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows),
[secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets),
[approving runs from a stranger's copy](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/approve-runs-from-forks),
[the repository's settings for Actions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository),
[starting a workflow by hand](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow),
[switching a workflow off](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows)
and [one run cancelling another](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency).

Read directly on this Mac: the three files checked, the three rulings, The Quiet Galaxy's and
The Belt Equation's workflow and settings files, the project's scripts, and the deploy tool's
code at version 4.151.1. Read from GitHub, changing nothing: that the repository is public,
who has access, its settings for Actions, and that no run has happened yet.
