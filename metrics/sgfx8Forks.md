# Forks

Question: How many forks of the repository were made during a specified period?

## Description
This is the number of forks, or copies, made of a specified repository. 

## Objectives
By forking a repository, one is then able to freely work and make changes to a project without affecting the original. By monitoring
the number of forks made to a repository, we are able to see how many people are using the repository, how many people are making edits to possibly propose
a change or using the project for a personal project. 

## Implementation
Aggregators:  
Count the total number of changes during the specified period. 

Parameters: 
Period of time, including the start and end date or set the period of time to indefinite. 
What repository is being monitored. 


### Filters 
By users, who forked the repository. 
By groups of users, who forked the repository given a shared characteristic. 

### Visualizations (optional)
Count per week over a specified time represented by a bar chart. 
Count per month over a specified time represented by a bar chart. 
Count per group over a specified time represented by a bar chart. 

## References
Used as a guide for creating this metric: https://github.com/chaoss/wg-evolution/blob/master/metrics/Code_Changes.md 
To learn more about forking a repository: https://help.github.com/en/enterprise/2.13/user/articles/fork-a-repo
