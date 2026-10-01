# Promise to Proof handoff

Idea to Promise and Promise to Proof are sibling workflows with a narrow,
identity-preserving interface.

## Idea to Promise owns

- problem framing,
- alternatives,
- decision-directed research,
- bounded experiments used for learning,
- human decision support,
- the final bounded source promise,
- identity and approval of that exact source.

## Promise to Proof owns

- acceptance requirements,
- seams and oracles,
- planned evidence,
- implementation,
- candidate identity,
- implementation review,
- proof and repair,
- publication and merge-readiness rules.

## Handoff artifact

The primary handoff is a normal project-authored source document, commonly under
`specs/`. It must be understandable without access to ignored ITP scratch state.

The ITP handoff record names:

```text
Source: specs/<slug>.md
Promise revision: vN
Promise identity: promise:sha256:<hash>
Approval: <approval record or attributable source>
Next: /plan-acceptance specs/<slug>.md
```

Before handoff, recompute the source SHA-256 and require it to equal the approved
identity. Drift means the approval does not cover the current source.

The source promise should state observable outcome, promised behavior,
boundaries/non-goals, binding constraints, and visible assumptions. It may include
advisory rationale and research references.

It must not contain a P2P acceptance matrix, proof verdict, implementation
candidate identity, or a claim that implementation has already been accepted.

## Transfer

Invoke P2P separately:

```text
/plan-acceptance <source-path>
```

P2P still applies its own contract planning, evidence, and approval rules. ITP
source approval does not authorize implementation or publication.

If the source promise changes, return to the source decision, increment the
promise revision, and obtain approval of the new exact bytes before reconciling
downstream work.
