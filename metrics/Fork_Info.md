# {Analysis of Forks}

Question: How many forks have been made of a given repository in a specified time period.

## Description
A fork of a repository/project is fairly self-explanitory, it is when a user creates a new fork (on github) of a repository/project. More specifically, it is when a user creates a "copy" of a repository/project to be able to create and change different files to that repository/project.

## Objectives
A measure of the amount of new contributors. Counting the number of new forks of repositories/projects are a good way to tell that new people are picking up the repository/project and adding it to work on. This is not a full-proof method, it is merely one dataset to derive new interest in a repository/project.

## Implementation
**Aggregators**
* Count the number of new forks of a repository

**Parameters**
* Date/Time Interval. Start and finish time period. Default: All-time. Period in which number of forks are considered.
* First forking. Boolean value (T/F). Default: F. Boolean value to give consideration to the first time that a project is forked.

### Filters (optional)
* By actors. Must match ID of the actors to create datasets based off of individuals.
* By repository/project. Must match the ID of each repository as to not allow data crossover between multiple datasets.

### Visualizations (optional)
* Bar Graph (x = time period, y = number of forks)
* Line Graph (x = time period, y = number of forks)
\nvizualization link- (https://github.com/JosephBurris/jpb68d/blob/master/Assignment_11/metric_visualization.png)

### Tools Providing the Metric (optional)
(TBD)

### Data Collection Strategies (Optional)
* Github (specifics TBD)

## References
(TBD)
