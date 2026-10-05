---
name: shape-promise
description: Shape a bounded beneficiary outcome and preserve exact, attributable source approval for a separate P2P handoff or amendment.
license: Apache-2.0
metadata:
  version: "0.6.0"
---

Read [the discovery protocol](references/discovery-protocol.md) before acting.
Bundled templates are optional aids, not a mandatory artifact checklist.

# Shape the source promise

Read the human-selected direction, frame, evidence and any challenge. No selected
direction means return to the missing choice, not assume the recommendation won.
Defer/reject means no build promise. Do not overwrite a decision while shaping
wording.

Explain the beneficiary's future experience versus the current workaround. A short
skeptical question is useful when it reveals ambiguity; a mandatory marketing FAQ
is not. Preserve agreed technical requirements rather than replacing them with
vague benefits. Carry appetite as binding only when explicitly adopted.

Draft Intended outcome, Promise, Boundaries, Binding constraints, Out of scope,
Assumptions and open questions, Advisory rationale. Experiments promise a bounded
learning activity and decision rule, not a favorable outcome. Leave acceptance
matrices, proof oracles, implementation decomposition and candidates to P2P.

## Make approval easy for the human

The approval conversation should feel like agreeing on wording, not operating a
cryptographic protocol.

Before asking for approval:

1. Save and reread the proposed durable source.
2. Compute and retain its exact identity internally.
3. Explain the promise in a short plain-language summary.
4. Show the exact source text that the human is being asked to approve.
5. Ask one direct question, for example:
   **"Are you happy to approve this as the agreed v1 promise?"**

Offer an equally simple revision path: "If not, tell me what you want changed."

Before approval, do not advertise `/plan-acceptance` as the next step. Keep the
call-to-action focused on this one human task: approve the exact promise or revise
it. Mention P2P only after approval has been recorded and re-verified, unless the
user explicitly asks what happens later.

Do not lead with the SHA-256 identity, receipt fields, structural-check output, or
source-state jargon. These protect the agreement but are not the user's main task.
Mention the identity briefly after the readable promise, or surface technical
details when requested or needed to explain a mismatch.

An answer such as "do that" to a recommendation selects the direction; it does not
approve later exact promise wording unless the exact wording was already shown and
the user's intent to approve it is clear.

## Recover gracefully from an early downstream command

If the user asks for `/plan-acceptance` before exact approval exists, do not respond
like a failed workflow engine. Say that the promise is drafted and there is just
one human step left. Show the exact promise (or concise summary plus the exact
source where the host can display it), then ask whether to approve it or revise it.

Do not treat `/plan-acceptance` itself as approval. Once exact approval is
recorded and verified, make the next action obvious:
`/plan-acceptance <source>`.

## Amendment discipline

When shaping a material amendment, keep the currently approved source/receipt
intact until replacement wording is separately approved. Retain the prior exact
source bytes or an immutable reference, increment the promise revision, and state
what changed and what remained binding. A P2P implementation/proof problem alone
is not permission to weaken or rewrite the promise.

## Exact approval and ownership

Only after explicit attributable approval save a separate receipt and handoff.
Reread and recompute the source identity. Do not change Status after approval.

If the decision record names a promise approver, require approval attributable to
that person/role or explain naturally who still needs to approve it; do not
silently substitute the decision owner or another participant. The checker verifies
structure, not organizational authority or human authenticity.

Use check_work_item.py with --root <project> --promise <source> --handoff for
consistency. Use inspect_work_item.py when available for read-only structural
status. Keep raw checker language out of the normal user-facing reply unless it
helps diagnose a problem.

For another checkout transfer source and approval evidence together; ignored local
paths are not portable. Source approval grants no implementation, commit,
publication or merge authority.

## Compound durable learning

If this work surfaces a durable, non-obvious lesson likely to help future ITP work,
invoke the `compound-learning` skill before finishing. Do not invoke it for routine
facts, one-off details, already-recorded evidence, or merely because the work was
difficult. Compounding is advisory: it must not create or replace a human decision,
change an approved promise, add scope, or silently rewrite shared ITP behavior.

