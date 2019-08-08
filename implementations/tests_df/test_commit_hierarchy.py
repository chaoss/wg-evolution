import unittest
import json
from pandas.util.testing import assert_frame_equal

import sys
sys.path.append('..')

from code_df import (
                        code_changes_git,
                        code_changes_lines,
                        new_contributors_of_commits
                    )


class TestCommitHierarchy(unittest.TestCase):

    def test_code_changes_git(self):
        pass

    def test_code_changes_lines(self):
        pass

    def test_new_contributors_of_commits(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
