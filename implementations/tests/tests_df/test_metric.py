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

from pandas.util.testing import assert_frame_equal

from implementations.code_df.commit_git import CommitGit


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


class TestMetric(unittest.TestCase):
    """
    Tests for the Metric class
    """

    def setUp(self):
        self.items = read_file('data/test_commits_data.json')

    def test_time_series_commit(self):
        """
        Test whether time_series correctly sets the
        index of the DataFrame to the `created_date` column
        """
        class Temp(CommitGit):
            """
            The Temp class.

            A temporary sub-class of the code_df.CommitGit class.

            It overrides the _agg method to simply return the passed
            dataframe without modification. This allows the testing of
            the time_series method, defined in the Metric class, in
            isolation.
            """

            def _agg(self, df, period):
                return df

        temp = Temp(self.items)
        expected_df = temp.df
        expected_df = expected_df.set_index('created_date')
        returned_df = temp.time_series('W')

        assert_frame_equal(expected_df, returned_df)


if __name__ == '__main__':
    unittest.main(verbosity=2)
