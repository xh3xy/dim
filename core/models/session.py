from core.models.user import User
from django.db import models
import uuid


class Session(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    token = models.BinaryField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(
        blank=True,
        null=True
    )
    #TODO: user_id missing on_update=models.CASCADE?
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    #TODO: parent_id missing on_update=models.CASCADE?
    parent_id = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    device_type = models.CharField(
        max_length=255,
        default='',
    )
    device_os = models.CharField(
        max_length=255,
        default='',
    )
    app_version = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    update_id = models.UUIDField(default=uuid.uuid7)
    is_pending_sync_reset = models.BooleanField(default=False)
    pin_expires_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=['token']),
            models.Index(fields=['update_id']),
        ]

    def save(self, *args, **kwargs):
        self.update_id = uuid.uuid7()
        super().save(*args, **kwargs)
