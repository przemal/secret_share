from secret_share.settings.base import *  # noqa


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db_test.sqlite3'),
    }
}
