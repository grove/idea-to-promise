# Evaluate discovery, not just Markdown

The suite contains fictional, multi-turn inputs for both `/discover` and individual
skills. Teaching examples are not run results. The default CI tests this harness
with a fixture adapter; it never spends model credits or claims live-agent quality.

## 1. Prepare

```bash
python3 scripts/evaluate.py prepare --out .itp/evals/prepared
```

This validates cases and retains exact skill/reference/template snapshots, case
inputs and an unfilled review form. It does NOT invoke a model. Rubrics and future
human turns are kept out of individual model requests during capture.

## 2. Capture a real host

Write/configure an adapter for your supported agent host. It is an ordinary trusted
program accepting one UTF-8 JSON request on stdin and returning ONE JSON object:

```json
{"reply": "The actual agent reply", "files": {"discovery.md": "complete virtual content"}}
```

The request contains schema `itp-eval-v1`, exact instructions, mode, conversation
messages to date, and the virtual workspace. Return the complete workspace
snapshot after this turn. Do not write model files to a real project. A fresh
adapter invocation receives full previous conversation/workspace each turn.
Preserve the actual reply; do not replace it with an expected answer.

```bash
python3 scripts/evaluate.py run \
  --command-json '["/absolute/path/to/your-host-adapter"]' \
  --kind live --host '<actual host/version>' --model '<actual model ID>' \
  --out .itp/evals/live-first --timeout 120
```

`--case <id>` limits a run. `--kind fixture` is the default for testing adapters;
`live` is an OPERATOR DECLARATION, not automatic authentication that an LLM ran.
Record genuine host/model identities; do not relabel fixture results as live.
The adapter must actually call the declared host for a live trial.

Commands run with shell=False in a temporary working directory. This is NOT a
sandbox: a trusted adapter still has the invoking user's filesystem/environment/
network permissions. Use your host's own sandbox/quotas and a disposable account
or workspace as appropriate. The harness has a per-turn timeout and response-size
limit, not a hard monetary/total-resource cap. Do not put secrets in arguments.
Run records may include confidential prompts/output; keep them local and review
before publication. stderr is not retained; adapter failures remain explicit.

## 3. Review behavior separately

Mechanical checks inspect virtual file paths and preservation, not whether the
reasoning is good. An agent saying the right word is not a semantic pass.

Copy review-template.json, fill reviewer, and judge each numbered criterion:
pass/fail/not-assessed. Every pass/fail needs a turn number, an exact excerpt from
the captured reply and a reason connecting it to the criterion. For omission
findings quote the relevant reply and explain the missing behavior. The form binds
the exact run.json hash. Changed runs or fabricated excerpts are rejected.

```bash
python3 scripts/evaluate.py report .itp/evals/live-first/run.json \
  --reviews .itp/evals/live-first/review.json
```

Exit codes for report: 0 all mechanical checks and explicit judgments pass;
1 failure; 2 invalid input; 3 incomplete/unassessed review. A prepared suite cannot
be reported as executed. Capture exit 0 means captured, NOT semantically passed.
Use a separate reviewer for stronger evidence and record actual independence;
self-review remains useful but must be labeled as such.

## Improve from evidence

Run the same cases against pinned old/new instruction snapshots with the same
host/model and inputs. Retain all attempts, errors and declines. Review without
knowing the variant when practical. Look at missed human-choice gates, fabricated
evidence, unnecessary questions, ignored limits, weak alternatives and useless
ceremony; avoid a single arbitrary product-quality score. Add observed failures
as regression cases, including no-build and negative controls.

This release ships the infrastructure and fixture validation. No independent
live-agent behavioral pass is claimed; see [validation status](../docs/validation.md).


## Friction observables

Captured runs also report descriptive interaction cost:

- assistant turns,
- question marks in replies,
- virtual files created,
- virtual files changed,
- total reply characters,
- elapsed adapter time.

These values help identify needless interviewing, document churn, and verbosity.
They are not semantic quality measures and have no automatic pass/fail threshold.
A difficult decision can legitimately need more interaction than a quick case.

Compare friction only alongside the same case inputs, behavioral review, and
host/model context. Do not optimize question counts by skipping load-bearing human
choices or evidence.

## Feedback-loop cases

The suite includes cases for team decision ownership, classifying P2P feedback
before a promise amendment, and refusing to call a delivered behavior a successful
real-world outcome when no outcome observations exist.
