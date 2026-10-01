# A challenge changes the selected approach

> Fictional teaching example. The dialogue and source notes are authored fixtures, not live-agent output, customer research, or real approval.

## Initial discovery

The fictional team wants operators to find failed uploads. O1 is finding the next
failed item, not replacing storage. S1 describes an existing failure list. A1 adds
a focused filter to that list; A2 migrates all upload history into a new search
system. The initial supplied evidence leaves migration effort uncertain.

**User:** “Choose A2. The outcome is worth at most one small iteration.”

D1 records the choice and appetite, but C3—“historical records can be migrated
cheaply”—remains high criticality and weakly evidenced. Choosing A2 did not resolve C3.

## Challenge

A same-context self-check, explicitly not an independent review, inspects fixture
S2: older history uses a different ownership model. A concrete rabbit hole is
reconciling owners during migration. The consequence is not generic scalability;
it is uncertain work beyond the chosen appetite. A plausible premortem is that
the team spends the iteration migrating data and never delivers a useful operator
view. This is a conditional risk, not a claim that failure has occurred.

**Agent:** “A1 can address O1 without migrating historical ownership. A2 may still
be valuable, but the supplied evidence does not bound it within your appetite.”

**User:** “Change the decision to A1. Keep migration out of scope.”

## History and new promise

Retain D1's original bytes in history/decision-D1.md. Create active D2 with
Supersedes: D1, the explicit new statement, evidence and accepted tradeoff: the
operator view is improved but historical cross-system search is not.

The draft promise now states that operators can filter the existing failure list
and identify the next failed upload, preserving the existing ownership boundary.
It excludes historical migration. It says nothing about which UI library to use.

## Handoff gate

Present exact proposed source wording for approval; there was no prior source
approval to reuse. The example does not claim a real receipt, a separate reviewing
agent, or implemented behavior. A challenge led to a human amendment—not an agent
overwriting the choice in the background.
