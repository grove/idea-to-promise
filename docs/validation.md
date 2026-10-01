# Evidence and limits for v0.5

There are three distinct evidence levels:

- Automated tests exercise the Python helpers, record consistency, standalone
  resource packaging, evaluation capture/reporting, and failure paths.
- Worked examples and scripted case inputs illustrate behavior. They are fictional,
  authored material, not observations of users or agents.
- Live evaluation requires an actual configured host adapter, retained outputs and
  attributed review. An adapter's kind/host/model labels are declarations, not
  authentication, and missing reviews remain unassessed.

For this release, no independent live-agent evaluation is claimed. This authoring
session had no configured model-execution adapter. The harness is exercised with
explicitly labeled fixture adapters, including failure controls. No model API
secrets, new paid services or production experiments are required by unit tests.

The npm installer needs network access. Offline package closure tests validate
copied individual skill directories, but they are not evidence of an npm install
or a particular host's invocation UX. Python/Git setup tests likewise do not prove
support for every filesystem or concurrent editing pattern.

A structurally matching approval/handoff is not authenticated human approval.
Likewise a green CI run is not proof of good brainstorming, product value,
evidence credibility, or successful live P2P delivery.

The next evidence to gather is a small real-host capture on the checked-in cases,
reviewed with explicit excerpts and all incomplete/error cases retained.

## Local release checks

The local Python/Git suite passed 43 tests, including fixture capture, deliberate
negative controls, source/receipt drift, path conflicts and standalone package
closure. Preparing the 10-case suite succeeded without model execution.
An actual npm installer smoke attempt failed at DNS resolution for
registry.npmjs.org (EAI_AGAIN); no npm-install success is claimed.
