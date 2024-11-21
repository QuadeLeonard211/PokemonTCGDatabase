from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
    listPokemon = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.username