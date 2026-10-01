# Changelog

## 0.3.0

- Added /decide as an explicit human decision stage between research and promise shaping.
- Research now ends with advisory synthesis and hands off to /decide instead of implicitly recording a choice.
- /decide reduces the work to viable options, explains tradeoffs, separates evidence from preference, and records only an explicit attributable human choice.
- Added decision-blocking behavior for unresolved load-bearing unknowns.
- Updated /discover, protocol docs, templates, scenarios, and tests for the seven-skill workflow.

## 0.2.0

- Added a durable local discovery work-item model under .itp/work/<slug>/.
- Added stable claim IDs, evidence/counterevidence, and explicit research stop rules.
- Added bounded experiment records and research-to-experiment feedback.
- Added /challenge-decision as an independent advisory pre-promise review.
- Added revisioned promise identity using exact-byte SHA-256.
- Added approval and drift-detectable Promise to Proof handoff records.
- Added canonical record templates, structural validation tools, scenarios, tests,
  and GitHub Actions checks.

## 0.1.0

Initial skills-first release with framing, brainstorming, research, promise
shaping, discovery coordination, and basic Promise to Proof handoff documentation.
