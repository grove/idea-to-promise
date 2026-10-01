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
/decide <research>
/challenge-decision <decision record>
/shape-promise <decision record>
```

Start at any stage when earlier work already exists. New evidence may return the
work to alternatives or research. There is no requirement that every idea become
a build.

## Research and experiments

Order research questions by decision impact. Keep stable claim IDs and record
counterevidence. When observation is cheaper than more argument, create a bounded
experiment under `.itp/work/<slug>/experiments/`.

Stop when another reasonable check is unlikely to change the decision or when an
agreed research bound is reached. Research may recommend a direction, but that is
not yet the human decision.

## Decide

Run:

```text
/decide .itp/work/<slug>/research.md
```

The skill reduces the work to the viable choices and explains the real tradeoffs.
It distinguishes evidence from preferences and uncertainty, then asks the human to
choose.

If an essential unknown still blocks a responsible choice, return to research or
run a bounded experiment. Otherwise the human chooses pursue, experiment, defer,
or reject and `decision.md` records that attributable choice.

## Challenge the decision

For consequential work, run `/challenge-decision` before shaping the promise.
The challenge is independent and advisory: it checks evidence-to-decision
traceability, ignored counterevidence, prematurely dismissed alternatives, and
load-bearing unknowns. It does not rewrite the decision.

Small, reversible decisions may skip this stage.

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
