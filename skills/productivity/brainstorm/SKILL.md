---
name: brainstorm
description: Explore needs and genuinely different approaches, including existing solutions and doing nothing.
license: Apache-2.0
metadata:
  version: "0.6.0"
---

Read [the discovery protocol](references/discovery-protocol.md) before acting.
Bundled templates are optional aids, not a mandatory artifact checklist.

# Explore opportunities, then alternatives

Read the frame. First identify distinct unmet needs or obstacles (O-IDs), marking
evidence versus assumptions. Then explore materially different mechanisms
(A-IDs) linked to those needs. For a narrow settled need, one opportunity is enough.

Include doing nothing, existing/native capability and a smaller/manual/reversible
intervention where credible. Treat an already-sufficient capability seriously;
do not discard it merely because it produces no new software. Do not call vendor
variants or cosmetic UI changes independent mechanisms.

For each useful option explain its mechanism, outcome, tradeoffs, prerequisites,
reversibility, important assumptions and cheapest useful check. Use the actual
criteria, not invented scores. Keep unsupported ideas labeled as ideas.

## Present alternatives simply

Whenever alternatives are shown to the end user, make them easy to scan. Use a
numbered or bulleted list by default rather than a dense table. Give each option a
short plain-language name, then explain:

- **What it means:** one or two simple sentences.
- **Why you might choose it:** the strongest reason in its favor.
- **Main downside:** the most important cost, risk, or limitation.

Include extra technical detail only when it helps the present decision. Do not
make the user decode internal IDs, evidence notation, or architecture jargon just
to understand the choices.

After the list, always give a clearly labeled **Recommendation**. Recommend the
strongest option when one stands out. If evidence does not justify a single
winner, recommend a small shortlist and explain what separates them, or recommend
an experiment/defer path when that is the most responsible next move.

A recommendation is advisory. It is never the human decision.

Save Options in the quick notebook or alternatives.md. Preserve prior IDs and
human edits. Recommend `/research <alternatives>` for consequential uncertainty;
otherwise `/decide <context>`. A leading option is not a human choice.

## Compound durable learning

If this work surfaces a durable, non-obvious lesson likely to help future ITP work,
invoke the `compound-learning` skill before finishing. Do not invoke it for routine
facts, one-off details, already-recorded evidence, or merely because the work was
difficult. Compounding is advisory: it must not create or replace a human decision,
change an approved promise, add scope, or silently rewrite shared ITP behavior.

