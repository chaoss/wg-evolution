import datetime
import json


def str_to_date(date):
    """
    Converts a given date (string) to a datetime object
    :param date: a date, of type string
        Note: the string format for the date in the json file is either:
         - %a %b %d %H:%M:%S %Y %z --> for commits
         - %Y-%m-%dT%H:%M:%SZ      --> for issues and pull requests

    :returns datetime_obj: the datetime object obtained from date string
    """
    try:
        datetime_str = datetime.datetime.strptime(
            date, "%a %b %d %H:%M:%S %Y %z").strftime("%Y-%m-%d")

    except ValueError:
        datetime_str = datetime.datetime.strptime(
            date, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")

    finally:
        datetime_obj = datetime.datetime.strptime(datetime_str, "%Y-%m-%d")
        return datetime_obj


def get_date(df, option='since'):
    """
    For certain metrics, computing a value for a repeated interval of time
    is important. For this, an initial and final date is necessary. This
    can become a problem since `since` and `until` date parameters to
    initialize the class are optional.
    Thus, if unspecified, since and until are set to the earliest and latest
    date of all data points respectively.

    :param df:
    :param option:

    :returns:

    :raises ValueError:
    """
    if option == 'since':
        return min(df['created_date'])

    elif option == 'until':
        return max(df['created_date'])
    else:
        raise ValueError("option parameter can take only 'since' or 'until'")


def read_json_file(path):
    """
    Given a JSON file, this function converts it to
    a list of python dictionaries.

    :param path: the path to the JSON file

    :returns items: a list of dictionaries
    """
    items = list()
    with open(path, 'r') as raw_data:
        for line in raw_data:
            line = json.loads(line)
            items.append(line)

    return items
