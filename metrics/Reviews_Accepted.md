# Reviews Accepted

Question: How many accepted reviews are present in a code change?

## Description

Reviews are defined as in [Reviews](https://github.com/chaoss/wg-evolution/blob/master/metrics/Reviews.md).
Accepted reviews are those that end with the corresponding changes
finally merged into the code base of the project.
Accepted reviews can be linked to one or more changes to the source
code, those corresponding to the changes proposed and finally merged.

For example, in GitHub when a pull request is accepted, all the
commits included in it are merged (maybe squashed, maybe rebased)
in the corresponding git repository. The same can be said of
GitLab merge requests. In the case of Gerrit, a code review usually
corresponds to a single commit.


## Objectives

* Volume of coding activity.  
    Accepted code reviews are a proxy for the activity in a project.
    By counting accepted code reviews in the set of repositories corresponding
    to a project, you can have an idea of the overall coding activity in
    that project that leads to actual changes.
    Of course, this metric is not the only one that should be
    used to track volume of coding activity.


## Implementation

**Aggregators:**
* Count. Total number of accepted reviews during the period.
* Ratio. Ratio of accepted reviews over total number of reviews during that period.

**Parameters:**
* Period of time. Start and finish date of the period during which accepted reviews are considered. Default: forever.  

* Criteria for source code. Algorithm. Default: all files are source code.  
    If we focus on source code, we need a criterion for deciding whether a file belongs to the source code or not.


### Filters

* By actor type (submitter, reviewer, merger). Requires merging identities corresponding to the same actor.
* By groups of actors (employer, gender... for each of the actors).
Requires actor grouping, and likely, actor merging.


### Visualizations

* Count per time period over time
* Ratio per time period over time

These could be grouped by actor type or actor group by applying the filters defined above.
These could be represented as bar charts, with time running in the X axis.
Each bar would represent accepted reviews to change the code
during a certain period (eg, a month).


### Tools Providing the Metric

* [Grimoirelab](https://chaoss.github.io/grimoirelab) provides this metric out of the box for GitHub Pull Requests and also provides data to build similar visualizations for GitLab Merge Requests and Gerrit Changesets.
  - View an example on the [CHAOSS instance of Bitergia Analytics](https://chaoss.biterg.io/app/kibana#/dashboard/a7b3fd70-ef16-11e8-9be6-c962f0cee9ae).  
  - Download and import a ready-to-go dashboard containing examples for this metric visualization based on GitHub Pull Requests data from the [GrimoireLab Sigils panel collection](https://chaoss.github.io/grimoirelab-sigils/panels/github-pullrequests/).
  - Add a sample visualization for GitHub Pull requests to any GrimoreLab Kibiter dashboard following these instructions:
    * Create a new `Timelion` visualization.
    * Select `Auto` as Interval.
    * Paste the following Timelion Expression:
    ```
    .es(index=git, q="title:Merge* OR files:0", timefield=grimoire_creation_date).bars().color(#94c3af).label("Pull Requests Merged")
    ```
    * The expression, step by step:
      * `.es()`: used to define an ElasticSearch query.
        * `index=git`: use git index.
        * `q="title:Merge* OR files:0"`: heuristic to filter in merges.
        * `timefield=grimoire_creation_date`: time will be based on commit creation date (as our query looks for merge commits, it should be the date in which the merge was effectively done).
      * `.bars()`: draw bars instead of lines.
      * `.color()` and `.label()`: some formatting options.
    * If you wish to get also the trend, use this instead (i.e. repeating the same expression twice and calling `trend()` the second time):
    ```
    .es(index=git, q="title:Merge* OR files:0", timefield=grimoire_creation_date).bars().color(#94c3af).label("Pull Requests Merged"),
    .es(index=git, q="title:Merge* OR files:0", timefield=grimoire_creation_date).trend().color(#ffb745).label("Trend")
    ```
    * As discussed [above for GitHub case](#specific-description-github), sometimes is not easy to identify merges. As you probably noticed, in this example we based our expression on GrimoireLab Git index. Besides, it could be applied to any other similar environment using Git repositories, not only to GitHub.
  - Example screenshot: ![GrimoireLab screenshot of metric Reviews Accepted](https://github.com/chaoss/wg-evolution/blob/master/metrics/images/reviews_accepted_GrimoireLab.png)


### Data Collection Strategies

**Specific description: GitHub**

In the case of GitHub, accepted reviews are defined as "pull requests
whose changes are included in the git repository",
as long as it proposes changes to source code files.

Unfortunately, there are several ways of accepting reviews, not
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
finding the corresponding commits in the git repository.

In some cases, projects have policies of mentioning the commits
when the pull request is closed (such as "closing by accepting commits
xxx and yyyy"), which may help to track commits in the git repository.

Mandatory parameters (for GitHub):

* Heuristic for detecting accepted pull requests not accepted
  via the web interface. Default: None.

**Specific description: GitLab**

In the case of GitLab, accepted reviews are defined as "merge requests
whose changes are included in the git repository",
as long as it proposes changes to source code files.

Mandatory parameters (for GitLab):

* Heuristic for detecting accepted pull requests not accepted
  via the web interface. Default: None.

**Specific description: Gerrit**

In the case of Gerrit, accepted reviews are defined as "changesets
whose changes are included in the git repository",
as long as they proposes changes to source code files.

Mandatory parameters (for Gerrit):

* None.



## References
 
