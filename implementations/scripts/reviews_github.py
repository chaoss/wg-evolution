from datetime import datetime

from implementations.scripts.pullrequest_github import PullRequestGitHub
from implementations.scripts.utils import read_json_file


class ReviewsGitHub(PullRequestGitHub):
    """
    Class for the Reviews metric (non-pandas)
    """

    def compute(self):
        """
        Compute the total number of reviews created, from the Perceval data.

        :returns: The total number of reviews created
        """

        pull_ids = {item['hash'] for item in self.items}
        return len(pull_ids)

    def __str__(self):
        return "Reviews"


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = read_json_file('../pull_requests.json')

    # total number of reviews
    reviews = ReviewsGitHub(items)
    print("The total number of reviews is {}"
          .format(reviews.compute()))

    # reviews created after a certain date
    reviews = ReviewsGitHub(items, (date_since, None))
    print("The number of reviews created after 2018-09-07 is {}"
          .format(reviews.compute()))
