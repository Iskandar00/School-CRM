import os
from django.conf import settings

if settings.DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['DATA_BASE_NAME'],
            'USER': os.environ['DATA_BASE_USER'],
            'PASSWORD': os.environ['DATA_BASE_PASSWORD'],
            'HOST': os.environ['DATA_BASE_HOST'],
            'PORT': '5432'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': settings.BASE_DIR / 'db.sqlite3',
        }
    }
