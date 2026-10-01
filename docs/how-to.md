# Use ITP in a real project

## Start naturally

Install the skills, open your project with a compatible agent, and say
`/discover <idea>`. The agent should answer the current question, reuse context
and ask only questions that could change the choice. You do not need to know the
record format. Use individual stages when only one part needs attention.

For a small reversible change try `/discover quick <idea>`. For a consequential
choice use `deep`, optionally adding an explicit research/tool/time budget.
A budget being exhausted means pause and explain uncertainty, not pretend certainty.

## Optional setup

In a Git project `/setup-idea-to-promise` previews local storage setup. From a
checkout you can inspect the same plan directly:

```bash
python3 scripts/setup_project.py --root /path/to/project
python3 scripts/setup_project.py --root /path/to/project --apply
```

Run from the actual repository root with no concurrent filesystem edits. Setup
preserves existing ignore-file bytes, appends the local storage exclusion when
needed and creates `.itp/work/`. It refuses tracked discovery files, symlinks and
path conflicts. It creates no specs, branches, commits or tracker configuration.

## Choose, then separately approve

Research might recommend A2. You may still choose A1 because reversibility matters
more. `/decide` records your actual statement, appetite, tradeoffs and revisit
trigger. It must not substitute its recommendation for your choice.

A choice to experiment commits to learning, not a favorable outcome. Defer or
reject ends discovery without a promise. Optional challenge examines material
risks. A same-context challenge is a self-check, not independent review.

`/shape-promise` saves a proposed source file and computes its identity before
asking you to approve exact wording. Approving an option earlier did not approve
this text. Approval goes into a separate receipt; never edit the source just to
change a status heading after approval.

## Resume without starting over

`/discover resume .itp/work/<slug>` reads the notebook or records and optional
session note. It reports the settled decisions, important unknown and next action.
It should not repeat your earlier interview or silently redo research.

`/discover revisit specs/<slug>.md` starts with what changed. A new dependency,
changed user behavior, or P2P observation may warrant a different choice. Keep
proposals separate from active records. A changed choice gets a new D-ID and
retained history; a material promise amendment gets a new revision and approval.

## Handoff

Use the checker with `--handoff` and then propose `/plan-acceptance <source>`.
For a different checkout transfer the source AND retained approval evidence;
a path into ignored `.itp/` storage is not a portable artifact. P2P independently
applies its acceptance-contract and authorization rules.

## Worked examples and evaluation

Read [the examples](../examples/README.md) for complete fictional conversations.
Use [the evaluation kit](../evaluations/README.md) to capture actual host output
and review process quality. Teaching examples and unit tests are not live trials.
