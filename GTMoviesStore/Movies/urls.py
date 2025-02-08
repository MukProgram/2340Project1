from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name = 'about'),
    path('movies', views.movies, name = 'movies'),
    path('<int:id/review/create/', views.create_review, name = 'movies.create_review')
    path('movies/<int:id>/', views.show, name='movies.show'),
]

