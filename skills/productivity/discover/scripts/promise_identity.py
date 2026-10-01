#!/usr/bin/env python3
"""Read exact UTF-8 promise bytes without normalization; never write the source."""
import argparse
import hashlib
from pathlib import Path


def promise_identity(path: Path) -> str:
    data = path.read_bytes()
    data.decode('utf-8')
    return 'promise:sha256:' + hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('promise', type=Path)
    args = parser.parse_args()
    try:
        print(promise_identity(args.promise))
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f'error: {exc}\n')


if __name__ == '__main__':
    main()
