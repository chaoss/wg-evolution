# Code Changes

Question: How many changes were made to the source code during a specified period? 


## Description

These are changes to the source code during a certain period.
For "change" we consider what developers consider an atomic change to their code.
In other words, a change is some change to the source code which usually
is accepted and merged as a whole, and if needed, reverted as a whole too.
For example, in the case of git, each "change" corresponds to a "commit",
or, to be more precise, "code change" corresponds to the part of a commit which
touches files considered as source code.


## Objectives

* Volume of coding activity.
    Code changes are a proxy for the activity in a project.
    By counting the code changes in the set of repositories corresponding
    to a project, you can have an idea of the overall coding activity in
    that project.
    Of course, this metric is not the only one that should be
    used to track volume of coding activity.


## Implementation

**Aggregators:**
* Count. Total number of changes during the period.

**Parameters:**
* Period of time. Start and finish date of the period. Default: forever.
 Period during which changes are considered.
* Criteria for source code. Algorithm. Default: all files are source code.
 If focused on source code, criteria for deciding whether a file is a part of the source code or not.


### Filters

* By actors (author, committer). Requires actor merging
(merging ids corresponding to the same author).

* By groups of actors (employer, gender...). Requires actor grouping,
and likely, actor merging.

* By [tags](https://www.odoo.com/documentation/13.0/reference/guidelines.html#tag-and-module-name) (used in the message of the commits).
Requires a structure for the message of commits.
This tag can be used in an open-source project to communicate to every contributors
if the commit is, for example, a fix for a bug or an improvement of a feature.

### Visualizations

* Count per month over time
* Count per group over time

These could be represented as bar charts, with time running in the X axis.
Each bar would represent a code changes during a certain period (eg, a month).


### Tools Providing the Metric

* [GrimoireLab](https://chaoss.github.io/grimoirelab) provides this metric out of the box.
  - View an example on the [CHAOSS instance of Bitergia Analytics](https://chaoss.biterg.io/app/kibana#/dashboard/Git).  
  - Download and import a ready-to-go dashboard containing examples for this metric visualization from the [GrimoireLab Sigils panel collection](https://chaoss.github.io/grimoirelab-sigils/panels/git/).
  - Add a sample visualization to any GrimoreLab Kibiter dashboard following these instructions:
    * Create a new `Vertical Bar` chart
    * Select the `git` index
    * Y-axis: `Unique Count` Aggregation, `hash` Field, `# Commits` Custom Label
    * X-axis: `Date Histogram` Aggregation, `grimoire_creation_date` Field, `Auto` Interval, `Time` Custom Label
  - Example screenshot:
  
    ![GrimoireLab screenshot of metric Code_Changes](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/code-development-activity/images/code-changes_grimoirelab.png)

* [Augur](http://augur.osshealth.io/) provides this metric both as [Code Changes](http://augur.osshealth.io/api_docs/#api-Evolution-code_changes_repo/) and as [Code Changes Lines](http://augur.osshealth.io/api_docs/#api-Evolution-code_changes_lines_repo). Both metrics are available in both the `repo` and the `repo_group` metric forms - more on that in the [Augur documentation](https://oss-augur.readthedocs.io/en/master/getting-started/create-a-metric/overview.html#metric-forms).

* [Gitdm](https://repo.or.cz/w/git-dm.git)


### Data Collection Strategies

**Specific description: Git**

See [reference implementation for git](https://github.com/chaoss/wg-evolution/blob/master/implementations/notebooks_df/code_changes_git.ipynb)

Mandatory parameters (for Git):

* Date type. Either author date or committer date. Default: author date.  
    For each git commit, two dates are kept: when the commit was authored, and when it was committed to the repository. For deciding on the period, one of them has to be selected.

* Include merge commits. Boolean. Default: True.  
    Merge commits are those which merge a branch, and in some cases are not considered as reflecting a coding activity.

* Include empty commits. Boolean. Default: True.  
    Empty commits are those which do not touch files, and in some cases are not considered as reflecting a coding activity.

## References

* https://www.odoo.com/documentation/13.0/reference/guidelines.html#tag-and-module-name
