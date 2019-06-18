import pandas as pd

class Metric():
    """
    Create a dataframe from items fetched by Perceval

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
