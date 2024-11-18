from django.urls import path
from . import views

app_name = "tcg_api"
urlpatterns = [
    path('', views.home, name='home'),
]