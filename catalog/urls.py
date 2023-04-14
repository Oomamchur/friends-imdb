from django.urls import path
from catalog.views import (
    index,
    GenreListView,
    GenreDetailView,
    GenreUpdateView,
    ActorListView,
    ActorDetailView,
    ActorCreateView,
    MovieListView,
    MovieDetailView,
    MovieCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("genres/<int:pk>/update", GenreUpdateView.as_view(), name="genre-update"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("actors/create/", ActorCreateView.as_view(), name="actor-create"),
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("movies/create/", MovieCreateView.as_view(), name="movie-create"),
]

app_name = "catalog"
