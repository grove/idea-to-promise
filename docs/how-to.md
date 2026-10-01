# Workflow guide

## End-to-end

```text
/discover We need to make retries safe for uploads over unreliable networks.
```

For a named work item, discovery records normally live under
`.itp/work/<slug>/`. The durable agreed source promise normally lives under
`specs/<slug>.md`.

## Stage by stage

```text
/frame <idea or notes>
/brainstorm <framing>
/research <questions or alternatives>
/challenge-decision <decision record>
/shape-promise <selected direction and evidence>
```

Start at any stage when earlier work already exists. New evidence may return the
work to alternatives or research. There is no requirement that every idea become
a build.

## Research and experiments

Order research questions by decision impact. Keep stable claim IDs and record
counterevidence. When observation is cheaper than more argument, create a bounded
experiment under `.itp/work/<slug>/experiments/`.

Stop when another reasonable check is unlikely to change the decision or when an
agreed research bound is reached.

## Challenge the decision

For consequential work, run `/challenge-decision` before shaping the promise.
The challenge is independent and advisory: it checks evidence-to-decision
traceability, ignored counterevidence, prematurely dismissed alternatives, and
load-bearing unknowns. It does not rewrite the decision.

## Shape and approve the promise

Use `/shape-promise` to create `.itp/work/<slug>/promise-draft.md`. After the
human selects the exact wording, save the durable source, for example
`specs/<slug>.md`.

Compute its identity:

```bash
python3 scripts/promise_identity.py specs/<slug>.md
```

Record that exact identity and attributable approval in
`.itp/work/<slug>/approval.md`. Any byte change invalidates that approval.

Validate a work item:

```bash
python3 scripts/check_work_item.py .itp/work/<slug> --promise specs/<slug>.md
```

## Hand off to Promise to Proof

After the approval hash matches the current source:

```text
/plan-acceptance specs/<slug>.md
```

Promise to Proof owns acceptance planning, implementation, review, and proof.
