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
