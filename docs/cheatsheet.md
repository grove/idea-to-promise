# ITP cheat sheet

Most of the time, start here:

```text
/discover <your idea>
```

If you remember only that, you can still use ITP successfully.

## Common commands

| Situation | Command |
|---|---|
| New idea | `/discover <idea>` |
| Small, reversible question | `/discover quick <idea>` |
| Important, expensive, or difficult-to-reverse choice | `/discover deep <idea>` |
| Continue previous work | `/discover resume .itp/work/<slug>` |
| Step back and reassess the whole project | `/discover zoom-out` |
| Reconsider an approved promise | `/discover revisit specs/<slug>.md` |
| P2P found something that may require changing the promise | `/discover amend specs/<slug>.md; trigger <evidence>` |
| Review whether delivered work actually improved the outcome | `/discover outcome specs/<slug>.md; evidence <observations>` |
| See structural status | `/discover status .itp/work/<slug>` |
| Hand approved source to delivery | `/plan-acceptance specs/<slug>.md` |

## Individual skills

Use individual skills when you deliberately want to work on only one part of the process.

| Skill | Main question |
|---|---|
| `/frame` | What problem or progress are we actually dealing with? |
| `/brainstorm` | What underlying opportunities and genuinely different approaches exist? |
| `/research` | What important assumption is weakly supported? |
| `/decide` | Given what we know, what does the human choose? |
| `/challenge-decision` | What could make this decision fail or exceed its appetite? |
| `/shape-promise` | What exact outcome are we willing to promise? |

You do **not** need to run them all manually. `/discover` is the umbrella.

## Healthy endings

Discovery does not always end with a build promise. A healthy result can be:

```text
PURSUE       → shape and approve a promise
EXPERIMENT   → commit to a bounded learning activity
DEFER        → stop, record why and what would reopen the decision
REJECT       → deliberately do not build
EXISTING     → use what already solves the need
```

## Three boundaries worth remembering

**Recommendation is not decision.**  
The agent may recommend; the human chooses.

**Decision is not exact approval.**  
Choosing the direction does not approve the final promise wording.

**Delivery proof is not outcome proof.**  
P2P can prove the behavior was delivered. Real-world evidence is still needed to know whether the intended outcome improved.


## When to zoom out

Use `/discover zoom-out` when you have been executing for a while and want to ask a bigger question:

> **Are we still spending our attention on the right things?**

Zoom-out looks across the project's goals, current work, decisions, promises, delivery/outcome evidence, changed constraints, and opportunities that may have been crowded out. It recommends whether to continue, change focus, validate something important, stop/defer work, revisit an existing promise, or start a new discovery.

It does **not** silently change existing decisions or promises.
