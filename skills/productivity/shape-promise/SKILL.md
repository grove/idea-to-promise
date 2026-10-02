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
Defer/reject means NO PROMISE. Do not overwrite a decision while shaping wording.

Explain the beneficiary's future experience versus the current workaround. A short
skeptical question is useful when it reveals ambiguity; a mandatory marketing FAQ
is not. Preserve agreed technical requirements rather than replacing them with
vague benefits. Carry appetite as binding only when explicitly adopted.

Draft Intended outcome, Promise, Boundaries, Binding constraints, Out of scope,
Assumptions and open questions, Advisory rationale. Experiments promise a bounded
learning activity and decision rule, not a favorable outcome. Leave acceptance
matrices, proof oracles, implementation decomposition and candidates to P2P.

## Amendment discipline

When shaping a material amendment, keep the currently approved source/receipt
intact until replacement wording is separately approved. Retain the prior exact
source bytes or an immutable reference, increment the promise revision, and state
what changed and what remained binding. A P2P implementation/proof problem alone
is not permission to weaken or rewrite the promise.

## Exact approval and ownership

Save and reread the proposed durable source before asking approval. Use the bundled
promise_identity.py against exact bytes; never invent a digest. Show the exact
wording and identity. Only after explicit attributable approval save a separate
receipt and handoff. Reread and recompute. Do not change Status after approval.

If the decision record names a promise approver, require approval attributable to
that person/role or report the approval gate unresolved; do not silently substitute
the decision owner or another participant. The checker verifies structure, not
organizational authority or human authenticity.

Use check_work_item.py with --root <project> --promise <source> --handoff for
consistency. Use inspect_work_item.py when available for read-only structural
status. Missing storage/tool/approval means handoff pending, not AGREED.

For another checkout transfer source and approval evidence together; ignored local
paths are not portable. Propose `/plan-acceptance <source>` separately. Source
approval grants no implementation, commit, publication or merge authority.
