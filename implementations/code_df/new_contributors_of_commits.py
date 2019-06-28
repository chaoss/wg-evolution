import pandas as pd
from datetime import datetime

import utils
import conditions
from commit import Commit


class NewContributorsOfCommits(Commit):
    """
    Class for New contributors of commits.
    """

    def compute(self, check_range=(None, None)):
        """
        Count number of new committers who committed between the two dates
        of check range.

        :param check_range: A tuple which represents the start and end date
            when new committers will be considered

        :returns count: the number of new committers who committed
            between the dates of check_range
        """

        self.check_since, self.check_until = check_range

        df = pd.DataFrame(columns=self.df.columns)

        if self.check_since is not None:
            df = self.df[self.df['created_date'] < self.check_since]

        committers_before_check_since = set(df['author'].tolist())

        df_new_committers = self.df['author'][
                    (~self.df['author']
                        .isin(
                            list(committers_before_check_since)))
                ]

        if self.check_since is not None:
            df_new_committers = df_new_committers[
                self.check_since <= self.df['created_date']]

        if self.check_until is not None:
            df_new_committers = df_new_committers[
                self.check_until >= self.df['created_date']]

        count_new_committers = len(df_new_committers.unique())
        return count_new_committers

    def _agg(self, df, period):
        """
        Call an aggregation operation on a DataFrame or Series
        to count the number of new committers in a period when
        compared to the previous period.

        :param df: a pandas DataFrame on which the aggregation will be
            applied.

        :param period: A string which can be any one of the pandas time
            series rules:
            'W': week
            'M': month
            'D': day

        :returns df: The final aggregated DataFrame
        """

        def __new_committers_count(series):
            """
            Aggregation method to count the number of new committers
            per period.

            The set of names of people who committed before the current
            period is stored in old_committers and any new committers
            in the current period whose names are not in old_committers
            are counted.

            :param series: a pandas DataFrame on which the aggregation will be
                applied.

            :param period: A string which can be any one of the pandas time
                series rules:
                'W': week
                'M': month
                'D': day

            :returns count: The number of new committers
            """
            if len(series) > 0:
                old_committers = \
                    set(
                        self.df['author'][
                            self.df['created_date'] < series.index[0]]
                        .tolist())

                count = len(series[~series.isin(list(old_committers))]
                            .unique())
                old_committers.update(series.tolist())
                return count

            else:
                return 0

        df = df.resample(period)['author'].agg([__new_committers_count])
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
