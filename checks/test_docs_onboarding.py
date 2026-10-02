from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class OnboardingDocsTests(unittest.TestCase):
    def test_onboarding_docs_exist(self) -> None:
        expected = [
            "docs/README.md",
            "docs/getting-started.md",
            "docs/mental-model.md",
            "docs/cheatsheet.md",
            "docs/recipes/README.md",
            "docs/recipes/new-feature.md",
            "docs/recipes/technical-decision.md",
            "docs/recipes/experiment.md",
            "docs/recipes/no-build.md",
            "docs/recipes/resume.md",
            "docs/recipes/revisit.md",
            "docs/recipes/amend-from-p2p.md",
            "docs/recipes/outcome-review.md",
            "docs/reference/README.md",
        ]
        for name in expected:
            with self.subTest(name=name):
                self.assertTrue((ROOT / name).is_file())

    def test_readme_has_clear_front_door(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("/discover <your idea>", text)
        self.assertIn("You do not fill out ITP forms", text)
        self.assertIn("5-minute Getting Started guide", text)

    def test_getting_started_teaches_boundaries(self) -> None:
        text = (ROOT / "docs/getting-started.md").read_text(encoding="utf-8")
        lowered = text.lower()
        self.assertIn("you make the decision", lowered)
        self.assertIn("exact promise", lowered)
        self.assertIn("/plan-acceptance", text)
        self.assertIn("what if the answer is", lowered)
        self.assertIn("build promise", lowered)

    def test_mental_model_names_core_concepts(self) -> None:
        text = (ROOT / "docs/mental-model.md").read_text(encoding="utf-8")
        for word in ("Idea", "Evidence", "Decision", "Promise", "Proof"):
            self.assertIn(f"## {word}", text)


if __name__ == "__main__":
    unittest.main()
