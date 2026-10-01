# Idea to Promise

Turn an uncertain idea into a researched, explicit promise worth making.

**Idea to Promise → Promise to Proof**

Idea to Promise (ITP) helps decide **what to promise, and why**. Its sibling,
[Promise to Proof](https://github.com/grove/promise-to-proof), turns that agreed
outcome into an acceptance contract, implements it, reviews it, and proves the
result.

ITP can also end in a bounded experiment, a deferred decision, or a deliberate
choice not to build. Research is not permission to implement.

## Start here

```text
/discover We need to make retries safe for uploads over unreliable networks.
```

For stage-by-stage work:

```text
/frame <idea or notes>
/brainstorm <framing>
/research <questions or alternatives>
/challenge-decision <decision record>
/shape-promise <selected direction and evidence>
```

These are agent skills, not shell commands. Invoke them through a compatible
host's skill interface.

## Six skills

| Skill | Question | Durable result |
|---|---|---|
| [`frame`](skills/productivity/frame/SKILL.md) | What problem are we actually addressing? | frame.md |
| [`brainstorm`](skills/productivity/brainstorm/SKILL.md) | What genuinely different paths could work? | alternatives.md |
| [`research`](skills/productivity/research/SKILL.md) | What evidence could change the decision? | research.md + experiments/ |
| [`challenge-decision`](skills/productivity/challenge-decision/SKILL.md) | Does the decision actually follow from the evidence? | challenge.md |
| [`shape-promise`](skills/productivity/shape-promise/SKILL.md) | What exact outcome are we prepared to promise? | promise draft + approval/handoff |
| [`discover`](skills/productivity/discover/SKILL.md) | How do we move the idea through the whole discovery loop? | coordinated work item |

The stages are intentionally not a rigid pipeline. New evidence may return the
work to alternatives or research. A no-build result is a valid outcome.

## v0.2 work-item model

Active discovery state lives locally under:

```text
.itp/work/<slug>/
├── frame.md
├── alternatives.md
├── research.md
├── experiments/
├── decision.md
├── challenge.md
├── promise-draft.md
├── approval.md
└── handoff.md
```

The directory is ignored by default because discovery can contain provisional or
sensitive material. The final agreed promise is a normal project-owned source
document, commonly:

```text
specs/<slug>.md
```

The final source must stand on its own; Promise to Proof must not need a previous
chat or ignored ITP files just to understand the binding promise.

See the [artifact format](docs/artifact-format.md) and
[discovery protocol](docs/discovery-protocol.md).

## Claim ledger and experiments

Research uses stable claim IDs (C1, C2, …) and distinguishes observations,
attributed reports, inferences, assumptions, unknowns, and preferences. Each
material claim records evidence, counterevidence, decision impact, and either the
next useful check or a reason to stop.

When observation is cheaper or more credible than more discussion, ITP can use a
bounded experiment (E1, E2, …) with an explicit exposure, observation, decision
rule, stop condition, actual result, and limitations. An experiment plan is never
treated as evidence that the expected outcome happened.

## Promise identity and approval

Promises use human-readable revisions such as v1 and v2. Material changes to
promised behavior, boundaries, binding constraints, or experiment decision rules
require a new revision and renewed approval.

Approval binds the **exact UTF-8 bytes** of the durable promise using:

```text
promise:sha256:<64 lowercase hex>
```

Compute it with:

```bash
python3 scripts/promise_identity.py specs/<slug>.md
```

The approval and handoff records store that identity outside the hashed promise,
avoiding a self-referential hash. Any byte change makes the old approval stale.

Validate the structural handoff with:

```bash
python3 scripts/check_work_item.py .itp/work/<slug> --promise specs/<slug>.md
```

The checker validates shape and identity only. It does not judge product value,
evidence quality, approval authenticity, or implementation readiness.

## Handoff to Promise to Proof

ITP owns framing, alternatives, decision-directed research, experiments for
learning, human decision support, and exact source-promise approval.

Promise to Proof owns acceptance planning, evidence planning, implementation,
candidate identity, review, proof, repair, and publication/merge-readiness rules.

After exact source approval and a matching identity:

```text
/plan-acceptance specs/<slug>.md
```

Source approval does not approve the later P2P acceptance contract and does not
authorize implementation or publication.

Read the [P2P handoff guide](docs/p2p-handoff.md).

## Install

```bash
npx skills@latest add grove/idea-to-promise
```

Install one skill:

```bash
npx skills@latest add grove/idea-to-promise --skill research
```

## Checks

Requires Python 3.11+ and no third-party Python packages:

```bash
python3 -m unittest discover -s checks -p 'test_*.py' -v
```

The [behavior scenarios](checks/scenarios.md) are evaluation cases for live
agents. Passing unit tests does not establish that an agent makes good product
decisions.

## Design principles

- Separate observations, reports, inferences, assumptions, unknowns, and preferences.
- Research the questions most likely to change the decision.
- Seek counterevidence and keep contradictions visible.
- Stop research deliberately instead of maximizing information.
- Keep recommendation, human decision, and exact promise approval distinct.
- Permit experiment, defer, and no-build outcomes.
- Preserve exact promise identity across the P2P boundary.
- Never treat source approval as implementation or publication authority.

## Contributing and license

Read [AGENTS.md](AGENTS.md), [CONTRIBUTING.md](CONTRIBUTING.md), and the
[Changelog](CHANGELOG.md).

Apache-2.0. See [LICENSE](LICENSE).
