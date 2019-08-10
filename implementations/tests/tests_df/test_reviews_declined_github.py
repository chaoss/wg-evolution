import unittest
import json

from pandas.util.testing import assert_frame_equal

from implementations.code_df.reviews_declined_github import ReviewsDeclinedGitHub


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


class TestReviewsDeclinedGitHub(unittest.TestCase):

    def setUp(self):
        """
        Run before each test to read the test data file
        """

        self.items = read_file('data/test_pulls_data.json')

    def test_compute(self):
        """
        Test the compute method of a ReviewsDeclinedGitHub
        object with default parameters.
        """

        reviews = ReviewsDeclinedGitHub(self.items)
        expected_count = 2
        count = reviews.compute()
        self.assertEqual(expected_count, count)

    def test__agg(self):
        """
        Test the _agg method of a ReviewsDeclinedGitHub
        object with default parameters when re-sampling
        on a weekly basis.
        """

        reviews_declined = ReviewsDeclinedGitHub(self.items)
        reviews_declined.df = reviews_declined.df.set_index('created_date')
        test_df = reviews_declined.df.copy(deep=True)

        test_df = test_df[~test_df['merged']
                          & (test_df['current_status'] == 'closed')]
        test_df = test_df.resample('W')['category'].agg(['count'])

        reviews_declined.df = reviews_declined._agg(reviews_declined.df, 'W')
        assert_frame_equal(test_df, reviews_declined.df)


if __name__ == '__main__':
    unittest.main(verbosity=2)
