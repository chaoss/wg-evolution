import pandas as pd


class Metric():
    """
    Create a dataframe from items, which is the data
    fetched by Perceval

    :param items: A list of dictionaries.
        Each element is a Perceval dictionary, obtained from a JSON
        file or from Perceval directly.
    """

    def __init__(self, items):
        flat_items = self._flatten_data(items)
        self.raw_df = pd.DataFrame(flat_items)

    def _flatten_data(self, items):
        raise NotImplementedError
