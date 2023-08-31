# Core MSK Clinical Data Mining group code.

## Using/installing this repo.

The simplest way to use this repo is to set up a conda env or environment of your choice
and then, after `git clone`-ing this directory, simply issue
```
make install
```
or
```
pip install .
```

## Contributing to this repo

If you're contributing to the code please run `make install_precommit_hooks` from the
root of the repository to install the pre-commit hooks. They will probably require you
to `git add` a second time after trying the first round of `git commit` (one of the
hooks is the Black linter, which modifies the source file, so you need to try to
`git commit` twice if it does).

You can run unit tests by issuing `make test` from the root dir.
