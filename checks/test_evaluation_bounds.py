"""Regression cases for aggregate transcripts and malformed empty-review reports."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import evaluate as ev


class EvaluationBoundsTests(unittest.TestCase):
    def test_aggregate_record_can_exceed_per_reply_limit(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'run.json'
            value = {'retained_transcript': 'x' * (ev.LIMIT + 1)}
            path.write_text(json.dumps(value))
            self.assertEqual(ev.load(path), value)
            with self.assertRaises(ValueError):
                ev.load(path, limit=ev.LIMIT)

    def test_empty_rubric_or_capture_cannot_be_a_pass(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'run.json'
            for case in ({'id': 'bad', 'rubric': [], 'status': 'captured', 'turns': []},
                         {'id': 'bad', 'rubric': ['criterion'], 'status': 'captured', 'turns': []}):
                with self.subTest(case=case):
                    ev.save(path, {'schema': 'itp-eval-v1', 'kind': 'fixture',
                                   'status': 'captured', 'cases': [case]})
                    with self.assertRaises(ValueError):
                        ev.report(path, None)


if __name__ == '__main__':
    unittest.main()
