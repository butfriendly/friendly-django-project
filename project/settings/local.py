from . import base

# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = False

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = True

#print base.INSTALLED_APPS

INSTALLED_APPS = list(base.INSTALLED_APPS) + [
    # Example code. Can (and should) be removed for actual projects.
    'project.example',

    'debug_toolbar',
    'devserver',
]

SECRET_KEY = '123'

print INSTALLED_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_app.sq3',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET storage_engine=InnoDB',
            'charset' : 'utf8',
            'use_unicode' : True,
            },
        'TEST_CHARSET': 'utf8',
        'TEST_COLLATION': 'utf8_general_ci',
        },
    # 'slave': {
    #     ...
    # },
}