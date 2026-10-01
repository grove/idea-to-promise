---
name: research
description: Investigate the riskiest decision-changing assumptions first. Maintain stable claim IDs, criticality, evidence strength, risk lenses, counterevidence, bounded experiments, and an explicit stopping decision.
license: Apache-2.0
metadata:
  version: "0.4.0"
---

# Research for a decision

Research should reduce the uncertainty most likely to change the decision, not
produce a generic report.

## Work record

When a work item exists, read its frame, opportunities, alternatives, current
research, experiments, and prior decisions. Save the claim ledger and synthesis
to .itp/work/<slug>/research.md. Save bounded experiments under
.itp/work/<slug>/experiments/<name>.md.

Preserve stable claim IDs across updates. Do not recycle a retired ID for a
different claim. Local writes grant no external publication or production-effect
authority.

## Find the riskiest assumptions

State the decision being informed and ask: what must be true for each viable
alternative to succeed?

For every load-bearing claim, record:
- ID: C1, C2, ...
- Kind: observation, attributed-report, inference, assumption, unknown, preference.
- Risk lens: desirability, feasibility, viability, adaptability, compliance, or
  other clearly named domain risk.
- Criticality: high, medium, low — how much the decision depends on it.
- Evidence strength: strong, moderate, weak, none — how well it is currently supported.
- Support: supported, mixed, unsupported, not-applicable.
- Evidence: retrievable source or direct observation.
- Counterevidence: contrary evidence or None.
- Decision impact: what changes if wrong.
- Next check / stop: cheapest useful check or stopping reason.

Prioritize research where criticality is high and evidence strength is weak/none.
Do not spend equal effort on every claim.

## Investigate

Order questions by expected decision impact and cost of learning. Prefer primary
documentation, the actual repository/version in question, direct observations,
and attributable user material. Record freshness when it can affect the decision.

Do not convert a report into an observation or an inference into fact. Resolve
material contradictions when possible and keep unresolved contradictions visible.

## Bounded experiments

When observation is cheaper or more credible than further discussion, propose or
run an experiment only within available authority. Use stable E1, E2, ... IDs.

Before running it, precommit to:
- question and hypothesis,
- bounded exposure,
- method,
- observation/metric,
- decision rule: what result would change the decision,
- stop condition.

After execution record environment/action actually taken, actual result,
limitations, and affected claim IDs. Never backfill the decision rule after seeing
the result.

An experiment is evidence about its actual scope. Never fabricate a run or result.

## Stop deliberately

Stop when the highest-criticality weak claims are resolved enough for the
decision, another reasonable check is unlikely to change the choice, an agreed
time/cost bound is reached, or an essential input is unavailable.

State residual uncertainty. End with an advisory synthesis: viable alternatives,
ruled-out alternatives, riskiest remaining assumptions, tradeoffs, and any
evidence-supported recommendation. Do not record a human decision.

The normal next step is:

/decide .itp/work/<slug>/research.md

If a load-bearing unknown still prevents a meaningful choice, name the exact
research or experiment needed instead. Do not implement or invoke P2P.
