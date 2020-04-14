# Issue Contributors

Question: How many contributors have contributed issues, or made comments on issues?

## Description
This metric is an indication of the volume of people who are active on issues at any point in time. 

Issues are core to any open source software as they allow those working on the project to stay updated on any ongoing
concerns with the project. This metric is interested in measuring the people who contribute to the issues whether by creating
them or creating comments on them. This is an important metric for community health becuase it signifies which members are
critically analyzing the project for errors and bugs.

## Objectives
The removal of bugs and issues is of course important for any project and by measuring the issue contributors we can get an
idea as to how many contributors to the project are testing the project for any sort of problematic issues. Issues by
themselves are useless if no one in the project acknowledges them, which is why this metric is important as it essentially
shows the engagement between the contributors and the issues on the project. Furthermore, engagement with issues can also be
used as a signifier for constant coding development to resolve said issues, meaning that the project is constantly growing
and doesn't remain stagnant.

## Implementation
Aggregators
  - Count. Total number of issue contributors.
  - Ratio. Ratio of active issue contributors over total project contributors.
Parameters 
  - Period of time. Start and finish date of the period during which issues are considered. Default: forever.
  - Criteria for source code. Algorithm. Default: all issues are related to source code.
   We assume that we only care about issues related to the source code if this is not the case the default can be modified.
  - Criteria for active. Algorithm. Default: Having created an issue or making a comment on a issue.

### Filters (optional)
  - By actors (submitter, commenter, closer). Requires merging identities corresponding to the same author.

### Visualizations (optional)
  - Count per time period over time
  - Ratio per time period over time

### Tools Providing the Metric (optional)

### Data Collection Strategies (Optional)

## References
Blog posts, websites, academic papers, or books that mention the metric and provide more background.
