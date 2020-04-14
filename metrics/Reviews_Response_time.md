# Reviews Response Time

Question: How quickly are code review requests responded to by other contributors?

## Description
This metric is measuring how much time there is between when a code review request is posted and is responded to by another contributor. When code is reviewed, it does not immediately go into the code base. The review request needs to be reviewed and responded to by other developers. This metric would be measuring the length of time from when the review is posted and another developer responds to it.

## Objectives
This metric can tell you how active the working group is. If reviews are a proxy for the activity in a project, then so is how quickly the reviews are responded to. Also, it can show you how cooperative the community around the working group is because the responses are done by other developers.

## Implementation
**Aggregators:**
* An average of the review response times in days.
* A median of the review response times in days.

**Parameters:**
* Period of time. Default: forever.

### Filters (optional)
* By actors
* By time measurement (over hours, days, weeks, months)
* Date code review was posted

### Visualizations (optional)
* Dashboard-style gauges for median and average times
* Bar chart of response time averages over months

### Tools Providing the Metric (optional)
* GrimoireLab
* Augur

### Data Collection Strategies (Optional)
Look at the dates that reviews are posted and subtract the dates reviews are accepted or declined.

## References

