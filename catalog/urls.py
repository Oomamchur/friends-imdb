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
    ActorDeleteView,
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
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
    path(
        "actors/<int:pk>/delete",
        ActorDeleteView.as_view(),
        name="actor-delete"
    ),
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("movies/create/", MovieCreateView.as_view(), name="movie-create"),
    path(
        "movies/<int:pk>/update",
        MovieUpdateView.as_view(),
        name="movie-update"
    ),
    path(
        "movies/<int:pk>/delete",
        MovieDeleteView.as_view(),
        name="movie-delete"
    ),
    # path("users/create/", UserCreateView.as_view(), name="user-create"),
]

app_name = "catalog"
