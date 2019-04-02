# Issues Active

Issues related to the source code that showed some activity
during a certain period.

## Description

Issues are defined as in [Issues](Issues.md).
Issues showing some activity are those that had some comment,
or some change in state (including closing the issue),
during a certain period.

For example, in GitHub Issues, a comment, a new tag, or
the action of closing an issue, is considered as a sign of activity.

### Parameters

Mandatory:

* Period of time. Start and finish date of the period. Default: forever.

    Period during which issues are considered.
    
* Criteria for source code. Algorithm. Default: all issues are related to
  source code.

    If we are focused on source code, we need a criteria for deciding
    whether an issues is related to the source code or not.
    
### Aggregators

Usual aggregators are:

* Count. Total number of active issues during the period.

## Specific description: GitHub

In the case of GitHub, active issues are defined as "issues
which get a comment, a change in tags, a change in assigned
person, or are closed",
as long as they are related to source code files.

### GitHub parameters

None.

## Specific description: GitLab

In the case of GitLab, active issues are defined as "issues
which get a comment, a change in tags, a change in assigned
person, or are closed",
as long as they are related to source code files.

### GitLab parameters

None.

## Specific description: Jira

In the case of Jira, active issues are defined as "issues
which get a comment, a change in state, a change in assigned
person, or are closed",
as long as they are related to source code files.

### Jira parameters

None.

## Specific description: Bugzilla

In the case of Bugzilla, active issues are defined as "bug reports
which get a comment, a change in state, a change in assigned
person, or are closed",
as long as they are related to source code files.

### Bugzilla parameters

None.

## Use Cases

* Volume of active issues in a project.

    Active issues are a proxy for the activity in a project.
    By counting active issues related to code in the set of repositories corresponding
    to a project, you can have an idea of the overall activity in
    working with issues in that project.
    Of course, this metric is not the only one that should be
    used to track volume of coding activity.


## Filters

Usual filters and bucketing are:

* By actors (submitter, commenter, closer). Requires actor merging
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

[ To be done. ]

## External References (Literature)
