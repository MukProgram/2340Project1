from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    movies = Movie.objects.all()
    template_data = {}
    template_data['title'] = 'GT Movies Store'
    return render(request, "Movies/index.html",  {'template_data': template_data})

def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, "Movies/about.html", {'template_data': template_data})
def movies(request):
    template_data = {}
    template_data['title'] = 'Movies'
    if request.method == 'POST' and request.POST['search'] != '':
        template_data['movies'] = Movie.objects.filter(title__icontains=request.POST['search'])
    else:
        template_data['movies'] = Movie.objects.all()
    return render(request, "Movies/movies.html", {'template_data': template_data})

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
    #template_data['description'] = movie.description
    template_data['image'] = movie.image
    template_data['movie'] = movie
    template_data['reviews'] = reviews
    return render(request, 'movies/show.html',{'template_data': template_data})

@login_required
def edit_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user:
        return redirect('movies.show',id=id)
    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit Review'
        template_data['review'] = review
        return render(request, 'movies/edit_review.html', {'template_data':template_data})
    elif request.method == 'POST' and request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('movies.show',id=id)
    else:
        return redirect('movies.show',id=id)

@login_required
def delete_review(request,id,review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    return redirect('movies.show',id=id)