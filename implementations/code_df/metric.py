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

    def _aggregate(self, series):
        """
        Aggregate the re-sampled DataFrame
        """

        raise NotImplementedError

    def compute_time_series(self, cols=None, period='M'):
        """
        The metric value is computed for each fixed interval of time
        from the "since" date to the "until" date arguments, specified
        during object initiation.

        The fixed time interval can be either a month or a week.

        :param cols: A list of columns on which aggregation will occur.
            In some cases, no particular column is required, for example,
            to get count. In this case, cols is set to the "category"
            column.

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
        # No particular column to aggregate on:
        if cols is None:
            cols = ['category']

        df = df[cols].resample(period).agg([self._aggregate])
        df.columns = df.columns.droplevel(0)

        return df
