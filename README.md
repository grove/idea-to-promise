# Idea to Promise

Turn an uncertain idea into a researched, explicit promise worth making.

**Idea to Promise → Promise to Proof**

Idea to Promise helps decide **what to promise, and why**. Its sibling,
[Promise to Proof](https://github.com/grove/promise-to-proof), turns that agreed
outcome into an acceptance contract, implements it, and checks the result.

Discovery can also end in an experiment, a deferred decision, or a deliberate
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
/shape-promise <selected direction and evidence>
```

These are agent skills, not shell commands. Invoke them through a compatible
host's skill interface.

## Five skills

| Skill | Question | Result |
|---|---|---|
| [`frame`](skills/productivity/frame/SKILL.md) | What problem are we actually addressing? | Outcome, audience, constraints, unknowns, decision criteria |
| [`brainstorm`](skills/productivity/brainstorm/SKILL.md) | What genuinely different paths could work? | Alternatives, tradeoffs, assumptions, cheapest checks |
| [`research`](skills/productivity/research/SKILL.md) | What would change the decision? | Claim ledger, evidence, counterevidence, stopping decision |
| [`shape-promise`](skills/productivity/shape-promise/SKILL.md) | What are we prepared to promise? | Bounded source promise or explicit no-build outcome |
| [`discover`](skills/productivity/discover/SKILL.md) | How do we move the idea forward end-to-end? | Human-led discovery episode |

The stages are intentionally not a rigid pipeline. Start where useful, revisit
alternatives when evidence changes the picture, and stop when the right decision
is not to build.

## Install

```bash
npx skills@latest add grove/idea-to-promise
```

Install one skill:

```bash
npx skills@latest add grove/idea-to-promise --skill research
```

## Handoff to Promise to Proof

Idea to Promise owns framing, alternatives, decision-directed research, and the
final agreed source promise. Promise to Proof owns acceptance planning,
implementation, review, and proof.

```text
idea → frame → brainstorm → research → decision → agreed source promise
                                                     ↓
                                      /plan-acceptance <source>
                                                     ↓
                                             Promise to Proof
```

A source promise should state the observable intended outcome, promised behavior,
boundaries/non-goals, binding constraints, and important remaining assumptions.
It should not contain a P2P acceptance matrix, proof verdict, or implementation
candidate identity.

Read the [workflow guide](docs/how-to.md),
[discovery protocol](docs/discovery-protocol.md), and
[P2P handoff guide](docs/p2p-handoff.md).

## Design principles

- Separate observations, reports, inferences, assumptions, unknowns, and preferences.
- Research the questions most likely to change the decision.
- Seek counterevidence and keep contradictions visible.
- Keep recommendation, human decision, and approval of exact promise wording distinct.
- Treat experiment outcomes as unknown until observed.
- Allow defer and no-build outcomes.
- Never treat source approval as implementation or publication authority.

## Contributing and license

Read [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

Apache-2.0. See [LICENSE](LICENSE).
