# What is this working group about?

![banner](~/Desktop/icon.png)

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

## Introduction

_Growth, Maturity and Decline_ is a working group focused on the lifecycle of open source projects. We do not valence the stages, but seek to build awareness of those stages among consumers of these metrics. Decline can be ok when a project's utility is waning; or terrible if 20% of the entire internet relies on that project. Context matters, and we are not the arbiters of your context. The "valence" of "good/bad" emerges from use cases and YOUR context.

This is a [wg-diversity-inclusion](https://chaoss.community) working group, focused on the [Growth-Maturity-Decline][gmd] metrics category. Its aim is to coordinate the definition of the metrics, and the production of software for implementing them, in this area.

This group meets every Wednesday at 11am CST. [Connection Information and minutes from previous meetings are located here.](./meeting_notes.md)

Focus areas for this working group include metrics related to ;
1. Growth Maturity and Decline
  * [Code Code Development](./focus_areas/code_development.md)
  * [Community Growth](./focus_areas/community_growth.md)
  * [Issue Resolution](./focus_areas/issue_resolution.md)
2. [Risk](./focus_areas/risk/risk.md)
3. [Value](./focus_areas/value/value.md)

[gmd]: gmd_metrics.md


## Table of Contents

- [Background](#background)
- [Usage](#usage)
- [Upcoming meetings](#meetings) 
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)


## Join our Mailing List
* We use the [CHAOSS mailing list](https://chaoss.community/participate/#user-content-join-the-mailing-list).
Please prefix the message subject with \[wg-gmd\] if it is specific to this working group.

## How to participate

You can start by introducing yourself on the CHAOSS mailing list (see below) explaining your interest. Then, you can have a look at the archives of the mailing lists, at the minutes of past meetings, and at the
- [issues](https://github.com/chaoss/wg-gmd/issues) and
- [pull requests](https://github.com/chaoss/wg-gmd/pulls) in
- [this repository](https://github.com/chaoss/wg-gmd).

Then, of course you can participate in the mailing list, in online meetings, and in issues and pull requests. [Mailing lists can be subscribed to here.](https://lists.linuxfoundation.org/mailman/listinfo/chaoss)

Currently, main lines of work are:

* [Use cases](use_cases). Proposal and discussion of use cases that help to understand metrics in context.
You can propose your use cases, and/or contribute to refine those that have been proposed already.

* Focus areas (definitions, goals, questions). Currently, in the [definition of GMD metrics] we strucuture
it in the following focus areas: [Issue Resolution](focus_areas/issue_resolution.md), [Code Development](focus_areas/code_development.md), and [Community Growth](focus_areas/communitiy_growth.md).

For each area of interest, we're following the [goal-question-metric methodology](https://en.wikipedia.org/wiki/GQM) defining questions and metrics that help to answer them.

You can contribute by proposing new goals for a focus area, or new questions for learning about those goals,
or new metrics for answering those questions. Or by helping to refine goals, and questions.




TODO: Fill out a short section that links to D&I metrics repo and explains how this repo fits into overall CHAOSS metrics effort.
[D&I](https://github.com/chaoss/wg-diversity-inclusion)



## Background
* Background - A lot of the current content at the top of the repo will be moved here and expanded on.



## Usage
* Provisionary Repository structure 
```
/wg-gmd
├── LICENSE
├── README.md
├── contributing.md
├── focus_areas
│   ├── code_development.md
│   ├── community_growth.md
│   ├── issue_resolution.md
│   ├── risk
│   │   └── risk.md
│   ├── templates
│   │   └── question_template
│   └── value
│       └── value.md
├── gmd_metrics.md
├── implementations
│   ├── Code_Commits.ipynb
│   ├── README.md
│   └── git-commits.json
├── meeting_notes.md
├── metrics
│   ├── archived_metrics
│   │   ├── apache-maturity-model.md
│   └── template_folder
│       ├── A-example-template.md
├── repo_structure.md
└── use_cases
    ├── README.md
    └── template.md
```

## Upcoming meetings
* We meet every Wednesday at 11am CDT (usually 18:00 CET, but beware different switches to Summer time in EU and US, [check your local time](http://www.thetimezoneconverter.com/?t=11am&tz=Chicago&)) in the CHAOSS Zoom room https://unomaha.zoom.us/j/720431288 (Meeting ID for [dial in](https://unomaha.zoom.us/zoomconference?m=DKGo2mmIuOv9xSjphoGZZmYKxr5HFrS9): 720 431 288)

Usually, we try to make decissions mainly during the last meeting of each month,
so that decisions can be brought when convenient to the monthtly main CHAOSS meeting,
which is the first meeting of each month. In all the meetings we may have an agenda,
but random issues can be raised if time allows, after we're done with the agenda.
Whenever possible, and specially if a decission needs to be made,
ensure that issues / pull requests about the subject matter were opened some time before the meeting,
so that anyone had the opportunity of commenting on them, and make up their mind about that subject matter.

**Exceptions** (these days there will be no meeting): none for now

[Meeting Notes](/meeting_notes.md) are available for past meetings.


## Contributing
* You can start by introducing yourself on the CHAOSS mailing list (see below) explaining your interest. Then, you can have a look at the archives of the mailing lists, at the minutes of past meetings, and at the
- [issues](https://github.com/chaoss/wg-gmd/issues) and
- [pull requests](https://github.com/chaoss/wg-gmd/pulls) in
- [this repository](https://github.com/chaoss/wg-gmd).

Then, of course you can participate in the mailing list, in online meetings, and in issues and pull requests. [Mailing lists can be subscribed to here.](https://lists.linuxfoundation.org/mailman/listinfo/chaoss)

Currently, main lines of work are:

* [Use cases](use_cases). Proposal and discussion of use cases that help to understand metrics in context.
You can propose your use cases, and/or contribute to refine those that have been proposed already.

* Focus areas (definitions, goals, questions). Currently, in the [definition of GMD metrics] we strucuture
it in the following focus areas: [Issue Resolution](focus_areas/issue_resolution.md), [Code Development](focus_areas/code_development.md), and [Community Growth](focus_areas/communitiy_growth.md).

For each area of interest, we're following the [goal-question-metric methodology](https://en.wikipedia.org/wiki/GQM) defining questions and metrics that help to answer them.

You can contribute by proposing new goals for a focus area, or new questions for learning about those goals,
or new metrics for answering those questions. Or by helping to refine goals, and questions.

 [the contributing file](contributing.md)!

PRs accepted.

## Relationship with the chaoss/metrics repository

This is a repository for the GMD working group.
When this working group decides to "release" a version of its metrics,
the relevant files will be dupmped to the
[chaoss/metrics](https://github.com/chaoss/metrics) repository,
as a pull request for updating the CHAOSS metriccs with
"GMD metrics release x.y".


## Maintainers

- [Jesus M. Gonzales-Barahona](https://github.com/jgbarah)
- [Sean P. Goggins](https://github.com/sgoggins)

## License
- MIT License 
Copyright © 2018 CHAOSS Projects See attached file LICENSE.md
