#!make
include config/.env
GREEN=\033[4;92m
RED=\033[0;31m
NC=\033[0m


djkey:
	python -c "from django.core.management.utils import get_random_secret_key;print(get_random_secret_key())"

install:
	sudo apt install docker docker-compose -y
	sudo systemctl enable docker
	sudo systemctl start docker
	sudo docker pull redis
	sudo docker pull celery

reset-db:
	rm -f ./data/db.sqlite3
	python manage.py migrate
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser($(DJANGO_SUPERUSER_USERNAME), $(DJANGO_SUPERUSER_EMAIL), $(DJANGO_SUPERUSER_PASSWORD))" | python manage.py shell
	echo "\n ${GREEN}Superuser ${DJANGO_SUPERUSER_USERNAME} created${NC}\n"
	python manage.py loaddata 001_news 002_courses 003_lessons 004_teachers

up:
	mkdir -p ./data/cache
	sudo docker-compose -f stack.yml up -d

down:
	sudo docker-compose -f stack.yml down
