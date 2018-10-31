# What is this working group about?

This is a [CHAOSS](https://chaoss.community) working group, 
focused on the [Growth-Maturity-Decline][gmd] metrics category.
Its aim is to coordinate the definition of the metrics, and
the production of software for implementing them, in this area.

[gmd]: gmd_metrics.md

# How to participate

You can start by introducing yourself on the CHAOSS mailing list (see below) explaining your interest.
Then, you can have a look at the archives of the mailing lists, at the minutes of past meetings,
and at the [issues](https://github.com/chaoss/wg-gmd/issues) and
[pull requests](https://github.com/chaoss/wg-gmd/pulls) in
[this repository](https://github.com/chaoss/wg-gmd).

Then, of course you can participate in the mailing list,
in online meetings, and in issues and pull requests.

Currently, main lines of work are:

* [Use cases](use_cases). Proposal and discussion of use cases that help to understand metrics in context.
You can propose your use cases, and/or contribute to refine those that have been proposed already.

* Focus areas (definitions, goals, questions). Currently, in the [definition of GMD metrics] we strucuture
it in the following focus areas: [Issue Resolution](focus_areas/issue_resolution.md), [Code Development](focus_areas/code_development.md), and [Community Growth](focus_areas/communitiy_growth.md).
For each area of interest, we're following the [goal-question-metric methodology](https://en.wikipedia.org/wiki/GQM) defining questions and metrics that help to answer them.
You can contribute by proposing new goals for a focus area, or new questions for learning about those goals,
or new metrics for answering those questions. Or by helping to refine goals, and questions
(see about metrics below).

* Metrics definition. For each metric, we have a document describing it,
all of them in the [metrics directory](metrics).
You can contribute by helping to refine those metrics definitions.

* Reference implementations. For each metric, we intend to produce reference implementations,
in the [implementations directory](implementations).
They are based on data from real data sources,
retrieved using [Perceval](https://github.com/chaoss/grimirelab-perceval).
The idea is to first use a Python notebook to study how to produce the metric, and
all the variations, parameters, etc, that are convenient to have into account.
And then, produce a simple script that will compute the metric from a Perceval dump.
These scripts would be used a reference implementations, both for informing other implementations,
and for ensuring that, if they intend to implement CHAOSS metrics, they produce the same results
on the same data sources.

In any of these subjects, you can propose your ideas by opening an issue,
proposing a pull request, introducing your concerns during a GMD meeting,
or via a message to the mailing list. However, the usual procedure
(meetings and general comments in the mailing list) is as follows:

* If you think something should be done (including a contribution by yourself),
please open an issue in this repository. That will allow others to learn that
you think some work should be done, and can comment on that.
If you intend to do the job yourself, please say that.

* Everyone with an opinion on the matter should comment on the issue,
explaining how they support the idea, propose some change to it,
or think it is not worth / it is not the moment for doing it.

* If comments are positive, and a certain consensus is achieved,
propose a pull request with the changes to the repository
(new document, changes to existing documents).

* Everyone with an opinion on the pulll request should comment on
it, and detailed reviews should be done, maybe asking for new
versions of the pull requet. Once comments and reviews are positive,
the change will be merged in the repository.

* If consensus is not reached at any of these points, or the
process stalls, it can be raised during one of the GMD meetings,
or in the mailing list, to try to unblock it.

* In some specific cases (eg, drafts for use cases), Google Docs
or other means could be used, if that helps newcomers to contribute their ideas.
But this will in general be the exception.

We're also open to discuss the [Definition of GMD itself],
but please refrain from this except that you have very good reasons for that,
just because currently we're focused on the definition of GMD and its refining
in focus areas

For further information on how to collaborate in CHAOSS,
please see the CHAOSS [CONTRIBUTING.md](https://github.com/chaoss/governance/blob/master/CONTRIBUTING.md).
We are committed to providing an inclusive and welcoming environment. Please see our [Code of Conduct.](https://github.com/chaoss/governance/blob/master/code-of-conduct.md)

Find below specific information about our meetings and mailing lists.

## Meetings

We meet every Wednesday at 11am CDT (usually 18:00 CET, but beware different switches to Summer time in EU and US, [check your local time](http://www.thetimezoneconverter.com/?t=11am&tz=Chicago&)) in the CHAOSS Zoom room https://unomaha.zoom.us/j/720431288 (Meeting ID for [dial in](https://unomaha.zoom.us/zoomconference?m=DKGo2mmIuOv9xSjphoGZZmYKxr5HFrS9): 720 431 288)

Usually, we try to make decissions mainly during the last meeting of each month,
so that decisions can be brought when convenient to the monthtly main CHAOSS meeting,
which is the first meeting of each month. In all the meetings we may have an agenda,
but random issues can be raised if time allows, after we're done with the agenda.
Whenever possible, and specially if a decission needs to be made,
ensure that issues / pull requests about the subject matter were opened some time before the meeting,
so that anyone had the opportunity of commenting on them, and make up their mind about that subject matter.

**Exceptions** (these days there will be no meeting): none for now

[Meeting Notes](/meeting_notes.md) are available for past meetings.

## Mailing list

We use the [CHAOSS mailing list](https://chaoss.community/participate/#user-content-join-the-mailing-list).
Please prefix the message subject with \[wg-gmd\] if it is specific to this working group.

# Relationship with the chaoss/metrics repository

This is a repository for the GMD working group.
When this working group decides to "release" a version of its metrics,
the relevant files will be dupmped to the
[chaoss/metrics](https://github.com/chaoss/metrics) repository,
as a pull request for updating the CHAOSS metriccs with
"GMD metrics release x.y".

# Maintainers

- [Jesus M. Gonzales-Barahona](https://github.com/jgbarah)
- [Sean P. Goggins](https://github.com/sgoggins)
