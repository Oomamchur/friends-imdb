from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from catalog.admin import GenreAdmin, ActorAdmin, MovieAdmin, UserAdmin
from catalog.models import Genre, Actor, Movie


class AdminTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.site = AdminSite()
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            email='test@gmail.com',
            password='password'
        )
        self.client.force_login(self.admin_user)

    def test_genre_admin(self) -> None:
        genre_admin = GenreAdmin(Genre, self.site)

        self.assertTrue(genre_admin.search_fields == ['name'])

    def test_actor_admin(self) -> None:
        actor_admin = ActorAdmin(Actor, self.site)
        self.assertTrue(
            actor_admin.search_fields == ['last_name', 'first_name']
        )

    def test_movie_admin(self) -> None:
        movie_admin = MovieAdmin(Movie, self.site)
        self.assertTrue(movie_admin.search_fields == ['title', 'year'])

    def test_user_admin(self) -> None:
        user_admin = UserAdmin(get_user_model(), self.site)
        self.assertTrue(user_admin.search_fields == ['username'])
