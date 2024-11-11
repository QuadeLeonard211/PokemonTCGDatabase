from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
    listPokemon = models.JSONField(default=list, blank=True)

    def add_pokemon(self, mon):
        self.listPokemon.append(mon)
        self.save()
        print("Added " + mon)
    
    def remove_pokemon(self, mon):
        if mon in self.listPokemon:
            self.listPokemon.remove(mon)
            self.save()
            print("Removed " + mon)
        else:
            print(mon + " not in list")
    
    def get_pokemon(self):
        return self.listPokemon
    
    def clear_pokemon(self):
        self.listPokemon.clear()
        self.save()

    def __str__(self):
        return self.username