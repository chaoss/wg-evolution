# Issue Resolution Duration

**Question: How long does it take for an issue to be closed?**

## Overview

Issue Resolution Duration measures  how long an issue remains open, on average, before it is closed. Data points are calculated by averaging the time elapsed between the initial opening date of each issue and its closure date. Prolonged resolution times can indicate difficluties during the development process, resource constraints, or communication challenges. This metric can also be used to evaluate the effort and time needed to conclude and resolve discussions. A project with a history of slow issue resolution may create a negative perception among contributors, potentially discouraging participation from diverse groups. With commitment to timely issue resolution, project maintainers can create a more inclusive environment for all contributors.

## Want to Know More?

<span markdown="1"><details>

<summary>Click to read more about this metric.</summary>

### Filters

*   By time. Provides average issue resolution duration time starting from the provided beginning date to the provided end date.
    *   By open time. Provides information for how long issues created from the provided beginning date to the provided end date took to be resolved.(The issue may be resolved in time later than the specified time period)
    *   By closed time. Provides information for how long old issues were that were closed from the provided beginning date to the provided end date took to be resolved.(The issue may be created in time earlier than the specified time period)

*   By actors (submitter, commenter, closer). Requires actor merging (merging ids corresponding to the same author).

*   By groups of actors (employer, gender... for each of the actors). Requires actor grouping, and likely, actor merging.

### Visualizations

*   Average over time (e.g. average for January, average for February, average for March, etc.)
*   Average for a given time period (e.g. average for all of 2019, or average for January to March)
    For each closed issue:
*   Issue Resolution Duration = Timestamp of issue closed - Timestamp of issue opened
*   Average amount of time (in days, by default) for an issue in the repository to be closed.
*   Period of time: Start and finish date of the period. Default: forever.

</details></span>

## References

*   http://augur.osshealth.io/api\_docs/#api-Evolution-Closed\_Issue\_Resolution\_Duration\_Repo\_

## Contributors

*   Sean P. Goggins
*   Vinod K. Ahuja
*   Kevin Lumbard
*   Yehui Wang
*   Peculiar C Umeh

## Additional Information

To edit this metric please [submit a Change Request here](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/issue-resolution/issue-resolution-duration.md)

To reference this metric in software or publications please use this stable URL: <https://chaoss.community/?p=3630>

<!-- # For groupings in the knowledge base
Context tags: Lifecycle, Platform, Contribution
Keyword tags: bug report, problems, issues, duration, time
→ 
