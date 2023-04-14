from django import forms
from django.core.validators import MinValueValidator

from catalog.models import Movie


class MovieForm(forms.ModelForm):
    min_year = 1930
    year = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(min_year)]
    )

    class Meta:
        model = Movie
        fields = "__all__"
