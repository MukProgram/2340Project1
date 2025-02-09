from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    movies = Movie.objects.all()
    template_data = {}
    template_data['title'] = 'GT Movies Store'
    return render(request, "Movies/index.html", {"movies": movies})
def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, "Movies/about.html")
def movies(request):
    movies = Movie.objects.all()
    template_data = {}
    template_data['title'] = 'Movies'
    return render(request, "Movies/movies.html", {"movies": movies})

@login_required
def create_review(request, id):
    if request.method == 'POST' and request.POST['comment']!= '':
        movie = Movie.objects.get(id=id)
        review = Review()
        review.comment = request.POST['comment']
        review.movie = movie
        review.user = request.user
        review.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)
def show(request, id):
    movie = Movie.objects.get(id = id)
    template_data = {}
    reviews = Review.objects.filter(movie = movie)
    template_data['title'] = movie.title
    template_data['image'] = movie.image
    template_data['movie'] = movie
    template_data['reviews'] = reviews
    return render(request, 'movies/show.html',{'template_data': template_data})
