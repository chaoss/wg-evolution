import unittest
from datetime import datetime
from copy import deepcopy
import json

from implementations.scripts.issue_github import IssueGithub


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


class TestIssueGithub(unittest.TestCase):
    """
    Class to test the IssueGithub class.
    """

    def setUp(self):
        """
        Run before each test to read the test data file
        """
        self.items = read_file('data/test_issues_events_data.json')

    def test__flatten_valid_input(self):
        """
        Test for valid input.An issue that satisfies all conditions
        passed while creating a IssueGithub object for testing.A properly flattened issue is expected.
        """
        issue = IssueGithub(self.items)

        flat_item = issue._flatten(self.items[0])
        flat_expected = [
            {
                'repo': 'https://github.com/chaoss/wg-evolution',
                'hash': 326952120,
                'category': 'issue',
                'author': 'aswanipranjal',
                'created_date': datetime(2018, 5, 28, 0, 0),
                'current_status': "closed",
                'events_data': [
                            {'actor':
                                {'avatar_url': 'https://avatars1.githubusercontent.com/u/9946566?v=4',
                                 'events_url': 'https://api.github.com/users/aswanipranjal/events{/privacy}',
                                 'followers_url': 'https://api.github.com/users/aswanipranjal/followers',
                                 'following_url': 'https://api.github.com/users/aswanipranjal/following{/other_user}',
                                 'gists_url': 'https://api.github.com/users/aswanipranjal/gists{/gist_id}',
                                 'gravatar_id': '',
                                 'html_url': 'https://github.com/aswanipranjal',
                                 'id': 9946566,
                                 'login': 'aswanipranjal',
                                 'node_id': 'MDQ6VXNlcjk5NDY1NjY=',
                                 'organizations_url': 'https://api.github.com/users/aswanipranjal/orgs',
                                 'received_events_url': 'https://api.github.com/users/aswanipranjal/received_events',
                                 'repos_url': 'https://api.github.com/users/aswanipranjal/repos',
                                 'site_admin': False,
                                 'starred_url': 'https://api.github.com/users/aswanipranjal/starred{/owner}{/repo}',
                                 'subscriptions_url': 'https://api.github.com/users/aswanipranjal/subscriptions',
                                 'type': 'User',
                                 'url': 'https://api.github.com/users/aswanipranjal'},
                             'commit_id': '5608435a9c7ea16a4e57e18c8e723f5dbb2b9252',
                             'commit_url': 'https://api.github.com/repos/aswanipranjal/grimoirelab-elk/commits/'
                                '5608435a9c7ea16a4e57e18c8e723f5dbb2b9252',
                             'created_at': '2018-06-24T05:54:26Z', 'event': 'referenced', 'id': 1697477931,
                             'node_id': 'MDE1OlJlZmVyZW5jZWRFdmVudDE2OTc0Nzc5MzE=',
                             'url': 'https://api.github.com/repos/chaoss/wg-evolution/issues/events/1697477931'},
                            {'actor':
                                {'avatar_url': 'https://avatars1.githubusercontent.com/u/9946566?v=4',
                                 'events_url': 'https://api.github.com/users/aswanipranjal/events{/privacy}',
                                 'followers_url': 'https://api.github.com/users/aswanipranjal/followers',
                                 'following_url': 'https://api.github.com/users/aswanipranjal/following{/other_user}',
                                 'gists_url': 'https://api.github.com/users/aswanipranjal/gists{/gist_id}',
                                 'gravatar_id': '', 'html_url': 'https://github.com/aswanipranjal',
                                 'id': 9946566,
                                 'login': 'aswanipranjal',
                                 'node_id': 'MDQ6VXNlcjk5NDY1NjY=',
                                 'organizations_url': 'https://api.github.com/users/aswanipranjal/orgs',
                                 'received_events_url': 'https://api.github.com/users/aswanipranjal/received_events',
                                 'repos_url': 'https://api.github.com/users/aswanipranjal/repos',
                                 'site_admin': False,
                                 'starred_url': 'https://api.github.com/users/aswanipranjal/starred{/owner}{/repo}',
                                 'subscriptions_url': 'https://api.github.com/users/aswanipranjal/subscriptions',
                                 'type': 'User',
                                 'url': 'https://api.github.com/users/aswanipranjal'},
                             'commit_id': '00a74ed7a5d2066650ead8cf3405f34c650f922f',
                             'commit_url': 'https://api.github.com/repos/aswanipranjal/grimoirelab-elk/commits/'
                                '00a74ed7a5d2066650ead8cf3405f34c650f922f',
                             'created_at': '2018-06-24T09:25:21Z',
                             'event': 'referenced',
                             'id': 1697531561,
                             'node_id': 'MDE1OlJlZmVyZW5jZWRFdmVudDE2OTc1MzE1NjE=',
                             'url': 'https://api.github.com/repos/chaoss/wg-evolution/issues/events/1697531561'},
                            {'actor':
                                {'avatar_url': 'https://avatars1.githubusercontent.com/u/9946566?v=4',
                                 'events_url': 'https://api.github.com/users/aswanipranjal/events{/privacy}',
                                 'followers_url': 'https://api.github.com/users/aswanipranjal/followers',
                                 'following_url': 'https://api.github.com/users/aswanipranjal/following{/other_user}',
                                 'gists_url': 'https://api.github.com/users/aswanipranjal/gists{/gist_id}',
                                 'gravatar_id': '',
                                 'html_url': 'https://github.com/aswanipranjal',
                                 'id': 9946566,
                                 'login': 'aswanipranjal', 'node_id': 'MDQ6VXNlcjk5NDY1NjY=',
                                 'organizations_url': 'https://api.github.com/users/aswanipranjal/orgs',
                                 'received_events_url': 'https://api.github.com/users/aswanipranjal/received_events',
                                 'repos_url': 'https://api.github.com/users/aswanipranjal/repos', 'site_admin': False,
                                 'starred_url': 'https://api.github.com/users/aswanipranjal/starred{/owner}{/repo}',
                                 'subscriptions_url': 'https://api.github.com/users/aswanipranjal/subscriptions', 'type': 'User',
                                 'url': 'https://api.github.com/users/aswanipranjal'},
                             'commit_id': 'd6e577a436a433875fbc9483eb9dceacd5975757',
                             'commit_url': 'https://api.github.com/repos/aswanipranjal/grimoirelab-elk/commits/'
                                'd6e577a436a433875fbc9483eb9dceacd5975757',
                             'created_at': '2018-06-25T08:42:13Z', 'event': 'referenced', 'id': 1698333888,
                             'node_id': 'MDE1OlJlZmVyZW5jZWRFdmVudDE2OTgzMzM4ODg=',
                             'url': 'https://api.github.com/repos/chaoss/wg-evolution/issues/events/1698333888'},
                            {'actor':
                                {'avatar_url': 'https://avatars0.githubusercontent.com/u/209533?v=4',
                                 'events_url': 'https://api.github.com/users/acs/events{/privacy}',
                                 'followers_url': 'https://api.github.com/users/acs/followers',
                                 'following_url': 'https://api.github.com/users/acs/following{/other_user}',
                                 'gists_url': 'https://api.github.com/users/acs/gists{/gist_id}', 'gravatar_id': '',
                                 'html_url': 'https://github.com/acs', 'id': 209533, 'login': 'acs',
                                 'node_id': 'MDQ6VXNlcjIwOTUzMw==',
                                 'organizations_url': 'https://api.github.com/users/acs/orgs',
                                 'received_events_url': 'https://api.github.com/users/acs/received_events',
                                 'repos_url': 'https://api.github.com/users/acs/repos', 'site_admin': False,
                                 'starred_url': 'https://api.github.com/users/acs/starred{/owner}{/repo}',
                                 'subscriptions_url': 'https://api.github.com/users/acs/subscriptions',
                                 'type': 'User', 'url': 'https://api.github.com/users/acs'},
                             'commit_id': None, 'commit_url': None,
                             'created_at': '2018-06-27T05:18:44Z',
                             'event': 'closed', 'id': 1702997519,
                             'node_id': 'MDExOkNsb3NlZEV2ZW50MTcwMjk5NzUxOQ==',
                             'url': 'https://api.github.com/repos/chaoss/wg-evolution/issues/events/1702997519'},
                            {'actor':
                                {'avatar_url': 'https://avatars0.githubusercontent.com/u/209533?v=4',
                                 'events_url': 'https://api.github.com/users/acs/events{/privacy}',
                                 'followers_url': 'https://api.github.com/users/acs/followers',
                                 'following_url': 'https://api.github.com/users/acs/following{/other_user}',
                                 'gists_url': 'https://api.github.com/users/acs/gists{/gist_id}',
                                 'gravatar_id': '', 'html_url': 'https://github.com/acs', 'id': 209533,
                                 'login': 'acs', 'node_id': 'MDQ6VXNlcjIwOTUzMw==',
                                 'organizations_url': 'https://api.github.com/users/acs/orgs',
                                 'received_events_url': 'https://api.github.com/users/acs/received_events',
                                 'repos_url': 'https://api.github.com/users/acs/repos', 'site_admin': False,
                                 'starred_url': 'https://api.github.com/users/acs/starred{/owner}{/repo}',
                                 'subscriptions_url': 'https://api.github.com/users/acs/subscriptions',
                                 'type': 'User', 'url': 'https://api.github.com/users/acs'},
                             'commit_id': 'd3091449479937135d3006b3369ca3d75294509b',
                             'commit_url': 'https://api.github.com/repos/chaoss/grimoirelab-elk/commits/'
                                'd3091449479937135d3006b3369ca3d75294509b',
                             'created_at': '2018-06-27T05:18:45Z', 'event': 'referenced', 'id': 1702997541,
                             'node_id': 'MDE1OlJlZmVyZW5jZWRFdmVudDE3MDI5OTc1NDE=',
                             'url': 'https://api.github.com/repos/chaoss/wg-evolution/issues/events/1702997541'}
                ]
            }
        ]

        self.assertEqual(flat_item, flat_expected)

    def test__flatten_invalid_input_since(self):
        """
        Test for invalid input. An empty list is expected to be returned.
        """
        # date in future, hence no issue will satisfy date check
        date_since = datetime.strptime("2020-09-20", "%Y-%m-%d")
        issue = IssueGithub(self.items, date_range=(date_since, None))

        flat_item = issue._flatten(self.items[0])
        flat_expected = []
        self.assertEqual(flat_item, flat_expected)

    def test__flatten_invalid_input_until(self):
        """
        Test for invalid input. An empty list is expected to be returned.
        """
        # date in past, hence no issue will satisfy date check
        date_until = datetime.strptime("1800-09-20", "%Y-%m-%d")
        issue = IssueGithub(self.items, date_range=(None, date_until))

        flat_item = issue._flatten(self.items[0])
        flat_expected = []
        self.assertEqual(flat_item, flat_expected)

    def test__add_item(self):
        """
        Test whether _add_item creates a modified copy of a
        passed item as expected.
        """
        issue = IssueGithub(self.items)
        item = issue.items[0]
        new_date = datetime.strptime("2018-05-01", "%Y-%m-%d")
        new_item = issue._add_item(item, new_date, 'closed')

        expected_item = deepcopy(item)
        expected_item.update(created_date=new_date, current_status='closed')
        self.assertDictEqual(expected_item, new_item)

    def test__update_with_reopened_items(self):
        """
        Test whether _update_with_reopened_items correctly updates
        the reopened issue.

        test_issue_reopened.json file contains only one issue,
        this issue is an reopened issue.
        """
        item = read_file('data/test_issue_reopened.json')
        issue = IssueGithub(item, reopen_as_new=True)
        self.assertEqual(len(issue.items), 2)
        self.assertEqual(issue.items[0]['current_status'], 'closed')
        self.assertEqual(issue.items[1]['current_status'], 'closed')

    def test_items_contain_no_issue(self):
        items = read_file('data/test_pulls_data.json')
        issue = IssueGithub(items)
        self.assertEqual(len(issue.items), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
