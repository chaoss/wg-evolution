# Code contributions by new contributors

## Description

This use case deals with how a project deals with new contributors of code.
First-time contributors could be easily discouraged if no one reviews or acknowledges
their work in a timely manner.

## Main goals

Understanding how a project deals with first code contributions by newcomers.

Having data for tracking the onboarding process for new code contributors,
and making informed decisions on improving it.

## Vocabulary

* Contribution: proposal to change the source code of a project.
The change may fix some bug, add some new functionality, etc.
For this use case, code contributions will be understood as
commits to the source code of the project.
Note that the contribution is considered when it is submitted:
it may happen that the contribution is not accepted.

* Contributor: person contributing one or more code contributions to the project.

* New contributor: code contributor who has submitted for the first time one,
or a very small number of code contributions, during a small period of time.

* Experienced contributor: code contributor who has submitted a large number of contributions
over a long period of time.

Both new contributors and experienced contributors are defined
with respect to a certain time moment. A contributor who is new on January 1st 2010
could be an experienced contributor in July 1st 2014.

Specific definitions of new contributors and experienced contributors
will be needed to operationalize metrics, such as "contributors in their first six months after their first contribution",
or "contributor who is a part of the team producing 80% of the changes during a period of six months".

## Primary actor

Person responsible for the onboarding process of the project.

## Stakeholders

* Community manager for the project, for tracking how the onboarding process is performing.

* Project community in general, for self-awareness about how the onboarding
process is performing.

* Prospective contributors, to make decisions on whether to
invest their time and effort in joining a community,
or in general, produce contributions for the project.

## Preconditions

* The project should have an interest in new people joining as code contributors.
* The project should have a certain history of new contributors,
for the data to be meaningful.

## Questions

* FractionAccepted:
What fraction of contributions by new contributors is accepted?

* FractionAcceptedCompared:
What fraction of contributions from new contributors are accepted versus contributions from experienced developers?

* ResolutionPeriod:
How long does it take (e.g. average or median) for contributions by new contributors to be resolved (e.g. accepted or declined)?
    
* ResolutionPeriodCompared:
How long does it take for contributions by new contributors to be resolved
with respect to contributions from experienced developers?

* AckPeriod: 
How long does it take (e.g. average or median) for contributions by new contributors to be responded (e.g. acknowledged, got first review, etc.)?

* AckPeriodCompared:
How long does it take for contributions by new contributors to be responded
with respect to contributions from experienced developers?

* AcceptanceEffect:
Does the acceptance of contributions by new contributors have an effect
on future contributions when they are no longer new contributors?

* AckEffect:
Does the responsiveness to contributions by new contributors have an effect
on future contributions when they are no longer new contributors?

## Metrics

\[Work in progress\]

> Metrics useful in this scenario.
> Each metric will have an identifier (which will be a link
> to the document with more details on the metric), and a short
> description of the metric, and which questions it helps to answer.

> * MId1: Description of Metric 1 (QuestionId, QuestionId...)
> * MId2: Description of Metric 2 (QuestionId, QuestionId...)
> * ...

[Change proposals](TODO).
Change proposals for source code files can be used as a proxy for code contributions proposed.
When filtered by new committers, it will give proposals by new contributors.
Change proposals could be pull requests (GitHub), merge requests (GitLab), patches (Gerrit), etc.
Question ids:
* FractionAccepted: implemented as
Change proposals (accepted, for new developers) / Change proposals (accepted, for all developers)



## Comments

This use case is focused on code contributions,
even when there are many other important kinds of contributions
to a project.
