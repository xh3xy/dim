from django.db import models


class AssetVisibility(models.TextChoices):
    ARCHIVE = 'Archive', 'archive',
    TIMELINE = 'Timeline', 'timeline',
    HIDDEN = 'Hidden', 'hidden',
    LOCKED = 'Locked', 'locked',
