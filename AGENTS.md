# Working on Idea to Promise

Read README.md, docs/discovery-protocol.md, docs/artifact-format.md and
CONTRIBUTING.md before changing workflow semantics. This is a skills-first
human-led discovery system, not an autonomous controller.

Keep reports, evidence, preferences, human choices, exact source approval and
P2P implementation authority separate. Preserve existing conventions and human
edits. Do not publish private research, transcripts, credentials or ignored state.

Canonical resources are docs/discovery-protocol.md, templates/*.md,
scripts/setup_project.py, scripts/check_work_item.py and scripts/promise_identity.py.
Regenerate skill copies with scripts/sync_skill_resources.py; do not edit copies.

```bash
python3 scripts/sync_skill_resources.py
python3 scripts/sync_skill_resources.py --check
python3 scripts/release_check.py
python3 -m unittest discover -s checks -p 'test_*.py' -v
```

Do not portray examples, keyword checks, fixture adapters or unassessed runs as
live-agent evidence. Preserve semantic failures and review limits. No unrelated
P2P changes, production experiments or paid live runs are implied by code edits.
