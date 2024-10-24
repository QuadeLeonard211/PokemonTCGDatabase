from django.urls import path
from .views import pokemondb_homepage_view

app_name = "pokemondb"
urlpatterns = [
    path('home/', pokemondb_homepage_view.as_view(), name='Pokemon TCG Homepage')
]