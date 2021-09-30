web: gunicorn nameless-retreat-88049.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate