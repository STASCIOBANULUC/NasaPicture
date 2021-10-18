# NasaPicture
1 python manage.py makemigrations
2 python manage.py migrate
3 python manage.py parsenasa - для загрузки данных вручную
4 docker-compose up
5 celery -A NasaPicture -l beat
6 celery -A NasaPicture -l worker INFO --pool=solo
