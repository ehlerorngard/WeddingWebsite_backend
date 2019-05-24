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
CORS_ORIGIN_WHITELIST = ['https://www.orngard.com']

CSRF_TRUSTED_ORIGINS = ['https://www.orngard.com']

# Marked True, will only send a CSRF token to a secure (https) location
CSRF_COOKIE_SECURE = True

# to decipher the DATABASE_URL into a format Django can read
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


# added due to SECURITY WARNINGS:

SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = False
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 60
