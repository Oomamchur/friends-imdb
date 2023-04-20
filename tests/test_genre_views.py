from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Genre

GENRE_URL = reverse("catalog:genre-list")


class PublicGenreTests(TestCase):
    def setUp(self) -> None:
        self.genre = Genre.objects.create(name="test")

    def test_genre_list(self) -> None:
        response = self.client.get(GENRE_URL)
        genres = Genre.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["genre_list"]), list(genres))
        self.assertTemplateUsed(response, "catalog/genre_list.html")

    def test_genre_detail(self) -> None:
        response = self.client.get(reverse(
            "catalog:genre-detail",
            kwargs={"pk": self.genre.pk}
        ))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/genre_detail.html")
        self.assertContains(response, self.genre.name)

    def test_no_access_to_update_genre_without_login(self) -> None:
        response = self.client.get(reverse(
            "catalog:genre-update",
            kwargs={"pk": self.genre.pk}
        ))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            "/accounts/login/?next=/genres/1/update"
        )


class PrivateGenreTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234"
        )
        self.client.force_login(self.user)
        self.genre = Genre.objects.create(name="test")

    def test_access_to_update_genre_with_login(self) -> None:
        response = self.client.get(reverse(
            "catalog:genre-update",
            kwargs={"pk": self.genre.pk}
        ))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/genre_form.html")

    def test_update_genre(self) -> None:
        new_data = {"name": "Comedy"}
        response = self.client.post(
            reverse("catalog:genre-update", kwargs={"pk": self.genre.pk}),
            new_data
        )
        updated_genre = Genre.objects.get(pk=self.genre.pk)

        self.assertRedirects(response, reverse("catalog:genre-list"))
        self.assertEqual(updated_genre.name, new_data["name"])
