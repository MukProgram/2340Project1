from django.shortcuts import render
from .models import *

def index(request):
    movies = Movie.objects.all()
    return render(request, "Movies/index.html", {"movies": movies})
