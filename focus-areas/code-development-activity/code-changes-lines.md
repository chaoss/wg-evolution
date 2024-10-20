# Code Changes Lines

**Question: What is the sum of the number of lines touched (lines added plus lines removed) in all changes to the source code during a certain period?**

## Overview

Code Changes Lines  measures the aggregated number of lines touched by changes to the source code performed during a certain period. This means that if a certain line in a certain file is touched in three different changes, it will count as three lines. Data points consist of the cumulative count of lines touched across all code changes during the measurement period which includes all developers touch (edit, add, remove). Increased code changes indicate significant development activity, while a decrease may suggest periods of maintenance or reduced development.
In most source code management systems it is difficult or impossible to tell accurately if a line was removed and then added, or just edited, in such case editing a line wil be consider as removing it and later adding it back with a new content. Therefore, if a certain line in a certain file is edited three times, it will count as six different changes (three removals, and three additions).
For this matter, changes to the source code is considered as defined in [Code Changes Commits](https://chaoss.community/metric-code-changes-commits/) and lines of code will be any line of a source code file, including comments and blank lines.

## Want to Know More?

<span markdown="1"><details>

<summary>Click to read more about this metric.</summary>

### Data Collection Strategies

**Specific description: Git**

In the cases of git, we define "code change" and "date of a change" as we detail in [Code Changes Commits](https://chaoss.community/metric-code-changes-commits/). The date of a change can be defined (for considering it in a period or not) as the author date or the committer date of the corresponding git commit.

Since git provides changes as diff patches (list of lines added and removed), each of those lines mentioned as a line added or a line removed in the diff will be considered as a line changed (touched). If a line is removed and added, it will be considered as two "changes to a line".

**Mandatory parameters:**

*   Kind of date. Either author date or committer date. Default: author date.\
    For each git commit, two dates are kept: when the commit was authored, and when it was committed to the repository. For deciding on the period, one of them has to be selected.<br>

*   Include merge commits. Boolean. Default: True.\
    Merge commits are those which merge a branch, and in some cases are not considered as reflecting a coding activity

Potential aggregators for the Code Changes Lines metric include:

*   Count. Total number of lines changes (touched) during the period.

Potential parameters for the Code Changes Lines metric include:

*   Period of time: Start and finish date of the period. Default: forever. Period during which changes are considered.
*   Criteria for source code; Algorithm Default: All files are source code. If we are focused on source code, we need a criterion for deciding whether a file is a part of the source code or not.
*   Type of source code change:
    *   Lines added
    *   Lines removed
    *   Whitespace

### Filters

*   By actors (author, committer). Requires actor merging (merging ids corresponding to the same author).
*   By groups of actors (employer, gender...). Requires actor grouping, and likely, actor merging.
*   By [tags](https://www.odoo.com/documentation/13.0/reference/guidelines.html#tag-and-module-name) (used in the message of the commits). Requires a structure for the message of commits. This tag can be used in an open-source project to communicate to every contributors if the commit is, for example, a fix for a bug or an improvement of a feature.
*   Count per month over time
*   Count per group over time

### Visualizations

*   [GrimoireLab](https://chaoss.github.io/grimoirelab)
    ![GrimoireLab screenshot of metric Code\_Changes\_Lines](https://raw.githubusercontent.com/chaoss/wg-evolution/main/focus-areas/code-development-activity/images/code-changes-lines_grimoirelab.png)

</details></span>

## References

*   [Coding Guidelines](https://www.odoo.com/documentation/13.0/reference/guidelines.html#tag-and-module-name)
*   [CHAOSS instance of Bitergia Analytics](https://chaoss.biterg.io/app/kibana#/dashboard/f13af0e0-18e5-11e9-ba47-d5cbef43f8d3).
*   [GrimoireLab Sigils panel collection](https://chaoss.github.io/grimoirelab-sigils/chaoss-gmd-cde/lines_of_code_changed/).

## Contributors

*   Matt Germonprez
*   Kevin Lumbard
*   Elizabeth Barron
*   Pecular C. Umeh

## Additional Information

To edit this metric please [submit a Change Request here](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/code-development-activity/code-changes-lines.md)

To reference this metric in software or publications please use this stable URL: <https://chaoss.community/?p=3591>

<!-- # For groupings in the knowledge base
Context tags: Contribution, Software, Lifecycle
Keyword tags: lines added, lines deleted, code changes, source code changes, coding activity, source code, merge commits, pull request changes
-→ 
