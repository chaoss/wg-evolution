import unittest
import sys
sys.path.append('..')
from code_df.metric import Metric
from code_df import utils
from code_df.code_changes_git import CodeChangesGit
from pandas.util.testing import assert_frame_equal


def read_file(file_path):
    items = list()
    with open(path, 'r') as raw_data:
        for line in raw_data:
            line = json.loads(line)

            items.append(line)
    return items

class TestCodeChangesGit(unittest.TestCase):

	def setUp(self):
		self.items = read_file('test_commits_data.json')

	def test_compute_trivial(self):
		changes = CodeChangesGit(self.items)
		expected_count = 21
		count = changes.compute()
		self.assertEqual(expected_count, count)

	def test_compute_with_duplicate(self):
		items_temp = self.items
		items_temp.append(self.items[0])
		changes = CodeChangesGit(items_temp)
		expected_count = 21
		count = changes.compute()
		self.assertEqual(expected_count, count)

	def test__agg(self):
		changes =  CodeChangesGit(self.items)
		changes.df = changes.df.set_index('created_date')
		test_df = changes.df
		test_df = test_df.resample('W')['category'].agg(['count'])
		
		changes.df = changes._agg(changes.df, 'W')
		assert_frame_equal(test_df, changes.df)	



if __name__ == '__main__':
    unittest.main(verbosity=2)
