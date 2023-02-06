#all:
#	TBD

init:
	pip3 install -r requirements.txt

run:
	python3 -O -m sovereign

run_debug:
	python3 -m sovereign

lint:
	python3 -m autopep8 --in-place --aggressive --aggressive sovereign/model/model.py
	python3 -m pylint sovereign

test:
	coverage run --omit="sovereign/tests/*" -m unittest discover
	coverage report
	coverage html

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

.PHONY: init run run_debug lint test clean
