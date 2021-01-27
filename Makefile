start:
	docker-compose -f docker-compose.yml up -d

stop:
	docker-compose -f docker-compose.yml stop

destroy:
	docker-compose -f docker-compose.yml down

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
	black --target-version py38 helios/
	isort helios/*.py
	flake8
	standard --fix helios/static/js/

test:
	pytest helios/
