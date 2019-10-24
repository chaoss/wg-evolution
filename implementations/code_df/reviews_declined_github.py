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

from implementations.code_df.pullrequest_github import PullRequestGitHub
from implementations.code_df.utils import read_json_file


class ReviewsDeclinedGitHub(PullRequestGitHub):
    """
    Class for the Reviews Declined metric
    """

    def compute(self):
        """
        Compute the total number of reviews which were declined, from the
        Perceval data. Declined reviews are in the "closed" state but
        are not merged.

        :returns count: The total number of reviews declined
        """

        count = len(self.df['hash'][~self.df['merged']
                    & (self.df['current_status'] == 'closed')])
        return count

    def _agg(self, df, period):
        """
        Perform an aggregation operation on a DataFrame to find
        the total number of reviews declined in every
        interval of the period specified in the time_series method,
        like 'M', 'W',etc.

        It computes the count of the "category" column of the
        DataFrame for those rows with the 'merge' column having False.

        :param df: a pandas DataFrame on which the aggregation will be
            applied.

        :param period: A string which can be any one of the pandas time
            series rules:
            'W': week
            'M': month
            'D': day

        :returns df: The aggregated dataframe, where aggregations have
            been performed on the "category" column
        """

        df = df[~df['merged']
                & (df['current_status'] == 'closed')]
        df = df.resample(period)['category'].agg(['count'])

        return df

    def _get_params(self):
        """
        Return parameters for creating a timeseries plot

        :returns: A dictionary with axes to plot, a title
            and if use_index should be true when creating
            the plot.
        """

        title = "Trends in Reviews Declined"
        x = None
        y = 'count'
        use_index = True
        return {'x': x, 'y': y, 'title': title, 'use_index': use_index}

    def __str__(self):
        return "Reviews Declined"


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = read_json_file('../pull_requests.json')

    # total number of reviews declined
    reviews_declined = ReviewsDeclinedGitHub(items)
    print("The total number of reviews declined is {}"
          .format(reviews_declined.compute()))

    # number of reviews declined after a certain date
    reviews_declined = ReviewsDeclinedGitHub(items, (date_since, None))
    print("The number of reviews created after 2018-09-07"
          "which were declined is {}"
          .format(reviews_declined.compute()))

    # time-series on a monthly basis for the number of reviews declined
    print("The trends in the number of declined reviews, created"
          " from 2018-09-07 onwards, are: ")
    print(reviews_declined.time_series('M'))
