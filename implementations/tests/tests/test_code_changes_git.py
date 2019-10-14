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

import json
import unittest

from implementations.scripts.code_changes_git import CodeChangesGit


def read_file(path):
    """
    Given a line-by-line JSON file, this function converts it to
    a Python dictionary and returns all such lines as a list.

    :param path: the path to the JSON file

    :returns items: a list of dictionaries read from the JSON file
    """

    items = list()
    with open(path, 'r') as raw_data:
        for line in raw_data:
            line = json.loads(line)

            items.append(line)
    return items


class TestCodeChangesGit(unittest.TestCase):

    def setUp(self):
        """
        Run before each test to read the test data file
        """

        self.items = read_file('data/test_commits_data.json')

    def test_compute_trivial(self):
        """
        Test the compute method of a CodeChangesGit
        object with default parameters.
        """

        changes = CodeChangesGit(self.items)
        expected_count = 21
        count = changes.compute()
        self.assertEqual(expected_count, count)

    def test_compute_with_duplicate(self):
        """
        Test the compute method of a CodeChangesGit
        object with default parameters but with a
        duplicate item in the test data.
        """

        items_temp = self.items
        items_temp.append(self.items[0])
        changes = CodeChangesGit(items_temp)
        expected_count = 21
        count = changes.compute()
        self.assertEqual(expected_count, count)


if __name__ == '__main__':
    unittest.main(verbosity=2)
