# Evidence and limits for v0.6

There are several distinct evidence levels; do not collapse them.

- Automated tests exercise Python helpers, setup conflicts, approval/handoff
  consistency, standalone skill packaging, status inspection, evaluation
  capture/reporting, friction observables and failure paths.
- Worked examples and scripted evaluation cases are authored fixtures, not
  observations of users or agents.
- The v0.6 self-use case study describes a real maintainer project change, but it
  is self-referential and not an independent evaluation.
- Live evaluation requires an actual configured host adapter, retained outputs
  and attributed review. Adapter host/model/kind labels are declarations, not
  authentication.

## What v0.6 establishes

GitHub Actions passed the release/resource checks and 59 unit tests on Python
3.11, 3.12 and 3.13 for the tested v0.6 branch. The 17-case evaluation suite also
prepared successfully without invoking a model.

The checks cover, among other things:

- exact promise/source/receipt drift and unsafe paths;
- setup conflicts and idempotence;
- independent standalone skill package closure;
- evaluation capture failure controls and excerpt-bound reviews;
- team-ownership/amendment/outcome-review case presence;
- read-only work-item status inspection;
- descriptive friction accounting;
- conversation ergonomics: plain-language resume, obvious next actions, inviting exact approval, and graceful recovery from premature downstream requests.

An initial v0.6 branch run caught an incorrect helper API call in the new work-item
inspector; the implementation was corrected and the complete matrix passed before
promotion. This is evidence that the checks can catch at least this class of
integration error, not evidence that they catch every defect.

## What remains unassessed

No independent live-agent behavioral pass is claimed. This environment still has
no configured model-execution adapter for the harness. Fixture adapters do not
count as live model evidence.

A green CI run does not prove:

- good product judgment or brainstorming;
- evidence/source credibility;
- real organizational decision authority or approver authenticity;
- successful customer outcomes;
- successful P2P delivery;
- that lower friction metrics imply better discovery.

P2P proof can establish delivered behavior for its exact contract/candidate. It
does not by itself establish adoption, customer value or the intended real-world
outcome; v0.6 outcome review keeps that state not-assessed when observations are
missing.

The npm installer requires network access. A successful online installer smoke
test has not been re-established for v0.6; standalone package-closure tests are
not a substitute for that host/network check.

## Next evidence to gather

1. Configure one real supported host adapter and capture the checked-in cases.
2. Review outputs with exact excerpts, retaining errors/declines.
3. Compare semantic findings and friction observables on the same case inputs.
4. Use ITP on several non-self-referential real project decisions.
5. Feed real post-delivery observations through the new outcome-review path.

Until then, v0.6 should be described as a tested protocol/tooling release with
live behavioral quality still unassessed.
