from enum import Enum
from typing import Type, Optional

from django.db import models


class EnumBasedManager(models.Manager):
    """Enum-baser ORM models manager

    Example:

    class UserStatusEnum(Enum):
        ACTIVE = 1
        BLOCKED = 2

    class UserStatus(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=255)  # will be initialized via UserStatusEnum.name

        objects = models.Manager()
        get = EnumBasedManager(enum=UserStatusEnum, enum_lookup_field='name')


    active = UserStatus.get.ACTIVE  # will delegate lookup to Manager.get() method
                                    # and pass `ACTIVE` as model's `name` attribute's filter
    """

    enum: Type[Enum] = None
    enum_lookup_field: str = None
    model_lookup_field: Optional[str] = None

    def __init__(self, enum: Type[Enum], enum_lookup_field: str, model_lookup_field: Optional[str] = None):
        """
        :param enum: Подкласс Enum, по атрибутам которого будет строиться QuerySet
        :param enum_lookup_field: атрибут Enum (name, value)
        :param model_lookup_field: атрибут Django-модели, по которой будет строиться QuerySet.
                                   Если не указан - используется значение enum_lookup_field
        """
        if not issubclass(enum, Enum):
            raise ValueError('`enum` must be a Enum subclass')

        if enum_lookup_field not in ('name', 'value'):
            raise ValueError('`enum_lookup_field` must be `name` or `value`')

        self.enum = enum
        self.enum_lookup_field = enum_lookup_field
        self.model_lookup_field = model_lookup_field or enum_lookup_field

        super().__init__()

    def __getattr__(self, item):
        if hasattr(self.enum, item):
            enum_item = getattr(self.enum, item, None)
            filter_kwargs = {self.model_lookup_field: getattr(enum_item, self.enum_lookup_field)}
            return self.get(**filter_kwargs)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")
