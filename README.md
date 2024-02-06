# Core MSK Clinical Data Mining group code.

New home for cdm-utilities with more flexible package layout/structure


## Requirements

For now the library requires python version at least `3.9`. If your install gives an
error about not being able to find compatible version of a library, check
```
python --version
```
If you're using an older python version, you'll need to upgrade.

## Using/installing this repo.
### Direct installation into your virtual environment
The simplest way to use this repo is to set up a conda env or environment of your choice
and then, after `git clone`-ing this directory, simply issue
```
make install
```
or
```
pip install .
```

### Building a Conda environment from a environment.yml file
A virtual environment can be defined and created through an environment.yml file. For example, the Conda environment conda-env-cdm can be created with this snippet included in environment.yml

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
   - minio
   - requests
   - ipykernel
   - conda-build
   - pip
   - pip: 
       - git+https://github.com/clinical-data-mining/msk_cdm.git
```




## Contributing to this repo

If you're contributing to the code please run `make install_precommit_hooks` from the
root of the repository to install the pre-commit hooks. They will probably require you
to `git add` a second time after trying the first round of `git commit` (one of the
hooks is the Black linter, which modifies the source file, so you need to try to
`git commit` twice if it does).

You can run unit tests by issuing `make test` from the root dir.

If you're updating this repo, please make a Pull Request via a git branch. If the change
is to the core functionality (i.e. modifies the core code in this repo possibly used
by other projects/peple) please request a code review.


## How to run the documentation page
This repo uses mkdocs. One can install all dependencies using pip:

```
pip install -r requirements.txt
```

Then to run locally:
```
mkdocs serve --dev-addr <Default 127.0.0.1:8000>
```

## How to deploy the documentation
Run:

```
mkdocs gh-deploy
```