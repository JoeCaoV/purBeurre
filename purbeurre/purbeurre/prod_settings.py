import dj_database_url

from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default']=dj_database_url.config()

ALLOWED_HOSTS = ['murmuring-falls-38065.herokuapp.com']