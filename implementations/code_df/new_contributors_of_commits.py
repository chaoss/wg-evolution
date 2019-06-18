import pandas as pd
from datetime import datetime
import utils
from is_source_code import IsSourceCode, Naive
from commit import Commit


class NewContributorsoFCommits(Commit):
    """
    Class for New contributors of commits.

    :param items: A list of dictionaries, each element a line from the
        JSON file with Perceval data
    :param date_range: A tuple which represents the start and end date of
        interest
    :param issrccode_obj: An object of IsSourceCode, used to determine
        what comprises source code.
    """

    def __init__(self, items, date_range=(None, None), issrccode_obj=None):
        super().__init__(items, date_range, issrccode_obj)

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

        if self.check_since is None:
            self.check_since = self.since

        if self.check_until is None:
            self.check_until = self.until

        df = self.df[self.df['created_date'] < self.check_since]

        committers_before_check_since = set()
        committers_before_check_since = set(df['author'].tolist())
        count_new_committers = 0
        df_new_committers = self.df['author'][
                    (self.check_since <= self.df['created_date'])
                    & (self.check_until >= self.df['created_date'])
                    & (~self.df['author']
                        .isin(
                            list(committers_before_check_since)))
                ]
        count_new_committers = len(df_new_committers.unique())
        return count_new_committers

    def compute_timeseries(self, period='month'):
        """
        The metric value is computed for each fixed interval of time
        from the "since" date to the "until" date arguments, specified
        during object initiation.

        The fixed time interval can be either a month or a week.

        :param period: A string which can be either "month" or "week"

        :returns dataframe: A DataFrame whose rows each represent an interval
            of "period" and the count for that interval
        """
        old_committers = set()

        def count_new(series):
            """
            An aggregate function that calculates only those values which
            are new in a grouping as compared to a previous dataframe
            grouping

            :param series: a pandas Series

            :returns count: the number of new elements in series
            """
            nonlocal old_committers

            count = len(series[~series.isin(list(old_committers))].unique())
            old_committers.update(series.tolist())
            return count

        df = self.df
        if period == 'month':
            timeseries_series = df['author'] \
                .groupby([df['created_date'].dt.year.rename('year'),
                          df['created_date'].dt.month.rename('month')]) \
                .agg(count_new)

            all_periods = pd.DataFrame(
                            pd.date_range(self.since, self.until, freq='M'),
                            columns=['Dates'])
            all_periods = pd.DataFrame(
                [all_periods['Dates'].dt.year.rename('year'),
                 all_periods['Dates'].dt.month.rename("month")]).T

        elif period == 'week':
            timeseries_series = df['author'] \
                .groupby([df['created_date'].dt.year.rename('year'),
                          df['created_date'].dt.week.rename('week')])   \
                .agg(count_new)

            all_periods = pd.DataFrame(
                            pd.date_range(self.since, self.until, freq='W'),
                            columns=['Dates'])
            all_periods = pd.DataFrame(
                [all_periods['Dates'].dt.year.rename('year'),
                 all_periods['Dates'].dt.week.rename('week')]).T

        else:
            raise ValueError("period parameter can take 'month' or 'week'")

        timeseries_df = pd.DataFrame(timeseries_series)
        timeseries_df.reset_index(inplace=True)
        timeseries_df.columns = ['year', period, 'new_committers']
        merged_df = all_periods.merge(timeseries_df, how='outer').fillna(0)

        dataframe = merged_df
        return dataframe


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    issourcecode = IsSourceCode(["tests/"], Naive)
    items = utils.read_JSON_file('../git-commits.json')
    new_committers = NewContributorsoFCommits(items, date_range=(date_since, None),
                                       issrccode_obj=issourcecode)
    print(new_committers.compute((date_since, None)))
