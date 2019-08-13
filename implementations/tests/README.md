# Tests

## Structure
- The tests directory has the structure:
```
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
```

## Adding Tests
For each metric that is implemented, two test files are generated, one for
each kind of implementation.  

