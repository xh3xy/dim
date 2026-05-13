from core.models.user import User
from django.db import models
import uuid


class Library(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
    )
    name = models.CharField(max_length=255)
    #TODO: missing on_update cascade?
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #import_paths = models.arrayfield?
    #exclusion_patterns = models.arrayfield?
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    refreshed_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    update_id = models.UUIDField(default=uuid.uuid7)

    class Meta:
        indexes = [
            models.Index(fields=['update_id']),
        ]

    def save(self, *args, **kwargs):
        self.update_id = uuid.uuid7()
        super().save(*args, **kwargs)
