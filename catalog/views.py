from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from catalog.models import Movie, Actor, Genre


def index(request: HttpRequest) -> HttpResponse:
    num_movies = Movie.objects.count()
    num_actors = Actor.objects.count()
    num_genres = Genre.objects.count()
    context = {
        "num_movies": num_movies,
        "num_actors": num_actors,
        "num_genres": num_genres
    }
    return render(request, "catalog/index.html", context=context)

