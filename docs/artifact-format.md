# Discovery artifact format

This document defines the lightweight v0.3 record shapes. Templates under
`templates/` are the canonical starting points.

## Local work root

Use `.itp/work/<slug>/` for active discovery state. Keep `.itp/` ignored by
default because research can be provisional or sensitive.

Core records:

- `frame.md` — problem, audience, outcome, constraints, unknowns.
- `alternatives.md` — genuinely different approaches and cheap checks.
- `research.md` — decision questions and stable claim ledger.
- `experiments/<name>.md` — bounded learning activities and actual results.
- `decision.md` — explicit attributable human choice, rationale, unknowns, tradeoffs, revisit triggers.
- `challenge.md` — independent advisory review of the decision.
- `promise-draft.md` — proposed source promise before durable publication.
- `approval.md` — exact promise revision/hash and attributable approval.
- `handoff.md` — exact source identity handed to Promise to Proof.

A project may retain selected discovery records in project-owned tracked paths.
Do not publish private or licensed research merely because a template names a
field for it.

## Decision record

The decision record is created by `/decide` only after an explicit human choice.
A leading research recommendation is not a decision.

The record must distinguish evidence-supported conclusions from preferences and
remaining unknowns, identify the selected direction, preserve why viable
alternatives were not selected, and name revisit triggers.

## Durable promise

The durable promise is a normal project-owned Markdown file such as
`specs/<slug>.md`. It contains the binding source agreement and enough context
to understand it without the ignored work directory.

Required headings for a build promise:

```markdown
# Promise: <title>

Promise revision: v1
Status: DRAFT | AGREED

## Intended outcome
## Promise
## Boundaries
## Binding constraints
## Out of scope
## Assumptions and open questions
## Advisory rationale
```

For an experiment promise, the binding content also names exposure, observation,
stop condition, and decision rule.

`AGREED` should only be written when approval for the exact bytes is being
recorded consistently. Prefer leaving the source status `DRAFT` and making
approval authoritative through `approval.md` if changing the status line would
otherwise invalidate the approved hash.

## Hashing

Promise identity is:

```text
promise:sha256:<64 lowercase hex characters>
```

Compute SHA-256 over the exact file bytes with no newline normalization. The
helper `scripts/promise_identity.py` prints this identity.

The approval record stores:
- Source
- Promise revision
- Promise identity
- Approval source
- Approved by
- Approved at/context

The handoff repeats the source, revision, identity, and approval reference so
drift can be detected without guessing.

## Claim ledger

Claims use stable IDs and the columns defined by the discovery protocol. Existing
IDs survive support-state changes and revisions. Never recycle a retired ID for a
different claim.

## Amendments

Material promise changes create a new human-readable revision and invalidate the
old approval for the changed bytes. Retain the prior source or an immutable
reference when historical traceability matters. Research updates alone do not
revise the promise unless they change binding content.
