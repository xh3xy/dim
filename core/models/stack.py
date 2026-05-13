from core.models.asset import Asset
from core.models.user import User
from django.db import models
import uuid


class Stack(models.Model):
    id = models.UUIDField(default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    update_id = models.UUIDField(default=uuid.uuid7)
    primary_asset = models.ForeignKey(Asset, on_delete=models.PROTECT) # TODO: protect?
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.update_id = uuid.uuid7()
        super().save(*args, **kwargs)
