# Change Request Reviews

### This metric is a release candidate. To comment on this metric please see Issue # [437](https://github.com/chaoss/wg-evolution/issues/437). Following a comment period, this metric will be included in the next regular release.

Question: To what extent are [change requests](https://chaoss.community/metric-change-requests/) put through a formal review process using platform features? 

## Description
Change requests are intended to be reviewed by other community members who assess the quality of the change, ensuring that the change matches project guidelines. Change request reviews may suggest improvements, or changes prior to merging. Software engineering research recognizes the general utility of code reviews for promoting software quality (Baker et al, 1997; Kemerer et al, 2009).  For many projects, successfully merging a change requires that the reviewers sign off on it. This metric assesses the formal review process and identifies how and to what extent change requests are reviewed before they are accepted or declined.  

Change request reviews include top level comments about the entire change request, file level comments asking for specific changes, and whether the change request was “accepted”, “had changes requested”, or the reasoning behind a change request being closed without getting merged. 

Notes:
* Change requests into a repository’s default branch may have different review characteristics than change requests moved into development branches.  
* Change request reviews are implemented in practice in a number of different ways. For example, some projects use change request comments as a form of review, while other projects use more formalized change request review features available on major open source software development platforms. The specific review practices of a project are sometimes documented. 

## Objectives
To understand the nature of change request review practice within a repository, and across a collection of repositories.

Change Request Reviews can help inform the quality of the software and the efficiency of development.

Examining change request review processes and timeliness over time is helpful for characterizing the evolution of an open source software project. 

## Implementation
*The usage and dissemination of health metrics may lead to privacy violations. Organizations may be exposed to risks. These risks may flow from compliance with the GDPR in the EU, with state law in the US, or with other law. There may also be contractual risks flowing from terms of service for data providers such as GitHub and GitLab. The usage of metrics must be examined for risk and potential data ethics problems. Please see [CHAOSS Data Ethics document](https://github.com/chaoss/metrics/blob/main/resources) for additional guidance*.

### Aggregators

* What percentage of Change requests are formally reviewed using platform features? 
* What is the mean and median number of reviews accompanying change requests that are reviewed? 
* What differences in change request review process exist among competing open source projects, and open source projects commonly deployed together? 

### Filters 
* Number of unique [contributors](https://chaoss.community/metric-contributors/) doing reviews
* Bot vs human reviews
* [Change Requests Accepted](https://chaoss.community/metric-change-requests-accepted/)
* [Change Requests Declined](https://chaoss.community/metric-change-requests-declined/)
* [Change Requests Duration](https://chaoss.community/metric-change-requests-duration/)
* [Change Requests Acceptance Ratio]([https://chaoss.community/metric-change-request-acceptance-ratio/](https://chaoss.community/metric-change-request-acceptance-ratio/))
* Is the change request review process documented in a CONTRIBUTING.md file? 
    * Does the project have a CONTRIBUTING.md file?
    * If so, does the CONTRIBUTING.md file contain the word “review”? 
    * Does the project follow these guidelines? (This would require a qualitative review of the document in contrast with observable practice). 
* Time period: Establishing a start and end date for analysis of change request review practices. 



### Tools Providing the Metric 
Augur provides these tables, where review information is stored. In the future, an API will be developed to provide these tables, where review information is stored. 
    * Pull_request_reviews (all reviews on a change request)
    * Pull_request_reviewers (all change request reviewers)
    * Pull_request_review_msg_ref (bridge table for messages from change request reviewers)
    * Messages (change request, issue, email, slack, and change request review messages, and comments) 


### Data Collection Strategies 
* [GitHub API] (https://docs.github.com/en/rest/reference/issues#comments)
* [Gitlab API] (https://docs.gitlab.com/ee/api/notes.html)


## References
* [https://opensource.com/article/19/3/managing-changes-open-source-projects](https://opensource.com/article/19/3/managing-changes-open-source-projects)
* [https://about.gitlab.com/handbook/engineering/infrastructure/change-management/](https://about.gitlab.com/handbook/engineering/infrastructure/change-management/) 
* Baker Jr, Richard A. "Code reviews enhance software quality." _Proceedings of the 19th international conference on Software engineering_. 1997.
* Kemerer, Chris F., and Mark C. Paulk. "The impact of design and code reviews on software quality: An empirical study based on psp data." _IEEE transactions on software engineering_ 35.4 (2009): 534-550

## Contributors
* Kevin Lumbard
* Elizabeth Barron
* Vinod Ahuja
* Sean Goggins
* Enoch Kaxada

***This metric was last reviewed on February 22, 2022 as part of the 2022-04 release.***

