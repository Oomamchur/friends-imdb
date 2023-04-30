from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Movie, Genre

MOVIE_URL = reverse("catalog:movie-list")


class PublicMovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(
            title="title",
            year="2000"
        )

    def test_movie_list(self) -> None:
        response = self.client.get(MOVIE_URL)
        movies = Movie.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["movie_list"]), list(movies))
        self.assertTemplateUsed(response, "catalog/movie_list.html")

    def test_movie_detail(self) -> None:
        response = self.client.get(reverse(
            "catalog:movie-detail",
            kwargs={"pk": self.movie.pk}
        ))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/movie_detail.html")
        self.assertContains(response, self.movie.title)

    def test_no_access_to_create_movie_without_login(self) -> None:
        response = self.client.get(reverse("catalog:movie-create"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            "/accounts/login/?next=/movies/create/"
        )

    def test_no_access_to_update_movie_without_login(self) -> None:
        response = self.client.get(reverse(
            "catalog:movie-update",
            kwargs={"pk": self.movie.pk}
        ))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            "/accounts/login/?next=/movies/1/update"
        )

    def test_movie_list_search(self) -> None:
        response = self.client.get(MOVIE_URL, {"year": "200"})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/movie_list.html")
        self.assertContains(response, "year")


class PrivateMovieTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234"
        )
        self.client.force_login(self.user)
        self.movie = Movie.objects.create(
            title="title",
            year="2000"
        )
        self.genre = Genre.objects.create(name="action")
        self.movie.genres.add(self.genre)

    def test_update_movie(self) -> None:
        response = self.client.get(reverse(
            "catalog:movie-update",
            kwargs={"pk": self.movie.pk}
        ))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/movie_form.html")

    def test_create_movie(self) -> None:
        new_data = {"title": "Avengers",
                    "year": 2020,
                    "genres": [self.genre.id]
                    }
        response = self.client.post(reverse("catalog:movie-create"), new_data)
        movie = Movie.objects.get(title="Avengers")

        self.assertRedirects(response, MOVIE_URL)
        self.assertEqual(movie.title, new_data["title"])
