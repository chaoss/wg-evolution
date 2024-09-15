# Code Changes Commits

**Question: How many changes were made to the source code during a specified period?** 


## Overview
Code Changes Commits measures changes to the source code over a specific period, where a "change" represents an atomic modification made by developers, typically in the form of a commit. Each data point corresponds to a commit that alters files considered part of the source code. This metric helps in assessing the health and sustainability of a project by providing insights into developers activity. A higher volume of code changes indicates active development, maintenance, and responsiveness to bugs or features. However, the metric alone doesn’t capture code quality or the significance of each change. Monitoring contributions across teams can help highlight engagement disparities, ensuring all community members are equally involved in the development process of each project.


## Want to Know More?

<span markdown="1"><details>
<summary>Click to read more about this metric.</summary>

### Data Collection Strategies

**Specific description: Git**

Mandatory parameters (for Git):
* Date type. Either author date or committer date. Default: author date. For each git commit, two dates are kept: when the commit was authored, and when it was committed to the repository. For deciding on the period, one of them has to be selected.
* Include merge commits. Boolean. Default: True. Merge commits are those which merge a branch, and in some cases are not considered as reflecting a coding activity.
* Include empty commits. Boolean. Default: True. Empty commits are those which do not touch files, and in some cases are not considered as reflecting a coding activity.


### Filters

* By actors (author, committer). Requires actor merging (merging ids corresponding to the same author).
* By groups of actors (employer, gender...). Requires actor grouping, and likely, actor merging.
* By [tags](https://www.odoo.com/documentation/13.0/reference/guidelines.html#tag-and-module-name) (used in the message of the commits). Requires a structure for the message of commits. This tag can be used in an open-source project to communicate to every contributors if the commit is, for example, a fix for a bug or an improvement of a feature.
* Count per month over time
* Count per group over time

### Visualizations
  - View an example on the [CHAOSS instance of Bitergia Analytics](https://chaoss.biterg.io/app/kibana#/dashboard/Git).  
  - Download and import a ready-to-go dashboard containing examples for this metric visualization from the [GrimoireLab Sigils panel collection](https://chaoss.github.io/grimoirelab-sigils/panels/git/).
  - Example screenshot:
  
    ![GrimoireLab screenshot of metric Code_Changes](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/code-development-activity/images/code-changes_grimoirelab.png)

</details></span>


## References

* https://www.odoo.com/documentation/13.0/reference/guidelines.html#tag-and-module-name


## Contributors
- Elizabeth Barron
- Georg Link
- Matt Germonprez
- Peculiar C Umeh


## Additional Information
To edit this metric please [submit a Change Request here](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/code-development-activity/code-changes-commits.md)

To reference this metric in software or publications please use this stable URL: [https://chaoss.community/?p=4707](https://chaoss.community/?p=4707)

<!-- # For groupings in the knowledge base
Context tags: Contribution, Software, Lifecycle
Keyword tags: change request, code changes, pull requests, merged, merging, source code
→
