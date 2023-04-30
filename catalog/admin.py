from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import Genre, Actor, User, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ["last_name", "first_name"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ["title", "year"]


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ["username"]
