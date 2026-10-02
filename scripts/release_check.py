#!/usr/bin/env python3
"""Cheap release consistency checks for Idea to Promise."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import sync_skill_resources as resources

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        print(f"ERROR: invalid VERSION: {version}", file=sys.stderr)
        return 1

    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"## {version}" not in changelog:
        print(f"ERROR: CHANGELOG has no {version} entry", file=sys.stderr)
        return 1

    errors = []
    for skill in resources.TEMPLATES:
        path = ROOT / "skills" / "productivity" / skill / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        if f'version: "{version}"' not in text:
            errors.append(f"{skill}: version mismatch")
    errors.extend(f"resource drift: {p}" for p in resources.sync(True))
    if errors:
        for error in errors:
            print("ERROR: " + error, file=sys.stderr)
        return 1

    print(f"RELEASE CHECK OK: {version}; live-agent quality NOT ASSESSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
