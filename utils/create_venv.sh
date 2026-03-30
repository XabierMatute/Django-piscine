python3 -m virtualenv django_venv
# enter
source django_venv/bin/activate

pip install django
pip install psycopg2-binary
psycopg2-binarypip freeze > requirements.txt