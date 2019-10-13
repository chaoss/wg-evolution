from datetime import datetime

from implementations.code_df.commit_git import CommitGit
from implementations.code_df.conditions import (Naive,
                                                DirExclude,
                                                PostfixExclude)
from implementations.code_df.utils import str_to_date, read_json_file


class NewContributorsOfCommitsGit(CommitGit):
    """
    Class for New_Contributors_of_Commits.

    Initializes self.df, the dataframe with one commit per row.

    :param items: A list of dictionaries.
        Each item is a Perceval dictionary, obtained from a JSON
        file or from Perceval directly.

    :param date_range: A tuple which represents the start and end date
        between which new committers will be considered.
        Either, or both can be None. If, for example, since is None, that
        all unique contributors whose commit lies between the first first commit
        to the commit which last falls inside the until range would be considered
        unique contributors.

    :param is_code:  list of CodeCondition objects
        It is used to determine what comprises source code.

    :param conds: list of Commit sub-class objects.
        Used to add restrictions on which commits are
        included in the analysis.
        """

    def __init__(self, items, date_range=(None, None),
                 is_code=[Naive()], conds=[]):

        super().__init__(items, date_range, is_code, conds)

        self.df = self.df.loc[self.df.groupby('author')['created_date']
                              .idxmin()]

        since, until = date_range

        if since:
            self.df = self.df[self.df['created_date'] >= since]

        if until:
            self.df = self.df[self.df['created_date'] <= until]

    def _flatten(self, item):
        """
        Flatten a raw commit fetched by Perceval into a flat dictionary.

        A list with a single flat directory will be returned.
        That dictionary will have the elements we need for computing metrics.
        The list may be empty, if for some reason the commit should not
        be considered.

        This method overrides CommitGit._flatten and does not ignore commits
        based on the dates in date_range. The difference lies in the
        meaning of date_range for this metric when compared to the default
        meaning. For this metric, date_range signifies the dates between which
        we look for new contributors when compared to all contributors,
        while the general use of date_range is to decide which commits to consider
        for analysis.

        :param item: raw item fetched by Perceval (dictionary)
        :returns:    list of a single flat dictionary
        """

        creation_date = str_to_date(item['data']['AuthorDate'])

        code_files = [file['file'] for file in item['data']['files'] if
                      all(condition.check(file['file'])
                          for condition in self.is_code)]

        if len(code_files) > 0:
            flat = {
                'repo': item['origin'],
                'hash': item['data']['commit'],
                'author': item['data']['Author'],
                'category': "commit",
                'created_date': creation_date,
                'committer': item['data']['Commit'],
                'commit_date': str_to_date(item['data']['CommitDate']),
                'files_no': len(item['data']['files']),
                'refs': item['data']['refs'],
                'parents': item['data']['parents'],
                'files': item['data']['files']
            }

            actions = 0
            for file in item['data']['files']:
                if 'action' in file:
                    actions += 1
            flat['files_action'] = actions

            if 'Merge' in item['data']:
                flat['merge'] = True
            else:
                flat['merge'] = False

            return [flat]
        else:
            return []

    def compute(self):
        """
        Count the number of new committers who committed between the two dates
        of date_range.

        :returns count_of_new_committers: the number of new committers who
            committed between the dates of date_range

            Since the dataframe self.df is modified in __init__ via groupby
            and idmin(), the number of unique entries in the dataframe gives
            us the number of new committers between the given dates.
        """

        count_of_new_committers = len(self.df.index)
        return count_of_new_committers

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

    def _get_params(self):
        """
        Return parameters for creating a timeseries plot

        :returns: A dictionary with axes to plot, a title
            and if use_index should be true when creating
            the plot.
        """

        title = "Trends in the Number of New Committers"
        x = None
        y = 'count'
        use_index = True
        return {'x': x, 'y': y, 'title': title, 'use_index': use_index}

    def __str__(self):
        return "New Contributors of Commits"


if __name__ == "__main__":

    date_since = datetime.strptime("2018-01-01", "%Y-%m-%d")
    date_until = datetime.strptime("2018-07-01", "%Y-%m-%d")

    items = read_json_file('../git-commits.json')

    # total number of new contributors
    new_committers = NewContributorsOfCommitsGit(items)
    print("New committers, total: {}".format(new_committers.compute()))

    # excluding certain files
    new_committers_interval = NewContributorsOfCommitsGit(
        items,
        (date_since, date_until),
        is_code=[DirExclude(['tests']),
                 PostfixExclude(['.md', 'COPYING'])])

    # # time-series on a monthly basis
    print("Variations in the number of new committers"
          " between 2018-01-01 and 2018-07-01: ")
    print(new_committers_interval.time_series(period='M'))

    # restricting to a certain range
    new_committers_dated = NewContributorsOfCommitsGit(
                                            items,
                                            (date_since, None),
                                            is_code=[
                                                DirExclude(
                                                    ['tests']),
                                                PostfixExclude(
                                                    ['.md', 'COPYING'])])
    print("New committers, after 2018-03-08 (excluding some files):",
          new_committers_dated.compute())
