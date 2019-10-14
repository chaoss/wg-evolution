# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CHAOSS
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     Aniruddha Karajgi <akarajgi0@gmail.com>
#

from datetime import datetime

from implementations.scripts.pullrequest_github import PullRequestGitHub
from implementations.scripts.utils import read_json_file


class ReviewsAcceptedGitHub(PullRequestGitHub):
    """
    Class for the Reviews Accepted metric (non-pandas)
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

    def __str__(self):
        return "Reviews Accepted"


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = read_json_file('../pull_requests.json')

    # total accepted reviews
    reviews_accepted = ReviewsAcceptedGitHub(items)
    print("The total number of reviews accepted is {}"
          .format(reviews_accepted.compute()))

    # accepted reviews created after a certain date
    reviews_accepted = ReviewsAcceptedGitHub(items, (date_since, None))
    print("The number of reviews created after 2018-09-07 which were accepted"
          "is {}"
          .format(reviews_accepted.compute()))

    print("The trends in the number of accepted reviews created"
          " from 2018-09-07 onwards are: ")
    print(reviews_accepted.time_series('M'))
