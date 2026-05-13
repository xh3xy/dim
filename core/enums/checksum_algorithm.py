from django.db import models


class ChecksumAlgorithm(models.TextChoices):
    SHA1FILE = 'sha1', 'sha1'
    SHA1PATH = 'sha1-path', 'sha1-path'
