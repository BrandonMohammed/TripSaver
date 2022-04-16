from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InputForm
from localflavor.us.us_states import US_STATES
from .models import InputAddress, PriceEstimate
import geocoder
import geopy.distance
from datetime import datetime
import random
from geopy.geocoders import Nominatim


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

            current_location = geocoder.ipinfo('me')
            # Destination
            loc1 = (dest_latitude, dest_longitude)
            # Current location
            loc2 = current_location.latlng

            degrees = input_address.distance * (1 / 69)
            estimate_list = []
            for i in range(5):
                lat = loc2[0]
                lon = loc2[1]
                check_time = datetime.now()
                base_price = 5.0
                surge_price = 1.0
                if 5 > check_time.hour >= 17:
                    surge_price = 2.5
                price_per_miles = random.uniform(1.0, 2.0)
                if i == 0:
                    # add degrees to lat
                    lat += degrees
                if i == 1:
                    # sub degrees from lat
                    lat -= degrees
                if i == 2:
                    # add degrees to long
                    lon += degrees
                if i == 3:
                    # subtract degrees from long
                    lon -= degrees

                temp_loc = (lat, lon)
                travel_distance = geopy.distance.geodesic(loc1, temp_loc).miles
                cost = price_per_miles * travel_distance * surge_price + base_price
                price_est = PriceEstimate()
                price_est.display_name = "UberX"
                price_est.distance = travel_distance
                price_est.estimate = cost

                geolocator = Nominatim(user_agent="Uber_price_check")
                price_est.address = geolocator.reverse(str(lat)+", " + str(lon))
                print(price_est.address)
                estimate_list.append(price_est)

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
