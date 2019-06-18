import datetime
import json


def str_to_date(date):
    """
    Converts date, of type string, to a datetime object
    :param date: a date, of type string
        Note: the string format for the date in the json file is either:
         - %a %b %d %H:%M:%S %Y %z --> for commits
         - %Y-%m-%dT%H:%M:%SZ      --> for issues and pull requests

    :returns datetimeobj: the datetime object obtained from date string
    """
    try:
        datetimestr = datetime.datetime.strptime(
            date, "%a %b %d %H:%M:%S %Y %z").strftime("%Y-%m-%d")

    except ValueError as ve:
        datetimestr = datetime.datetime.strptime(
                date, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")

    finally:
        datetimeobj = datetime.datetime.strptime(datetimestr, "%Y-%m-%d")
        return datetimeobj


def get_date(df, option='since'):
    """
    For certain metrics, computing a value for a repeated interval of time
    if important. For this, an initial and final date is necessary. This
    can become a problem since `since` and `until` date parameters to __init__
    are optional.
    Thus, if unspecified, since and until are set to the earliest and latest
    date of all data points respectively.

    :param df:
    :param option:

    :returns:

    :raises ValueError:
    """

    if option == 'since':
        return df['created_date'].min()
    elif option == 'until':
        return df['created_date'].max()
    else:
        raise ValueError("option parameter can take only 'since' or 'until'")


def read_JSON_file(path):
    """
    Given a line-by-line JSON file, this function converts it to
    a Python dict and returns all such lines as a list.

    :param path: the path to the JSON file

    :returns items: a list of dictionaries read from a JSON file
    """
    items = list()
    with open(path, 'r') as raw_data:
        for line in raw_data:
            line = json.loads(line)

            items.append(line)
    return items
