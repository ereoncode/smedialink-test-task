"""Auction platform settings"""

from web_auction.settings.components import BASE_DIR, config

ADMIN_USERNAME = config('ADMIN_USERNAME')
ADMIN_EMAIL = config('ADMIN_EMAIL')
ADMIN_PASSWORD = config('ADMIN_PASSWORD')

POST_SETUP_HOOK_PATH = 'common.setup_hooks.post_setup_hooks'
