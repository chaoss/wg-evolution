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

import unittest
import json
from datetime import datetime

from implementations.scripts.utils import (str_to_date,
                                           read_json_file)


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


class TestUtils(unittest.TestCase):
    """
    Tests for utility functions
    """

    def test_str_to_date_commit(self):
        """
        Test whether _str_to_date correctly converts
        a commit's date string to a datetime object.
        """

        date = "Tue Aug 18 18:08:27 2015 +0200"
        expected = datetime.strptime(
                            date,
                            "%a %b %d %H:%M:%S %Y %z") \
            .strftime("%Y-%m-%d")

        expected = datetime.strptime(expected, "%Y-%m-%d")

        datetimeobj = str_to_date(date)
        self.assertEqual(expected, datetimeobj)

    def test_str_to_date_issue(self):
        """
        Test whether str_to_date correctly converts
        a commit's date string to a datetime object.
        """

        date = "2013-10-20T01:56:25Z"
        expected = datetime.strptime(
                            date,
                            "%Y-%m-%dT%H:%M:%SZ") \
            .strftime("%Y-%m-%d")

        expected = datetime.strptime(expected, "%Y-%m-%d")

        datetimeobj = str_to_date(date)
        self.assertEqual(expected, datetimeobj)

    def test_read_json_file(self):
        """
        Test whether read_json_file correctly reads a file of
        Perceval data, where each line in the file is of json format.
        """

        expected = read_file('data/test_commits_data.json')
        items = read_json_file('data/test_commits_data.json')

        self.assertEqual(expected, items)


if __name__ == '__main__':
    unittest.main(verbosity=2)
