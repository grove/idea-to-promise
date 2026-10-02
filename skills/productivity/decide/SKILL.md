---
name: decide
description: Present real tradeoffs and record the attributable human choice, ownership, appetite, decision posture and history.
license: Apache-2.0
metadata:
  version: "0.6.0"
---

Read [the discovery protocol](references/discovery-protocol.md) before acting.
Bundled templates are optional aids, not a mandatory artifact checklist.

# Make the choice explicit

Read context and any existing decision. Present only genuinely relevant choices,
with the reason other alternatives left contention. Keep a viable existing/native
solution in contention. Explain evidence, uncertainty, preference, reversibility,
cost of being wrong, and appetite in ordinary language. Appetite is what the
outcome is worth, not an estimate or a promise about delivery time.

Reuse an explicit human choice and appetite already present; do not ask for them
again without a material reason. Ask only for unresolved decisions. A recommendation
stays advisory. If an unknown blocks an unconditional build, explain what it blocks
and offer a bounded experiment, defer or no-build where applicable.

## Ownership without bureaucracy

For an individual decision, do not force team-role fields. For shared decisions,
record only the distinctions that matter:

- Decision owner: who has authority to choose the direction.
- Consulted: material contributors whose input informed the choice.
- Affected: important groups/roles that bear consequences, when useful.
- Promise approver: person/role expected to approve exact source wording if
  different from the decision owner.

If authority is materially ambiguous, leave the choice pending and ask the smallest
ownership question needed. Do not infer organizational authority from participation.

## Decision posture

After an attributable choice record pursue/experiment/defer/reject and the actual
statement/context. Include supporting C/A/O IDs when used, preferences, unknowns,
appetite, consequences, revisit triggers and a compact posture:

- Evidence: strong / moderate / weak / mixed / unknown.
- Important unknowns: none / bounded / load-bearing, with names.
- Reversibility: high / medium / low.
- Downside if wrong: low / medium / high, with reason.
- Appetite fit: good / uncertain / poor.

These are descriptive categories, not a confidence score or prediction. Preserve
the underlying evidence; do not mechanically compute an overall rating.

Preserve decision history under the protocol's D-ID/supersession rules. Proposed
changes never overwrite the active choice. For defer/reject stop with NO PROMISE
and a revisit trigger. For pursue/experiment suggest `/shape-promise <decision>`;
`/challenge-decision <decision>` is optional when consequential. Choosing an option
is not approval of exact promise text or authority to implement.
