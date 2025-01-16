# Issues New

**Question:** How many new issues are created during a certain period?

## Overview

Issues New measures the number of new issues created within a specified period. Each of these tickets (issues) are opened (submitted) by a certain person, and are later commented and annotated by many others. Data points consist of the count of issues that were initially opened or submitted during the measurement period. Issues can be reopened after being closed. Reopening an issue can be considered as opening a new issue (see parameters, below). For example, "issues" correspond to "issues" in the case of GitHub, GitLab or Jira, to "bug reports" in the case of Bugzilla, and to "issues" or "tickets" in other systems. Tracking issues provide insights into project activity and engagement. A high volume of new issues indicates an active community discussing problems, proposing solutions, and contributing to project development. Issues New monitors the level of ongoing discussion and engagement too. Analyzing the types of issues being created can provide insights into potential areas where DEI efforts may be needed to address specific concerns to participation.

## Want to Know More?

<span markdown="1"><details>

<summary>Click to read more about this metric.</summary>

### Data Collection Strategies

**Specific description: GitHub**

In the case of GitHub, an issue is defined as an "issue".

The date of the issue can be defined (for considering it in a period or not)
as the date in which the issue was opened (submitted).

**Specific description: GitLab**

In the case of GitHub, an issue is defined as an "issue".

The date of the issue can be defined (for considering it in a period or not)
as the date in which the issue was opened (submitted).

**Specific description: Jira**

In the case of Jira, an issue is defined as an "issue".

The date of the issue can be defined (for considering it in a period or not)
as the date in which the issue was opened (submitted).

**Specific description: Bugzilla**

In the case of Bugzilla, an issue is defined as a "bug report",
as long as it is related to source code files.

The date of the issue can be defined (for considering it in a period or not)
as the date in which the bug report was opened (submitted).

**Aggregators:**

*   Count. Total number of new issues during the period.
*   Ratio. Ratio of new issues over total number of issues during that period.

**Parameters:**

*   Period of time. Start and finish date of the period during which issues are considered. Default: forever.

*   Criterion for source code. Algorithm. Default: all issues are related to
    source code.\
    If we focus on source code, we need a criterion for deciding
    whether an issue is related to the source code or not.<br>

*   Reopen as new. Boolean. Default: False.\
    Criterion for defining whether reopened issues are considered
    as new issues.

### Filters

*   By actors (submitter, commenter, closer). Requires merging identities corresponding to the same author.
*   By groups of actors (employer, gender... for each of the actors).
    Requires actor grouping, and likely, actor merging.

### Visualizations

*   Count per time period over time
*   Ratio per time period over time

These could be grouped by applying the filters defined above.
These could be represented as bar charts, with time running in the X axis.
Each bar would represent proposals to change the code
during a certain period (eg, a month).

</details></span><br>

## Contributors

*   Georg J.P. Link
*   Dawn Foster
*   Kevin Lumbard
*   Peculiar C Umeh

## Additional Information

To edit this metric please [submit a Change Request here](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/code-development-efficiency/change-requests-duration.md)

To reference this metric in software or publications please use this stable URL: <https://chaoss.community/?p=3587>

<!-- # For groupings in the knowledge base
Context tags: Lifecycle, Contribution, Platform
Keyword tags: change request, accepted changes, review duration,  merged, code base, 
-->
