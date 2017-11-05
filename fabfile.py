import os
import django

# set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    django.setup()
except Exception as e:
    print("WARNING: Can't configure Django -- tasks depending on Django will fail:\n%s" % e)

from fabric.api import local
from fabric.decorators import task


@task(alias='run')
def run_django():
    local("python manage.py runserver")


@task
def install_reqs():
    local("pip install -r requirements.txt")


@task
def init_db():
    """
        Set up new dev database.
    """
    local("python manage.py makemigrations")
    local("python manage.py migrate")

