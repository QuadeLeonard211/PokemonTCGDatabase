from django.shortcuts import render
from tcg_api.models import API_cards

def card_list(request): 
    cards = API_cards.objects.all()
    for card in cards:
        print(card.name)
    return render(request, 'home.html', {'cards': cards})
    