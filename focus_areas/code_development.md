# Focus Area: Code Development

Scope: Aspects related to how the source code changes over time, and the mechanisms that the project has to perform and control those changes.

## Goals

* Activity: Learning about activity involved in developing (e.g. adding/changing) code
* Efficiency: Learning how effective new code is merged into the code base
* Quality: Learning about the processes to improve/review quality that are used (for example: testing, code review)

Observations:

* Usually these goals, which in general correspond to the evaluation of some processes,
are considered over a certain time period. Therefore, questions and metrics will also refer, usually,
to time periods.

* Since the focus area is code development, goals (and therefore relevant questions and metrics) are specific for code development. Therefore, any metric related to these goals should be considered as filtering only data relevant to code development (for example, changes only to source code files). In any case, very likely these same goals could be applied to other artifacts (such as documentation) when it is developed in a similar way to the source code.

* For Quality, we assume that there are measurable processes to improve/review quality (testing, code review, etc.). If they don't exist, this goal cannot be satisfied.

## Questions & metrics

\[Work in progress\]

Goal **Activity**:

* Question **Changes**: How many changes are happening to the source code, during a certain time period? 
  * Metric **Code_Changes**(Period): Number of changes to the source code
  (see [Code_Changes](../metrics/Code_Changes.md)).
  * Metric **Code_Changes_Lines**(Period): Aggregated number of lines touched in all changes
  (see [Code_Changes_Lines](../metrics/Code_Changes_Lines.md)).

* Question **Reviews**: How many reviews to proposed changes to the source code
are happening during a certain time period?

  * Metric **Reviews**(Period): Number of new review requests for changes
  to the source code
  (see [Reviews](../metrics/Reviews.md)).

  * Metric **Reviews_Accepted**(Period): Number of reviews for changes
  to the source code that ended accepting the change
  (see [Reviews_Accepted](../metrics/Reviews_Accepted.md)).

  * Metric **Reviews_Declined**(Period): Number of reviews for changes
  to the source code that ended declining the change
  (see [Reviews_Declined](../metrics/Reviews_Declined.md)).


* Question **Issues**: How many issues related to the source code are there
  during a certain time period?

  * Metric **Issues**(Period): Number of new issues related to the source code
  (see [Issues_New](../metrics/Issues_New.md)).
  * Metric **Issues_Active**(Period): Number of issues related to
  the source code that showed some activity during the period
  (see [Issues_Active](../metrics/Issues_Active.md)).
  * Metric **Issues_Closed**(Period): Number of issues related to
  the source code that were closed
  (see [Issues_Closed](../metrics/Issues_Closed.md)).

Goal **Efficiency**:

* Question **Reviews**: How efficient is the project in reviewing proposed
 changes to the code, during a certain time period?

  * Metric **Reviews_Duration**(Period): For how long proposed changes are
  reviewed before they are accepted
  (see [Reviews_Duration](../metrics/Reviews_Duration.md)).
  * Metric **Review_Acceptance**(Period): How many reviews end accepting
  the code change.
  * Metric **Review_Participants**(Period): How many persons participated in
  reviews of code changes.
  * Metric: **Review_Backlog**(Period): How many reviews are still undecided
  (proposed changes were neither accepted nor declined)?
  * Summary metric: **Review_Acceptance_Ratio**(Period): Which fraction of
  new proposals for changes are finally accepted after a review process?
  * Summary metric: **Review_Throughput**(Period): How many proposals for
   changes are decided after code review
   (either accepted or declined) with respect to the number of proposals submitted?
    
* Question **Issues**: How efficient is the project in dealing with issues related to
the source code, for issues proposed during a certain time period?

  * Metric **Issue_Duration**(Period): Time since an issue is proposed until it is closed.
  * Metric **Issue_Participants**(Period): How many persons participated in the discussion
  of issues.
  * Metric: **Issue_Backlog**(Period): How many issues are still open?
  * Summary metric: **Issue_Throughput**(Period): How many issues are closed
  with respect to the number of issues opened?


Goal **Quality**:

* Question **Code_Review**: Which fraction of the code goes through code review?

* Question **Testing**: Which fraction of the code is tested?

## Summary of metrics

This is the list of metrics that we consider as defined,
even when some of them are still work in progress in some details:

Goal | Question | Metric
--- | --- | ---
Activity | Changes | [Code_Changes](../metrics/Code_Changes.md)
Activity | Changes | [Code_Changes_Lines](../metrics/Code_Changes_Lines.md)
Activity | Issues  | [Issues_New](../metrics/Issues_New.md)
Activity | Issues  | [Issues_Active](../metrics/Issues_Active.md)
Activity | Issues  | [Issues_Closed](../metrics/Issues_Closed.md)
Activity | Reviews | [Reviews](../metrics/Reviews.md)
Activity | Reviews | [Reviews_Accepted](../metrics/Reviews_Accepted.md)
Activity | Reviews | [Reviews_Declined](../metrics/Reviews_Declined.md)
Efficiency | Reviews | [Reviews_Duration](../metrics/Reviews_Duration.md)


## Legacy metrics and questions

We're in the process of discussing questions and metrics. Meanwhile, below is the former list of metrics, and their related questions.

Metric | Question
--- | ---
[Pull Requests Merged](../metrics/pull-requests-merged.md) | What is the number of pull requests merged?
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
The name/question pairs have been identified based on CHAOSS-related outreach activities. We thank everyone who participated.

**How to contribute:**
- To advance the document, fork the repo, make your changes and create a pull request.
- To ask questions or make comments open an [issue on GitHub][issue] or join the discussion on the [mailing list or weekly calls](https://chaoss.community/participate/).

[issue]: https://github.com/chaoss/wg-gmd/issues
