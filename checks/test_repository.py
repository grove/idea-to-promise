from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills" / "productivity"


class RepositoryTests(unittest.TestCase):
    def test_expected_skills_exist_and_are_v020(self) -> None:
        expected = {
            "frame",
            "brainstorm",
            "research",
            "challenge-decision",
            "shape-promise",
            "discover",
        }
        actual = {p.name for p in SKILLS.iterdir() if (p / "SKILL.md").is_file()}
        self.assertEqual(actual, expected)
        for name in expected:
            text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"))
            self.assertIn(f"name: {name}\n", text)
            self.assertIn('version: "0.2.0"', text)

    def test_markdown_relative_links_resolve(self) -> None:
        pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            for target in pattern.findall(text):
                if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                    continue
                target = target.split("#", 1)[0]
                if not target or "<" in target or ">" in target:
                    continue
                resolved = (path.parent / target).resolve()
                self.assertTrue(resolved.exists(), f"{path}: broken link {target}")


if __name__ == "__main__":
    unittest.main()
