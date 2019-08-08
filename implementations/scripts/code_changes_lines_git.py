from datetime import datetime

from implementations.code_df.commit_git import CommitGit
from implementations.code_df.conditions import (DirExclude,
                                                MasterInclude,
                                                PostfixExclude)
from implementations.code_df.utils import (read_json_file,
                                           str_to_date)


class CodeChangesLinesGit(CommitGit):
    """
    Class for Code_Changes_Lines for Git repositories (non-pandas)
    """

    def _flatten(self, item):
        """
        Flatten a raw commit fetched by Perceval into a flat dictionary.

        A list with a single flat directory will be returned.
        That dictionary will have the elements we need for computing metrics.
        The list may be empty, if for some reason the commit should not
        be considered.

        :param item: raw item fetched by Perceval (dictionary)
        :returns:    list of a single flat dictionary
        """

        creation_date = str_to_date(item['data']['AuthorDate'])
        if self.since and (self.since > creation_date):
            return []

        if self.until and (self.until < creation_date):
            return []

        code_files = [file['file'] for file in item['data']['files'] if
                      all(condition.check(file['file'])
                          for condition in self.is_code)]

        if len(code_files) > 0:
            flat = {
                'repo': item['origin'],
                'hash': item['data']['commit'],
                'author': item['data']['Author'],
                'category': "commit",
                'created_date': creation_date,
                'committer': item['data']['Commit'],
                'commit_date': str_to_date(item['data']['CommitDate']),
                'files_no': len(item['data']['files']),
                'refs': item['data']['refs'],
                'parents': item['data']['parents'],
                'files': item['data']['files']
            }

            # actions
            actions = 0
            for file in item['data']['files']:
                if 'action' in file:
                    actions += 1
            flat['files_action'] = actions

            # Merge commit check
            if 'Merge' in item['data']:
                flat['merge'] = True
            else:
                flat['merge'] = False

            # modifications
            modified_lines = 0
            for file in item['data']['files']:
                if 'added' and 'removed' in file:
                    try:
                        modified_lines += int(file['added']) \
                                        + int(file['removed'])

                    except ValueError:
                        # in case of compressed files,
                        # additions and deletions are "-"
                        pass

            flat['modifications'] = modified_lines

            return [flat]
        else:
            return []

    def compute(self):
        """
        Compute the number of lines modified in the data fetched
        by Perceval.

        It computes the sum of the 'modifications' key
        in the dictionary.

        :returns modifications_count: The total number of
            lines modified (int)
        """

        modifications_count = 0
        for item in self.items:
            modifications_count += item['modifications']

        return modifications_count

    def __str__(self):
        return "Code Changes Lines"


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = read_json_file('../git-commits.json')

    # total number of line changes
    changes = CodeChangesLinesGit(items, date_range=(None, None))
    print("Code_Changes_Lines, total changes:", changes.compute())

    # number of line changes after imposing conditions
    changes = CodeChangesLinesGit(items, date_range=(None, None),
                                  is_code=[DirExclude(['tests']),
                                           PostfixExclude(
                                            ['.md', 'COPYING'])])
    print("Code_Changes_Lines, excluding some files:", changes.compute())

    # total line changes after a certain date
    changes = CodeChangesLinesGit(items, date_range=(date_since, None),
                                  conds=[MasterInclude()])
    print("Code_Changes_Lines, only for master:", changes.compute())
