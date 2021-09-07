# Issue Resolution Duration

Question: How long does it take for an issue to be closed?

## Description
This metric is an indication of how long an issue remains open, on average, before it is closed. 
Issues are defined as in [Issues Closed](https://chaoss.community/metric-issues-closed/).

For issues that were reopened and closed again, only the last close date is relevant for this metric.

## Objectives
This metric can be used to evaluate the effort and time needed to conclude and resolve discussions. This metric can also provide insights to the level of responsiveness in a project.

## Implementation

For each closed issue:
* Issue Resolution Duration = Timestamp of issue closed - Timestamp of issue opened 

**Aggregators:**
* Average. Average amount of time (in days, by default) for an issue in the repository to be closed.

**Parameters:**
* Period of time. Start and finish date of the period. Default: forever.  
    Period during which issues are considered.


### Filters

* By time. Provides average issue resolution duration time starting from the provided beginning date to the provided end date.
  - By open time. Provides information for how long issues created from the provided beginning date to the provided end date took to be resolved.(The issue may be resolved in time later than the specified time period)
  - By closed time. Provides information for how long old issues were that were closed from the provided beginning date to the provided end date took to be resolved.(The issue may be created in time earlier than the specified time period)

* By actors (submitter, commenter, closer). Requires actor merging (merging ids corresponding to the same author).

* By groups of actors (employer, gender... for each of the actors). Requires actor grouping, and likely, actor merging.



### Visualizations

* Average over time (e.g. average for January, average for February, average for March, etc.)
* Average for a given time period (e.g. average for all of 2019, or average for January to March)


### Tools Providing the Metric

* [Augur](http://augur.osshealth.io/) provides this metric as [Closed Issue Resolution Duration](http://augur.osshealth.io/api_docs/#api-Evolution-Closed_Issue_Resolution_Duration_Repo_). This metrics are available in both the `repo` and the `repo_group` metric forms - more on that in the [Augur documentation](https://oss-augur.readthedocs.io/en/master/getting-started/create-a-metric/overview.html#metric-forms).


### Data Collection Strategies

For specific descriptions of collecting data about closed issues, please refer to the [corresponding section of Issues Closed](https://chaoss.community/metric-issues-closed/).


## References

