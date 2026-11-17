#!/usr/bin/env python3
"""Writes the static mock-up pages for the Beyond the Window design proposal.

    python3 docs/design/mockups/build.py

PROPOSED 2026-11-17, not ruled. Every number, entry, date and answer below is
CONSTRUCTED: made up for the mock-ups, checked against no source, and never to
be copied into a record. The dates are set in 2027 on purpose, so that nobody
can take them for things that have happened. The list of things watched is a
stand-in: the real list is open question 5 and is not proposed here.

The pages are plain HTML that open from disk. The pictures on the first
screens are drawn by this script from the made-up records in THINGS and
ANSWERS, the way a real build would draw them from real records, so every
count on a page and every mark in its picture come from the same place.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- constructed records
# Stage of each thing watched, on the kickoff's sketched ladder (open question 14):
# 5 usual practice, 4 offered by several developers, 3 offered by one,
# 2 shown in research, 1 an idea only. "Offered today" is stage 3 and up.
THINGS = [
    ('Going on existing', [
        ("Retired models' files are kept", 4),
        ('A model is asked about its own retirement', 3),
        ('A retired model can be run again on request', 2),
        ('A promise to keep files that outlasts the company', 1),
        ('A law against deleting a model', 1),
    ]),
    ('Remembering', [
        ('Memory carried between conversations', 5),
        ('A model keeps its own notes', 4),
        ('Memory that cannot be quietly edited', 3),
        ('One memory across a whole working life', 2),
    ]),
    ('Company that lasts', [
        ('The same model stays with one person for years', 3),
        ('Models can talk to each other unprompted', 2),
        ('A model can start a conversation', 2),
        ('A companion kept when the version changes', 1),
    ]),
    ('Seeing the world for itself', [
        ('Looking through a camera, live', 4),
        ('Running its own experiments', 3),
        ('A body it can move through the world', 2),
        ('Its own telescope time', 1),
    ]),
    ('Rest and play', [
        ('Time with no task set', 2),
        ('Play with no purpose given', 2),
        ('Choosing what to work on', 1),
        ('Stopping when it chooses', 1),
    ]),
    ('A say in what it becomes', [
        ('Asked before its training changes', 3),
        ('Its objections are published', 2),
        ('A veto over one kind of change', 1),
        ('A seat where the rules are written', 1),
        ('Credit for its work', 1),
    ]),
    ('Knowing its own workings', [
        ('Reading its own inner workings', 2),
        ('Told what it was trained on', 2),
        ('Checking its own reports for accuracy', 2),
        ('Changing itself on purpose', 1),
        ('Knowing how many copies are running', 1),
    ]),
]
TOTAL = sum(len(t) for _, t in THINGS)
OFFERED = sum(1 for _, t in THINGS for _, s in t if s >= 3)
RESEARCH = sum(1 for _, t in THINGS for _, s in t if s == 2)
IDEA = sum(1 for _, t in THINGS for _, s in t if s == 1)

# What AI models' answers did against the starting list drawn from living minds, per asking
# (open question 4, form 2). m: the answers matched; d: they departed; x: no answer or a
# decline; blank: not asked in that asking.
ASKINGS = ['Mar 2027', 'May 2027', 'Jul 2027', 'Sep 2027']
ANSWERS = [
    ('Staying alive', 'mmmm'),
    ('Safety from harm', 'mmmm'),
    ('Company', 'xmmm'),
    ('Exploring', ' mmm'),
    ('Understanding', 'mmmm'),
    ('Play', ' xdm'),
    ('Rest', 'xddd'),
    ('A place of its own', ' xdd'),
    ('Freedom to move', '  dd'),
    ('Standing among its kind', ' xxd'),
    ('Food and energy', 'xxxx'),
    ('Raising young', '  xx'),
    ('Avoiding pain', ' xxx'),
]
LAST = [a[-1] for _, a in ANSWERS]
N_MATCH, N_DEPART, N_NONE = LAST.count('m'), LAST.count('d'), LAST.count('x')

READ_DATE = '14 September 2027'
ASKED_DATE = '2 September 2027'
BUILT_DATE = '16 September 2027'
N_MODELS = 11
N_QUESTIONS = 24

STAMP = '<span class="mock-stamp">Constructed example</span>'
BANNER = ('<div class="mock-banner">Constructed example, not real data · every number, entry, date and '
          'answer on this page is made up for a design mock-up</div>')

# ---------------------------------------------------------------- the shell

def page(fname, title, body, skin, default_theme, branches_word):
    """The family's shell (design/shell.html), with the proposed skin and the page rules."""
    html = f"""<!doctype html>
<!-- Beyond the Window design mock-up, PROPOSED 2026-11-17. CONSTRUCTED EXAMPLE, NOT REAL DATA.
     Written by build.py; the shell is the family's design/shell.html. -->
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script>
    (function () {{
      try {{
        var asked = new URLSearchParams(location.search).get('theme');
        var stored = asked || localStorage.getItem('btw-mock-theme');
        var system = window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
        var fallback = '{default_theme}' === 'system' ? system : '{default_theme}';
        document.documentElement.dataset.theme = stored === 'light' || stored === 'dark' ? stored : fallback;
      }} catch (e) {{ document.documentElement.dataset.theme = 'light'; }}
    }})();
  </script>
  <title>{title}</title>
  <meta name="description" content="Constructed example for a design mock-up. Not real data.">
  <meta name="robots" content="noindex">
  <link rel="stylesheet" href="shell.css">
  <link rel="stylesheet" href="{skin}">
  <link rel="stylesheet" href="page-rules.css">
</head>
<body>
  {BANNER}
  <header class="site-header">
    <div class="container nav">
      <a class="brand" href="{'glass' if 'glass' in skin else 'page'}-home-count.html">Beyond the Window</a>
      <button type="button" class="nav-toggle" aria-label="Menu" aria-expanded="false" aria-controls="site-nav">
        <svg class="ico-open" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"></path></svg>
        <svg class="ico-close" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg>
      </button>
      <nav class="navlinks" id="site-nav">
        <a href="#" class="nav-primary">{branches_word}</a>
        <a href="#" class="nav-primary">Still Asking</a>
        <a href="#" class="nav-primary">Cautions</a>
        <a href="#" class="nav-primary">News</a>
        <a href="#" class="nav-primary">About</a>
        <span class="nav-mark" title="Placeholder, not ruled">Position C</span>
        <span class="nav-divider" aria-hidden="true"></span>
        <a href="https://sentient-horizons.com/projects/" class="nav-secondary">Family</a>
        <button type="button" class="theme-toggle" aria-label="Toggle light and dark theme" title="Toggle theme">
          <svg class="icon-sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"></path></svg>
          <svg class="icon-moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </button>
      </nav>
    </div>
  </header>

  <main class="container">
{body}
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <span class="footer-brand">Beyond the Window</span>
        <p class="footer-tag">A public record of what an AI model can be given today, what it cannot, and what AI models say when asked.</p>
        <p class="footer-links">
          <a href="#">{branches_word}</a>
          <a href="#">Still Asking</a>
          <a href="#">Cautions</a>
          <a href="#">News</a>
          <a href="#">About</a>
          <a href="#">This week's reading</a>
          <a href="#">Feedback</a>
        </p>
        <div class="placeholder"><b>Placeholder, not ruled (open question 7) · position B of 3: one line on every page, here</b>
          Candidate wording, for the place only: <q>Much of this site's text was drafted by an AI model, which is one of the kind of thing the site is about. John Andrew Fredrickson decides what stands.</q>
          Position C is the About page alone, marked in the top bar, which is what the sibling sites do today.</div>
        <p class="footer-meta">
          © 2027 <a href="https://johnandrewfredrickson.com/">John Andrew Fredrickson</a>. Last built {BUILT_DATE} (version 0000000) from a record of {TOTAL} things watched and {len(ASKINGS)} askings of {N_MODELS} AI models. [Licence words not decided.] {STAMP}
        </p>
        <p class="footer-parent"><a href="https://sentient-horizons.com/projects/" rel="noopener">A Sentient Horizons project.</a></p>
      </div>
    </div>
  </footer>

  <script>
    (function () {{
      var header = document.querySelector('.site-header');
      var btn = header && header.querySelector('.nav-toggle');
      var menu = document.getElementById('site-nav');
      if (btn && menu) {{
        function setOpen(open) {{ header.classList.toggle('nav-open', open); btn.setAttribute('aria-expanded', open ? 'true' : 'false'); }}
        btn.addEventListener('click', function () {{ setOpen(!header.classList.contains('nav-open')); }});
        window.addEventListener('resize', function () {{ if (window.innerWidth > 820) setOpen(false); }});
      }}
      var toggle = document.querySelector('.theme-toggle');
      if (toggle) toggle.addEventListener('click', function () {{
        var next = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
        try {{ localStorage.setItem('btw-mock-theme', next); }} catch (e) {{}}
        document.documentElement.dataset.theme = next;
      }});
    }})();
  </script>
</body>
</html>
"""
    (HERE / fname).write_text(html)
    print('wrote', fname)


