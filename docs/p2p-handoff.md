# A narrow, portable handoff to Promise to Proof

ITP owns discovery and the human's source promise. P2P owns acceptance contracts,
evidence planning, implementation, candidate identity, review and proof.

## Before handoff

Save exact proposed source bytes, calculate identity, and obtain attributable human
approval of that exact wording. Keep the receipt separate.

```bash
python3 scripts/check_work_item.py .itp/work/<slug> \
  --promise specs/<slug>.md --handoff
```

Only then propose `/plan-acceptance specs/<slug>.md`. ITP approval does not
approve P2P's contract or authorize implementation/publication.

## Another checkout

The receiving context needs exact source bytes plus retrievable approval evidence.
Ignored `.itp/` records do not travel through Git automatically. Recompute source
identity after transfer. A digest alone cannot reconstruct the approved document.

## Classify P2P feedback before crossing the boundary back

Stay in P2P when the approved promise is still right and the problem is
implementation, candidate identity, tests/evidence, CI, publication or another
delivery concern.

Return to ITP when evidence indicates the promise/decision itself must change:

```text
/discover amend specs/<slug>.md; trigger <P2P evidence>
```

The current approved promise remains active while an amendment is proposed.
A material replacement requires a new promise revision, human decision where
needed, exact approval and a fresh `/plan-acceptance` handoff. Delivery difficulty
is not permission to weaken scope.

## Outcome is a separate question

After delivery, P2P proof can establish delivered behavior. To assess whether the
intended beneficiary/operator outcome improved, use real-world observations:

```text
/discover outcome specs/<slug>.md; evidence <P2P + outcome observations>
```

No outcome observations means `not-assessed`, not success. Outcome learning is
advisory; it can trigger revisit/amend/new opportunity but never silently becomes
a requirement.

See [the feedback loop](feedback-loop.md).
