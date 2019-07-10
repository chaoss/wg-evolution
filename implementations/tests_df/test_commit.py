import datetime
import unittest
import json

import sys
sys.path.append('..')
from code_df.commit import Commit
from code_df import utils
from code_df import conditions
from pandas.util.testing import assert_frame_equal


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


class Test_filterout(unittest.TestCase):
    """
    Class to test the _filterout method, defined in the Commit class.
    """

    def setUp(self):
        """
        Run before each test to read the test data file
        """

        self.items = read_file('test_commits_data.json')

        class Temp(Commit):
            """
            The Temp class.

            A temporary sub-class of the code_df.Commit class.

            It overrides the __init__ method so that there is no
            implicit call to the _filterout method while instantiating
            an object of this class, which happens in the case of
            the Commit class.
            """

            def __init__(self, items, date_range=(None, None),
                         is_code=[conditions.Naive()], conds=[]):

                (self.since, self.until) = date_range
                self.is_code = is_code
                self.conds = conds
                super().__init__(items)

                # Initialize conditions
                for condition in self.conds:
                    if isinstance(condition, conditions.Commit):
                        condition.set_commits(self.df)
        self.temp_class = Temp

    def test__filterout(self):
        """
        Test whether _filterout works as expected
        when no condition is passed.
        """
        temp = self.temp_class(self.items, conds=[])
        expected_df = temp.df
        for condition in temp.conds:
            for index, row in expected_df.iterrows():
                if not condition.check(row['hash']):
                    expected_df.drop(index, inplace=True)

        for condition in temp.conds:
            self._filterout(condition)

        assert_frame_equal(expected_df, temp.df)

    def test__filterout_MasterInclude(self):
        """
        Test whether _filterout includes only master commits
        when this condition is passed
        """
        temp = self.temp_class(self.items, conds=[conditions.MasterInclude()])
        expected_df = temp.df
        for condition in temp.conds:
            for index, row in expected_df.iterrows():
                if not condition.check(row['hash']):
                    expected_df.drop(index, inplace=True)

        for condition in temp.conds:
            self._filterout(condition)

        assert_frame_equal(expected_df, temp.df)

    def test__filterout_EmptyExclude(self):
        """
        Test whether _filterout excludes empty
        commits when this condition is passed
        """
        temp = self.temp_class(self.items, conds=[conditions.EmptyExclude()])
        expected_df = temp.df
        for condition in temp.conds:
            for index, row in expected_df.iterrows():
                if not condition.check(row['hash']):
                    expected_df.drop(index, inplace=True)

        for condition in temp.conds:
            self._filterout(condition)

        assert_frame_equal(expected_df, temp.df)

    def test__filterout_MergeExclude(self):
        """
        Test whether _filterout excludes merge
        commits when this condition is passed
        """
        temp = self.temp_class(self.items, conds=[conditions.MergeExclude()])
        expected_df = temp.df
        for condition in temp.conds:
            for index, row in expected_df.iterrows():
                if not condition.check(row['hash']):
                    expected_df.drop(index, inplace=True)

        for condition in temp.conds:
            self._filterout(condition)

        assert_frame_equal(expected_df, temp.df)


class Test_flatten(unittest.TestCase):
    """
    Class to the _flatten method, defined in the Commit class.
    """

    def setUp(self):
        """
        Run before each test to read the test data file
        """

        self.items = utils.read_file('test_commits_data.json')

    def test__flatten_valid_input(self):
        """
        Test for valid input. A commit that satisfies all conditions
        passed while creating the Commit object for testing. A properly
        flattened commit is expected.
        """

        commit = Commit(self.items)

        flat_item = commit._flatten(self.items[0])
        flat_expected = [
            {
                'repo': 'http://github.com/chaoss/grimoirelab-perceval',
                'hash': 'dc78c254e464ff334892e0448a23e4cfbfc637a3',
                'author': 'Santiago Dueñas <sduenas@bitergia.com>',
                'category': 'commit',
                'created_date': datetime.datetime(2015, 8, 18, 0, 0),
                'committer': 'Santiago Dueñas <sduenas@bitergia.com>',
                'commit_date': datetime.datetime(2015, 8, 18, 0, 0),
                'files_no': 3,
                'refs': [],
                'parents': [],
                'files': [
                    {'action': 'A', 'added': '10', 'file': '.gitignore',
                     'indexes': ['0000000', 'ceaedd5'],
                        'modes': ['000000', '100644'], 'removed': '0'},
                    {'action': 'A', 'added': '1', 'file': 'AUTHORS',
                     'indexes': ['0000000', 'a67f214'],
                        'modes': ['000000', '100644'], 'removed': '0'},
                    {'action': 'A', 'added': '674', 'file': 'LICENSE',
                     'indexes': ['0000000', '94a9ed0'],
                        'modes': ['000000', '100644'], 'removed': '0'}],
                'files_action': 3,
                'merge': False
             }
        ]
        self.assertEqual(flat_item, flat_expected)

    def test__flatten_invalid_input(self):
        """
        Test for invalid input. An empty list is expected to be
        returned.
        """

        # date in future, hence no commit will satisfy date check
        date_since = datetime.datetime.strptime("2020-09-20", "%Y-%m-%d")
        commit = Commit(self.items, date_range=(date_since, None))

        flat_item = commit._flatten(self.items[0])
        flat_expected = []
        self.assertEqual(flat_item, flat_expected)

    def test__flatten_DirExclude(self):
        """
        Test whether _flatten correctly excludes commits based
        on DirExclude. It tests against the default value for
        the `dirs` parameter: ['tests', 'bin']
        """

        commit = Commit(self.items, is_code=[conditions.DirExclude()])
        expected_df = Commit(self.items).df

        for index, item in expected_df.iterrows():

            valid_files = [file['file'] for file in item['files'] if
                           all(condition.check(file['file'])
                               for condition in commit.is_code)]

            if len(valid_files) == 0:
                expected_df.drop(index, inplace=True)
        expected_df = expected_df.reset_index(drop=True)
        assert_frame_equal(expected_df, commit.df)

    def test__flatten_PostfixExclude(self):
        """
        Test whether _flatten correctly excludes commits based
        on PostfixExclude condition. The default file types of
        markdown(.md) and README are excluded in this test.
        """

        commit = Commit(self.items, is_code=[conditions.PostfixExclude()])
        expected_df = Commit(self.items).df

        for index, item in expected_df.iterrows():

            valid_files = [file['file'] for file in item['files'] if
                           all(condition.check(file['file'])
                               for condition in commit.is_code)]

            if len(valid_files) == 0:
                expected_df.drop(index, inplace=True)
        expected_df = expected_df.reset_index(drop=True)
        assert_frame_equal(expected_df, commit.df)


if __name__ == '__main__':
    unittest.main(verbosity=2)
