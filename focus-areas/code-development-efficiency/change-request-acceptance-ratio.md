# Change Request Acceptance Ratio

**Question:** What is the ratio of change requests accepted to change requests closed without being merged?

## Overview

Change Request Acceptance Ratio  measures the ratio of change requests merged (accepted) vs change requests closed without being merged. Each [change request](https://chaoss.community/kb/metric-change-requests/) can be in one of three states: open, merged (accepted), and closed without merge (declined). Data points are derived from the ratio of merged change requests to closed change requests without merges. This provides insight into several repository characteristics, including openness to outside contributions, growth of the contributor community, the efficiency of code review processes, and, when measured over time, the trajectory of a project in its evolution. Different ratios should be interpreted in the context of each repository or project.  Reviewing this metric over time can help identify trends and inform strategies for improving project health and sustainability and actively promote a culture of acceptance and collaboration.

## Want to Know More?

<span markdown="1"><details>

<summary>Click to read more about this metric.</summary>

## Data Collection Strategies

Potential parameters include:

*   Time Period Granularity (Weekly, Monthly, Annually).
*   Change in ratio over the period of time.
*   Show contributor count
*   Origin of change request: branch or fork? Change requests from repository forks are more commonly from outside contributors, while branch originating change requests come from people with repository commit rights.

Potential aggregators include:

*   Total change requests merged (accepted)
*   Total change requests closed without merge
*   Total change requests in an open state

### Visualizations

CHAOSS tools provide a number of visualizations for this metric. The first visualization shows the accepted and declined change requests organized annually, from which ratios can be derived.

![Closed PR Volume](https://raw.githubusercontent.com/chaoss/wg-evolution/main/focus-areas/code-development-efficiency/images/change-request-acceptance-ratio_closed-pr-volume.png)

![Review/Week](https://raw.githubusercontent.com/chaoss/wg-evolution/main/focus-areas/code-development-efficiency/images/change-request-acceptance-ratio_review-week.png)

![Reviews Accepted/Week](https://raw.githubusercontent.com/chaoss/wg-evolution/main/focus-areas/code-development-efficiency/images/change-request-acceptance-ratio_reviews-accepted-week.png)

</details></span><br>

## References

*   [Augur Zephyr report on pull requests](https://docs.google.com/presentation/d/11b48Zm5Fwsmd1OIHg4bse5ibaVJUWkUIZbVqxTZeStg/edit#slide=id.g7ec7768776_1_56)
*   [Augur Community requests](https://github.com/chaoss/augur-community-reports)
*   [Augur](https://github.com/chaoss/augur)

## Contributors

*   Matt Germonprez
*   Kevin Lumbard
*   Elizabeth Barron
*   Peculiar C Umeh

## Additional Information

To edit this metric please [submit a Change Request here](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/code-development-efficiency/change-request-acceptance-ratio.md)

To reference this metric in software or publications please use this stable URL: <https://chaoss.community/?p=3598>

<!-- # For groupings in the knowledge base
Context tags: Platform, Contribution
Keyword tags: change request, acceptance ratio, change requests closed, code review, declined, change request merged
-->
