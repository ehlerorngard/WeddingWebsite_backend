import os
import psycopg2


# Debug only here in development
DEBUG = True


# ––––– Database –––––
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


# Specify permitted origins and hosts for the the cross-origin connection:
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'orngard.herokuapp.com']

CORS_ORIGIN_WHITELIST = ['http://localhost:3000', 'https://orngard.com']

CSRF_TRUSTED_ORIGINS = ['localhost:3000', 'orngard.com']


# Permitted request headers
CORS_ALLOW_HEADERS = [
    'accept',
    'access-control-request-headers',
    'access-control-request-method',
    'accept-encoding',
    'accept-language',
    'authorization',
    'connection',
    'content-type',
    'cookie',
    'date',
    'dnt',
    'host',
    'origin',
    'referer',
    'user-agent',
    'vary',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ALLOW_CREDENTIALS = True
CSRF_USE_SESSIONS = False
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_NAME = 'csrftoken'
CSRF_COOKIE_SECURE = False
CORS_REPLACE_HTTPS_REFERER = False
CORS_EXPOSE_HEADERS = [
    'x-csrftoken',
]

SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
HOST_SCHEME = "http://"
SECURE_HSTS_SECONDS = None
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_FRAME_DENY = False
