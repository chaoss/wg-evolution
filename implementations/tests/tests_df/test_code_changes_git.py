import json
import unittest

from pandas.util.testing import assert_frame_equal

from implementations.code_df.code_changes_git import CodeChangesGit


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

    def test__agg(self):
        """
        Test the _agg method of a CodeChangesGit
        object with default parameters when re-sampling
        on a weekly basis.
        """

        changes = CodeChangesGit(self.items)
        changes.df = changes.df.set_index('created_date')
        test_df = changes.df
        test_df = test_df.resample('W')['category'].agg(['count'])

        changes.df = changes._agg(changes.df, 'W')
        assert_frame_equal(test_df, changes.df)


if __name__ == '__main__':
    unittest.main(verbosity=2)
