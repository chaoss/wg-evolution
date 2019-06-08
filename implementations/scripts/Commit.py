import json
import datetime
import pandas as pd
from .Metric import Metric
from . import utils
from .SourceCode import SourceCode


class Commit(Metric):

    def __init__(self, data_list, date_range=(None, None), source_code_obj=None):
        """
        Initilizes self.df, the dataframe with one commit per row.
        The source_code_exclude_list parameter is a list which contains file extensions
        which are to be ignored. All possible file extensions are allowed. 
        For files without a standard ".xyz" extension, like LICENCE or AUTHORS, the "others" 
        extension is used. 
        
        :param data_list: A list of dictionaries, each element a line from the JSON file
        :param date_range: A tuple which represents the start and end date of interest
        :param source_code_obj: An object of SourceCode, to be used to determine what comprises
            source code.
        """
                
        super().__init__(data_list)

        clean_data_list = list()
        self.since = date_range[0]
        self.until = date_range[1]

        for line in self.raw_df.iterrows():
            commit = line[1].to_dict()
            commit = self._clean_commit(commit)
            if source_code_obj is None or source_code_obj.is_source_code(commit):
                clean_data_list.append(commit)

        self.df = pd.DataFrame(clean_data_list)
        if self.since:
            for df in self.clean_dict.values():
                df = df[df['created_date'] >= utils.str_to_dt_other(self.since)]
        else: 
            self.since = utils.get_date(self.df, "since")
            
        if self.until:
            for df in self.clean_dict.values():
                df = df[df['created_date'] < utils.str_to_dt_other(self.until)]
        else: 
            self.until = utils.get_date(self.df, "until")

    def _clean_commit(self, line):
        """
        This method is for cleaning a raw commit fetched by Perceval. 
        Since all attributes of the data are not of our importance, it is 
        better to just keep the ones which are required.

        :param line: a raw line fetched by Perceval, present in the JSON file
            It is a dictionary.
        """
        cleaned_line =  \
        {
            'repo': line['origin'],
            'hash': line['data_commit'],
            'author': line['data_Author'],
            'category': "commit",
            'created_date': utils.str_to_dt_data(line['data_AuthorDate']),
            'commit': line['data_Commit'],
            'commit_date': utils.str_to_dt_data(line['data_CommitDate']),
            'files_no': len(line['data_files']),
            'refs': line['data_refs'],
            'parents': line['data_parents'],
            'files': line['data_files']
        }

        actions = 0
        for file in line['data_files']:
            if 'action' in file:
                actions += 1
        cleaned_line['files_action'] = actions

        if 'data_Merge' in line:
            cleaned_line['merge'] = True
        else:
            cleaned_line['merge'] = False

        return cleaned_line
        
    
