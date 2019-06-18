# Examples of implementations for metrics

Notebooks, built on top of data collected by Perceval,
for illustrating how to compute different metrics of the Evolution Working Group. The notebooks will be explanatory in regard to the analysis performed. They should help the user understand how to calculate these metrics, as well as to understand how the metric is defined.

The contents of this directory are the notebooks(present in [notebooks_df](./notebooks_df/), as well as some scripts in the [code_df](./code_df/) package. The "_df" suffix is to show that these scripts and notebooks make use of the Pandas library. `code_df` contains the following modules:

- **Root module ([module](./code_df/metric.py))**:     
This file contains the root class, `Metric`. All other classes inherit from it. It takes JSON data collected by Perceval and converts it into a form easier to analyze: like a dataframe, or a list of dictionaries.  

- **Category modules**:  
These classes provide basic functionality which is common to all metric classes working on the same category of data: commits, issues or pull request.
The three category modules are:
    + **commit.py ([module](./code_df/commit.py))**
    + **issue.py ([module](./code_df/issue.py))**
    + **pullrequest.py ([module](./code_df/pullrequest.py))**

- **Individual Metric modules**:  
These are python scripts converted from the reference implementation notebooks. They inherit from the Category modules, but have the most important function of all --- to calculate values for the metrics they represent.   

- **source code check ([module](code_df/conditions.py))**:  
An important aspect of several metrics is how source code is defined. The `is_source_code` module provides several algorithms. Currently, the following are provided:

    + Naive
    + FolderExclude
    + ExtensionExclude  

- **utilities ([module](./code_df/utils.py))**:  
    `utils.py` contains functions which help in reading JSON files, converting dates in string format to datetime objects, etc.

To summarize, the class heirarchy is:
```
Root class (metric.py) <- Category classes (commit.py, for example) <- Metric classes
```

### Note
- Every metric is calculated for the data structures of items as a whole. If a data structure contains items of only one repository, only that will be considered for calculating the metric. Likewise, using the data of an entire project, (consisting of several repositories) will result in the metric being computed for the entire project and not for each individual repository. 
- Another assumption is that the JSON data file has items of the same kind, for example, commits, issues or pull requests.
    
## A list of implementations
* **Code Changes ([module](./code_df/code_changes_git.py) • [notebook](./notebooks_df/code_changes_git.ipynb) • [description](https://github.com/chaoss/wg-evolution/blob/master/metrics/Code_Changes.md))**  
    This metric is computed for the data in the file `git-commits.json`.

# How to run the notebooks

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
