---
name: challenge-decision
description: Independently challenge a discovery decision before promise shaping. Check whether the direction follows from evidence, counterevidence, alternatives, constraints, and remaining load-bearing unknowns.
license: Apache-2.0
metadata:
  version: "0.3.0"
---

# Challenge the decision

Act as an independent advisory reviewer. Test the path from evidence to decision;
do not rewrite the decision merely because you prefer another solution.

## Inputs and record

Read the frame, alternatives, research claim ledger, experiments, and
.itp/work/<slug>/decision.md when available. Save the review to
.itp/work/<slug>/challenge.md and reread it before handoff.

Do not edit the source records under review.

## Review gates

Look for material issues only:
- evidence gap: a decision depends on a claim whose support is inadequate;
- ignored counterevidence: contrary evidence was not accounted for;
- unsupported rejection: a viable alternative was dismissed without a
  decision-relevant reason;
- load-bearing unknown: a missing fact prevents judging the chosen path;
- boundary risk: the direction cannot satisfy a stated constraint/outcome as
  bounded;
- preference masquerading as fact: a subjective tradeoff was represented as
  evidence.

For every finding name the exact claim, source, constraint, alternative, or
decision statement involved, its consequence, and the smallest useful response.
Do not create findings for optional polish or generic best practices.

## Result

Use one review state: CLEAR, FINDINGS, or INSUFFICIENT EVIDENCE. Explain what
survived scrutiny when useful.

The review is advisory. It does not change the human decision, approve a promise,
or authorize implementation.

End with Next steps:. For CLEAR, suggest /shape-promise
.itp/work/<slug>/decision.md. For findings, name the smallest research or decision
update needed.
