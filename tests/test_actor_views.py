from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Actor

ACTOR_URL = reverse("catalog:actor-list")


class PublicActorTests(TestCase):
    def setUp(self) -> None:
        self.actor = Actor.objects.create(
            first_name="name",
            last_name="surname"
        )

    def test_actor_list(self) -> None:
        response = self.client.get(ACTOR_URL)
        actors = Actor.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["actor_list"]), list(actors))
        self.assertTemplateUsed(response, "catalog/actor_list.html")

    def test_actor_detail(self) -> None:
        response = self.client.get(reverse(
            "catalog:actor-detail",
            kwargs={"pk": self.actor.pk}
        ))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/actor_detail.html")
        self.assertContains(response, self.actor.last_name)

    def test_no_access_to_create_actor_without_login(self) -> None:
        response = self.client.get(reverse("catalog:actor-create"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            "/accounts/login/?next=/actors/create/"
        )

    def test_no_access_to_update_actor_without_login(self) -> None:
        response = self.client.get(reverse(
            "catalog:actor-update",
            kwargs={"pk": self.actor.pk}
        ))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            "/accounts/login/?next=/actors/1/update"
        )

    def test_actor_list_search(self) -> None:
        response = self.client.get(ACTOR_URL, {"name": "sur"})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/actor_list.html")
        self.assertContains(response, "name")


class PrivateActorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234"
        )
        self.client.force_login(self.user)
        self.actor = Actor.objects.create(
            first_name="name",
            last_name="surname"
        )

    def test_update_actor(self) -> None:
        response = self.client.get(reverse(
            "catalog:actor-update",
            kwargs={"pk": self.actor.pk}
        ))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/actor_form.html")

    def test_create_actor(self) -> None:
        new_data = {"first_name": "Bill", "last_name": "Murray"}
        response = self.client.post(reverse("catalog:actor-create"), new_data)
        actor = Actor.objects.get(last_name=new_data["last_name"])

        self.assertRedirects(response, ACTOR_URL)
        self.assertEqual(actor.last_name, new_data["last_name"])
