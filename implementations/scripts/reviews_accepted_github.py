from datetime import datetime

import utils
from pullrequest_github import PullRequestGitHub


class ReviewsAccepted(PullRequestGitHub):
    """
    Class for Reviews Accepted
    """

    def compute(self):
        """
        Compute the total number of reviews which were accepted, from
        the Perceval data.

        :returns: The total number of reviews accepted
        """

        pull_ids = {item['hash'] for item in self.items
                    if item['merged'] is True}

        return len(pull_ids)


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = utils.read_json_file('../pull_requests.json')

    # total accepted reviews
    reviews_accepted = ReviewsAccepted(items)
    print("The total number of reviews accepted is {}"
          .format(reviews_accepted.compute()))

    # accepted reviews created after a certain date
    reviews_accepted = ReviewsAccepted(items, (date_since, None))
    print("The number of reviews created after 2018-09-07 which were accepted"
          "is {}"
          .format(reviews_accepted.compute()))

    print("The trends in the number of accepted reviews created"
          " from 2018-09-07 onwards are: ")
    print(reviews_accepted.time_series('M'))
