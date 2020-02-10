"""Authentication settings

https://django-rest-auth.readthedocs.io/en/latest/installation.html#jwt-support-optional

if REST_USE_JWT == True - JSONWebTokenAuthentication will be used instead of TokenAuthentication
JWT_AUTH settings: https://jpadilla.github.io/django-rest-framework-jwt/
"""
from datetime import timedelta

from web_auction.settings.components import config

REST_USE_JWT = True

# only if REST_USE_JWT == True
JWT_AUTH = {
    'JWT_SECRET_KEY': config('JWT_SECRET_KEY', default=config('SECRET_KEY')),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_EXPIRATION_DELTA': timedelta(seconds=300)
}
