import pandas as pd
import datetime
import json


def str_to_dt_other(date):
    """
    :param date: date (a string with format "%Y-%m-%d")
    Converts date to a datetime object if date has the above format
    """
    datetimeobj =  datetime.datetime.strptime(date, "%Y-%m-%d")
    return datetimeobj

def str_to_dt_data(date):
    """
    :param date: converts date (str) to a datetime object 
    Note: the string format for the date in the json file is either: 
     - %a %b %d %H:%M:%S %Y %z --> for commits
     - %Y-%m-%dT%H:%M:%SZ      --> for issues and pull requests
    """        
    try:
        datetimestr =  datetime.datetime.strptime(date, "%a %b %d %H:%M:%S %Y %z").strftime("%Y-%m-%d")
    
    except ValueError as ve:
        datetimestr =  datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
    
    finally:
        datetimeobj = datetime.datetime.strptime(datetimestr, "%Y-%m-%d")
        return datetimeobj

def get_date(df, option="since"):
    """
    For certain metrics, computing a value for a repeated interval of time
    if important. For this, an initial and final date is necessary. This 
    can become a problem since `since` and `until` date parameters to __init__
    are optional. 
    Thus, if unspecified, since and until are set to the earliest and latest
    date of all data points respectively
    """
    if option == "since":
        return min(df['created_date'])

    if option == "until":
        return max(df['created_date'])

def read_JSON_file(path):
    """
    Given a line-by-line JSON file, this function converts it a Python dict 
    and returns all such lines as a list.

    :param path: the path to the JSON file
    """
    data_list = list()
    with open(path, 'r') as raw_data:
        for line in raw_data:
            line = json.loads(line)

            data_list.append(line)
    return data_list
