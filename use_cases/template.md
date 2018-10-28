# Template for CHAOSS GMD Working Group use cases

To produce a new use case, copy this file,
remove everything above the horizontal rule below,
and fill in everything below the horizontal rule below,
removing lines starting with `Explanation`.

This template is based on the structure of
[SPDX use cases](https://github.com/spdx/spdx-github/wiki/Use-Cases)

---

# Title (name of the use case)

The title should be as terse as possible. It could be the same text
used for the main goal, below (but it could also be a shorter text).

## Description

Explanation: Some lines describing the use case, its context, etc.

## Main goal

Main goal of the use case. In some cases, it could be more than one.
Usually, it will start by "Understanding...", or
"Having data for making informed decissions on...", or
"Tracking...", or something like that.

## Primary actor

The role of the person(s) interested in the use case.

## Stakeholders

List of stakeholders, usually including the primary actor,
and the reason why they have a stake in the use case.

* Stakeholder 1: Reason for having a stake.
* Stakeholder 2: Reason for having a stake.
* ...

## Preconditions

Preconditions, if any, for this case to be meaningful or relevant.

## Questions

These questions should help to fulfill the main goal(s).
Each question will have an identifier (usually one word,
which can be used when describing metrics),
and a text (the question itself).
They should be structured as a list:

* QId1: Question 1
* QId2: Question 2
* ...

## Metrics

Metrics useful in this scenario.
Each metric will have an identifier (which will be a link
to the document with more details on the metric), and a short
description of the metric, and which questions it helps to answer.

* MId1: Description of Metric 1 (QuestionId, QuestionId...)
* MId2: Description of Metric 2 (QuestionId, QuestionId...)
* ...

## Comments

Any other relevant comment. For example, specific threasholds for metrics could be provided, such as "if XXX metric reaches YYY value, the benefits for the project are clear".
