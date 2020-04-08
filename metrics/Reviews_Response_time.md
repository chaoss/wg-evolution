# Reviews Response Time

Question: How quickly were code review requests responded to?

## Description
This metric is how quickly a code review request get responded to. When code is reviewed, it does not immediately go into the code base. The review request needs to be responded to and reviewed by other developers. This metric would be measuring the length of time from when the review is posted and another developer responds to it.

## Objectives
This metric can tell you how active the working group is. If reviews are a proxy for the activity in a project, then so is how quickly the reviews are responded to. Also, it can show you how cooperative the community around the working group is because the responses are done by other developers.

## Implementation
•	A measure of how long the period of time from when the review was posted and another developers looked over the review

•	An average of the review response times

•	A median of the review response times

•	What developers respond the quickest

### Filters (optional)
•	By actors

•	By time measurement (over hours, days, weeks, months)

•	Date review was opened

### Visualizations (optional)
•	Dashboard-style gauges for median and average times

•	Bar chart of response time averages over months

### Tools Providing the Metric (optional)
•	GrimoireLab

•	Augur

### Data Collection Strategies (Optional)
Look at the dates that reviews are posted and subtract the dates reviews are accepted or declined.

## References

Completed by Noah Frew
