# New Contributors Closing Issues

Question: How many contributors are closing issues for the first time?

## Description
This metric is an indication of the volume of contributors who are closing issues for their first time. When a contributor closes an issue for the first time it is some indication of "stickiness" for the individual within a project, especially for contributors who are not also committers.

## Objectives
To know how contributors are moving through the [contributor funnel](https://mikemcquaid.com/2018/08/14/the-open-source-contributor-funnel-why-people-dont-contribute-to-your-open-source-project/) by identifying “closing issues” as a milestone in the contributor journey.

## Implementation

**Aggregators:**
* Count. Total number of new contributors closing issues on this project for the first time during a given time period.

**Parameters:**
* Period of time. Start and finish date of the period. Default: forever.
 Period during which new issue closers are counted.

### Filters
* Exclude reopened issues (optionally, filter if reopened in less than 1 hour)

### Visualizations
Table with names of contributors who closed an issue for the first time and when that was

### Data Collection Strategies
Based on the [Issues Closed](https://github.com/chaoss/wg-evolution/blob/master/metrics/Issues_Closed.md) and [Contributor](https://github.com/chaoss/wg-common/blob/master/focus-areas/who/contributors.md) definitions, enrich contributors with the date of their first time closing an issue.

## References

* [Contributor Funnel by Mike McQuaid](https://mikemcquaid.com/2018/08/14/the-open-source-contributor-funnel-why-people-dont-contribute-to-your-open-source-project/)
