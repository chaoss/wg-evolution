# Reference implementations

This directory provides reference implementations for the metrics defined by the
working group. All these reference implementations use data produced by
[Perceval](https://github.com/chaoss/grimoirelab-perceval) to show how the
metric could be implemented in detail.
All of these reference implementations are not intended to be specially good
in performance, or ready for production, but good and easy to follow examples
of how the intended metrics can be computed.

## List of reference implementations



| metric | plain python script | pandas script | plain python notebook | pandas notebook | description |
| --- | --- | --- | --- | --- | --- |
| **Code Changes** | [module](./scripts/code_changes_git.py) | [with-pandas](./code_df/code_changes_git.py) | [notebook](./notebooks/code_changes_git.ipynb) | [with-pandas notebook](./notebooks_df/code_changes_git.ipynb)| [description](https://github.com/chaoss/wg-evolution/blob/master/metrics/Code_Changes.md) |
| **Code Changes Lines** | [module](./scripts/code_changes_lines_git.py) | [with-pandas](./code_df/code_changes_lines_git.py) | [notebook](./notebooks/code_changes_lines_git.ipynb) | [with-pandas notebook](./notebooks_df/code_changes_lines_git.ipynb)| [description](https://github.com/chaoss/wg-evolution/blob/master/metrics/Code_Changes_Lines.md) |
| **Reviews** | [module](./scripts/reviews_github.py) | [with-pandas](./code_df/reviews_github.py) | [notebook](./notebooks/reviews_github.ipynb) | [with-pandas notebook](./notebooks_df/reviews_github.ipynb)| [description](https://github.com/chaoss/wg-evolution/blob/master/metrics/Reviews.md) |
| **Reviews Accepted** | [module](./scripts/reviews_accepted_github.py) | [with-pandas](./code_df/reviews_accepted_github.py) | [notebook](./notebooks/reviews_accepted_github.ipynb) | [with-pandas notebook](./notebooks_df/reviews_accepted_github.ipynb)| [description](https://github.com/chaoss/wg-evolution/blob/master/metrics/Reviews_Accepted.md) |
| **Reviews Declined** | [module](./scripts/reviews_declined_github.py) | [with-pandas](./code_df/reviews_declined_github.py) | [notebook](./notebooks/reviews_declined_github.ipynb) | [with-pandas notebook](./notebooks_df/reviews_declined_github.ipynb)| [description](https://github.com/chaoss/wg-evolution/blob/master/metrics/Reviews_Declined.md) |
| **Reviews Duration** | [module](./scripts/reviews_duration_github.py) | [with-pandas](./code_df/reviews_duration_github.py) | [notebook](./notebooks/reviews_duration_github.ipynb) | [with-pandas notebook](./notebooks_df/reviews_duration_github.ipynb)| [description](https://github.com/chaoss/wg-evolution/blob/master/metrics/Reviews_Duration.md) |




## Contents of this directory

We use Python Jupyter notebooks as the framework for producing the implementations that will be explanatory in regard to the analysis performed. These notebooks come in two flavors:

* [notebooks](./notebooks/) are reference implementations using
plain Python for computing the metrics.
In these cases, the data produced by Perceval is processed as
a Python list, using plain Python mechanisms as much as possible.

* [notebooks_df](./notebooks_df/) are reference implementations
using Pandas data frames as the basis for computing the metrics.
In these cases, the data produced by Perceval is converted to a Pandas
dataframe, and then processed to produce the metrics.

Notebooks are also exported as Python modules. These are more useful
if you intend to look only at the code:

* [scripts](./scripts/) are notebooks in the [notebooks](./notebooks/)
directory exported as Python modules

* [code_df](./code_df/) are notebooks in the [notebooks_df](./notebooks_df/)
directory exported as Python modules

For the implementations, you can find the following modules:

- **Root module ([module](./scripts/metric.py) [with-pandas](./code_df/metric.py))**:     
This file contains the root class, `Metric`. All other classes inherit from it. It takes JSON data collected by Perceval and converts it into a form easier to analyze: like a dataframe, or a list of dictionaries.  

- **Category modules**:  
These classes provide basic functionality which is common to all metric classes working on the same category of data: commits, issues or pull request.
The three category modules are:
    + **commit_git.py ([module](./scripts/commit_git.py) [with-pandas](./code_df/metric.py))**
    + **issue_github.py ([module](./scripts/issue_github.py) [with-pandas](./code_df/metric.py))**
    + **pullrequest_github.py ([module](./scripts/pullrequest_github.py) [with-pandas](./code_df/metric.py))**

- **Individual Metric modules**:  
These are python scripts exported from the reference implementation notebooks. They inherit from the Category modules, but have the functionality to calculate the value of the metric they correspond to. For the pandas version of the implementations, the time-series can be generated for a particular metric. 

- **source code check ([module](scripts/conditions.py) [with-pandas](code_df/conditions.py))**:  
An important aspect of several metrics is how source code is defined. This module provides several algorithms, which help define source code. Currently, the following are provided:

    + Naive
    + DirExclude
    + PostfixExclude  
    
In the case of metrics using Git, restrictions on the kinds of commits being considered can be imposed. For example, one can consider only those commits made on the master branch, or exclude empty or merge commits. Currently, the following restrictions are provided:
    + MasterInclude
    + EmptyExclude
    + MergeExclude

- **utilities ([module](./scripts/utils.py) [with-pandas](./code_df/utils.py))**:  
    The following functionality is provided:
    - covert dates in string format to datetime objects
    - read json files into a python list

To summarize, the class hierarchy for both kinds of implementations is:
```
Root class (metric.py) <- Category classes (commit_git.py, for example) <- Metric classes (code_changes_git.py, for example)
```

## How to run the notebooks

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/chaoss/wg-gmd/master?filepath=implementations)

You can run the notebooks directly in [Binder](https://mybinder.org):
Just click on the "launch binder" logo above.

You can also run the notebooks locally on your computer.
For that, you need a Python3 environment with certain modules installed
(it is recommended to use a virtual environment,
  see [Creation of virtual environments](https://docs.python.org/3/library/venv.html)).
To install the modules, just use pip3:

```bash
$ pip install jupyter
$ pip install pandas
$ pip install perceval
```

(check at the beginning of each notebook just in case more modules need to be installed).

Clone this repository and change directory to where this notebook resides:

```
$ git clone https://github.com/chaoss/wg-gmd
$ cd wg-gmd/implementations/notebooks_df
```

Then launch Jupyter from the command line...

```
$ jupyter notebook
```

This will launch the Jupyter kernel, and will open your default browser
with the directory with all the notebooks loaded.
Click on the notebook you want to run, and you're ready to go.
More detailed instructions can be found in
[Introducing the Notebook Server’s Command Line Options](https://jupyter-notebook.readthedocs.io/en/stable/config.html).

Once you have the notebook in your browser, you can execute the selected cell
by clicking \[CTRL\]\[Enter\], or \[Shift\]\[Enter\]. In the latter case,
the current cell will be run, and the next one will be selected.
For selecting any cell, just click on it.

So, if you want to execute the whole dashboard, just select the first cell,
and click \[Shift\]\[Enter\] until you're done.
You can also click on the Cell menu, and select "Run All",
which will also run all the cells in the notebook.
More details can be found in [Executing a notebook](https://jupyter-notebook-beginner-guide.readthedocs.io/en/stable/execute.html#executing-a-notebook).

If you want to modify any cell, just click on it, look for the cursor,
and start writing.

If you want more details and context about Jupyter notebooks, have a look at
[Jupyter Notebook Tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook).


## Adding reference implementations

### Files per metric
Every metric that is defined by the Evolution working group is implemented in two forms: a plain Python implementation, and another one which makes use of Pandas data structures, particularly data frames.

Each metric also has a jupyter notebook dedicated to it, and the python scripts associated with a metric are derived from this notebook. The notebook discusses key functionality and also discusses how the metric is computed.

### Naming convention
A metric class follows the following naming convention:
```
<name of the metric>_<data source>.py
```
For example, `code_changes_git.py` or `reviews_accepted_github.py`.
All issue and pull request related metrics use the `github api` as a data source.  
Notebooks follow the same convention.

### Structure of a metric class
The pandas version of a metric has the `compute` and the `_agg` methods, while the non-pandas or plain Python version has only the `compute` method. The `compute` method calculates the value of the metric for the given time period while the `_agg` returns a data frame to the `time_series` method defined in
`metric.py`


## Notes

* Every metric is computed for all the items in the data structure used to instantiate the
corresponding class.
If a data structure contains items of a single repository,
only that repository will be considered for calculating the metric.
Likewise, using the data of an entire project,
(consisting of several repositories)
will result in the metric being computed for the entire project and not for each individual repository. 

* Another assumption is that the JSON data file has items of the same kind, for example: commits, issues or pull requests.
    
