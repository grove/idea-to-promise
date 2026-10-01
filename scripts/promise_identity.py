#!/usr/bin/env python3
"""Print the exact-byte SHA-256 identity of a promise file."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path


def promise_identity(path: Path) -> str:
    return "promise:sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: promise_identity.py <promise.md>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    if not path.is_file():
        print(f"error: not a file: {path}", file=sys.stderr)
        return 2
    print(promise_identity(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
