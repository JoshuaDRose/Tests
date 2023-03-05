install:
	@python -m pip install -r requirements.txt
test:
	@python -m coverage run -m unittest discover -s tests
	@python -m coverage report 

export:
	@python -m coverage html

lint:
	flake8 *.py

codecov_badge:
	coverage-badge > res/coverage.html
