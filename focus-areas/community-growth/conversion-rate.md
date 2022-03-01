### This metric is a release candidate. To comment on this metric please see Issue [#[put the respective Issue Number here]](URL to issue). Following a comment period, this metric will be included in the next regular release. 


# Conversion Rate 

Question: What are the rates at which new contributors become more sustained contributors? 
 

## Description 

The conversion rate metric is primarily aimed at identifying how new community members become more sustained contributors over time. However, the conversion rate metric can also help understand the changing roles of contributors, how a community is growing or declining, and paths to maintainership within an open source community.  

The conversion rate metric can have an impact on diversity, equity, and inclusion by indicating how new members are taking on increasingly signifcant roles in a porject. Diversity, equity, and inclusion can be better understood through the conversion rate metric in knowing how community initiatives and outreach may be  helping or hurting members in becoming more involved. 
 

## Objectives

- Observe if new members are becoming more involved with an open source project  
- Observe if new members are taking on leadership roles within an open source project  
- Observe if outreach efforts are generating new contributors to an open source project 
- Observe if outreach efforts are impacting roles of existing community members 
- Observe if community conflict results in changing roles within an open source community 
- Identify casual, regular, and core contributors  

## Implementation 

### Filters

- Commits  
- Issue creation
- Issue comments
- Change request creation
- Change request comments
- Merged change requests 
- Code Reviews
- Code Review Comments
- Reactions (emoji)
- Chat platform messages
- Maillist messages
- Meetup attendance 

### Visualizations 

![Overall Community Structure](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/community-growth/images/structure.png)

Source: https://chaoss.github.io/grimoirelab-sigils/assets/images/screenshots/sigils/overall-community-structure.png  


![Developer Level](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/community-growth/images/level.png)

Source: https://opensource.com/sites/default/files/uploads/2021-09-15-developer-level-02.png  

### Tools Providing the Metric 

- [GrimoireLab](https://github.com/chaoss/grimoirelab)
- [Augur](https://github.com/chaoss/augur)

### Data Collection Strategies 

The following is an example from the [openEuler](https://www.openeuler.org/en/) community:  

A group of people who attended an offline event A held by the community, can be identified as Group A. Demographic information of Group A could be fetched from an on-line survey when people register for the event. To identify the conversation rate of these participants:

1) Some people from Group A started watching and forking the repos, indicating they have shown some interest in this community. We marked them as subgroup D0 (Developer Level 0) as a subset of Group A.
    - Conversion rate from the total number of people in Group A to the number of people in subgroup D0 is: D0/Group A 

2) Some people from subgroup D0 make more contributions beyond just watching or forking, including creating issues, making comments on an issue, or performed a code review. We marked them as subgroup D1 (Developer Level 1) as a subset of D0.
    - Conversion rate from the total number of people in Subgroup D0 to the number of people in subgroup D1 is: D1/D0. 

3) Some people from subgroup D1 continue to make more contributions, like code contributions, to the project. This could include creating merge requests and merging new project code. We marked them as subgroup D2 (Developer Level 2) as a subset of D1.
    - Conversion rate from the total number of people in subgroup D1 to the number of people in subgroup D2 is: D2/D1. 

![Contributor Funnel](https://github.com/chaoss/wg-evolution/blob/main/focus-areas/community-growth/images/funnel.png)

Definitions:  
- Developer Level 0 (D0) example: Contributors who have given the project a star, or are watching or have forked the repository 
- Developer Level 1 (D1): Contributors who have created issues, made comments on an issue, or performed a code review 
- Developer Level 2 (D2): Contributors who have created a merge request and successfully merged code 
- Conversion Rate (Group A -> D0): CR (Group A -> D2) = D0/Group A 
- Conversion Rate (D0 -> D1): CR (D0 -> D1) = D1/D0 
- Conversion Rate (D1 -> D2): CR (D1 -> D2) = D2/D1 

## References 
- https://opensource.com/article/21/11/data-open-source-contributors
- https://gitee.com/openeuler/website-v2/blob/master/web-ui/docs/en/blog/zhongjun/2021-09-15-developer-level.md  
- https://chaoss.github.io/grimoirelab-sigils/common/onion_analysis/ 
- https://mikemcquaid.com/2018/08/14/the-open-source-contributor-funnel-why-people-dont-contribute-to-your-open-source-project/  

## Contributors 
- Yehui Wang 
- Clement Li 
- zhongjun 
- Xiaoya Xia 
- Matt Germonprez  
- Sean Goggins  
- King Gao  
