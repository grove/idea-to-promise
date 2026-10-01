from __future__ import annotations
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import sync_skill_resources as resources


class RepositoryTests(unittest.TestCase):
    def test_skills_have_valid_frontmatter_and_current_version(self):
        expected = set(resources.TEMPLATES)
        actual = {p.name for p in (ROOT / 'skills/productivity').iterdir() if (p / 'SKILL.md').is_file()}
        self.assertEqual(actual, expected)
        version = (ROOT / 'VERSION').read_text().strip()
        for name in actual:
            text = (ROOT / f'skills/productivity/{name}/SKILL.md').read_text()
            self.assertTrue(text.startswith('---\n'))
            metadata = text.split('---', 2)[1]
            self.assertIn(f'name: {name}\n', metadata)
            self.assertIn(f'version: "{version}"', metadata)
            description = re.search(r'^description: (.+)$', metadata, re.M).group(1)
            self.assertTrue(1 <= len(description) <= 1024)
            self.assertLess(len(text.splitlines()), 500)

    def test_generated_resources_match(self):
        self.assertEqual(resources.sync(True), [])

    def test_markdown_links_resolve(self):
        pattern = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
        for path in ROOT.rglob('*.md'):
            if '.git' in path.parts or '.itp' in path.parts:
                continue
            for target in pattern.findall(path.read_text(encoding='utf-8')):
                if '://' in target or target.startswith(('#', 'mailto:')) or '<' in target:
                    continue
                target = target.split('#', 1)[0]
                if target:
                    self.assertTrue((path.parent / target).exists(), f'{path}: {target}')

    def test_standalone_skill_closure_and_bundled_helpers(self):
        for name in resources.TEMPLATES:
            with self.subTest(skill=name), tempfile.TemporaryDirectory() as td:
                base = Path(td) / name
                shutil.copytree(ROOT / 'skills/productivity' / name, base)
                for path in base.rglob('*.md'):
                    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text()):
                        if '://' in target or '<' in target or target.startswith('#'):
                            continue
                        resolved = (path.parent / target.split('#')[0]).resolve()
                        self.assertTrue(resolved.is_relative_to(base))
                        self.assertTrue(resolved.exists())
                for script in (base / 'scripts').glob('*.py'):
                    result = subprocess.run([sys.executable, str(script), '--help'], capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stderr)

    def test_sync_check_detects_drift_without_writing(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for src, dst in resources.mapping(ROOT):
                a, b = root / src.relative_to(ROOT), root / dst.relative_to(ROOT)
                a.parent.mkdir(parents=True, exist_ok=True)
                a.write_bytes(src.read_bytes())
                b.parent.mkdir(parents=True, exist_ok=True)
                b.write_bytes(src.read_bytes())
            victim = resources.mapping(root)[0][1]
            victim.write_text('local change')
            self.assertTrue(resources.sync(True, root))
            self.assertEqual(victim.read_text(), 'local change')
            resources.sync(False, root)
            self.assertEqual(resources.sync(True, root), [])

    def test_examples_are_explicitly_fictional(self):
        paths = [p for p in (ROOT / 'examples').glob('*.md') if p.name not in ('README.md', 'export-promise.md')]
        self.assertEqual(len(paths), 6)
        for path in paths:
            self.assertIn('Fictional teaching example', path.read_text())


if __name__ == '__main__':
    unittest.main()
