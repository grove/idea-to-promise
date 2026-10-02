#!/usr/bin/env python3
"""Read-only structural status for an Idea to Promise work item."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import check_work_item as cw
import promise_identity as pi


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def field(text: str, name: str) -> str | None:
    matches = re.findall(rf"^{re.escape(name)}:[ \t]*(.*?)[ \t]*$", text, re.M)
    if len(matches) != 1:
        return None
    value = matches[0].strip()
    return value or None


def inside(root: Path, path: Path) -> Path:
    resolved = path.resolve()
    if not resolved.is_relative_to(root):
        raise ValueError(f"path escapes project root: {path}")
    return resolved


def inspect(work: Path, root: Path, promise: Path | None) -> dict:
    work = inside(root, work)
    if not work.is_dir():
        raise ValueError(f"work item is not a directory: {work}")
    present = sorted(
        str(p.relative_to(work))
        for p in work.rglob("*")
        if p.is_file() and ".git" not in p.parts
    )
    result = {
        "work_item": str(work.relative_to(root)),
        "records": present,
        "mode": None,
        "decision": None,
        "promise": None,
        "handoff_errors": [],
        "next": None,
    }

    for name in ("session.md", "discovery.md"):
        p = work / name
        if p.is_file():
            mode = field(read_text(p), "Mode")
            if mode:
                result["mode"] = mode
                break

    decision_path = work / "decision.md"
    if decision_path.is_file():
        text = read_text(decision_path)
        result["decision"] = {
            "id": field(text, "Decision ID"),
            "status": field(text, "Status"),
            "direction": field(text, "Direction"),
            "owner": field(text, "Decision owner"),
            "approver": field(text, "Promise approver"),
        }

    if promise is not None:
        promise = inside(root, promise)
        if not promise.is_file():
            raise ValueError(f"promise is not a file: {promise}")
        data = promise.read_bytes()
        text = data.decode("utf-8")
        result["promise"] = {
            "path": str(promise.relative_to(root)),
            "revision": field(text, "Promise revision"),
            "identity": pi.identity(data),
        }
        if (work / "handoff.md").exists() or (work / "approval.md").exists():
            result["handoff_errors"] = cw.check(
                work, root, promise, handoff=(work / "handoff.md").exists()
            )

    decision = result["decision"] or {}
    direction = decision.get("direction")
    if (work / "amendment-proposed.md").is_file():
        result["next"] = "resolve proposed amendment without overwriting the active promise"
    elif direction in ("defer", "reject"):
        result["next"] = "terminal decision; revisit only if a trigger changes"
    elif not decision:
        if any((work / n).exists() for n in ("research.md", "alternatives.md", "discovery.md")):
            result["next"] = "record the missing human decision (/decide or /discover resume)"
        else:
            result["next"] = "continue discovery from the current need (/discover)"
    elif promise is None:
        result["next"] = "shape the selected direction into a source promise (/shape-promise)"
    elif not (work / "approval.md").is_file():
        result["next"] = "obtain attributable approval of the exact saved promise bytes"
    elif not (work / "handoff.md").is_file():
        result["next"] = "create and verify the P2P handoff record"
    elif result["handoff_errors"]:
        result["next"] = "repair handoff consistency before P2P"
    else:
        result["next"] = f"ready to propose /plan-acceptance {result['promise']['path']}"
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("work_item", type=Path)
    parser.add_argument("--promise", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        work = args.work_item if args.work_item.is_absolute() else root / args.work_item
        promise = args.promise
        if promise is not None and not promise.is_absolute():
            promise = root / promise
        result = inspect(work, root, promise)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"Work item: {result['work_item']}")
        print(f"Mode: {result['mode'] or 'not recorded'}")
        if result["decision"]:
            d = result["decision"]
            print(f"Decision: {d.get('id') or '?'} {d.get('status') or '?'} {d.get('direction') or '?'}")
        else:
            print("Decision: not recorded")
        if result["promise"]:
            p = result["promise"]
            print(f"Promise: {p['path']} {p.get('revision') or '?'} {p['identity']}")
        else:
            print("Promise: not supplied")
        if result["handoff_errors"]:
            print("Handoff: inconsistent")
            for error in result["handoff_errors"]:
                print(f"  - {error}")
        elif result["promise"] and (work / "handoff.md").exists():
            print("Handoff: structurally consistent")
        else:
            print("Handoff: not complete")
        print(f"Next: {result['next']}")
        print("Status is structural guidance, not product judgment or execution authority.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
