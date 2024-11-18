import requests
from django.core.management.base import BaseCommand
from tcg_api.models import api_cards

class Commands(BaseCommand):
    help = "Fetch data from API and populate database"

    def handel(self, *args, **kwargs):
        response = requests.get