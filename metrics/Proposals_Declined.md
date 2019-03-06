# Proposals_Declined

Proposals for changes to the source code that were declined
during a certain period.

## Description

Proposals are defined as in [Proposals](Proposals.md).
Declined proposals are those that are finally closed without
being merged into the code base of the project.

For example, in GitHub when a pull request is closed without
merging, and the commits referenced in it cannot be found
in the git repository, it can be considered to be declined
(but see detailed discussion below). The same can be said of
HitLab merge requests. In the case of Gerrit, code reviews
can be formally "abandoned", which is the way of detecting
declined proposals in this system. 

### Parameters

Mandatory:

* Period of time. Start and finish date of the period. Default: forever.

    Period during which declined proposals are considered.
    
* Criteria for source code. Algorithm. Default: all files are source code.

    If we are focused on source code, we need a criteria for deciding
    whether a file is a part of the source code or not.
    
### Aggregators

Usual aggregators are:

* Count. Total number of declined proposals during the period.

## Specific description: GitHub

In the case of GitHub, accepted proposals are defined as "pull requests
that are closed with their changes not being included in the git repository",
as long as it proposes changes to source code files.

See the discussion in the specific description for GitHub in
[Proposals_Accepted](Proposals_Accepted.md), since it applies here
as well.

### GitHub parameters

Mandatory:

* Heuristic for detecting declined pull requests, telling appart
  those cases where the pull request was closed, but the
  changes were included in the git repository manually.
  Default: None.

## Specific description: GitLab

In the case of GitLab, accepted proposals are defined as "merge requests
that are closed with their changes not being included in the git repository",
as long as it proposes changes to source code files.

[ Details to be done ]

### GitLab parameters

Mandatory:

* Heuristic for detecting declined merge requests, telling appart
  those cases where the merge request was closed, but the
  changes were included in the git repository manually.
  Default: None.

## Specific description: Gerrit

In the case of Gerrit, declined proposals are defined as "changesets
absndoned", as long as they propose changes to source code files.

[ Details to be done ]


### Gerrit parameters

None.


## Use Cases

* Volume of coding activity.

    Declined code proposals are a proxy for the activity in a project.
    By counting declined code proposals in the set of repositories corresponding
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
Each bar would represent declined proposals during a certain period
(eg, a month).

## Reference Implementation

[ To be done. ]

## Known Implementations


## External References (Literature)
