import pandas as pd

from metric import Metric
import utils


class Commit(Metric):
    """
    Initilizes self.df, the dataframe with one commit per row.

    :param items: A list of dictionaries.
        Each element is a Perceval dictionary, obtained from a JSON
        file or from Perceval directly.

    :param date_range: A tuple which represents the period of interest
        It is of the form (since, until), where since and until are strings.
        Either, or both can be None. If, for example, since is None, that
        would mean that all commits from the first commit to the commit
        who last falls inside the until range will be included.

    :param issrccode_obj: A reference to IsSourceCode class.
        It is used to determine what comprises source code.
        """

    def __init__(self, items, date_range=(None, None), issrccode_obj=None):

        self.issrccode_obj = issrccode_obj
        (self.since, self.until) = date_range

        super().__init__(items)

        if self.since is None:
            self.since = utils.get_date(self.df, 'since')
        if self.until is None:
            self.until = utils.get_date(self.df, 'until')

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

        if all(not self.issrccode_obj.check(file)
                for file in item['data']['files']):
            return []

        flat = {
            'repo': item['origin'],
            'hash': item['data']['commit'],
            'author': item['data']['Author'],
            'category': "commit",
            'created_date': creation_date,
            'commit': item['data']['Commit'],
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
