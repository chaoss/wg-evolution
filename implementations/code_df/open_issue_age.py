from datetime import datetime

import utils
from issue import Issue


class OpenIssueAge(Issue):
    """
    Class for Age of Open Issues
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

        flat = {
            'repo': item['origin'],
            'hash': item['data']['id'],
            'category': "issue",
            'author': item['data']['user']['login'],
            'created_date': creation_date,
            'current_status': item['data']['state']
        }

        if flat['current_status'] == 'open':
            flat['open_issue_age'] = \
               (datetime.now() - flat['created_date']).days

        else:
            return []

        return [flat]

    def compute(self):
        """
        Compute the average open issue age for all issues in the Perceval data.

        :returns avg_open_issue_age: the average age of open
            issues
        """

        avg_open_issue_age = self.df['open_issue_age'].mean()
        return avg_open_issue_age

    def _agg(self, df, period):
        """
        Perform an aggregation operation on a DataFrame to find
        the average age of open issues created in a every
        interval of the period specified in the time_series method,
        like 'M', 'W',etc.

        It computes the mean of the 'open_issue_age' column of the
        DataFrame.

        :param df: a pandas DataFrame on which the aggregation will be
            applied.

        :param period: A string which can be any one of the pandas time
            series rules:
            'W': week
            'M': month
            'D': day

        :returns df: The aggregated dataframe, where aggregations have
            been performed on the "open_issue_age" column
        """

        df = df.resample(period).agg({'open_issue_age': 'mean'})
        df['open_issue_age'] = df['open_issue_age'].fillna(0)

        return df


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = utils.read_json_file('../issues.json')

    # the GitHub API considers all pull requests to be issues. Any
    # pull request represented as an issue has a 'pull_request'
    # attribute, which is used to filter them out from the issue
    # data.

    items = [item for item in items if 'pull_request' not in item['data']]
    open_issue_age = OpenIssueAge(items)
    print("The average age of all open issues is {:.2f}"
          .format(open_issue_age.compute()))

    open_issue_age = OpenIssueAge(items, (date_since, None))
    print("The average age of open issues created after 2018-09-07 is {:.2f}"
          .format(open_issue_age.compute()))

    print("The changes in the age of open issues on a monthly basis: ")
    print(open_issue_age.time_series('M'))
