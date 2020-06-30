# Inactive Contributors

Question: How many Contributors have gone inactive over a specific period of time?

_This metric is a release candidate The 30 day comment period for this metric begins on 07/01/2020 and ends on 07/031/2020. To comment on this metric please see [Issue #357](https://github.com/chaoss/wg-evolution/issues/357). Following the comment period this metric will be included in the next regular release._


## Description
A metric that shows how many contributors have stopped contributing over a specific period of time. The period of time required for a contributor to be counted as inactive can be decided by a variable and this metric will display the number of contributors that have been labeled as inactive over a given time frame.

## Objectives
The objective is to determine how many people have stopped contributing actively. This could be useful for community managers to determine if key members are losing interest, or are taking a break.

## Implementation
The metric will take in two variables - a time period and a interval. The time period will be the period over which the number of inactive members will be displayed. For example if time period=year then it will display the number of contributors that have gone inactive each year. The interval will determine how long it takes for a contributor to be labeled as inactive. If a contributor has not made a contribution for a length of time longer than the interval, they will be counted as inactive.

The metric will work by:
1. getting a list of all contributors
2. checking the last contribution date
3. if the last contribution date is before the cutoff then add them to the inactivity count of the period they last contibuted in.
4. create list of inactive contributors

**Aggregators:**
- inactive: number of inactive contributors

### Filters
- Minimum contributions required to be considered active
- Period of time to determine inactivity
- Start date/End date
- Period of graph

### Data Collection Strategies
The list of contributors can be collected using the existing contributors metric.
To determine the last contribution date new code may be needed.
