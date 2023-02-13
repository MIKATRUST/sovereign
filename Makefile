
PY = python3
VENV = venv
BIN = $(VENV)/bin
DIR = sovereign

# make it work on windows too
ifeq ($(OS), Windows_NT)
	BIN=$(VENV)/Scripts
	PY=python
endif

all: lint test

$(VENV): requirements.txt requirements-dev.txt #setup.py
	$(PY) -m venv $(VENV)
	$(BIN)/pip install --upgrade -r requirements.txt
	$(BIN)/pip install --upgrade -r requirements-dev.txt
#	$(BIN)/pip install -e .
	touch $(VENV)

.PHONY: format
format: $(VENV)
	$(BIN)/autopep8 $(DIR) --recursive --in-place --pep8-passes 2000 --verbose

.PHONY: lint
lint: $(VENV)
	$(BIN)/pylint $(DIR)

.PHONY: test
test: $(VENV)
#	$(BIN)/pytest
	$(BIN)/coverage run -m unittest discover
	$(BIN)/coverage report
	$(BIN)/coverage html -d ./sovereign/docs/

.PHONY: coverage
coverage: $(VENV)
	$(BIN)/coverage report

.PHONY: run
run: $(VENV)
	$(PY) -O -m $(DIR)

.PHONY: run-debug
run-debug: $(VENV)
	$(PY) -m $(DIR)

#.PHONY: release
#release: $(VENV)
#	$(BIN)/python setup.py sdist bdist_wheel upload

clean:
	rm -rf $(VENV)
	rm -rf ./docs/*
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete

