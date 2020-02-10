"""Actions performed after django.setup()"""
import sys

from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


def init_default_users():
    """Adding default users and roles"""
    sys.stdout.write('init default users\n')

    admin, created = User.objects.get_or_create(
        username=settings.ADMIN_USERNAME,
        email=settings.ADMIN_EMAIL,
        is_staff=True,
        is_superuser=True
    )
    if created:
        admin.set_password(settings.ADMIN_PASSWORD)
        admin.save()


def post_setup_hooks():
    """Actions performed after django.setup()"""
    init_default_users()
