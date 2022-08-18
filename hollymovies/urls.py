from django.contrib import admin
from django.urls import path

from viewer.models import Genre, Actor, Movie
from viewer.views import MoviesView, ActorsView, ActorCreateView, MovieDeleteView, MovieUpdateView, MoviCreateView

admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('actors/', ActorsView.as_view(), name="actors"),
    path('actors/create', ActorCreateView.as_view()),

    path('', MoviesView.as_view(), name="index"),
    path('movies/', MoviesView.as_view()),

    path('movie/create', MoviCreateView.as_view(), name = "movie_create"),
    path('movie/update/<pk>', MovieUpdateView.as_view()),
    path('movie/delete/<pk>', MovieDeleteView.as_view()),
]