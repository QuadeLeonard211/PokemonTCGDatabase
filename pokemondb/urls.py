from django.urls import path
from .views import pokemondb_homepage_view, pokemondb_search_results_view, filter_cards


app_name = "pokemondb"
urlpatterns = [
    path('home/', pokemondb_homepage_view.as_view(), name='Pokemon TCG Homepage'),
    path('search/', pokemondb_search_results_view.as_view(), name='search_results'),
    path('filter/', filter_cards, name='filter'),
]