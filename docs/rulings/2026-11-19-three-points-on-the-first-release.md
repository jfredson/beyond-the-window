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
