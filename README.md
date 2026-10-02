# Idea to Promise

**Turn a rough idea into a decision you understand and a promise worth making.**

You normally only need one command:

```text
/discover <your idea>
```

For example:

```text
/discover We should add offline mode to our mobile app.
```

Then talk naturally. Idea to Promise (ITP) helps you understand the real need, explore sensible alternatives, investigate the uncertainty that actually matters, and make an explicit human decision. If the decision is to move forward, it helps shape the exact outcome you are willing to promise.

ITP does **not** implement the idea, make the decision for you, or silently approve a promise. Once the promise is approved, [Promise to Proof](https://github.com/grove/promise-to-proof) takes over to plan acceptance, implement, review, and prove the agreed behavior.

## Start in two minutes

Install the skills:

```bash
npx skills@latest add grove/idea-to-promise
```

Then start with your actual idea:

```text
/discover <your idea>
```

Optional project setup is available with `/setup-idea-to-promise`, but you do not need setup just to have a useful discovery conversation.

**You do not fill out ITP forms.** The records, evidence IDs, decision history, and approval identity exist so the conversation can be trustworthy and resumable. You normally interact with the conversation, not the machinery underneath it.

A good ITP reply should also make the next step obvious. It should say where things stand in plain language, recommend a sensible direction when useful, and ask for one clear decision or approval when that is what is needed. Internal IDs, hashes, checker output, and protocol terminology stay in the background unless they help you.

## What will happen?

Suppose you start with:

```text
/discover We should add AI summaries to support tickets.
```

ITP might help uncover that the real problem is not “we lack summaries,” but that support agents struggle to find the customer’s current unresolved question in long threads. It then explains the sensible alternatives in plain language, shows the main upside and downside of each, and gives you a clear recommendation with the reason behind it. **You** still choose.

A successful discovery may end with a promise such as:

> Support agents can identify the customer’s current unresolved question without reading the entire ticket history.

Or it may end with an experiment, a deferral, an existing feature you should use instead, or a deliberate decision not to build anything.

## The whole idea in one picture

```text
rough idea
   ↓
understand the real need
   ↓
explore opportunities and alternatives
   ↓
research what could change the decision
   ↓
human chooses
   ↓
exact approved promise
   ↓
Promise to Proof
   ↓
implementation + review + proof
```

ITP can also revisit an old promise, classify feedback coming back from P2P, and review whether delivered behavior actually improved the original real-world outcome.

## What should I read next?

If this is your first time here, start with the **[5-minute Getting Started guide](docs/getting-started.md)**. It walks through one idea from “maybe we should build this” to a clear promise, without requiring you to understand the internal artifact format.

If you want the big picture, read **[The mental model](docs/mental-model.md)**. If you already know what you want to do and just need the command, use the **[cheat sheet](docs/cheatsheet.md)**. For common situations such as a new feature, technical decision, experiment, no-build outcome, revisit, or P2P amendment, browse the **[recipe book](docs/recipes/README.md)**.

For maintainers and advanced users, the deeper protocol, artifact, security, evaluation, and P2P handoff documentation remains available through the **[reference index](docs/reference/README.md)**.

## Quick examples

| I want to… | Start with |
|---|---|
| Explore a new idea | `/discover <idea>` |
| Think about a small reversible change | `/discover quick <idea>` |
| Work through an expensive or hard-to-reverse choice | `/discover deep <idea>` |
| Continue previous discovery | `/discover resume .itp/work/<slug>` |
| Reconsider an approved promise | `/discover revisit specs/<slug>.md` |
| Handle a P2P finding that may change the promise | `/discover amend specs/<slug>.md; trigger <evidence>` |
| Check whether delivered work actually helped | `/discover outcome specs/<slug>.md; evidence <observations>` |
| Hand an approved promise to delivery | `/plan-acceptance specs/<slug>.md` |

If you are unsure which one to use, use plain `/discover <idea>`. The umbrella skill is designed to guide the rest.

## Project status

ITP v0.6 has automated structural and packaging checks, worked examples, and an evaluation harness. Independent live-agent behavioral quality is still explicitly **unassessed** until real host runs are captured and reviewed. See [validation status](docs/validation.md) for the exact evidence and limits.

For contributing, see [CONTRIBUTING.md](CONTRIBUTING.md), [AGENTS.md](AGENTS.md), [SECURITY.md](SECURITY.md), and [CHANGELOG.md](CHANGELOG.md).

Apache-2.0; see [LICENSE](LICENSE).
