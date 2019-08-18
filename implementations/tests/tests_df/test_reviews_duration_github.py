import unittest
import json

from pandas.util.testing import assert_frame_equal

from implementations.code_df.reviews_duration_github import ReviewsDurationGitHub


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


class TestReviewsDurationGitHub(unittest.TestCase):

    def setUp(self):
        """
        Run before each test to read the test data file
        """

        self.items = read_file('data/test_pulls_data.json')

    def test_compute(self):
        """
        Test the compute method of a ReviewsDurationGitHub
        object with default parameters.
        """

        reviews_duration = ReviewsDurationGitHub(self.items)
        expected_median = 0.5
        median_duration = reviews_duration.compute()
        self.assertEqual(expected_median, median_duration)

    def test__agg(self):
        """
        Test the _agg method of a ReviewsDurationGitHub
        object with default parameters when re-sampling
        on a weekly basis.
        """

        reviews_duration = ReviewsDurationGitHub(self.items)
        reviews_duration.df = reviews_duration.df.set_index('created_date')
        test_df = reviews_duration.df.copy(deep=True)

        test_df = test_df.resample('W')['duration'].agg(['median'])
        test_df = test_df.dropna()

        reviews_duration.df = reviews_duration._agg(reviews_duration.df, 'W')

        print(test_df)
        assert_frame_equal(test_df, reviews_duration.df)

    def test__get_params(self):
        """
        Test whether the _get_params method correctly returns
        the expected parameters for plotting a timeseries plot
        for the Reviews Duration metric.
        """

        changes = ReviewsDurationGitHub(self.items)
        params = changes._get_params()

        expected_params = {
            'x': None,
            'y': 'median',
            'title': "Trends in the Duration of Reviews",
            'use_index': True
        }

        self.assertEqual(expected_params, params)


if __name__ == '__main__':
    unittest.main(verbosity=2)
