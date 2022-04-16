from django.db import models
from uber_rides.session import session
from uber_rides.client import UberRidesClient

# Create your models here.

# This is where all the API calls begin
# session = Session(server_token<TOEKEN>)
# client = UberRidesClient(session)

class PriceEstimate(models.Model):
	display_name = models.CharField()
	distance = models.FloatFied()
	high_estimate = models.FloatField()
	low_estimate = models.FloatField()
	estimate = modeld.CharField()