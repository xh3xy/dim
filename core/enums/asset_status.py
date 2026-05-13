from django.db import models


class AssetStatus(models.TextChoices):
    ACTIVE = 'Active', 'active',
    TRASHED = 'Trashed', 'trashed',
    DELETED = 'Deleted', 'deleted',
