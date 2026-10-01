---
name: research
description: Investigate decision-changing questions about an idea or approach. Maintain stable claim IDs, evidence and counterevidence, bounded experiments, and an explicit research stopping decision.
license: Apache-2.0
metadata:
  version: "0.2.0"
---

# Research for a decision

Research should reduce specific uncertainty, not produce a generic report.

## Work record

When a work item exists, read its framing, alternatives, current research,
experiments, and decisions. Save the claim ledger and synthesis to
.itp/work/<slug>/research.md. Save bounded experiments under
.itp/work/<slug>/experiments/<name>.md.

Preserve stable claim IDs across updates. Do not recycle a retired ID for a
different claim. Local writes grant no external publication or production-effect
authority.

## Plan the investigation

State the decision being informed, ordered questions most likely to change it,
the cheapest credible source/check for each, and an explicit stopping rule.

Use only tools and sources actually available. Prefer primary documentation, the
actual repository/version in question, direct observations, and attributable user
material. Record freshness when it can affect the decision.

## Claim ledger

For every material claim use a stable ID C1, C2, ... and record:
- Kind: observation, attributed-report, inference, assumption, unknown, preference.
- Support: supported, mixed, unsupported, not-applicable.
- Evidence: retrievable source or direct observation.
- Counterevidence: contrary evidence or None.
- Decision impact: what changes if wrong.
- Next check / stop: cheapest useful check or stopping reason.

Do not convert a report into an observation, or an inference into fact. Resolve
material contradictions when possible and keep unresolved contradictions visible.

## Bounded experiments

When observation is cheaper or more credible than further discussion, propose or
run an experiment only within available authority. Use stable E1, E2, ... IDs.

Record question, hypothesis, exposure, method, observation, decision rule, stop
condition, environment/action actually taken, result, limitations, and affected
claim IDs.

An experiment is evidence about its actual scope. Do not generalize beyond what
it establishes. Never fabricate an experiment or result.

## Stop deliberately

Stop when another reasonable check is unlikely to change the decision, an agreed
time/cost bound is reached, or an essential input is unavailable. State residual
uncertainty.

End with one synthesis: pursue, experiment, defer, or reject, with the evidence
and uncertainty that support it. This is advisory until the human selects a
direction.

For consequential decisions, suggest /challenge-decision
.itp/work/<slug>/decision.md after the human decision is recorded. Do not
implement or invoke P2P.
