# Change Request Commits

**Question:** How many [code change commits](https://chaoss.community/metric-code-change-commits/) are included in a [change request](https://chaoss.community/metric-change-requests/)?

## Overview
The **Change Request Commits** metric counts the number of individual commits associated with a change request (such as a pull request). It lists each contributor who authored commits and includes references to parent commits. This count provides insights into repository activity patterns and the complexity of each change request: higher commit counts often signal complex or collaborative requests, potentially influencing the merging process and identifying contributors who actively work on more challenging changes. 

This metric can also guide repository management by revealing local and community-wide patterns in change request sizes and participant counts. Understanding these patterns helps maintainers refine repository policies, spot outliers in commit behaviors, and assess inclusiveness by examining contributors who regularly submit commits through change requests.
This metric may inform the diversity and inclusiveness of a project through exploration of the [demographics](https://github.com/drnikki/open-demographics) of contributors who get commits accepted through a change request process.

## Want to Know More?

<span markdown="1"><details>
<summary>Click to read more about this metric.</summary>

### Data Collection Strategies
- **Mining Git Logs** — Use git logs to identify the commits associated with each change request.
- **API Calls to Platforms** — Retrieve data on commits and change requests from platform APIs, such as GitHub or GitLab.

### Filters 
- **Lines of Code Added/Removed per Commit**
- **Change in Code Over Time** — Measures the progression of changes in each commit.
- **Iteration of Commits** — Number of times the same file is modified in a change request.
- **Files Changed per Commit**
- **Contributors per Commit**

### Visualizations
![augur_api](https://github.com/chaoss/wg-evolution/focus-areas/code-development-activity/images/change-request-commits_augur-api.png)  
*Figure X: Change Request Commits Visualization (Augur)*

</details></span><br>

## References
- [Goggins, S., Lumbard, K., & Germonprez, M. (2021). *Augur: Architecture for Capturing, Reshaping, and Socially Contextualizing Open Source Software Communities*. ACM SoHeal Conference.](https://www.seangoggins.net/wp-content/plugins/zotpress/lib/request/request.dl.php?api_user_id=655145&dlkey=HNG22ZSU&content_type=application/pdf)

## Contributors
- Vinod Ahuja
- Kevin Lumbard
- Elizabeth Barron
- Sean Goggins
- Armstrong Foundjem
- Yigakpoa L. Samuel

## Additional Information
To edit this metric please [submit a Change Request here](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/code-development-activity/change-request-commits.md).  
To reference this metric in software or publications, please use this stable URL: [https://chaoss.community/?p=4731](https://chaoss.community/?p=4731)  

<!-- # For groupings in the knowledge base
Context tags: contribution, software, lifecycle
Keyword tags: change request, pull requests, code changes, commits, merged, merging, source code
-->
