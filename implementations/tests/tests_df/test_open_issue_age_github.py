import unittest
import json

from pandas.util.testing import assert_frame_equal

from implementations.code_df.open_issue_age_github import OpenIssueAgeGitHub


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


class TestOpenIssueAgeGitHub(unittest.TestCase):

    def setUp(self):
        """
        Run before each test to read the test data file
        """

        self.items = read_file('data/test_issues_data.json')

    def test_compute(self):
        """
        Test the compute method of a OpenIssueAgeGitHub
        object with default parameters.
        """

        open_issue_age = OpenIssueAgeGitHub(self.items)
        expected_mean = 1132.0
        mean_age = open_issue_age.compute()
        self.assertEqual(expected_mean, mean_age)

    def test__agg(self):
        """
        Test the _agg method of a OpenIssueAgeGitHub
        object with default parameters when re-sampling
        on a weekly basis.
        """

        open_issue_age = OpenIssueAgeGitHub(self.items)

        open_issue_age.df = open_issue_age.df.set_index('created_date')
        test_df = open_issue_age.df.copy(deep=True)

        test_df = test_df.resample('W')['open_issue_age'].agg(['mean'])
        test_df = test_df.dropna()

        open_issue_age.df = open_issue_age._agg(open_issue_age.df, 'W')
        print(open_issue_age.df)
        assert_frame_equal(test_df, open_issue_age.df)

    def test__get_params(self):
        """
        Test whether the _get_params method correctly returns
        the expected parameters for plotting a timeseries plot
        for the Open Issue Age metric.
        """

        open_issue_age = OpenIssueAgeGitHub(self.items)
        params = open_issue_age._get_params()

        expected_params = {
            'x': None,
            'y': 'mean',
            'title': "Trends in Open Issue Age",
            'use_index': True
        }

        self.assertEqual(expected_params, params)


if __name__ == '__main__':
    unittest.main(verbosity=2)
