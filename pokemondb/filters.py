import django_filters
from .models import Card
from accounts.models import CustomUser

class CardFilter(django_filters.FilterSet):

    class Meta:
        model = Card
        fields = ["element_type", "collection"]

    