# Proposals_Accepted

Proposals for changes to the source code that were accepted
during a certain period.

## Description

Proposals are defined as in [Proposals](Proposals.md).
Accepted proposals are those that are finally merged into the code
base of the project.
Accepted proposals can be linked to one or more changes to the source
code, those corresponding to the changes proposed and finally merged.

For example, in GitHub when a pull request is accepted, all the 
commits included in it are merged (maybe squashed, maybe rebased)
in the correspnding git repository. The same can be said of
GitLab merge requests. In the case of Gerrit, a code review usually
corresponds to a single commit. 

### Parameters

Mandatory:

* Period of time. Start and finish date of the period. Default: forever.

    Period during which accepted proposals are considered.
    
* Criteria for source code. Algorithm. Default: all files are source code.

    If we are focused on source code, we need a criteria for deciding
    whether a file is a part of the source code or not.
    
### Aggregators

Usual aggregators are:

* Count. Total number of accepted proposals during the period.

## Specific description: GitHub

In the case of GitHub, accepted proposals are defined as "pull requests
whose changes are included in the git repository",
as long as it proposes changes to source code files.

Unfortunately, there are several ways of accepting proposals, not
all of them making it easy to identify that they were accepted.
The easiest situation is when the pull request is accepted and
merged (or rebased, or squashed and merged). In that case,
the pull request can easily be identified as accepted, and
the corresponding commits can be found via queries to the GitHub API.

But reviews can also be closed, and commits merged manually in the
git repository. In this case, commits may still be found in the
git repository, since their hash is the same found in the GitHub API
for those in the pull request.

In a more difficult scenario, reviews can also be closed, and commits
rebased, or maybe squashed and then merged, manually. In these cases,
hashes are different, and only an approximate matching via dates and
authors, and/or comparison of diffs, can be used to track commits in
the git repository.

From the point of view of knowing if they were accepted, the
problem is that if they are included in the git repository manually,
the only way of knowing that the pull request was accepted is
finding the corresponding commits in the git repositoriy.

In some cases, projects have policies of mentioning the commits
when the pull request is closed (such as "closing by accepting commits
xxx and yyyy"), which may help to track commits in the git repository.

### GitHub parameters

Mandatory:

* Heuristic for detecting accepted pull requests not accepted
  via the web interface.
  Default: None.

## Specific description: GitLab

In the case of GitLab, accepted proposals are defined as "merge requests
whose changes are included in the git repository",
as long as it proposes changes to source code files.

[ Details to be done ]

### GitLab parameters

Mandatory:

* Heuristic for detecting accepted pull requests not accepted
  via the web interface.
  Default: None.

## Specific description: Gerrit

In the case of Gerrit, accepted proposals are defined as "changesets
whose changes are included in the git repository",
as long as they proposes changes to source code files.

[ Details to be done ]



### Gerrit parameters

None.



## Use Cases

* Volume of coding activity.

    Accepted code proposals are a proxy for the activity in a project.
    By counting accepted code proposals in the set of repositories corresponding
    to a project, you can have an idea of the overall coding activity in
    that project that leads to actual changes.
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
Each bar would represent accepted proposals to change the code
during a certain period (eg, a month).

## Reference Implementation

[ To be done. ]

## Known Implementations


## External References (Literature)
