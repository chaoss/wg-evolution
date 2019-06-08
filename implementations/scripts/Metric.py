import datetime
import pandas as pd
from . import utils


class Metric():
    
    def __init__(self, data_list):
        """
        Create a dataframe from data-list, which is the data 
        fetched by Perceval

        :param data_list: a list of dictionaries, where each line
            is a data line in the JSON file fetched by Perceval
        """

        data_list_flattened = Metric._flatten_data(data_list)
        self.raw_df = pd.DataFrame(data_list_flattened)

    @staticmethod
    def _flatten_data(data_list):
        data_rows = list()

        for data_line in data_list:
            row = dict()
            for key, val in data_line.items():
                if isinstance(val, dict):
                    for sub_key, sub_val in val.items():
                        row[key + "_" + sub_key] = sub_val
                else:
                    row[key] = val
            data_rows.append(row)
        return data_rows
