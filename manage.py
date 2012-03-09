#!/usr/bin/env python
import os
from django.utils.importlib import import_module
from django.core.management import execute_manager

# Edit this if necessary or override the variable in your environment.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

try:
    from foundation import manage
    manage.setup_environment(__file__)
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in %r.\n" % PROJECT_ROOT)
    sys.exit(1)

if __name__ == "__main__":
    manage.main()
