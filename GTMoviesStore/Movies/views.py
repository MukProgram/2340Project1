from django.shortcuts import render
from .models import *

def index(request):
    movies = Movie.objects.all()
    return render(request, "Movies/index.html", {"movies": movies})
def cart(request):
    movies = Movie.objects.all()
    return render(request, "Movies/cart.html", {"movies": movies})
def about(request):
    return render(request, "Movies/about.html")
def movies(request):
    movies = Movie.objects.all();
    return render(request, "Movies/movies.html", {"movies": movies})