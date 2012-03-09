import os
import sys

from foundation.settings import *

# Defines the views served for root URLs.
ROOT_URLCONF = 'project.urls'

INSTALLED_APPS = list(INSTALLED_APPS) + [
    # Application base, containing global templates.
    'project.base',
]

PIPELINE_CSS = {
    'common': {
        'source_filenames': (
            'css/core.less',
#            'css/colors/*.less',
#            'css/layers.less'
        ),
        'output_filename': 'css/common.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'jquery': {
        'external_urls': (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.5.2/jquery-ui.min.js',
        ),
    },
    'common': {
        'source_filenames': (
#            'js/d3.js',
#            'js/collections/*.js',
            'js/application.js',
#            'js/templates/**/*.jst', # JavsScript templates
        ),
        'output_filename': 'js/common.js',
    }
}

# SOUTH

# SOUTH_AUTO_FREEZE_APP = True

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