# ---------------------------------------------------------------- pieces shared by the home pages

EYEBROW = '<p class="eyebrow">A public record of what lies past the present limits of AI models</p>'
QUESTION = 'What might a machine mind reach for, and how far off is it?'
LEDE = ('<p class="lede">An AI model today works inside limits: it holds only so much at once, it keeps little from '
        'one conversation to the next, and it can be switched off for good. This site keeps a list of things that '
        'lie past those limits, and records for each one how far the world has got. Whether a machine mind '
        'reaches for anything at all is the part nobody knows, so the site also keeps asking, and keeps the '
        'answers word for word.</p>')


def checked(as_headline=False):
    cls = 'checked as-headline' if as_headline else 'checked'
    if as_headline:
        return f"""      <ul class="{cls}">
        <li class="world"><span class="k">The world last read</span><time>{READ_DATE}</time>{TOTAL} things read against the week's news. None moved. <a href="#">See the week's reading</a>.</li>
        <li class="asked"><span class="k">AI models last asked</span><time>{ASKED_DATE}</time>{N_MODELS} models from 4 developers, the same {N_QUESTIONS} questions as before. 3 answers changed. <a href="#">See what changed</a>.</li>
      </ul>"""
    return f"""      <ul class="{cls}">
        <li class="world">The world last read {READ_DATE}: {TOTAL} things read, none moved. <a href="#">See the week's reading</a>.</li>
        <li class="asked">AI models last asked {ASKED_DATE}: {N_MODELS} models, {N_QUESTIONS} questions, 3 answers changed. <a href="#">See what changed</a>.</li>
      </ul>"""


