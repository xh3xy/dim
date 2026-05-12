from core.enums.sync_entity_type import SyncEntityType
from core.models.session import Session
from django.db import models
import uuid


class SyncCheckpoint(models.Model):
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
    )
    type = models.CharField(
        max_length=64,
        choices=SyncEntityType.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ack = models.CharField(max_length=255)
    update_id = models.UUIDField(default=uuid.uuid7)


    class Meta:
        indexes = [
            models.Index(fields=['update_id'])
        ]
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'session',
                    'type',
                ],
                name='unique_session_per_type',
            )
        ]
