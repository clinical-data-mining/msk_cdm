# Python
These instructures are for terminal access only. For Python environments in JupyterHub, please see JupyterHub.

## Virtualenv

You may create a virtualenv by pointing to a particular version of python. Different versions of **Python** interpreters are available,
### Python Versions
```
On the phi server:

/mind_data/sw
├── python3.7
├── python3.8
└── python3.9

On the de-identified servers:

/gpfs/mskmind_ess/sw/
├── python3.7
├── python3.8
└── python3.9
```
So, for example you may create a virtual environment with python3.7 as shown below.

**Note**: LD_LIBRARY_PATH needs to be set to include the lib of the version you choose. 

### virtualenv
```
$ export LD_LIBRARY_PATH=/usr/lib64:/gpfs/mskmind_ess/sw/python3.7/lib
$ /gpfs/mskmind_ess/sw/python3.7/bin/python3.7 -m venv venv
$ source venv/bin/activate
(venv) $ which python
~/venv/bin/python
(venv) $ python --version
Python 3.7.11   
(venv) $ deactivate
```
Install packages with pip :
```
(venv) $ pip install numpy
```
**N.B.**, do not use the --user  option to pip (otherwise it will install to your home directory).

## Miniconda

Miniconda gives you the Python interpreter itself, along with a command-line tool called conda which operates as a cross-platform package manager geared toward Python packages. You may use Miniconda on the compute servers to manage your own python environments and packages for your projects. This means you do not have to depend on any centralized or system-wide python environment for your projects. 

### Setup

Install Miniconda using the instructions below in your ESS sub-directory your mind_data sub-directory

#### Miniconda Installation
```
# or `cd` into any directory of your choice (e.g. /mind_data/<YOUR_USER_NAME>)
$ cd /gpfs/mskmind_ess/<YOUR_USER_NAME>/

# Download the python 3.9 (or latest) installer (See Ref 1)
# NOTE: You can choose different versions of python for different projects later
# using the conda package manager. This is described in the Test section below.
# If having issues w/ insecure warnings, add --no-check-certificate flag
$ wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh

# Verify Hash
$ sha256sum Miniconda3-py39_4.10.3-Linux-x86_64.sh
1ea2f885b4dbc3098662845560bc64271eb17085387a70c2ba3f29fff6f8d52f

$ chmod +x Miniconda3-py39_4.10.3-Linux-x86_64.sh

$ ./Miniconda3-py39_4.10.3-Linux-x86_64.sh
```
When prompted for location of installation, point the installer to `/gpfs/mskmind_ess/<YOUR_USER_NAME>/miniconda`. Make sure the directory does not already exist.

Allow the installer to run conda init and select defaults for the rest of the installation. 

Log out of your shell and log back in. 

### Test

Test your miniconda installation by following the steps below. If these commands execute, your conda environment is set up correctly. 
```
$ source ~/.bashrc

$ which conda
/gpfs/mskmind_ess/<YOUR_USER_NAME>/miniconda/bin/conda

$ conda update conda

$ conda --version

$ conda --help

$ conda list
```
You may now create separate python environments and install separate versions of python packages in these environments following the instructions below. 

Create an environment file with the following contents. Note that you can specify the version of python you want to use that is independent of the version of python chosen when installing miniconda. 
#### conda environment file
```
name: project_1
dependencies:
- python=3.9 # or 3.7, 3.10, etc.
- pip
- pip:
    - numpy==1.23.5
```

Now create and activate your environment. 
```
$ conda env create -f project_1.yml

$ conda activate project_1
```
Install additional packages with pip or conda:
```
$ pip install pandas

$ conda install poetry
```
**N.B.**, do not `pip install`  packages with the `--user`  option.

To deactivate, remove an environment and clean conda cache, 
#### cleanup environment
```
$ conda deactivate

$ conda remove --name project_1 --all

$ conda clean --all
```
### Teardown

To remove miniconda altogether, follow these instructions below. NOTE: With many environment installs and uninstalls, the miniconda dir tends to grow in size, so it would be good to re-install it from time to time. 
#### uninstall miniconda
```
$ rm -rf /gpfs/mskmind_ess/<YOUR_USER_NAME>/miniconda

$ rm -rf ~/.conda
```
Edit your ~/.bashrc (or .bash_profile) file and remove all lines between, and including these lines. 
```
# >>> conda initialize >>>
...
# <<< conda initialize <<<
```



## References
1. [Miniconda installers](https://docs.conda.io/en/latest/miniconda.html#linux-installers)
2. [Conda Tasks](https://conda.io/projects/conda/en/latest/user-guide/tasks/index.html)

---
[Documentation adapted from MSK-MIND](https://mskconfluence.mskcc.org/display/MM/Python)