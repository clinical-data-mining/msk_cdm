.PHONY: install
install:
	pip install .

.PHONY: test
test:
	pip install .[test]
	pytest .

.PHONY: clean
clean:
	find src/ -name "__pycache__" | xargs rm -r
	rm -r ./build/

DOCS_EXCLUDE = */test_*.py
.PHONY: docs
docs:
	pip install .[docs]
	sphinx-apidoc -f -e -d 6 -o docs/source src/msk_cdm $(DOCS_EXCLUDE)
	sphinx-build -b html docs/source docs/build

.PHONY: install_precommit_hooks
install_precommit_hooks:
	pip install pre-commit
	pre-commit install
