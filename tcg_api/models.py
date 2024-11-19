from django.db import models

class API_cards(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    rarity = models.CharField(max_length=255, default="normal")

    def __str__(self):
        return self.id