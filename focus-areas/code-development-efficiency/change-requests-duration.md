# Change Requests Duration

Question: What is the duration of time between the moment a change request starts and the moment it is accepted or closed?

## Description

Change requests are defined as in [Change Requests](https://chaoss.community/metric-change-requests/). Accepted change requests are defined in [Change Requests Accepted](https://chaoss.community/metric-change-requests-accepted/).

The change request duration is the duration of the period since the change request started, to the moment it ended (by being accepted and being merged in the code base). This only applies to accepted change requests. For example, in GitLab a change request starts when a developer uploads a proposal for a change in code, opening a change request. It finishes when the change request is finally accepted and merged in the code base, closing the change request.

In case there are comments or other events after the code is merged, they are not considered for measuring the duration of the change request.

## Objectives
Review duration for accepted change requests is one of the indicators showing how long does a project take before accepting a contribution of code. Of course, this metric is not the only one that should be used to track volume of coding activity.

## Implementation

Potential aggregators include: 
* Median. Median (50% percentile) of change request duration for all accepted change requests in the considered period of time.

Potential parameters include:
* Period of time. Start and finish date of the period. Default: forever. Period during which accepted change requests are considered. An accepted change request is considered to be in the period if its creation event is in the period.
* Criteria for source code. Algorithm. Default: all files are source code. If we are focused on source code, we need a criteria for deciding whether a file is a part of the source code or not.

### Filters

* By actors (submitter, reviewer, merger). Requires actor merging (merging ids corresponding to the same author).
* By groups of actors (employer, gender... for each of the actors). Requires actor grouping, and likely, actor merging.
* Median per month over time
* Median per group over time
* Distribution of durations for a certain period

### Data Collection Strategies

**Specific description: GitHub**

In the case of GitHub, duration is considered for pull requests that are accepted and merged in the code base. For an individual pull request, duration starts when it is opened, and finishes when the commits it includes are merged into the code base.

Mandatory parameters (for GitHub): None.

**Specific description: GitLab**

In the case of GitLab, duration is considered for merge requests that are accepted and merged in the code base. For an individual merge request, duration starts when it is opened, and finishes when the commits it includes are merged into the code base.

Mandatory parameters (for GitLab): None.

**Specific description: Gerrit**

In the case of Gerrit, duration is considered for code reviews that are accepted and merged in the code base. For an individual code review, duration starts when it is opened, and finishes when the commits it includes are merged into the code base.

Mandatory parameters (for Gerrit): None.
