import unittest
import sys
sys.path.append('..')
from code_df.commit import Commit
from code_df import utils
from pandas.util.testing import assert_frame_equal
import json


def read_file(path):
    items = list()
    with open(path, 'r') as raw_data:
        for line in raw_data:
            line = json.loads(line)

            items.append(line)
    return items


class TestMetric(unittest.TestCase):
    """
    Tests for the Metric class
    """

    def setUp(self):
        self.items = read_file('test_commits_data.json')

    def test_time_series_commit(self):
        """
        Test whether time_series correctly sets the
        index of the DataFrame to the `created_date` column
        """
        class Temp(Commit):

            def _agg(self, df, period):
                return df

            def _flatten(self, item):
                """
                Flatten a raw commit fetched by Perceval into a flat
                dictionary.

                A list with a single flat directory will be returned.
                That dictionary will have the elements we need for
                computing metrics. The list may be empty, if for some
                reason the commit should not be considered.

                :param item: raw item fetched by Perceval (dictionary)
                :returns:    list of a single flat dictionary
                """

                creation_date = utils.str_to_date(item['data']['AuthorDate'])
                if self.since and (self.since > creation_date):
                    return []

                if self.until and (self.until < creation_date):
                    return []

                code_files = [file['file'] for file in item['data']['files'] if
                              all(condition.check(file['file'])
                                  for condition in self.is_code)]

                if len(code_files) > 0:
                    flat = {
                        'repo': item['origin'],
                        'hash': item['data']['commit'],
                        'author': item['data']['Author'],
                        'category': "commit",
                        'created_date': creation_date,
                    }

                    return [flat]

                else:
                    return []

        temp = Temp(self.items)
        expected_df = temp.df
        expected_df = expected_df.set_index('created_date')
        returned_df = temp.time_series('W')

        assert_frame_equal(expected_df, returned_df)


if __name__ == '__main__':
    unittest.main(verbosity=2)
