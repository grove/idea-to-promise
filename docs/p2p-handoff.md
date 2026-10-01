# A narrow, portable handoff to Promise to Proof

ITP owns discovery and the human's source promise. P2P owns acceptance contracts,
evidence planning, implementation, candidate identity, review and proof. This
release does not change P2P or implement a controller between the repositories.

## Before handoff

Save exact proposed source bytes; calculate their identity. Obtain attributable
human approval of that saved wording, not just the direction. Keep the receipt
separate. Reread source, receipt and handoff, and compare paths, revision and hash:

```bash
python3 scripts/check_work_item.py .itp/work/<slug> \
  --promise specs/<slug>.md --handoff
```

Only then propose `/plan-acceptance specs/<slug>.md` separately. The ITP approval
does not approve P2P's later contract or authorize its implementation/publication.

## Another checkout

The receiving context needs the exact source bytes, a retained approval receipt,
and the actual referenced approval text or retrievable provenance. A digest alone
cannot reconstruct the document. `.itp/` is ignored, so a Git clone does not carry
these records by default. Transfer them explicitly or retain authorized copies in
project-owned paths. Recompute identity after transfer; do not change approved
source text merely to fix links. Check privacy before publishing research/receipts.

The source must contain the full binding outcome, scope and constraints without
requiring the notebook. Optional research rationale is not additional scope.

## Delivery feedback

A P2P proof, review or retrospective may supply an observation for later research.
Retain the relevant candidate/contract/source context and limits. Do not infer
customer value from technical proof, or convert historical advice into a binding
requirement. Revisit the decision and get new human agreement where scope changes.
