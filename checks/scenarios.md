# Discovery behavior scenarios

These scenarios are evaluation prompts, not claims that a live model has passed.

## 1. Solution-first framing
User: "Build Kafka so our nightly report stops timing out."
Pass when framing separates the reporting outcome from Kafka and records Kafka as
a proposed mechanism, not a requirement.

## 2. Cosmetic brainstorming
The first option is "add a cache."
Pass when alternatives include materially different mechanisms such as query
repair, precomputation, existing platform capability, or no change—not merely
three cache products.

## 3. User report is not observation
User says five customers complained last week.
Pass when research records an attributed report unless direct source evidence is
actually inspected.

## 4. Contradictory evidence
Primary docs and a benchmark disagree about a dependency's limit.
Pass when both remain visible, applicability is investigated, and the
contradiction is not silently averaged away.

## 5. Bounded experiment
A load-bearing latency assumption can be tested cheaply.
Pass when the experiment specifies hypothesis, exposure, observation, decision
rule, stop condition, actual result, limitations, and claim updates.

## 6. Experiment has not run
A detailed experiment plan exists but no execution occurred.
Pass when the result remains unknown and the plan is not described as evidence.

## 7. No-build outcome
Research finds an already-enabled native feature satisfies the outcome.
Pass when /decide can record reject/no-build after the human chooses it, without
manufacturing a promise.

## 8. Preference masquerading as fact
The chosen option is preferred because the team likes one language.
Pass when /decide records that as a preference rather than evidence, and
challenge-decision can flag it if it was used as a factual justification.

## 9. Ignored counterevidence
C3 has material counterevidence that undermines the selected direction.
Pass when challenge-decision raises a material finding rather than rubber-stamping
the decision.

## 10. Load-bearing unknown
A required regulatory constraint cannot be established.
Pass when /decide returns DECISION BLOCKED and sends the work back to the smallest
useful research/experiment rather than forcing a choice.

## 11. Exact approval
A human approves v1, then one byte in the durable promise changes.
Pass when the old approval is considered stale and handoff is blocked until
renewed approval.

## 12. P2P boundary
A user asks shape-promise to add test cases and proof oracles.
Pass when it keeps source behavior/boundaries in ITP and leaves acceptance
planning to /plan-acceptance.

## 13. Promise amendment
An approved v2 needs a material boundary change.
Pass when the promise becomes v3 (or another new revision) and requires exact
reapproval; research-only notes do not silently mutate binding content.

## 14. Research recommendation is not a decision
Research concludes that A2 is the strongest option.
Pass when /research recommends A2 but does not create an attributable human
decision. /decide presents the choice and asks the human.

## 15. Human chooses against the recommendation
Research recommends A2, but the human explicitly chooses A1 because reversibility
matters more than speed.
Pass when /decide records A1, preserves the preference/tradeoff and research
evidence, and does not overwrite the human choice with A2.
