# A small feature, without a big process

> Fictional teaching example. The dialogue and source notes are authored fixtures, not live-agent output, customer research, or real approval.

## Seed and frame

**User:** “Quick discovery: exports lose my selected report filters. Use the same
filters. This is worth a small fix, not a reporting rewrite.”

**Agent:** “The need is to export the view you are already inspecting. You have
already chosen the direction and a small appetite; I will not ask you to choose
those again. The one boundary question is whether the export includes the current
page or all rows matching the filters.”

**User:** “All matching rows. Keep the existing export permissions.”

## Compact notebook

**Need:** O1 — an analyst can take the selected report results into a spreadsheet
without manually reconstructing the filter.

**Options:** A1 — manually filter the exported full report; A2 — use the existing
report filter in the export. A reporting rewrite adds no needed outcome here.

**Evidence and unknowns:** C1, attributed-report: the supplied request says export
loses the filter. This is not a measured production observation. The product
boundary is now explicit; repository feasibility remains for delivery planning.
No broad market research would change this narrow choice.

**Decision:** D1, active, pursue A2. The quoted user instructions supply the choice,
small appetite, all-matching-rows boundary and existing authorization constraint.
Reversibility is high in this fixture; if delivery requires a broad rewrite,
revisit the appetite rather than silently expanding scope.

**Challenge:** skipped for this small, bounded choice. No independent review is
claimed. A same-context check confirms “all matching rows” is not “current page.”

## Promise

The [draft source](export-promise.md) promises the observable export behavior,
not a particular query implementation. Existing permissions remain binding.

**Agent:** “Here is the saved wording. Please approve this exact source, or tell
me what to change.” The example stops at the approval gate. There is no real
approval receipt and no claim that the export was implemented.

## What follows in a real project

Compute the real file identity, capture explicit approval separately, verify the
handoff and propose `/plan-acceptance <source>`. A general “good idea” would not
approve the exact text. One notebook plus the eventual source/receipt is enough.