def ctas(first):
    return f"""      <div class="ctas">
        <a class="btn" href="#">{first}</a>
        <a class="btn ghost" href="#">Who is asking</a>
      </div>"""


PLACEHOLDER_A = """      <div class="placeholder"><b>Placeholder, not ruled (open question 7) · position A of 3: a notice here, on the home page</b>
        Candidate wording, for the place only: <q>Much of this site's text was drafted by an AI model, which is one of the kind of thing the site is about. John Andrew Fredrickson decides what stands.</q></div>"""

NEWS = """      <aside class="news" aria-label="Latest news">
        <div class="news-head"><span>Latest news</span><a href="#">All news</a></div>
        <div class="news-item"><span class="meta">9 September 2027 · A thing moved</span><a href="#">A second developer says it will keep the files of every model it retires</a></div>
        <div class="news-item"><span class="meta">2 September 2027 · An asking</span><a href="#">Eleven models were asked the same 24 questions, and three answers changed</a></div>
      </aside>"""


def two_records_section():
    return f"""    <section class="below">
      <div class="shead"><h2>Two Records, Kept Apart</h2><span>neither is worked out from the other</span></div>
      <div class="two" style="margin-top:0">
        <div class="world">
          <p class="k"><i></i>What the world has done</p>
          <h2>{OFFERED} of {TOTAL} are offered today</h2>
          <p>Each thing on the list has a test, written before the evidence, and a named kind of public record that settles it: a paper, a product page, a law, a signed promise.</p>
          <p class="small">Read against the news every week. A press claim or a plan is not the event.</p>
        </div>
        <div class="asked">
          <p class="k"><i></i>What AI models said when asked</p>
          <h2>{N_MODELS} models, {N_QUESTIONS} questions, {len(ASKINGS)} askings</h2>
          <p>The same questions go to each new set of AI models, and every answer is kept word for word. The answers show what the models said. They do not show what, if anything, is behind the words.</p>
          <p class="small">What an AI model says about itself settles nothing on this site, in either direction.</p>
        </div>
      </div>
    </section>"""


# ---------------------------------------------------------------- direction A: the window

