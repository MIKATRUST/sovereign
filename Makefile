init:
	pip3 install -r requirements.txt

run:
	python3 -m sovereign

test:
	coverage run --omit="sovereign/tests/*" -m unittest discover
	coverage report
	coverage html

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

.PHONY: init run test clean
