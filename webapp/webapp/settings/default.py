import dj_database_url
import django_cache_url
import os
import re


# ===================
# = Global Settings =
# ===================

DEBUG = os.environ.get('DEBUG')
ADMINS = (
    ('admin', 'admin@webapp.com'),
)
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ["*"]
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)
TIME_ZONE = 'Europe/Zurich'
SITE_ID = 1
USE_I18N = True
USE_L10N = False
USE_TZ = True
DATE_FORMAT = 'd.m.Y'
DATE_INPUT_FORMATS = ('%d.%m.%Y',)
DATETIME_FORMAT = 'd.m.y H:i'
ATOMIC_REQUESTS = True


# ===============================
# = Databases, Caches, Sessions =
# ===============================

DATABASES = {'default': dj_database_url.parse(
    'postgres://postgres@{host}:{port}/postgres'.format(
        host=os.environ.get('DB_PORT_5432_TCP_ADDR'),
        port=os.environ.get('DB_PORT_5432_TCP_PORT')))}

CACHES = {
    'default': django_cache_url.config(
        'hiredis://{host}:{port}/1/webapp'.format(
            host=os.environ.get('REDIS_PORT_6379_TCP_ADDR'),
            port=os.environ.get('REDIS_PORT_6379_TCP_PORT'))),
    'sessions': django_cache_url.config(
        'hiredis://{host}:{port}/2/webapp'.format(
            host=os.environ.get('REDIS_PORT_6379_TCP_ADDR'),
            port=os.environ.get('REDIS_PORT_6379_TCP_PORT'))),
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'sessions'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
SESSION_COOKIE_HTTPONLY = True


# ===========================
# = Directory Declaractions =
# ===========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ROOT_URLCONF = 'webapp.urls'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# ================
# = File serving =
# ================

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'webapp', 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# ===========================
# = Django-specific Modules =
# ===========================

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',  # must be loaded first
    'debreach.middleware.RandomCommentMiddleware',  # must be loaded first or right next after GZipMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'debreach.middleware.CSRFCryptMiddleware',  # must be loaded before django CsrfViewMiddleware
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# =============
# = Templates =
# =============

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'webapp', 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'debreach.context_processors.csrf',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# ===============
# = Django Apps =
# ===============

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'debreach',  # provides basic mitigation against the BREACH attack
    'webapp',
)


# ===========
# = Logging =
# ===========

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(name)-40s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.handlers.SentryHandler',
            'filters': ['require_debug_false'],
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console', 'sentry'],
            'propagate': False,  # Root loggers cannot propagate up further...
        },
        'django.db': {
            'level': 'INFO',  # Don't show normal DB queries on console
            'handlers': ['console'],
            'propagate': True,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}

CELERYD_HIJACK_ROOT_LOGGER = False


# ==========
# = Celery =
# ==========

CELERYBEAT_SCHEDULE = {
    # 'eaxample-print': {
    #     'task': 'tasks.print',
    #     'schedule': timedelta(seconds=30)
    # },
}

BROKER_URL = 'amqp://admin:{password}@{host}//'.format(
                password=os.environ.get('RABBITMQ_ENV_RABBITMQ_PASS'),
                host=os.environ.get('RABBITMQ_PORT_5672_TCP_ADDR'))
CELERY_RESULT_BACKEND = 'redis://{host}:{port}/0'.format(
                            host=os.environ.get('REDIS_PORT_6379_TCP_ADDR'),
                            port=os.environ.get('REDIS_PORT_6379_TCP_PORT'))
CELERY_SEND_EVENTS = False
CELERY_ENABLE_UTC = True
CELERY_TASK_SERIALIZER = 'json'


# ==========================
# = Miscellaneous Settings =
# ==========================

IGNORABLE_404_URLS = (
    re.compile(r'^/cgi-bin/'),
    re.compile(r'\.php$'),
    re.compile(r'\.pl$'),
    re.compile(r'\.cgi$'),
)
