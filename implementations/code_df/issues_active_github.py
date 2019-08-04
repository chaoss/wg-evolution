from datetime import datetime
import pandas as pd

from implementations.code_df.utils import read_json_file, str_to_date
from implementations.code_df.issue_github import IssueGitHub


class IssuesActiveGitHub(IssueGitHub):
    """
    Class for Issues Active
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
        updation_date = str_to_date(item['data']['updated_at'])

        # considering only those issues who were updated
        # within the given period

        if self.since and (self.since > creation_date) \
                and (self.since > updation_date):
            return []

        if self.until and (self.until < creation_date) \
                and (self.until < updation_date):
            return []

        flat = {
            'repo': item['origin'],
            'hash': item['data']['id'],
            'category': "issue",
            'author': item['data']['user']['login'],
            'created_date': creation_date,
            'current_status': item['data']['state'],
            'updated_date': updation_date
        }

        return [flat]

    def compute(self):
        """
        Compute the number of active issues in the Perceval data.

        :returns active_issues: the number of issues created
        """

        active_issues = len(self.df.index)
        return active_issues

    def _agg(self, df, period):
        """
        Perform a count operation on a DataFrame to find
        the number of active issues in a every interval of the
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

        :returns df: The DataFrame representing the number of active
            issues in a given period.
        """

        resampled_items = df.resample(period)

        df = pd.DataFrame(columns=['count'])
        for item in resampled_items.__iter__():
            group_end_date = item[0]
            group_df = item[1]

            # considering only those issues that were
            # updated within the same period
            group_df = group_df[group_df['updated_date'] <= group_end_date]
            df.loc[group_end_date] = len(group_df.index)

        return df


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = read_json_file('../issues.json')

    # the GitHub API considers all pull requests to be issues. Any
    # pull request represented as an issue has a 'pull_request'
    # attribute, which is used to filter them out from the issue
    # data.

    items = [item for item in items if 'pull_request' not in item['data']]

    # total active issues
    active_issues = IssuesActiveGitHub(items)
    print("The total number of new issues is {:.2f}"
          .format(active_issues.compute()))

    # active issues created after a certain date
    active_issues = IssuesActiveGitHub(items, (date_since, None))
    print("The number of issues created after 2018-09-07 is {:.2f}"
          .format(active_issues.compute()))

    # time-series for issues created on a monthly basis
    print("The changes in the number of issues created on a monthly basis: ")
    print(active_issues.time_series('M'))
