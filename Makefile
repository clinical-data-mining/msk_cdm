.PHONY: install
install:
	pip install .

.PHONY: test
test:
	pip install .[test]
	pytest .

.PHONY: install_precommit_hooks
install_precommit_hooks:
	pip install pre-commit
	pre-commit install
