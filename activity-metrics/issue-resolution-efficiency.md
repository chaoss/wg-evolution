# Issue Resolution Efficiency

## 1. Description
What is the number of closed issues/number of open issues?

## 2. Use Cases
* A project interested in knowing if they are coping well or not
with the issues being open, and how that evolves over time.
This metric informs them exactly about that.
If there are more issues being opened that issues being closed
during a long period of time, the number of unresolved issues is going to grow.

## 3. Formula
The definition is for a time period (for example, for a certain month):

**Definitions:**

* `issues_closed`: Total number of issues closed during the period
* `issues_opened`: Total number of issues opened during the period
* `issues_backlog`: Total number of issues open at the beginning of the period (backlog of open issues)

**Formula:** 'issues_closed / (issues_opened + issues_backlog)'

**Interpretation:**

* The closer to 1, the less bugs remaining open at the end of the period
(the project is coping well with pending work).
* The closer to 0,
the more bugs remaining open (the project is not coping well with pending work).
* If the number remains stable over time,
the project is closing issues at about the same pace
(relative to the pending work).
* If the number decreases,
the project is closing less stuff than it should be closing...

**Comments:**

The metric is built in a way that the the chances of the denominator being 0
is minimized. Only if the project has no backlog of open issues, and there
are no new issues open during the period, the denominator will be 0.
But in that case, there will be also no closed issues during the period,
and therefore the metric will be 0/0, which we could assimilate to 0.

We're not using "issues resolved" instead of issues closed, because in many cases
we don't have that data. When it is available (eg, in those cases when
there is a state "Resolved"), a more specific metric could be defined.
Or that could be used as a filter.

## 4. Sample Filter and Visualization
Include a Sample Filter and Visualization (screenshot) of the metric from any implementation. TBD.

## 5. Sample Implementation
An example implementation, for example a SQL or Elasticsearch query. TBD

## 6. Known Implementations
Examples of where and how metric is used. (include links to dashboard or location where metric is visible or is talked about having been used). TBD

## 7. Test Cases (Examples)
Sample inputs (including contexts) and expected outputs for this metric. Implementers can test their implementations against these test cases. For quantitative metrics, this could include a static repository with known metric results, or just inputs and output. For qualitative metrics, this may be more difficult. TBD.

## 8. External References (Literature)
Blog posts, websites, academic papers, or books that mention the metric. TBD.
