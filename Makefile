bash:
	docker exec -it helios-django bash

build:
	docker build -t mantiby/helios:latest .

migrate:
	docker exec -it helios-django python manage.py migrate

static:
	docker exec -it helios-django python manage.py collectstatic --no-input

messages:
	python manage.py makemessages -a

check:
	flake8 helios/
	black --target-version py38 helios/
	standard --fix helios/static/js/

test:
	pytest helios/
