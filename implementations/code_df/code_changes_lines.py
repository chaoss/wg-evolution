from datetime import datetime

import conditions
import utils
from commit import Commit


class CodeChangesLines(Commit):
    """
    Class for Code_Changes_Lines

    :param items: A list of dictionaries, each element a line from the
        JSON file with Perceval data

    :param date_range: A tuple which represents the start and end date of
        interest

    :param is_code:  list of CodeCondition objects
        It is used to determine what comprises source code.

    :param conds: A list of Commit objects. It is used to
        exclude or include different kinds of commits, like
        empty or merge commits, or commits made on the master
        branch.
    """

    def __init__(self, items, date_range=(None, None),
                 is_code=[conditions.Naive()], conds=[]):
        super().__init__(items, date_range, is_code, conds)

        self.df = self._add_lines_modified_cols(self.df)

    def compute(self):
        """
        Count the number of lines added or deleted in the data fetched
        by Perceval.

        It computes the sums of the 'additions' and 'deletions' columns
        in the DataFrame.

        :returns modified: A tuple representing the number of lines
            modified. modified -> (additions, deletions)
        """

        df = self.df
        additions = df['additions'].sum()
        deletions = df['deletions'].sum()

        modified = (additions, deletions)

        return modified

    def _agg(self, df, period):
        """
        Perform an aggregation operation on a DataFrame or Series
        to find the total number of lines modified in a every interval
        of the period specified in the time_series method, like
        'M', 'W',etc.

        It adds the number of lines modified for every row in the
        series.

        :param df: a pandas DataFrame on which the aggregation will be
            applied.

        :param period: A string which can be any one of the pandas time
            series rules:
            'W': week
            'M': month
            'D': day

        :returns df: The aggregated dataframe, where aggregations have
            been perform on "additions" and "deletions" columns
        """

        df = df.resample(period).agg({"additions": 'sum', "deletions": 'sum'})

        return df

    def _add_lines_modified_cols(self, df):

        if len(df) == 0:
            raise ValueError("DataFrame empty. "
                             "Please check instantiation parameters")

        additions = list()
        deletions = list()
        for _, commit in df.iterrows():
            added_lines = 0
            removed_lines = 0
            for file in commit['files']:
                if 'added' and 'removed' in file:
                    try:
                        added_lines += int(file['added'])
                        removed_lines += int(file['removed'])

                    except ValueError:
                        # in case of compressed files,
                        # additions and deletions are "-"
                        pass

            additions.append(added_lines)
            deletions.append(removed_lines)

        df['additions'] = additions
        df['deletions'] = deletions

        return df


if __name__ == "__main__":  
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = utils.read_json_file('../git-commits.json')
    changes = CodeChangesLines(items, date_range=(None, None))
    print("Code_Changes_Lines, total changes:", changes.compute())

    changes = CodeChangesLines(items, date_range=(date_since, None),
                               is_code=[conditions.DirExclude(['tests']),
                                        conditions.PostfixExclude(
                                            ['.md', 'COPYING'])])
    print("Code_Changes_Lines, excluding some files:", changes.compute())

    changes = CodeChangesLines(items, date_range=(date_since, None),
                               conds=[conditions.MasterInclude()])
    print("Code_Changes_Lines, only for master:", changes.compute())

    print("The number of lines modified over several months is: ")
    print(changes.time_series())
