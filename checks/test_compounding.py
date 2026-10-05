from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import sync_skill_resources as resources


class CompoundingTests(unittest.TestCase):
    def test_compound_skill_is_packaged(self):
        self.assertIn("compound-learning", resources.TEMPLATES)
        text = (ROOT / "skills/productivity/compound-learning/SKILL.md").read_text(encoding="utf-8")
        self.assertIn(".itp/learnings/<slug>.md", text)
        self.assertIn("Automatic detection and local capture are allowed", text)
        self.assertIn("Compounding never creates a human decision", text)

    def test_behavioral_skills_can_invoke_compounding(self):
        names = {"frame", "brainstorm", "research", "decide", "challenge-decision", "shape-promise", "discover"}
        for name in names:
            with self.subTest(skill=name):
                text = (ROOT / f"skills/productivity/{name}/SKILL.md").read_text(encoding="utf-8")
                self.assertIn("invoke the `compound-learning` skill", text)
                self.assertIn("must not create or replace a human decision", text)

    def test_compounding_evaluation_cases_exist(self):
        cases = json.loads((ROOT / "evaluations/cases.json").read_text(encoding="utf-8"))
        ids = {case["id"] for case in cases}
        self.assertTrue({"compound-project-learning", "compound-shared-behavior-proposal"}.issubset(ids))


if __name__ == "__main__":
    unittest.main()
