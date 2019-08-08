import datetime
import unittest
import json
from pandas.util.testing import assert_frame_equal

import sys
sys.path.append('..')

from code_df.issue_github import IssueGitHub


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


class TestIssueGitHub(unittest.TestCase):
    """
    Class to test the IssueGitHub class.
    """

    def setUp(self):
        """
        Run before each test to read the test data file
        """

        self.items = read_file('test_issues_data.json')

    def test__flatten_valid_input(self):
        """
        Test for valid input. An issue that satisfies all conditions
        passed while creating a IssueGitHub object for testing. A
        properly flattened issue is expected.
        """

        issue = IssueGitHub(self.items)

        flat_item = issue._flatten(self.items[0])
        flat_expected = [
            {
                'repo': 'https://github.com/atom/language-java',
                'hash': 41815742,
                'category': 'issue',
                'author': 'kevinsawicki',
                'created_date': datetime.datetime(2011, 3, 15, 0, 0),
                'current_status': "closed",
             }
        ]
        self.assertEqual(flat_item, flat_expected)

    def test__flatten_invalid_input(self):
        """
        Test for invalid input. An empty list is expected to be
        returned.
        """

        # date in future, hence no issue will satisfy date check
        date_since = datetime.datetime.strptime("2020-09-20", "%Y-%m-%d")
        issue = IssueGitHub(self.items, date_range=(date_since, None))

        flat_item = issue._flatten(self.items[0])
        flat_expected = []
        self.assertEqual(flat_item, flat_expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
