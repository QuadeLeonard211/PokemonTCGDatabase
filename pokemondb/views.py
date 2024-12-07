from itertools import zip_longest
import json
from typing import Any
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from django.db import models
from .models import Card
from tcg_api.models import API_cards
from accounts.models import CustomUser
from django.db.models import Q
from django.shortcuts import render
from .filters import CardFilter
from django.core.management import call_command

# Create your views here.
class pokemondb_homepage_view(TemplateView):
    template_name = "pokemondb/homepage.html"

    #function to add a 'greeting' that can be used in the HTML template (this will likely be changed later to information that is more useful than a greeting)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['greeting'] = 'Welcome to my homepage!'
        return context
    
class pokemondb_gallery_view(TemplateView):
    template_name = 'pokemondb/gallery.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Welcome to the gallery!'
        return context

    def get(self, request):
        if (not API_cards.objects.exists()):
            call_fetch_cards(request)
        #test case to make sure only cards in list show set to True to display owned cards
        show_owned = request.GET.get('toggle-ownership-filter') == 'true'  # Will be True if checked, False if not
        card_list = Card.objects.all()
        api_list = API_cards.objects.all()

        combined_list = zip(card_list, api_list)
        

        current_user = request.user
        if show_owned:
            owned_cards = current_user.listPokemon
            card_list = Card.objects.filter(id__in=owned_cards)
            api_list = API_cards.objects.filter(id__in=owned_cards)
        
        my_filter = CardFilter(request.GET, queryset=card_list)
        card_list = my_filter.qs

        context = {"card_list":combined_list, "api_list":api_list, "my_filter":my_filter}

        return render(request, "pokemondb/gallery.html", context)

    
class pokemondb_search_results_view(ListView):
    model = Card
    template_name = 'pokemondb/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = Card.objects.filter(
            Q(name__icontains = query) | Q(card_number__icontains = query) | Q(collection__icontains = query) 
        )
        return object_list

class pokemondb_toggle_card_in_collection(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        button_id = data.get('buttonId')
        print("Button "+str(button_id)+" pressed!")
        # Perform actions based on button_id

        added = False
        if not request.user.remove_pokemon(button_id):  # If we fail to remove the card (user didn't have it yet)
            request.user.add_pokemon(button_id)         # Then add it to the user!
            added = True

        response_data = {
            'message': f'{"Card added to your collection!" if added else "Card removed from your collection."}',
            'success': True
        }
        return JsonResponse(response_data)

    def get(self, request, *args, **kwargs):
        return JsonResponse({'success': False}, status=400)

def filter_cards(request):
    #test case to make sure only cards in list show set to True to display owned cards
    show_owned = False
    card_list = Card.objects.all()
    current_user = request.user
    if show_owned:
        owned_cards = current_user.listPokemon
        card_list = Card.objects.filter(id__in=owned_cards)
    
    my_filter = CardFilter(request.GET, queryset=card_list)
    card_list = my_filter.qs

    context = {"card_list":card_list, "my_filter":my_filter}

    return render(request, "pokemondb/filter.html", context)

def call_fetch_cards(request):
        call_command('fetch_cards')
        return HttpResponse('Custom command has been executed!')