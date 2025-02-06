from django.shortcuts import render
from .models import *

def index(request):
    template_data = {}
    template_data['title'] = 'GT Movies Store'
    movies = Movie.objects.all()
    return render(request, "Movies/index.html", {"movies": movies})
def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, "Movies/about.html")
def movies(request):
    template_data = {}
    template_data['title'] = 'Movie Library'
    movies = Movie.objects.all()
    return render(request, "Movies/movies.html", {"movies": movies})
def show(request, id):
    movie = movies[id - 1] #EXCEPTION HERE
    template_data = {}
    template_data['title'] = movie['name']
    template_data['movie'] = movie
    return render(request, 'movies/show.html',{'template_data': template_data})