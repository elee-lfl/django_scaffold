import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

sys.path.append(ROOT_DIR)
sys.path.append(os.path.join(ROOT_DIR, '<<PROJECT>>'))

os.environ['DJANGO_SETTINGS_MODULE'] = '<<PROJECT>>.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
