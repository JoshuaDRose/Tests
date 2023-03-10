install:
	@python -m pip install -r requirements.txt

test:
	@python -m coverage run -m unittest discover -s tests
	@python -m coverage report 
	@python -m coverage html
	@rm ./res/coverage.svg
	@coverage-badge -o ./res/coverage.svg

lint:
	@flake8 * --exclude README.md,Makefile
