# Number of Downloads

### This metric is a release candidate. To comment on this metric please see [Issue #463](https://github.com/chaoss/wg-evolution/issues/463). Following a comment period, this metric will be included in the next regular release.

Question: How many downloads occurred since the software artifact was released? 

Synonyms: Clones

## Description
Number of Downloads measures the relative and absolute traffic to a project’s repository on the frequency of downloaded or cloned software artifacts (this may also include downloads through package managers, e.g., homebrew, pip, apt) Maintainers can use this information to analyze the demographics of download activity of a given repository and the number of downloads per user (density of downloads).

## Objectives

To determine the number of downloads of software artifacts and determine the number of hosts downloading software artifacts.

While this metric is not central to an organization's KPI index, it is, however, important to understand external factors such as end-user demographics and download patterns.
Open source software should be made available to every user who accepts the terms and conditions irrespective of their demographics, language, etc.  

## Implementation
*The usage and dissemination of health metrics may lead to privacy violations. Organizations may be exposed to risks. These risks may flow from compliance with the GDPR in the EU, with state law in the US, or with other law. There may also be contractual risks flowing from terms of service for data providers such as GitHub and GitLab. The usage of metrics must be examined for risk and potential data ethics problems. Please see [CHAOSS Data Ethics document](https://github.com/chaoss/community/blob/main/data-use-statement.md) for additional guidance.*

### Filters 
- Time
- Format/Platform/OS
- Location/Channels
- Programming languages (eg., Python, Julia)
- Packages (eg., PyPi packages)
- APIs (eg., cloud based such as boto3/awscli, gcloud )
- Mobile versus Desktop
- Versions

It is important to note that some software can be downloaded multiple times on the same system, and different versions of the same software too.

### Visualizations 

![example charts showing traffic activity from GitHub](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/community-growth/images/traffic-github.png)

Source: https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository

![example chart showing number of downloads from sourceforge](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/community-growth/images/number-of-downloads-sourceforge.png)

Source: https://sourceforge.com

### Tools Providing the Metric

- https://formulae.brew.sh/analytics/install/365d/
- https://opensource.guide/metrics/

### Data Collection Strategies

- Web scraping
- System logs
- Platform-provided data, if project is hosted

## References

https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository


## Known Contributors

- Armstrong Foundjem
- Elizabeth Barron

***This metric was last reviewed on November 30, 2022 as part of the continuous release process.***
