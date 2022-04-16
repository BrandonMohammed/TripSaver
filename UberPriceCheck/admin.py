from django.contrib import admin
from .models import PriceEstimate, InputAddress


# Register your models here.
admin.site.register(PriceEstimate)
admin.site.register(InputAddress)