#!/usr/bin/env python3
"""Contrast ratios for the two proposed skins, read from the skin files themselves.

    python3 docs/design/mockups/contrast.py

Prints one table per skin and theme, and exits with an error if any pair that
is used for text falls below 4.5 to 1 (the usual bar for ordinary text).
Colours written with an alpha value are skipped: they are rules and fills.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def lum(hexcol):
    h = hexcol.lstrip('#')
    rgb = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def tokens(css, light):
    blocks = re.findall(r"(:root(?:\[data-theme='light'\])?)\s*\{(.*?)\}", css, re.S)
    out = {}
    for sel, body in blocks:
        if ('light' in sel) != light:
            continue
        for name, val in re.findall(r"(--[\w-]+):\s*(#[0-9a-fA-F]{6})\b", body):
            out[name] = val
    return out


# (label, foreground token, background token, is it used for text)
PAIRS = [
    ('headings on the page', '--text', '--bg', True),
    ('running text on the page', '--text-soft', '--bg', True),
    ('captions on the page', '--muted', '--bg', True),
    ('captions on a card', '--muted', '--panel', True),
    ('links on the page', '--accent', '--bg', True),
    ('links on a card', '--accent', '--panel', True),
    ('button text on the button', '--on-accent', '--accent', True),
    ('second mark on the page', '--accent-2', '--bg', True),
    ('second mark on a card', '--accent-2', '--panel', True),
    ('data colour on the page', '--accent-3', '--bg', None),
    ('ink on the data colour', '--text', '--accent-3', None),
    ('yes mark on the page', '--ok', '--bg', True),
    ('no mark on the page', '--no', '--bg', True),
]

# Where the data colour carries text, per skin (see the proposal, section 4).
DATA_TEXT = {'skin-glass.css': 'data colour on the page', 'skin-page.css': 'ink on the data colour'}

failed = False
for skin in ('skin-glass.css', 'skin-page.css'):
    css = (HERE / skin).read_text()
    for light in (False, True):
        t = tokens(css, light)
        if light:
            base = tokens(css, False)
            base.update(t)
            t = base
        print(f"\n{skin} · {'light' if light else 'dark'}")
        for label, fg, bg, is_text in PAIRS:
            r = ratio(t[fg], t[bg])
            if is_text is None:
                # In the dark theme of Page the marker is a wash behind light text, checked in the proposal.
                is_text = DATA_TEXT[skin] == label and not (skin == 'skin-page.css' and not light)
            flag = ''
            if is_text and r < 4.5:
                flag = '  BELOW 4.5'
                failed = True
            elif not is_text:
                flag = '  (not used for text)'
            print(f"  {label:<28} {t[fg]} on {t[bg]}  {r:5.1f}{flag}")

sys.exit(1 if failed else 0)
