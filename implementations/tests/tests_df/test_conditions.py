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

from implementations.code_df.commit_git import CommitGit
from implementations.code_df.metric import Metric
from implementations.code_df.conditions import (
            Naive, DirExclude, PostfixExclude,
            MasterInclude, MergeExclude, EmptyExclude,
            )


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


class TestNaive(unittest.TestCase):
    """
    Tests for the Naive class in the conditions module.
    """

    def setUp(self):
        """
        Run before each test to initialize test files.
        """

        commits = read_file('data/test_commits_data.json')
        self.file_gitignore = commits[0]['data']['files'][0]['file']
        self.file_tests = commits[1]['data']['files'][0]['file']
        self.file_bin = commits[2]['data']['files'][0]['file']
        self.file_py = commits[4]['data']['files'][0]['file']
        self.file_authors = commits[0]['data']['files'][1]['file']

    def test_check(self):
        """
        Test whether the check method of the Naive class
        returns True for all test files.
        """

        self.assertTrue(Naive().check(self.file_gitignore))
        self.assertTrue(Naive().check(self.file_tests))
        self.assertTrue(Naive().check(self.file_bin))
        self.assertTrue(Naive().check(self.file_py))
        self.assertTrue(Naive().check(self.file_authors))


class TestDirExclude(unittest.TestCase):
    """
    Tests for the DirExclude class in the conditions module.
    """

    def setUp(self):
        """
        Run before each test to initialize test files.
        """

        commits = read_file('data/test_commits_data.json')
        self.file_gitignore = commits[0]['data']['files'][0]['file']
        self.file_tests = commits[1]['data']['files'][0]['file']
        self.file_bin = commits[2]['data']['files'][0]['file']
        self.file_perceval = commits[7]['data']['files'][0]['file']
        self.file_authors = commits[0]['data']['files'][1]['file']

    def test_check(self):
        """
        Test whether the check method of the DirExclude class
        correctly returns False for files in the `tests` and `bin`
        directories, which are excluded by default.
        """

        self.assertTrue(DirExclude().check(self.file_gitignore))
        self.assertTrue(DirExclude().check(self.file_perceval))
        self.assertTrue(DirExclude().check(self.file_authors))

        self.assertFalse(DirExclude().check(self.file_tests))
        self.assertFalse(DirExclude().check(self.file_bin))

    def test_check_exclude_none(self):
        """
        Test whether the check method of the DirExclude class
        correctly returns True for all files when no directories
        to be excluded are passed to the check method.
        """

        self.assertTrue(DirExclude([]).check(self.file_gitignore))
        self.assertTrue(DirExclude([]).check(self.file_perceval))
        self.assertTrue(DirExclude([]).check(self.file_authors))
        self.assertTrue(DirExclude([]).check(self.file_tests))
        self.assertTrue(DirExclude([]).check(self.file_bin))

    def test_check_exclude_perceval(self):
        """
        Test whether the check method of the DirExclude class
        correctly returns False for all files in the 'perceval'
        directory.
        """

        self.assertTrue(DirExclude(['perceval']).check(self.file_gitignore))
        self.assertTrue(DirExclude(['perceval']).check(self.file_authors))
        self.assertTrue(DirExclude(['perceval']).check(self.file_tests))
        self.assertTrue(DirExclude(['perceval']).check(self.file_bin))

        self.assertFalse(DirExclude(['perceval']).check(self.file_perceval))


