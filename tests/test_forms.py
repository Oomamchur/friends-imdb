from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.forms import ImdbUserCreationForm, MovieForm
from catalog.models import Genre, Movie


class FormsTest(TestCase):
    def test_user_creation_form(self) -> None:
        form_data = {
            "username": "test",
            "password1": "pass1234Q",
            "password2": "pass1234Q",
            "first_name": "first name",
            "last_name": "last name",
            "email": "admin@admin.com"
        }
        form = ImdbUserCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class PrivateMovieTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234"
        )
        self.client.force_login(self.user)
        self.genre = Genre.objects.create(name='Action')

    def test_movie_creation_form_is_valid(self) -> None:
        form_data = {
            "title": "Title",
            "year": 2000,
            "genres": [self.genre.id]
        }
        form = MovieForm(data=form_data)
        is_valid = form.is_valid()
        self.client.post(reverse("catalog:movie-create"), data=form_data)
        new_movie = Movie.objects.get(title=form_data["title"])

        self.assertTrue(is_valid)
        self.assertEqual(new_movie.title, form_data["title"])

    def test_movie_creation_form_is_not_valid(self) -> None:
        form_data = {
            "title": "Title",
            "year": 1900,
            "genres": [self.genre.id]
        }
        form = MovieForm(data=form_data)

        self.assertFalse(form.is_valid())
