from django.shortcuts import render
from .models import *

def index(request):
    template_data = {}
    template_data['title'] = 'GT Movies Store'
    movies = Movie.objects.all()
    return render(request, "Movies/index.html", {"movies": movies})

def cart(request):
    template_data = {}
    template_data['title'] = 'Shopping Cart'
    movies = Movie.objects.all()
    return render(request, "Movies/cart.html", {"movies": movies})
def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, "Movies/about.html")
def movies(request):
    template_data = {}
    template_data['title'] = 'Movie Library'
    movies = Movie.objects.all()
    return render(request, "Movies/movies.html", {"movies": movies})