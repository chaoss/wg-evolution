# Code_Changes_Lines

All lines touched (added / removed)
in all changes to the source code during a certain period.

## Description

When introducing changes to the source code, developers touch
(edit, add, remove) lines of the source code files.
This metric considers the aggregated number of lines touched
by changes to the source code performed during a certain period.
This means that if a certain line in a certain file is touched
in three different changes, it will count as three lines.
Since in most source code management systems it is difficult
or impossible to tell accurately if a lines was removed and then
added, or just edited, we will consider editing a line as removing it
and later adding it back with a new content. Each of those
(removing and adding) will be considered as "touching".
Therefore, if a certain line in a certain file is edited three times,
it will count as six different changes (three removals,
and three additions).

For this matter, we consider changes to the source code as
defined in [Code_Changes](Code_Changes.md). Lines of code will
be any line of a source code file, including comments and blank lines.

### Parameters

Mandatory:

* Period of time. Start and finish date of the period. Default: forever.

    Period during which changes are considered.

* Criteria for source code. Algorithm. Default: all files are source code.

    If we are focused on source code, we need a criteria for deciding
    whether a file is a part of the source code or not.

### Aggregators

Usual aggregators are:

* Count. Total number of lines changes (touched) during the period.

## Specific description: git

In the cases of git, we define "code change" and "date of a change"
as we detail in [Code_Changes](Code_Changes.md).
The date of a change can be defined (for considering it in a period or not)
as the author date or the commiter date of the corresponding git commit.

Since git provides changes as diff patches (list of lines added and removed),
each of those lines mentioned as a lines added or a line removed in the diff
will be considered as a lines changed (touched).
If a line is removed and added, it will be considered as to "changes to a line".

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


## Use Cases

* Volume of coding activity:

  Although code changes can be a proxy to the coding activity of a project,
  not all changes are the same. Considering the aggregated number of
  lines touched in all changes gives a complementary idea of how large
  the changes are, and in general, how large is the volume of coding
  activity.

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

[ Work in progress ]

## Known Implementations

* [Grimoirelab](https://chaoss.github.io/grimoirelab) provides this metric out of the box.
  - View an example on the [CHAOSS instance of Bitergia Analytics](https://chaoss.biterg.io/app/kibana#/dashboard/f13af0e0-18e5-11e9-ba47-d5cbef43f8d3).  
  - Download and import a ready-to-go dashboard containing examples for this metric visualization from the [GrimoireLab Sigils panel collection](https://chaoss.github.io/grimoirelab-sigils/chaoss-gmd-cde/lines_of_code_changed/).
  - Add a sample visualization to any GrimoreLab Kibiter dashboard following these instructions:
    * Create a new `Area` chart
    * Select the `git` index
    * Y-axis 1: `Sum` Aggregation, `lines_added` Field, `Lines Added` Custom Label
    * Y-axis 2: `Sum` Aggregation, `painless_inverted_lines_removed_git` Field, `Lines Removed` Custom Label
    * X-axis: `Date Histogram` Aggregation, `grimoire_creation_date` Field, `Auto` Interval, `Time` Custom Label
  - Example screenshot: ![GrimoireLab screenshot of metric Code_Changes_Lines](./images/code_changes_lines-GrimoireLab.png)


## External References (Literature)
