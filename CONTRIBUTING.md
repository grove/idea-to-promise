# Contributing

Read [AGENTS.md](AGENTS.md). Prefer a concrete observed failure over another stage
or mandatory form. Python helpers use the standard library; setup tests need Git.

Edit canonical resources, run `python3 scripts/sync_skill_resources.py`, then:

```bash
python3 scripts/sync_skill_resources.py --check
python3 -m unittest discover -s checks -p 'test_*.py' -v
python3 scripts/evaluate.py prepare --out .itp/evals/local-prepare
```

Each skill must work when copied out of the collection. Keep relative reference
links inside its directory and generated copies byte-identical. The sync script
owns only explicitly mapped paths and never deletes arbitrary files.

Add behavior cases to [the evaluation suite](evaluations/README.md) when changing
human-facing behavior. The [scenario catalog](checks/scenarios.md) remains useful
for exploratory review. Keyword/static checks are packaging checks, not semantic
evaluations. Examples must remain visibly fictional. Never manufacture approvals.

Use a trusted configured host for live capture and an attributed reviewer for
behavior judgments. Keep outputs local under .itp/ by default. Publish only after
privacy review and explicit authorization. Compare exact old/new snapshots and
retain errors, incomplete cases, and failures instead of selecting only successes.
