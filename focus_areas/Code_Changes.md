# Code_Changes

Changes to the source code during a certain period.

## 1. Description

These are changes to the source code during a certain period.
For "change" we consider what developers consider an atomic change to their code.
In other words, a change is some change to the source code which usually
is accepted and merged as a whole, and if needed, reverted as a whole too.
For example, in the case of git, each "change" corresponds to a "commit",
or, to be more precice, "code change" corresponds to the part of a commit which
touches files considered as source code.

### Parameters

Mandatory:

* Period of time. Period during which changes are considered.
* Criteria for source code. Which criteria is used for deciding a file is a source code file.

### Aggregators

Usual aggregators are:

* Number. Total number of changes during the period.
* Mean. Mean number of changes during the period.
* Median. Median number of changes during the period.

### Git Case

In the cases of git, a code change is defined as the part of
a git commit that "touches" a source file.
That is, for each git commit, only the part related to
deletions or additions of lines to files that are considered source code
will be considered as the code change.

The date of a change can be defined (for considering it in a period or not)
as the author date or the commiter date of the corresponding git commit.

#### Parameters

Mandatory:

* Kind of date. Either author date or committer date, used for deciding if
a commit happens during a period.

## 2. Use Cases

## 3. Sample Filter and Visualization

## 4. Sample Implementation

## 5. Known Implementations

## 6. External References (Literature)
