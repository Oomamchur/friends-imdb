from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator

from catalog.models import Movie, User, Genre, Actor, Rating


class MovieForm(forms.ModelForm):
    min_year = 1930
    year = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(min_year)]
    )
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    actors = forms.ModelMultipleChoiceField(
        queryset=Actor.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Movie
        fields = "__all__"


class MovieSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by title or year"}
        ),
    )


class ImdbUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email"
        )


class ActorSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        ),
    )


class RatingForm(forms.ModelForm):
    rating = forms.IntegerField(
        min_value=1,
        max_value=10,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Write your rating"}
        ),
    )

    class Meta:
        model = Rating
        exclude = ["movie", "user"]
