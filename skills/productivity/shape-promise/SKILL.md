---
name: shape-promise
description: Turn a human-selected direction and decision-relevant evidence into a revisioned source promise, exact approval receipt, and drift-detectable handoff to Promise to Proof.
license: Apache-2.0
metadata:
  version: "0.3.0"
---

# Shape the promise

Turn a selected direction into source material suitable for human agreement. This
is not a Promise to Proof acceptance contract or implementation plan.

## Establish the selected direction

Read the frame, alternatives, research, experiments, decision, and challenge
record when present. Do not assume the leading recommendation was selected.

Valid directions are pursue, experiment, defer, and reject.

For defer or reject, record rationale and revisit trigger in the decision record
and return NO PROMISE. Do not manufacture a build promise.

## Draft

For pursue or an experiment worth committing to, save
.itp/work/<slug>/promise-draft.md with these sections: title, Promise revision,
Status: DRAFT, Intended outcome, Promise, Boundaries, Binding constraints, Out of
scope, Assumptions and open questions, Advisory rationale.

For an experiment promise, binding content also names bounded exposure,
observation, stop condition, and decision rule. Promise the learning activity,
not a favorable result.

Do not add acceptance matrices, seams, proof oracles, implementation tasks,
candidate identities, or proof verdicts.

## Revision rules

Use human-readable revisions v1, v2, ... . Material changes to promised behavior,
boundaries, binding constraints, or experiment decision rules require a new
revision and renewed approval. Advisory research changes alone need not revise
the promise unless binding content changes.

## Exact approval

Present the exact proposed durable source text for human approval. A
recommendation, saved draft, issue label, or heading is not approval.

After the human explicitly approves that exact text:
1. save it to a project-owned durable path such as specs/<slug>.md;
2. compute SHA-256 over exact file bytes with no normalization;
3. save .itp/work/<slug>/approval.md naming source path, revision,
   promise:sha256:<hash>, approver/approval source, and context;
4. recompute the hash and require it still matches;
5. save .itp/work/<slug>/handoff.md with the same identity and approval reference.

If saving or hash verification fails, report approval handoff incomplete. If any
promise byte changes, the old approval does not cover it.

Do not silently change Status after hashing if doing so changes approved bytes.
The approval receipt is authoritative for exact identity.

## Handoff

Only after exact approval and a matching hash report AGREED and give:
/plan-acceptance <durable-source-path>

Do not invoke P2P automatically. Source approval does not approve its later
acceptance contract or authorize implementation, commit, push, publication, or
merge.
