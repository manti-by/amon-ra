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

test:
	pytest helios/

check:
	git add .
	pre-commit run

pip:
	pip install -r requirements.txt

update-requirements:
	pcu requirements.txt -u
