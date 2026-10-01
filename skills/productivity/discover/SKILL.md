---
name: discover
description: Guide an idea through need framing, opportunity exploration, risk-prioritized research, explicit human decision with appetite, optional premortem challenge, and exact source-promise approval before Promise to Proof.
license: Apache-2.0
metadata:
  version: "0.4.0"
---

# Guide a discovery episode

Coordinate Idea to Promise in the current interaction. This is a human-led
discovery workflow, not an autonomous product controller, and it stops before
implementation.

When working in a writable repository, keep local records under
.itp/work/<slug>/. The final agreed source promise belongs in a normal
project-owned path such as specs/<slug>.md.

## 1. Frame the need

Establish actors, progress sought, current workaround, intended outcome,
behavior/change needed, constraints, decision criteria, status-quo consequence,
assumptions, material unknowns, and research bounds. Separate the need from the
initially proposed solution. Save frame.md.

## 2. Explore opportunities, then solutions

First identify distinct opportunity/need statements using stable O1, O2, ... IDs.
Then generate materially different alternatives A1, A2, ... for the most relevant
opportunities. Include status quo, existing/native capability, smaller/reversible
interventions, and larger approaches where useful. Save alternatives.md.

## 3. Research the riskiest assumptions

Ask what must be true for viable alternatives to succeed. Use stable C1, C2, ...
claim IDs, explicit evidence/counterevidence, criticality, evidence strength, and
risk lenses. Investigate high-criticality weakly supported claims first.

When observation is the cheapest credible answer, use a bounded E1, E2, ...
experiment with a precommitted decision rule and stop condition. Never invent
results. Save research.md and experiments/.

Research may recommend a direction, but it must not silently become the human
decision.

## 4. Decide with an appetite

Present the viable choices and real tradeoffs. Distinguish evidence, uncertainty,
preferences, appetite, and constraints.

Ask how much effort/complexity/risk the outcome is worth. Appetite is a decision
boundary, not an estimate.

If a load-bearing unknown prevents a responsible choice, return to research.
Otherwise ask the human to choose pursue, experiment, defer, or reject. Save the
explicit attributable choice in decision.md.

## 5. Challenge when useful

For consequential work, independently review evidence-to-decision traceability,
appetite fit, and material unknowns. Then:
- inspect likely rabbit holes that could blow the appetite,
- run a grounded premortem: assume the decision failed and identify the few most
  plausible reasons.

Save challenge.md. Findings are advisory. Small, reversible decisions may skip
this stage.

## 6. Shape and approve

Before drafting, work backwards from the beneficiary's future experience. Make
sure the promised world is clearly better than the current workaround and that
the promise addresses the chosen opportunity rather than merely naming a feature.

For pursue/experiment, draft a revisioned source promise. Present the exact durable
source text. Only after explicit human approval save it, compute exact-byte
SHA-256, record approval, reread/re-hash, and record a matching handoff.

Any byte change invalidates that approval. For defer/reject, stop with NO PROMISE.

## 7. Stop at the boundary

For an exact approved source with matching identity, give:
/plan-acceptance <source-path>

Do not invoke P2P automatically. Do not implement product code, commit, push, or
publish external changes without separate authority.
