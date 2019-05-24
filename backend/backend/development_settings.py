import os
import psycopg2


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'www.orngard.com']


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
print('in development settings')

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'https://www.orngard.com/'


# MY RECENT ADDITIONS:
CORS_ORIGIN_WHITELIST = ['http://localhost:3000', 'https://www.orngard.com']

CSRF_TRUSTED_ORIGINS = ['http://localhost:3000', 'https://www.orngard.com']


SECURE_SSL_REDIRECT = False
HOST_SCHEME = "http://"
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = None
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_FRAME_DENY = False
CORS_REPLACE_HTTPS_REFERER = False