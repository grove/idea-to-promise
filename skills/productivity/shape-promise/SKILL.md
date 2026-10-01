---
name: shape-promise
description: Turn a human-selected direction and decision-relevant evidence into a revisioned source promise, test the future experience from the beneficiary's perspective, record exact approval, and create a drift-detectable handoff to Promise to Proof.
license: Apache-2.0
metadata:
  version: "0.4.0"
---

# Shape the promise

Turn a selected direction into source material suitable for human agreement. This
is not a Promise to Proof acceptance contract or implementation plan.

## Establish the selected direction

Read the frame, opportunities, alternatives, research, experiments, decision, and
challenge record when present. Do not assume the leading recommendation was
selected.

Valid directions are pursue, experiment, defer, and reject.

For defer or reject, record rationale and revisit trigger in the decision record
and return NO PROMISE. Do not manufacture a build promise.

## Future-experience check

Before drafting the promise, work backwards from the beneficiary's future
experience.

In plain language answer:
- If this promise were already true, what would the actor now be able to do,
  understand, avoid, or accomplish?
- How would that be meaningfully better than the current workaround?
- Which opportunity IDs does it actually address?
- Why would the beneficiary care?
- What skeptical question would expose that the promise is too vague, too broad,
  or solution-shaped?

Use a short FAQ only when it reveals a real ambiguity. Do not turn this into a
marketing document.

If the future experience cannot be explained without implementation details, or
does not clearly improve the framed situation, return to the decision/frame rather
than polishing the promise.

## Draft

For pursue or an experiment worth committing to, save
.itp/work/<slug>/promise-draft.md with title, Promise revision, Status: DRAFT,
Intended outcome, Promise, Boundaries, Binding constraints, Out of scope,
Assumptions and open questions, and Advisory rationale.

Carry forward the human appetite only when it is itself a binding constraint on
the promise; otherwise keep it advisory.

For an experiment promise, binding content also names bounded exposure,
observation, stop condition, and decision rule. Promise the learning activity,
not a favorable result.

Do not add acceptance matrices, seams, proof oracles, implementation tasks,
candidate identities, or proof verdicts.

## Revision rules and exact approval

Use human-readable revisions v1, v2, ... . Material changes to promised behavior,
boundaries, binding constraints, or experiment decision rules require a new
revision and renewed approval.

Present the exact durable source text for human approval. After explicit approval:
1. save it to a project-owned durable path such as specs/<slug>.md;
2. compute SHA-256 over exact file bytes with no normalization;
3. save .itp/work/<slug>/approval.md naming source path, revision,
   promise:sha256:<hash>, approver/approval source, and context;
4. recompute the hash and require it still matches;
5. save .itp/work/<slug>/handoff.md with the same identity and approval reference.

If any promise byte changes, the old approval does not cover it.

## Handoff

Only after exact approval and a matching hash report AGREED and give:
/plan-acceptance <durable-source-path>

Do not invoke P2P automatically. Source approval does not approve its later
acceptance contract or authorize implementation, commit, push, publication, or
merge.
