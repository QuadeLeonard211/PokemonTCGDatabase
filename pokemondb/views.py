from typing import Any
from django.views.generic import TemplateView, ListView
from .models import Card
from django.db.models import Q
from django.shortcuts import render
from .filters import CardFilter

# Create your views here.
class pokemondb_homepage_view(TemplateView):
    template_name = "pokemondb/homepage.html"

    #function to add a 'greeting' that can be used in the HTML template (this will likely be changed later to information that is more useful than a greeting)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['greeting'] = 'Welcome to my homepage!'
        return context
    
class pokemondb_search_results_view(ListView):
    model = Card
    template_name = 'pokemondb/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = Card.objects.filter(
            Q(name__icontains = query) | Q(card_number__icontains = query) | Q(collection__icontains = query) 
        )
        return object_list

def filter_cards(request):
    card_list = Card.objects.all()
    my_filter = CardFilter(request.GET, queryset=card_list)
    card_list = my_filter.qs

    context = {"card_list":card_list, "my_filter":my_filter}

    return render(request, "pokemondb/filter.html", context)
