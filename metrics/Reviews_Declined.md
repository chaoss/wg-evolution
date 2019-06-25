# Reviews_Declined

Reviews for changes to the source code that ended declining the change
during a certain period.

## Description

Reviews are defined as in [Reviews](https://github.com/chaoss/wg-evolution/blob/master/metrics/Reviews.md).
Declined reviews are those that are finally closed without
being merged into the code base of the project.

For example, in GitHub when a pull request is closed without
merging, and the commits referenced in it cannot be found
in the git repository, it can be considered to be declined
(but see detailed discussion below). The same can be said of
GitLab merge requests. In the case of Gerrit, code reviews
can be formally "abandoned", which is the way of detecting
declined reviews in this system.

### Parameters

Mandatory:

* Period of time. Start and finish date of the period. Default: forever.

    Period during which declined reviews are considered.

* Criteria for source code. Algorithm. Default: all files are source code.

    If we are focused on source code, we need a criteria for deciding
    whether a file is a part of the source code or not.

### Aggregators

Usual aggregators are:

* Count. Total number of declined reviews during the period.

## Specific description: GitHub

In the case of GitHub, accepted reviews are defined as "pull requests
that are closed with their changes not being included in the git repository",
as long as it proposes changes to source code files.

See the discussion in the specific description for GitHub in
[Reviews_Accepted](https://github.com/chaoss/wg-evolution/blob/master/metrics/Reviews_Accepted.md), since it applies here as well.

### GitHub parameters

Mandatory:

* Heuristic for detecting declined pull requests, telling apart
  those cases where the pull request was closed, but the
  changes were included in the git repository manually.
  Default: None.

## Specific description: GitLab

In the case of GitLab, accepted reviews are defined as "merge requests
that are closed with their changes not being included in the git repository",
as long as it proposes changes to source code files.

[ Details to be done ]

### GitLab parameters

Mandatory:

* Heuristic for detecting declined merge requests, telling apart
  those cases where the merge request was closed, but the
  changes were included in the git repository manually.
  Default: None.

## Specific description: Gerrit

In the case of Gerrit, declined reviews are defined as "changesets
abandoned", as long as they propose changes to source code files.

[ Details to be done ]


### Gerrit parameters

None.


## Use Cases

* Volume of coding activity.

    Declined code reviews are a proxy for the activity in a project.
    By counting declined code reviews in the set of repositories corresponding
    to a project, you can have an idea of the overall coding activity in
    that project that did not lead to actual changes.
    Of course, this metric is not the only one that should be
    used to track volume of coding activity.

## Filters

Usual filters and bucketing are:

* By actors (submitter, reviewer, merger). Requires actor merging
(merging ids corresponding to the same author).

* By groups of actors (employer, gender... for each of the actors).
Requires actor grouping, and likely, actor merging.

## Visualizations

Some useful visualizations are:

* Count per month over time
* Count per group over time

These could be represented as bar charts, with time running in the X axis.
Each bar would represent declined reviews during a certain period
(eg, a month).

## Reference Implementation

[ To be done. ]

## Known Implementations


## External References (Literature)
