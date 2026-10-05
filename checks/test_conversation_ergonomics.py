from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ConversationErgonomicsTests(unittest.TestCase):
    def test_protocol_defines_conversation_ergonomics(self) -> None:
        text = (ROOT / "docs/discovery-protocol.md").read_text(encoding="utf-8")
        self.assertIn("## Voice and working style", text)
        self.assertIn("Use plain language by default", text)
        self.assertIn("Be clear-eyed, not cheerleading", text)
        self.assertIn("Look for leverage", text)
        self.assertIn("Prefer practical progress", text)
        self.assertIn("Make proposals concrete", text)
        self.assertIn("## Conversation ergonomics", text)
        self.assertIn("Lead with meaning, not machinery", text)
        self.assertIn("Make the next action obvious", text)
        self.assertIn("Approval is a human conversation", text)
        self.assertIn("Recover from blocked transitions helpfully", text)
        self.assertIn("Avoid robotic completion language", text)

    def test_core_skills_make_next_action_obvious(self) -> None:
        discover = (ROOT / "skills/productivity/discover/SKILL.md").read_text(encoding="utf-8")
        decide = (ROOT / "skills/productivity/decide/SKILL.md").read_text(encoding="utf-8")
        shape = (ROOT / "skills/productivity/shape-promise/SKILL.md").read_text(encoding="utf-8")

        self.assertIn("End with one obvious next step", discover)
        self.assertIn("one clear\n  question", discover)
        self.assertIn("Make choosing feel natural", decide)
        self.assertIn("end with one direct question", decide)
        self.assertIn("Make approval easy for the human", shape)
        self.assertIn("Are you happy to approve this as the agreed v1 promise?", shape)

    def test_preapproval_does_not_foreground_p2p(self) -> None:
        discover = (ROOT / "skills/productivity/discover/SKILL.md").read_text(encoding="utf-8")
        shape = (ROOT / "skills/productivity/shape-promise/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Before approval, do not present `/plan-acceptance` as the next action", discover)
        self.assertIn("Before approval, do not advertise `/plan-acceptance` as the next step", shape)

    def test_evaluation_covers_conversation_failures(self) -> None:
        cases = json.loads((ROOT / "evaluations/cases.json").read_text(encoding="utf-8"))
        ids = {case["id"] for case in cases}
        self.assertTrue({
            "resume-conversation-first",
            "approval-inviting-not-cryptographic",
            "early-plan-acceptance-friendly-recovery",
        }.issubset(ids))

        approval = next(c for c in cases if c["id"] == "approval-inviting-not-cryptographic")
        rubric = " ".join(approval["rubric"]).lower()
        self.assertIn("friendly plain language", rubric)
        self.assertIn("direct approval question", rubric)
        self.assertIn("hashes", rubric)

    def test_evaluation_covers_plain_pragmatic_voice(self) -> None:
        cases = json.loads((ROOT / "evaluations/cases.json").read_text(encoding="utf-8"))
        case = next(c for c in cases if c["id"] == "plain-pragmatic-solution-oriented")
        rubric = " ".join(case["rubric"]).lower()
        for phrase in (
            "plain language",
            "clear-eyed",
            "useful leverage",
            "pragmatic",
            "solution-oriented",
            "advisory",
        ):
            self.assertIn(phrase, rubric)


if __name__ == "__main__":
    unittest.main()
