# Focus Area: Code Development

Scope: Aspects related to how the source code changes over time, and the mechanisms that the project has to perform and control those changes.

## Goals

* Activity: Learning about hwo much activity in involved in changing (or adding) code
* Efficiency: Learning how effective new code is merged into the code base
* Quality: Learning about the processes to improve/review quality that are used (for example: testing, code review)

Observations:

* Usually these goals, which in general correspond to the evaluation of some processes,
are consiedered over a certain time period. Therefore, questions and metrics will also refer, usually,
to time periods.

* Since the focus area is code development, goals (and therefore relevant questions and metrics) are specific for code development. Therefore, any metric related to these goals should be considered as fitering only data relevant to code development (for example, changes only to source code files). In any case, very likely these same goals could be applied to other artifacts (such as documentation) when it is developed in a similar way to source code.

* For Quality, we assume that there are measurable processes to improve/review quaitly (testing, code review, etc.). If they don't exist, this goal cannot be satisfied.

## Questions & metrics

\[Work in progress\]

Goal **Activity**:

* Question **Changes**: How many changes are happening to the code base, during a certain time period? 

  * Metric **Changes_No**(Period): Number of changes to the code base
  * Metric **Lines_No**(Period): Number of lines changed in the source code
  * Metric **Change_Size**(Period): Number of lines of changes

* ...

Goal **Efficiency**:

* Question **Proposals**: How efficient is the project in considering proposals for changes, for proposals proposed during a certain time period?

  * Metric **Proposal_Duration**(Period): For how long proposed changes are discussed before they are accepted
  * Metric **Proposal_Acceptance**(Period): How many proposals are finally accepted
  * Metric **Proposal_Participants**(Period): How many 

* ...

Goal **Quality**:

  * ...

## Legacy metrics and questions

We're in the process of discussing questions and metrics. Meanwhile, below is the former list of metrics, and their related questions.

Metric | Question
--- | ---
[Pull Requests Merged](../metrics/pull-requests-merged.md) | What is the number of code commits?
[Lines of Code Changed](../metrics/code-lines-of-code-changed.md) | What is the number of lines of code changed?
[Code Reviews](../metrics/pull-requests-code-reviews.md) | What is the number of code reviews?
[Pull Request Merge Duration](../metrics/pull-requests-merge-duration.md) | What is the duration of time between code merge request and code commit?
[Code Review Efficiency](../metrics/pull-requests-code-reviews-efficiency.md) | What is the number of merged code changes/number of abandoned code change requests?
[Maintainer Response to Merge Request Duration](../metrics/pull-requests-maintainer-response-duration.md) | What is the duration of time for a maintainer to make a first response to a code merge request?
[Code Review Iteration](../metrics/pull-requests-code-reviews-iteration.md) | What is the number of iterations that occur before a merge request is accepted or declined?
[Forks](../metrics/forks.md) | Forks are a concept in distributed version control systems like GitHub. It is a proxy for the approximate number of developers who have taken a shot at building and deploying the codebase *for development*.
[Pull Requests Open](../metrics/pull-requests-open.md) | Number of open pull requests.
[Pull Requests Closed](../metrics/pull-requests-closed.md) | Number of closed pull requests.
[Pull Request Comment Duration](../metrics/pull-requests-comment-duration.md) | The difference between the timestamp of the pull request creation date and the most recent comment on the pull request.
[Pull Request Comment Diversity](../metrics/pull-requests-participants.md) | Number of each people discussing each pull request.
[Pull Request Comments](../metrics/pull-requests-comments.md) | Number of comments on each pull request.

**Disclaimer:**
The name/question pairs listed are not meant to represent a fully comprehensive list. It is expected that this list will evolve as people have insights and thoughts about the name/question pairs that comprise Growth-Maturity-Decline.

**Tooling:**
The name/question pairs are intended to be a starting point for CHAOSS-related software. It is expected that this list will evolve based on the ability (or inability) of software to successfully implement the specific name/question pairs.

**Background:**
The name/question pairs have been identified based CHAOSS-related outreach activities. We thank everyone who participated.

**How to contribute:**
- To advance the document, fork the repo, make your changes and create a pull request.
- To ask questions or make comments open an [issue on GitHub][issue] or join the discussion on the [mailing list or weekly calls](https://chaoss.community/participate/).

[issue]: https://github.com/chaoss/wg-gmd/issues