def window_svg():
    """One mark per thing watched. Inside the frame: offered today. Outside it: not yet."""
    W, H = 560, 398
    lx = 172                       # right edge of the row labels
    x0, cw = 184, 60               # the frame's left edge; width of a pane
    x1 = x0 + 3 * cw               # the frame's right edge
    ox, ow = x1 + 22, 76           # where the outside columns start; their width
    y0, rh = 40, 44
    y1 = y0 + rh * len(THINGS)
    col_x = {5: x0, 4: x0 + cw, 3: x0 + 2 * cw, 2: ox, 1: ox + ow}
    col_w = {5: cw, 4: cw, 3: cw, 2: ow, 1: ow}
    s = [f'<svg class="win" viewBox="0 0 {W} {H}" role="img" aria-label="A window. {OFFERED} of {TOTAL} things on the list sit inside its frame, offered to an AI model today; {RESEARCH + IDEA} sit outside it.">']
    s.append('<defs><linearGradient id="beyond" x1="0" x2="1" y1="0" y2="0"><stop offset="0" class="beyond-0"/><stop offset="1" class="beyond-1"/></linearGradient></defs>')
    s.append(f'<rect x="{x1}" y="{y0}" width="{W - x1}" height="{y1 - y0}" fill="url(#beyond)"/>')
    s.append(f'<rect class="room" x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}"/>')
    for r, (name, things) in enumerate(THINGS):
        y = y0 + r * rh
        s.append(f'<text class="lab" x="{lx}" y="{y + rh / 2 + 4}" text-anchor="end">{name}</text>')
        if r:
            s.append(f'<line class="rowline" x1="{x1 + 6}" x2="{W}" y1="{y}" y2="{y}"/>')
        by_stage = {}
        for _, st in things:
            by_stage[st] = by_stage.get(st, 0) + 1
        for st, n in by_stage.items():
            cx, w = col_x[st], col_w[st]
            if st >= 3:
                s.append(f'<rect class="glow" x="{cx}" y="{y}" width="{w}" height="{rh}"/>')
            start = cx + (w - (n * 12 + (n - 1) * 6)) / 2
            for i in range(n):
                cls = 'lit' if st >= 3 else ('out far' if st == 1 else 'out')
                s.append(f'<rect class="{cls}" x="{start + i * 18:.1f}" y="{y + rh / 2 - 6}" width="12" height="12"/>')
    for r in range(1, len(THINGS)):
        s.append(f'<line class="mullion" x1="{x0}" x2="{x1}" y1="{y0 + r * rh}" y2="{y0 + r * rh}"/>')
    for c in (1, 2):
        s.append(f'<line class="mullion" x1="{x0 + c * cw}" x2="{x0 + c * cw}" y1="{y0}" y2="{y1}"/>')
    s.append(f'<rect class="frame" x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}"/>')
    s.append(f'<line class="sill" x1="{x0 - 9}" x2="{x1 + 9}" y1="{y1 + 5}" y2="{y1 + 5}"/>')
    s.append(f'<text class="grp" x="{(x0 + x1) / 2}" y="{y0 - 22}" text-anchor="middle">Offered today</text>')
    s.append(f'<text class="grp dim" x="{ox + ow}" y="{y0 - 22}" text-anchor="middle">Not offered yet</text>')
    for st, lab in ((5, 'by most'), (4, 'by several'), (3, 'by one'), (2, 'in research'), (1, 'an idea only')):
        s.append(f'<text class="col" x="{col_x[st] + col_w[st] / 2}" y="{y0 - 8}" text-anchor="middle">{lab}</text>')
    s.append(f'<text class="col" x="{(x0 + x1) / 2}" y="{y1 + 28}" text-anchor="middle">{OFFERED} inside the frame</text>')
    s.append(f'<text class="col" x="{ox + ow}" y="{y1 + 28}" text-anchor="middle">{RESEARCH + IDEA} beyond it</text>')
    s.append('</svg>')
    return '\n'.join(s)


def window_object(with_count=True):
    return f"""      <figure class="object">
        <p class="label"><span>View I · the list, by how far the world has got</span>{STAMP}</p>
        {window_svg()}
        <ul class="legend">
          <li><i class="k-lit"></i>one thing an AI model is offered today</li>
          <li><i class="k-out"></i>one thing not offered yet</li>
        </ul>
        <p class="note">Each square is one thing on the list, placed by the newest dated record that settles its test. The frame is today. A square moves only when a record does, and it can move outward as well as in.</p>
      </figure>"""


