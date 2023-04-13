from django.urls import path
from catalog.views import index, GenreListView, ActorListView

urlpatterns = [
    path("", index, name="index"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
]

app_name = "catalog"
