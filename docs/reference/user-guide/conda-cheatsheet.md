# Conda Cheatsheet
Command line package and environment manager
Learn to use conda in 30 minutes at bit.ly/tryconda

## Getting Started

### Setting up Conda on your machine
When using `tllihpcmind6`, initialize Conda by `source ~/.bashrc`
```
$ source ~/.bashrc

$ which conda
/gpfs/mskmind_ess/<YOUR_USER_NAME>/miniconda/bin/conda

$ conda update conda

$ conda --version

$ conda --help

$ conda list
```

### Creating a Virtual Environment
A virtual environment can be defined and created through an `environment.yml` file. For example, the Conda environment `conda-env-cdm` can be created with this snippet included in `environment.yml`
```
name: conda-env-cdm
channels:
  - pytorch
  - nvidia
  - conda-forge
dependencies:
   - python == 3.10
   - pandas
   - pyyaml
   - requests
   - setuptools_scm
   - setuptools
   - pip
   - pip: 
       - git+https://github.com/clinical-data-mining/msk_cdm.git
   - minio
```

## Conda Basics
- `conda info`: Verify conda is installed, check version number
- `conda update conda`: Update conda to the current version
- `conda install PACKAGENAME`: Install a package included in Anaconda
- `spyder`: Run a package after install, example Spyder*
- `conda update PACKAGENAME`: Update any installed program
- `COMMANDNAME --help`: Command line help
    - `conda install --help`

## Using Environments
- `conda create --name py35 python=3.5`: Create a new environment named py35, install Python 3.5
- `conda env create -f environment.yaml`: Create a new environment with specifications in `environment.yaml` (See Start-up)
- `conda activate py35`: Activate the new environment to use it
- `conda env list`: Get a list of all my environments, active environment is shown with *
- `conda list`: List all packages and versions installed in active environment
- `conda env remove --name bio-env`: Delete an environment and everything in it
- `conda deactivate`: Deactivate the current environment

## Installing Packages
Anaconda includes both the Python and R programming languages, most of the common Python libraries used in science and engineering (including NumPy, SciPy, Matplotlib, and pandas), and many commonly used R packages (https://anaconda.org/).

- `conda install -c anaconda pandas`: Install Pandas into your activate environment

