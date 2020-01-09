# Issue Age

Question: What is the aggregated time that issues have been left open in a project?

## Description
This aggregated metric is an indication of how long issues have been left open in the considered time period. If an issue has been closed but re-opened again within that period if will be considered as having remained open since its initial opening date.

## Objectives
When the issue age is increasing, identify the oldest open issues in a project to gain insight as to why they have been open for an extended period of time. Additionally, to understand how well maintainers are resolving issues and how quickly issues are resolved. 

## Implementation
For all open issues, get the date the issue was opened and calculate the number of days to current date.

**Aggregators:**
* Average. Average age of all open issues.
* Median. Median age of all open issues.

**Parameters:**
* Period of time. Start and finish date of the period during which open issues are considered. Default: forever (i.e., the entire observable period of the project's issue activity).

### Filters
* Module or working group
* Tags/labels on issue

### Visualizations

1. Summary data for open issues
![Summary data for open issues](./images/open_issue_data.png)

2. Count of open issues per day
![Count of open issues per day](./images/open_issue_count_timeseries.png)

### Tools Providing the Metric

* [GrimoireLab](https://chaoss.github.io/grimoirelab/)
* [Augur](http://augur.osshealth.io/api_docs/#api-Evolution-Open_Issue_Age_Repo_)

### Data Collection Strategies 

For specific descriptions of collecting data about closed issues, please refer to the [corresponding section of Issues Closed](./Issues_Closed.md#data-collection-strategies).

## Resources
