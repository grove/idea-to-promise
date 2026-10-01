---
name: discover
description: Guide an idea through durable framing, alternatives, decision-directed research, explicit human decision, optional decision challenge, and exact source-promise approval before a separate Promise to Proof handoff.
license: Apache-2.0
metadata:
  version: "0.3.0"
---

# Guide a discovery episode

Coordinate Idea to Promise in the current interaction. This is a human-led
discovery workflow, not an autonomous product controller, and it stops before
implementation.

When working in a writable repository, keep local records under
.itp/work/<slug>/. The final agreed source promise belongs in a normal
project-owned path such as specs/<slug>.md.

## 1. Frame

Establish problem/opportunity, audience, observable intended outcome, constraints,
decision criteria, assumptions, material unknowns, and research bounds. Separate
the need from the initially proposed solution. Save frame.md.

## 2. Explore

Generate materially different alternatives. Include status quo, existing/native
capability, smaller/reversible intervention, and larger approaches where useful.
Use stable A1, A2, ... IDs. Save alternatives.md.

## 3. Research

Investigate only questions likely to change the decision. Use actual available
sources, stable C1, C2, ... claim IDs, explicit evidence/counterevidence, and a
stopping rule. Save research.md.

When observation is the cheapest credible answer, use a bounded E1, E2, ...
experiment within actual authority and save it under experiments/. Never invent
results.

Research may recommend a direction, but it must not silently turn that
recommendation into the human decision.

## 4. Decide

Present the viable choices and real tradeoffs in plain language. Distinguish
evidence, uncertainty, preferences, and constraints.

If a load-bearing unknown prevents a responsible choice, return to research or a
bounded experiment.

Otherwise ask the human to choose pursue, experiment, defer, or reject. Only
after an explicit human choice save decision.md with the attributable selection,
evidence-supported conclusions, preferences/tradeoffs, alternatives not selected,
and revisit triggers.

## 5. Challenge when useful

For consequential work, independently challenge evidence-to-decision traceability,
ignored counterevidence, unsupported alternative rejection, constraints, and
load-bearing unknowns. Save challenge.md. Findings are advisory and do not replace
the human decision.

Small, reversible decisions may proceed without this optional challenge.

## 6. Shape and approve

For pursue/experiment, draft a revisioned source promise separating binding
outcome/boundaries/constraints from advisory rationale. Save promise-draft.md.

Present the exact durable source text. Only after explicit human approval: save
the durable source, compute exact-byte SHA-256, record approval in approval.md,
reread/re-hash, and record a matching handoff.md.

Any byte change invalidates that approval. For defer/reject, stop with NO PROMISE.

## 7. Stop at the boundary

For an exact approved source with matching identity, give:

/plan-acceptance <source-path>

Do not invoke P2P automatically. Do not implement product code, commit, push, or
publish external changes without separate authority.
