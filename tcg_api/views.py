from django.shortcuts import render
from tcg_api.models import API_cards

def card_list(request): 
    print('testing if this view is actually getting called')
    cards = API_cards.objects.all()
    for card in cards:
        # pass
        print(card.name + " " + str(card.trendPrice))
    return render(request, 'api-test.html', {'cards': cards})
    