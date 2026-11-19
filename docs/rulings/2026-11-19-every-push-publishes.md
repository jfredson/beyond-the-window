# Ruling: every push publishes the site once the checks pass, as on the sibling sites

Ruled by John on 2026-11-19, in conversation with the master planning session. **Decided by:
mixed** (a session re-examined its own earlier proposal and recommended dropping it; John
approved). Written by Claude (Fable 5.2), an AI model.

This ruling replaces point 2 of `docs/rulings/2026-11-19-hosting-private-and-by-hand.md` ("it
goes out only when the deploy is started by hand"). With
`docs/rulings/2026-11-19-repository-is-public.md` it leaves nothing of that ruling's two
differences from the sibling sites. That file is left as it was.

## How it came up

John asked to be walked through each difference from the sibling sites as if its reason were
not known. This was the second.

## What the session told him

- The reason given had been that a push should never be a release, and each release should be
  his go.
- Before the first release that does real work: the site cannot go out by accident while it is
  being fixed. After it, it mostly slows the work, since every correction waits for a button.
  John had said he wants to publish a first version and iterate from there.
- The siblings' protection is the checks and not a button: a push that fails a check publishes
  nothing, and this site has the same checks.
- The rule behind the difference is a project guideline that publishing waits for John, and he
  wrote of those guidelines that none should get in the way.
- *The recommendation:* match the siblings. A push publishes once the checks pass, and the
  button stays as well, as on theirs.
- *How the first release then works:* nothing can publish until the two secret values are on
  the repository, so the first release is John setting them and saying go. Until he says so,
  nothing is pushed after they are set.
- *Confidence:* moderate. *Standard practice* in the family.
- *Strongest alternative:* keep it by hand, so that he sees every release first, at the cost
  that each fix waits for him.
- *One consequence said to him:* a session's checked change goes live without him reading it
  first, as on the siblings. Corrections stay dated and public, and anything in his own first
  person still comes to him before it is pushed.

The question put to him was "Does every push publish the site, as on the sibling sites?"
John: "Yes, like the siblings". **Decided by: mixed.**

## What is ruled

1. **A push to `main` that touches the records, the scripts or the pages runs the checks and,
   if they pass, publishes the site.** The deploy can also be started by hand, as on the
   siblings.
2. **The first release is still John's go.** He sets the two secret values and says go.

## How the session applies it (decided by: agent)

- Before any push, the master session looks at whether the two secret values are set on the
  repository (their names and dates only). Once they are set, it pushes nothing until John has
  given the go for the first release.
- After the first release, only work that a different session has checked is pushed, and any
  sentence in John's first person goes to him before it is pushed.
- The three smaller differences that followed from releases being by hand, or that had no
  reason strong enough to stand against "copy them as much as possible", are dropped: a newer
  run cancels an older one, as on the siblings; the plain Cloudflare address is on, as on the
  siblings; and the step that tells Sentient Horizons to rebuild its Projects page is copied
  in, where it only warns until its secret value exists.
- One difference is left, and it is nothing to copy: the siblings' small script for a second
  domain, which this site does not have.

Nothing is published.
