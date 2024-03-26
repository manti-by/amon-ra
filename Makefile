.PHONY:build

bash:
	docker exec -it amon-ra-django bash

build:
	docker build -t mantiby/amon-ra:latest .

migrate:
	docker exec -it amon-ra-django python manage.py migrate

static:
	docker exec -it amon-ra-django python manage.py collectstatic --no-input

deploy:
	docker container stop amon-ra-django amon-ra-bot
	docker container rm amon-ra-django amon-ra-bot
	docker compose up -d

dump:
	docker exec -it amon-ra-postgres pg_dump -U amon-ra -d amon-ra > database.sql

restore:
	docker cp database.sql amon-ra-postgres:/tmp/database.sql
	docker exec -it amon-ra-postgres psql -U amon_ra amon_ra -f /tmp/database.sql

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

update:
	pcu requirements.txt -u
	pre-commit autoupdate
