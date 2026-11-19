# Ruling: the site is hosted as the sibling sites are, from a private repository, and published only by hand

Ruled by John on 2026-11-19, in conversation with the master planning session. **Decided by:
mixed** (a session proposed and recommended, John approved). Written by Claude (Fable 5.2), an
AI model.

## How it came up

Hosting is the fifth of the six things the short path to a first version needs
(`docs/rulings/2026-11-19-first-version-short-path.md`). The session looked at how The Quiet
Galaxy is set up, which its own files say is the pattern for the family: the code sits in a
public repository on GitHub, and every push to it builds the site, runs the checks and puts the
result on Cloudflare, using two secret values stored on the repository.

## What the session told him

- *The choice:* the family's arrangement with two differences, a private repository and
  publishing only by hand; or the family's arrangement exactly as it is.
- *Why private:* this repository holds the ten sealed questions, and the method says they are
  not published while they are still being asked. The last withdrawal they are for is on
  2027-01-14. A public repository would publish them, with every past version of every file.
- *Why by hand:* on the sibling sites every push publishes. Here a push is never a release, and
  each release is John's go.
- *Confidence:* high on private. Moderate on publishing by hand, which is safer and slightly
  slower each time.
- *Standard practice or judgment call:* the arrangement is standard practice in the family. The
  two differences are judgment calls.
- *Strongest alternative:* public, like the siblings, which lets anyone inspect the records and
  their history. Its cost is that the sealed questions become public, unless a new repository
  is made without them and without the history.
- *What a yes would cover:* the session creates a private repository on GitHub for this project
  and pushes `main` to it, which is not publishing; a session writes the two files that build
  and deploy the site, and a different session checks them.
- *What it would not cover:* the two secret values on the repository, which are keys and are
  John's to set; pointing beyondthewindow.org at the site; and the first release.

The question put to him was "Host it like the sibling sites, with a private repository and
publishing only by hand?" John: "Yes, private, by hand". **Decided by: mixed.**

## What is ruled

1. **The repository on GitHub is private.**
2. **The site is built and put on Cloudflare the way the sibling sites are,** with one
   difference: it goes out only when the deploy is started by hand. A push does not publish.
3. **The master session creates the repository and pushes `main` to it.**
4. **A session writes the deploy files, and a different session checks them.**

## Not covered by this ruling

- **The two secret values.** John sets them himself. No session reads, prints or handles them.
- **Pointing the address at the site, and the first release.** Each waits for his go.
- **Making the repository public.** If that is ever wanted, it is put to John first, because of
  the sealed questions and because the documents inside say which were written by a model.
- **Later pushes.** The master session reads his yes as covering later pushes of `main` to this
  private repository, since a hosted site cannot be kept up without them. That reading is the
  session's (decided by: agent). Other sessions still do not push.

Nothing is published.
