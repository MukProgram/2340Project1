from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name = 'cart'),
    path('about', views.about, name = 'about'),
    path('movies', views.movies, name = 'movies')
]
