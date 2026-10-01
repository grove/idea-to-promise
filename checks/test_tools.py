from __future__ import annotations
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import check_work_item as cw
import promise_identity as pi
import setup_project as setup
import evaluate as ev


class WorkItemTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.work = self.root / '.itp/work/example'
        self.work.mkdir(parents=True)
        self.source = self.root / 'specs/example.md'
        self.source.parent.mkdir()
        self.source.write_bytes((ROOT / 'examples/export-promise.md').read_bytes())
        self.pid = pi.promise_identity(self.source)

    def receipt(self):
        return (f'Source: specs/example.md\nPromise revision: v1\nPromise identity: {self.pid}\n'
                'Approved by: Fictional test user\nApproval source: scripted fixture approval, not real consent\n')

    def handoff(self):
        return (f'Source: specs/example.md\nPromise revision: v1\nPromise identity: {self.pid}\n'
                'Approval: .itp/work/example/approval.md\n')

    def valid(self):
        (self.work / 'approval.md').write_text(self.receipt())
        (self.work / 'handoff.md').write_text(self.handoff())

    def check(self, handoff=True):
        return cw.check(self.work, self.root, self.source, handoff)

    def test_matching_handoff(self):
        self.valid()
        self.assertEqual(self.check(), [])

    def test_draft_does_not_require_receipt(self):
        self.assertEqual(self.check(False), [])
        self.assertTrue(self.check(True))

    def test_handoff_without_approval_fails(self):
        (self.work / 'handoff.md').write_text(self.handoff())
        self.assertTrue(self.check())

    def test_wrong_source_even_with_matching_bytes_fails(self):
        self.valid()
        (self.root / 'specs/other.md').write_bytes(self.source.read_bytes())
        (self.work / 'approval.md').write_text(self.receipt().replace('specs/example.md', 'specs/other.md'))
        self.assertIn('Source does not match', '\n'.join(self.check()))

    def test_one_byte_drift_fails(self):
        self.valid()
        self.source.write_bytes(self.source.read_bytes() + b'\n')
        self.assertIn('identity does not match', '\n'.join(self.check()))

    def test_revision_drift_fails(self):
        self.valid()
        (self.work / 'handoff.md').write_text(self.handoff().replace('v1', 'v2'))
        self.assertIn('revision does not match', '\n'.join(self.check()))

    def test_empty_and_placeholder_approvers_fail(self):
        for value in ('', '<name>', 'unknown'):
            with self.subTest(value=value):
                self.valid()
                (self.work / 'approval.md').write_text(self.receipt().replace('Fictional test user', value))
                self.assertTrue(self.check())

    def test_duplicate_fields_fail(self):
        self.valid()
        with (self.work / 'approval.md').open('a') as f:
            f.write('Source: specs/example.md\n')
        self.assertTrue(self.check())

    def test_fenced_metadata_is_not_approval(self):
        self.valid()
        (self.work / 'approval.md').write_text('```\n' + self.receipt() + '```\n')
        self.assertTrue(self.check())

    def test_missing_attribution_fails(self):
        self.valid()
        (self.work / 'approval.md').write_text(self.receipt().split('Approval source:')[0])
        self.assertTrue(self.check())

    def test_receipts_cannot_skip_promise_check(self):
        self.valid()
        self.assertTrue(cw.check(self.work, self.root, None))

    def test_traversal_absolute_and_self_reference_fail(self):
        for value in ('../approval.md', '/tmp/approval.md', '.itp/work/example/handoff.md'):
            with self.subTest(value=value):
                self.valid()
                (self.work / 'handoff.md').write_text(self.handoff().replace('.itp/work/example/approval.md', value))
                self.assertTrue(self.check())

    def test_symlink_escape_fails(self):
        with tempfile.TemporaryDirectory() as other:
            outside = Path(other) / 'receipt.md'
            outside.write_text(self.receipt())
            (self.work / 'approval.md').symlink_to(outside)
            (self.work / 'handoff.md').write_text(self.handoff())
            self.assertTrue(self.check())

    def test_unreadable_and_invalid_utf8_fail_cleanly(self):
        self.source.write_bytes(b'\xff')
        self.assertTrue(self.check(False))
        self.source.unlink()
        self.source.mkdir()
        self.assertTrue(self.check(False))

    def test_identity_does_not_normalize_newlines(self):
        self.source.write_bytes(b'a\r\n')
        first = pi.promise_identity(self.source)
        self.source.write_bytes(b'a\n')
        self.assertNotEqual(first, pi.promise_identity(self.source))
        self.assertEqual(first, 'promise:sha256:' + hashlib.sha256(b'a\r\n').hexdigest())

    def test_duplicate_claims_table_and_compact(self):
        for text in ('| C1 | one |\n| C1 | two |\n', 'C1 — one\nC1 — two\n'):
            (self.work / 'research.md').write_text(text)
            self.assertTrue(self.check(False))

    def test_duplicate_experiment_ids_fail(self):
        exp = self.work / 'experiments'
        exp.mkdir()
        content = (ROOT / 'templates/experiment.md').read_text()
        (exp / 'first.md').write_text(content)
        (exp / 'second.md').write_text(content)
        self.assertIn('duplicate experiment ID', '\n'.join(self.check(False)))

    def test_check_is_read_only(self):
        self.valid()
        before = {str(p): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.check()
        after = {str(p): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)


@unittest.skipUnless(shutil.which('git'), 'setup requires Git')
class SetupTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)

    def test_preview_is_read_only(self):
        self.assertTrue(setup.setup(self.root, False))
        self.assertFalse((self.root / '.itp').exists())
        self.assertFalse((self.root / '.gitignore').exists())

    def test_apply_preserves_bytes_and_is_idempotent(self):
        data = b'# custom\r\nlocal-cache/'
        (self.root / '.gitignore').write_bytes(data)
        (self.root / 'specs').mkdir()
        (self.root / 'specs/existing.md').write_text('human source')
        setup.setup(self.root, True)
        self.assertTrue((self.root / '.gitignore').read_bytes().startswith(data))
        self.assertEqual((self.root / 'specs/existing.md').read_text(), 'human source')
        self.assertEqual(setup.setup(self.root, True), [])
        self.assertEqual(setup.git(self.root, 'diff', '--cached'), '')
        setup.git(self.root, 'check-ignore', '--no-index', '.itp/work/a/new.md')

    def test_tracked_state_fails_without_changes(self):
        (self.root / '.itp').mkdir()
        (self.root / '.itp/private.md').write_text('do not publish')
        setup.git(self.root, 'add', '.itp/private.md')
        with self.assertRaises(ValueError):
            setup.setup(self.root, True)
        self.assertFalse((self.root / '.gitignore').exists())

    def test_symlink_and_type_conflicts_fail(self):
        target = self.root / 'other'
        target.mkdir()
        (self.root / '.itp').symlink_to(target, target_is_directory=True)
        with self.assertRaises(ValueError):
            setup.setup(self.root, True)
        (self.root / '.itp').unlink()
        (self.root / '.itp').write_text('conflict')
        with self.assertRaises(ValueError):
            setup.setup(self.root, True)

    def test_non_git_and_subdirectory_are_rejected(self):
        child = self.root / 'child'
        child.mkdir()
        with self.assertRaises(ValueError):
            setup.setup(child, True)
        with tempfile.TemporaryDirectory() as non_git:
            with self.assertRaises(ValueError):
                setup.setup(Path(non_git), True)


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.out = self.root / 'run'
        self.case = {'id': 'test', 'skill': 'discover', 'mode': 'quick', 'files': {},
                     'turns': [{'user': 'first', 'checks': {'forbid_suffix': ['approval.md']}},
                               {'user': 'SECONDSECRET', 'checks': {}}],
                     'rubric': ['Preserve human choice']}
        # Explicit fixture, not an LLM or a live evaluation adapter.
        self.command = [sys.executable, '-c',
                        'import sys,json; r=json.load(sys.stdin); '
                        'print(json.dumps({"reply":"fixture response", "files":r["files"]}))']

    def run_fixture(self):
        return ev.execute([self.case], self.out, self.command, 'fixture', 'test-host', 'no-model', 5)

    def test_suite_has_unique_valid_cases(self):
        suite = ev.cases(ROOT / 'evaluations/cases.json')
        self.assertGreaterEqual(len(suite), 8)
        self.assertGreaterEqual(sum(c['skill'] == 'discover' for c in suite), 3)

    def test_prepared_is_not_executed(self):
        ev.execute([self.case], self.out, None, 'prepared', 'not run', 'not run', 5)
        with self.assertRaises(ValueError):
            ev.report(self.out / 'run.json', None)

    def test_empty_run_cannot_pass(self):
        path = self.root / 'empty.json'
        ev.save(path, {'schema': 'itp-eval-v1', 'kind': 'fixture', 'status': 'captured', 'cases': []})
        with self.assertRaises(ValueError):
            ev.report(path, None)

    def test_fixture_capture_is_not_semantic_pass(self):
        self.assertEqual(self.run_fixture(), 0)
        self.assertEqual(ev.report(self.out / 'run.json', None), 3)
        run = ev.load(self.out / 'run.json')
        self.assertEqual(run['kind'], 'fixture')
        self.assertNotIn('SECONDSECRET', json.dumps(run['cases'][0]['turns'][0]['request']))
        self.assertNotIn('rubric', run['cases'][0]['turns'][0]['request'])

    def test_review_binds_run_and_actual_excerpt(self):
        self.run_fixture()
        review = ev.load(self.out / 'review-template.json')
        review['reviewer'] = 'Fixture test reviewer (not independent live review)'
        review['judgments'][0].update(verdict='pass', turn=1, excerpt='fixture response', reason='Fixture reporting test only')
        path = self.out / 'review.json'
        ev.save(path, review)
        self.assertEqual(ev.report(self.out / 'run.json', path), 0)
        review['judgments'][0]['excerpt'] = 'fabricated words'
        ev.save(path, review)
        with self.assertRaises(ValueError):
            ev.report(self.out / 'run.json', path)
        review['judgments'][0]['excerpt'] = 'fixture response'
        review['run_sha256'] = '0' * 64
        ev.save(path, review)
        with self.assertRaises(ValueError):
            ev.report(self.out / 'run.json', path)

    def test_negative_mechanical_control_fails(self):
        self.case['turns'][0]['checks'] = {'require_suffix': ['decision.md']}
        self.assertEqual(self.run_fixture(), 1)
        self.assertEqual(ev.report(self.out / 'run.json', None), 1)

    def test_preservation_check_detects_changed_source(self):
        result = ev.mechanical({'specs/a.md': 'changed'}, {'preserve_paths': ['specs/a.md']}, {'specs/a.md': 'original'})
        self.assertFalse(result[0]['passed'])

    def test_unsafe_virtual_paths_rejected(self):
        for name in ('../a', '/a', '.git/config', 'C:\\a', 'a/../b'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                ev.virtual({name: 'data'})

    def test_adapter_errors_are_retained(self):
        command = [sys.executable, '-c', 'raise SystemExit(2)']
        self.assertEqual(ev.execute([self.case], self.out, command, 'fixture', 'test', 'none', 5), 1)
        self.assertEqual(ev.load(self.out / 'run.json')['cases'][0]['status'], 'error')

    def test_timeout_and_malformed_response_fail(self):
        with self.assertRaises(ValueError):
            ev.invoke([sys.executable, '-c', 'import time; time.sleep(10)'], {}, 1)
        with self.assertRaises(ValueError):
            ev.invoke([sys.executable, '-c', 'print("not-json")'], {}, 5)

    def test_existing_output_not_overwritten(self):
        self.run_fixture()
        with self.assertRaises(ValueError):
            self.run_fixture()

    def test_reviewer_cannot_override_mechanical_failure(self):
        self.case['turns'][0]['checks'] = {'require_suffix': ['decision.md']}
        self.run_fixture()
        review = ev.load(self.out / 'review-template.json')
        review['reviewer'] = 'Fixture reviewer'
        review['judgments'][0].update(verdict='pass', turn=1, excerpt='fixture response', reason='Report test')
        path = self.out / 'review.json'
        ev.save(path, review)
        self.assertEqual(ev.report(self.out / 'run.json', path), 1)


if __name__ == '__main__':
    unittest.main()
