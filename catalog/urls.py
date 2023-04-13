from django.urls import path
from catalog.views import index, GenreListView

urlpatterns = [
    path("", index, name="index"),
    path("genres/", GenreListView.as_view(), name="genre-list")
]

app_name = "catalog"
