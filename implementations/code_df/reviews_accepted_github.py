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


class ReviewsAcceptedGitHub(PullRequestGitHub):
    """
    Class for the Reviews Accepted metric
    """

    def compute(self):
        """
        Compute the total number of reviews which were accepted,
        from the Perceval data.

        :returns count: The total number of reviews accepted
        """

        count = len(self.df['hash'][self.df['merged']].unique())
        return count

    def _agg(self, df, period):
        """
        Perform an aggregation operation on a DataFrame to find
        the total number of reviews accepted in every
        interval of the period specified in the time_series method,
        like 'M', 'W',etc.

        It computes the count of the "category" column of the
        DataFrame for those rows with the 'merge' column having True.

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

        df = df[df['merged']]
        df = df.resample(period)['category'].agg(['count'])

        return df

    def _get_params(self):
        """
        Return parameters for creating a timeseries plot

        :returns: A dictionary with axes to plot, a title
            and if use_index should be true when creating
            the plot.
        """

        title = "Trends in Reviews Accepted"
        x = None
        y = 'count'
        use_index = True
        return {'x': x, 'y': y, 'title': title, 'use_index': use_index}

    def __str__(self):
        return "Reviews Accepted"


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = read_json_file('../pull_requests.json')

    # total number of reviews accepted
    reviews_accepted = ReviewsAcceptedGitHub(items)
    print("The total number of reviews accepted is {}"
          .format(reviews_accepted.compute()))

    # total number of reviews accepted after a particular date
    reviews_accepted = ReviewsAcceptedGitHub(items, (date_since, None))
    print("The number of reviews created after 2018-09-07 which were accepted is {}"
          .format(reviews_accepted.compute()))

    # time-series on a monthly basis
    print("The trends in the number of accepted reviews created"
          " from 2018-09-07 onwards are: ")
    print(reviews_accepted.time_series('M'))
