"""Django smtp settings"""

from web_auction.settings.components import config

EMAIL_HOST = config('SMTP_HOST')
EMAIL_PORT = config('SMTP_PORT', 465, cast=int)
EMAIL_HOST_USER = config('SMTP_USER')
EMAIL_HOST_PASSWORD = config('SMTP_PASSWORD')
EMAIL_USE_TLS = config('SMTP_USE_TLS', cast=bool, default=True)
EMAIL_NO_REPLY = config('EMAIL_NO_REPLY', EMAIL_HOST_USER)
