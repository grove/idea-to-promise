#!/usr/bin/env python3
"""Preview or apply minimal ITP setup. No commits, network access, or spec creation."""
from __future__ import annotations
import argparse
import subprocess
from pathlib import Path


def git(root: Path, *args: str) -> str:
    proc = subprocess.run(['git', '-C', str(root), *args], capture_output=True, text=True, timeout=10)
    if proc.returncode:
        raise ValueError(proc.stderr.strip() or 'Git command failed')
    return proc.stdout


def plan(root: Path) -> tuple[bytes | None, bytes, list[str]]:
    if Path(git(root, 'rev-parse', '--show-toplevel').strip()).resolve() != root:
        raise ValueError('select the Git repository root, not a subdirectory')
    for name in ('.gitignore', '.itp', '.itp/work'):
        path = root / name
        if path.is_symlink():
            raise ValueError(f'refusing symlink: {name}')
        if path.exists() and (path.is_dir() if name == '.gitignore' else not path.is_dir()):
            raise ValueError(f'conflicting file type: {name}')
    if git(root, 'ls-files', '--', '.itp').strip():
        raise ValueError('.itp already contains tracked files; reconcile them explicitly first')
    path = root / '.gitignore'
    before = path.read_bytes() if path.exists() else None
    original = before or b''
    original.decode('utf-8')
    # An explicit trailing directory rule covers future contents as well as samples.
    lines = original.splitlines()
    nonempty = [line.strip() for line in lines if line.strip() and not line.lstrip().startswith(b'#')]
    after = original
    if not nonempty or nonempty[-1] != b'/.itp/':
        newline = b'\r\n' if b'\r\n' in original else b'\n'
        after += (newline if original and not original.endswith(b'\n') else b'') + b'/.itp/' + newline
    changes = []
    if after != original:
        changes.append('append /.itp/ to .gitignore (preserve existing bytes)')
    if not (root / '.itp/work').is_dir():
        changes.append('create .itp/work/')
    return before, after, changes


def setup(root: Path, apply: bool) -> list[str]:
    root = root.resolve()
    before, after, changes = plan(root)
    if not apply:
        return changes
    # Validate again immediately before effects. Concurrent edits remain unsupported.
    if plan(root) != (before, after, changes):
        raise ValueError('setup inputs changed; preview again')
    ignore = root / '.gitignore'
    if after != (before or b''):
        if before is None:
            with ignore.open('xb') as stream:
                stream.write(after)
        else:
            with ignore.open('ab') as stream:
                stream.write(after[len(before):])
    (root / '.itp/work').mkdir(parents=True, exist_ok=True)
    _, _, remaining = plan(root)
    if remaining:
        raise ValueError('setup readback incomplete; inspect local changes before retrying')
    git(root, 'check-ignore', '--no-index', '.itp/work/readback-probe.md')
    return changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    try:
        changes = setup(args.root, args.apply)
        print(('APPLIED' if args.apply else 'PREVIEW') + ': ' + ('; '.join(changes) or 'already configured'))
        print('Existing source/spec paths unchanged. No files staged or committed.')
    except (OSError, UnicodeError, ValueError, subprocess.SubprocessError) as exc:
        parser.exit(2, f'error: {exc}\n')


if __name__ == '__main__':
    main()
