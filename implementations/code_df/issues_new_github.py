from datetime import datetime

from implementations.code_df.utils import read_json_file
from implementations.code_df.issue_github import IssueGitHub


class IssuesNewGitHub(IssueGitHub):
    """
    Class for Issues New
    """

    def compute(self):
        """
        Compute the number of new issues in the Perceval data.

        :returns new_issues: the number of issues created
        """

        new_issues = len(self.df.index)
        return new_issues

    def _agg(self, df, period):
        """
        Perform an aggregation operation on a DataFrame to find
        the number of issues created in a every interval of the
        period specified in the time_series method, like 'M', 'W',etc.

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

        df = df.resample(period)['category'].agg(['count'])
        return df


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = read_json_file('../issues.json')

    # the GitHub API considers all pull requests to be issues. Any
    # pull request represented as an issue has a 'pull_request'
    # attribute, which is used to filter them out from the issue
    # data.

    items = [item for item in items if 'pull_request' not in item['data']]

    # total new issues
    new_issues = IssuesNewGitHub(items)
    print("The total number of new issues is {:.2f}"
          .format(new_issues.compute()))

    # new issues created after a certain date
    new_issues = IssuesNewGitHub(items, (date_since, None))
    print("The number of issues created after 2018-09-07 is {:.2f}"
          .format(new_issues.compute()))

    # time-series for issues created after a certain date
    print("The changes in the number of issues created on a monthly basis: ")
    print(new_issues.time_series('M'))
