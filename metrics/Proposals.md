# Proposals

New proposals for changes to the source code, during a certain period.

## Description

When a project uses code review processes, changes are not directly
submitted to the code base, but are first proposed for discussion
as "proposals for change to the source code".
Each of these proposals are intended to be reviewed by other developers,
who may suggest improvements that will lead to the original proposers
sending new versions of their proposals, until reviews are
positive, and the code is accepted, or until it is decided that
the proposal is declined.

For example, "proposals" correspond to "pull requests" in the case of GitHub,
to "merge requests" in the case of GitLab, and to "code reviews"
or in some contexts "changesets" in the case of Gerrit.

### Parameters

Mandatory:

* Period of time. Start and finish date of the period. Default: forever.

    Period during which proposals are considered.
    
* Criteria for source code. Algorithm. Default: all files are source code.

    If we are focused on source code, we need a criteria for deciding
    whether a file is a part of the source code or not.
    
### Aggregators

Usual aggregators are:

* Count. Total number of proposals during the period.

## Specific description: GitHub

In the case of GitHub, a proposal is defined as a "pull request",
as long as it proposes changes to source code files.

The date of the proposal can be defined (for considering it in a period or not)
as the date in which the pull request was submitted.

### GitHub parameters

None.

## Specific description: GitLab

In the case of GitLab, a proposal is defined as a "merge request",
as long as it proposes changes to source code files.

The date of the proposal can be defined (for considering it in a period or not)
as the date in which the merge request was submitted.

### GitLab parameters

None.

## Specific description: Gerrit

In the case of Gerrit, a proposal is defined as a "code review",
or in some contexts, a "changeset",
as long as it proposes changes to source code files.

The date of the proposal can be defined (for considering it in a period or not)
as the date in which the code review was started by submitting a
patchset for review.

### Gerrit parameters

None.


## Use Cases

* Volume of changes proposed to a project.

    Proposals are a proxy for the activity in a project.
    By counting proposals to change code in the set of repositories corresponding
    to a project, you can have an idea of the overall activity in
    proposing changes to that project.
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
Each bar would represent proposals to change the code
during a certain period (eg, a month).

## Reference Implementation

[ To be done. ]

## Known Implementations

* [Grimoirelab](https://chaoss.github.io/grimoirelab). Enriched index for
GitHub Pull Requests, GitLab Merge Requests,
and Gerrit repositories is composed of one item per proposal,
which makes it basically correspond to this metric when counted.
The GitHub Pull Requests, GitLab Merge Requests, and Gerrit summary panels,
available out of the box, provide exactly that.

## External References (Literature)
