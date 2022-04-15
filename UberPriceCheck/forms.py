from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class InputForm(forms.Form):
    destination = forms.CharField()
    distance = forms.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])