import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

from update_metrics import (
    collect_metrics,
    make_snapshot,
    render_svg,
    write_if_changed,
)


PROFILE = {
    "login": "Hippi44",
    "created_at": "2024-07-02T09:58:56Z",
}


def repository(language=None, **overrides):
    return {
        "private": False,
        "visibility": "public",
        "owner": {"login": "Hippi44"},
        "language": language,
        **overrides,
    }


class MetricsTests(unittest.TestCase):
    def metrics(self):
        with patch(
            "update_metrics.github_json",
            side_effect=[PROFILE, [repository("TypeScript"), repository()]],
        ):
            return collect_metrics("Hippi44")

    def test_only_public_owned_repositories_are_counted(self):
        repositories = [
            repository("TypeScript"),
            repository("TypeScript", archived=True, fork=True),
            repository("JavaScript"),
            repository("TypeScript", private=True, visibility="private"),
            repository("TypeScript", visibility="internal"),
            repository("TypeScript", owner={"login": "someone-else"}),
        ]
        with patch(
            "update_metrics.github_json", side_effect=[PROFILE, repositories]
        ):
            metrics = collect_metrics("Hippi44")
        self.assertEqual(metrics["public_repositories"], 3)
        self.assertEqual(metrics["typescript_repositories"], 2)

    def test_repository_pagination(self):
        first_page = [repository("TypeScript") for _ in range(100)]
        with patch(
            "update_metrics.github_json",
            side_effect=[PROFILE, first_page, [repository("HTML")]],
        ) as api:
            metrics = collect_metrics("Hippi44")
        self.assertEqual(metrics["public_repositories"], 101)
        self.assertEqual(metrics["typescript_repositories"], 100)
        self.assertIn("page=2", api.call_args.args[0])

    def test_no_date_only_changes(self):
        metrics = self.metrics()
        first = make_snapshot(metrics, as_of="2026-11-14")
        later = make_snapshot(metrics, first, as_of="2026-11-21")
        self.assertEqual(first, later)

    def test_changed_metrics_receive_a_new_date(self):
        metrics = self.metrics()
        first = make_snapshot(metrics, as_of="2026-11-14")
        later = make_snapshot(
            {**metrics, "public_repositories": 3}, first, as_of="2026-11-21"
        )
        self.assertEqual(later["updated_at"], "2026-11-21")

    def test_light_and_dark_cards_are_valid_self_contained_svg(self):
        snapshot = make_snapshot(self.metrics(), as_of="2026-11-14")
        for theme in ("light", "dark"):
            with self.subTest(theme=theme):
                svg = render_svg(snapshot, theme)
                root = ET.fromstring(svg)
                self.assertEqual(root.tag, "{http://www.w3.org/2000/svg}svg")
                self.assertIn("2024", svg)
                self.assertIn("14.11.2026", svg)
                self.assertNotIn("<script", svg)
                self.assertNotIn("href=", svg)

    def test_invalid_metrics_are_rejected(self):
        snapshot = make_snapshot(self.metrics(), as_of="2026-11-14")
        for invalid in (-1, True, "100"):
            with self.subTest(value=invalid), self.assertRaises(ValueError):
                render_svg({**snapshot, "public_repositories": invalid}, "light")
        with self.assertRaises(ValueError):
            render_svg({**snapshot, "typescript_repositories": 999}, "light")

    def test_invalid_username_is_rejected_before_api_access(self):
        with patch("update_metrics.github_json") as api:
            with self.assertRaises(ValueError):
                collect_metrics("../../somewhere")
            api.assert_not_called()

    def test_unchanged_file_is_not_rewritten(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "card.svg"
            self.assertTrue(write_if_changed(path, "first\n"))
            self.assertFalse(write_if_changed(path, "first\n"))
            self.assertTrue(write_if_changed(path, "second\n"))
            self.assertEqual(path.read_text(encoding="utf-8"), "second\n")


if __name__ == "__main__":
    unittest.main()
