# Reviews_Duration

Duration of the period between the moment a code review starts,
and the moment it is accepted.

## Description

Reviews are defined as in [Reviews](Reviews.md).
Accepted reviews are defined in [Reviews_Accepted](Reviews_Accepted).

The review duration is the duration of the period since the
code review started, to the moment it ended (by being accepted
and being merged in the code base).
This only applies to accepted reviews.

For example, in GitLab a merge request starts when a developer
uploads a proposal for a change in code, opening a merge request.
It finishes when the proposal is finally accepted and merged
in the code base, closing the merge request.

In case there are comments or other events after the code is
merged, they are not consdiered for measuring the duration of
the code review.

### Parameters

Mandatory:

* Period of time. Start and finish date of the period. Default: forever.

    Period during which accepted reviews are considered.
    An accepted review is consdiered to be in the period if
    its creation event is in the period.
    
* Criteria for source code. Algorithm. Default: all files are source code.

    If we are focused on source code, we need a criteria for deciding
    whether a file is a part of the source code or not.

### Aggregators

Usual aggregators are:

* Median. Median (50% percentile) of review duration for all
  accepted reviews in the considered period of time.
  
## Specific description: GitHub

In the case of GitHub, duration is considered for
pull requests that are accepted and merged in the code base.
For an individual pull request, duration starts when it
is opened, and finishes when the commits it includes
are merged into the code base.

### GitHub parameters

None.

## Specific description: GitLab

In the case of GitLab, duration is considered for
merge requests that are accepted and merged in the code base.
For an individual merge request, duration starts when it
is opened, and finishes when the commits it includes
are merged into the code base.

### GitLab parameters

None.

## Specific description: Gerrit

In the case of Gerrit, duration is considered for
code reviews that are accepted and merged in the code base.
For an individual cod review, duration starts when it is opened,
and finishes when the commits it includes
are merged into the code base.

### Gerrit parameters

None.

## Use Cases

* Duration of acceptance of contributions processes.

    Review duration for accepted reviews is one of the indicators
    showing how long does a project take before accepting
    a contribution of code.
    Of course, this metric is not the only one that should be
    used to track volume of coding activity.

## Filters

Usual filters and bucketing are:

* By actors (submitter, reviewer, merger). Requires actor merging
(merging ids corresponding to the same author).

* By groups of actors (employer, gender... for each of the actors).
Requires actor grouping, and likely, actor merging.

## Visualizations

Some useful visualizations are:

* Median per month over time
* Median per group over time

These could be represented as bar charts, with time running in the X axis.
Each bar would represent accepted reviews to change the code
during a certain period (eg, a month).

* Distribution of durations for a certain period

These could be represented with the usual statistical distribution
curves, or with bar charts, with buckets for duration in the
X axis, and number of reviews in the Y axis.

## Reference Implementation

[ To be done. ]

## Known Implementations


## External References (Literature)


