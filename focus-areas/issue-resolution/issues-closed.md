# Issues Closed

**Question: How many issues were closed during a certain period?**

## Overview

Issues Closed measures issues  that changed to state closed during a certain period. Issues are defined as in [Issues New](https://chaoss.community/metric-issues-new/). Data points consist of the count of issues that transitioned to a closed state during the measurement period.  Some projects may use different states or tags, such as 'fixed,' to indicate a closed issue. In most issue trackers, closed issues can be reopened after they are closed. Reopening an issue can be considered as opening a new issue, or making void the previous close (see parameters, below).
A high volume of closed issues indicates a productive and engaged community actively resolving issues.  By tracking code-related closed issues, you can gain insights into the overall activity level of a project in completing its work. This metric is not the only one that should be used to track volume of coding activitY.

## Want to Know More?

<span markdown="1"><details>

<summary>Click to read more about this metric.</summary>

### Data Collection Strategies

**Specific description: GitHub**

In the case of GitHub, closed issues are defined as "issues which are closed".

**Specific description: GitLab**

In the case of GitLab, closed issues are defined as "issues
that are closed".

**Specific description: Jira**

In the case of Jira, closed issues are defined as "issues that change to the closed state".

**Specific description: Bugzilla**

In the case of Bugzilla, closed issues are defined as "bug reports that change to the closed state".

**Aggregators:**

*   Count. Total number of closed issues during the period.
*   Ratio. Ratio of closed issues over total number of issues during that period.
*   Reactions. Number of "thumb-ups" or other reactions on issues.

**Parameters:**

*   Period of time. Start and finish date of the period during which issues are considered. Default: forever.

*   Criteria for source code. Algorithm. Default: all issues are related to
    source code.\
    If we focus on source code, we need a criterion for deciding
    whether an issue is related to the source code or not.
    All issues could be included in the metric by altering the default.

*   Reopen as new. Boolean, defining whether reopened issues are considered
    as new issues. If false, it means the closing event previous to a
    reopen event should be considered as void. Note: if this parameter is
    false, the number of closed issues for any period could change in the
    future, if some of them are reopened.

*   Criteria for closed. Algorithm. Default: having a closing event during
    the period of interest.

### Filters

*   By actors (submitter, commenter, closer). Requires merging identities corresponding to the same author.
*   By groups of actors (employer, gender... for each of the actors). Requires actor grouping, and likely, actor merging.

### Visualizations

*   Count per time period over time
*   Ratio per time period over time

These could be grouped by applying the filters defined above or represented as bar charts, with time running in the X axis.

[GrimoireLab](https://chaoss.github.io/grimoirelab)
![GrimoireLab](https://raw.githubusercontent.com/chaoss/wg-evolution/main/focus-areas/issue-resolution/images/issues-closed_grimoirelab.png).

</details></span>

## Contributors

*   Vinod K. Ahuja
*   Dawn Foster
*   Kevin Lumbard
*   Peculiar C Umeh

## Additional Information

To edit this metric please [submit a Change Request here](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/issue-resolution/issues-closed.md)

To reference this metric in software or publications please use this stable URL: <https://chaoss.community/?p=3633>

<!-- # For groupings in the knowledge base
Context tags: Platform, Contribution, Lifecycle
Keyword tags: bug report, problems, issues, closed
→
