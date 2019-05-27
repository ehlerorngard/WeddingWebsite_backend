import os
import psycopg2


# CONNECT to the postgres database using a uri and psycopg2:
DATABASE_URL = os.environ.get('DATABASE_URL', '')

conn = psycopg2.connect(DATABASE_URL, sslmode='require')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['orngard.herokuapp.com']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'https://www.orngard.com/'




# Ensures the CSRF cookies is sent from a secure (https) location
CSRF_COOKIE_SECURE = True

CORS_ALLOW_HEADERS = [
    'accept',
    'access-control-request-headers',
    'access-control-request-method',
    'accept-encoding',
    'accept-language',
    'authorization',
    'cache',
    'connection',
    'content-type',
    'cookie',
    'csrftoken',
    'date',
    'dnt',
    'host',
    'origin',
    'referer',
    'server',
    'user-agent',
    'vary',
    'x-csrftoken',
    'x-csrf-token',
    'x-requested-with',
]


# to decipher the DATABASE_URL into a format Django can read
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


# added due to SECURITY WARNINGS:

SESSION_COOKIE_SAMESITE = None
CRSF_COOKIE_SAMESITE = None


SECURE_CONTENT_TYPE_NOSNIFF = False
SESSION_COOKIE_SECURE = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_SSL_REDIRECT = False
X_FRAME_OPTIONS = 'DENY'

# SECURE_HSTS_SECONDS = 60

CSRF_USE_SESSIONS = False
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_NAME = 'csrftoken'

# CSRF_COOKIE_DOMAIN = 'orngard.com' # don't need with CSRF_TRUSTED_ORIGINS


# Don't need since I'm not using cookies for authentication:
CORS_ALLOW_CREDENTIALS = True

CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'


"""
As of v3.0.0 (May 2019) whitelisted CORS origins must include 
a scheme ('http://' or 'https://') as well as hostname:
"""
CORS_ORIGIN_WHITELIST = ['https://orngard.com', 'http://localhost:3000', 'https://www.orngard.com']
# CORS_ORIGIN_ALLOW_ALL = True

CSRF_TRUSTED_ORIGINS = ['localhost:3000', 'www.orngard.com', 'orngard.com']
