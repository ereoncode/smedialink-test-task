from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class TimestampMixin(models.Model):
    """Add following attributes to Django model"""

    created_at = models.DateTimeField(verbose_name=_('creation date'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('modified date'), auto_now=True)

    class Meta:
        abstract = True


class CreatedAtMixin(models.Model):
    """Add following attributes to Django model"""

    created_at = models.DateTimeField(verbose_name=_('creation date'), auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedAtMixin(models.Model):
    """Add following attributes to Django model"""

    updated_at = models.DateTimeField(verbose_name=_('modified date'), auto_now_add=True)

    class Meta:
        abstract = True


class DeletedAtMixin(models.Model):
    """Add following attributes to Django model"""

    deleted_at = models.DateTimeField(verbose_name=_('delete date'), null=True)

    class Meta:
        abstract = True
