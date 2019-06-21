from metric import Metric
import utils


class Issue(Metric):

    def __init__(self, items, date_range=(None, None)):
        """
        Initilizes self.df, the dataframe with one commit per row.

        :param items: A list of dictionaries.
            Each item is a Perceval dictionary, obtained from a JSON
            file or from Perceval directly.

        :param date_range: A tuple which represents the period of interest
            It is of the form (since, until), where since and until are
            strings. Either, or both can be None. If, for example, since
            is None, that would mean that all commits from the first commit
            to the commit who last falls inside the until range will be
            included.
        """

        self.since, self.until = date_range
        super().__init__(items)

    def _flatten(self, item):
        """
        Flatten a raw issue fetched by Perceval into a flat dictionary.

        A list with a single flat directory will be returned.
        That dictionary will have the elements we need for computing metrics.
        The list may be empty, if for some reason the commit should not
        be considered.

        :param item: raw item fetched by Perceval (dictionary)
        :returns:   list of a single flat dictionary
        """

        creation_date = utils.str_to_date(item['data']['created_at'])
        if self.since and (self.since > creation_date):
            return []

        if self.until and (self.until < creation_date):
            return []

        flat = {
            'repo': item['origin'],
            'hash': item['data']['id'],
            'category': "issue",
            'author': item['data']['user']['login'],
            'created_date': creation_date,
            'current_status': item['data']['state']
        }

        return [flat]
