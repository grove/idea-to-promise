# An architecture choice that needs observation

> Fictional teaching example. The dialogue and source notes are authored fixtures, not live-agent output, customer research, or real approval.

## Seed and frame

**User:** “Deep discovery: move report generation to a queue. We need to know
whether it reduces user waiting, but we cannot touch production yet.”

S1 is a supplied fictional architecture note: local report replay is available;
production latency and queue overhead are not measured. O1 is reduced waiting,
not owning a queue. A1 retains synchronous reports, A2 adds a queue, A3 precomputes
common reports. All three remain hypotheses about the outcome.

## Risk-prioritized research

C1: “A queue reduces experienced waiting” is high criticality with no direct
evidence. C2: “The queue library supports our language” is supported by the
fictional brief, but says nothing about C1. More library comparisons would miss
the important uncertainty.

**Agent:** “An unconditional queue decision is not justified yet. A bounded local
replay could test waiting and overhead without production exposure.”

**User:** “Choose that experiment. One engineering day, local replay only. No
production credentials or infrastructure changes.”

## Decision and challenge

D1 records experiment, not pursue-the-queue. Appetite is one day and exposure is
local only. A same-context self-check highlights that replay traffic may not
represent real usage. That is a limitation to retain, not a reason to demand the
answer before running a properly bounded experiment.

## Experiment promise draft

E1 will compare the existing path and a local queue prototype on the same supplied
replay input. Before running, the human must settle the meaningful waiting-time
threshold. Record the input, method and threshold before observing results.
Stop at the one-day bound or any need for production access. Record actual results,
queue overhead and representativeness limits, including an inconclusive outcome.

The promised activity is to learn and apply the decision rule—not to demonstrate
that queues win. E1 remains PLANNED and its result is unknown in this example.

## Handoff gate

The threshold is still an unresolved part of exact promise wording. The source is
not ready for approval yet. Neither choosing the experiment nor writing its plan
runs it or authorizes production work.
