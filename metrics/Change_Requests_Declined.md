# Change Requests Declined

Question: What change requestsended up being declined during a certain period?

### This metric is a release candidate. To comment on this metric please see [Issue #384](https://github.com/chaoss/wg-evolution/issues/384/). Following a comment period, this metric will be included in the next regular release.  

## Description

Change requests are defined as in [Change Requests](https://github.com/chaoss/wg-evolution/blob/master/metrics/Change_Requests.md).
Declined change requests are those that are finally closed without
being merged into the code base of the project.

For example, in GitHub when a pull request is closed without
merging, and the commits referenced in it cannot be found
in the git repository, it can be considered to be declined
(but see detailed discussion below). The same can be said of
GitLab merge requests. In the case of Gerrit, code reviews
can be formally "abandoned", which is the way of detecting
declined change requests in this system.


## Objectives

* Volume of coding activity.
    Declined change requests are a proxy for the activity in a project.
    By counting declined change requests in the set of repositories corresponding
    to a project, you can have an idea of the overall coding activity in
    that project that did not lead to actual changes.
    Of course, this metric is not the only one that should be
    used to track volume of coding activity.

## Implementation

**Aggregators**:
* Count. Total number of declined change requests during the period.
* Ratio. Ratio of declined change requests over the total number of change requests during that period.

**Parameters:**
* Period of time. Start and finish date of the period during which declined change requests are considered. Default: forever.
* Criteria for source code. Algorithm. Default: all files are source code.
    If we focus on source code, we need a criterion to decide
    whether a file belongs to the source code or not.


### Filters

* By actors (submitter, reviewer, merger). Requires merging identities corresponding to the same actor.
* By groups of actors (employer, gender... for each of the actors). Requires actor grouping, and likely, actor merging.


### Visualizations

* Count per period over time
* Ratio per period over time

These could be grouped (per actor type, or per group of actors) by applying the filters,
and could be represented as bar charts, with time running in the X axis.
Each bar would represent declined change requests during a certain period (e.g., a month).


### Data Collection Strategies

**Specific description: GitHub**

In the case of GitHub, declined change requests are defined as "pull requests
that are closed with their changes not being included in the git repository",
as long as it proposes changes to source code files.

See the discussion in the specific description for GitHub in
[Change Requests Accepted](https://github.com/chaoss/wg-evolution/blob/master/metrics/Change_Requests_Accepted.md), since it applies here as well.

Mandatory parameters (for GitHub):

* Heuristic for detecting declined change requests, telling apart
  those cases where the change request was closed, but the
  changes were included in the git repository manually.
  Default: None.

**Specific description: GitLab**

In the case of GitLab, declined reviews are defined as "merge requests
that are closed with their changes not being included in the git repository",
as long as it proposes changes to source code files.

Mandatory parameters (for GitLab):

* Heuristic for detecting declined change requests, telling apart
  those cases where the merge request was closed, but the
  changes were included in the git repository manually. Default: None.

**Specific description: Gerrit**

In the case of Gerrit, declined change requests are defined as "changesets
abandoned", as long as they propose changes to source code files.

Mandatory parameters (for Gerrit): None.

## References
