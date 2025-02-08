# Change Requests Duration

**Question:** What is the duration of time between the moment a change request starts and the moment it is accepted or closed?

## Overview

Change Requests Duration measures the time from when a change request starts to when it ends (by being accepted and merged into the code base), applicable only to [accepted change requests](https://chaoss.community/metric-change-requests-accepted/). Data points here represent the duration of each accepted change request, calculated from its opening date to the date it is merged into the codebase. In case there are comments or other events after the code is merged, they are not considered for measuring the duration of the [change requests](https://chaoss.community/metric-change-requests/).  For example, in GitLab a change request starts when a developer uploads a proposal for a change in code, opening a change request. A project with a history of long change request durations may create a negative perception among contributors, and might discourage them from participating.

## Want to Know More?

<span markdown="1"><details>

<summary>Click to read more about this metric.</summary>

### Data Collection Strategies

**Specific description: GitHub**

In the case of GitHub, duration is considered for pull requests that are accepted and merged in the code base. For an individual pull request, duration starts when it is opened, and finishes when the commits it includes are merged into the code base.

Mandatory parameters (for GitHub): None.

**Specific description: GitLab**

In the case of GitLab, duration is considered for merge requests that are accepted and merged in the code base. For an individual merge request, duration starts when it is opened, and finishes when the commits it includes are merged into the code base.

Mandatory parameters (for GitLab): None.

**Specific description: Gerrit**

In the case of Gerrit, duration is considered for code reviews that are accepted and merged in the code base. For an individual code review, duration starts when it is opened, and finishes when the commits it includes are merged into the code base.

*   Mandatory parameters (for Gerrit): None.

Potential aggregators include:

*   Median. Median (50% percentile) of change request duration for all accepted change requests in the considered period of time.

Potential parameters include:

*   Period of time. Start and finish date of the period. Default: forever. Period during which accepted change requests are considered. An accepted change request is considered to be in the period if its creation event is in the period.
*   Criteria for source code. Algorithm. Default: all files are source code. If we are focused on source code, we need a criteria for deciding whether a file is a part of the source code or not.

### Filters

*   By actors (submitter, reviewer, merger). Requires actor merging (merging ids corresponding to the same author).
*   By groups of actors (employer, gender... for each of the actors). Requires actor grouping, and likely, actor merging.
*   Median per month over time
*   Median per group over time
*   Distribution of durations for a certain period

</details></span><br>

## Reference

None Specified

## Contributors

*   Matt Germonprez
*   Elizabeth Barron
*   Kevin Lumbard
*   Peculiar C. Umeh

## Additional Information

To edit this metric please [submit a Change Request here](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/code-development-efficiency/change-requests-duration.md)<br>
To reference this metric in software or publications please use this stable URL: <https://chaoss.community/?p=3587>

<!-- # For groupings in the knowledge base
Context tags: Lifecycle, Contribution, Platform
Keyword tags: change request, accepted changes, review duration,  merged, code base, 
-->
