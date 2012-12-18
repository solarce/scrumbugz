from __future__ import absolute_import

import os

import dj_database_url

from .base import *

SITE_URL = 'http://scrumbugz.paas.allizom.org'

ADMINS = (
    ('Paul', 'pmac@mozilla.com'),
)
MANAGERS = ADMINS

DATABASES = {'default': dj_database_url.config()}

SECRET_KEY = os.environ['SECRET_KEY']

# Celery
BROKER_URL = os.environ['REDIS_URL']
CELERY_RESULT_BACKEND = BROKER_URL

if os.environ.get('MEMCACHIER_SERVERS'):
    os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS')
    os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME')
    os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD')
