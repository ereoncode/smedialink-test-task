"""
WSGI config for auction project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.utils.module_loading import import_string
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_auction.settings')
STATIC_ROOT = os.environ.get('WHITE_NOISE_STATIC_ROOT')

application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_ROOT)

try:
    setup_hook_path = getattr(settings, 'POST_SETUP_HOOK_PATH')
    post_setup_hook = import_string(setup_hook_path)

    post_setup_hook()
except (ImportError, Exception) as e:
    sys.stderr.write(repr(e) + '\n')
