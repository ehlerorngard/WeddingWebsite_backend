import os
import psycopg2


# CONNECT to the postgres database using a uri and psycopg2:
DATABASE_URL = os.environ.get('DATABASE_URL', '')

conn = psycopg2.connect(DATABASE_URL, sslmode='require')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.orngard.com']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}
print('in production settings')

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'https://www.orngard.com/'


# MY RECENT ADDITIONS:
CORS_ORIGIN_WHITELIST = ['https://www.orngard.com', 'https://orngard.com']

CSRF_TRUSTED_ORIGINS = ['https://www.orngard.com', 'https://orngard.com']

# Ensures the CSRF cookies is sent from a secure (https) location
CSRF_COOKIE_SECURE = False

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
    'x-requested-with',
]

CORS_REPLACE_HTTPS_REFERER = True

CORS_ORIGIN_ALLOW_ALL = True

# to decipher the DATABASE_URL into a format Django can read
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


# added due to SECURITY WARNINGS:

SECURE_CONTENT_TYPE_NOSNIFF = False
SESSION_COOKIE_SECURE = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_SSL_REDIRECT = False
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 60
