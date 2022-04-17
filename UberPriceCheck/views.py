from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InputForm
from localflavor.us.us_states import US_STATES
from .models import InputAddress, PriceEstimate

# from uber_rides.session import Session
# from uber_rides.client import UberRidesClient


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

			for item in est_list:
				print(item.address)
				print(item.distance)
				print(item.estimate)

			# session = Session(server_token<TOKEN>)
			# client = UberRidesClient(session)
			# response = client.get_price_estimates(
			#     start_latitude=?????,
			#     start_longitude=?????,
			#     end_latitude=dest_latitude,
			#     end_longitude=dest_longitude
			# )
			# price_estimate = response.json.get('prices')

			return redirect('UPC-home')
	else:
		form = InputForm()
		return render(request, 'UberPriceCheck/homepage.html', {'form': form})
