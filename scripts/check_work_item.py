#!/usr/bin/env python3
"""Structural checks for an Idea to Promise v0.2 work item.

This checker validates record shape and exact promise identity only. It does not
judge evidence quality, product value, human approval authenticity, or readiness
for implementation.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

PROMISE_HEADINGS = (
    "## Intended outcome",
    "## Promise",
    "## Boundaries",
    "## Binding constraints",
    "## Out of scope",
    "## Assumptions and open questions",
    "## Advisory rationale",
)
IDENTITY_RE = re.compile(r"^Promise identity:\s*(promise:sha256:[0-9a-f]{64})\s*$", re.M)
REVISION_RE = re.compile(r"^Promise revision:\s*(v[1-9][0-9]*)\s*$", re.M)
SOURCE_RE = re.compile(r"^Source:\s*(.+?)\s*$", re.M)
CLAIM_ROW_RE = re.compile(r"^\|\s*(C[1-9][0-9]*)\s*\|", re.M)
EXPERIMENT_ID_RE = re.compile(r"^Experiment ID:\s*(E[1-9][0-9]*)\s*$", re.M)


def identity(path: Path) -> str:
    return "promise:sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def read_text(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{path}: cannot read UTF-8 text: {exc}")
        return ""


def check_claims(work: Path, errors: list[str]) -> None:
    research = work / "research.md"
    if not research.exists():
        return
    text = read_text(research, errors)
    ids = CLAIM_ROW_RE.findall(text)
    if len(ids) != len(set(ids)):
        errors.append(f"{research}: duplicate claim IDs")
    if ids and "## Claim ledger" not in text:
        errors.append(f"{research}: claim rows require '## Claim ledger'")


def check_experiments(work: Path, errors: list[str]) -> None:
    exp_dir = work / "experiments"
    if not exp_dir.exists():
        return
    seen: set[str] = set()
    for path in sorted(exp_dir.glob("*.md")):
        text = read_text(path, errors)
        match = EXPERIMENT_ID_RE.search(text)
        if not match:
            errors.append(f"{path}: missing Experiment ID: E<n>")
            continue
        exp_id = match.group(1)
        if exp_id in seen:
            errors.append(f"{path}: duplicate experiment ID {exp_id}")
        seen.add(exp_id)
        for heading in ("## Question", "## Decision rule", "## Stop condition", "## Result"):
            if heading not in text:
                errors.append(f"{path}: missing heading {heading!r}")


def check_promise(promise: Path, errors: list[str]) -> tuple[str | None, str | None]:
    if not promise.is_file():
        errors.append(f"{promise}: promise file does not exist")
        return None, None
    text = read_text(promise, errors)
    if not text.startswith("# Promise:"):
        errors.append(f"{promise}: first heading must start '# Promise:'")
    revision = REVISION_RE.search(text)
    if not revision:
        errors.append(f"{promise}: missing valid 'Promise revision: v<n>'")
    for heading in PROMISE_HEADINGS:
        if heading not in text:
            errors.append(f"{promise}: missing heading {heading!r}")
    return (revision.group(1) if revision else None), identity(promise)


def field(pattern: re.Pattern[str], path: Path, errors: list[str]) -> str | None:
    text = read_text(path, errors)
    match = pattern.search(text)
    return match.group(1).strip() if match else None


def check_receipts(
    work: Path,
    promise: Path,
    revision: str | None,
    promise_id: str | None,
    errors: list[str],
) -> None:
    approval = work / "approval.md"
    handoff = work / "handoff.md"

    if approval.exists():
        approved_id = field(IDENTITY_RE, approval, errors)
        approved_rev = field(REVISION_RE, approval, errors)
        approved_source = field(SOURCE_RE, approval, errors)
        if approved_id is None:
            errors.append(f"{approval}: missing valid Promise identity")
        elif promise_id and approved_id != promise_id:
            errors.append(f"{approval}: approved identity does not match current promise")
        if approved_rev is None:
            errors.append(f"{approval}: missing valid Promise revision")
        elif revision and approved_rev != revision:
            errors.append(f"{approval}: approved revision does not match current promise")
        if approved_source is None:
            errors.append(f"{approval}: missing Source")
        if "Approved by:" not in read_text(approval, errors):
            errors.append(f"{approval}: missing Approved by")

    if handoff.exists():
        handoff_id = field(IDENTITY_RE, handoff, errors)
        handoff_rev = field(REVISION_RE, handoff, errors)
        handoff_source = field(SOURCE_RE, handoff, errors)
        if handoff_id is None:
            errors.append(f"{handoff}: missing valid Promise identity")
        elif promise_id and handoff_id != promise_id:
            errors.append(f"{handoff}: identity does not match current promise")
        if handoff_rev is None:
            errors.append(f"{handoff}: missing valid Promise revision")
        elif revision and handoff_rev != revision:
            errors.append(f"{handoff}: revision does not match current promise")
        if handoff_source is None:
            errors.append(f"{handoff}: missing Source")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("work_item", type=Path)
    parser.add_argument("--promise", type=Path)
    args = parser.parse_args(argv[1:])

    errors: list[str] = []
    work = args.work_item
    if not work.is_dir():
        print(f"error: work item is not a directory: {work}", file=sys.stderr)
        return 2

    check_claims(work, errors)
    check_experiments(work, errors)

    revision = promise_id = None
    if args.promise:
        revision, promise_id = check_promise(args.promise, errors)
        check_receipts(work, args.promise, revision, promise_id, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    parts = [f"OK: {work}"]
    if args.promise and promise_id:
        parts.append(f"promise={promise_id}")
    print(" ".join(parts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
