import os
import psycopg2


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}

# CONNECT to the postgres database using a uri and psycopg2:
DATABASE_URL = os.environ.get('DATABASE_URL', '')

conn = psycopg2.connect(DATABASE_URL, sslmode='require')


# Use dj_database_url to decipher the DATABASE_URL into a format Django can read
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)




# Static files (CSS, JavaScript, Images) 
# (I'm not actually needing to serve static files from the backend.)
STATIC_URL = 'https://www.orngard.com/'



# Allow the web server host:
ALLOWED_HOSTS = ['orngard.herokuapp.com']

"""
As of v3.0.0 (May 2019) whitelisted CORS origins must include 
a scheme ('http://' or 'https://') as well as hostname:
"""
CORS_ORIGIN_WHITELIST = ['https://orngard.com', 'http://localhost:3000', 'https://www.orngard.com']

CSRF_TRUSTED_ORIGINS = ['localhost:3000', 'www.orngard.com', 'orngard.com']

# Allow these headers on the request
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

# Allow cross origin cookies:
SESSION_COOKIE_SAMESITE = None
CRSF_COOKIE_SAMESITE = None


"""
________[ NOTE ]________
Many of the following are synonymous with the defaults for those settings,
but I like clarity and prefer minimizing ambiguity regarding things that
impact critical functionality, so I am including them for easy future reference.
"""

# Ensure the CSRF cookie is sent from a secure (https) location:
CSRF_COOKIE_SECURE = True

CORS_ALLOW_CREDENTIALS = True

CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'
CSRF_COOKIE_NAME = 'csrftoken'

CSRF_USE_SESSIONS = False

# True would disallow csrf cookies in a response (anything other than in HTTP)
CSRF_COOKIE_HTTPONLY = False

# Only send session cookies to https:
SESSION_COOKIE_SECURE = False

SECURE_CONTENT_TYPE_NOSNIFF = False

# Enable XSS filter in the browser, and force it to always block suspected XSS attacks:
SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = False

X_FRAME_OPTIONS = 'DENY'
