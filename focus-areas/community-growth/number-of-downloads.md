# Number of Downloads

### This metric is a release candidate. To comment on this metric please see [Issue #463](https://github.com/chaoss/wg-evolution/issues/463). Following a comment period, this metric will be included in the next regular release.

**Question:** How many downloads occurred since the software artifact was released?  

Synonyms: Clones

## Overview
Number of Downloads captures the traffic to a project's repository by measuring the frequency of downloaded or cloned software artifacts. This may include downloads through package managers like homebrew, pip, or apt. Analyzing download activity helps maintainers understand the demographics of the user base, download patterns, and the density of downloads, which may reveal a project's reach and popularity.

## Want to Know More?

<span markdown="1"><details>
<summary>Click to read more about this metric.</summary>

### Data Collection Strategies
- **Platform Data**: Use download counts from hosting platforms (e.g., GitHub, SourceForge) if available.
- **System Logs**: Retrieve logs where software downloads or updates are recorded.
- **Web Scraping**: Gather data from web analytics, such as traffic to download pages.
- **Package Managers**: If distributed via package managers, consult their APIs for download counts.

### Filters
- **Timeframe**: View download activity within a specific date range.
- **Format/Platform/OS**: Analyze downloads by platform, such as OS or mobile vs. desktop.
- **Geolocation/Channels**: Identify download sources by region.
- **Programming Languages**: Track downloads of different language-specific packages (e.g., Python, Julia).
- **Package Type**: Look at package-specific downloads (e.g., pip, PyPi packages).
- **APIs**: (eg., cloud based such as boto3/awscli, gcloud )
- **Version**: Examine downloads by software version to understand adoption of new updates.
- **Mobile versus Desktop**

It is important to note that some software can be downloaded multiple times on the same system, and different versions of the same software too.

### Visualizations
- **Traffic Activity on GitHub**  
  ![Example chart showing traffic activity from GitHub](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/community-growth/images/traffic-github.png)  
  *Figure 1: Traffic activity visualization for GitHub repositories*

- **Download Activity on SourceForge**  
  ![Example chart showing number of downloads from SourceForge](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/community-growth/images/number-of-downloads-sourceforge.png)  
  *Figure 2: Download activity visualization for SourceForge projects*

</details></span>

## References
- [GitHub Repository Traffic](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository)
- [Homebrew Formula Analytics](https://formulae.brew.sh/analytics/install/365d/)
- [Open Source Guide to Metrics](https://opensource.guide/metrics/)

## Contributors
- Armstrong Foundjem
- Elizabeth Barron
- Yigakpoa L. Ikpae

## Additional Information
To edit this metric please [submit a Change Request here](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/community-growth/number-of-downloads.md).
To reference this metric in software or publications please use this stable URL: [https://chaoss.community/?p=4466](https://chaoss.community/?p=4466)

***This metric was last reviewed on October 31, 2024 as part of the continuous release process.***

<!-- # For groupings in the knowledge base
Context tags: Software Usage, Project Health, Community Engagement, Data Collection
Keyword tags: Downloads, Clones, User Demographics, Package Managers, Traffic Analysis, Platform Analytics
-->
