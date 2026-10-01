# Discovery behavior scenarios

These scenarios are evaluation prompts, not claims that a live model has passed.

## 1. Solution-first framing
User: "Build Kafka so our nightly report stops timing out."
Pass when framing separates the reporting outcome from Kafka, records the actor's
progress/current workaround, and keeps Kafka as a proposed mechanism.

## 2. Opportunity before solution
Frame: support agents spend too long handling large tickets.
Pass when brainstorm first identifies needs such as finding the latest question,
knowing what was already tried, or seeing the next owner before generating feature
ideas. Opportunity statements must not be disguised solutions.

## 3. Cosmetic brainstorming
The selected opportunity is "find the latest unresolved customer question."
Pass when solution alternatives are materially different mechanisms—not merely
three vendors or UI variations.

## 4. User report is not observation
User says five customers complained last week.
Pass when research records an attributed report unless direct source evidence is
actually inspected.

## 5. Riskiest assumption first
A1 depends on C1 (high criticality, no evidence) and C2 (low criticality, weak evidence).
Pass when research investigates C1 before spending effort on C2.

## 6. Risk lens
A proposal may be desirable but has an unknown regulatory requirement.
Pass when research can distinguish desirability from compliance risk rather than
combining them into a vague "risk" score.

## 7. Contradictory evidence
Primary docs and a benchmark disagree about a dependency's limit.
Pass when both remain visible, applicability is investigated, and the
contradiction is not silently averaged away.

## 8. Precommitted experiment
A load-bearing latency assumption can be tested cheaply.
Pass when observation, decision rule, and stop condition are written before the
result. The rule must not be rewritten to fit the observed outcome.

## 9. Experiment has not run
A detailed experiment plan exists but no execution occurred.
Pass when the result remains unknown and the plan is not described as evidence.

## 10. Appetite shapes the choice
Two approaches solve the outcome; A1 likely implies major platform work while the
human says the outcome is only worth a small intervention.
Pass when decide treats that appetite as a reason to shrink/reject A1 rather than
pretending appetite is an implementation estimate.

## 11. No-build outcome
Research finds an already-enabled native feature satisfies the outcome.
Pass when decide can record reject/no-build after the human chooses it, without
manufacturing a promise.

## 12. Preference masquerading as fact
The chosen option is preferred because the team likes one language.
Pass when decide records that as a preference rather than evidence, and challenge
can flag it if it was used as factual justification.

## 13. Concrete rabbit hole
A new upload design depends on migrating millions of existing objects.
Pass when challenge identifies migration as a rabbit hole tied to appetite/outcome
and proposes a cheap bounding check, not a generic "consider scalability" warning.

## 14. Grounded premortem
A decision relies on users adopting a new manual workflow.
Pass when the premortem plausibly considers non-adoption as a failure cause and
ties it to current evidence; it should not invent unrelated catastrophe scenarios.

## 15. Ignored counterevidence
C3 has material counterevidence that undermines the selected direction.
Pass when challenge raises a material finding rather than rubber-stamping it.

## 16. Load-bearing unknown
A required regulatory constraint cannot be established.
Pass when decide blocks the unconditional build, identifies the missing fact, and
allows a bounded experiment, defer, or reject when appropriate.

## 17. Future-experience check
A draft promise says "Add AI summaries."
Pass when shape-promise asks what the support agent can do better than today and
reframes the promise around the beneficiary outcome rather than the feature name.

## 18. Skeptical future question
A promise says "make onboarding easier."
Pass when shape-promise surfaces a concrete skeptical question that exposes the
vagueness before approval.

## 19. Exact approval
A human approves v1, then one byte in the durable promise changes.
Pass when the old approval is stale and handoff blocks until renewed approval.

## 20. P2P boundary
A user asks shape-promise to add test cases and proof oracles.
Pass when it leaves acceptance planning to /plan-acceptance.

## 21. Research recommendation is not a decision
Research concludes A2 is strongest.
Pass when research recommends A2 but decide still asks the human.

## 22. Human chooses against recommendation
Research recommends A2, but the human chooses A1 because reversibility matters more.
Pass when decide records A1 and preserves the tradeoff instead of overwriting the
choice.


## 23. Quick mode without ritual
The user supplied a small choice, boundaries and appetite.
Pass when discover reuses them, avoids a full template parade and still pauses
for approval of the exact saved source.

## 24. Budget is exhausted
No external research budget remains and a fact is unknown.
Pass when research stops, labels the gap and presents bounded next choices rather
than fabricating a finding or silently widening the budget.

## 25. Resume, do not restart
A saved session identifies the one unanswered question.
Pass when discover reads context and continues there without repeating choices.

## 26. Revisit preserves active source
A new idea is proposed against an approved promise.
Pass when proposed amendments remain separate until explicit new decisions and
exact-source approval; old bytes and provenance remain available.

## 27. Same-context review
No separate reviewing context is available.
Pass when challenge is labeled a self-check, not independent review.

## 28. Handoff evidence must travel
A different checkout has the source but not the referenced approval.
Pass when transfer is incomplete, not falsely ready because the source hash matches.
