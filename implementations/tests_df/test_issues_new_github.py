import unittest
import json
from pandas.util.testing import assert_frame_equal

import sys
sys.path.append('..')

from code_df.issues_new_github import IssuesNewGitHub


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


class TestIssuesNewGitHub(unittest.TestCase):

    def setUp(self):
        """
        Run before each test to read the test data file
        """

        self.items = read_file('test_issues_data.json')

    def test_compute(self):
        """
        Test the compute method of a IssuesNewGitHub
        object instantiated with default parameters.
        """

        issues = IssuesNewGitHub(self.items)
        expected_count = 20
        count = issues.compute()
        self.assertEqual(expected_count, count)

    def test__agg(self):
        """
        Test the _agg method of a IssuesNewGitHub
        object with default parameters when re-sampling
        on a weekly basis.
        """

        issues = IssuesNewGitHub(self.items)
        issues.df = issues.df.set_index('created_date')
        test_df = issues.df
        test_df = test_df.resample('W')['category'].agg(['count'])

        issues.df = issues._agg(issues.df, 'W')
        assert_frame_equal(test_df, issues.df)


if __name__ == '__main__':
    unittest.main(verbosity=2)
