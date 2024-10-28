import django_filters
from django_filters import CharFilter
from .models import Card

class CardFilter(django_filters.FilterSet):

    class Meta:
        model = Card
        fields = ["element_type"]