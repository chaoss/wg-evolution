# Branch Lifecycle

Question: How do projects manage the lifecycle of their version control branches?

## Description
This metric makes the lifecycle of version control branches visible. A branch lifecycle includes acts of branch creation and deletion, as well as persistence of version control branches. When writing code, a development team may create multiple branches, focused around specific features. Subsequently, those branches may be merged into more persistent branches, such as the main branch of a repository. Some branches persist for the life of the repository, while others are deleted after code is merged into a more persistent branch.  By understanding these patterns, we can learn how branch creation, destruction, and merging reflect the development practices of a particular project.  A repository’s typical branch lifecycle and management approach can be used to help identify a project’s repository management style.

## Objectives
This metric’s objective is to increase the visibility of a repository’s volume and frequency of branch creation and deletion, as well as persistence of version control branches, in the context of other project characteristics. In turn, this helps potential contributors understand how to initiate and sustain participation in a project. This metric may help  potential contributors understand how to initiate and sustain participation in a project. Questions that can be addressed through this metric include:
- How many branches have been merged but not deleted?
- How long has a branch been merged and not deleted?
- How many branches have existed longer than a certain number of days, months, or years?
- How often do projects or repositories create branches?
- In the aggregate, how long do branches usually live?
- How can we distinguish between branch “death” (i.e., never intended to be used again; deletion) or branch “dormancy” (i.e., inactive for long periods of time, but may be used again) in cases where branches are infrequently deleted in a repository?

## Implementation
The stated advice regarding management of the branch lifecycle  for a project may be visible in a CONTRIBUTING.md document, and these documents can be compared across repositories using linguistic analysis, and contrasted with data derived from actual project practices to draw insights within, and across repositories. In most cases, however, the data we focus on in this metric is quantitative in nature.

**Aggregators:**
- Count of branches created.
- Count of branches deleted.
- Count of branches merged.
- Count of branches abandoned (had unique commits, but never got merged before it was deleted)
- Total count of branches.
- Average age of open branches.
- Rate/ratio at which branches are created vs. deleted.


**Parameters:**
- Period of time. Start and finish date of the period. Default: forever.
- Period during which change requests are considered.


### Filters (optional)
- Collections of repositories
- Default branch name versus descriptive name with regard to branch persistence

### Tools Providing the Metric (optional)
Metric must be currently deployed/available, in contrast to a tool having the "potential" to provide the metric. Provide direct link to implementation/documentation, if applicable

Augur Community Reports (https://github.com/chaoss/augur-community-reports)

### Data Collection Strategies (Optional)

*Specific description: Git*

Git branching data exists at several different levels in a version control ecosystem, usually both locally on a developer’s machine as well on a hosted platform like GitHub or BitBucket. This branch data on the hosted platform may also differ from each developer’s machine, and additionally, different developers may have different branch data on their machine even for the same repository.

In the specific case of Git, a significant amount of additional complexity is introduced due to Git’s design as a distributed version control system, which means that Git allows multiple remotes for a single repository (for example, a user’s fork at github.com/user/project and the upstream version at github.com/chaoss/project). More often than not, many individual contributors may work in the same branch locally, and push changes to the remote repository. The local copies, therefore, will sometimes be different than the remote, hosted internally or on platforms like GitHub, GitLab, and BitBucket., since they’re likely either being managed by different people (likely with different branching styles) or they are both being used by one person to “silo” the work they are doing.

Data about Git branches can be derived from a Git log directly, or through a Git platform’s API.

Is picking a “canonical” version of the repo for branching data is useful? This gives a meaningful base for comparing between instances of the repo with different data. Could also prove to

`git branch -a` will list all existing branches.


## References
Blog posts, websites, academic papers, or books that mention the metric and provide more background.

Adopting a Git Branching Strategy: https://docs.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops

Choose the Right Git Branching Strategy: https://www.creativebloq.com/web-design/choose-right-git-branching-strategy-121518344      

The Effect of Branching Strategies on Software Quality  by Emad Shihab, Christian Bird, and Thomas Zimmermann
https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/shihab-esem-2012.pdf

OpenStack: 
https://docs.openstack.org/project-team-guide/other-branches.html
