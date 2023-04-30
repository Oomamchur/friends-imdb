# Generated by Django 4.2 on 2023-04-17 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_alter_movie_actors_alter_movie_genres"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="movie",
            options={"ordering": ("year",)},
        ),
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="catalog.actor"
            ),
        ),
    ]
