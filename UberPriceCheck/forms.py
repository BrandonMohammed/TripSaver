from django import forms
from .models import InputAddress
from localflavor.us.us_states import US_STATES

class InputForm(forms.Form):
    address = forms.CharField(max_length=128)
    city = forms.CharField(max_length=64)
    state = forms.CharField(widget=forms.Select(choices=US_STATES))
    zip_code = forms.CharField(max_length=5)
    distance = forms.IntegerField(label='Distance you are willing to walk', widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '5', 'id':'myDistance'}))
    