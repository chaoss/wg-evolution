import pandas as pd
from datetime import datetime
import utils
from is_source_code import IsSourceCode, Naive
from commit import Commit


class CodeChangesGit(Commit):
    """Class for Code_Changes for Git repositories.

    :param items: A list of dictionaries, each element a line from the
        JSON file with Perceval data
    :param date_range: A tuple which represents the start and end date of
        interest
    :param issrccode_obj: An object of IsSourceCode, used to determine
        what comprises source code.
    """

    def __init__(self, items, date_range=(None, None), issrccode_obj=None):

        super().__init__(items, date_range, issrccode_obj)

    def compute(self, incl_empty=True, incl_merge=True, master_only=False):
        """Count number of commits of different types, like including empty commits
        or counting only those commits made on the master branch.

        :param incl_empty: Include empty commits
        :param incl_merge: Include merge commits
        :param master_only: Include only commits made on master branch

        :returns count: the number of commits satisfying the passed
            conditions above
        """
        df = self.df

        if master_only:
            count = self._count_master_only(incl_empty)

        else:
            if not incl_empty:
                df = df[df['files_action'] != 0]
            if not incl_merge:
                df = df[~df['merge']]
            count = df['hash'].nunique()

        return count

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

        df = self.df
        if period == 'month':
            timeseries_series = df['created_date'] \
                .groupby([df['created_date'].dt.year.rename('year'),
                          df['created_date'].dt.month.rename('month')]) \
                .agg('count')

            all_periods = pd.DataFrame(
                            pd.date_range(self.since, self.until, freq='M'),
                            columns=['Dates'])
            all_periods = pd.DataFrame(
                [all_periods['Dates'].dt.year.rename('year'),
                 all_periods['Dates'].dt.month.rename("month")]).T

        elif period == 'week':
            timeseries_series = df['created_date'] \
                .groupby([df['created_date'].dt.year.rename('year'),
                          df['created_date'].dt.week.rename('week')])   \
                .agg('count')

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
        timeseries_df.columns = ['year', period, 'count']
        merged_df = all_periods.merge(timeseries_df, how='outer').fillna(0)

        dataframe = merged_df
        return dataframe

    def _count_master_only(self, incl_empty=True):
        """
        Counts commits present only on the master branch.

        :param incl_empty: exclude empty commits on the master branch

        :returns commits_count: the number of commits created on the
            master branch
        """

        df = self.df
        todo = set()
        for _, commit in df.iterrows():
            if 'HEAD -> refs/heads/master' in commit['refs']:
                todo.add(commit['hash'])

        master = set()
        while len(todo) > 0:
            current = todo.pop()
            master.add(current)

            if len(df[df['hash'] == current]['parents']) > 0:
                for parent in df[df['hash'] == current]['parents'].iloc[0]:
                    if parent not in master:
                        todo.add(parent)

        if not incl_empty:
            commits_count = 0
            for commit_id in master:
                commit = df[df['hash'] == commit_id]
                if len(commit['files']) > 0:
                    for file in commit['files'].iloc[0]:
                        if 'action' in file:
                            commits_count += 1
                            break

        else:
            commits_count = len(master)

        return commits_count


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    issourcecode = IsSourceCode(["tests/"], Naive)
    items = utils.read_JSON_file('../git-commits.json')
    changes = CodeChangesGit(items, date_range=(date_since, None),
                             issrccode_obj=issourcecode)
    print(changes.compute())
