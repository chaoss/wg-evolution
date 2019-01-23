# Community Manager

## Description

This use case deals with how a project's community manager might keep track of a collection of repositories. 

## Main goals

Help a community manager maintain awareness of a repository collection. 

Support and enhance communication about a repository collection to other stakeholders. In some cases these will be individuals who are funding the community manager's role. In other cases, and possibly simultaneously, they will be organizations with a shared interest in a particular community. 

## Vocabulary
* Community Manager: takes a variety of perspectives, depending on where their communities are in the lifecycle of growth, maturity and decline. 

* Community: A collection of interconnected repositories. Sometimes referred to as an "ecosystem" if it scales largely enough. 

* Community Manager Metrics: This is an evolving use case of what we are learning from community managers, some of whom we are working with on live experiments with a CHAOSS project prototyping software tool called Augur (http://www.github.com/CHAOSS/augur). At this point we are paying particular focus to how community managers consume metrics and how the presentation of open source software health and sustainability metrics could make them more and in some cases less useful for doing their jobs. 

* Others as defined in [First Code Contribution](./first-code-contributions.md) use case. 

## Primary actor

Person responsible for managing the community of repositories. 

## Stakeholders

* Community manager for the project, for tracking how the onboarding process is performing.

* Project community in general, for self-awareness about how the onboarding
process is performing.

* Prospective contributors, to make decisions on whether to
invest their time and effort in joining a community,
or in general, produce contributions for the project.

## Preconditions

* The community manager should have an interest in a broad perspective on many projects. 
* The community manager should have a larger than 1 set of repositories they are interested in tracking collectively.  

## Questions

* Embedded in Metrics Definition

## Metrics

\[Work in progress\]

Right now, based on Augur prototypes and follow up discussions so far,
we have the following observations that will inform our work both the
the \"Growth Maturity and Decline\" working group and in Augur
Development. There are a few things we have learned from prototyping
Augur with community managers. These features in Augur are particularly
valued:

1.  Allowing comparisons with projects within a defined universe is
    essential

2.  Allow community managers to add and remove repositories that they
    monitor from their repertoires periodically.

3.  Downloadable graphics

4.  Downloadable data (.csv or .json)

5.  Availability of a \"Metrics API\", limiting the amount of software
    infrastructure the CM needs to maintain for themselves. This is more
    valued by program managers overseeing larger portfolios right now,
    but we think has potential to grow as awareness of the relatively
    light weight of this approach becomes more apparent. By apparent, we
    really mean \"easy to use and understand\"; right now it is for a
    programmer, but less so for a community manager without this
    background or current interest.

Date Summarized Comparison Metrics
==================================

With these advantages in mind, making the most of this opportunity to
help community managers with useful metrics is going to include the
availability of *date summarized comparison metrics*. These types of
metrics have two \"filters\" or \"parameters\" fed into them that are
more abstractly defined in the Growth, Maturity and Decline metrics on
the CHAOSS project.

1.  Given a pool of repositories of interest for a community manager,
    rank them in ascending or descending order by a metric.

2.  Over a specified time period or

3.  Over a specified periodicity (i.e., month) for a length of time
    (i.e., year).

For example, one open source program office we talked with is interested
in the following set of *date summarized comparison metrics*. Given a
pool of repositories of interest to the program office (dozens to
hundreds of repositories):

1.  What ten repositories have the most commits this year (straight
    commits, and lines of code)?

2.  How many new projects were launched this year?

3.  What are the top ten new repositories in terms of commits this year
    (straight commits, and lines of code)?

4.  How many commits and lines of code were contributed by outside
    contributors this calendar year? Organizationally sponsored
    contributors?

5.  What organizations are the top five external contributors of
    commits, comments and merges?

6.  What are the total number of repository watchers we have across all
    of our projects?

7.  Which repositories have the most stars? Of the ones new this year?
    Of all the projects? Which projects have the most new stars this
    year?

Open Ended Community Manager Questions to Support with Metrics
==============================================================

There are other, more open ended questions that may be useful to open
source community managers:

1.  Is a repository active?

    1.  Visual differentiation that examines issue and commit data

    2.  Activity in the past 30 days

    3.  Across all repositories, present the 50th percentile as a
        baseline and show repositories above and below that line.

2.  Should we archive this repository?

    1.  Enable an input from the manager after reviewing statistics.

    2.  Activity level, inactivity level and dependencies

    3.  Mean/Median/Mode histogram for commits/repo

3.  Should we feature this repository in our top 10? (Probably a
    subjective decision based on some kind of *composite scoring system*
    that is likely specific to the needs of every community manager or
    program office.)

4.  Who are our top authors? (Some kind of aggregated contribution
    ranking by time period \[year, month, week, day?\]. *nominally, I
    have a concern about these kinds of metrics being \"gameable\", but
    if they are not visible to contributors themselves, there is less
    \"gaming\" opportunity.*)

5.  What are our top repositories? (Probably a subjective decision based
    on some kind of *composite scoring system* that is likely specific
    to the needs of every community manager or program office.)

6.  Most active repositories by time period \[Week? Month? Year?\].
    Activity to be revealed through a mix of Retention and Maintainer
    activity primarily focusing on the latter. Number of issues and
    commits. Also the frequency of pull requests and the number of
    closed issues.

7.  Least active repositories by time period \[Week? Month? Year?\].
    *Bottom of scores calculated, as above.*

8.  Who is our most active contributor (Some kind of aggregated
    contribution ranking by time period \[year, month, week, day?\].
    *nominally, I have a concern about these kinds of metrics being
    \"gameable\", but if they are not visible to contributors
    themselves, there is less \"gaming\" opportunity.*)

9.  What new contributors submitted their first new patches/issues this
    week? (*Visualization Note:* New contributors can be colored in
    visualizations and then additionally a graph can be made for number
    of)

10. Which contributors became inactive? (Will need a mechanism for
    setting \"inactive\" thresholds.)

11. Baseline level for the \"average\" repository in an organization and
    for each, individual organization repository.

12. What projects outside of a community manager's general view (GitHub
    organization or other boundary) doe my repositories depend on or do
    my contributors also significantly contribute to?

13. Build a summary report in 140 characters or less. For example,
    \"Your total commits in this time period \[week? month?\] across the
    organization increased 12% over the last period. Your most active
    repositories remained the same. You have 8 new contributors, which
    is 1 below your mean for the past year. For more information, click
    here.\"

14. Once a metrics baseline is established, what can be done to move
    them? [^1]

15. Are there optimal measures for some metrics?

    1.  Pull request size?

    2.  Ratio of maintainers to contributors?

    3.  New contributor to consistent contributor ratio?

    4.  New contributor to maintainer ratio?



## Comments

This use case is focused on code contributions,
even when there are many other important kinds of contributions
to a project.
