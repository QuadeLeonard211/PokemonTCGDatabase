from django.urls import path
from . import views

app_name = "tcg_api"
urlpatterns = [
    path('cards/', views.card_list, name='card_list'),
]