from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InputForm
from localflavor.us.us_states import US_STATES
from .models import InputAddress, PriceEstimate

def home(request):
	if request.method == 'POST':
		form = InputForm(request.POST)
		if form.is_valid():
			input_address = InputAddress()
			input_address.address = form.cleaned_data.get('address')
			input_address.city = form.cleaned_data.get('city')
			input_address.state = form.cleaned_data.get('state')
			input_address.destination = form.cleaned_data.get('destination')
			input_address.distance = form.cleaned_data.get('distance')

			est_list = input_address.BuildEstimateList()

		context = {
			'estimates': est_list,
			'form': form
		}	

		return render(request, 'UberPriceCheck/homepage.html', context)
	else:
		form = InputForm()
		return render(request, 'UberPriceCheck/homepage.html', {'form': form})
