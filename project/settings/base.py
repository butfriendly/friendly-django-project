import os
import sys

#from .manage import PROJECT_ROOT

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

path = lambda *x: os.path.join(PROJECT_ROOT, *x)

# Is this a dev instance?
DEV = False

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

ROOT_URLCONF = 'project.urls'
#ROOT_URLCONF = '%s.urls' % os.path.basename(PROJECT_ROOT)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.redirects',
    'raven.contrib.django',
    'waffle',
    # Application base, containing global templates.
    'project.base',
    )

SEND_BROKEN_LINK_EMAILS = True

COMMENTS_HIDE_REMOVED = False

# SOUTH

SOUTH_AUTO_FREEZE_APP = True

#COMPRESS_VERSION = True
#COMPRESS_AUTO = False
#COMPRESS_CSS = {
#    'flother': {
#        'source_filenames': (
#            'core/css/reset.css', 
#            'core/css/structure.css',
#            'core/css/typography.css', 
#            'core/css/sections.css'
#        ),
#        'output_filename': 'core/css/flother.r?.css',
#        'extra_context': {
#            'media': 'screen,projection',
#        },
#    },
#}
#COMPRESS_JS = {}
#CSSTIDY_ARGUMENTS = '--preserve_css=true --remove_last_\;=true --lowercase_s=true --sort_properties=true --template=highest'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    )

TEMPLATE_DIRS = (
    path('templates'),
)

MIDDLEWARE_CLASSES = (
    # Log 404 events to the Sentry server
    'raven.contrib.django.middleware.Sentry404CatchMiddleware',

    # Sentry supports sending a message ID to your clients so that
    # they can be tracked easily by your development team.
    'raven.contrib.django.middleware.SentryResponseErrorIdMiddleware',

    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'waffle.middleware.WaffleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)


##
# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
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
    },
}

##
# DEVSERVER
# https://github.com/dcramer/django-devserver

DEVSERVER_ARGS = []
DEVSERVER_DEFAULT_ADDR = '127.0.0.1'
DEVSERVER_DEFAULT_PORT = '8000'
DEVSERVER_IGNORED_PREFIXES = ['/media', '/static']
DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # Modules not enabled by default
    'devserver.modules.ajax.AjaxDumpModule',
    'devserver.modules.profile.MemoryUseModule',
    'devserver.modules.cache.CacheSummaryModule',
    'devserver.modules.profile.LineProfilerModule',
    )

##
# SENTRY

# No trailing slash!
SENTRY_URL_PREFIX = 'http://127.0.0.1'

# SENTRY_KEY is a unique randomly generated secret key for your server, and it
# acts as a signing token
SENTRY_KEY = '0123456789abcde'

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    # 'worker_class': 'gevent',
}