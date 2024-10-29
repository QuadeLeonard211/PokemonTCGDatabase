from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class userPokemon(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    numberOfPokemon = models.PositiveIntegerField()
