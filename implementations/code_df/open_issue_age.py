from datetime import datetime

import pandas as pd
import numpy as np

import utils
from issue import Issue


class OpenIssueAge(Issue):
    """
    Class for Age of Open Issues

    :param items: A list of dictionaries.
        Each item is a Perceval dictionary, obtained from a JSON
        file or from Perceval directly.

    :param date_range: A tuple which represents the period of interest
        It is of the form (since, until), where since and until are strings.
        Either, or both can be None. If, for example, since is None, that
        would mean that all commits from the first commit to the commit
        who last falls inside the until range will be included.
    """

    def __init__(self, item_list, date_range=(None, None)):

        super().__init__(item_list, date_range)

        self.df = self._add_open_issue_age_col(self.df)

    def compute(self):
        """
        Compute the average open issue age for all issues in the Perceval data.

        :returns avg_open_issue_age: the average age of open
            issues
        """

        open_issue_ages = [age for age in self.df['open_issue_age']
                           if not pd.isna(age)]

        avg_open_issue_age = np.mean(open_issue_ages)
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

        df = df.resample(period)['open_issue_age'].agg(['mean'])

        return df

    def _add_open_issue_age_col(self, df):
        """
        Adds the open_issue_age column to df if it is
        not empty.

        :param df: A pandas DataFrame.
        :returns df: Modified DataFrame

        :raises ValueError: No analysis possible if no valid data in df.
        """

        if len(df) > 0:
            # add open_issue_age column
            df['open_issue_age'] = pd.np.nan

            # replace NaN values for open issues by their "age"
            issue_status_series = datetime.now() - df["created_date"][
                df["current_status"] == "open"]

            ages_in_days = [x.days for x in issue_status_series]
            df.loc[df["current_status"] == "open",
                   ['open_issue_age']] = ages_in_days

        else:
            raise ValueError("DataFrame empty. "
                             "Please check instantiation parameters")

        return df


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = utils.read_json_file('../issues.json')
    open_issue_age = OpenIssueAge(items)
    print("The average age of all open issues is {:.2f}"
          .format(open_issue_age.compute()))

    open_issue_age = OpenIssueAge(items, (date_since, None))
    print("The average age of open issues created after 2018-09-07 is {:.2f}"
          .format(open_issue_age.compute()))

    print(open_issue_age.time_series('M'))
