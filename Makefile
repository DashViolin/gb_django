#!make
include config/.env

reset:
	rm -f ./db.sqlite3
	python manage.py migrate
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser($(DJANGO_SUPERUSER_USERNAME), $(DJANGO_SUPERUSER_EMAIL), $(DJANGO_SUPERUSER_PASSWORD))" | python manage.py shell
	echo "  Superuser created."
	python manage.py loaddata 001_news 002_courses 003_lessons 004_teachers
