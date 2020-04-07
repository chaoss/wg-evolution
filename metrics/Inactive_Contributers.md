# {Inactive_Contributers}

Question: How many Contributers have gone inactive over a specific period of time.

## Description
A metric that shows how many contributers have stopped committing over a specific period of time. The period of time required for a contributer to be counted as inactive can be decided by a variable and this metric will display the number of contributers that have been labeled as inactive over a given time frame.
The first few sentences should match the description in the [metrics list](../activity-metrics-list.md).

## Objectives
The objective is to determine how many people are losing intrest in the project. This can be useful in determining intrest in the project. It is important to know if many people are leaving the project and have stopped commiting.

## Implementation
The metric will take in 2 variables a period and a cutoff. The period will be the period over which the number of inactive members will be displayed. For example if period=year then it will display the number of contributers that have gone inactive each year. The cutoff will determine how long it takes for a contributer to be labeled as inactive. If a previous contributer has not made any commits for longer than the cutoff, then they will be added to the inactive count of the period of their last commit. Because of this there will be a bit of a delay between when a user stops commiting and a user shows up as inactive thus this metric will not work for days more recent than the cuttoff.

The metric will work by:
1. getting a list of all contributers
2. checking the last commit date
3. if the last commit date is before the cutoff then add them to the inactivity count of the period they last committed in.

### Filters (optional)
Include a Filter

### Visualizations (optional)


### Tools Providing the Metric (optional)


### Data Collection Strategies (Optional)
The list of contributers can be collected usign the existing contributers metric.
To determine the last commit date new code may be needed.

## References

