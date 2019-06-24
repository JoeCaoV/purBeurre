import dj_database_url

from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

ALLOWED_HOSTS = ['.herokuapp.com']
