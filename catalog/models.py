from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ("username",)


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("last_name",)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    year = models.IntegerField()
    description = models.TextField(blank=True)
    genres = models.ManyToManyField(Genre, related_name="movies")
    actors = models.ManyToManyField(Actor, blank=True, related_name="movies")

    class Meta:
        ordering = ("year",)

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"


class Rating(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="ratings"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="ratings"
    )
    rating = models.IntegerField()

    class Meta:
        unique_together = ('movie', 'user',)