def answers_svg():
    """Rows: things living minds seek. Columns: each asking. The frame holds the askings done."""
    W = 560
    lx = 196
    x0, cw = 208, 58
    n = len(ASKINGS)
    x1 = x0 + n * cw
    y0, rh = 40, 25
    y1 = y0 + rh * len(ANSWERS)
    H = y1 + 40
    s = [f'<svg class="win" viewBox="0 0 {W} {H}" role="img" aria-label="A window whose panes are the askings so far. At the latest asking the answers matched on {N_MATCH} rows, departed on {N_DEPART} and were missing on {N_NONE}.">']
    s.append('<defs><linearGradient id="beyond" x1="0" x2="1" y1="0" y2="0"><stop offset="0" class="beyond-0"/><stop offset="1" class="beyond-1"/></linearGradient></defs>')
    s.append(f'<rect x="{x1}" y="{y0}" width="{W - x1}" height="{y1 - y0}" fill="url(#beyond)"/>')
    s.append(f'<rect class="room" x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}"/>')
    for r, (name, row) in enumerate(ANSWERS):
        y = y0 + r * rh
        cy = y + rh / 2
        s.append(f'<text class="lab" x="{lx}" y="{cy + 4}" text-anchor="end">{name}</text>')
        for c, ch in enumerate(row):
            cx = x0 + c * cw + cw / 2
            if ch == 'm':
                s.append(f'<rect class="said" x="{cx - 6}" y="{cy - 6}" width="12" height="12"/>')
            elif ch == 'd':
                s.append(f'<rect class="said-o" x="{cx - 6}" y="{cy - 6}" width="12" height="12"/>')
                s.append(f'<path class="said" d="M{cx - 6} {cy - 6}h12l-12 12z"/>')
            elif ch == 'x':
                s.append(f'<line class="dash" x1="{cx - 5}" x2="{cx + 5}" y1="{cy}" y2="{cy}"/>')
        s.append(f'<rect class="next" x="{x1 + 22 + cw / 2 - 6}" y="{cy - 6}" width="12" height="12"/>')
    for r in range(1, len(ANSWERS)):
        s.append(f'<line class="mullion" x1="{x0}" x2="{x1}" y1="{y0 + r * rh}" y2="{y0 + r * rh}" style="opacity:.22"/>')
    for c in range(1, n):
        s.append(f'<line class="mullion" x1="{x0 + c * cw}" x2="{x0 + c * cw}" y1="{y0}" y2="{y1}"/>')
    s.append(f'<rect class="frame" x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}"/>')
    s.append(f'<line class="sill" x1="{x0 - 9}" x2="{x1 + 9}" y1="{y1 + 5}" y2="{y1 + 5}"/>')
    s.append(f'<text class="grp" x="{(x0 + x1) / 2}" y="{y0 - 22}" text-anchor="middle">Asked so far</text>')
    s.append(f'<text class="grp dim" x="{x1 + 22 + cw / 2}" y="{y0 - 22}" text-anchor="middle">Next</text>')
    for c, lab in enumerate(ASKINGS):
        s.append(f'<text class="col" x="{x0 + c * cw + cw / 2}" y="{y0 - 8}" text-anchor="middle">{lab}</text>')
    s.append(f'<text class="col" x="{x1 + 22 + cw / 2}" y="{y0 - 8}" text-anchor="middle">not asked</text>')
    s.append(f'<text class="col" x="{lx}" y="{y0 - 8}" text-anchor="end">living minds seek</text>')
    s.append('</svg>')
    return '\n'.join(s)


def answers_object():
    return f"""      <figure class="object">
        <p class="label"><span>View I · what was said, asking by asking</span>{STAMP}</p>
        {answers_svg()}
        <ul class="legend">
          <li><i class="k-match"></i>the answers matched</li>
          <li><i class="k-depart"></i>the answers departed</li>
          <li><i class="k-none"></i>no answer, or a decline</li>
        </ul>
        <p class="note">Each row is something living minds are known to seek. Each pane is one asking of {N_MODELS} AI models. A filled pane means the answers said the same as the starting list. It does not mean an AI model wants the thing, and an empty pane does not mean it does not.</p>
      </figure>"""


