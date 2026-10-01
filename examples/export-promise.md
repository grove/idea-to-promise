# Promise: Preserve report filters in exports

Promise revision: v1
Status: DRAFT

## Intended outcome
An analyst can export the report results they selected without rebuilding filters.

## Promise
Export all rows matching the report's currently selected filters, not only the
current page. Retain the existing report export format.

## Boundaries
Applies to an export initiated from the current report view. It does not introduce
a scheduler or change how filters are chosen.

## Binding constraints
Preserve existing export authorization and data access boundaries.

## Out of scope
Scheduled exports, report-engine replacement, and new report formats.

## Assumptions and open questions
Repository feasibility remains for acceptance planning. No customer measurement
or live implementation result is claimed by this fictional fixture.

## Advisory rationale
This draft illustrates the quick-export example. It is not a real approved source.
