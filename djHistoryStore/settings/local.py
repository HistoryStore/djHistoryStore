from .base import *
from . keys import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = djangoKey

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}





