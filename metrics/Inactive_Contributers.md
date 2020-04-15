# Inactive_Contributors

Question: How many Contributors have gone inactive over a specific period of time?

## Description
A metric that shows how many contributors have stopped contributing over a specific period of time. The period of time required for a contributer to be counted as inactive can be decided by a variable and this metric will display the number of contributors that have been labeled as inactive over a given time frame.

## Objectives
The objective is to determine how many people have stopped contributing actively. This could be useful for community managers to determine if key members are losing interest, or are taking a break.

## Implementation
The metric will take in 2 variables a time period and a interval. The time period will be the period over which the number of inactive members will be displayed. For example if time period=year then it will display the number of contributors that have gone inactive each year. The interval will determine how long it takes for a contributer to be labeled as inactive. If a contributor has not made a contribution for a length of time longer than the interval, they will be counted as inactive.

The metric will work by:
1. getting a list of all contributors
2. checking the last contribution date
3. if the last contribution date is before the cutoff then add them to the inactivity count of the period they last contibuted in.
4. create list of inactive contributors

** Aggregators:**
- inactive: number of inactive contributors

### Filters
- Minimum contributions required to be considered active
- Period of time to determine inactivity
- Start date/End date
- Period of graph

### Data Collection Strategies
The list of contributors can be collected usign the existing contributors metric.
To determine the last contribution date new code may be needed.


