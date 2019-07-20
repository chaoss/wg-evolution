import unittest
import json
import sys
sys.path.append('..')

# from code_df.metric import Metric
# from code_df import utils
# from code_df.code_changes_git import CodeChangesGit
from code_df.conditions import (
            Naive, DirExclude, PostfixExclude,
            MasterInclude, MergeExclude, EmptyExclude
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

        commits = read_file('test_commits_data.json')
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

        commits = read_file('test_commits_data.json')
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

        commits = read_file('test_commits_data.json')
        self.file_gitignore = commits[0]['data']['files'][0]['file']
        self.file__init__ = commits[8]['data']['files'][0]['file']
        self.file_bin = commits[2]['data']['files'][0]['file']
        self.file_py = commits[4]['data']['files'][0]['file']
        self.file_authors = commits[0]['data']['files'][1]['file']
        self.file_md = commits[20]['data']['files'][0]['file']

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

        self.assertFalse(PostfixExclude().check(self.file_md))

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
        self.assertTrue(PostfixExclude([]).check(self.file_md))

    def test_check_exclude_py(self):
        """
        Test whether the check method of the PostfixExclude class
        correctly returns False for all python files.        directory.
        """

        self.assertTrue(PostfixExclude(['py']).check(self.file_gitignore))
        self.assertTrue(PostfixExclude(['py']).check(self.file_authors))
        self.assertTrue(PostfixExclude(['py']).check(self.file_bin))
        self.assertTrue(PostfixExclude(['py']).check(self.file_md))

        self.assertFalse(PostfixExclude(['py']).check(self.file_py))
        self.assertFalse(PostfixExclude(['py']).check(self.file__init__))


if __name__ == '__main__':
    unittest.main(verbosity=2)
