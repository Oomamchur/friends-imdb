from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Movie, Actor, Genre


def index(request: HttpRequest) -> HttpResponse:
    num_movies = Movie.objects.count()
    num_actors = Actor.objects.count()
    num_genres = Genre.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_movies": num_movies,
        "num_actors": num_actors,
        "num_genres": num_genres,
        "num_visits": num_visits + 1,
    }
    return render(request, "catalog/index.html", context=context)


class GenreListView(generic.ListView):
    model = Genre
    template_name = "catalog/genre_list.html"
    context_object_name = "genre_list"
    queryset = Genre.objects.all().order_by("name")


class GenreDetailView(LoginRequiredMixin, generic.DetailView):
    model = Genre


class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Genre
    fields = "__all__"
    template_name = "catalog/genre_form.html"
    success_url = reverse_lazy("catalog:genre-list")


class ActorListView(generic.ListView):
    model = Actor
    template_name = "catalog/actor_list.html"
    context_object_name = "actor_list"
    queryset = Actor.objects.all().order_by("last_name")
    paginate_by = 10


class ActorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Actor


class ActorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Actor
    fields = "__all__"
    success_url = reverse_lazy("catalog:actor-list")


class ActorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Actor
    fields = "__all__"
    success_url = reverse_lazy("catalog:actor-list")


class ActorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Actor
    fields = "__all__"
    template_name = "catalog/actor_confirm_delete.html"
    success_url = reverse_lazy("catalog:actor-list")


class MovieListView(generic.ListView):
    model = Movie
    template_name = "catalog/movie_list.html"
    context_object_name = "movie_list"
    queryset = Movie.objects.all().prefetch_related("genres")
    paginate_by = 10


class MovieDetailView(LoginRequiredMixin, generic.DetailView):
    model = Movie


class MovieCreateView(LoginRequiredMixin, generic.CreateView):
    model = Movie
    fields = "__all__"
    success_url = reverse_lazy("catalog:movie-list")


class MovieUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Movie
    fields = "__all__"
    success_url = reverse_lazy("catalog:movie-list")


class MovieDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Movie
    fields = "__all__"
    template_name = "catalog/movie_confirm_delete.html"
    success_url = reverse_lazy("catalog:movie-list")
