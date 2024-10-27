from django.views.generic import TemplateView, ListView
from .models import Card

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