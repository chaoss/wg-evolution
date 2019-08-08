from implementations.code_df.metric import Metric
from implementations.code_df.utils import str_to_date


class PullRequestGitHub(Metric):
    """
    Initializes self.df, the dataframe with one pull_request per row.

    :param items: A list of dictionaries.
        Each item is a Perceval dictionary, obtained from a JSON
        file or from Perceval directly.

    :param date_range: A tuple which represents the period of interest
        It is of the form (since, until), where since and until are
        strings. Either, or both can be None. If, for example, since
        is None, that would mean that all pull_requests from the first
        pull_request to the pull_request which last falls inside the
        until range will be included.
    """

    def __init__(self, items, date_range=(None, None)):

        self.since, self.until = date_range
        super().__init__(items)

    def _flatten(self, item):
        """
        Flatten a raw pull_request fetched by Perceval into a flat dictionary.

        A list with a single flat directory will be returned.
        That dictionary will have the elements we need for computing metrics.
        The list may be empty, if for some reason the pull_request should not
        be considered.

        :param item: raw item fetched by Perceval (dictionary)
        :returns:   list of a single flat dictionary
        """

        creation_date = str_to_date(item['data']['created_at'])
        if self.since and (self.since > creation_date):
            return []

        if self.until and (self.until < creation_date):
            return []

        flat = {
            'repo': item['origin'],
            'hash': item['data']['id'],
            'category': "pull_request",
            'author': item['data']['user']['login'],
            'created_date': creation_date,
            'current_status': item['data']['state'],
            'merged': item['data']['merged']
        }

        return [flat]
