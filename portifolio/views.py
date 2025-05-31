from django.shortcuts import render
from .dados import habilidades

# Create your views here.
def home(request):
    return render(request, 'home.htm', {'habilidades':habilidades})    