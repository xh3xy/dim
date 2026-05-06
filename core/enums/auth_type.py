from django.db import models


class AuthType(models.TextChoices):
    PASSWORD = 'password', 'Password'
    OAUTH = 'oauth', 'OAuth'
