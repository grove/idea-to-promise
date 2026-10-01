# Contributing

Start with [AGENTS.md](AGENTS.md), the
[discovery protocol](docs/discovery-protocol.md), and the
[artifact format](docs/artifact-format.md).

A useful change should improve framing, alternative generation, decision-directed
research, bounded experimentation, decision challenge, promise shaping, or the
identity-preserving handoff to Promise to Proof without duplicating P2P's
acceptance and delivery responsibilities.

## Local checks

Python 3.11+ is sufficient:

```bash
python3 -m unittest discover -s checks -p 'test_*.py' -v
```

The tooling is intentionally dependency-free.

When changing behavioral semantics, add or update a case in
[checks/scenarios.md](checks/scenarios.md). Those scenarios are evaluation prompts,
not proof that a live model has passed.

## Scope discipline

Prefer a small improvement to an existing skill or protocol rule over adding a
new workflow stage. Do not require exhaustive research. Do not force every idea
to become a promise. Do not let an advisory challenge silently rewrite the human
decision.
