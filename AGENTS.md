# Working on Idea to Promise

Read README.md, docs/discovery-protocol.md, and docs/artifact-format.md before
changing workflow semantics.

This repository ships agent skills and lightweight structural tools, not a
product-delivery controller.

Preserve these distinctions:
- observation vs attributed report vs inference vs assumption vs preference;
- recommendation vs human decision;
- decision vs exact source-promise approval;
- ITP source approval vs P2P acceptance approval;
- source approval vs authority to implement, commit, push, publish, or merge.

Keep the boundary with Promise to Proof crisp: ITP decides what is worth
promising; P2P plans acceptance, implements, reviews, and proves that promise.

Keep .itp/ and .p2p/ ignored. Do not commit private research, credentials, or
model transcripts by default.

Run:

```bash
python3 -m unittest discover -s checks -p 'test_*.py' -v
```

Structural checks are not evidence that live agent judgment is correct. Update
checks/scenarios.md when changing decision behavior.
