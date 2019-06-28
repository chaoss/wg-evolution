import pandas as pd


class Metric():
    """
    Create a DataFrame from items fetched by Perceval

    All classes computing metrics based on data frames
    will be descendents of this class.

    :param items: A list of dictionaries.
        Each element is a Perceval dictionary, obtained from a JSON
        file produced by Perceval, or directly from Perceval.
    """

    def __init__(self, items):

        flat_items = []
        for item in items:
            flat_items.extend(self._flatten(item))
        self.df = pd.DataFrame(flat_items)

    def _flatten(self, item):
        """
        Flattens an item into a list of flat dictionaries

        The produced dictionaries are intended to be used
        when building a data frame.
        This method will be overridden by descendant classes.

        :param item: item to flatten
        :return:     list of flat dictionaries

        """

        raise NotImplementedError

    def _agg(self, df, period):
        """
        Aggregate the DataFrame

        :param df: A pandas DataFrame
        """

        raise NotImplementedError

    def time_series(self, period='M'):
        """
        The metric value is computed for each fixed interval of time
        from the "since" date to the "until" date arguments, specified
        during object initiation.

        :param period: A string which can be any one of the pandas time
        series rules:
            'W': week
            'M': month
            'D': day

        :returns df: A DataFrame whose rows each represent an interval
            of "period" and the count for that interval
        """

        df = self.df

        df = df.set_index('created_date')
        df = self._agg(df, period)

        return df
