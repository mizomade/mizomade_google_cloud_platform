from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql',
        'HOST':'/cloudsql/mizomade-266914:us-central1:mizodb',
        'NAME':'postgres',
        'USER':'postgres',
        'PASSWORD':'postgres',
    }
}

SECRET_KEY = "an insecure secret"
ALLOWED_HOSTS = ['mizomade-266914.appspot.com']