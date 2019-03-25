# Code_Changes

Changes to the source code during a certain period.

## Description

These are changes to the source code during a certain period.
For "change" we consider what developers consider an atomic change to their code.
In other words, a change is some change to the source code which usually
is accepted and merged as a whole, and if needed, reverted as a whole too.
For example, in the case of git, each "change" corresponds to a "commit",
or, to be more precise, "code change" corresponds to the part of a commit which
touches files considered as source code.

### Parameters

Mandatory:

* Period of time. Start and finish date of the period. Default: forever.

    Period during which changes are considered.
    
* Criteria for source code. Algorithm. Default: all files are source code.

    If we are focused on source code, we need a criteria for deciding
    whether a file is a part of the source code or not.
    
### Aggregators

Usual aggregators are:

* Count. Total number of changes during the period.

## Specific description: git

In the cases of git, a code change is defined as the part of
a git commit that "touches" a source file.
That is, for each git commit, only the part related to
deletions or additions of lines to files that are considered source code
will be considered as the code change.

The date of a change can be defined (for considering it in a period or not)
as the author date or the commiter date of the corresponding git commit.

In a set of repositories, the same commit may be present in more than one
of them. Therefore, for counting unique changes,
repeated commits should be counted only once.

### Git parameters

Mandatory:

* Kind of date. Either author date or committer date. Default: author date.

    For each git commit, two dates are kept: when the commit was authored,
    and when it was committed to the repository.
    For deciding on the period, one of them has to be selected.

* Include merge commits. Boolean. Default: True.

    Merge commits are
    those which merge a branch, and in some cases are not considered as
    reflecting a coding activity

* Include empty commits. Boolean. Default: True.

    Empty commits are
    those which do not touch files, and in some cases are not considered as
    reflecting a coding activity.

## Use Cases

* Volume of coding activity.

    Code changes are a proxy for the activity in a project.
    By counting the code changes in the set of repositories corresponding
    to a project, you can have an idea of the overall coding activity in
    that project.
    Of course, this metric is not the only one that should be
    used to track volume of coding activity.

## Filters

Usual filters and bucketing are:

* By actors (author, committer). Requires actor merging
(merging ids corresponding to the same author).

* By groups of actors (employer, gender...). Requires actor grouping,
and likely, actor merging.

## Visualizations

Some useful visualizations are:

* Count per month over time
* Count per group over time

These could be represented as bar charts, with time running in the X axis.
Each bar would represent a code changes during a certain period (eg, a month).

## Reference Implementation

See [reference implementation for git](../implementations/Code_Changes-Git.ipynb)
([see it in Binder](https://mybinder.org/v2/gh/chaoss/wg-gmd/master?filepath=implementations/Code_Changes-Git.ipynb)).

## Known Implementations

* [Grimoirelab](https://chaoss.github.io/grimoirelab). Enriched index for git repositories is composed of
one item per commit, which makes it basically correspond to this metric
when counted. The Git panel, available out of the box, provides exactly that.

* [Augur](https://chaoss.github.io/augur/). Provides this metric out of the box.

* [Gitdm](https://repo.or.cz/w/git-dm.git). Provides this metric out of the box.

## External References (Literature)
