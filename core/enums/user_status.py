from django.db import models


class UserStatus(models.TextChoices):
    ACTIVE = 'active', 'Active'
    REMOVING = 'removing', 'Removing'
    DELETED = 'deleted', 'Deleted'
