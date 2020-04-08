# Forks

Question: How many times was a given repository forked?

## 1. Description
Number of forks on a given repository. 

## 2. Use Cases (Objectives)
We have to distinguish two main use cases for Forks.

1) On GitHub, forks are used in the regular contribution workflow. A developer first needs to fork a repository, before being able to create pull requests. In this use case, forks indicate the level of engagement with developers. These developers belong to the same community and contribute back to the same repository.

2) From a community perspective, forks are the option to develop an alternative version of a software and to build a separate community. A forked community (e.g., LibreOffice forked OpenOffice.org, NextCloud forked OwnCloud) develops it own practices and often does not contribute back. Forks of communities can indicate disagreements over governance but more often are disagreements about the technical future of a project.

## Implementation 
This metric can be implemented by simply counting all of the forks in a given repository. We may also want to count the number of forks that are forked by a single developer vs. the number of forks that are forked by a community/organization. This will count the two separate use cases defined above. If there are a high number of forks by developers, we might determine that the project is rather healthy and is growing, because many developers are forking it, and thus are contributing to it. If there are a high number of forks by organizations, we could determine that there are disagreements between developers about the direction of the project. 

## 3. Sample Filter and Visualization

## 4. Sample Implementation
### GHTorrent: Number of direct forks for each project that is not itself a fork (does not take into account forks of forks)

```SQL
select base_projects.base_project_id, base_projects.name as base_project_name,
base_projects.url as base_project_url, count(forks.id) as num_forks from
(select * from projects) as forks
right join
(select id as base_project_id, name, url from projects
where forked_from is null) as base_projects
on forks.forked_from = base_projects.base_project_id
group by base_projects.base_project_id
```

## 5. Known Implementations

[GHData](https://github.com/OSSHealth/ghdata)

## 6. External References (Literature)
