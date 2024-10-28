from django.db import models
import django_filters

#creates table categories for the card database
class Card(models.Model):
    # name of the card (ie:bulbasaur, pokemon_catcher)
    name = models.CharField(max_length=100, default="bulbasaur")

    # the set the card came from (ie:twilight_masquerade)
    collection = models.CharField(max_length=100, default="twilight_masquerade")

    # the category of the card NOT THE POKEMON TYPE (ie: supporter, pokemon)
    card_type = models.CharField(max_length=50, default="item")

    # the pokemon's type (ie: grass) trainers are empty
    element_type = models.CharField(max_length=50, default="trainer")

    # the card image
    image = models.CharField(max_length=128, default="images/1-Venusaur-ex-Stellar-Crown.png")

    # the pokemon's stage (basic=0, trainer=null)
    stage = models.SmallIntegerField(null=True)

    # the pokemon's hp (trainer=null)
    hp = models.IntegerField(null=True)

    # the pokemon's suffix if applicable (ie:ex, v, vstar)
    suffix = models.CharField(max_length=20, default="")

    #the dumb card number cause sam said so
    card_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    