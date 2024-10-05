from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pokemondb_homepage(request):
    return render(request, 'pokemondb/homepage.html')