import json
from typing import Any
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from django.db import models
from pokemondb.models import Card
from pokemondb.filters import CardFilter
from accounts.models import CustomUser
from tcg_api.models import API_cards
from django.db.models import Q
from django.shortcuts import render

# Create your views here.

class collection_view(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Welcome to your collection!'
        return context
    
    def get(self, request):
        current_user = request.user
        owned_cards = current_user.listPokemon
        card_list = Card.objects.filter(id__in=owned_cards)
        
        my_filter = CardFilter(request.GET, queryset=card_list)
        card_list = my_filter.qs

        api_card_list = []
        collection_value = 0
        for card in card_list:
            temp_id = card.set_id + "-" + str(card.card_number)
            temp_api_card = API_cards.objects.get(temp_id)
            api_card_list.append(temp_api_card)
            collection_value += temp_api_card.trendPrice

        combined_list = zip(card_list, api_card_list)

        context = {"card_list":combined_list, "my_filter":my_filter, "api_card_list":api_card_list}

        return render(request, "collection/collection.html", context)
