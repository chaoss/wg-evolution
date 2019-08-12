from datetime import datetime

from implementations.scripts.commit_git import CommitGit
from implementations.scripts.conditions import (DirExclude,
                                                MasterInclude,
                                                PostfixExclude)
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
