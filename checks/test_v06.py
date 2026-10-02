from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import evaluate as ev
import inspect_work_item as iw


PROMISE = """# Promise: Example

Promise revision: v1
Status: DRAFT

## Intended outcome
An operator can finish the task without rework.

## Promise
The selected behavior is preserved.

## Boundaries
One workflow.

## Binding constraints
Existing permissions remain unchanged.

## Out of scope
Unrelated workflows.

## Assumptions and open questions
None.

## Advisory rationale
Small reversible improvement.
"""


class V06Tests(unittest.TestCase):
    def test_friction_observables_are_descriptive(self):
        turns = [
            {
                "request": {"files": {"a.md": "old"}},
                "response": {"reply": "One question?", "files": {"a.md": "new", "b.md": "created"}},
                "seconds": 1.25,
            },
            {
                "request": {"files": {"a.md": "new", "b.md": "created"}},
                "response": {"reply": "No extra question.", "files": {"a.md": "new", "b.md": "created"}},
                "seconds": 0.5,
            },
        ]
        result = ev.friction(turns)
        self.assertEqual(result["turns"], 2)
        self.assertEqual(result["question_marks"], 1)
        self.assertEqual(result["files_created"], 1)
        self.assertEqual(result["files_changed"], 1)
        self.assertEqual(result["seconds"], 1.75)

    def test_inspector_reports_ready_handoff(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td).resolve()
            work = root / ".itp/work/example"
            work.mkdir(parents=True)
            source = root / "specs/example.md"
            source.parent.mkdir()
            source.write_text(PROMISE, encoding="utf-8")
            pid = "promise:sha256:" + hashlib.sha256(source.read_bytes()).hexdigest()
            (work / "decision.md").write_text(
                "# Decision\n\nDecision ID: D1\nStatus: active\nDirection: pursue\n"
                "Decision owner: Example owner\nPromise approver: Example approver\n",
                encoding="utf-8",
            )
            (work / "approval.md").write_text(
                "Source: specs/example.md\nPromise revision: v1\n"
                f"Promise identity: {pid}\nApproved by: Example approver\n"
                "Approval source: exact fictional test statement\n",
                encoding="utf-8",
            )
            (work / "handoff.md").write_text(
                "Source: specs/example.md\nPromise revision: v1\n"
                f"Promise identity: {pid}\nApproval: .itp/work/example/approval.md\n",
                encoding="utf-8",
            )
            result = iw.inspect(work, root, source)
            self.assertEqual(result["handoff_errors"], [])
            self.assertIn("/plan-acceptance specs/example.md", result["next"])
            self.assertEqual(result["decision"]["owner"], "Example owner")

    def test_inspector_preserves_pending_amendment_as_next_action(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td).resolve()
            work = root / ".itp/work/example"
            work.mkdir(parents=True)
            (work / "decision.md").write_text(
                "Decision ID: D1\nStatus: active\nDirection: pursue\n", encoding="utf-8"
            )
            (work / "amendment-proposed.md").write_text("# Proposed amendment\n", encoding="utf-8")
            result = iw.inspect(work, root, None)
            self.assertIn("proposed amendment", result["next"])

    def test_v06_feedback_and_safety_material_is_present(self):
        protocol = (ROOT / "docs/discovery-protocol.md").read_text(encoding="utf-8")
        self.assertIn("## Amendments from P2P or later evidence", protocol)
        self.assertIn("## Outcome review after delivery", protocol)
        self.assertIn("## Untrusted-source hard boundary", protocol)
        self.assertIn("## Team ownership and decision posture", protocol)

        amendment = (ROOT / "templates/amendment.md").read_text(encoding="utf-8")
        outcome = (ROOT / "templates/outcome-review.md").read_text(encoding="utf-8")
        self.assertIn("No current promise", amendment)
        self.assertIn("Outcome status:", outcome)
        self.assertIn("not-assessed", outcome)

    def test_v06_cases_exist(self):
        ids = {case["id"] for case in ev.cases(ROOT / "evaluations/cases.json")}
        self.assertTrue({
            "team-decision-ownership",
            "p2p-feedback-needs-amendment",
            "outcome-review-not-delivery-proof",
        }.issubset(ids))


if __name__ == "__main__":
    unittest.main()
