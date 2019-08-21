import unittest
import json
from pandas.util.testing import assert_frame_equal

from implementations.code_df.issues_closed_github import IssuesClosedGitHub


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


class TestIssuesClosedGitHub(unittest.TestCase):

    def setUp(self):
        """
        Run before each test to read the test data file
        """

        self.items = read_file('data/test_issues_events_data.json')

    def test_compute(self):
        """
        Test the compute method of a IssuesClosedGitHub
        object instantiated with default parameters.
        """

        issues = IssuesClosedGitHub(self.items)
        expected_count = 20
        count = issues.compute()
        self.assertEqual(expected_count, count)

    def test_compute_reopen_as_new(self):
        """
        Test whether the reopen_as_new parameter works as expected.
        """

        issues = IssuesClosedGitHub(self.items, reopen_as_new=True)
        expected_count = 21
        count = issues.compute()
        self.assertEqual(expected_count, count)

    def test__agg(self):
        """
        Test the _agg method of a IssuesClosedGitHub
        object with default parameters when re-sampling
        on a weekly basis.
        """

        issues = IssuesClosedGitHub(self.items)
        issues.df = issues.df.set_index('created_date')
        test_df = issues.df
        test_df = test_df.resample('W')['category'].agg(['count'])

        issues.df = issues._agg(issues.df, 'W')
        assert_frame_equal(test_df, issues.df)

    def test__get_params(self):
        """
        Test whether the _get_params method correctly returns
        the expected parameters for plotting a timeseries plot
        for the Issues Closed metric.
        """

        changes = IssuesClosedGitHub(self.items)
        params = changes._get_params()

        expected_params = {
            'x': None,
            'y': 'count',
            'title': "Trends in Issues Closed",
            'use_index': True
        }

        self.assertEqual(expected_params, params)


if __name__ == '__main__':
    unittest.main(verbosity=2)
