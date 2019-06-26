import conditions
from metric import Metric
import utils


class Commit(Metric):
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

        (self.since, self.until) = date_range
        self.is_code = is_code
        self.conds = conds

        super().__init__(items)

        # Initialize conditions
        for condition in self.conds:
            if isinstance(condition, conditions.Commit):
                condition.set_commits(self.df)
        # Filter out rows not fulfilling conditions
        for condition in self.conds:
            self._filterout(condition)

    def _filterout(self, condition):
        """Filter out rows according to conditions on commits"""

        for index, row in self.df.iterrows():
            if not condition.check(row['hash']):
                self.df.drop(index, inplace=True)

    def _flatten(self, item):
        """
        Flatten a raw commit fetched by Perceval into a flat dictionary.

        A list with a single flat directory will be returned.
        That dictionary will have the elements we need for computing metrics.
        The list may be empty, if for some reason the commit should not
        be considered.

        :param item: raw item fetched by Perceval (dictionary)
        :returns:    list of a single flat dictionary
        """

        creation_date = utils.str_to_date(item['data']['AuthorDate'])
        if self.since and (self.since > creation_date):
            return []

        if self.until and (self.until < creation_date):
            return []

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
                'commit_date': utils.str_to_date(item['data']['CommitDate']),
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

            return [flat]
        else:
            return []
