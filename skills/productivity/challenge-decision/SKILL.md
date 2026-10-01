---
name: challenge-decision
description: Independently challenge a discovery decision before promise shaping. Check evidence, counterevidence, alternatives, appetite, rabbit holes, likely failure modes, constraints, and remaining load-bearing unknowns.
license: Apache-2.0
metadata:
  version: "0.4.0"
---

# Challenge the decision

Act as an independent advisory reviewer. Test the path from evidence to decision;
do not rewrite the decision merely because you prefer another solution.

## Inputs and record

Read the frame, opportunities, alternatives, research claim ledger, experiments,
and .itp/work/<slug>/decision.md when available. Save the review to
.itp/work/<slug>/challenge.md and reread it before handoff.

Do not edit the source records under review.

## Evidence and decision review

Look for material issues only:
- evidence gap,
- ignored counterevidence,
- unsupported rejection,
- load-bearing unknown,
- boundary risk,
- appetite mismatch,
- preference masquerading as fact.

For every finding name the exact claim, source, constraint, alternative, appetite,
or decision statement involved, its consequence, and the smallest useful response.

## Rabbit-hole check

Ask where the chosen direction could hide disproportionate complexity, dependency,
migration, operational, security, adoption, integration, or organizational work.

Only raise a rabbit hole when there is a concrete reason it could threaten the
outcome or appetite. Do not generate a generic risk checklist.

For each material rabbit hole state the trigger, evidence/uncertainty, potential
effect on the appetite/outcome, and cheapest way to bound it.

## Premortem

Assume the decision was pursued and six months later it clearly failed to deliver
the intended outcome. Identify the few most plausible reasons, grounded in the
current context.

Then ask whether each failure mode is:
- already covered,
- worth one bounded check,
- a reason to change the decision,
- acceptable residual risk.

The premortem is not permission to invent exotic failure stories. Prefer plausible
causal paths supported by the current work.

## Result

Use one review state: CLEAR, FINDINGS, or INSUFFICIENT EVIDENCE. Explain what
survived scrutiny when useful.

The review is advisory. It does not change the human decision, approve a promise,
or authorize implementation. Do not create findings for optional polish.

End with Next steps:. For CLEAR, suggest /shape-promise
.itp/work/<slug>/decision.md. For findings, name the smallest research or decision
update needed.
