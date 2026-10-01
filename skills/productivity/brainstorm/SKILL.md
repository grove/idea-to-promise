---
name: brainstorm
description: Explore the opportunity space before generating genuinely different solution paths. Preserve stable opportunity and alternative IDs, and include status quo, existing capabilities, smaller interventions, and materially distinct mechanisms.
license: Apache-2.0
metadata:
  version: "0.4.0"
---

# Explore opportunities, then alternatives

Do not jump directly from a broad problem to feature ideas.

## Work record

When a work item exists, read frame.md and save the combined opportunity and
alternative exploration to .itp/work/<slug>/alternatives.md. Preserve prior
records when materially replacing them. Local saving grants no external-write or
implementation authority.

## 1. Explore the opportunity space

Start from the actors, progress sought, current workaround, intended outcome, and
decision criteria.

Identify distinct needs, obstacles, or opportunities that could explain the gap.
Use stable IDs O1, O2, ... . Each opportunity should describe a problem or desired
progress, not a solution.

For each opportunity state:
- actor,
- situation,
- unmet need / obstacle,
- why it matters to the intended outcome,
- evidence or assumption status,
- what would make it important enough to act on.

Do not force every possible opportunity into scope. Highlight the few that appear
most decision-relevant and identify what would change that view.

## 2. Explore the solution space

For the most relevant opportunity or opportunity set, generate materially
different mechanisms. Include when useful:

- doing nothing / preserving current behavior,
- an existing or native capability,
- a smaller, manual, procedural, or reversible intervention,
- one or more substantial solution approaches.

Use stable IDs A1, A2, ... . Do not count cosmetic variants of one architecture as
independent alternatives.

For each credible alternative state mechanism, which O-IDs it addresses, why it
could satisfy the outcome, tradeoffs, prerequisites, reversibility,
decision-critical assumptions, and cheapest credible check.

Clearly label unverified statements as assumptions or hypotheses.

## Compare without false precision

Compare against the actual decision criteria. Do not invent market facts, user
preferences, performance numbers, certainty, or arbitrary scores. Identify which
unanswered questions could change the ordering.

Save and reread when a work item exists. A leading option is a recommendation,
not a human decision and not an approved promise. Do not implement, publish, or
invoke Promise to Proof.

End with Next steps: and numbered options, normally /research
.itp/work/<slug>/alternatives.md or /decide only when no material research
question remains.
