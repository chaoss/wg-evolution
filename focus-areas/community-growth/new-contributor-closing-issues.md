# **New Contributors Closing Issues**

**Question:** How many contributors are closing issues for the first time in a given project?

## Overview
This metric tracks the number of contributors who close an issue for the first time in a project. Closing an issue for the first time can signal that a contributor has become more engaged in the project, indicating "stickiness" or progression along the contributor journey. It is especially relevant for non-committer contributors, as issue management is a critical activity in the health of open-source communities.

Measuring the number of new contributors who close issues provides insight into how individuals are progressing through the contributor funnel. It helps project maintainers understand whether contributors are transitioning from participation in discussions to more involved roles, which is a good indicator of community growth and retention. This metric can also highlight opportunities for encouraging new contributors to take on more responsibilities in the project.

## Want to Know More?

<span markdown="1"><details>
<summary>Click to read more about this metric.</summary>

### Data Collection Strategies
- Based on the [Issues Closed](https://chaoss.community/metric-issues-closed/) and [Contributor](https://chaoss.community/metric-contributors/) definitions, enrich contributors with the date of their first time closing an issue.
- Track the number of unique contributors who close an issue for the first time by collecting timestamps when contributors close an issue.
- Use contributor information to identify first-time issue closers.
- Enrich contributor data by adding the date they first closed an issue.

### Filters 
- **Exclude Reopened Issues:** Optionally exclude issues that were reopened within a specific period (e.g., less than one hour).

### Visualizations
- **Table:** A table showing the names of contributors who closed an issue for the first time and the date when that occurred.
- **Timeline:** A timeline with time on the x-axis and the aggregated count of new issue closers on the y-axis, showing how the number of new contributors closing issues changes over time.

</details></span><br>

## References
- [Contributor Funnel by Mike McQuaid](https://mikemcquaid.com/2018/08/14/the-open-source-contributor-funnel-why-people-dont-contribute-to-your-open-source-project/)

## Contributors
None specified

## Additional Information
- To edit this metric please [submit a Change Request here](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/community-growth/new-contributor-closing-issues.md).  
- To reference this metric in software or publications, please use this stable URL: [https://chaoss.community/?p=3615](https://chaoss.community/?p=3615).

<!-- # For groupings in the knowledge base
**Context tags:** contributor retention, issue management, community growth  
**Keyword tags:** new contributors, issue closing, contributor engagement, open source projects, community retention, contributor funnel
 -->
