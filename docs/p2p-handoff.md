# Promise to Proof handoff

Idea to Promise and Promise to Proof are sibling workflows with a narrow interface.

## Idea to Promise owns

- problem framing,
- alternatives,
- decision-directed research,
- claim/evidence synthesis,
- human decision support,
- the final bounded source promise.

## Promise to Proof owns

- acceptance requirements,
- seams and oracles,
- planned evidence,
- implementation,
- candidate identity,
- implementation review,
- proof and repair,
- publication/merge-readiness rules.

## Handoff artifact

The handoff is a normal project-authored source document, commonly under `specs/`.

It should state:
- intended observable outcome,
- promised behavior,
- boundaries and non-goals,
- binding constraints,
- important assumptions/open questions,
- advisory research/rationale where useful,
- revision identity,
- actual approval reference when available.

It should **not** contain a P2P acceptance matrix or claim that implementation has been proved.

## Transfer

Once the exact source text is agreed:

```text
/plan-acceptance <source-path>
```

P2P must still apply its own contract planning and approval rules. If the source promise changes, return to the source decision and obtain renewed agreement before reconciling downstream work.
