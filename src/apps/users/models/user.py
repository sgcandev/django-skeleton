from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from src.apps.core.querysets import CoreQuerySet


class BaseUserManager(UserManager):
    """
    Provides a Manager to handle Query Sets and manage soft deleting
    """

    def __init__(self, *args, **kwargs):
        self.with_trashed = kwargs.pop("with_trashed", False)
        self.only_trashed = kwargs.pop("only_trashed", False)
        super(BaseUserManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.only_trashed:
            return CoreQuerySet(self.model).exclude(deleted_at=None)
        if not self.with_trashed:
            return CoreQuerySet(self.model).filter(deleted_at=None)
        return CoreQuerySet(self.model)

    def force_delete(self):
        return self.get_queryset().force_delete()

    def deleted_queryset(self):
        return CoreQuerySet(self.model).exclude(deleted_at__isnull=True)

    def complete_queryset(self):
        return CoreQuerySet(self.model).all()

    """
    Create and save a user with the given username, email, and password.
    """

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class BaseUserModel(AbstractUser):
    # managers
    objects: BaseUserManager = BaseUserManager()
    all_objects = BaseUserManager(with_trashed=True, only_trashed=False)
    trashed_objects = BaseUserManager(only_trashed=True, with_trashed=False)

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
