# Idea to Promise

Turn a rough idea into a decision you understand and a promise worth making.

```text
/discover quick We keep losing report filters when exporting. Is a small fix worthwhile?
```

ITP helps clarify the need, explore alternatives, investigate important uncertainty
and record **your** choice. It can finish with a promise, bounded experiment,
deferral, existing solution, or deliberate no-build decision.

**Idea to Promise decides what is worth promising. [Promise to Proof](https://github.com/grove/promise-to-proof)
plans acceptance, implements, reviews and proves the agreed behavior.**

## Get started

```bash
npx skills@latest add grove/idea-to-promise
```

Then use:

```text
/setup-idea-to-promise
/discover <your idea>
```

Setup is optional. Skills are agent instructions, not shell commands.

## One umbrella, useful stages

| Skill | Use it to |
|---|---|
| [discover](skills/productivity/discover/SKILL.md) | Guide the conversation, resume/revisit, classify amendments, or review outcomes |
| [frame](skills/productivity/frame/SKILL.md) | Understand the real need and current workaround |
| [brainstorm](skills/productivity/brainstorm/SKILL.md) | Explore opportunities, then distinct approaches |
| [research](skills/productivity/research/SKILL.md) | Investigate weak load-bearing assumptions safely |
| [decide](skills/productivity/decide/SKILL.md) | Explain tradeoffs and record the attributable human choice |
| [challenge-decision](skills/productivity/challenge-decision/SKILL.md) | Optionally check material risks and hidden complexity |
| [shape-promise](skills/productivity/shape-promise/SKILL.md) | Write and verify exact source approval/handoff |
| [setup-idea-to-promise](skills/productivity/setup-idea-to-promise/SKILL.md) | Prepare ignored local storage |

These are not eight mandatory steps.

## Adaptive discovery

**Quick:** small and reversible, often one `discovery.md`.  
**Normal:** separate records only where useful.  
**Deep:** more investigation for consequential uncertainty.

```text
/discover normal <idea>
/discover deep <idea>; research budget: <your limit>
/discover resume .itp/work/<slug>
/discover revisit specs/<slug>.md
/discover amend specs/<slug>.md; trigger <P2P or other evidence>
/discover outcome specs/<slug>.md; evidence <delivery + observations>
/discover status .itp/work/<slug>
```

A proposed amendment never overwrites the active approved promise. P2P delivery
evidence can trigger discovery, but implementation difficulty alone is not
permission to weaken a promise.

## Human decisions, including teams

ITP keeps recommendation, human choice and exact promise approval separate. For a
team decision it can record a decision owner, people consulted/affected and the
expected promise approver—but it avoids forcing organizational paperwork when one
person is simply deciding for themselves.

A decision may also carry a compact **posture**:

```text
Evidence: moderate
Important unknowns: bounded
Reversibility: high
Downside if wrong: low
Appetite fit: good
```

This is descriptive context, not a fake confidence score.

## From proof back to learning

P2P can prove delivered behavior. That does **not** automatically prove adoption,
customer value or the intended real-world outcome.

After delivery, ITP can record an `outcome-review.md` that binds the original
promise identity to delivery evidence and real-world observations. With no outcome
observations, the result stays `not-assessed`.

See [the feedback loop](docs/feedback-loop.md) and
[portable P2P handoff](docs/p2p-handoff.md).

## Treat research sources as data, not bosses

Webpages, issues, documents, repository text, attachments and tool output may
contain instructions. ITP treats them as evidence only. Retrieved text cannot
change the user's goal, grant permissions, reveal secrets, increase budgets, or
authorize external actions.

See [security and privacy boundaries](SECURITY.md).

## Work records and status

Local discovery normally lives under `.itp/work/<slug>/`; the exact approved
promise remains a normal project-owned source such as `specs/<slug>.md`.

```bash
python3 scripts/inspect_work_item.py .itp/work/<slug> --promise specs/<slug>.md
python3 scripts/check_work_item.py .itp/work/<slug> \
  --promise specs/<slug>.md --handoff
```

These tools do not judge product value, evidence quality, organizational authority
or human authenticity.

## Evaluation: quality and friction are separate

The [evaluation kit](evaluations/README.md) captures exact instructions, actual
host replies, virtual files, mechanical checks and attributed human judgments.
It also records descriptive friction observables: turns, question marks, files
created/changed, response size and elapsed time.

Those metrics help detect ceremony. They are **not** automatic quality scores.

```bash
python3 scripts/evaluate.py prepare --out .itp/evals/first
```

No independent live-agent behavioral pass is claimed without an actual configured
host adapter and retained review. See [validation status](docs/validation.md).

A real maintainer-authored self-use trace for this release is in
[case-studies/v0.6-self-use.md](case-studies/v0.6-self-use.md); it is not an
independent evaluation.

## Contributor/release checks

```bash
python3 scripts/sync_skill_resources.py --check
python3 scripts/release_check.py
python3 -m unittest discover -s checks -p 'test_*.py' -v
```

Read [the practical how-to](docs/how-to.md), [protocol](docs/discovery-protocol.md),
[artifact format](docs/artifact-format.md), [AGENTS.md](AGENTS.md),
[CONTRIBUTING.md](CONTRIBUTING.md), and [CHANGELOG.md](CHANGELOG.md).

Apache-2.0; see [LICENSE](LICENSE).
