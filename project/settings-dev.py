from .settings import *

DEBUG = True
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = "jhksgdfkjghjhasdgfhkjgasdhkjfg645654%&*"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'datahub',
        'PASSWORD': 'datahub',
        'HOST': os.environ.get('PROJECT_PG_HOST', '127.0.0.1'),
        'PORT': os.environ.get('PROJECT_PG_PORT', '5432'),
    }
}
