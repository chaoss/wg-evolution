from datetime import datetime

from implementations.scripts.pullrequest_github import PullRequestGitHub
from implementations.scripts.utils import read_json_file


class ReviewsDeclinedGitHub(PullRequestGitHub):
    """
    Class for the Reviews Declined metric (non-pandas)
    """

    def compute(self):
        """
        Compute the total number of reviews which were declined, from the
        Perceval data. Declined reviews are in the "closed" state but
        are not merged.

        :returns: The total number of reviews declined
        """

        pull_ids = {item['hash'] for item in self.items
                    if item['merged'] is False and item['current_status'] == 'closed'}

        return len(pull_ids)

    def __str__(self):
        return "Reviews Declined"


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = read_json_file('pull_requests.json')

    # total number of reviews declined
    reviews_declined = ReviewsDeclinedGitHub(items)
    print("The total number of reviews declined is {}"
          .format(reviews_declined.compute()))

    # number of reviews declined after a certain date
    reviews_declined = ReviewsDeclinedGitHub(items, (date_since, None))
    print("The number of reviews created after 2018-09-07 "
          "which were declined is {}"
          .format(reviews_declined.compute()))
