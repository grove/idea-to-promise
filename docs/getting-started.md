# Getting Started in five minutes

The fastest way to understand Idea to Promise is to use it once.

Imagine you are working on a support product and someone says:

> We should add AI summaries to long support tickets.

That sounds like a solution already. ITP helps you slow down just enough to understand what problem is worth solving, without turning the conversation into a heavyweight workshop.

## What a good ITP conversation should feel like

ITP has quite a lot of rigor underneath, but you should not have to operate that machinery yourself. A good conversation tells you where you are in ordinary language, explains the important choices clearly, recommends a sensible path, and makes the next human action obvious.

For example, after resuming earlier work, a good reply is closer to:

> We’ve already agreed that the first version should stay small. The remaining choice is whether the first artifact should be a simple generated index or a full application. I recommend the generated index because it gives us something useful quickly without committing us to a new runtime. Shall we use that for v1?

It should **not** make you interpret internal IDs, work-item state, hashes, structural-check output, or protocol gates unless those details actually matter to the decision.

The same principle applies to approval. When the promise is ready, ITP should show the readable exact wording and ask a simple question such as:

> **Are you happy to approve this as the agreed v1 promise?**  
> If not, tell me what you want changed.

Until you approve it, that should be the obvious next action. ITP should not push you toward `/plan-acceptance` yet.

## 1. Start with the idea you actually have

Use:

```text
/discover We should add AI summaries to long support tickets.
```

You do not need to prepare a brief first. You do not need to choose a discovery mode, create a folder, fill in a canvas, or know which individual skill comes next.

A good ITP conversation should quickly help clarify the underlying situation. For example, it may discover that support agents are not asking for “summaries” as such. Their real difficulty may be that long threads make it hard to find the customer’s latest unresolved question.

That difference matters because the first solution you thought of may not be the simplest or best way to improve the situation.

## 2. Expect ITP to explore the problem before defending the feature

Once the need is clearer, ITP should consider different ways to improve it. It might compare AI summaries with better thread structure, highlighting the unresolved question, an existing product capability, a smaller manual workflow, or doing nothing if the pain is not important enough.

This is not brainstorming for its own sake. The purpose is to avoid spending research and engineering effort on several cosmetic versions of the same assumption.

You should be able to see the real choices and why they differ without decoding methodology or internal IDs. ITP should normally show them as a short list. For example:

1. **Highlight the unresolved question** — A small UI change that makes the current question obvious. **Why choose it:** simple and reversible. **Main downside:** it may not help with other parts of a long thread.
2. **Add AI summaries** — Generate a short summary of the conversation. **Why choose it:** potentially helps with more of the ticket. **Main downside:** more uncertainty, operational complexity, and room for wrong summaries.
3. **Use the current workflow** — Build nothing and keep reading the thread manually. **Why choose it:** no implementation cost. **Main downside:** the existing pain remains.

After showing the options, ITP should give a clear recommendation. At this point it might say:

> **Recommendation:** Start with highlighting the unresolved question. It directly addresses the clearest need, is easy to reverse, and does not depend on the still-uncertain value of AI summaries.

If the evidence does not support one clear choice, ITP can recommend a small shortlist or recommend an experiment before committing.

## 3. Research only what could change the choice

Suppose the AI-summary option depends on a crucial assumption:

> Agents will save meaningful time if the latest unresolved question is summarized automatically.

If that assumption is weakly supported and important to the decision, ITP should investigate it before spending time on lower-impact details. It may suggest existing evidence, direct observation, or a bounded experiment.

If the available evidence already answers the important question, it should **not** perform research merely because a research stage exists.

This is one of the core ideas in ITP: research is there to reduce decision-changing uncertainty, not to make the document look thorough.

## 4. You make the decision

After the useful evidence is on the table, ITP can explain something like:

- A small UI change is simpler and reversible.
- AI summaries may produce a larger improvement, but the benefit is less certain and the operational complexity is higher.
- Doing nothing remains reasonable if the current problem is rare enough.

ITP should recommend a direction whenever it presents alternatives, but it does not convert that recommendation into your decision. A good recommendation is short, explains why the option fits the evidence and your stated preferences, and says what uncertainty could change the recommendation.

You might say:

> Let’s choose the smaller UI approach. We only think this outcome is worth one small iteration, and reversibility matters more than maximum capability.

That is the decision.

For a team decision, ITP can also preserve who owns the decision and who is expected to approve the final promise. For a simple individual choice, it should not force you through organizational paperwork.

## 5. Turn the choice into an exact promise

Now the question changes from:

> What should we do?

to:

> What exact outcome are we willing to commit to?

A draft promise might become:

```markdown
# Promise: Make the current customer question easy to find

## Intended outcome
Support agents can identify the customer's current unresolved question without
reading the entire ticket history.

## Promise
Long support tickets clearly surface the current unresolved customer question.

## Boundaries
Applies to the existing support-ticket view.

## Out of scope
Automatic ticket summarization and suggested replies.
```

The exact wording matters. Choosing the direction earlier does **not** mean you have approved this text.

ITP saves the proposed source, shows you the exact wording, and only records approval after you explicitly approve those exact bytes. That protects the agreement from silently changing later.

You normally do not need to think about the hash mechanics yourself. The useful mental model is simply:

> **ITP remembers exactly which promise you approved.**

## 6. Hand the promise to Promise to Proof

Once the source is approved, ITP stops before implementation.

The next command is:

```text
/plan-acceptance specs/current-question.md
```

Promise to Proof now takes responsibility for defining precise acceptance, implementing against that contract, reviewing the implementation, and proving the promised behavior.

That separation is deliberate:

```text
Idea to Promise: What should we promise?
Promise to Proof: Did we actually keep that promise?
```

## What if the answer is “don’t build it”?

That is a successful ITP outcome too.

For example, research may show that the product already has a feature that solves the need. Or the human may decide the problem is not worth the complexity. In those cases ITP should record the decision and stop rather than manufacturing a build promise just to keep the workflow moving.

Likewise, you can end with a bounded experiment if you are not ready to promise a solution yet.

## When you have been working for a long time

Sometimes the useful question is not "what should we do with this feature?" but:

> **Are we still working on the right things?**

Use:

```text
/discover zoom-out
```

You can also just say something natural like "We’ve been working on this for months. Help me step back and look at the bigger picture."

ITP should review the project's original goals, what has changed, where effort is going, what may now deserve less attention, and what important opportunities might have disappeared from view. It should then give you a few understandable strategic directions and recommend one.

A zoom-out review does not silently rewrite decisions or promises. If you choose a material change, ITP takes that choice through the normal decision or revisit path.

## You usually only need `/discover`

The individual skills—`/frame`, `/brainstorm`, `/research`, `/decide`, `/challenge-decision`, and `/shape-promise`—are useful when you want to work directly on one stage. They are not a checklist you need to run manually every time.

For everyday use, remember:

```text
/discover <your idea>
```

Then talk normally.

## Where next?

Read **[The mental model](mental-model.md)** to understand the five concepts that make ITP work, or jump straight to the **[recipe book](recipes/README.md)** for the situation you are facing today.
