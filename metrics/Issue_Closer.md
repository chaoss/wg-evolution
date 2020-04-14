# Issue Closers

Question: Who is closing the issues?

## Description
This metric will answer the question as to who closed an issue, how many they have closed, and what issues were closed.


## Objectives
This metric is necessary due to problems of someone closing an issue they thought was resolved, and then someone revisits this issue and see the issue is in fact unresolved, and be able to contact the closer and see why they closed it prematurely, or why they thought the issue was completed.

This metric can also allow users to monitor someone who may be closing a large amount of issues within a short amount of time, which can raise some questions that contributors may want to contact the closer about.
## Implementation

**Aggregators:**
* Max - find user that closed the most issues of said repo.
* Average - find average of issues closed by user

### Filters (optional)
* Date - how many issues user closed in a specific timeframe
* Repo (optional) - find specific closed issues of a repo from repo group


## References
https://help.github.com/en/github/managing-your-work-on-github/deleting-an-issue
