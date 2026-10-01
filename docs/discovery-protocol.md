# Discovery protocol

Idea to Promise (ITP) turns an uncertain idea into a researched, explicit source
promise worth making. It stops before acceptance planning and implementation.

## Boundary

ITP answers **what should we promise, and why?** Promise to Proof (P2P) answers
**what exactly would make that promise true, can we implement it faithfully, and
can we prove it?**

```text
need/job
  ↓
opportunity space
  ↓
solution alternatives
  ↓
riskiest assumptions
  ↓
research ↔ bounded experiment
  ↓
human decision + appetite
  ↓
optional challenge: rabbit holes + premortem
  ↓
future-experience check
  ↓
exact source promise
  ↓
Promise to Proof
```

ITP must not create P2P acceptance matrices, select proof oracles, invent
candidate identities, declare implementation acceptance, or treat source approval
as delivery authority.

## Frame the real need

A frame separates the proposed solution from the underlying need. It records:

- actors,
- progress sought,
- current workaround,
- intended observable outcome,
- behavior/change needed,
- status-quo consequence,
- constraints,
- decision criteria,
- assumptions and material unknowns,
- research bounds.

The purpose is to avoid feature-first framing. A proposed feature may be useful
context but is not automatically the requirement.

## Opportunity before solution

Brainstorming first explores the opportunity space using stable O1, O2, ... IDs.
An opportunity describes an unmet need, obstacle, or desired progress for an
actor. It must not secretly encode a solution.

Only then does the workflow create solution alternatives A1, A2, ... and record
which O-IDs each addresses.

This separation helps reveal when several apparently different features are
actually attempts to solve the same underlying need, or when one broad problem
contains several distinct opportunities.

## Risk-prioritized research

Research asks: **what must be true for this alternative to work?**

Each material claim C1, C2, ... records:
- kind,
- risk lens,
- criticality,
- evidence strength,
- support,
- evidence,
- counterevidence,
- decision impact,
- next check or stopping reason.

Risk lenses may include desirability, feasibility, viability, adaptability,
compliance, or another clearly named domain risk.

Criticality describes how much the decision depends on the claim. Evidence
strength describes how well the claim is currently supported.

Research normally attacks high-criticality claims with weak or no evidence first.
It should not spend equal effort on every uncertainty.

Do not convert user reports into observations or plausible inferences into facts.
Keep material contradictions visible.

## Bounded experiments

Use an experiment when observation can answer a load-bearing question more
cheaply or credibly than more discussion.

Before execution, record:
- question and hypothesis,
- scope/exposure,
- method,
- observation/metric,
- decision rule describing what result would change the decision,
- stop condition.

After execution record the actual action, result, limitations, and affected claim
IDs. Never define the decision rule after seeing the result.

Experiments do not gain production authority merely because they are part of ITP.

## Stop research deliberately

Stop when the high-criticality weak claims are resolved enough for the decision,
another reasonable check is unlikely to change the choice, an agreed bound is
reached, or an essential input is unavailable.

Residual uncertainty remains visible. Research may recommend a direction, but it
cannot make the human decision.

## Decide with an appetite

The decide stage reduces the work to viable options and distinguishes:
- evidence,
- uncertainty,
- preferences,
- binding constraints,
- appetite.

Appetite answers **how much is this outcome worth?** It may bound effort,
complexity, operational burden, or experiment exposure. It is not an estimate or
a guarantee that delivery will fit.

Use appetite to reject, shrink, or reshape options that demand more than the
outcome is worth.

Only an explicit attributable human choice creates or updates decision.md.
Valid directions remain pursue, experiment, defer, and reject.

## Independent challenge

For consequential work, challenge-decision checks the evidence-to-decision path
and then adds two focused techniques.

### Rabbit holes

Identify concrete areas where hidden complexity, dependencies, migration,
operations, security, adoption, integration, or organizational work could
disproportionately threaten the outcome or appetite.

Do not emit a generic risk checklist. Every rabbit hole needs a plausible trigger
and a cheap way to bound it where possible.

### Premortem

Assume the decision was pursued and six months later clearly failed to deliver
the intended outcome. Identify the few most plausible causal explanations grounded
in the current context.

Classify each as already covered, worth a bounded check, a reason to change the
decision, or acceptable residual risk.

Challenge findings are advisory and cannot silently replace the human decision.

## Work backwards from the future experience

Before shaping the promise, explain the beneficiary's future experience:
- what they can now do, understand, avoid, or accomplish,
- why that is meaningfully better than the current workaround,
- which opportunity it addresses,
- what skeptical question could expose vagueness or overbreadth.

If the value can only be explained in implementation terms, or the future is not
clearly better, return to framing/decision rather than polishing the promise.

## Work item and exact approval

Active discovery records remain under .itp/work/<slug>/ and the final durable
promise normally lives in a project-owned path such as specs/<slug>.md.

Promises use human-readable revisions. Exact approval remains bound to SHA-256 of
the exact UTF-8 bytes of the durable promise. Any byte change invalidates the old
approval.

After exact source approval, hand the promise to P2P separately:

```text
/plan-acceptance <agreed-source-path>
```

ITP approval does not approve the later P2P acceptance contract or authorize
implementation, commit, push, publication, or merge.
