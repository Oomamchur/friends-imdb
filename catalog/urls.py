from django.urls import path
from catalog.views import (
    index,
    GenreListView,
    GenreDetailView,
    GenreUpdateView,
    ActorListView,
    ActorDetailView,
    ActorCreateView,
    ActorUpdateView,
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path(
        "genres/<int:pk>/update",
        GenreUpdateView.as_view(),
        name="genre-update"
    ),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("actors/create/", ActorCreateView.as_view(), name="actor-create"),
    path(
        "actors/<int:pk>/update",
        ActorUpdateView.as_view(),
        name="actor-update"
    ),
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("movies/create/", MovieCreateView.as_view(), name="movie-create"),
    path(
        "movies/<int:pk>/update",
        MovieUpdateView.as_view(),
        name="movie-update"
    ),
]

app_name = "catalog"
