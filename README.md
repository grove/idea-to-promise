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
/decide <research>
/challenge-decision <decision record>
/shape-promise <decision record>
```

These are agent skills, not shell commands.

## Seven skills

| Skill | Main question |
|---|---|
| [`frame`](skills/productivity/frame/SKILL.md) | What progress is someone actually trying to make, and what happens today? |
| [`brainstorm`](skills/productivity/brainstorm/SKILL.md) | What underlying opportunities exist, and what genuinely different solutions could address them? |
| [`research`](skills/productivity/research/SKILL.md) | Which load-bearing assumptions are weakly evidenced, and what should we learn first? |
| [`decide`](skills/productivity/decide/SKILL.md) | Given the evidence and our appetite, what do we choose? |
| [`challenge-decision`](skills/productivity/challenge-decision/SKILL.md) | What could blow up the decision or make it fail? |
| [`shape-promise`](skills/productivity/shape-promise/SKILL.md) | What future experience are we actually willing to promise? |
| [`discover`](skills/productivity/discover/SKILL.md) | How do we guide the whole discovery loop? |

The stages are intentionally not rigid. New evidence may send the work back to
framing, opportunities, or research. A no-build result is valid.

## The v0.4 discovery loop

```text
real need / job
      ↓
opportunity space
      ↓
solution alternatives
      ↓
riskiest assumptions
      ↓
research ↔ bounded experiment
      ↓
human decision + appetite
      ↓
rabbit holes + premortem (when useful)
      ↓
future-experience check
      ↓
exact approved promise
      ↓
Promise to Proof
```

The main ideas are simple:

- Understand the real progress sought before discussing features.
- Explore the problem/opportunity space before the solution space.
- Research the weakest load-bearing assumptions first.
- Decide how much the outcome is worth before accepting complexity.
- Try to explain how the decision could fail before committing.
- Make sure the promised future is actually better for the beneficiary.

## Work-item model

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

The final agreed promise is a normal project-owned source document, commonly
`specs/<slug>.md`. It must stand on its own.

See the [artifact format](docs/artifact-format.md),
[discovery protocol](docs/discovery-protocol.md), and
[workflow guide](docs/how-to.md).

## Research discipline

Research uses stable claim IDs C1, C2, ... and now also records:

- **criticality** — how much the decision depends on the claim,
- **evidence strength** — how well it is supported,
- **risk lens** — e.g. desirability, feasibility, viability, adaptability, compliance.

ITP prioritizes high-criticality claims with weak/no evidence rather than
researching everything equally.

Experiments precommit to the observation, decision rule, and stop condition before
the result is known.

## Decision discipline

`/decide` separates evidence from preference and asks the human to set an
**appetite**: how much effort, complexity, operational burden, or experiment risk
the outcome is worth. Appetite is a decision boundary, not an implementation
estimate.

For consequential choices, `/challenge-decision` looks for concrete rabbit holes
and runs a grounded premortem: assume the decision failed and ask why.

## Promise discipline

Before drafting, `/shape-promise` works backwards from the beneficiary's future
experience. If the promise cannot explain what is meaningfully better without
falling back to implementation details, it is not ready.

Promises retain exact-byte SHA-256 identity and explicit approval before handoff
to P2P.

## Handoff to Promise to Proof

After exact source approval and a matching identity:

```text
/plan-acceptance specs/<slug>.md
```

ITP does not create the P2P acceptance contract or authorize implementation.

## Install

```bash
npx skills@latest add grove/idea-to-promise
```

## Checks

Requires Python 3.11+ and no third-party Python packages:

```bash
python3 -m unittest discover -s checks -p 'test_*.py' -v
```

The [behavior scenarios](checks/scenarios.md) are evaluation cases for live
agents. Passing unit tests does not prove good product judgment.

## Contributing and license

Read [AGENTS.md](AGENTS.md), [CONTRIBUTING.md](CONTRIBUTING.md), and the
[Changelog](CHANGELOG.md).

Apache-2.0. See [LICENSE](LICENSE).
