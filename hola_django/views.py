from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola_mundo_django(request):
    return HttpResponse("!Hola Mundo Perros¡")

