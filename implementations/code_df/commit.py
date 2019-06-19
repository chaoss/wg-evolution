import pandas as pd
from .metric import Metric
from . import utils


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
        which last falls inside the until range will be included.

    :param issrccode_obj: A reference to IsSourceCode class.
        It is used to determine what comprises of source code.
        """

    def __init__(self, items, date_range=(None, None), issrccode_obj=None):

        self.issrccode_obj = issrccode_obj
        (self.since, self.until) = date_range

        clean_items = list()

        for line in items:
            commit = self._flatten_data(line)
            if commit is not None:
                clean_items.append(commit)

        self.df = pd.DataFrame(clean_items)

        if self.since is None:
            self.since = utils.get_date(self.df, 'since')
        if self.until is None:
            self.until = utils.get_date(self.df, 'until')

    def _flatten_data(self, item):
        """
        This method is for cleaning a raw commit fetched by Perceval.
        Since all attributes of the data are not of importance, it is
        better to just keep the ones which are required.

        :param item: a raw item (of type dict) fetched by Perceval,
        present in the JSON file (items object)

        :returns cleaned_item: A clean, flattened commit, of type dict
        """
        creation_date = utils.str_to_date(item['data']['AuthorDate'])

        if self.since and self.since > creation_date:
            return None

        if self.until and self.until < creation_date:
            return None

        if all(not self.issrccode_obj.check(file)
               for file in item['data']['files']):
            return None

        cleaned_item = {
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
        cleaned_item['files_action'] = actions

        if 'Merge' in item['data']:
            cleaned_item['merge'] = True
        return cleaned_item
