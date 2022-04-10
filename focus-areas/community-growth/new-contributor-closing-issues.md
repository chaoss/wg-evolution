# New Contributors Closing Issues

Question: How many contributors are closing issues for the first time in a given project?

## Description
This metric is an indication of the volume of contributors who are closing issues for their first time within a given project. When a contributor closes an issue for the first time it is some indication of "stickiness" of the individual within that project, especially for contributors who are not also committers.

## Objectives
To know how contributors are moving through the [contributor funnel](https://mikemcquaid.com/2018/08/14/the-open-source-contributor-funnel-why-people-dont-contribute-to-your-open-source-project/) by identifying “closing issues” as a milestone in the contributor journey.

## Implementation
*The usage and dissemination of health metrics may lead to privacy violations. Organizations may be exposed to risks. These risks may flow from compliance with the GDPR in the EU, with state law in the US, or with other law. There may also be contractual risks flowing from terms of service for data providers such as GitHub and GitLab. The usage of metrics must be examined for risk and potential data ethics problems. Please see [CHAOSS Data Ethics document](https://github.com/chaoss/community/blob/main/data-use-statement.md) for additional guidance.*

**Aggregators:**
* Count. Total number of contributors closing issues on this project for the first time during a given time period.
* Percentage. Proportion of contributors closing issues on this project *for the first time* during a given time period, computed against *all* contributors having closed issues on this project during the same time period.

**Parameters:**
* Period of time. Start and finish date of the period during which new issue closers are counted. Default: forever (i.e., the entire observable project lifetime)

### Filters
* Exclude reopened issues (optionally, filter if reopened in less than 1 hour)

### Visualizations
* Table with names of contributors who closed an issue for the first time and when that was.
* Timeline showing the time on the x-axis, and the aggregated metric value on the y-axis for fixed consecutive periods of time (e.g. on a monthly basis). This visualisation allows to show how the metric is evolving over time for the considered project.

### Data Collection Strategies
Based on the [Issues Closed](https://chaoss.community/metric-issues-closed/) and [Contributor](https://chaoss.community/metric-contributors/) definitions, enrich contributors with the date of their first time closing an issue.

## References

* [Contributor Funnel by Mike McQuaid](https://mikemcquaid.com/2018/08/14/the-open-source-contributor-funnel-why-people-dont-contribute-to-your-open-source-project/)
