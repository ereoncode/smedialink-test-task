# -*- coding: utf-8 -*-

"""
This file contains all the settings that defines the development server.
SECURITY WARNING: don't run with debug turned on in production!
"""
import os
from typing import List

from decouple import Csv

from web_auction.settings.components import config, BASE_DIR

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '[::1]',
] + config('ALLOWED_HOSTS', cast=Csv())

STATICFILES_DIRS: List[str] = []

STATICFILES_STORAGE = (
    'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
)

STATIC_ROOT = BASE_DIR.joinpath('static')

STATIC_URL = '/static/'

os.environ.setdefault('WHITE_NOISE_STATIC_ROOT', str(STATIC_ROOT))

MEDIA_ROOT = STATIC_ROOT.joinpath('media')

MEDIA_URL = '/media/'