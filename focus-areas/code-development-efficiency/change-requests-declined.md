# **Change Requests Declined**

**Question:** What change requests ended up being declined during a certain period?

## Overview
This metric measures the number of change requests that were proposed but ultimately declined during a given period. A change request is considered declined when it is closed without being merged into the codebase. Examples include GitHub pull requests that are closed without merging, GitLab merge requests that are not accepted, and Gerrit changesets that are abandoned.

Tracking declined change requests helps assess how many proposals or contributions did not result in code changes. This can provide insight into inefficiencies in the development process or highlight areas of improvement in managing code contributions. Understanding which change requests are declined and why can also inform Diversity, Equity, and Inclusion (DEI) efforts by revealing potential biases in review processes.

## Want to Know More?

<details>
<summary>Click to read more about this metric.</summary>

### Data Collection Strategies 

Potential aggregators include: 
* Count. Total number of declined change requests during the period.
* Ratio. Ratio of declined change requests over the total number of change requests during that period.

Potential parameters include: 
* Period of time. Start and finish date of the period during which declined change requests are considered. Default: forever.
* Criteria for source code. Algorithm. Default: all files are source code. If we focus on source code, we need a criterion to decide whether a file belongs to the source code or not.

**Specific description: GitHub**

In the case of GitHub, declined change requests are defined as "pull requests that are closed with their changes not being included in the git repository", as long as it proposes changes to source code files.

See the discussion in the specific description for GitHub in [Change Requests Accepted](https://chaoss.community/metric-change-requests-accepted/), since it applies here as well.

Mandatory parameters (for GitHub):

* Heuristic for detecting declined change requests, telling apart those cases where the change request was closed, but the changes were included in the git repository manually. Default: None.

**Specific description: GitLab**

In the case of GitLab, declined reviews are defined as "merge requests that are closed with their changes not being included in the git repository", as long as it proposes changes to source code files.

Mandatory parameters (for GitLab):

* Heuristic for detecting declined change requests, telling apart those cases where the merge request was closed, but the changes were included in the git repository manually. Default: None.

**Specific description: Gerrit**

In the case of Gerrit, declined change requests are defined as "changesets abandoned", as long as they propose changes to source code files.

- Collect data from repositories on declined pull requests, merge requests, or abandoned changesets.
- Collect metadata about the reasons for declined change requests, such as reviewer comments, to understand patterns.

### Filters 
- **By Actor:** Submitter, reviewer, or merger.
- **By Group:** Filter by employer, gender, or other actor attributes.
- **By Time Period:** Specify the start and end dates for analysis.
- **By Ratio:** Ratio of declined change requests to total change requests.

### Visualizations
- None Specified

</details>

## References
None specified

## Contributors
None specified

## Additional Information
- To edit this metric please [submit a Change Request here](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/code-development-efficiency/change-requests-declined.md).  
- To reference this metric in software or publications, please use this stable URL: [https://chaoss.community/?p=3588](https://chaoss.community/?p=3588).

<!-- # For groupings in the knowledge base
**Context tags:** code contribution, code review, change requests, project activity  
**Keyword tags:** declined change requests, pull requests, merge requests, Gerrit, GitHub, GitLab
-->
