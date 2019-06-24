import dj_database_url

from .settings import *

DEBUG = False

MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['murmuring-falls-38065.herokuapp.com']
