# Issue Response Time

Question: How much time passes between the opening of an issue and a response in the issue thread from another contributor?

## Description
This metric is an indication of how much time passes between the opening of an issues and a response from other contributors. 

This metric is a specific case of the [Time to First Reponse metric](https://github.com/chaoss/wg-common/blob/master/focus-areas/when/time-to-first-response.md) in the [Common working group](https://github.com/chaoss/wg-common). 


## Objectives
Learn about the responsiveness of an open source community. 

## Implementation

**Aggregators:**
* Average. Average response time in days.
* Median. Median response time in days. 

**Parameters:**
* Period of time. Start and finish date of the period. Default: forever.
*  Period during which responses are counted.

### Filters
* response from role in project (e.g., first maintainer response)
* bot versus human (e.g., filter out automated “welcome first contributor messages”)
* opened by role in project (e.g., responsiveness to new contributors versus long-timers)
* date issue was opened
* status of issue (e.g., only look at currently open issues)

### Visualizations
![Example visualization from GrimoireLab](images/issue_response_duration_grimoirelab.png)

### Tools Providing the Metric 
* GrimoireLab: [General for any ticketing system](https://chaoss.github.io/grimoirelab-sigils/panels/efficiency-timing-overview/), [GitHub Issues](https://chaoss.github.io/grimoirelab-sigils/panels/github-issues-efficiency/), [GitLab Issues](https://chaoss.github.io/grimoirelab-sigils/panels/gitlab-issues-efficiency/)
* [Augur](http://augur.osshealth.io/api_docs/#api-Evolution-Issue_Response_Time_Repo_)

### Data Collection Strategies

Look at the [Issues New](https://github.com/chaoss/wg-evolution/blob/master/metrics/Issues_New.md) metric for a definiton of “issues.” Subtract the issue opened timestamp from the first response timestamp. Do not count responses if created by the author of the issue.

## References
