from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet, Q, Avg
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from catalog.forms import (
    ActorSearchForm,
    MovieForm,
    MovieSearchForm,
    ImdbUserCreationForm,
    RatingForm,
)
from catalog.models import Movie, Actor, Genre, User, Rating


def index(request: HttpRequest) -> HttpResponse:
    num_movies = Movie.objects.count()
    num_actors = Actor.objects.count()
    num_users = User.objects.count()
    last_added = Movie.objects.all().order_by("-id")[:3]
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_movies": num_movies,
        "num_actors": num_actors,
        "num_users": num_users,
        "num_visits": num_visits + 1,
        "last_added": last_added,
    }
    return render(request, "catalog/index.html", context=context)


class GenreListView(generic.ListView):
    model = Genre
    queryset = Genre.objects.prefetch_related("movies")
    template_name = "catalog/genre_list.html"
    context_object_name = "genre_list"


class GenreDetailView(generic.DetailView):
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
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(ActorListView, self).get_context_data(**kwargs)

        context["search_form"] = ActorSearchForm

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Actor.objects.prefetch_related("movies")
        form = ActorSearchForm(self.request.GET)

        if form.is_valid():
            query = Q(last_name__icontains=form.cleaned_data["last_name"]) | Q(
                first_name__icontains=form.cleaned_data["last_name"]
            )
            return queryset.filter(query)
        return queryset


class ActorDetailView(generic.DetailView):
    model = Actor


class ActorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Actor
    fields = "__all__"
    success_url = reverse_lazy("catalog:actor-list")


class ActorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Actor
    fields = "__all__"

    def get_success_url(self) -> HttpResponse:
        return reverse("catalog:actor-detail", args=[self.object.pk])


class ActorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Actor
    fields = "__all__"
    template_name = "catalog/actor_confirm_delete.html"
    success_url = reverse_lazy("catalog:actor-list")


class MovieListView(generic.ListView):
    model = Movie
    template_name = "catalog/movie_list.html"
    context_object_name = "movie_list"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(MovieListView, self).get_context_data(**kwargs)

        context["search_form"] = MovieSearchForm

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Movie.objects.prefetch_related("genres")
        form = MovieSearchForm(self.request.GET)

        if form.is_valid():
            query = Q(title__icontains=form.cleaned_data["title"]) | Q(
                year__icontains=form.cleaned_data["title"]
            )
            return queryset.filter(query)
        return queryset


class MovieDetailView(generic.DetailView):
    model = Movie

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["genre_list"] = self.object.genres.all()
        context["form"] = RatingForm()
        avg_rating = self.object.ratings.aggregate(Avg("rating"))
        if avg_rating["rating__avg"]:
            context["avg_rating"] = round(avg_rating["rating__avg"], 1)
        if self.request.user.is_authenticated:
            user = get_user(self.request)
            rating = Rating.objects.filter(user=user, movie=self.object).first()
            rate = rating.rating if rating else None
            context["rating"] = rate
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = RatingForm(request.POST)
        if form.is_valid():
            movie = Movie.objects.get(pk=kwargs.get("pk"))
            rating, created = Rating.objects.get_or_create(
                movie=movie, user=request.user
            )
            if created or "rating" in form.changed_data:
                rating.rating = form.cleaned_data["rating"]
                rating.save()
            return HttpResponseRedirect(
                reverse("catalog:movie-detail", args=[kwargs.get("pk")])
            )


class MovieCreateView(LoginRequiredMixin, generic.CreateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy("catalog:movie-list")


class MovieUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Movie
    form_class = MovieForm

    def get_success_url(self) -> HttpResponse:
        return reverse("catalog:movie-detail", args=[self.object.pk])


class MovieDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Movie
    fields = "__all__"
    template_name = "catalog/movie_confirm_delete.html"
    success_url = reverse_lazy("catalog:movie-list")


class UserCreateView(generic.CreateView):
    model = User
    form_class = ImdbUserCreationForm
    success_url = reverse_lazy("login")
