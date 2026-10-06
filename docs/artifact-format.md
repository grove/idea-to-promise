# Records in v0.6

Use the smallest durable record that preserves the decision. Quick discovery may
use `.itp/work/<slug>/discovery.md` with Need, Options, Evidence and unknowns,
Decision, Next. A pending choice stays pending. Normal/deep work may use frame.md,
alternatives.md, research.md, experiments/, decision.md and challenge.md.
`session.md` is optional resume context, not executable workflow state. A project-level strategic review may also retain `zoom-out.md` when that review will help later decisions.

Canonical [templates](../templates/discovery.md) are aids, not mandatory forms.
Every installed skill carries the relevant copies and the same protocol.

## Identities and history

O/A/C/E IDs identify opportunities, alternatives, claims and experiments. Preserve
an ID while refining the same thing. Decision D-IDs survive clarifications, but a
materially changed human choice gets the next D-ID, a Supersedes reference, and
retained prior bytes such as `history/decision-D1.md`. Active decision status is
active/superseded/abandoned. Pending alternatives to it go in decision-proposed.md.
Do not delete or silently rewrite prior rationale or approved sources.

The decision basis describes evidence, major unknowns, reversibility and downside.
Appetite is a human-set boundary, not a delivery estimate. Source provenance
records observation versus interpretation, version/time when relevant and limits.
Retained P2P observations are advisory evidence only.

## Promise and receipts

Source promises remain ordinary project-authored UTF-8 Markdown, usually
`specs/<slug>.md`, with `Promise revision: vN` and nonempty sections Intended
outcome, Promise, Boundaries, Binding constraints, Out of scope, Assumptions and
open questions, Advisory rationale. `None` may be a deliberate section value.

Save and inspect bytes before approval. SHA-256 uses those exact bytes, not a
newline-normalized representation. Do not store the hash inside the hashed file.
A DRAFT status may remain in an approved source; the separate receipt binds exact
bytes. Any byte change needs renewed approval, and material changes increment vN.

Approval fields: Source, Promise revision, Promise identity, Approved by,
Approval source. Handoff fields: Source, Promise revision, Promise identity,
Approval. The last field names the retrievable separate approval record.
References are plain project-root-relative paths, not URLs, absolute paths or
Markdown links. Approval source is attributed text/context and may cite a URL;
the checker does not fetch or authenticate it. Duplicate or empty metadata is
invalid. Fenced examples are not metadata.

## Checker modes and compatibility

The default checker inspects present claims/experiments and a supplied promise.
It does not require every discovery artifact or imply approval. Existing approval
or handoff records require `--promise` so identity checks cannot be silently skipped.
`--handoff` additionally requires handoff.md and its referenced approval. Both
records must match actual source path, revision and digest. Escaping references,
unreadable files, mismatches, duplicate metadata and incomplete receipts fail.

v0.4 core promise sections and identity format are unchanged. Old drafts are not
rewritten. Old receipts missing attribution or handoff Approval references now
need explicit reconciliation. Never fill these fields by inventing a human
approval. Legacy table claim IDs are still inspected alongside compact C-ID lines.

These checks establish structural consistency only, not source credibility,
approver authenticity, complete Markdown semantics or implementation readiness.


## Team ownership and decision posture

For shared decisions, decision.md may record Decision owner, Consulted, Affected
and Promise approver. These fields are optional when irrelevant. They do not prove
organizational authority; they preserve what the human process actually established.

Decision posture records Evidence, Important unknowns, Reversibility, Downside if
wrong and Appetite fit. These are descriptive categories with reasons, never an
overall numeric confidence score.

## Amendments

A pending material change lives in `amendment-proposed.md`. It records the
current source/revision/identity, trigger provenance, classification, proposed
binding change, unchanged commitments and decision impact. The active approved
source and receipt remain unchanged until replacement bytes receive exact approval.

An implementation-only P2P problem does not require an amendment record. A material
replacement gets a new promise revision and fresh P2P acceptance-planning handoff.

## Outcome reviews

`outcome-review.md` binds an approved source identity to delivery evidence and
real-world observations. It records observation context, delivered behavior,
actual outcome observations, counterevidence, assumption updates, advisory learning
and decision impact.

Allowed outcome states are improved, mixed, no-improvement and not-assessed.
Without direct/attributed outcome observations, use not-assessed even when P2P proof
is green. Outcome review never mutates the approved promise.

## Zoom-out reviews

`zoom-out.md` is an optional advisory project-level review. It can record the
project's intended outcomes, material changes, current attention, work that may
deserve less focus, missed opportunities, strategic options, recommendation, and
the next human choice.

It is deliberately not an active decision record. A zoom-out review does not
supersede `decision.md`, mutate an approved promise, authorize implementation, or
create new scope. If the human chooses a material change, use the normal
decision/revisit/amend path and preserve existing history.

## Structural status

`scripts/inspect_work_item.py` reads records and optional source identity to show
structural state and a likely next action. It is read-only. Its output is not a
decision, approval, readiness verdict or execution plan.
