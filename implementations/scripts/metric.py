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


class Metric():
    """
    Create a list of dictionaries from items fetched by Perceval

    All classes computing metrics based on data frames
    will be descendants of this class.

    :param items: A list of dictionaries.
        Each element is a Perceval dictionary, obtained from a JSON
        file produced by Perceval, or directly from Perceval.
    """

    def __init__(self, items):

        flat_items = []
        for item in items:
            flat_items.extend(self._flatten(item))
        self.items = flat_items

    def _flatten(self, item):
        """
        Flatten an item into a list of flat dictionaries

        The produced dictionaries are intended to be used
        when building a data frame.
        This method will be overridden by descendant classes.

        :param item: item to flatten
        :return:     list of flat dictionaries

        """

        raise NotImplementedError
