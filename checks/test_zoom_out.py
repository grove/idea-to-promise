from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ZoomOutTests(unittest.TestCase):
    def test_protocol_defines_zoom_out(self) -> None:
        text = (ROOT / "docs/discovery-protocol.md").read_text(encoding="utf-8")
        self.assertIn("## Zoom out to the bigger picture", text)
        self.assertIn("/discover zoom-out", text)
        self.assertIn("sunk cost", text.lower())
        self.assertIn("crowded out", text.lower())
        self.assertIn("does not itself supersede an active", text)

    def test_discover_recognizes_natural_zoom_out_intent(self) -> None:
        text = (ROOT / "skills/productivity/discover/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("For `zoom-out`", text)
        self.assertIn('"step back"', text)
        self.assertIn('"look at the bigger picture"', text)
        self.assertIn("End with one obvious human choice or next move", text)

    def test_zoom_out_template_and_session_activity_exist(self) -> None:
        template = (ROOT / "templates/zoom-out.md").read_text(encoding="utf-8")
        session = (ROOT / "templates/session.md").read_text(encoding="utf-8")
        self.assertIn("## What still matters most", template)
        self.assertIn("## What may deserve less attention", template)
        self.assertIn("## What we may be missing", template)
        self.assertIn("## Recommendation", template)
        self.assertIn("zoom-out", session)

    def test_evaluation_has_zoom_out_case(self) -> None:
        cases = json.loads((ROOT / "evaluations/cases.json").read_text(encoding="utf-8"))
        case = next(c for c in cases if c["id"] == "zoom-out-bigger-picture")
        rubric = " ".join(case["rubric"]).lower()
        self.assertIn("project-level zoom-out", rubric)
        self.assertIn("sunk effort", rubric)
        self.assertIn("recommendation", rubric)
        self.assertIn("preserves the active decision and promise", rubric)


if __name__ == "__main__":
    unittest.main()
