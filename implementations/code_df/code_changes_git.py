from datetime import datetime

from implementations.code_df.commit_git import CommitGit
from implementations.code_df.conditions import (DirExclude,
                                                MasterInclude,
                                                PostfixExclude)
from implementations.code_df.utils import read_json_file


class CodeChangesGit(CommitGit):
    """
    Class for Code Changes for Git repositories.
    """

    def compute(self):
        """
        Count number of commits of different types, like including
        empty commits or counting only those commits made on
        the master branch.

        :returns count: the number of commits satisfying the conditions passed
            while instantiating CodeChangesGit.
        """

        return len(self.df['hash'].unique())

    def _agg(self, df, period):
        """
        Perform an aggregation operation on a DataFrame or Series
        to count the number of commits created in a every interval
        of the period specified in the time_series method, like
        'M', 'W',etc.

        It simply counts the number of rows in the series, excluding
        NaN values.

        :param df: A pandas DataFrame on which to apply the aggregation

        :param period: A string which can be any one of the pandas time
        series rules:
            'W': week
            'M': month
            'D': day

        :returns count: the number of commits in the given series.
        """

        df = df.resample(period)['category'].agg(['count'])
        return df

    def __str__(self):
        return "Code Changes"


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = read_json_file('../git-commits.json')

    # total changes
    changes = CodeChangesGit(items, date_range=(date_since, None))
    print("Code_Changes, total:", changes.compute())

    # excluding certain files
    changes = CodeChangesGit(items, date_range=(date_since, None),
                             is_code=[DirExclude(['tests']),
                                      PostfixExclude(['.md', 'COPYING'])])
    print("Code_Changes, excluding some files:", changes.compute())

    # considering commits only on the master
    changes = CodeChangesGit(items, date_range=(date_since, None),
                             conds=[MasterInclude()])
    print("Code_Changes, only for master:", changes.compute())

    # time-series on a monthly basis considering only master commits
    print("The number of commits created on a monthly basis is:")
    print(changes.time_series(period='M'))
