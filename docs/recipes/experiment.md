# Recipe: choose an experiment first

## Situation

You have a promising direction, but one important unknown prevents a responsible commitment.

For example, you suspect queueing report generation will meaningfully reduce user waiting time, but you have no relevant measurements yet.

## Start with

```text
/discover We think queueing reports could reduce waiting, but we need evidence before committing.
```

## What to expect

ITP should identify the load-bearing unknown and ask whether a bounded observation can answer it more cheaply than further discussion.

A good experiment defines the question, hypothesis, exposure, method, observation, decision rule, and stop condition **before** the result is known. The decision rule matters because it prevents the team from rewriting success after seeing the data.

The experiment itself still needs the appropriate authority to run. A plan is not evidence that the experiment happened.

## Healthy result

The promise is about the learning activity, not about getting a favorable answer.

For example:

> Run the local replay against the representative workload and choose queueing only if the predefined waiting-time threshold is met.

After the experiment, the actual observations can update the decision.
