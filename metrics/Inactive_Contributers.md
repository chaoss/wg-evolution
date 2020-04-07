# Inactive_Contributers

Question: How many Contributers have gone inactive over a specific period of time.

## Description
A metric that shows how many contributers have stopped committing over a specific period of time. The period of time required for a contributer to be counted as inactive can be decided by a variable and this metric will display the number of contributers that have been labeled as inactive over a given time frame.

## Objectives
The objective is to determine how many people are losing intrest in the project. This can be useful in determining intrest in the project. User intrest and user retention is an important metric for determing the health of a project and watching how many users are going inactive can help in finding those values. It is important to know if many people are leaving the project and have stopped commiting.

## Implementation
The metric will take in 2 variables a period and a cutoff. The period will be the period over which the number of inactive members will be displayed. For example if period=year then it will display the number of contributers that have gone inactive each year. The cutoff will determine how long it takes for a contributer to be labeled as inactive. If a previous contributer has not made any commits for longer than the cutoff, then they will be added to the inactive count of the period of their last commit. Because of this there will be a bit of a delay between when a user stops commiting and a user shows up as inactive thus this metric will not work for days more recent than the cuttoff.

The metric will work by:
1. getting a list of all contributers
2. checking the last commit date
3. if the last commit date is before the cutoff then add them to the inactivity count of the period they last committed in.
4. create list of inactive contributers

### Aggregators:
- inactive: number of inactive contributers

### Filters
- Minimum commits required to be considered active
- Period of time to determine inactivity
- Start date/End date
- Period of graph

### Data Collection Strategies
The list of contributers can be collected usign the existing contributers metric.
To determine the last commit date new code may be needed.


