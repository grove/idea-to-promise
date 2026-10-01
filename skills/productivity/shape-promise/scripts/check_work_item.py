#!/usr/bin/env python3
"""Read-only structure/identity checks, never approval authentication or readiness."""
from __future__ import annotations
import argparse
import hashlib
import re
import sys
from pathlib import Path

HEADINGS = ('Intended outcome', 'Promise', 'Boundaries', 'Binding constraints',
            'Out of scope', 'Assumptions and open questions', 'Advisory rationale')
PLACEHOLDERS = {'', 'none', 'unknown', 'pending', 'tbd', 'not checked'}


def identity(data: bytes) -> str:
    return 'promise:sha256:' + hashlib.sha256(data).hexdigest()


def prose(text: str) -> str:
    """Exclude fenced examples and blockquotes from metadata parsing."""
    lines, fence = [], None
    for line in text.splitlines():
        m = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if m:
            mark = m.group(1)
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
            lines.append('')
        else:
            lines.append(line if fence is None and not line.lstrip().startswith('>') else '')
    return '\n'.join(lines)


def field(text: str, name: str) -> str:
    values = re.findall(r'^' + re.escape(name) + r':[ \t]*(.*?)[ \t]*$', prose(text), re.M)
    if len(values) != 1:
        raise ValueError(f'{name}: expected exactly one field')
    value = values[0]
    if value.casefold() in PLACEHOLDERS or '<' in value or '>' in value:
        raise ValueError(f'{name}: missing value or unresolved placeholder')
    return value


def local(root: Path, value: str) -> Path:
    """Record references are project-relative, plain paths, not URLs or Markdown."""
    p = Path(value)
    if p.is_absolute() or '\\' in value or ':' in value or '..' in p.parts:
        raise ValueError(f'not a project-relative path: {value}')
    target = (root / p).resolve()
    if not target.is_relative_to(root):
        raise ValueError(f'path escapes project: {value}')
    return target


def read(path: Path, root: Path) -> tuple[bytes, str]:
    if not path.resolve().is_relative_to(root):
        raise ValueError(f'path escapes project: {path}')
    data = path.read_bytes()
    return data, data.decode('utf-8')


def check(work: Path, root: Path, promise: Path | None, handoff: bool = False) -> list[str]:
    errors: list[str] = []

    def attempt(label, fn):
        try:
            return fn()
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f'{label}: {exc}')
            return None

    if not work.is_dir() or not work.resolve().is_relative_to(root):
        return ['work item must be a directory inside the project root']
    for name in ('research.md', 'discovery.md'):
        path = work / name
        if path.exists():
            def claims():
                text = prose(read(path, root)[1])
                ids = re.findall(r'^\|[ \t]*(C[1-9][0-9]*)[ \t]*\|', text, re.M)
                ids += re.findall(r'^(C[1-9][0-9]*)[ \t]+[—-]', text, re.M)
                if len(ids) != len(set(ids)):
                    raise ValueError('duplicate claim IDs')
            attempt(name, claims)
    seen = set()
    for path in sorted((work / 'experiments').glob('*.md')):
        def experiment():
            text = read(path, root)[1]
            eid = field(text, 'Experiment ID')
            if not re.fullmatch(r'E[1-9][0-9]*', eid) or eid in seen:
                raise ValueError('missing/invalid or duplicate experiment ID')
            seen.add(eid)
            for h in ('Question', 'Decision rule', 'Stop condition', 'Result'):
                if not re.search(r'^## ' + re.escape(h) + r'[ \t]*$', prose(text), re.M):
                    raise ValueError(f'missing heading {h}')
        attempt(str(path), experiment)
    if promise is None:
        if handoff or any((work / n).exists() for n in ('approval.md', 'handoff.md')):
            errors.append('--promise is required to check approval or handoff identity')
        return errors

    def source():
        data, text = read(promise, root)
        if not text.startswith('# Promise:'):
            raise ValueError("first heading must start '# Promise:'")
        revision = field(text, 'Promise revision')
        if not re.fullmatch(r'v[1-9][0-9]*', revision):
            raise ValueError('invalid Promise revision')
        clean = prose(text)
        for heading in HEADINGS:
            match = re.search(r'^## ' + re.escape(heading) + r'[ \t]*\n(.*?)(?=^## |\Z)',
                              clean, re.M | re.S)
            if match is None or not match.group(1).strip():
                raise ValueError(f'missing or empty heading {heading}')
        return revision, identity(data)
    expected = attempt(str(promise), source)
    if expected is None:
        return errors

    def receipt(path: Path, approval: bool):
        text = read(path, root)[1]
        if local(root, field(text, 'Source')) != promise.resolve():
            raise ValueError('Source does not match the supplied promise path')
        if field(text, 'Promise revision') != expected[0]:
            raise ValueError('revision does not match current promise')
        if field(text, 'Promise identity') != expected[1]:
            raise ValueError('identity does not match current promise')
        if approval:
            field(text, 'Approved by')
            field(text, 'Approval source')
        else:
            referenced = local(root, field(text, 'Approval'))
            if referenced == path.resolve() or referenced == promise.resolve():
                raise ValueError('Approval must reference a separate receipt')
            receipt(referenced, True)
        return text

    approval_path, handoff_path = work / 'approval.md', work / 'handoff.md'
    if approval_path.exists():
        attempt('approval', lambda: receipt(approval_path, True))
    if handoff_path.exists():
        attempt('handoff', lambda: receipt(handoff_path, False))
    elif handoff:
        errors.append('handoff.md is required for --handoff')
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('work_item', type=Path)
    parser.add_argument('--promise', type=Path)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--handoff', action='store_true', help='require a complete matching handoff')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    work = args.work_item if args.work_item.is_absolute() else root / args.work_item
    promise = args.promise
    if promise is not None and not promise.is_absolute():
        promise = root / promise
    errors = check(work, root, promise, args.handoff)
    for error in errors:
        print('ERROR: ' + error, file=sys.stderr)
    if errors:
        return 1
    print('STRUCTURE OK' + ('; handoff identities match' if args.handoff else '') +
          '; evidence quality, approval authenticity and delivery readiness NOT ASSESSED')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