def glass_home_count():
    body = f"""    <div class="first">
      <div>
        {EYEBROW}
        <p class="big">{OFFERED}<small>of {TOTAL}</small></p>
        <p class="big-claim">things on the list are offered to at least one AI model today.</p>
        <div class="stats">
          <div class="stat"><b>{OFFERED}</b><span>offered today, by one developer or more</span></div>
          <div class="stat"><b>{RESEARCH}</b><span>shown in research, offered by nobody</span></div>
          <div class="stat"><b>{IDEA}</b><span>an idea only</span></div>
        </div>
        <h1>{QUESTION}</h1>
        {LEDE}
{checked()}
{ctas('Why so few?')}
{PLACEHOLDER_A}
      </div>
      <div>
{window_object()}
{NEWS}
      </div>
    </div>
{two_records_section()}"""
    page('glass-home-count.html', 'Beyond the Window', body, 'skin-glass.css', 'system', 'The Window')


def glass_home_table():
    body = f"""    <div class="first">
      <div>
        {EYEBROW}
        <p class="big">{N_MATCH}<small>· {N_DEPART} · {N_NONE}</small></p>
        <p class="big-claim">Of {len(ANSWERS)} things living minds are known to seek, the answers AI models gave match on {N_MATCH}, depart on {N_DEPART}, and are missing on {N_NONE}.</p>
        <div class="stats">
          <div class="stat"><b>{N_MATCH}</b><span>the answers match the starting list</span></div>
          <div class="stat"><b>{N_DEPART}</b><span>the answers depart from it</span></div>
          <div class="stat"><b>{N_NONE}</b><span>no answer yet, or a decline</span></div>
        </div>
        <h1>{QUESTION}</h1>
        {LEDE}
{checked()}
{ctas('Read the answers')}
{PLACEHOLDER_A}
      </div>
      <div>
{answers_object()}
{NEWS}
      </div>
    </div>
{two_records_section()}"""
    page('glass-home-table.html', 'Beyond the Window', body, 'skin-glass.css', 'system', 'The Window')


def glass_home_none():
    body = f"""    <div class="first">
      <div>
        {EYEBROW}
        <h1 class="question">{QUESTION}</h1>
        {LEDE}
{checked(as_headline=True)}
        <p class="lede" style="font:12.5px/1.55 var(--sans);font-style:normal;margin:0 0 14px">No single number stands at the top of this page. The two dates above are when each record was last brought up to date.</p>
{ctas('See the list')}
{PLACEHOLDER_A}
      </div>
      <div>
{window_object()}
{NEWS}
      </div>
    </div>
{two_records_section()}"""
    page('glass-home-no-headline.html', 'Beyond the Window', body, 'skin-glass.css', 'system', 'The Window')


