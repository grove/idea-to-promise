# Recipe: make a technical decision

## Situation

You need to choose between technical approaches—perhaps a queue, database, architecture, dependency, migration strategy, or reliability mechanism.

Technical decisions are valid ITP work. You do not have to translate every technical requirement into marketing-style user benefits.

## Start with

```text
/discover deep We need to decide whether report generation should stay synchronous or move to a queue.
```

Use `deep` when the decision is consequential, expensive, or hard to reverse. If it is a small local choice, plain `/discover` may be enough.

## What to expect

ITP should clarify the actual technical outcome and constraints, identify materially different approaches, and make important assumptions visible. It should distinguish evidence about the actual system/version from generic best practices.

If a critical performance or feasibility assumption can be tested cheaply, ITP may suggest a bounded experiment instead of pretending the architecture can already be chosen confidently.

The decision should also make appetite and reversibility explicit. A theoretically powerful architecture may still be the wrong choice if the problem is only worth a small intervention.

## Healthy result

The human chooses a direction with a clear decision basis, important unknowns remain visible, and the resulting promise states the technical behavior or boundary precisely enough for P2P to plan acceptance later.
