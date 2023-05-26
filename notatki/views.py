from django.shortcuts import render
from django.http import HttpResponse
from .models import Notatka

def index(request):
    notatki = Notatka.objects.all()
    return render(request, "index.html", {'notatki': notatki})

def allNotes(request):
    return HttpResponse("eo vieww")