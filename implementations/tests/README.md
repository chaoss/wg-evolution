# Tests

## Structure of the tests directory
- The tests directory has the structure:
```bash
tests
├── data
├── README.md
├── run_tests.py
├── tests
└── tests_df
```
- There are two kinds of tests, `tests`, for the plain Python series of implementations, and `tests_df`, for the version of implementations using pandas.
- The `run_tests` module runs a test suite over both kinds of tests.


## Running tests
Tests can be run from the `tests/` directory.
```bash
$ cd tests
$ python3 run_tests.py
.............................................................................................
----------------------------------------------------------------------
Ran 93 tests in 0.884s

OK

```

## Adding Tests
For each metric that is implemented, two test files are created -- one tests the plain-python implementation while the other is for the module using pandas.

A test should test all the primary methods defined in that module. Ideally, each method should be tested with a variety of potential input cases that could arise.

For example, the test suite for the pandas implementation of the Code Changes metric, which can be found [here](./tests_df/test_code_changes_git.py), tests the `compute`, `_agg` and `_get_params` methods.
```python
class TestCodeChangesGit(unittest.TestCase):

    def test_compute(self):
        pass

    def test_compute_with_duplicate(self):
        pass

    def test__agg(self):
        pass

    def test__get_params(self):
        pass
```

Notice that the `compute` method is tested in two different cases: with and without duplicates. This is done to ensure that the implementation doesn't break when there are repetitions in the data.