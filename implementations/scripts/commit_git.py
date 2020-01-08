# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CHAOSS
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     Aniruddha Karajgi <akarajgi0@gmail.com>
#

from implementations.scripts.metric import Metric
from implementations.scripts.conditions import Naive, Commit
from implementations.scripts.utils import str_to_date


class CommitGit(Metric):
    """
    Initializes self.items, a list with items(dictionary) as
    elements.

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

    :param conds: list of Commit sub-class objects.
        Used to add restrictions on which commits are
        included in the analysis.
        """

    def __init__(self, items, date_range=(None, None),
                 is_code=[Naive()], conds=[]):

        (self.since, self.until) = date_range
        self.is_code = is_code
        self.conds = conds

        super().__init__(items)

        # Initialize conditions
        for condition in self.conds:
            if isinstance(condition, Commit):
                condition.set_commits(self.items)
        # Filter out rows not fulfilling conditions
        for condition in self.conds:
            self._filterout(condition)

    def _filterout(self, condition):
        """Filter out rows according to conditions on commits"""

        new_items = [item for item in self.items
                     if condition.check(item['hash'])]

        self.items = new_items

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

        creation_date = str_to_date(item['data']['AuthorDate'])
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
                'commit_date': str_to_date(item['data']['CommitDate']),
                'files_no': len(item['data']['files']),
                'refs': item['data']['refs'],
                'parents': item['data']['parents'],
                'files': item['data']['files'],
                'message': item['data']['message']
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
