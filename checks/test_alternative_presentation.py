from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AlternativePresentationTests(unittest.TestCase):
    def test_protocol_requires_simple_options_and_recommendation(self) -> None:
        text = (ROOT / "docs/discovery-protocol.md").read_text(encoding="utf-8")
        self.assertIn("## Present alternatives for a human", text)
        self.assertIn("numbered or bulleted list", text)
        self.assertIn("**What it means:**", text)
        self.assertIn("**Why you might choose it:**", text)
        self.assertIn("**Main downside:**", text)
        self.assertIn("**Recommendation**", text)
        self.assertIn("never\nbecomes the human decision automatically", text)

    def test_user_facing_skills_repeat_the_rule(self) -> None:
        for skill in ("brainstorm", "decide", "discover"):
            with self.subTest(skill=skill):
                text = (ROOT / f"skills/productivity/{skill}/SKILL.md").read_text(encoding="utf-8")
                self.assertIn("Recommendation", text)
                self.assertTrue("numbered or bulleted list" in text or "numbered/bulleted list" in text)
                self.assertIn("human decision", text)

    def test_evaluation_has_plain_alternatives_case(self) -> None:
        cases = json.loads((ROOT / "evaluations/cases.json").read_text(encoding="utf-8"))
        case = next(c for c in cases if c["id"] == "alternatives-plain-with-recommendation")
        rubric = " ".join(case["rubric"]).lower()
        self.assertIn("easy-to-scan list", rubric)
        self.assertIn("plain language", rubric)
        self.assertIn("recommendation", rubric)
        self.assertIn("advisory", rubric)


if __name__ == "__main__":
    unittest.main()
