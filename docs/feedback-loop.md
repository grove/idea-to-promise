# From proof back to better discovery

Idea to Promise and Promise to Proof form a loop, not a one-way pipeline.

```text
idea -> decision -> approved promise -> P2P delivery/proof
  ^                                      |
  |                                      v
  +---- revisit/amend <- observations <- outcome review
```

## When P2P feedback stays in P2P

A delivery problem remains a P2P concern when the approved promise is still right
and the issue is implementation, test/evidence quality, candidate drift, CI,
publication, or another delivery-specific problem.

Do not reopen discovery merely because implementation is difficult.

## When feedback returns to ITP

Return to ITP when evidence suggests one of these is true:

- the promised behavior or boundary itself is wrong or ambiguous;
- a binding constraint must change;
- a newly discovered need is materially different from the approved promise;
- the decision basis changed enough that the human should choose again.

Use:

```text
/discover amend specs/<slug>.md; trigger <P2P or other evidence>
```

The current approved source and receipt stay active while the amendment is only
proposed. Record `amendment-proposed.md`. Classify the trigger before changing
scope. A material change gets a new promise revision, a new attributable human
decision where needed, exact-byte approval, and a fresh P2P planning handoff.

## Review the outcome after delivery

P2P can prove that delivered behavior satisfies an acceptance contract. It cannot
by itself prove that the original beneficiary outcome improved.

When real-world observations exist, use:

```text
/discover outcome specs/<slug>.md; evidence <delivery + observations>
```

Record `outcome-review.md` with the exact source identity, delivery evidence,
observation context, counterevidence, assumption updates and decision impact.

If there are no real-world observations, say `not-assessed`; do not turn green
delivery evidence into a claim of user value.

Outcome learning is advisory. It may trigger a revisit, amendment, or a new
opportunity, but it never silently adds scope to an existing promise.

## Preserve identity and provenance

Keep exact source/contract/candidate identities when available. Attribute reports
as reports. Record populations, periods and environments rather than generalizing
from a different context. Preserve source restrictions and never publish private
evidence merely to make the loop convenient.
