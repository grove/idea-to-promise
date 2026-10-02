# The mental model

Idea to Promise becomes much easier to understand when you separate five things that teams often blur together: **idea, evidence, decision, promise, and proof**.

You do not need to memorize a methodology. You only need to understand why these five things should not silently become one another.

## Idea

An **idea** is something you might do.

> Add AI summaries.  
> Switch databases.  
> Add offline mode.  
> Introduce a queue.  
> Redesign onboarding.

Ideas are useful starting points, but they often contain an assumed solution before the real need is understood. ITP treats the idea seriously without treating it as an already-approved requirement.

## Evidence

**Evidence** is what helps you understand whether an option is likely to address the need and what remains uncertain.

Evidence can include direct observations, primary documentation, repository facts, experiments, attributed user reports, or relevant delivery history. ITP deliberately distinguishes these from assumptions and preferences.

The important question is not “how much research do we have?” It is:

> **Do we know enough about the important things to make the decision?**

ITP focuses research on the weak assumptions that carry the most weight.

## Decision

A **decision** is what the human chooses.

Research can recommend. An agent can explain tradeoffs. A challenge can expose a problem. None of those automatically becomes the decision.

When ITP presents alternatives, it should make them easy for a human to understand: a short list, plain-language explanations, the strongest reason to choose each option, and the main downside. It should then recommend one option—or a small shortlist when the evidence is genuinely close—and explain why. The recommendation is useful decision support, not a substitute for the human choice.

A decision may be:

- pursue an option,
- run a bounded experiment,
- defer,
- reject,
- or use an existing solution and build nothing.

For shared work, the record can also preserve who owns the choice. For simple individual work, that ceremony is unnecessary.

## Promise

A **promise** is the exact outcome you are willing to commit to.

This is narrower and more deliberate than “we chose option A.” A promise states what should become true, its boundaries, important constraints, and what is deliberately outside scope.

The human separately approves the exact saved wording. That gives ITP a clean boundary:

> We are no longer merely discussing an idea. We are willing to make this specific promise.

## Proof

**Proof** belongs downstream.

Once the promise is approved, Promise to Proof turns it into precise acceptance, implements against that contract, reviews the implementation, and proves whether the promised behavior exists on the exact candidate.

That gives the full lifecycle:

```text
Idea
  ↓
Evidence
  ↓
Decision
  ↓
Promise
  ↓
Proof
```

## Why the separation matters

Without these boundaries, several dangerous shortcuts become easy:

> “Research recommends A, therefore we decided A.”  
> “We chose A, therefore this wording is approved.”  
> “The implementation passes tests, therefore the original user outcome improved.”

ITP is designed to stop those silent jumps.

Technical proof can establish that promised behavior was delivered. It does not automatically prove adoption, usefulness, or customer value. That is why ITP can also perform an outcome review after delivery when real-world observations exist.

## One sentence to remember

**Don’t implement an idea. Understand it until you are willing to make a precise promise; then implement and prove exactly that promise.**
