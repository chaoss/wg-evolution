# Change Request Reviews

**Question:** To what extent are [change requests](https://chaoss.community/metric-change-requests/) put through a formal review process using platform features?

## Overview
The **Change Request Reviews** metric evaluates the level and quality of formal review processes for change requests (e.g., pull requests) within open-source projects. This metric tracks specific data points such as the number of reviews, types of review feedback, and review outcomes (e.g., accepted, declined) to determine the rigor and quality of reviews. Measuring this helps project maintainers gauge the thoroughness of code evaluation, process efficiency, and software quality. Change request reviews include top level comments about the entire change request, file level comments asking for specific changes, and whether the change request was “accepted”, “had changes requested”, or the reasoning behind a change request being closed without getting merged. Additionally, this metric can reveal insights into DEI-related aspects, such as the diversity of contributors participating in review processes.

Notes:

* Change requests into a repository’s default branch may have different review characteristics than change requests moved into development branches.  
* Change request reviews are implemented in practice in a number of different ways. For example, some projects use change request comments as a form of review, while other projects use more formalized change request review features available on major open source software development platforms. The specific review practices of a project are sometimes documented.

## Want to Know More?

<span markdown="1"><details>
<summary>Click to read more about this metric.</summary>

### Data Collection Strategies
- **Interviews with Contributors** — Gather feedback on contributors' experiences with the review process, such as perceived fairness and thoroughness.
- **Platform API Data** — Collect data from GitHub or GitLab APIs, such as the number of reviews per change request, review duration, and contributor involvement.
- **Code Review Analysis** — Review change requests for specific feedback types (e.g., technical improvements, code standards adherence).

### Filters
- **Contributor Type** — Differentiate between bot- and human-driven reviews.
- **Request Outcome** — Filter by accepted vs. declined change requests.
- **Review Duration** — Analyze the time between submission and final review.
- **Review Process Documentation** — Check for documented guidelines in `CONTRIBUTING.md` and consistency with actual practices.

### Visualizations
None Provided

</details></span><br>

## References
- [Managing changes in open-source projects](https://opensource.com/article/19/3/managing-changes-open-source-projects)
- [GitLab change management handbook](https://about.gitlab.com/handbook/engineering/infrastructure/change-management/)
- Baker, R. A. (1997). *Code reviews enhance software quality*. Proceedings of the 19th international conference on Software engineering.
- Kemerer, C. F., & Paulk, M. C. (2009). *The impact of design and code reviews on software quality: An empirical study based on PSP data*. IEEE Transactions on Software Engineering, 35(4), 534-550.

## Contributors
- Kevin Lumbard
- Elizabeth Barron
- Vinod Ahuja
- Sean Goggins
- Enoch Kaxada
- Yigakpoa L Samuel

## Additional Information
To edit this metric, please [submit a Change Request here](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/code-development-process-quality/change-request-reviews.md).  
To reference this metric in software or publications, please use this stable URL: [https://chaoss.community/?p=4712](https://chaoss.community/?p=4712)

<!-- # For groupings in the knowledge base
Context tags: contribution, software, code review, process
Keyword tags: change request, merge request, pull request, formal review, code review, open, closed
-->
