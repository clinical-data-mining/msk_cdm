.PHONY: install
install:
	pip install .

.PHONY: test
test:
	pip install .[test]
	pytest .

.PHONY: docs
docs:
	pip install .[docs]
	sphinx-apidoc -f -o docs/source src/msk_cdm
	sphinx-build -b html docs/source docs/build

.PHONY: install_precommit_hooks
install_precommit_hooks:
	pip install pre-commit
	pre-commit install
