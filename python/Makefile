.PHONY: app docs

help:
	@echo "Commands:"
	@echo "install         : installs requirements."
	@echo "install-dev     : installs development requirements."
	@echo "test            : run unit tests."
	@echo "style           : run style formatting."
	@echo "clean           : cleans all unnecessary files."
	@echo "checks          : runs all checks (test, style and clean)."
	@echo "docs            : serve generated documentation."

install:
	python -m pip install -e .

install-dev:
	python -m pip install -e ".[dev]"

test:
	pytest --cov PKGNAME --cov-report html --disable-pytest-warnings

style:
	black .
	isort .
	flake8

clean:
	find . -type f -name "*.DS_Store" -ls -delete
	find . -type f -name "*.swp" -ls -delete
	find . -not -path "./venv" | grep -E "(\.egg.info|__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	rm -f .coverage

docs:
	python -m mkdocs serve
