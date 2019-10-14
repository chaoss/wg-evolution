# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CHAOSS
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     Aniruddha Karajgi <akarajgi0@gmail.com>
#

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

    except ValueError:
        datetimestr = datetime.datetime.strptime(
                date, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")

    finally:
        datetimeobj = datetime.datetime.strptime(datetimestr, "%Y-%m-%d")
        return datetimeobj


def read_json_file(path):
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
