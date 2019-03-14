from .base import *

DEBUG = True

ALLOWED_HOSTS = ['192.168.24.72']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'

#MEDIA_ROOT = os.path.join(BASE_DIR, 'websites')
MEDIA_URL = '/'


