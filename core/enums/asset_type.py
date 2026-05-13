from django.db import models


class AssetType(models.TextChoices):
    IMAGE = 'Image', 'IMAGE'
    VIDEO = 'Video', 'VIDEO'
    AUDIO = 'Audio', 'AUDIO'
    OTHER = 'Other', 'OTHER'
