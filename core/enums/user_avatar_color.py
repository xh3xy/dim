from django.db import models


class UserAvatarColor(models.TextChoices):
    PRIMARY = 'primary', 'Primary'
    PINK = 'pink', 'Pink'
    RED = 'red', 'Red'
    YELLOW = 'yellow', 'Yellow'
    BLUE = 'blue', 'Blue'
    GREEN = 'green', 'Green'
    PURPLE = 'purple', 'Purple'
    ORANGE = 'orange', 'Orange'
    GRAY = 'gray', 'Gray'
    AMBER = 'amber', 'Amber'
