# Workflow guide

## End-to-end

```text
/discover We need to make retries safe for uploads over unreliable networks.
```

## Stage by stage

```text
/frame <idea or notes>
/brainstorm <framing>
/research <questions or alternatives>
/decide <research>
/challenge-decision <decision record>
/shape-promise <decision record>
```

## Frame the real need

Use `/frame` to identify the actors, progress sought, current workaround,
intended outcome, behavior/change needed, decision criteria, and important
unknowns. Avoid turning the proposed feature into the problem statement.

## Explore opportunities before solutions

`/brainstorm` first creates O-IDs for distinct needs/obstacles. Only then does it
create A-IDs for solution mechanisms. This reduces premature feature fixation.

## Research the riskiest assumptions

`/research` asks what must be true for the viable alternatives to work. It
prioritizes claims that are both important and weakly evidenced. For each claim it
records criticality, evidence strength, and a risk lens.

When a bounded experiment is better than more discussion, precommit to the
observation, decision rule, and stop condition before running it.

## Decide with an appetite

`/decide` presents the viable choices, separates evidence from preference, and
asks how much the outcome is worth in effort, complexity, operational burden, or
experiment exposure.

Appetite is not an estimate. It helps reject or shrink solutions that are too
expensive for the value of the outcome.

## Challenge consequential choices

`/challenge-decision` looks for evidence gaps and then asks two extra questions:

1. Where could hidden complexity or dependencies blow the appetite?
2. Assume this failed six months from now. What are the few most plausible reasons?

Only material, context-grounded concerns should become findings.

## Shape from the future experience

`/shape-promise` asks what the beneficiary will actually be able to do,
understand, avoid, or accomplish if the promise is true, and why that is better
than the current workaround.

If the answer only makes sense in terms of implementation details, go back rather
than polishing the promise.

## Approve and hand off

Save the final source such as `specs/<slug>.md`, compute its exact identity,
record approval, and verify the handoff:

```bash
python3 scripts/promise_identity.py specs/<slug>.md
python3 scripts/check_work_item.py .itp/work/<slug> --promise specs/<slug>.md
```

Then invoke P2P separately:

```text
/plan-acceptance specs/<slug>.md
```
