from django import forms
from .models import City

class FavoriteCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'country']