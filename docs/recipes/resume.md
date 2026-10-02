# Recipe: resume discovery

## Situation

You worked on an idea earlier and want to continue without repeating the interview or reconstructing every decision from memory.

## Start with

```text
/discover resume .itp/work/<slug>
```

## What to expect

ITP should read the existing notebook, decision records, evidence, and optional session note. It should summarize what is already settled, identify the current blocker or missing choice, and continue from there.

It should not ask you again for information that is already clearly recorded unless new evidence makes the old answer materially questionable.

## Healthy result

The conversation resumes at the next useful decision-changing question.

If you only want a structural snapshot of the work item, you can also use:

```text
/discover status .itp/work/<slug>
```

The status view is structural guidance, not a product decision.
