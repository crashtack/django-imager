from .settings import *
import os
import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(',')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
SECRET_KEY = os.environ.get("SECRET_KEY")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = '401.imagersite@gmail.com'
SERVER_EMAIL = '401.imagersite@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '401.imagersite@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DATABASES = {
    'default': dj_database_url.config(default=os.environ['DATABASE_URL'])
}
