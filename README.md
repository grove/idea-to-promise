# Idea to Promise

Turn a rough idea into a decision you understand and a promise worth making.

Start with an idea, not a form:

```text
/discover quick We keep losing report filters when exporting. Is a small fix worthwhile?
```

ITP helps clarify the need, explore real alternatives, investigate important
uncertainty and record **your** choice. The result can be a promise, a bounded
experiment, a deferral, or a deliberate decision not to build.

**Idea to Promise decides what is worth promising. [Promise to Proof](https://github.com/grove/promise-to-proof)
plans acceptance, implements, reviews and proves the agreed behavior.**

## Get started

Install through the skills installer:

```bash
npx skills@latest add grove/idea-to-promise
```

Then, in your agent's skill interface:

```text
/setup-idea-to-promise
/discover <your idea>
```

Setup is optional. It previews creation of ignored `.itp/work/` storage and
preserves existing source/spec conventions. Skills are agent instructions, not
shell commands; invocation syntax depends on the host. Manual installation means
copying an entire skill folder, including its references, templates and scripts.
Each skill is packaged independently; a sibling checkout is not required.

## One umbrella, useful stages

| Skill | Use it to |
|---|---|
| [discover](skills/productivity/discover/SKILL.md) | Guide the conversation end to end, or resume/revisit it |
| [frame](skills/productivity/frame/SKILL.md) | Understand the real need and today's workaround |
| [brainstorm](skills/productivity/brainstorm/SKILL.md) | Explore opportunities, then distinct approaches |
| [research](skills/productivity/research/SKILL.md) | Investigate the weakest important assumptions |
| [decide](skills/productivity/decide/SKILL.md) | Explain tradeoffs and record the human choice |
| [challenge-decision](skills/productivity/challenge-decision/SKILL.md) | Optionally check material risks and hidden complexity |
| [shape-promise](skills/productivity/shape-promise/SKILL.md) | Write and verify the exact source handoff |
| [setup-idea-to-promise](skills/productivity/setup-idea-to-promise/SKILL.md) | Prepare local storage without changing product files |

These are not eight mandatory steps. Start where the uncertainty is.

## Enough rigor, not more paperwork

**Quick:** a small reversible question, often one `discovery.md` notebook.
**Normal:** separate records only where useful.
**Deep:** more investigation for consequential uncertainty.

Modes never waive honest evidence, human choice, or exact source approval. They
are not fixed durations or spending guarantees. Supplied decisions and appetite
are reused rather than asked for again. An existing solution is a valid finish.

```text
/discover normal <idea>
/discover deep <idea>; research budget: <your limit>
/discover resume .itp/work/<slug>
/discover revisit specs/<slug>.md
```

A revisit preserves the old approved promise while any replacement is pending.
Past P2P delivery experience can inform research, but never automatically becomes
new scope. No background work or autonomous controller is implied.

## See the whole conversation

[Six worked examples](examples/README.md) show a quick improvement, a bad feature
idea, an experiment-first technical choice, an existing-solution/no-build outcome,
a choice changed after challenge, and a revisit with a P2P handoff. They are
explicitly fictional teaching examples, **not live evaluations or customer evidence**.

For the practical workflow see [the how-to](docs/how-to.md). For persistence,
approval and amendments see [the protocol](docs/discovery-protocol.md) and
[artifact format](docs/artifact-format.md).

## Trust the handoff, not a green checkbox

The final source is a normal project-owned file such as `specs/<slug>.md`.
A human approves its exact saved bytes; approval lives in a separate receipt.
Any byte change needs renewed approval. P2P still has its own contract approval.

```bash
python3 scripts/promise_identity.py specs/<slug>.md
python3 scripts/check_work_item.py .itp/work/<slug> \
  --promise specs/<slug>.md --handoff
```

The checker requires matching source paths, revisions, identities and a retrievable
approval receipt in handoff mode. **It checks consistency, not whether the evidence
is good, the approver is authentic, or the work is ready to implement.** See
[portable handoffs](docs/p2p-handoff.md); ignored files do not travel through Git.

## Evaluate behavior, honestly

The [evaluation kit](evaluations/README.md) includes multi-turn cases, a host-neutral
adapter interface, exact instruction snapshots, virtual file captures, mechanical
checks and an evidence-linked human review form. The umbrella skill is tested
separately from individual stages.

```bash
python3 scripts/evaluate.py prepare --out .itp/evals/first
```

Preparing cases does not run a model. Live capture requires a configured trusted
host adapter. Fixture execution, live-labelled captures and human judgments remain
separate; unassessed criteria never turn into passes. See [current evidence and
limits](docs/validation.md).

## Contributor checks

Python 3.11+ and Git; no third-party Python packages or model credentials:

```bash
python3 scripts/sync_skill_resources.py --check
python3 -m unittest discover -s checks -p 'test_*.py' -v
```

Edit canonical resources, regenerate packaged copies, and test before publishing.
Read [AGENTS.md](AGENTS.md), [CONTRIBUTING.md](CONTRIBUTING.md),
[SECURITY.md](SECURITY.md), and [CHANGELOG.md](CHANGELOG.md).
Apache-2.0; see [LICENSE](LICENSE).
