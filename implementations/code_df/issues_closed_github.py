from datetime import datetime

from implementations.code_df.utils import read_json_file, str_to_date
from implementations.code_df.issue_github import IssueGitHub


class IssuesClosedGitHub(IssueGitHub):
    """
    Class for Issues Closed
    """

    def compute(self):
        """
        Compute the number of closed issues in the Perceval data
        for the given period.

        :returns closed_issues: the number of issues closed in the
            given period.
        """

        closed_issues = len(self.df[self.df['current_status'] == 'closed'])
        return closed_issues

    def _agg(self, df, period):
        """
        Perform an aggregation operation on a DataFrame to find
        the number of closed issues which were created in a every
        interval of the period specified in the time_series method,
        like 'M', 'W',etc.

        It computes the count of the 'category' column of the
        DataFrame.

        :param df: a pandas DataFrame on which the aggregation will be
            applied.

        :param period: A string which can be any one of the pandas time
            series rules:
            'W': week
            'M': month
            'D': day

        :returns df: The aggregated dataframe, where aggregations have
            been performed on the "category" column.
        """

        df = df[df['current_status'] == 'closed'].resample(period)['category'].agg(['count'])
        return df

    def _get_params(self):
        """
        Return parameters for creating a timeseries plot

        :returns: A dictionary with axes to plot, a title
            and if use_index should be true when creating
            the plot.
        """

        title = "Trends in Issues Closed"
        x = None
        y = 'count'
        use_index = True
        return {'x': x, 'y': y, 'title': title, 'use_index': use_index}

    def __str__(self):
        return "Issues Closed"


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = read_json_file('../issues_events.json')

    # the GitHub API considers all pull requests to be issues. Any
    # pull request represented as an issue has a 'pull_request'
    # attribute, which is used to filter them out from the issue
    # data.

    items = [item for item in items if 'pull_request' not in item['data']]

    # total closed issues
    issues = IssuesClosedGitHub(items)
    print("The total number of closed issues is {:.2f}"
          .format(issues.compute()))

    # closed issues created after a certain date, considering reopened issues
    # as new
    issues = IssuesClosedGitHub(items, (date_since, None), reopen_as_new=False)
    print("The number of issues closed after 2018-09-07, considering reopened issues"
          " as new, is {:.2f}"
          .format(issues.compute()))

    # time-series for closed issues created after a certain date
    print("The changes in the number of issues closed on a monthly basis: ")
    print(issues.time_series('M'))
