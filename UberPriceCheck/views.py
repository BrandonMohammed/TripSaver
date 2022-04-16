from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InputForm
from localflavor.us.us_states import US_STATES
from .models import InputAddress
import geocoder
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

            # Convert street address to coordinates for API call
            coordinates = input_address.get_Coordinates()
            dest_latitude = coordinates[0]
            dest_longitude = coordinates[1]

            current_location = geocoder.ip('me')
            print(current_location.latlng)


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
