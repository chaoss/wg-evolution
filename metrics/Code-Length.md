# Code Length

Question: How long has the code gotten over time, and have there been efforts to shorten it?


## Description

This metric keeps track of the length of the source code over time.
Length is a combination of line length and total number of lines.
Basically, the number of characters in the code.
The purpose of this metric is to track how long the code has gotten over time,
and see the effects of attempts to shorten the code or make it more efficient.


## Objectives

* Focus on simple, minimal code
    Code that gets too long becomes difficult to understand and fix.
    Code that stays short is easy to fix, change, and adapt.
    The goal is to have shorter, more readable codes, that do one
    job well.


## Implementation

**Aggregators:**
* Count. Total number of characters at a given time.

**Parameters:**
* Point in time. When the measurement occurs.
* Criteria for source code. Algorithm. Default: all files are source code.
 If focused on source code, criteria for deciding whether a file is a part of the source code or not.


### Filters

* By actors (author, committer). Requires actor merging
(merging ids corresponding to the same author).

* By groups of actors (employer, gender...). Requires actor grouping,
and likely, actor merging.

* By [tags](https://www.odoo.com/documentation/13.0/reference/guidelines.html#tag-and-module-name) (used in the message of the commits).
Requires a structure for the message of commits.
This tag can be used in an open-source project to communicate to every contributors
if the commit is, for example, a fix for a bug or an improvement of a feature.

### Visualizations

* Count per month over time

This could be represented as a line graph, with number of characters on the y axis
and time on the x axis.


## References

* https://suckless.org/philosophy/
