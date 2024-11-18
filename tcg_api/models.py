from django.db import models

class api_cards(models.Model):
    id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    market_price = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.id