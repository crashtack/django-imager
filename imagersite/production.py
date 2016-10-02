from settings import *
import os

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['ec2-54-70-2-170.us-west-2.compute.amazonaws.com',
                 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = '401.imagersite@gmail.com'
SERVER_EMAIL = '401.imagersite@gmail.com'

DATABASES = {
    'default': djdatabase_url.config(default="postgres://myname:mypass@myhost:5432/mydbname")
}
