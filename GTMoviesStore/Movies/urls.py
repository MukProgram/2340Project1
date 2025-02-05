from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name = 'about'),
    path('movies', views.movies, name = 'movies'),
    path('movies/<int:id>/', views.show, name='movies.show'),
]

