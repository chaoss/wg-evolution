import pandas as pd
from Metric import Metric
import utils


class PullRequest(Metric):

    def __init__(self, data_list, date_range=(None, None)):
        """
        Initilizes self.df, the dataframe with one commit per row.

        :param data_list: A list of dictionaries, each element a
            line from the JSON file
        :param date_range: A tuple which represents the start and
            end date of interest
        """

        super().__init__(data_list)

        clean_data_list = list()
        self.since = date_range[0]
        self.until = date_range[1]

        for line in self.raw_df.iterrows():
            pull_request = line[1].to_dict()
            pull_request = self._clean_pull_request(pull_request)

            clean_data_list.append(pull_request)

        self.df = pd.DataFrame(clean_data_list)
        if self.since:
            for df in self.clean_dict.values():
                df = df[df['created_date']
                        >= utils.str_to_dt_other(self.since)]
        else:
            self.since = utils.get_date(self.df, "since")

        if self.until:
            for df in self.clean_dict.values():
                df = df[df['created_date']
                        < utils.str_to_dt_other(self.until)]
        else:
            self.until = utils.get_date(self.df, "until")

    def _clean_pull_request(line):
        cleaned_line = {
            'repo': line['origin'],
            'hash': line['data_id'],
            'category': "pull_request",
            'author': line['data_user']['login'],
            'created_date': line['data_created_at'],
            'current_status': line['data_state']
        }

        return cleaned_line
