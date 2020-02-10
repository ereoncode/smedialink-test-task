# -*- coding: utf-8 -*-

"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""
from os import environ

from split_settings.tools import include, optional

environ.setdefault('DJANGO_ENV', 'development')
ENV = environ['DJANGO_ENV']

base_settings = [
    'components/base.py',
    'components/auth.py',
    'components/email.py',
    'components/celery.py',
    'components/platform.py',

    # Select the right env:
    'environments/{0}.py'.format(ENV),

    # Optionally override some settings:
    optional('environments/local.py'),
]

include(*base_settings)
