import os
from getenv import env

ROOT = os.path.dirname(os.path.abspath(__file__))
cd = lambda *a: os.path.join(ROOT, *a)
PROJECT = os.path.basename(ROOT)

RAVEN_CONFIG = {
    'dsn': env('SENTRY_DSN', 'https://ea4cd3cd72224776a2e940e15657547a:fd09a90078754f1a9bcad0b202faee92@app.getsentry.com/19720'
),
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', '#a--*0*hy)r9uqqlt)640o$78(4lp)-d+7-!p+^l#i4n56+s9&')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
    'products',
    'debug_toolbar',
    'bootstrap3',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'raven.contrib.django.middleware.Sentry404CatchMiddleware',
    'raven.contrib.django.middleware.SentryResponseErrorIdMiddleware',
)

ROOT_URLCONF = '%s.urls' % PROJECT

WSGI_APPLICATION = '%s.wsgi.application' % PROJECT



# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default=env('DATABASE_URL', 'sqlite:////Users/annalopatinski/DJANGO/mebelm/mebelmdb.sqlite3'))
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
MEDIA_ROOT = cd('public/uploads')
MEDIA_URL = '/uploads/'
STATIC_ROOT = cd('public', 'assets')
STATIC_URL = '/assets/'

TEMPLATE_DIRS = (
    cd('templates'),
)
