from django.db import models
from uber_rides.session import session
from uber_rides.client import UberRidesClient

# Create your models here.

# This is where all the API calls begin
# session = Session(server_token<TOEKEN>)
# client = UberRidesClient(session)

class PriceEstimate(models.Model):
	start_latitude = models.FloatField()
	start_longitude = models.FloatField()
	end_latitute = modeld.FloatField()
	end_longitude = models.FloatField()