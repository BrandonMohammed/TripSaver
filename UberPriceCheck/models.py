from django.db import models
# from uber_rides.session import session
# from uber_rides.client import UberRidesClient
from geopy.geocoders import Nominatim


# Create your models here.

class PriceEstimate(models.Model):
    display_name = models.CharField()
    distance = models.FloatField()
    high_estimate = models.FloatField()
    low_estimate = models.FloatField()
    estimate = models.CharField()


class InputAddress(models.Model):
    address = models.CharField()
    city = models.CharField()
    state = models.CharField()
    zip_code = models.IntegerField()
    distance = models.IntegerField()

    def get_Coordinates(self):
        locator = Nominatim(user_agent="Uber_Price_Comparison")
        location = locator.geocode(self.address + " " + self.city + " " + self.state + " " + self.zip_code)
        return list([location.latitude, location.longitude])
