# Change Request Commits

Question: How many [code change commits](https://chaoss.community/metric-code-change-commits/) are included in a  [change request](https://chaoss.community/metric-change-requests/)? 

Context tags: Contribution, Software, Lifecycle

Keywords: change request, pull requests, code changes, commits, merged, merging, source code

## Description
This metric enumerates each code change commit associated by a git platform with a change request, and lists the [contributors](https://chaoss.community/metric-contributors/) who made each commit, and any references to parent commits embedded within it. 

There are a number of nuances to be aware of when reviewing the change request commits reported by a platform. If, when, and how commits are squashed has a significant influence on change request commit data reported when compared to code change commit data mined from a software repository directly. It is, for example, common to squash commits when a change request is merged. Often this leads to there being less detail in the change request commits data provided by an API. In addition, each change request also becomes a commit in the branch to which it was merged git log. Notably, only commits that make it to the default branch are reflected in a repository’s code change commits metric, mined from the git log. It is possible to mine commits and pull request commits from other branches, but this practice is not common. Note that there are often Change Requests that are not into the default branch. 

## Objectives
- This metric provides information that can help inform how, in general, a repository’s change request process is managed.  The count of commits in a merge request and the number of people involved in those commits tend to be locally consistent, but across all of open source, there is a wide range of patterns. 
- Enable a maintainer to know which contributors have a history of collaborating with others on a single change request. 
- Larger commit totals on a change request signal greater complexity for merging.  Being aware of this helps to identify potential contributors for future maintainer status (i.e. required skill level)., 
- Knowing the number of change request commits creates awareness of potential change request’s complexity and could influence repository policies and guidelines. 
- To identify change requests that are anomalous to more typical commit patterns (i.e., commit size, commit sequence), or change request patterns (i.e. number of commits).
- This metric may inform the diversity and inclusiveness of a project through exploration of the [demographics](https://github.com/drnikki/open-demographics) of contributors who get commits accepted through a change request process.

## Implementation

### Filters 
* Lines of code added per commit
* Lines of code removed per commit
* Change in code over the period of time
* Iteration in the commits (How many times is the same file touched in the commits included in a merge request)
* Number of files changed per commit
* Contributors per commit

### Visualizations 

![augur_api](https://github.com/chaoss/wg-evolution/focus-areas/code-development-activity/images/change-request-commits_augur-api.png)

[Source: Image is obtained from Augur API](http://augur.chaoss.io/api/unstable/pull_request_reports/average_commits_per_PR?repo_id=25440&start_date=06-01-2021)

### Tools Providing the Metric 

* Augur
    * API Endpoint: [http://augur.chaoss.io/api/unstable/pull_request_reports/average_commits_per_PR?repo_id=25440](http://augur.chaoss.io/api/unstable/pull_request_reports/average_commits_per_PR?repo_id=25440) 
* Grimoire Lab
    * [https://chaoss.github.io/grimoirelab-sigils/chaoss-gmd-cde/lines_of_code_changed/](https://chaoss.github.io/grimoirelab-sigils/chaoss-gmd-cde/lines_of_code_changed/) 

### Data Collection Strategies
* Mining git logs
* API Calls to Platforms

## References
* [Goggins, S., Lumbard, K., & Germonprez, M. (2021). Augur: Architecture for Capturing, Reshaping, and Socially Contextualizing Open Source Software Communities. ACM SoHeal Conference. International Conference on Software Engineering, Virtual. https://doi.org/DOI: 10.5281/zenodo.4627236  ](https://www.seangoggins.net/wp-content/plugins/zotpress/lib/request/request.dl.php?api_user_id=655145&dlkey=HNG22ZSU&content_type=application/pdf)

## Contributors
* Vinod Ahuja
* Kevin Lumbard
* Elizabeth Barron
* Sean Goggins
* Armstrong Foundjem 

