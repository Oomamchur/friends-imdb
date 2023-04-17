from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator

from catalog.models import Movie, User


class MovieForm(forms.ModelForm):
    min_year = 1930
    year = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(min_year)]
    )

    class Meta:
        model = Movie
        fields = "__all__"


class ImdbUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email"
        )