class TestPostfixExclude(unittest.TestCase):
    """
    Tests for the PostfixExclude class in the conditions module.
    """

    def setUp(self):
        """
        Run before each test to initialize test files.
        """

        commits = read_file('data/test_commits_data.json')
        self.file_gitignore = commits[0]['data']['files'][0]['file']
        self.file__init__ = commits[8]['data']['files'][0]['file']
        self.file_bin = commits[2]['data']['files'][0]['file']
        self.file_py = commits[4]['data']['files'][0]['file']
        self.file_authors = commits[0]['data']['files'][1]['file']

    def test_check(self):
        """
        Test whether the check method of the PostfixExclude class
        correctly returns False for all README and markdown files,
        which are excluded by default.
        """

        self.assertTrue(PostfixExclude().check(self.file_gitignore))
        self.assertTrue(PostfixExclude().check(self.file_py))
        self.assertTrue(PostfixExclude().check(self.file_authors))
        self.assertTrue(PostfixExclude().check(self.file__init__))
        self.assertTrue(PostfixExclude().check(self.file_bin))

    def test_check_exclude_none(self):
        """
        Test whether the check method of the PostfixExclude class
        correctly returns True for all files when no extensions
        to be excluded are passed to the check method.
        """

        self.assertTrue(PostfixExclude([]).check(self.file_gitignore))
        self.assertTrue(PostfixExclude([]).check(self.file_py))
        self.assertTrue(PostfixExclude([]).check(self.file_authors))
        self.assertTrue(PostfixExclude([]).check(self.file__init__))
        self.assertTrue(PostfixExclude([]).check(self.file_bin))

    def test_check_exclude_py(self):
        """
        Test whether the check method of the PostfixExclude class
        correctly returns False for all python files.        directory.
        """

        self.assertTrue(PostfixExclude(['py']).check(self.file_gitignore))
        self.assertTrue(PostfixExclude(['py']).check(self.file_authors))
        self.assertTrue(PostfixExclude(['py']).check(self.file_bin))

        self.assertFalse(PostfixExclude(['py']).check(self.file_py))
        self.assertFalse(PostfixExclude(['py']).check(self.file__init__))


class TestCommitConditions(unittest.TestCase):
    """
    Tests for Commit Conditions, the Commit hierarchy of
    classes in the conditions module.
    """

    def setUp(self):
        """
        Run before each test to initialize test files.
        """

        self.items = read_file('data/test_commits_data_2.json')

        class Temp(Metric):
            """
            The Temp class.

            A temporary sub-class of the code_df.Metric class.

            It overrides the __init__ method so that there is no
            implicit call to the set_commits and _filterout methods while
            instantiating an object of this class, which happens in the case of
            the Commit class.
            """

            def __init__(self, items, date_range=(None, None),
                         is_code=[Naive()], conds=[]):

                (self.since, self.until) = date_range
                self.is_code = is_code
                self.conds = conds

                super().__init__(items)

        self.Temp = Temp
        self.Temp._flatten = CommitGit._flatten

    def test_set_commits_master_include(self):
        """
        Test whether the set_commits method of the MasterInclude
        class correctly identifies commits made on the master branch.
        """

        temp = self.Temp(self.items, conds=[MasterInclude()])
        master_include = temp.conds[0]
        master_include.set_commits(temp.df)

        commit = CommitGit(self.items, conds=[MasterInclude()])
        self.assertEqual(master_include.included, commit.conds[0].included)

    def test_set_commits_empty_exclude(self):
        """
        Test whether the set_commits method of the EmptyExclude
        class correctly identifies empty commits.
        """

        temp = self.Temp(self.items, conds=[EmptyExclude()])
        empty_exclude = temp.conds[0]
        empty_exclude.set_commits(temp.df)

        commit = CommitGit(self.items, conds=[EmptyExclude()])
        self.assertEqual(empty_exclude.included, commit.conds[0].included)

    def test_set_commits_merge_exclude(self):
        """
        Test whether the set_commits method of the EmptyExclude
        class correctly identifies merge commits.
        """

        temp = self.Temp(self.items, conds=[MergeExclude()])
        merge_exclude = temp.conds[0]
        merge_exclude.set_commits(temp.df)

        commit = CommitGit(self.items, conds=[MergeExclude()])
        self.assertEqual(merge_exclude.included, commit.conds[0].included)


if __name__ == '__main__':
    unittest.main(verbosity=2)
