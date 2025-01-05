import os
import dj_database_url
from emmerce_crm_backend.settings.base import *

from decouple import config, Csv

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False)  

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='emmercecrmbackend-production.up.railway.app,127.0.0.1,localhost').split(',')
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='', cast=Csv())

DJANGO_ALLOWED_HOSTS= os.getenv('ALLOWED_HOSTS', 'emmercecrmbackend-production.up.railway.app,127.0.0.1,localhost').split(',')

DATABASES = {
    'default': dj_database_url.config(
        default=f"postgres://{config('POSTGRES_USER')}:{config('POSTGRES_PASSWORD')}@{config('DB_HOST')}:{config('DB_PORT')}/{config('POSTGRES_DB')}"
    )
}

