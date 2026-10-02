#!/usr/bin/env python3
"""Copy only mapped canonical resources into independently installable skill folders."""
from __future__ import annotations
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = {
    'frame': ('frame', 'discovery'),
    'brainstorm': ('alternatives', 'discovery'),
    'research': ('research', 'experiment', 'discovery'),
    'decide': ('decision', 'discovery'),
    'challenge-decision': ('challenge',),
    'shape-promise': ('promise', 'approval', 'handoff', 'amendment'),
    'discover': ('discovery', 'session', 'frame', 'alternatives', 'research', 'experiment',
                 'decision', 'challenge', 'promise', 'approval', 'handoff', 'amendment', 'outcome-review'),
    'setup-idea-to-promise': (),
}


def mapping(root=ROOT):
    pairs = []
    for skill, names in TEMPLATES.items():
        base = root / 'skills/productivity' / skill
        pairs.append((root / 'docs/discovery-protocol.md', base / 'references/discovery-protocol.md'))
        pairs.append((root / 'LICENSE', base / 'LICENSE'))
        pairs.extend((root / f'templates/{n}.md', base / f'templates/{n}.md') for n in names)
        scripts = ('setup_project',) if skill == 'setup-idea-to-promise' else (
            ('check_work_item', 'promise_identity', 'inspect_work_item') if skill in ('discover', 'shape-promise') else ())
        pairs.extend((root / f'scripts/{n}.py', base / f'scripts/{n}.py') for n in scripts)
    return pairs


def sync(check=False, root=ROOT):
    pending = []
    for src, dst in mapping(root):
        for path in (src, dst):
            if any(p.is_symlink() for p in (path, *path.parents) if p != root.parent):
                raise ValueError(f'symlink resource path: {path}')
        data = src.read_bytes()
        if not dst.is_file() or dst.read_bytes() != data:
            pending.append(str(dst.relative_to(root)))
            if not check:
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(data)
    return pending


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        pending = sync(args.check)
    except (OSError, ValueError) as exc:
        parser.exit(2, f'error: {exc}\n')
    if args.check and pending:
        parser.exit(1, 'out-of-date resources:\n' + '\n'.join(pending) + '\n')
    print('Resources match canonical sources.' if args.check else f'Updated {len(pending)} resources.')


if __name__ == '__main__':
    main()
