import os
import sys

activate_this = os.path.join("/home/djangolackey/code/harmonysite", "bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "church/")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "church/apps/")))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

os.environ['DJANGO_SETTINGS_MODULE'] = 'church.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
