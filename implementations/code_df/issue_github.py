from implementations.code_df.metric import Metric
from implementations.code_df.utils import str_to_date


class IssueGitHub(Metric):
    """
    Initializes self.df, the DataFrame, with one issue per row.

    :param items: A list of dictionaries.
        Each item is a Perceval dictionary, obtained from a JSON
        file or from Perceval directly.

    :param date_range: A tuple which represents the period of interest
        It is of the form (since, until), where since and until are
        strings. Either, or both can be None. If, for example, since
        is None, that would mean that all issues from the first issue
        to the issue which last falls inside the until range will be
        included.

    :param reopen_as_new: A criteria for deciding whether reopened issues
        are considered as new issues. If True, every time an item is reopened,
        it is treated as a new issue.
    """

    def __init__(self, items, date_range=(None, None), reopen_as_new=False):

        self.since, self.until = date_range
        super().__init__(items)

        if reopen_as_new is True:
            self.df = self._update_with_reopened_items(self.df)

    def _flatten(self, item):
        """
        Flatten a raw issue fetched by Perceval into a flat dictionary.

        A list with a single flat directory will be returned.
        That dictionary will have the elements we need for computing metrics.
        The list may be empty, if for some reason the issue should not
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
            'category': "issue",
            'author': item['data']['user']['login'],
            'created_date': creation_date,
            'current_status': item['data']['state'],
            'events_data': item['data']['events_data']
        }

        return [flat]

    def _update_with_reopened_items(self, df):
        """
        Add reopened items as new items to the data frame df.

        The original item to be replaced is removed, while its constituent
        items (created from a reopen-close cycle) are appending to the dataframe.

        :param df: A pandas DataFrame, containing items obtained from Perceval.

        :returns df: A modified pandas DataFrame.
        """

        reopened_items = []
        new_items = []
        for index, item in df.iterrows():

            events = [event for event in item['events_data'] if event['event'] == 'closed'
                      or event['event'] == 'reopened']

            if events:

                # the first closing event gives us our first item
                new_item = self._add_item(item, item['created_date'], 'closed')
                new_items.append(new_item)

                # for every reopen-close pair, create another event
                for i in range(1, len(events), 2):
                    if events[i]['event'] == 'reopened':
                        if i == len(events) - 1:
                            new_item = self._add_item(item, str_to_date(events[i]['created_at']), 'open')
                        else:
                            new_item = self._add_item(item, str_to_date(events[i]['created_at']), 'closed')
                        # print(new_item['created_date'])
                        new_items.append(new_item)
                reopened_items.append(index)

        # remove the items that we split into constituent items
        df = df.drop(reopened_items)

        df = df.append(new_items, ignore_index=True)
        return df

    def _add_item(self, item, created_date, current_status):
        """
        Create a copy of an item with slight modifications to status and
        creation date.

        :param item: A pandas Series object, a single unit of Perceval data.

        :param created_date: A datetime object representing when the item to be
            added was created.

        :param current status: A string representing the current state of the item
            to be added. Either "open" or "closed"

        :returns new_item: A pandas Series object, a constituent of item.
        """

        new_item = item.copy(deep=True)
        new_item['created_date'] = created_date
        new_item['current_status'] = current_status
        return new_item
