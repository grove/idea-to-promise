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

## Make choosing feel natural

The user should feel like they are choosing between understandable paths, not
operating a decision-record format. Lead with the choices and recommendation.
Keep IDs, posture labels, record paths, and history mechanics in the background
unless they help the current choice or the user asks for them.

When a choice is still needed, end with one direct question. Prefer:

"Which direction do you want to take?"

or, when the recommendation is strong:

"I recommend option 1. Shall we go with that, choose another option, or investigate
the remaining uncertainty first?"

Avoid ending with a generic workflow status or several unrelated questions.

## Present the choices for a human

Whenever you show alternatives to the user, use a numbered or bulleted list by
default so the choices are easy to scan. For each option provide:

- **What it means:** a short explanation in ordinary language.
- **Why you might choose it:** its strongest advantage for this decision.
- **Main downside:** the most important tradeoff, risk, or cost.

Prefer a few decision-relevant options over a long catalogue. Keep internal IDs
available for traceability, but never make the user understand A-IDs/C-IDs merely
to follow the choice.

Always follow the alternatives with a clearly labeled **Recommendation**. Recommend
one option when the evidence and stated preferences support it. Recommend a small
shortlist when the evidence does not distinguish a single best choice. If a
load-bearing unknown makes commitment premature, recommend the bounded experiment,
deferral, or narrower option that best reduces the uncertainty.

Explain the recommendation in plain language and name the uncertainty that could
change it. Never turn the recommendation into the human decision.

Reuse an explicit human choice and appetite already present; do not ask for them
again without a material reason. Ask only for unresolved decisions. If an unknown
blocks an unconditional build, explain what it blocks and offer a bounded
experiment, defer or no-build where applicable.

When the user chooses, acknowledge the choice plainly before discussing any
record-keeping. "We'll go with the smaller reversible option" is more useful than
"D1 is now active."

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
changes never overwrite the active choice. For defer/reject explain the stopping
point naturally and name the revisit trigger. For pursue/experiment, make the next
step obvious: shape the exact promise. Choosing an option is not approval of exact
promise text or authority to implement.

## Compound durable learning

If this work surfaces a durable, non-obvious lesson likely to help future ITP work,
invoke the `compound-learning` skill before finishing. Do not invoke it for routine
facts, one-off details, already-recorded evidence, or merely because the work was
difficult. Compounding is advisory: it must not create or replace a human decision,
change an approved promise, add scope, or silently rewrite shared ITP behavior.

