# The go to publish, and the first release

Given by John on 2026-11-19, in conversation with the master planning session. **Decided by:
John.** Written by Claude (Fable 5.2), an AI model.

## The go

The site had been checked as fit to publish
(`docs/reviews/2026-11-19-check-of-the-last-fixes.md`), and John had approved the sentences
that are his (`docs/rulings/2026-11-19-about-page-sentences-stand.md`). The master session set
out the four steps that put the site out and said: "Say go when you want it out." He had asked
the session to "handle as much of this process as possible".

John: "Stored, go".

## What was done, and by whom

- *The records for beyondthewindow.org:* read by the session in the Cloudflare dashboard after
  John signed in. There were none.
- *The key:* the session filled in Cloudflare's form from the template "Edit Cloudflare
  Workers", named `beyond-the-window`, matching the sibling sites' keys, and stopped at the
  summary. John pressed the button that creates it. The session never saw the key's value.
- *The account id:* stored on the repository by the session. It is an identifier, not a key.
- *The key's value:* stored on the repository by John, from his own Terminal.
- *The push:* by the session, on the go, at the commit that corrected the deploy note
  (`73fd4af`).

## What happened

1. **The first run failed at its last step,** "Deploy to Cloudflare Workers", with Cloudflare's
   message "Invalid format for Authorization header". Every check before it passed, nothing
   reached Cloudflare, and the address still pointed nowhere. The value stored as the key was
   not a key: the command that stores it had been run three times, each run replacing the
   value with whatever was pasted.
2. **The key was given a fresh value** (Cloudflare calls this rolling it). The session opened
   the confirmation and stopped; John confirmed, and stored the value with a command that
   reads the clipboard directly.
3. **The session started the same run again, and it passed.** 23 files were sent. Cloudflare
   attached `beyondthewindow.org` and `www.beyondthewindow.org`.

**The site has been public at https://beyondthewindow.org/ since 2026-11-19** (about 23:45
universal time). The session fetched the home page, the About page, the Still Asking page, the
list, one entry, the headline file and the robots file, each of which answered, and a missing
address, which gave the page for a missing address. The home page carries the ruled sentence
and no instruction to search engines to stay away. The pages are also reachable at the plain
Cloudflare address, `beyondthewindow.jfredson.workers.dev`, as the sibling sites' are.

## What follows

- From now on a push that touches the records, the scripts or the pages and passes the checks
  publishes (`docs/rulings/2026-11-19-every-push-publishes.md`). Only work a different session
  has checked is pushed, and sentences in John's first person go to him first.
- Corrections are dated and stay visible (guideline 7).
- Open question 13, on timing, is answered by the fact: the first version went out on
  2026-11-19.
- The line "No AI model has yet been asked any of the questions this record will keep" must
  change when the sealed capture runs, and the new wording goes to John first.
