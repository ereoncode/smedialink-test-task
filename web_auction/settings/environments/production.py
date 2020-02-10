# -*- coding: utf-8 -*-

"""
This file contains all the settings used in production.
This file is required and if development.py is present these
values are overridden.
"""
import os

from decouple import Csv

from web_auction.settings.components import config, BASE_DIR

# Production flags:
# https://docs.djangoproject.com/en/2.2/howto/deployment/

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
] + config('ALLOWED_HOSTS', cast=Csv())

# Staticfiles
# https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/

STATICFILES_STORAGE = (
    'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
)

STATIC_ROOT = BASE_DIR.joinpath('static')

STATIC_URL = '/static/'

os.environ.setdefault('WHITE_NOISE_STATIC_ROOT', str(STATIC_ROOT))

MEDIA_ROOT = STATIC_ROOT.joinpath('media')

MEDIA_URL = '/media/'

SESSION_COOKIE_AGE = 5 * 60

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
