.PHONY: help clean package test

help:
	@echo "This project uses Poetry for dependency management."
	@echo "The following make targets are available:"
	@echo "	 dev 	install all deps for dev env"
	@echo "	 test	run all tests with coverage"

clean:
	rm -rf dist/*

dev:
	pip install --upgrade pip poetry
	poetry install

package:
	poetry build

test:
	poetry run tox