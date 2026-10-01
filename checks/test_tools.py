from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDENTITY = ROOT / "scripts" / "promise_identity.py"
CHECKER = ROOT / "scripts" / "check_work_item.py"

PROMISE = """# Promise: Example

Promise revision: v1
Status: DRAFT

## Intended outcome
An observable result.

## Promise
The result will hold.

## Boundaries
- One boundary.

## Binding constraints
- One constraint.

## Out of scope
- One exclusion.

## Assumptions and open questions
- None.

## Advisory rationale
C1 supports the choice.
"""


class ToolTests(unittest.TestCase):
    def run_tool(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_identity_is_exact_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "promise.md"
            path.write_bytes(b"hello\n")
            result = self.run_tool(str(IDENTITY), str(path))
            expected = "promise:sha256:" + hashlib.sha256(b"hello\n").hexdigest()
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.strip(), expected)

    def test_checker_accepts_matching_approval_and_handoff(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            work = root / ".itp" / "work" / "example"
            work.mkdir(parents=True)
            promise = root / "specs" / "example.md"
            promise.parent.mkdir()
            promise.write_text(PROMISE, encoding="utf-8")
            pid = "promise:sha256:" + hashlib.sha256(promise.read_bytes()).hexdigest()
            receipt = (
                "# Promise approval: Example\n\n"
                "Source: specs/example.md\n"
                "Promise revision: v1\n"
                f"Promise identity: {pid}\n"
                "Approved by: Example User\n"
            )
            (work / "approval.md").write_text(receipt, encoding="utf-8")
            handoff = (
                "# Promise to Proof handoff: Example\n\n"
                "Source: specs/example.md\n"
                "Promise revision: v1\n"
                f"Promise identity: {pid}\n"
            )
            (work / "handoff.md").write_text(handoff, encoding="utf-8")
            result = self.run_tool(str(CHECKER), str(work), "--promise", str(promise))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(pid, result.stdout)

    def test_checker_rejects_promise_drift(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            work = root / ".itp" / "work" / "example"
            work.mkdir(parents=True)
            promise = root / "specs" / "example.md"
            promise.parent.mkdir()
            promise.write_text(PROMISE, encoding="utf-8")
            wrong = "promise:sha256:" + "0" * 64
            (work / "approval.md").write_text(
                "# Approval\n\n"
                "Source: specs/example.md\n"
                "Promise revision: v1\n"
                f"Promise identity: {wrong}\n"
                "Approved by: Example User\n",
                encoding="utf-8",
            )
            result = self.run_tool(str(CHECKER), str(work), "--promise", str(promise))
            self.assertEqual(result.returncode, 1)
            self.assertIn("does not match current promise", result.stderr)

    def test_checker_rejects_duplicate_claim_ids(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            work = Path(td) / "work"
            work.mkdir()
            (work / "research.md").write_text(
                "# Research\n\n## Claim ledger\n\n"
                "| ID | Kind | Claim |\n|---|---|---|\n"
                "| C1 | observation | one |\n"
                "| C1 | inference | two |\n",
                encoding="utf-8",
            )
            result = self.run_tool(str(CHECKER), str(work))
            self.assertEqual(result.returncode, 1)
            self.assertIn("duplicate claim IDs", result.stderr)


if __name__ == "__main__":
    unittest.main()
