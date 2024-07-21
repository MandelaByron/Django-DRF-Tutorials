
python manage.py migrate --no-input

python manage.py load_json_data

python manage.py collectstatic --no-input

exec gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 3


