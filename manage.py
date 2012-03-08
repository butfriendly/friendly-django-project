#!/usr/bin/env python
import os

from django.utils.importlib import import_module 
from django.core.management import execute_manager

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

try:
    module_name = 'project.settings'
    module = import_module(module_name) 
#    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in %r.\n" % PROJECT_ROOT)
    sys.exit(1)

#import settings

if __name__ == "__main__":
    execute_manager(module)
