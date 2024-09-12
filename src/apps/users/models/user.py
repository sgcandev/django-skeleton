from django.contrib.auth.models import AbstractUser
from django.db import models

from src.apps.core.managers import CoreUserManager


class BaseUserModel(AbstractUser):
    # managers
    objects = CoreUserManager()
    all_objects = CoreUserManager(with_trashed=True, only_trashed=False)
    trashed_objects = CoreUserManager(only_trashed=True, with_trashed=False)

    class Meta:
        abstract = True


class User(BaseUserModel):
    class UserType(models.TextChoices):
        INTERNAL = "1", "Internal"
        EXTERNAL = "2", "External"

    # attributes
    email = models.EmailField(unique=True)
    type = models.CharField(
        max_length=2, choices=UserType.choices, default=UserType.EXTERNAL
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(
        blank=True, null=True, db_index=True, editable=False
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password", "type", "is_active"]

    class Meta:
        db_table = "auth_user"
        permissions = [("manage_user", "Can manage users")]
