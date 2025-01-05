import os
from emmerce_crm_backend.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SENDING_MAIL = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DOMAIN = config('DOMAIN', default='')

