from datetime import datetime

from implementations.code_df.utils import read_json_file, str_to_date
from implementations.code_df.issue_github import IssueGitHub


class IssuesClosedGitHub(IssueGitHub):
    """
    Class for Issues Closed
    """

    def _flatten(self, item):
        """
        Flatten a raw issue fetched by Perceval into a flat dictionary.

        A list with a single flat directory will be returned.
        That dictionary will have the elements we need for computing metrics.
        The list may be empty, if for some reason the commit should not
        be considered.

        :param item: raw item fetched by Perceval (dictionary)
        :returns:   list of a single flat dictionary
        """

        creation_date = str_to_date(item['data']['created_at'])

        if self.since and (self.since > creation_date):
            return []

        if self.until and (self.until < creation_date):
            return []

        flat = {
            'repo': item['origin'],
            'hash': item['data']['id'],
            'category': "issue",
            'author': item['data']['user']['login'],
            'created_date': creation_date,
            'current_status': item['data']['state'],
        }

        if flat['current_status'] is not 'closed':
            return []

        return [flat]

    def compute(self):
        """
        Compute the number of closed issues in the Perceval data
        for the given period.

        :returns closed_issues: the number of issues closed in the
            given period.
        """

        closed_issues = len(self.df.index)
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

    # total closed issues
    new_issues = IssuesClosedGitHub(items)
    print("The total number of closed issues is {:.2f}"
          .format(new_issues.compute()))

    # closed issues created after a certain date
    new_issues = IssuesClosedGitHub(items, (date_since, None))
    print("The number of issues closed after 2018-09-07 is {:.2f}"
          .format(new_issues.compute()))

    # time-series for closed issues created after a certain date
    print("The changes in the number of issues closed on a monthly basis: ")
    print(new_issues.time_series('M'))
