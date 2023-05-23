# Contribution Attribution

Question: Who has contributed to an open source project and what attribution information about people and organizations is assigned for contributions?

## Description
This metric evaluates who has worked on the project and specific project tasks and provides the attribution to  project contributors and affiliated organizations.  The aim is to understand, through insights into the paid contribution dynamics of a community, “how the work gets done.”

## Objectives
1. Who is working on the project?
2. What is the ratio of volunteer work, sponsored work, and blended work?
3. How many contributions are sponsored?
4. Who is sponsoring the contributions?
5. What [types of contributions](https://chaoss.community/metric-types-of-contributions/) are sponsored?
6. [How diverse is the community of contributors working on a project?](https://github.com/chaoss/wg-diversity-inclusion/tree/master/demographic-data)

## Implementation

Most contributions can be implicitly attributed using trace data, and these attributions are reflected in other metrics. However, this metric relies heavily on data that is volunteered by contributors and interpreted by project leadership. The implementation of this metric demands that the human in the loop determine what organizations, and what individual contributors a contribution is attributed to. Each individual contributor should be offered the opportunity to indicate what firm, foundation, project, and/or client paid for a particular change.

### Filters

* [Type of Contributor (individual, organization, gender, race, global status, work location)](https://chaoss.community/metric-contributors/)
    * Volunteer
    * Sponsored by a firm and/or client
    * [Role](https://www.drupal.org/project/drupalorg/issues/3214849) that a contributor plays on a project (i.e., maintainer, board member, etc.)
* [Type of Contribution](https://chaoss.community/metric-types-of-contributions/)
    * Links to contribution artifacts, like merge requests, issues, and the like, where relevant.
    * Indication of contribution types not managed in Git platforms like GitHub, GitLab, and BitBucket.
    * See also: https://chaoss.community/metric-types-of-contributions/
* Volunteer versus sponsored - Related to [Organizational Diversity](https://chaoss.community/metric-organizational-diversity/)and[Labor Investment](https://chaoss.community/metric-labor-investment/)

### Visualizations

![Contributions by Volunteer vs Sponsored](https://raw.githubusercontent.com/chaoss/wg-evolution/main/focus-areas/community-growth/images/contributions-by-volunteer-vs-sponsored.png)

![Contributions by Gender](https://raw.githubusercontent.com/chaoss/wg-evolution/main/focus-areas/community-growth/images/contributions-by-gender.png)

### Tools Providing the Metric

1. The Drupal community built this tool, began using it in [2015](https://www.drupal.org/blog/who-sponsors-drupal-development), and has been reporting their results [annually](https://dri.es/who-sponsors-drupal-development-2020)
2. There is an [issue open with GitLab](https://gitlab.com/gitlab-org/gitlab/-/issues/327138) to implement this functionality

### Data Collection Strategies
The Drupal Community implemented an example of how to gather information necessary for this metric to be calculated. It associates individuals, and organizations those individuals indicate as warranting attribution, for each discrete contribution.

### Data Ethics Considerations
Although this metric requires the capture of a relationship between individuals and the contributions they make, the intent of this metric is NOT to measure individuals. The aim is to enable a wider understanding of how contributions to this project are motivated. Explicitly, it is not the intent of this metric to contribute to gamification of individual contributor work.

## References
* https://dri.es/a-method-for-giving-credit-to-organizations-that-contribute-code-to-open-source
* https://www.drupal.org/blog/who-sponsors-drupal-development
* https://dri.es/who-sponsors-drupal-development-2020
* https://gitlab.com/gitlab-org/gitlab/-/issues/327138

## Contributors
* Matthew Tift
* Sean Goggins
* Elizabeth Barron
* Vinod Ahuja
* Armstrong Foundjem
* Kevin Lumbard