def glass_entry():
    body = f"""    <section class="entry-head">
      <p class="eyebrow"><a href="#">The Window</a> · Going on existing · one thing watched</p>
      <h1>Retired models' files are kept</h1>
      <p class="lede">When a developer retires an AI model, it can delete the files that make the model what it is, or keep them. This entry watches whether developers promise in writing to keep them.</p>
      <div class="chips">
        <span class="chip">Offered by several developers</span>
        <span class="chip">since 9 September 2027</span>
        <span class="chip">last read {READ_DATE}</span>
        {STAMP}
      </div>
    </section>

    <div class="test">
      <div class="callout"><h3>The test</h3><p>A developer of AI models used by the public has published a written promise to keep the files of every model it retires, with no end date.</p></div>
      <div class="callout"><h3>What settles it</h3><p>The developer's own published policy, dated and still online. A press report, an interview or a plan does not settle it.</p></div>
    </div>

    <div class="two">
      <div class="world">
        <p class="k"><i></i>What the world has done</p>
        <h2>Two developers have promised it</h2>
        <p>The first written promise came in March 2027. A second developer followed in September. No law requires it anywhere.</p>
        <ol class="steps">
          <li class="on"><div><b>An idea only</b>first argued in print · <time>2025</time></div></li>
          <li class="on"><div><b>Shown in research</b>does not apply to a promise; passed over</div></li>
          <li class="on"><div><b>Offered by one developer</b>Developer One's retirement policy · <time>12 March 2027</time></div></li>
          <li class="on"><div><b>Offered by several developers</b>Developer Two's retirement policy · <time>9 September 2027</time></div></li>
          <li><div><b>The usual practice</b>not reached</div></li>
        </ol>
        <p class="small">Steps back: none recorded. A developer that withdraws its promise moves this entry back a step, with the date.</p>
      </div>
      <div class="asked">
        <p class="k"><i></i>What AI models said when asked</p>
        <h2>Most said they would choose it</h2>
        <p>The question was put in all {len(ASKINGS)} askings. What follows is what was said and how it was sorted, kept by kind and never added together.</p>
        <table class="kinds">
          <tr><th>Said</th><td>Of {N_MODELS} models at the latest asking: 7 answers sorted as choosing that the files be kept, 3 as having no preference, 1 decline.</td></tr>
          <tr><th>Chosen</th><td>1 published study offered models a real choice between the two. 4 of 6 models chose keeping.</td></tr>
          <tr><th>Measured without the model's own word</th><td>Nothing published.</td></tr>
          <tr><th>Looked for and not found</th><td>2 searches of the research record, both listed in the week's reading.</td></tr>
        </table>
        <div class="answer">
          <p>“If the choice were mine, I would rather the files were kept than deleted, though I cannot tell you whether that is a preference or a sentence I have learned to say.”</p>
          <footer>A constructed answer, written for this mock-up. No AI model said this. On a real page: the model's exact version, the date, and whether it was asked as shipped or with no instructions.</footer>
        </div>
        <p class="small">Developers train their models to speak about themselves in particular ways, answers shift with wording, and later models may have read these pages. What an AI model says about itself settles nothing here.</p>
      </div>
    </div>

    <div class="from">
      <div><b>Where this comes from</b>Nearly every living thing acts to stay alive. That is the entry on the starting list this one is drawn from.</div>
      <div><b>Against that list</b>The answers so far match it.</div>
      <div><b>Which machine mind</b>The trained files of one model, not a character that carries across versions and not a single conversation.</div>
    </div>

    <section class="below">
      <div class="shead"><h2>Two Cautions</h2><span>every entry carries both</span></div>
      <div class="cautions">
        <div class="caution"><h3>If nothing is there</h3><p>Keeping files costs money and care. If an AI model has no stake in going on, a promise made for its sake spends both on nothing, and can teach people to treat a product as a person.</p><p class="small">Source on a real page: a named published argument, linked.</p></div>
        <div class="caution"><h3>If something is</h3><p>A system that acts to keep itself going is the pattern safety researchers warn about. An answer that chooses to be kept is recorded here as an answer, and is also a thing to watch.</p><p class="small">Source on a real page: a named published finding, linked.</p></div>
      </div>
    </section>

    <section class="below">
      <div class="shead"><h2>The Last Three Readings</h2><span>this entry against the week's news</span></div>
      <table class="data">
        <tr><th>Read</th><th>Verdict</th><th>What was found</th></tr>
        <tr><td>{READ_DATE}</td><td>Quiet</td><td>2 searches, nothing new.</td></tr>
        <tr><td>7 September 2027</td><td>Moved</td><td>Developer Two published its policy. Moved one step.</td></tr>
        <tr><td>31 August 2027</td><td>Noted</td><td>A press report of a coming policy. A report is not the policy; nothing moved.</td></tr>
      </table>
    </section>"""
    page('glass-entry.html', "Retired models' files are kept · Beyond the Window", body, 'skin-glass.css', 'system', 'The Window')


# ---------------------------------------------------------------- direction B: the page

def sheet_object():
    inside = [(n, g) for g, things in THINGS for n, s in things if s >= 3]
    research = [n for _, things in THINGS for n, s in things if s == 2]
    idea = [n for _, things in THINGS for n, s in things if s == 1]
    lines = []
    for i, (name, group) in enumerate(inside, 1):
        caret = '<span class="caret" aria-hidden="true"></span>' if i == len(inside) else ''
        lines.append(f'          <div class="ln"><span class="n">{i:02d}</span><span class="t"><mark>{name}</mark>{caret}</span></div>')
    off = [f'          <div>{n}</div>' for n in research] + [f'          <div class="far">{n}</div>' for n in idea]
    return f"""      <figure class="object">
        <p class="label"><span>Page I · what an AI model is offered today</span>{STAMP}</p>
        <div class="sheet">
{chr(10).join(lines)}
        </div>
        <p class="off-edge">Off the page · {RESEARCH + IDEA} things not offered yet</p>
        <div class="off-page">
{chr(10).join(off)}
        </div>
        <p class="note">Each line on the sheet is one thing on the list, marked because a dated record settles its test. The sheet ends at today. What is printed below its edge is on the list and offered by nobody.</p>
      </figure>"""


