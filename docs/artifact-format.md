# Discovery artifact format

This document defines the lightweight v0.4 record shapes. Templates under
`templates/` are the canonical starting points.

## Local work root

Use `.itp/work/<slug>/` for active discovery state.

Core records:

- `frame.md` — actors, progress sought, current workaround, outcome, behavior change, constraints, unknowns.
- `alternatives.md` — opportunity space (O-IDs) followed by solution alternatives (A-IDs).
- `research.md` — decision questions, risk-prioritized claim ledger, and advisory synthesis.
- `experiments/<name>.md` — bounded learning activities and actual results.
- `decision.md` — explicit attributable human choice, appetite, tradeoffs, consequences, revisit triggers.
- `challenge.md` — advisory evidence review, rabbit holes, and premortem.
- `promise-draft.md` — proposed source promise before durable publication.
- `approval.md` — exact promise revision/hash and attributable approval.
- `handoff.md` — exact source identity handed to Promise to Proof.

## Opportunity and alternative IDs

Opportunities use stable O1, O2, ... IDs. They describe needs/obstacles, never
solutions. Alternatives use stable A1, A2, ... IDs and state which opportunities
they address.

## Claim ledger

Claims use stable C-IDs and record kind, risk lens, criticality, evidence
strength, claim, support, evidence, counterevidence, decision impact, and next
check/stopping reason.

High-criticality weakly evidenced claims should normally be investigated before
low-impact uncertainty.

## Decision record

The decision record is created only after an explicit human choice. It records an
appetite: how much effort, complexity, operational burden, or experiment exposure
the outcome is worth. Appetite constrains choice; it is not a delivery estimate.

The record distinguishes evidence-supported conclusions from preferences and
remaining unknowns, preserves alternatives not selected, records consequences,
and names revisit triggers.

## Challenge record

The challenge records material findings, concrete rabbit holes that may threaten
the outcome/appetite, and a grounded premortem. It is advisory and does not rewrite
the decision.

## Durable promise

The durable promise remains a normal project-owned Markdown file such as
`specs/<slug>.md`. It contains the binding source agreement and enough context
to understand it without ignored discovery files.

Required headings remain: Intended outcome, Promise, Boundaries, Binding
constraints, Out of scope, Assumptions and open questions, Advisory rationale.

Before approval, shape-promise should be able to explain the beneficiary's future
experience and why it is meaningfully better than the current workaround.

## Hashing and amendments

Promise identity remains `promise:sha256:<64 lowercase hex>`, computed over exact
file bytes. Approval and handoff repeat source, revision, identity, and approval
reference. Any byte change invalidates the old approval.

Material promise changes require a new revision and renewed approval. Research or
challenge updates alone do not revise the promise unless binding content changes.
