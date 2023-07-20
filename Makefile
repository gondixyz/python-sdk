test-all coverage:
	poetry run coverage run -m unittest discover -v -f -b -p '*.py' -s ./test
	poetry run coverage report -m --fail-under=80

test-local-quick:
	poetry run python -m pytest test/*/*.py --testmon
