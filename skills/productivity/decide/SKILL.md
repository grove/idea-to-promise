---
name: decide
description: Turn research and viable alternatives into a clear human decision. Present the real choices and tradeoffs, set an explicit appetite for the outcome, surface load-bearing unknowns, ask the human to choose, and save the attributable decision.
license: Apache-2.0
metadata:
  version: "0.4.0"
---

# Make the decision explicit

Help the human choose what to do with the research. Evidence informs the decision;
it does not silently make the decision.

## Inputs and work record

Read the frame, opportunities, alternatives, research claim ledger, experiments,
and any existing decision record. When a work item exists, save the final human
choice to .itp/work/<slug>/decision.md.

Do not create a final decision record merely because research has a leading
recommendation.

## Reduce to the real choices

Discard alternatives that are clearly infeasible, already satisfied by existing
behavior, or contradicted by established constraints, but preserve the reason they
left contention.

Present only genuinely decision-relevant choices. For each state:
- what it means,
- which opportunity/outcome it addresses,
- strongest supporting evidence,
- important counterevidence or uncertainty,
- main tradeoffs,
- reversibility,
- riskiest remaining assumption,
- what would have to be true for it to be a good choice.

Do not use arbitrary scores, fake precision, or a generic pros/cons dump.

## Set the appetite

Before committing to a substantial direction, ask how much the outcome is worth.
Appetite is a decision boundary, not an implementation estimate.

Record a practical bound such as:
- small / medium / large effort,
- days / weeks / quarter-scale attention,
- acceptable complexity or operational burden,
- maximum exposure/risk for an experiment.

Do not promise that implementation will fit the appetite. Instead use it to reject,
shrink, or reshape options whose likely scope is incompatible with what the human
is willing to spend.

For trivial or already bounded work, appetite may be "not material".

## Separate evidence from preference

Make clear which parts of the choice are evidence, uncertainty, value judgments,
preferences, appetite, and binding constraints.

If a load-bearing unknown prevents a responsible choice, say DECISION BLOCKED and
give the smallest useful research or experiment needed. Do not pressure the human
to choose anyway.

## Ask for the human choice

Ask the human to choose:
- pursue <option>,
- experiment before choosing,
- defer,
- reject / no-build.

You may recommend a direction when evidence supports one, but label it as a
recommendation. Never record your recommendation as the human decision.

## Save the decision

Only after an explicit attributable human choice, save Decision ID, Direction,
Selected direction, Appetite, Evidence-supported conclusions, Load-bearing
unknowns, Preferences and tradeoffs, Alternatives not selected, Human decision,
Consequences, and Revisit triggers.

Use a stable D-ID when revising the same decision. If the human changes the
selected direction later, preserve the prior decision in history when practical
and record the new decision context.

## Handoff

For consequential decisions, suggest:

/challenge-decision .itp/work/<slug>/decision.md

For small or readily reversible work where independent challenge adds little,
suggest:

/shape-promise .itp/work/<slug>/decision.md

Do not shape the promise yourself, implement, publish, or invoke Promise to Proof.
