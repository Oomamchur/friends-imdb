from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import Genre, Actor, Movie


class ModelsTests(TestCase):
    def test_genre_str(self) -> None:
        genre = Genre.objects.create(name="test")

        self.assertEquals(str(genre), genre.name)

    def test_actor_str(self) -> None:
        actor = Actor.objects.create(first_name="name", last_name="surname")

        self.assertEquals(str(actor), f"{actor.first_name} {actor.last_name}")

    def test_movie_str(self) -> None:
        movie = Movie.objects.create(
            title="title",
            year=2000,
            description="best movie ever"
        )
        self.assertEquals(str(movie), f"{movie.title} ({movie.year})")

    def test_create_user(self) -> None:
        username = "test"
        password = "password"
        email = "test@gmail.com"
        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            email=email
        )
        self.assertEquals(user.username, username)
        self.assertTrue(user.check_password(password))
        self.assertEquals(user.email, email)
