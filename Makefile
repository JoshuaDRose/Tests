install:
	@python -m pip install -r requirements.txt

test:
	@python -m coverage run -m unittest unittest discover -s tests
	@python -m coverage report 
	@python -m coverage html
	@coverage-badge > res/coverage.svg

lint:
	flake8 *.py
