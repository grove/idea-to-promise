---
name: decide
description: Turn research and viable alternatives into a clear human decision. Present the real choices and tradeoffs, surface load-bearing unknowns, ask the human to choose, and save the attributable decision without pretending evidence made the choice automatically.
license: Apache-2.0
metadata:
  version: "0.3.0"
---

# Make the decision explicit

Help the human choose what to do with the research. Evidence informs the decision;
it does not silently make the decision.

## Inputs and work record

Read the current frame, alternatives, research claim ledger, experiments, and any
existing decision record. When a work item exists, save the final human choice to:

.itp/work/<slug>/decision.md

Do not create a final decision record merely because research has a leading
recommendation.

## Reduce to the real choices

Discard alternatives that are clearly infeasible, already satisfied by existing
behavior, or contradicted by established constraints, but preserve the reason they
left contention.

Present only the choices that remain genuinely decision-relevant. For each, state
in plain language:

- what it means,
- which intended outcome it addresses,
- strongest supporting evidence,
- important counterevidence or uncertainty,
- main tradeoffs,
- reversibility,
- what would have to be true for it to be a good choice.

Do not use arbitrary scores, fake precision, or a generic pros/cons dump.

## Separate evidence from preference

Make clear which parts of the choice are:

- established or supported by evidence,
- still uncertain,
- value judgments or preferences,
- constraints that rule choices in or out.

If a load-bearing unknown prevents a responsible choice, say DECISION BLOCKED and
give the smallest useful research or experiment needed. Do not pressure the human
to choose anyway.

## Ask for the human choice

When the viable options and tradeoffs are clear, ask the human to choose among:

- pursue <option>,
- experiment before choosing,
- defer,
- reject / no-build.

You may recommend a direction when the evidence supports one, but label it as a
recommendation. Never record your recommendation as the human decision.

## Save the decision

Only after an explicit attributable human choice, save:

# Decision: <work item>

Decision ID: D1
Direction: pursue | experiment | defer | reject

## Selected direction
<what the human chose>

## Evidence-supported conclusions
- C1 — <conclusion>

## Load-bearing unknowns
- <remaining unknown or None>

## Preferences and tradeoffs
- <human preference distinguished from evidence>

## Alternatives not selected
- A1 — <reason>

## Human decision
Selected by: <person or attributable source>
Decision context: <conversation, issue, meeting, etc.>

## Revisit triggers
- <condition that should reopen the decision>

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
