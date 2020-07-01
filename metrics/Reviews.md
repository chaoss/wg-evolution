# Reviews

Question: What new review requests for changes to the source code occurred during a certain period?

_This metric is a release candidate. The 30 day comment period for this metric begins on 07/01/2020 and ends on 07/31/2020. To comment on this metric please see [Issue #337](https://github.com/chaoss/wg-evolution/issues/337). Following the comment period, this metric will be included in the release._


## Description
When a project uses code review processes, changes are not directly
submitted to the code base, but are first proposed for discussion
as "proposals for change to the source code".
Each of these proposals are intended to be reviewed by other developers,
who may suggest improvements that will lead to the original proposers
sending new versions of their proposals, until reviews are
positive, and the code is accepted, or until it is decided that
the proposal is declined.

For example, "reviews" correspond to "pull requests" in the case of GitHub,
to "merge requests" in the case of GitLab, and to "code reviews"
or in some contexts "changesets" in the case of Gerrit.


## Objectives
* Volume of changes proposed to a project.
    Reviews are a proxy for the activity in a project.
    By counting reviews to code changes in the set of repositories corresponding
    to a project, you can have an idea of the overall activity in
    reviewing changes to that project.
    Of course, this metric is not the only one that should be
    used to track volume of coding activity.


## Implementation

**Aggregators:**
* Count. Total number of reviews during the period.

**Parameters:**

* Period of time. Start and finish date of the period. Default: forever.  
    Period during which reviews are considered.

* Criteria for source code. Algorithm. Default: all files are source code.  
    If we are focused on source code, we need a criteria for deciding
    whether a file is a part of the source code or not.


### Filters

* By actors (submitter, reviewer, merger). Requires actor merging
(merging ids corresponding to the same author).
* By groups of actors (employer, gender... for each of the actors).
Requires actor grouping, and likely, actor merging.
* Status (open, closed)


### Visualizations

* Count per month over time
* Count per group over time

These could be represented as bar charts, with time running in the X axis.
Each bar would represent reviews to change the code
during a certain period (eg, a month).



### Tools Providing the Metric

* [Grimoirelab](https://chaoss.github.io/grimoirelab) provides this metric out of the box for GitHub Pull Requests, GitLab Merge Requests and Gerrit Changesets.  
  - View an example on the [CHAOSS instance of Bitergia Analytics](https://chaoss.biterg.io/app/kibana#/dashboard/GitHub-Pull-Requests).  
  - Download and import a ready-to-go dashboard containing examples for this metric visualization based on GitHub Pull Requests data from the [GrimoireLab Sigils panel collection](https://chaoss.github.io/grimoirelab-sigils/panels/github-pullrequests/).
  - Add a sample visualization for GitHub Pull requests to any GrimoreLab Kibiter dashboard following these instructions:
    * Create a new `Vertical Bar` chart.
    * Select the `github_issues` index.
    * Filter: `pull_request` is `true`.
    * Metrics Y-axis: `Count` Aggregation, `# Pull Requests` Custom Label.
    * X-axis: `Date Histogram` Aggregation, `grimoire_creation_date` Field, `Auto` Interval, `Time` Custom Label.
    * Buckets Split Series: `Terms` Sub Aggregation, `state` Field, `metric: # Pull Requests` Order By, `Descending` Order, `1000` Size, `State` Custom Label. Notice this visualization is based on Pull Requests creation date, so items are counted at the date they were created and its state, as set here, would be their current state at the moment of visualizing the data, e.g. `n` Pull Requests created at a give time range are currently `open` or `closed`.
  - Example screenshot: ![GrimoireLab screenshot of metric Reviews](https://github.com/chaoss/wg-evolution/blob/master/metrics/images/reviews-GrimoireLab.png)


### Data Collection Strategies

**Specific description: GitHub**

In the case of GitHub, a review is defined as a "pull request",
as long as it proposes changes to source code files.

The date of the review can be defined (for considering it in a period or not)
as the date in which the pull request was submitted.

**Specific description: GitLab**

In the case of GitLab, a review is defined as a "merge request",
as long as it proposes changes to source code files.

The date of the review can be defined (for considering it in a period or not)
as the date in which the merge request was submitted.

**Specific description: Gerrit**

In the case of Gerrit, a review is defined as a "code review",
or in some contexts, a "changeset",
as long as it proposes changes to source code files.

The date of the review can be defined (for considering it in a period or not)
as the date in which the code review was started by submitting a
patchset for review.

## References
