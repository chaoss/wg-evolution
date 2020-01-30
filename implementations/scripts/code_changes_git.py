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

from datetime import datetime

from implementations.scripts.commit_git import CommitGit
from implementations.scripts.conditions import (DirExclude,
                                                MasterInclude,
                                                PostfixExclude,
                                                CommitByTag)
from implementations.scripts.utils import read_json_file


class CodeChangesGit(CommitGit):
    """
    Class for Code_Changes for Git repositories. (non-pandas)
    """

    def compute(self):
        """
        Count number of commits of different types, like including
        empty commits or counting only those commits made on
        the master branch.

        :returns count: the number of commits satisfying the conditions passed
            while instantiating CodeChangesGit.
        """

        commit_hashes = {item['hash'] for item in self.items}
        return len(commit_hashes)


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = read_json_file('../git-commits.json')

    changes = CodeChangesGit(items, date_range=(date_since, None))
    print("Code_Changes, total:", changes.compute())

    changes = CodeChangesGit(items, date_range=(date_since, None),
                             is_code=[DirExclude(['tests']),
                                      PostfixExclude(
                                 ['.md', 'COPYING'])])
    print("Code_Changes, excluding some files:", changes.compute())

    changes = CodeChangesGit(items, date_range=(date_since, None),
                             conds=[MasterInclude()])
    print("Code_Changes, only for master:", changes.compute())

    # considering only those commits that contain either the [api] or the
    # [backend] tag in their message.
    tags = ["[api]", "[backend]"]
    for tag in tags:
        print("Code_Changes, only for the commits whose message starts with {}: {}".format(
            tag,
            CodeChangesGit(items, conds=[CommitByTag(tag)]).compute()))

    print("Code_Changes, only for the commits whose message starts with either [api] or [backend]: {}".format(
        CodeChangesGit(items, conds=[CommitByTag(tags)]).compute()))
