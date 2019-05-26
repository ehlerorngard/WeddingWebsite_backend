import os
import psycopg2


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'orngard.com']


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


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'https://www.orngard.com/'


# MY RECENT ADDITIONS:
CORS_ORIGIN_WHITELIST = ['http://localhost:3000', 'https://orngard.com']

CSRF_TRUSTED_ORIGINS = ['localhost:3000', 'orngard.com']

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'referer',
    'user-agent',
    'x-csrftoken',
    'x-csrf-token',
    'csrftoken',
    'x-requested-with',
    'Access-Control-Request-Headers',
    'Access-Control-Request-Method',
    'host',
    'connection',
    'cookie',
    'accept-language',
]

SECURE_SSL_REDIRECT = False
HOST_SCHEME = "http://"
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = None
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_FRAME_DENY = False
CORS_REPLACE_HTTPS_REFERER = False

CORS_EXPOSE_HEADERS = [
    'csrftoken',
    'x-csrftoken',
]

# CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'