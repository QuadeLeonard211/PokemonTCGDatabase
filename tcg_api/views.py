from django.shortcuts import render
import requests

def home(request):
    response = requests.get('https://api.pokemontcg.io/v2/cards/sv6-1')
    data = response.json()
    return render(request, 'home.html', {
        'card_data': data['data']
    })