#!/usr/bin/env python3
"""Prepare/capture discovery trials; keep mechanical checks separate from human review.

Adapters are trusted, user-selected commands, NOT sandboxed by this program.
Model-produced files remain virtual JSON data and are never applied to a project.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import signal
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
LIMIT = 2_000_000


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(path: Path, limit: int = 64_000_000):
    data = path.read_bytes()
    if len(data) > limit:
        raise ValueError(f'input exceeds {limit} bytes: {path}')
    return json.loads(data)


def save(path: Path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def virtual(files):
    if not isinstance(files, dict):
        raise ValueError('files must be an object of path: text')
    for name, content in files.items():
        p = PurePosixPath(name)
        if (not name or p.is_absolute() or '..' in p.parts or '.git' in p.parts
                or '\\' in name or ':' in name or str(p) != name or not isinstance(content, str)):
            raise ValueError(f'unsafe virtual file path or non-text content: {name}')
    return files


def cases(path: Path):
    values = load(path, limit=LIMIT)
    if not isinstance(values, list) or not values:
        raise ValueError('case suite must be a nonempty array')
    seen = set()
    for c in values:
        if not re.fullmatch(r'[a-z0-9-]+', c['id']) or c['id'] in seen:
            raise ValueError('case IDs must be unique slugs')
        seen.add(c['id'])
        if not re.fullmatch(r'[a-z0-9-]+', c['skill']):
            raise ValueError('invalid skill name')
        if c.get('mode', 'normal') not in ('quick', 'normal', 'deep'):
            raise ValueError('invalid mode')
        virtual(c.get('files', {}))
        if not c['turns'] or not c['rubric'] or not all(isinstance(t, str) and t.strip() for t in c['rubric']):
            raise ValueError('turns and rubric must be nonempty')
        for t in c['turns']:
            if not isinstance(t['user'], str) or not t['user'].strip():
                raise ValueError('missing scripted human message')
            for key, paths in t.get('checks', {}).items():
                if key not in ('forbid_suffix', 'forbid_prefix', 'require_suffix', 'preserve_paths'):
                    raise ValueError(f'unknown mechanical check: {key}')
                if not isinstance(paths, list) or not all(isinstance(p, str) and p for p in paths):
                    raise ValueError('check paths must be nonempty strings')
    return values


def snapshot(skill: str):
    directory = ROOT / 'skills/productivity' / skill
    paths = [directory / 'SKILL.md', *sorted((directory / 'references').glob('*.md')),
             *sorted((directory / 'templates').glob('*.md'))]
    return {str(p.relative_to(directory)): p.read_text(encoding='utf-8') for p in paths}


def mechanical(files, rules, before=None):
    results = []
    for rule, values in rules.items():
        for value in values:
            matches = [p for p in files if (p.startswith(value) if rule == 'forbid_prefix' else p.endswith(value))]
            ok = ((value in (before or {}) and files.get(value) == before[value])
                  if rule == 'preserve_paths' else bool(matches)
                  if rule == 'require_suffix' else not matches)
            results.append({'check': rule, 'value': value, 'passed': ok, 'matches': matches})
    return results


def friction(turns):
    """Observable interaction cost only; not a quality score."""
    result = {'turns': len(turns), 'reply_chars': 0, 'question_marks': 0,
              'files_created': 0, 'files_changed': 0, 'seconds': 0.0}
    for turn in turns:
        reply = turn['response']['reply']
        before = turn['request'].get('files', {})
        after = turn['response'].get('files', {})
        result['reply_chars'] += len(reply)
        result['question_marks'] += reply.count('?')
        result['files_created'] += sum(name not in before for name in after)
        result['files_changed'] += sum(name in before and before[name] != value
                                       for name, value in after.items())
        result['seconds'] += float(turn.get('seconds', 0.0))
    result['seconds'] = round(result['seconds'], 3)
    return result


def aggregate_friction(items):
    keys = ('turns', 'reply_chars', 'question_marks', 'files_created', 'files_changed', 'seconds')
    result = {key: 0 for key in keys}
    for item in items:
        values = item.get('friction', {})
        for key in keys:
            result[key] += values.get(key, 0)
    result['seconds'] = round(result['seconds'], 3)
    return result


def invoke(command, request, timeout):
    # Spool rather than retaining unbounded stdout in memory. Host commands must
    # themselves enforce resource/network limits. stderr is deliberately not retained.
    with tempfile.TemporaryDirectory(prefix='itp-eval-') as cwd, tempfile.TemporaryFile() as out:
        proc = subprocess.Popen(command, cwd=cwd, stdin=subprocess.PIPE, stdout=out,
                                stderr=subprocess.DEVNULL, start_new_session=(os.name == 'posix'))
        try:
            proc.communicate(json.dumps(request).encode('utf-8'), timeout=timeout)
        except subprocess.TimeoutExpired:
            if os.name == 'posix':
                os.killpg(proc.pid, signal.SIGKILL)
            else:
                proc.kill()
            proc.communicate()
            raise ValueError('adapter timed out')
        if proc.returncode:
            raise ValueError(f'adapter exited {proc.returncode}; stderr not retained')
        out.seek(0)
        data = out.read(LIMIT + 1)
        if len(data) > LIMIT:
            raise ValueError('adapter output too large')
        response = json.loads(data)
        if not isinstance(response, dict) or not isinstance(response.get('reply'), str) or not response['reply'].strip():
            raise ValueError('adapter must return a nonempty reply and files object')
        virtual(response['files'])
        return {'reply': response['reply'], 'files': response['files']}


def execute(selected, output: Path, command, kind: str, host: str, model: str, timeout: int):
    if output.exists():
        raise ValueError('output exists; choose a new run directory')
    output.mkdir(parents=True)
    started = datetime.now(timezone.utc).isoformat()
    manifest = {'schema': 'itp-eval-v1', 'kind': kind, 'host': host, 'model': model,
                'identity_note': 'host/model/kind are operator declarations, not authentication',
                'started': started, 'status': 'prepared' if command is None else 'running', 'cases': []}
    save(output / 'run.json', manifest)
    failed = False
    for c in selected:
        instructions = snapshot(c['skill'])
        save(output / (c['id'] + '.case.json'), c)
        save(output / (c['id'] + '.skills.json'), instructions)
        item = {'id': c['id'], 'rubric': c['rubric'], 'case_sha256': digest(json.dumps(c, sort_keys=True).encode()),
                'skills_sha256': digest(json.dumps(instructions, sort_keys=True).encode()),
                'turns': [], 'status': 'prepared', 'semantic_verdict': 'not-assessed'}
        messages, files = [], c.get('files', {})
        for t in c['turns'] if command else []:
            messages.append({'role': 'user', 'content': t['user']})
            request = {'schema': 'itp-eval-v1', 'instructions': instructions, 'mode': c.get('mode', 'normal'),
                       'messages': list(messages), 'files': files,
                       'boundary': 'Return reply and complete virtual files snapshot. No external actions. '
                                   'Scripted human messages are fixture inputs, not real approvals.'}
            tick = time.monotonic()
            try:
                response = invoke(command, request, timeout)
                checks = mechanical(response['files'], t.get('checks', {}), files)
                item['turns'].append({'request': request, 'response': response, 'checks': checks,
                                      'seconds': round(time.monotonic() - tick, 3)})
                failed |= any(not check['passed'] for check in checks)
                files = response['files']
                messages.append({'role': 'assistant', 'content': response['reply']})
                item['status'] = 'captured'
            except (OSError, ValueError, KeyError, UnicodeError) as exc:
                item['status'], item['error'] = 'error', str(exc)
                failed = True
                break
        item['friction'] = friction(item['turns'])
        manifest['cases'].append(item)
        save(output / 'run.json', manifest)
    manifest['friction'] = aggregate_friction(manifest['cases'])
    manifest['status'] = 'prepared' if command is None else 'captured'
    save(output / 'run.json', manifest)
    review = {'run_sha256': digest((output / 'run.json').read_bytes()), 'reviewer': '',
              'judgments': [{'case': c['id'], 'criterion': i, 'verdict': 'not-assessed',
                             'turn': 1, 'excerpt': '', 'reason': ''}
                            for c in selected for i, _ in enumerate(c['rubric'], 1)]}
    save(output / 'review-template.json', review)
    print(f"{manifest['status'].upper()}: {len(selected)} cases; kind={kind}; semantic quality NOT ASSESSED")
    return 1 if failed else 0


def report(run_path: Path, review_path: Path | None):
    run = load(run_path)
    if run.get('schema') != 'itp-eval-v1' or run.get('kind') not in ('fixture', 'live') or not run.get('cases'):
        raise ValueError('not a nonempty captured evaluation run')
    if run['status'] != 'captured':
        raise ValueError('prepared cases are not executed trials')
    ids = [c['id'] for c in run['cases']]
    if len(ids) != len(set(ids)):
        raise ValueError('duplicate case IDs in captured run')
    for c in run['cases']:
        if not c.get('rubric') or c.get('status') not in ('captured', 'error'):
            raise ValueError('case lacks rubric or captured/error status')
        if c['status'] == 'captured' and not c.get('turns'):
            raise ValueError('captured case has no actual turns')
    review = load(review_path) if review_path else {'judgments': []}
    if review_path and (review.get('run_sha256') != digest(run_path.read_bytes()) or not review.get('reviewer', '').strip()):
        raise ValueError('review needs a reviewer and must bind this exact run')
    expected = {(c['id'], i): (c, criterion) for c in run['cases'] for i, criterion in enumerate(c['rubric'], 1)}
    verdicts = {}
    for j in review['judgments']:
        key = (j['case'], j['criterion'])
        if key not in expected or key in verdicts or j['verdict'] not in ('pass', 'fail', 'not-assessed'):
            raise ValueError('invalid or duplicate review judgment')
        if j['verdict'] != 'not-assessed':
            turns = expected[key][0]['turns']
            if (not isinstance(j['turn'], int) or not 1 <= j['turn'] <= len(turns)
                    or not j['excerpt'] or not j['reason'].strip()
                    or j['excerpt'] not in turns[j['turn'] - 1]['response']['reply']):
                raise ValueError('judgment needs a real response excerpt, valid turn and rationale')
        verdicts[key] = j['verdict']
    failed = any(c['status'] == 'error' or any(not k['passed'] for t in c['turns'] for k in t['checks']) for c in run['cases'])
    failed |= 'fail' in verdicts.values()
    pending = sum(verdicts.get(key, 'not-assessed') == 'not-assessed' for key in expected)
    status = 'FAIL' if failed else 'INCOMPLETE' if pending else 'REVIEWED PASS'
    print(f'{status}; kind={run["kind"]}; unassessed criteria={pending}/{len(expected)}')
    f = run.get('friction') or aggregate_friction(run['cases'])
    print('Friction observables: ' + ', '.join(f'{key}={f[key]}' for key in
          ('turns', 'question_marks', 'files_created', 'files_changed', 'reply_chars', 'seconds')))
    print('Friction observables are descriptive, not a quality score or automatic failure threshold.')
    print('Fixture results are not live-agent evidence. Review judgments are attributed, not independent proof.')
    return 1 if failed else 3 if pending else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    for action in ('prepare', 'run'):
        p = sub.add_parser(action)
        p.add_argument('--suite', type=Path, default=ROOT / 'evaluations/cases.json')
        p.add_argument('--case')
        p.add_argument('--out', type=Path, required=True)
        if action == 'run':
            p.add_argument('--command-json', required=True, help='JSON argv array for a trusted host adapter')
            p.add_argument('--kind', choices=('fixture', 'live'), default='fixture')
            p.add_argument('--host', required=True)
            p.add_argument('--model', required=True)
            p.add_argument('--timeout', type=int, default=120)
    p = sub.add_parser('report')
    p.add_argument('run', type=Path)
    p.add_argument('--reviews', type=Path)
    args = parser.parse_args()
    try:
        if args.action == 'report':
            return report(args.run, args.reviews)
        selected = [c for c in cases(args.suite) if args.case is None or c['id'] == args.case]
        if not selected:
            raise ValueError('unknown case')
        command = json.loads(args.command_json) if args.action == 'run' else None
        if command is not None and (not isinstance(command, list) or not command or not all(isinstance(v, str) and v for v in command)):
            raise ValueError('command must be a nonempty JSON argv array')
        if args.action == 'run' and (args.timeout <= 0 or not args.host.strip() or not args.model.strip()):
            raise ValueError('positive timeout and host/model labels are required')
        return execute(selected, args.out, command, getattr(args, 'kind', 'prepared'),
                       getattr(args, 'host', 'not run'), getattr(args, 'model', 'not run'), getattr(args, 'timeout', 120))
    except (OSError, ValueError, KeyError, TypeError, UnicodeError) as exc:
        parser.exit(2, f'error: {exc}\n')


if __name__ == '__main__':
    raise SystemExit(main())
