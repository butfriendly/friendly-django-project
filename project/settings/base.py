import os
import sys

from foundation.settings import *

# Defines the views served for root URLs.
ROOT_URLCONF = 'project.urls'

INSTALLED_APPS = list(INSTALLED_APPS) + [
    # Application base, containing global templates.
    'project.base',
    # Example code. Can (and should) be removed for actual projects.
    'project.example',
]

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

