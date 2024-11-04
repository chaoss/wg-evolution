# **Change Requests Accepted**

**Question:** How many accepted change requests are present in a code change?

## Overview
Change requests are defined as in [Change Requests](https://chaoss.community/metric-change-requests/). This metric measures the number of change requests that have been accepted and merged into a project's codebase. It includes changes proposed through platforms like GitHub (pull requests), GitLab (merge requests), or Gerrit (changesets). Tracking the number of accepted change requests helps to understand the level of coding activity that results in concrete changes to the code. 

By measuring this metric, project maintainers can assess the volume of accepted contributions, which serves as a proxy for project vitality and contributor engagement. The metric can also highlight trends over time, such as increased or decreased coding activity.

This metric can indirectly inform Diversity, Equity, and Inclusion (DEI) by identifying patterns in who submits accepted change requests, offering insight into the inclusivity of the project's contribution process.

## Want to Know More?

<span markdown="1"><details>
<summary>Click to read more about this metric.</summary>

### Data Collection Strategies 
- **GitHub:** Count the number of merged pull requests over a period. This can be retrieved via GitHub API.
- **GitLab:** Count merge requests accepted into the repository.
- **Gerrit:** Track accepted changesets, which are merged into the project’s code.

### Filters 
- **By Actor:** Submitter, reviewer, and merger roles.
- **By Time Period:** Filter by specific date ranges.
- **By Repository or Project:** Focus on one or more repositories.
- **By Groups of Actors:** Filter by attributes like employer, gender, or team roles.

### Visualizations
- None specified

</details></span><br>

## References
None specified

## Contributors
None specified

## Additional Information
- To edit this metric please [submit a Change Request here](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/code-development-efficiency/change-requests-accepted.md).  
- To reference this metric in software or publications, please use this stable URL: [https://chaoss.community/?p=3589](https://chaoss.community/?p=3589).

<!-- # For groupings in the knowledge base
**Context tags:** code review, source code, contribution  
**Keyword tags:** pull requests, merge requests, accepted change requests, gerrit, git, source code contribution
-->
