# Idea to Promise

Turn an uncertain idea into a researched, explicit promise worth making.

**Idea to Promise → Promise to Proof**

Idea to Promise helps you decide **what to promise, and why**. Its sibling,
[Promise to Proof](https://github.com/grove/promise-to-proof), turns that agreed
outcome into an acceptance contract, implements it, and checks the result.

Discovery can also end in an experiment, a deferred decision, or a deliberate
choice not to build. A polished proposal is not evidence, and research is not
permission to implement.

## Start here

```text
/discover We need to make retries safe for uploads over unreliable networks.
```

The agent frames the problem, explores alternatives, investigates the questions
that could change the decision, and proposes a bounded promise. You choose the
direction and approve the exact promise. No implementation starts automatically.

For deliberate, stage-by-stage work:

```text
/frame <idea, local document, or issue reference>
/brainstorm <framing record>
/research <questions or brainstorm record>
/shape-promise <research and selected direction>
```

These are agent skills, not shell commands. Invoke them through your host's skill
interface; slash-command presentation and tool availability depend on the host.
They also work by explicitly asking an agent to read the relevant `SKILL.md`.

## Five skills, one small workflow

| Skill | Question | Result |
|---|---|---|
| [`frame`](skills/productivity/frame/SKILL.md) | What problem are we actually addressing? | Outcome, audience, constraints, unknowns, and decision criteria |
| [`brainstorm`](skills/productivity/brainstorm/SKILL.md) | What genuinely different paths could work? | Alternatives, including a smaller or existing solution and doing nothing |
| [`research`](skills/productivity/research/SKILL.md) | What would change our decision? | Claim ledger, source records, contradictions, and a stopping decision |
| [`shape-promise`](skills/productivity/shape-promise/SKILL.md) | What are we prepared to promise? | Bounded source promise or an explicit no-build decision |
| [`discover`](skills/productivity/discover/SKILL.md) | How do we move this idea forward? | A human-led discovery episode using the stages above |

The stages are not a mandatory pipeline. Start from existing research, return to
brainstorming after a contradiction, or stop early. `discover` is a conversational
coordinator, not an autonomous controller or a separate-agent execution engine.

## Install

Install from GitHub after the repository is published:

```bash
npx skills@latest add grove/idea-to-promise
```

Install just one skill:

```bash
npx skills@latest add grove/idea-to-promise --skill research
```

From a local checkout, including an unpublished source archive:

```bash
npx skills@latest add . --list
npx skills@latest add . --skill '*'
```

Each skill includes its own protocol and templates. A single-skill installation
needs no sibling checkout. `discover` includes inline stage instructions so it
also works on its own. Alternatively, copy an entire skill directory into your
host's supported skills directory; do not copy only `SKILL.md`.

The skills require an agent that can read instructions and supplied context.
Research uses only tools the host actually provides. Missing browsing, repository,
or experiment capabilities are reported as evidence limits, not invented results.
Python 3.11+ is needed only for the optional checker and contributor checks. The
skills installer requires Node.js/npm; manual installation does not.

See the [Agent Skills specification](https://agentskills.io/specification) and
[skills installer documentation](https://github.com/vercel-labs/skills).

## The handoff to Promise to Proof

A final source document separates binding outcomes, boundaries, and constraints
from advisory research and alternatives. It does **not** define P2P acceptance
matrices, test oracles, proof verdicts, or implementation tasks.

```text
.itp/work/<slug>/          specs/<slug>.md              .p2p/work/<slug>/
local exploration    →    retained source promise  →   P2P delivery records
```

`specs/` is a convention, not a reserved directory. Preserve useful research and
approval records in project-owned paths when authorized. Do not leave a final
promise dependent on inaccessible `.itp/` scratch files or a previous chat.

Once the exact promise is agreed, invoke P2P separately:

```text
/plan-acceptance specs/retry-safe-uploads.md
```

P2P owns its contract and approval rules. An agreed source promise does not
approve a later acceptance contract or authorize delivery. Changes to the promise
require renewed agreement rather than silently changing the delivery scope.

Read [the workflow guide](docs/how-to.md), [the handoff contract](docs/p2p-handoff.md),
and [the discovery protocol](docs/discovery-protocol.md).

## Examples

The [retry-safe uploads walkthrough](examples/retry-safe-uploads/seed.md) uses a
clearly labeled fictional brief, alternatives, a claim ledger, and an example
promise awaiting approval. The [no-build example](examples/no-build/decision.md)
shows that discovering an existing solution can end the work without a promise.
Neither example claims real user research or product validation.

## Checks and current limits

```bash
python3 scripts/sync_skill_resources.py --check
python3 -m unittest discover -s checks -p 'test_*.py' -v
python3 scripts/check_promise.py examples/retry-safe-uploads/promise.md
```

The optional promise checker checks **structure only**, computes the exact file's
SHA-256, and makes no claim about evidence quality, approval, feasibility, or
readiness. It never writes files, browses, or invokes P2P.

This initial version includes five skills, templates, examples, a structural
checker, packaging checks, and a GitHub Actions workflow. Automated tests validate
software and packaging properties. They do not establish the quality of an
agent's brainstorming or judgment. [Behavioral scenarios](checks/scenarios.md)
are provided for human or agent evaluation; they are not live evaluations merely
because the unit tests pass.

There is no web app, model API integration, autonomous controller, issue
publisher, or change to Promise to Proof in this release.

## Contributing and license

Read [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md). Shared resources
are copied into skill packages by a checked-in script; edit their canonical
sources and regenerate, rather than editing the copies.

Apache-2.0. See [LICENSE](LICENSE).
