from django.db import models
# from uber_rides.session import session
# from uber_rides.client import UberRidesClient
from geopy.geocoders import Nominatim
import geopy.distance
import geocoder
from datetime import datetime
import random
import requests


# Create your models here.

class PriceEstimate(models.Model):
	display_name = models.CharField(max_length=20)
	distance = models.FloatField()
	estimate = models.FloatField()
	address = models.CharField(max_length=128)

	def LatLngToAddr(self, lat, lng):
		geolocator = Nominatim(user_agent="Uber_price_check")
		self.address = geolocator.reverse(str(lat)+", " + str(lng))


class InputAddress(models.Model):
	address = models.CharField(max_length=128)
	city = models.CharField(max_length=64)
	state = models.CharField(max_length=20)
	zip_code = models.CharField(max_length=5)
	distance = models.IntegerField()

	def addrToLatLng(self):
		# TODO: Check for invalid location error check
		locator = Nominatim(user_agent="Uber_Price_Comparison")
		location = locator.geocode(self.address + " " + self.city + " " + self.state + " " + self.zip_code)
		if (location):
			return (location.latitude, location.longitude)
		else:
			return None

	def BuildEstimateList(self):
		estimate_list = []
		degrees = self.distance * (1 / 69)

		current_location = geocoder.ipinfo('me').latlng
		print(current_location)
		dest_location = self.addrToLatLng()

		if (not dest_location):
			return estimate_list

		for i in range(5):
				lat = current_location[0]
				lon = current_location[1]
				check_time = datetime.now()
				base_price = 5.0
				surge_price = 1.0
				price_per_miles = random.uniform(1.0, 2.0)

				if 5 > check_time.hour >= 17:
					surge_price = 2.5

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

				travel_distance = geopy.distance.geodesic((lat, lon), dest_location).miles
				cost = price_per_miles * travel_distance * surge_price + base_price
				price_est = PriceEstimate()
				price_est.display_name = "UberX"
				price_est.distance = float("{0:.2f}".format(travel_distance))
				price_est.estimate = float("{0:.2f}".format(cost))

				r = requests.get('https://api.uber.com/v1.2/estimates/price',
								headers = {'Authorization': 'TOK:'},
								params = {'start_latitude': lat, 'end_latitude': lon, 'start_longitude': dest_location[0], 'end_longitude': dest_location[1]})


				price_est.LatLngToAddr(lat, lon)
				estimate_list.append(price_est)

		return estimate_list

