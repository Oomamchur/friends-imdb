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
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name="genres")
    actors = models.ManyToManyField(Actor, related_name="actors")

    class Meta:
        ordering = ("title",)

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"


