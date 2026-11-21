#!/usr/bin/env python3
"""Tests for scripts/check_news.py and the news part of scripts/check_site.py (rule 14).
Run: python3 scripts/test_news.py

Added 2026-11-21 with the news section, in the form of The Upgrade Tree's scripts/test_news.py and
Outrunning Ageing's scripts/test_news_photos.py. Every post and record in this file is a
constructed example, made up to exercise a rule. None is real, and none describes anything any
developer does.
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_news as n  # noqa: E402
import check_site as s  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "news"

# A constructed record: one entry with a change on 2026-11-10, and one act on another entry.
WINDOW = {
    "entries": [
        {"id": "a-made-up-thing", "added": "2026-01-05", "state": {"set_on": "2026-01-05"},
         "history": [{"date": "2026-11-10"}], "checks": {"against_sources": "2026-01-05"}},
        {"id": "another-made-up-thing", "added": "2026-01-05", "state": {"set_on": "2026-01-05"},
         "history": [], "checks": None},
    ],
    "headline": {"readings": {"acts": [{"entry": "another-made-up-thing", "date": "2026-06"}]}},
}

GOOD = """---
title: "A constructed post"
date: {date}
kind: {kind}
summary: "Constructed for a test."
records: [{records}]
sources:
  - label: "A constructed source"
    url: https://example.org/
---

A constructed paragraph with no figures.

A constructed paragraph with a figure, 3, and [its source](https://example.org/).
"""


def post(date: str = "2026-11-12", kind: str = "state-changed", records: str = "a-made-up-thing",
         extra: str = "", body: str = "") -> str:
    text = GOOD.format(date=date, kind=kind, records=records)
    if extra:
        text = text.replace("---\n\n", extra + "\n---\n\n", 1)
    return text + body


class NewsCheck(unittest.TestCase):
    def run_check(self, files: dict[str, str], published: bool = False) -> list[str]:
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)
            for name, text in files.items():
                (folder / name).write_text(text, encoding="utf-8")
            if published:
                saved = n.PUBLISHED
                n.PUBLISHED = folder
                try:
                    return n.check(folder, WINDOW, pictures_dir=None)[0]
                finally:
                    n.PUBLISHED = saved
            return n.check(folder, WINDOW, pictures_dir=None)[0]

    def test_a_good_post_passes(self):
        self.assertEqual(self.run_check({"2026-11-12-a-good-post.md": post()}), [])

    def test_file_name_and_date(self):
        self.assertTrue(self.run_check({"a-post.md": post()}))
        self.assertTrue(self.run_check({"2026-11-13-a-post.md": post()}))

    def test_kind_outside_the_six(self):
        self.assertTrue(self.run_check({"2026-11-12-a-post.md": post(kind="rung-reached")}))

    def test_names_no_entry_or_a_missing_one(self):
        self.assertTrue(self.run_check({"2026-11-12-a-post.md": post(records="")}))
        self.assertTrue(self.run_check({"2026-11-12-a-post.md": post(records="no-such-thing")}))

    def test_story_and_opener_need_no_entry(self):
        self.assertEqual(self.run_check({"2026-11-12-a-post.md": post(kind="story", records="")}), [])
        self.assertEqual(self.run_check({"2026-11-12-a-post.md": post(kind="start-here", records="")}), [])

    def test_story_carries_no_before_and_after(self):
        bad = post(kind="story", records="", extra='before: "1"\nafter: "2"')
        self.assertTrue(self.run_check({"2026-11-12-a-post.md": bad}))

    def test_one_opener(self):
        two = {"2026-11-12-a.md": post(kind="start-here", records=""),
               "2026-11-13-b.md": post(date="2026-11-13", kind="start-here", records="")}
        self.assertTrue(self.run_check(two))

    def test_no_source(self):
        bad = post().replace("url: https://example.org/", "url: http://example.org/")
        self.assertTrue(self.run_check({"2026-11-12-a-post.md": bad}))

    def test_figure_with_no_link(self):
        bad = post(body="\nA constructed paragraph with a bare figure, 12.\n")
        self.assertTrue(self.run_check({"2026-11-12-a-post.md": bad}))

    def test_entry_shows_no_change_near_the_post(self):
        # a-made-up-thing changed on 2026-11-10: a post on 2026-11-24 is inside fourteen days,
        # one on 2026-11-25 is not.
        self.assertEqual(self.run_check({"2026-11-24-a-post.md": post(date="2026-11-24")}), [])
        self.assertTrue(self.run_check({"2026-11-25-a-post.md": post(date="2026-11-25")}))

    def test_an_act_counts_as_a_change_from_its_first_day(self):
        ok = post(date="2026-06-10", records="another-made-up-thing")
        self.assertEqual(self.run_check({"2026-06-10-a-post.md": ok}), [])
        late = post(date="2026-07-20", records="another-made-up-thing")
        self.assertTrue(self.run_check({"2026-07-20-a-post.md": late}))

    def test_constructed_post_refused_only_where_the_site_publishes_from(self):
        made_up = post(extra="constructed: true")
        self.assertEqual(self.run_check({"2026-11-12-a-post.md": made_up}), [])
        problems = self.run_check({"2026-11-12-a-post.md": made_up}, published=True)
        self.assertTrue(any("constructed" in p for p in problems))

    def test_picture_rules(self):
        bare = post(body='\n<img src="/news/a.jpg" alt="A constructed picture">\n')
        self.assertTrue(self.run_check({"2026-11-12-a-post.md": bare}))
        unlisted = post(body='\n<figure><img src="/news/a.jpg" alt="x"><figcaption>A caption</figcaption></figure>\n')
        self.assertTrue(self.run_check({"2026-11-12-a-post.md": unlisted}))

    def test_the_fixtures_pass_outside_the_published_folder(self):
        import json
        window = json.loads((Path(__file__).resolve().parent.parent / "site" / "src" / "data" / "window.json").read_text())
        problems, count = n.check(FIXTURES, window, pictures_dir=None)
        self.assertEqual(problems, [])
        self.assertEqual(count, 3)


class SiteRule14(unittest.TestCase):
    def build(self, pages: dict[str, str], feed_items: int | None) -> list[str]:
        with tempfile.TemporaryDirectory() as d:
            dist = Path(d)
            for rel, text in pages.items():
                f = dist / rel.lstrip("/") / "index.html"
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_text(text, encoding="utf-8")
            if feed_items is not None:
                (dist / "news").mkdir(exist_ok=True)
                (dist / "news" / "feed.xml").write_text("<rss>" + "<item></item>" * feed_items + "</rss>")
            return s.news_problems(dist, sorted(dist.rglob("*.html")))

    def test_feed_matches_post_pages(self):
        pages = {"/news/": "<p>News</p>", "/news/2026-11-12-a/": "<p>A post</p>"}
        self.assertEqual(self.build(pages, 1), [])
        self.assertTrue(self.build(pages, 0))
        self.assertTrue(self.build(pages, None))

    def test_constructed_post_refused(self):
        pages = {"/news/": "<p>News</p>",
                 "/news/2026-11-12-a/": '<p class="constructed-post">Constructed example</p>'}
        self.assertTrue(self.build(pages, 1))


if __name__ == "__main__":
    unittest.main(verbosity=1)
