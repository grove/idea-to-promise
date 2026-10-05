---
name: compound-learning
description: Capture durable, non-obvious, reusable learning from ITP work without turning evidence into decisions, changing approved promises, or silently rewriting shared behavior.
license: Apache-2.0
metadata:
  version: "0.6.0"
---

Read [the discovery protocol](references/discovery-protocol.md) before acting.

# Compound reusable learning

Use this skill when ITP work reveals a lesson likely to matter again. It may be
invoked directly or by another ITP skill. Do not create a diary of every session;
preserve knowledge whose loss would plausibly cause future mistakes, risk, or
substantial rediscovery.

## Apply a high bar

Capture a learning only when all three are true:

- **Non-obvious:** the useful reasoning is not already clear from current records,
  source material, the final promise, or existing documentation.
- **Reusable:** it is likely to help another discovery, revisit, outcome review, or
  maintainer improvement beyond the exact current turn.
- **Material:** forgetting it would plausibly cause repeated investigation, a bad
  recommendation, an avoidable mistake, or meaningful risk.

Use this counterfactual: if the learning disappeared, would a future ITP run be
meaningfully worse or repeat work? If not, do not compound it. Do not capture
routine facts, ephemeral details, unverified guesses, duplicated evidence, or
lessons whose only basis is that the task was difficult.

## Put the learning in the right place

Choose the narrowest useful destination:

- **Project/domain learning:** reusable evidence, context, constraints, or patterns
  for this project. When writable ignored ITP storage is available, save a concise
  record under `.itp/learnings/<slug>.md`.
- **ITP behavior improvement:** a repeated weakness or better method in ITP itself.
  Record a candidate improvement and identify the smallest skill, protocol,
  checker, or evaluation target. Do not silently edit shared ITP behavior.
- **Regression/evaluation:** when an observed failure should never recur, propose an
  evaluation case first; use a deterministic checker/test when the invariant can be
  enforced mechanically.
- **Current decision or promise change:** this is not compounding. Return to the
  appropriate decide/revisit/amend flow and preserve human authority and exact
  approval.

Prefer strengthening an existing canonical record over creating a duplicate. Search
available local learnings and relevant current records before writing a new one.

## Capture enough provenance to stay honest

A project learning should state, compactly:

- the reusable lesson;
- where it applies and where it may not;
- the evidence or observed experience that supports it;
- important uncertainty or counterevidence;
- why it is worth reusing; and
- the suggested destination if it should later become a skill, eval, or checker.

Treat the record as advisory evidence, not a requirement or decision. Do not copy
private or restricted source material merely to make the learning convenient.
Preserve human edits and update an overlapping learning instead of forking it.

If writable local storage is unavailable, return the learning inline and say that
it was not persisted. Never claim another skill, eval, or checker changed unless it
actually did.

## Promote shared behavior carefully

For a proposed ITP behavior change, prefer this sequence:

1. describe the repeated observed failure or opportunity;
2. propose the smallest behavior change;
3. add or identify a regression/evaluation case;
4. compare old and new behavior with the same host/model/context when practical;
5. have the shared change reviewed through the repository's normal workflow.

Automatic detection and local capture are allowed. Promotion into shared ITP
behavior remains reviewable. Do not turn one anecdote into a global rule.

## Keep compounding out of the user's way

Do not interrupt a discovery conversation just to announce that a learning may be
captured. When no new human decision or authority is required, capture it and keep
the main conversation focused on the user's goal. Surface the learning when it is
useful, when persistence failed, or when a shared-behavior proposal needs review.

Compounding never creates a human decision, exact promise approval, implementation
authority, publication authority, or P2P handoff.
