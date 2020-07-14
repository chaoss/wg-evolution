# Inactive Contributors

Question: How many Contributors have gone inactive over a specific period of time?

_This metric is a release candidate. The 30 day comment period for this metric begins on 07/01/2020 and ends on 07/31/2020. To comment on this metric please see [Issue #357](https://github.com/chaoss/wg-evolution/issues/357). Following the comment period, this metric will be included in the release._

## Description

A metric that shows how many contributors have stopped contributing over a specific period of time. The time required for a contributor to be counted as inactive will be variable to the community. This metric will display the number of contributors labeled as inactive over a given time frame.

## Objectives
The objective is to determine how many people have stopped contributing actively. This could be useful for community managers to determine if key members are losing interest, or are taking a break.

## Implementation

The metric will take in two variables - the inactive interval and a time period. The inactive interval will determine how long it takes for a contributor to be labeled as inactive. If a contributor has not made a contribution for a length of time longer than the inactive interval, they will count as inactive. The time period will be the period over which the number of members became inactive. For example, if the time period is one year, then it will display the number of contributors who have gone inactive each year.

The metric can be measured by:

1. Gathering data on contributions to the community in a standardized format.
This data may include manually adding "offline" contributions that the community tracks outside of online participation.
2. Checking the last contribution date for each contributor.
3. if the last contribution date is before the inactive interval, then add them to the inactivity count for the selected time period.
4. Generate a list of inactive contributors.

**Aggregators:**

- Inactive: number of inactive contributors

### Filters

- Minimum contributions required to be considered active
- Time period to determine inactivity
- Start date and end date

### Data Collection Strategies

TODO
