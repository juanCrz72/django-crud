set -o errexit




python manage.py collectstatic --no-input
python manage.py migrate

pip install -r requirements.txt