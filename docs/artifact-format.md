# Records in v0.5

Use the smallest durable record that preserves the decision. Quick discovery may
use `.itp/work/<slug>/discovery.md` with Need, Options, Evidence and unknowns,
Decision, Next. A pending choice stays pending. Normal/deep work may use frame.md,
alternatives.md, research.md, experiments/, decision.md and challenge.md.
`session.md` is optional resume context, not executable workflow state.

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
