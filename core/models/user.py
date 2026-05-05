from core.enums.user_avatar_color import UserAvatarColor
from core.enums.user_status import UserStatus
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import uuid

def profile_image_file_path(instance, filename):
    #TODO: Requires processing?
    #TODO: > Trace appear in src/utils/profile-image.ts
    #TODO: >> Appears that server uses generateThumbnail in generateProfileImage
    #TODO: >> (src/repositories/media.repository.ts)
    return f'profile/{instance.id}/{uuid.uuid4()}.{filename.split('.')[-1]}'


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    email = models.EmailField(unique=True)
    pin_code = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(
        upload_to=profile_image_file_path,
        blank=True,
        null=True,
    )
    is_admin = models.BooleanField(default=False)
    should_change_password = models.BooleanField(default=True)
    avatar_color = models.CharField(
        max_length=64,
        choices=UserAvatarColor.choices,
    )
    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    oauth_id = models.CharField(
        max_length=255,
        blank=True,
        default='',
    )
    updated_at = models.DateTimeField(auto_now=True)
    storage_label = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=64,
        default='',
    )
    quota_size_in_bytes = models.BigIntegerField(
        blank=True,
        null=True,
    )
    quota_usage_in_bytes = models.BigIntegerField(default=0)
    status = models.CharField(
        max_length=64,
        choices=UserStatus.choices,
    )
    profile_changed_at = models.DateTimeField(auto_now_add=True)
    update_id = models.UUIDField(
        default=uuid.uuid4,
        db_index=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        indexes = [
            models.Index(
                fields=['updated_at', 'id']
            )
        ]

    def __str__(self):
        return self.email
