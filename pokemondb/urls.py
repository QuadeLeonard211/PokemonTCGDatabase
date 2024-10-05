from django.urls import path

from . import views

app_name = "pokemondb"
urlpatterns = [
    path('home/', views.pokemondb_homepage, name='Pokemon TCG Homepage')
]