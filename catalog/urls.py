from django.urls import path
from catalog.views import (
    index,
    GenreListView,
    ActorListView,
    MovieListView
)

urlpatterns = [
    path("", index, name="index"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("movies/", MovieListView.as_view(), name="movie-list"),
]

app_name = "catalog"
