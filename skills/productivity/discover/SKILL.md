---
name: discover
description: Guide an idea through framing, alternatives, decision-directed research, and a bounded source promise. Use for an end-to-end human-led discovery episode; stop at approval or an explicit no-build decision.
license: Apache-2.0
metadata:
  version: "0.1.0"
---

# Guide a discovery episode

Coordinate Idea to Promise in the current interaction. This is a human-led discovery workflow, not an autonomous controller, and it does not start implementation.

## 1. Frame
Establish the problem or opportunity, audience, desired observable outcome, constraints, decision criteria, assumptions, and material unknowns. Separate the need from the initially suggested solution.

## 2. Explore
Generate genuinely different alternatives. Include the status quo, existing/native capability, a smaller intervention, and larger approaches where useful. Explain mechanisms, tradeoffs, assumptions, reversibility, and the cheapest useful checks.

## 3. Research
Investigate only questions likely to change the decision. Use actual available sources. Maintain a claim ledger, seek counterevidence, preserve contradictions, and stop when more checking is unlikely to alter the choice or the agreed bounds are reached.

## 4. Decide and shape
Synthesize pursue/experiment/defer/reject. Ask the human for essential choices rather than inventing them. For pursue/experiment, draft a bounded source promise that separates binding outcomes/boundaries/constraints from advisory rationale and research.

## 5. Preserve and stop
Present the exact source for approval. Only report **AGREED** when a real attributable human approval covers that exact text. For an agreed promise, propose the separate next command:

```text
/plan-acceptance <source-path>
```

Do not invoke Promise to Proof automatically. Do not implement, commit product code, or publish external changes without separate authority.
