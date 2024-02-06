# CDM Data Query Quick Start Guide

This repo offers several Jupyter Notebooks that will help query and transform data. Here's how to get started!


## Create virtual environment from requirements.txt file
At the command line, create a virtual envirnoment called `env`
```
python3 -m venv env
```

Then, activate the virtual env:
```
source env/bin/activate
```

If it's been awhile (or the first time), update pip:
```
<path-to-repo>/cdm-utilities/env/bin/python3 -m pip install --upgrade pip
```

Once activated, install the packages listed in the `requirements.txt` file
```
python3 -m pip install -r requirements.txt
```

After packages have been installed, run `jupyter-lab` (make sure a web browser is open) and start prototyping!

## Query Data
With your environment set up, this [Jupyter Notebook](https://github.com/clinical-data-mining/cdm-utilities/blob/main/dremio_api/dremio_connection_test.ipynb) will show you how to query data from our Dremio instance.

To understand how to use our data (better), check out the [data dictionary](https://clinical-data-mining.github.io/cdm-utilities/data-dictionary/).

