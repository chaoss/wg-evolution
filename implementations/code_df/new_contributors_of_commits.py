import pandas as pd
from datetime import datetime

import utils
import conditions
from commit import Commit


class NewContributorsOfCommits(Commit):
    """
    Initilizes self.df, the dataframe with one commit per row.

    :param items: A list of dictionaries.
        Each item is a Perceval dictionary, obtained from a JSON
        file or from Perceval directly.

    :param date_range: A tuple which represents the period of interest
        It is of the form (since, until), where since and until are strings.
        Either, or both can be None. If, for example, since is None, that
        would mean that all commits from the first commit to the commit
        who last falls inside the until range will be included.

    :param is_code:  list of CodeCondition objects
        It is used to determine what comprises source code.
        """

    def __init__(self, items, date_range=(None, None),
                 is_code=[conditions.Naive()], conds=[]):

        super().__init__(items, date_range, is_code, conds)

        self.df = self.df.loc[self.df.groupby('author')['created_date'].idxmin()]

    def compute(self, check_range=(None, None)):
        """
        Count number of new committers who committed between the two dates
        of check range.

        :param check_range: A tuple which represents the start and end date
            when new committers will be considered

        :returns count_new_committers: the number of new committers who committed
            between the dates of check_range
        """

        self.check_since, self.check_until = check_range

        df = self.df

        if self.check_since is not None:
            df = df[df['created_date'] < self.check_since]

        if self.check_until is not None:
            df = df[df['created_date'] >= self.check_until]

        count_new_committers = len(df.index)
        return count_new_committers

    def _agg(self, df, period):
        """
        Perform an aggregation operation on a DataFrame or Series
        to count the number of new committers in a period when
        compared to committers before that period.

        This method uses the 'count' aggregation method.

        :param df: a pandas DataFrame on which the aggregation will be
            applied.

        :param period: A string which can be any one of the pandas time
            series rules:
            'W': week
            'M': month
            'D': day

        :returns df: The final aggregated DataFrame
        """

        df = df.resample(period)['author'].agg(['count'])
        return df


if __name__ == "__main__":

    date_since = datetime.strptime("2018-01-01", "%Y-%m-%d")
    date_until = datetime.strptime("2018-07-01", "%Y-%m-%d")
    check_since = datetime.strptime("2018-03-08", "%Y-%m-%d")
    check_until = datetime.strptime("2018-06-08", "%Y-%m-%d")
    items = utils.read_json_file('../git-commits.json')

    new_committers = NewContributorsOfCommits(items)    
    print("New committers, total: {}".format(new_committers.compute()))

    new_committers_interval = NewContributorsOfCommits(
        items,
        (date_since, date_until),
        is_code=[conditions.DirExclude(['tests']),
                 conditions.PostfixExclude(['.md', 'COPYING'])])

    print("Variations in the number of new committers"
          " between 2018-01-01 and 2018-07-01: ")
    print(new_committers_interval.time_series(period='M'))

    new_committers_dated = NewContributorsOfCommits(
                                            items,
                                            (date_since, date_until),
                                            is_code=[
                                                conditions.DirExclude(['tests']),
                                                conditions.PostfixExclude(
                                                    ['.md', 'COPYING'])])
    print("New committers, after 2018-03-08 (excluding some files):",
          new_committers.compute(check_range=(check_since, None)))
