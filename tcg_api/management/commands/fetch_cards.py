import requests
from django.core.management.base import BaseCommand
from tcg_api.models import API_cards

class Command(BaseCommand):
    help = "Fetch data from API and populate database for SV6"

    def handle(self, *args, **kwargs):
        response = requests.get('https://api.pokemontcg.io/v2/cards?q=set.id:sv6')
        if response.status_code == 200:
            pokemon_data = response.json()
            for pokemon in pokemon_data['data']:
                # self.stdout.write(f"Current Pokemon: {pokemon} (Type: {type(pokemon)})")
                # if isinstance(pokemon, dict):
                #     isbn = pokemon.get('id', 'N/A')  # Safely get 'isbn'
                #     self.stdout.write(f"ID: {isbn}")
                # else:
                #     self.stderr.write("Unexpected data format. Skipping this entry.")
                API_cards.objects.update_or_create(
                    id=pokemon['id'],
                    defaults={
                        'name': pokemon['name'],
                        'url': pokemon['tcgplayer']['url'],
                    }
                )
            self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch data from the API'))