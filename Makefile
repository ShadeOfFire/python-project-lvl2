# Makefile

install:
	poetry install

gendiff:  
	poetry run gendiff

test:
	poetry run pytest --cov=gendiff --cov-report xml tests/

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test-coverage:
	pytest --cov=tests/ --cov-report xml
