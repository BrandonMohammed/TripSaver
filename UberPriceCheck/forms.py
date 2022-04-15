from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class InputForm(forms.Form):
    destination = forms.CharField()
    distance_in_miles = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '5', 'id':'myDistance'}))