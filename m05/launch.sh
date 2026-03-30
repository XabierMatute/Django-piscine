make -C Database
source ./django_venv/bin/activate
python d05/manage.py migrate
python d05/manage.py runserver