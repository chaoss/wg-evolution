from copy import deepcopy

from implementations.scripts.metric import Metric
from implementations.scripts.utils import str_to_date


class IssueGithub(Metric):
    """
    Generic class for issue metrics without pandas structure
    """

    def __init__(self, items, date_range=(None, None), reopen_as_new=False):
        """
        Constructor of this class

        :param items: list of issues fetched by Perceval into a flat dictionary
        :param date_range: Tuple, containing a range of date
        :param reopen_as_new: A criteria for deciding whether reopened issues
                are considered as new issues. If True, every time an issue is
                reopened, it is treated as a new issue.

                    A limitation to keep in mind is that Perceval
                    currently does not retrieve the event data necessary
                    for deciding whether or not an issue has been reopened. Thus,
                    parameter does not work as expected and shouldn't be set to True.
        """
        self.since, self.until = date_range
        super().__init__(items)

        if reopen_as_new:
            self.items = self._update_with_reopened_items(self.items)

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
        if item['category'] != 'issue':
            return []

        creation_date = str_to_date(item['data']['created_at'])
        if self.since and (self.since > creation_date):
            return []
        elif self.until and (self.until < creation_date):
            return []

        flat = {
            'repo': item['origin'],
            'hash': item['data']['id'],
            'category': 'issue',
            'author': item['data']['user']['login'],
            'created_date': creation_date,
            'current_status': item['data']['state']
        }

        if 'events_data' in item['data']:
            flat.update(events_data=item['data']['events_data'])

        return [flat]

    def _update_with_reopened_items(self, items):
        """
        Add reopened issues as new issues into the list of dictionary

        The original item to be replaced is removed, while its constituent
        items (created from a reopen-close cycle) are appending to the dictionary.

        :param items: A list of dictionary containing the issues

        :returns: The modified list of dictionary containing the issues
        """
        reopened_items = []
        for index, item in zip(range(len(items)), items):
            events = []

            if 'events_data' in item:
                events = [event for event in item['events_data'] if event['event'] == 'closed' or event['event'] == 'reopened']

            if events:
                # the first closing event gives us our first item
                new_item = self._add_item(item, item['created_date'], 'closed')
                items.append(new_item)

                # for every reopen-close pair, create another event
                for i in range(1, len(events), 2):
                    if events[i]['event'] == 'reopened':
                        if i == len(events) - 1:
                            new_item = self._add_item(item, str_to_date(events[i]['created_at']), 'open')
                        else:
                            new_item = self._add_item(item, str_to_date(events[i]['created_at']), 'closed')
                        items.append(new_item)
                reopened_items.append(index)

        # remove the items that we split into constituent items
        for i in range(len(reopened_items)):
            del items[reopened_items[i] - i]

        return items

    def _add_item(self, item, created_date, current_status):
        """
        Create a copy of an item with slight modifications to status and
        creation date.

        :param item: A dictionary, a single unit of Perceval data.

        :param created_date: A datetime object representing when the item to be
                added was created.

        :param current status: A string representing the current state of the item
                to be added. Either "open" or "closed"

        :returns new_item: A dictionary, a constituent of item.
        """

        new_item = deepcopy(item)
        new_item['created_date'] = created_date
        new_item['current_status'] = current_status
        return new_item

    def compute(self):
        raise NotImplementedError

    def __str__(self):
        return "Issues in Github"
