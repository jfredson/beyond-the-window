# Rulings: three points about the first release

Ruled by John on 2026-11-19, in conversation with the master planning session, one point at a
time. Written by Claude (Fable 5.2), an AI model. The points come from the check of the deploy
files (`docs/reviews/2026-11-19-check-of-deploy-files.md`).

## Point 1: one go covers the first release and pointing the address at it

**Decided by: mixed** (a session proposed and recommended, John approved).

The hosting ruling (`docs/rulings/2026-11-19-hosting-private-and-by-hand.md`) listed "pointing
the address at the site" and "the first release" as two things that each wait for John's go.
The check found that, as the files are written, the first run does both in one step.

- *The choice:* one go covers both, or the first release is split in two: a first run to a
  plain Cloudflare address, which John looks at, then a second run that points
  beyondthewindow.org at it.
- *The recommendation:* one go.
- *Why:* Cloudflare serves pages built by the same steps from the same files as the copy on
  this Mac, and the two-step route creates a second public address that must then be switched
  off or left standing.
- *Confidence:* moderate. A first release to a new host can go wrong in ways a local copy does
  not show.
- *Standard practice or judgment call:* one go is what the sibling sites do; following them
  here is a judgment call.
- *Strongest alternative:* two steps, which lets John see the real pages before his address
  carries them, at the cost of an extra run and a second public address.
- *Two things said to hold either way:* John looks at the records for beyondthewindow.org
  first, because a run started from GitHub replaces a clashing record for the address or its
  `www` form without asking; and the steps for taking the site down are written before the
  first release.

The question put to him was "Does one go from you cover both the first release and pointing
the address at it?" John: "Yes, one go".

**Ruled:** John's go to publish covers both the first release and pointing
beyondthewindow.org and www.beyondthewindow.org at it. This revises the hosting ruling on that
one point. It is not itself the go.

## Points 2 and 3: copy the sibling sites, and explain any difference

**Decided by: John** for the principle (his own words). The applications below are the master
session's reading of it (**decided by: agent**), told to him the same day.

Put the question "Which Cloudflare key do you make for this site?", with a narrow key
recommended over Cloudflare's ready-made template, John answered with a principle:

> "What key do the other sites use? Copy them as much as possible since they seem to be working
> fine. If there is a need to deviate, please explain why"

**What the session found.** The deploy files of all five tracker sites (The Belt Equation, The
Quiet Galaxy, The Upgrade Tree, Outrunning Ageing and the AGI Zeitgeist) describe the same key
in their opening comment: two permissions, "Workers Scripts: Edit" on the account and "Workers
Routes: Edit" on the site's own zone. Each repository holds its own stored copy, set between
2026-09-20 and 2026-10-17 (names and dates read from GitHub; no value was read or can be). That
is the narrow key. The template was the deploy note's own suggestion and matches no sibling.

**Ruled, by the principle:** this site's deploy setup copies the sibling sites wherever it can,
and every difference is explained.

**Applied (decided by: agent):**

- *The key (point 2):* the same two permissions as the siblings, with the zone set to
  beyondthewindow.org. Not Cloudflare's template.
- *Who can start a release (point 3):* no extra guard is added. The check noted that once the
  secrets are set, a session on this Mac could start a release with one command. On the
  sibling sites any push already publishes, so this site is still the more guarded of the two
  arrangements, and the project's guideline that a release needs John's go stands.

**The differences from the siblings that remain, each with its reason:**

1. *The repository is private.* It holds the ten sealed questions. Ruled by John.
2. *A release starts by hand, not on every push.* So that a push is never a release. Ruled by
   John.
3. *A second press waits for the first to finish* (the check's should-fix 6). On the siblings a
   newer push cancels an older run, which is right when pushes publish. With releases started
   by hand, cancelling could stop a run halfway through sending pages.
4. *The plain Cloudflare address is switched off* (`workers_dev` is false; the siblings keep
   it on). With it on, the site would have a second public address. This one is the writing
   session's choice and the weakest of the differences: it can be switched to match the
   siblings at no cost.
5. *The step that tells Sentient Horizons to rebuild its Projects page is left out.* This site
   is not on that page yet. It is added when John puts it there.
6. *No small script for the `www` address.* The Quiet Galaxy has one only because it forwards a
   second domain. This site has no second domain.

Nothing is published, and no key has been made, read or handled.
