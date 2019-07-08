from datetime import datetime
import numpy as np

import utils
from issue import Issue


class IssueResponseTimeGithub(Issue):
    """
    Class for Issue Response Time
    """

    def _flatten(self, item):
        """
        Flatten a raw issue fetched by Perceval into a flat dictionary.

        A list with a single flat directory will be returned.
        That dictionary will have the elements we need for computing metrics.
        The list may be empty, if for some reason the issue should not
        be considered.

        :param item: raw item fetched by Perceval (dictionary)
        :returns:   list of a single flat dictionary
        """

        creation_date = utils.str_to_date(item['data']['created_at'])
        if self.since and (self.since > creation_date):
            return []

        if self.until and (self.until < creation_date):
            return []

        # all pull requests are considered to be issues by default.
        # this check removes pull requests from the
        # analysis.
        if 'pull_request' in item['data']:
            return []

        flat = {
            'repo': item['origin'],
            'hash': item['data']['id'],
            'category': "issue",
            'author': item['data']['user']['login'],
            'created_date': creation_date,
            'current_status': item['data']['state']
        }

        member_comments = [comment for comment in item['data']['comments_data']
                           if comment['author_association'] == 'MEMBER']

        flat['issue_resp_time'] = np.NaN if len(member_comments) == 0 \
            else (datetime.now()
                  - utils.str_to_date(
                    min(comment['created_at']
                        for comment in member_comments))) \
            .days

        return [flat]

    def compute(self):
        """
        Compute the average issue response time for all issues
        in the Perceval data.

        :returns avg_issue_resp_time: the average time taken for
        the first comment by a maintainer on an issue.
        """

        avg_issue_resp_time = self.df['issue_resp_time'].mean()
        return avg_issue_resp_time

    def _agg(self, df, period):
        """
        Perform an aggregation operation on a DataFrame to find
        the average response time for issue created in a every
        interval of the period specified in the time_series method,
        like 'M', 'W',etc.

        It computes the mean of the 'issue_res_time' column of the
        DataFrame.

        :param df: a pandas DataFrame on which the aggregation will be
            applied.

        :param period: A string which can be any one of the pandas time
            series rules:
            'W': week
            'M': month
            'D': day

        :returns df: The aggregated dataframe, where aggregations have are the
        so called items
            been performed on the "issue_resp_time" column
        """

        df = df.resample(period).agg({'issue_resp_time': 'mean'})
        df['issue_resp_time'] = df['issue_resp_time'].fillna(0)

        return df


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = utils.read_json_file('../issues.json')
    issue_resp_time = IssueResponseTimeGithub(items)
    print("The average response time of all issues is {:.2f}"
          .format(issue_resp_time.compute()))

    issue_resp_time = IssueResponseTimeGithub(items, (date_since, None))
    print("The average response time of issues created after 2018-09-07 is {:.2f}"
          .format(issue_resp_time.compute()))

    print("The changes in the response time of issues on a monthly basis: ")
    print(issue_resp_time.time_series('M'))
