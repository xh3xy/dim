from core.models.user import User
from django.db import models
import uuid


class ApiKey(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True
    )
    name = models.CharField(max_length=255)
    key = models.BinaryField(unique=True)
    # TODO: missing on_update=CASCADE?
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # TODO: Permissions
    # permissions = arrayfield?
    update_id = models.UUIDField(default=uuid.uuid7)

    class Meta:
        indexes = [
            models.Index(fields=['key']),
        ]

    def save(self, *args, **kwargs):
        self.update_id = uuid.uuid7()
        super().save(*args, **kwargs)
