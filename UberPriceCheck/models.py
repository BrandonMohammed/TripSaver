from django.db import models
# from uber_rides.session import session
# from uber_rides.client import UberRidesClient
from geopy.geocoders import Nominatim


# Create your models here.

class PriceEstimate(models.Model):
    display_name = models.CharField(max_length=20)
    distance = models.FloatField()
    high_estimate = models.FloatField()
    low_estimate = models.FloatField()
    estimate = models.CharField(max_length=20)


class InputAddress(models.Model):
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=5)
    distance = models.IntegerField()

    def get_Coordinates(self):
        # TODO: Check for invalid location error check
        locator = Nominatim(user_agent="Uber_Price_Comparison")
        location = locator.geocode(self.address + " " + self.city + " " + self.state + " " + self.zip_code)
        return list([location.latitude, location.longitude])
