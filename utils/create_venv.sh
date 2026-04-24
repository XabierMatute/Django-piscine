python3 -m virtualenv django_venv
# enter
source django_venv/bin/activate

pip install django
pip freeze > requirements.txt