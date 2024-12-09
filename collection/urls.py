from django.urls import path
from .views import collection_view

app_name = "collection"
urlpatterns = [
    path('', collection_view.as_view(), name='homepage'),
]