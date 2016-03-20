.PHONY: help db clean install info server uwsgi

help:
	@echo "This project assumes that an active Python virtualenv is present."
	@echo "The following make targets are available:"
	@echo "  install     install dependencies"
	@echo "  clean       remove unwanted files"
	@echo "  lint        flake8 lint check"
	@echo "  test        run unit tests"


db:
	sqlite3 ./indienews.db < ./sql/schema.sql

install-hook:
	git-pre-commit-hook install --force --plugins json --plugins yaml --plugins flake8 \
                              --flake8_ignore E111,E124,E126,E201,E202,E221,E241,E302,E501,N802,N803

install-uwsgi:
	pip install uwsgi

install:
	pip install -Ur requirements.txt

install-dev: install
	pip install -Ur requirements-test.txt

clean:
	@rm -f violations.flake8.txt
	python manage.py clean

lint: clean
	flake8 --exclude=env --exclude=archive . > violations.flake8.txt

test: lint
	python manage.py test

coverage: lint
	@coverage run --source=iwn manage.py test
	@coverage html
	@coverage report

info:
	@uname -a
	@pyenv --version
	@pip --version
	@python --version
	@pyenv version

ci: info coverage
	CODECOV_TOKEN=`cat .codecov-token` codecov

server:
	python manage.py server

uwsgi:
	uwsgi --socket 127.0.0.1:5080 --module uwsgi-app --callable application
