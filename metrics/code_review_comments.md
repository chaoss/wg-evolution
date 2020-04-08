Code Review Comments by Jonah Marz

Question: What comments were posted on a given code review on a repository?

## Description
This metric is meant to be used on Code Review comments for pull requests on github. This is meant to store comments for every code review of a given repository. 

## Objectives
Knowing comments that are attached to a given code review can give an overall feeling or attitude attached to a given code review. It also can show how much interest was given on a particular code review based on how many comments there are. 

## Implementation
We can look at a given code review of a repository and then measure the amount of comments on that review and store the text data of the comments in order to be able to display them. This metric would more be up to the user to interpret the comments themselves unless we wanted to put some sort of language processing involved to get the idea of a comment.

### Tools Providing the Metric
The github api can look at comments for a repository. That documentation is listed here https://developer.github.com/v3/pulls/comments/.

### Data Collection Strategies (Optional)
In my opinion the best way to collect the data would be use the github api to get the comments for code reviews on github, and then use a simple MySQL function to count the amount of comments per code review. 

## References
Here is a reference page to code reviews on github which also talks about comments 
https://github.com/features/code-review/
