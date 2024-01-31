bash:
	docker exec -it amon-ra-django bash

build:
	docker build -t mantiby/amon-ra:latest .

migrate:
	docker exec -it amon-ra-django python manage.py migrate

static:
	docker exec -it amon-ra-django python manage.py collectstatic --no-input

messages:
	python manage.py makemessages -a

test:
	pytest amon_ra/

check:
	git add .
	pre-commit run

django-check:
	./manage.py makemigrations --dry-run --check --verbosity=3 --settings=amon_ra.settings.sqlite
	./manage.py check --fail-level WARNING --settings=amon_ra.settings.sqlite

pip:
	pip install -r requirements.txt

update-requirements:
	pcu requirements.txt -u
