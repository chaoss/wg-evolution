import unittest
import json

from pandas.util.testing import assert_frame_equal

from implementations.code_df.metric import Metric
from implementations.code_df.reviews import Reviews


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


class TestReviewsGitHub(unittest.TestCase):

    def setUp(self):
        """
        Run before each test to read the test data file
        """

        self.items = read_file('data/test_pulls_data.json')

    def test_compute_trivial(self):
        """
        Test the compute method of a ReviewsGitHub
        object with default parameters.
        """

        reviews = Reviews(self.items)
        expected_count = 20
        count = reviews.compute()
        self.assertEqual(expected_count, count)

    def test_compute_with_duplicate(self):
        """
        Test the compute method of a ReviewsGitHub
        object with default parameters but with a
        duplicate item in the test data.
        """

        items_temp = self.items
        items_temp.append(self.items[0])
        reviews = Reviews(items_temp)
        expected_count = 20
        count = reviews.compute()
        self.assertEqual(expected_count, count)

    def test__agg(self):
        """
        Test the _agg method of a ReviewsGitHub
        object with default parameters when re-sampling
        on a weekly basis.
        """

        reviews = Reviews(self.items)
        reviews.df = reviews.df.set_index('created_date')
        test_df = reviews.df
        test_df = test_df.resample('W')['category'].agg(['count'])

        reviews.df = reviews._agg(reviews.df, 'W')
        assert_frame_equal(test_df, reviews.df)


if __name__ == '__main__':
    unittest.main(verbosity=2)
