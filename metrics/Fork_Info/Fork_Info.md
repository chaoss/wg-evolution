# {Forks}

Question: How many forks have been made of a given repository in a specified time period.

## Description
A description of what the metric is and what it captures.
The first few sentences should match the description in the [metrics list](../activity-metrics-list.md).

A fork of a repository/project is fairly self-explanitory, it is when a user creates a new fork (on github) of a repository/project. More specifically, it is when a user creates a "copy" of a repository/project to be able to create and change different files to that repository/project.

## Objectives
Answer the question for why someone wants to measure this metric and what can be known with it.

A measure of the amount of new contributors. Counting the number of new forks of repositories/projects are a good way to tell that new people are picking up the repository/project and adding it to work on. This is not a full-proof method, it is merely one dataset to derive new interest in a repository/project.

## Implementation
Provide details on how to measure the metric, collect the data, and analyze it. The following sub-headings are optional but help to structure the different aspects of implementation.

Aggregators:
- Count the number of new forks of a repository

Parameters:
- Period of time. Start and finish time period. Default: All-time. Period in which number of forks are considered.
- First forking. Boolean value (T/F). Default: F. Boolean value to give consideration to the first time that a project is forked.

### Filters (optional)
Include a Filter

- By actors. Must match ID of the actors to create datasets based off of individuals.
- By repository/project. Must match the ID of each repository as to not allow data crossover between multiple datasets.

### Visualizations (optional)
Include visualizations such as screenshot of the metric. There may be many more visualizations for this metric, we only want to provide a flavor for what this metric is about.

- Bar Graph (x = time period, y = number of forks)
- Line Graph (x = time period, y = number of forks)
Screenshot included in folder.

### Tools Providing the Metric (optional)
Metric must be currently deployed/available, in contrast to a tool having the "potential" to provide the metric. Provide direct link to implementation/documentation, if applicable

### Data Collection Strategies (Optional)
If there are several different ways to collect data for this metric, list them here.
This may include expressing a metric in different ways.

## References
Blog posts, websites, academic papers, or books that mention the metric and provide more background.
