from django.urls import path
from catalog.views import (
    index,
    GenreListView,
    ActorListView,
    MovieListView, GenreDetailView, ActorDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("movies/", MovieListView.as_view(), name="movie-list"),
]

app_name = "catalog"
