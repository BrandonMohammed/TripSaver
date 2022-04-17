from django import forms
from .models import InputAddress
from localflavor.us.us_states import US_STATES


class InputForm(forms.ModelForm):

    class Meta:
        model = InputAddress
        fields = '__all__'

        widgets = {
            'state': forms.Select(choices=US_STATES),
            'distance': forms.NumberInput(attrs={'type': 'range', 'step': '1', 'min': '1', 'max': '5', 'id': 'myDistance'})
        }

        labels = {
            'distance': "Distance you are willing to walk"
        }
