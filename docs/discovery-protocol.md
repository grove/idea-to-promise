# Discovery protocol

Idea to Promise (ITP) turns an uncertain idea into a researched, explicit source
promise worth making. It stops before acceptance planning and implementation.

## Boundary

ITP answers **what should we promise, and why?** Promise to Proof (P2P) answers
**what exactly would make that promise true, can we implement it faithfully, and
can we prove it?**

```text
idea → frame → alternatives → research ↔ experiment → decision → source promise
                                                               ↓
                                                        Promise to Proof
```

ITP must not create P2P acceptance matrices, select proof oracles, invent
candidate identities, declare implementation acceptance, or treat source approval
as delivery authority.

## Work item

Active discovery records live under:

```text
.itp/work/<slug>/
├── frame.md
├── alternatives.md
├── research.md
├── experiments/
│   └── <experiment>.md
├── decision.md
├── promise-draft.md
├── challenge.md
├── approval.md
└── handoff.md
```

Not every record is required. The path is a local working convention and is
normally ignored by Git. It may contain sensitive or provisional material.

The durable product output is a normal project-owned source document, commonly:

```text
specs/<slug>.md
```

A final promise must stand on its own. It must not require a future reader to
recover ignored `.itp/` files or a previous conversation merely to understand
the binding outcome, boundaries, and constraints.

## Stable identities

Within a work item use stable IDs for material research claims: `C1`, `C2`, …
Do not renumber an existing claim just because its support changes. Allocate a
new ID for a materially different claim.

Experiments may use `E1`, `E2`, … and decisions `D1`, `D2`, … when multiple
records need to be referenced.

A promise carries a human-readable revision such as `v1`, `v2`, … . Material
changes to promised behavior, boundaries, binding constraints, or experiment
decision rules require a new revision and renewed approval.

The immutable identity of an approval is the SHA-256 of the exact UTF-8 bytes of
the durable promise file. The hash is stored in `approval.md` or another durable
approval record, not inside the hashed promise itself.

## Evidence discipline

Research is decision-directed. First state the decision being informed and order
questions by how likely their answers are to change that decision.

For each material claim record:

| Field | Meaning |
|---|---|
| ID | Stable claim ID |
| Kind | observation, attributed-report, inference, assumption, unknown, preference |
| Claim | One decision-relevant statement |
| Support | supported, mixed, unsupported, not-applicable |
| Evidence | Retrievable source or direct observation |
| Counterevidence | Evidence that weakens or contradicts the claim |
| Decision impact | What changes if this claim is wrong |
| Next check / stop | Cheapest useful check, or why more checking is not worth it |

Do not convert user reports into observations. Do not convert an inference into a
fact because it is plausible. Do not fabricate citations, interviews,
measurements, experiments, precision, or consensus.

Prefer primary documentation, the actual repository/version in question, direct
observations, and attributable user material. Record source freshness when it can
change the decision.

Research stops when another reasonable check is unlikely to alter the choice, an
agreed time/cost bound is reached, or an essential input is unavailable. Report
the residual uncertainty rather than hiding it.

## Experiments

Use an experiment when a load-bearing question can be answered more cheaply or
credibly by observation than by more discussion.

A bounded experiment records:

- ID and question
- hypothesis
- scope/exposure
- method
- observation or metric
- decision rule
- stop condition
- environment and exact action actually taken
- result
- limitations
- claim IDs updated by the result

An experiment promise commits to performing a bounded learning activity and
applying its decision rule. It never promises a favorable result.

Experiments do not receive production authority from this protocol. External or
persistent effects require the same explicit authority they would require outside
ITP.

## Decision

A decision record distinguishes:

- evidence-supported conclusions,
- unresolved load-bearing unknowns,
- preferences/tradeoffs,
- the human-selected direction,
- alternatives rejected or deferred and why,
- revisit triggers.

Valid terminal directions are `pursue`, `experiment`, `defer`, and `reject`.
A no-build outcome is valid; never manufacture a promise solely to continue the
workflow.

## Independent challenge

Before shaping a consequential promise, a separate `challenge-decision` review
may test whether the decision follows from the evidence, whether important
counterevidence was ignored, whether alternatives were dismissed for unsupported
reasons, and whether load-bearing unknowns remain.

Challenge findings are advisory. They cannot silently change the decision or
promise.

## Promise and approval

A source promise separates binding content from advisory rationale.

Binding:
- intended observable outcome,
- promised behavior,
- boundaries,
- non-goals,
- binding constraints,
- for an experiment: exposure, observation, stop and decision rules.

Advisory:
- research summary,
- rationale,
- alternatives,
- implementation ideas.

A proposal is `DRAFT` until a human approves the exact durable source text.
Approval must name the promise path, revision, exact SHA-256, approver or
attributable approval source, and approval time/context when available.

A saved file, recommendation, issue label, or heading is not approval.

If the promise bytes change after approval, the old approval no longer covers the
new source. Create a new revision and obtain renewed approval.

## Handoff to Promise to Proof

After exact source approval, create a handoff record containing the durable source
path, revision, exact SHA-256, and approval reference. Then invoke P2P separately:

```text
/plan-acceptance <agreed-source-path>
```

P2P applies its own acceptance planning and approval rules. ITP approval does not
approve a later P2P acceptance contract and does not authorize implementation,
commit, push, publication, or merge.
