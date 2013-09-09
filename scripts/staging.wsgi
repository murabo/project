# -*- mode: Python; -*-
#import site
#site.addsitedir('/var/webapps/gokudo/shared/lib/python2.5/site-packages')
envpath = '/usr/local/lib/python2.7/site-packages'
import os
#import sys

#path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#if path2 not in sys.path:
#   sys.path.insert(0, path2)

#path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../cocolink'))
#if path not in sys.path:
#   sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_staging'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