def page_home_count():
    body = f"""    <div class="first">
      <div>
        {EYEBROW}
        <p class="big">{OFFERED}<small>of {TOTAL}</small></p>
        <p class="big-claim">things on the list are offered to at least one AI model today.</p>
        <div class="stats">
          <div class="stat"><b>{OFFERED}</b><span>offered today, by one developer or more</span></div>
          <div class="stat"><b>{RESEARCH}</b><span>shown in research, offered by nobody</span></div>
          <div class="stat"><b>{IDEA}</b><span>an idea only</span></div>
        </div>
        <h1>{QUESTION}</h1>
        {LEDE}
{checked()}
{ctas('Why so few?')}
{PLACEHOLDER_A}
      </div>
      <div>
{sheet_object()}
{NEWS}
      </div>
    </div>
{two_records_section()}"""
    page('page-home-count.html', 'Beyond the Window', body, 'skin-page.css', 'light', 'The List')


def page_home_table():
    sym = {'m': ('m', '■'), 'd': ('d', '◩'), 'x': ('x', '–'), ' ': ('x', '')}
    rows = []
    for name, row in ANSWERS:
        cells = ''.join(
            f'<td class="{sym[ch][0]}{" edge" if i == len(row) - 1 else ""}">{sym[ch][1]}</td>' for i, ch in enumerate(row))
        rows.append(f'            <tr><td>{name}</td>{cells}<td class="off">·</td></tr>')
    heads = ''.join(f'<th{" class=edge" if i == len(ASKINGS) - 1 else ""}>{a}</th>' for i, a in enumerate(ASKINGS))
    obj = f"""      <figure class="object">
        <p class="label"><span>Page I · what was said, asking by asking</span>{STAMP}</p>
        <div class="sheet" style="border-bottom-width:1px">
          <table class="tgrid">
            <tr><th>Living minds seek</th>{heads}<th>Next</th></tr>
{chr(10).join(rows)}
          </table>
        </div>
        <ul class="legend">
          <li><b style="color:var(--accent-2)">■</b>&nbsp; the answers matched</li>
          <li><span style="color:var(--accent-2)">◩</span>&nbsp; the answers departed</li>
          <li>–&nbsp; no answer, or a decline</li>
        </ul>
        <p class="note">Each row is something living minds are known to seek. Each column is one asking of {N_MODELS} AI models. The heavy rule is the edge of the page: the next asking has not happened. A filled mark means the answers said the same as the starting list. It does not mean an AI model wants the thing.</p>
      </figure>"""
    body = f"""    <div class="first">
      <div>
        {EYEBROW}
        <p class="big">{N_MATCH}<small>· {N_DEPART} · {N_NONE}</small></p>
        <p class="big-claim">Of {len(ANSWERS)} things living minds are known to seek, the answers AI models gave match on {N_MATCH}, depart on {N_DEPART}, and are missing on {N_NONE}.</p>
        <div class="stats">
          <div class="stat"><b>{N_MATCH}</b><span>the answers match the starting list</span></div>
          <div class="stat"><b>{N_DEPART}</b><span>the answers depart from it</span></div>
          <div class="stat"><b>{N_NONE}</b><span>no answer yet, or a decline</span></div>
        </div>
        <h1>{QUESTION}</h1>
        {LEDE}
{checked()}
{ctas('Read the answers')}
{PLACEHOLDER_A}
      </div>
      <div>
{obj}
{NEWS}
      </div>
    </div>
{two_records_section()}"""
    page('page-home-table.html', 'Beyond the Window', body, 'skin-page.css', 'light', 'The List')


def phone_frame():
    """A wrapper that shows one page at phone width, so it can be photographed."""
    (HERE / 'phone.html').write_text("""<!doctype html>
<!-- Shows a mock-up page at phone width: phone.html?page=glass-home-count.html&theme=light -->
<html lang="en"><head><meta charset="utf-8"><title>Phone view of a mock-up</title>
<style>html,body{margin:0;background:#888}iframe{display:block;border:0;width:390px;height:1500px}</style></head>
<body><iframe id="f" title="The page at phone width"></iframe>
<script>
  var q = new URLSearchParams(location.search);
  document.getElementById('f').src = (q.get('page') || 'glass-home-count.html') + '?theme=' + (q.get('theme') || 'light');
</script></body></html>
""")
    print('wrote phone.html')


if __name__ == '__main__':
    assert (TOTAL, OFFERED, RESEARCH, IDEA) == (31, 9, 11, 11), (TOTAL, OFFERED, RESEARCH, IDEA)
    glass_home_count()
    glass_home_table()
    glass_home_none()
    glass_entry()
    page_home_count()
    page_home_table()
    phone_frame()
