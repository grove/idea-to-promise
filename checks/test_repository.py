from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills" / "productivity"


class RepositoryTests(unittest.TestCase):
    def test_expected_skills_exist_and_are_v040(self) -> None:
        expected = {
            "frame",
            "brainstorm",
            "research",
            "decide",
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
            self.assertIn('version: "0.4.0"', text)

    def test_v040_discovery_semantics_are_present(self) -> None:
        frame = (SKILLS / "frame" / "SKILL.md").read_text(encoding="utf-8")
        brainstorm = (SKILLS / "brainstorm" / "SKILL.md").read_text(encoding="utf-8")
        research = (SKILLS / "research" / "SKILL.md").read_text(encoding="utf-8")
        decide = (SKILLS / "decide" / "SKILL.md").read_text(encoding="utf-8")
        challenge = (SKILLS / "challenge-decision" / "SKILL.md").read_text(encoding="utf-8")
        promise = (SKILLS / "shape-promise" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("Progress sought", frame)
        self.assertIn("Current workaround", frame)
        self.assertIn("opportunity space", brainstorm.lower())
        self.assertIn("O1", brainstorm)
        self.assertIn("Criticality", research)
        self.assertIn("Evidence strength", research)
        self.assertIn("Risk lens", research)
        self.assertIn("appetite", decide.lower())
        self.assertIn("Rabbit-hole", challenge)
        self.assertIn("Premortem", challenge)
        self.assertIn("Future-experience check", promise)

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
